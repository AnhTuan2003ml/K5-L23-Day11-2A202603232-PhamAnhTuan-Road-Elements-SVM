import argparse
import json
import math
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter
from pathlib import Path

from .cvat_xml import Image, Shape, Tag, to_xml
from .taxonomy import raw_labels


def convert_snapshot(snapshot):
    if snapshot['annotations'].get('tracks'):
        raise ValueError('Video tracks cannot be exported as image annotations')
    definitions = {label['id']: label for label in snapshot['labels']}
    start = int(snapshot['meta'].get('start_frame', 0))
    images = [Image(frame['name'], int(frame['width']), int(frame['height'])) for frame in snapshot['meta']['frames']]
    seen = set()
    removed = Counter()
    for group in ('shapes', 'tags'):
        for record in snapshot['annotations'].get(group, []):
            frame = record.get('frame')
            if type(frame) is not int or not start <= frame < start + len(images):
                raise ValueError('Annotation frame does not exist in snapshot metadata')
            if record.get('label_id') not in definitions:
                raise ValueError('Unknown CVAT label ID')
            definition = definitions[record['label_id']]
            attribute_names = {entry['id']: entry['name'] for entry in definition.get('attributes', [])}
            attributes = {}
            for attribute in record.get('attributes', []):
                if attribute['spec_id'] not in attribute_names:
                    raise ValueError('Unknown CVAT attribute ID')
                attributes[attribute_names[attribute['spec_id']]] = str(attribute['value'])
            image = images[frame - start]
            source = record.get('source', 'manual')
            if group == 'tags':
                key = (group, frame, definition['name'], tuple(sorted(attributes.items())))
                item = Tag(definition['name'], attributes)
            else:
                kind = record.get('type')
                if kind not in {'rectangle', 'polyline', 'polygon'}:
                    raise ValueError('Unsupported annotation shape')
                flat = record.get('points', [])
                if len(flat) % 2 or len(flat) < (6 if kind == 'polygon' else 4) or kind == 'rectangle' and len(flat) != 4:
                    raise ValueError('Invalid annotation coordinates')
                if any(isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) for value in flat):
                    raise ValueError('Coordinates must be finite numbers')
                points = list(zip(flat[::2], flat[1::2]))
                key = (group, frame, definition['name'], kind, tuple(flat), bool(record.get('occluded')), tuple(sorted(attributes.items())))
                item = Shape(definition['name'], kind, points, attributes, bool(record.get('occluded')), len(image.shapes))
            if key in seen:
                removed[group] += 1
                continue
            seen.add(key)
            item.source = source
            (image.tags if group == 'tags' else image.shapes).append(item)
    summary = {'task_id': snapshot['task']['id'], 'task_status': snapshot['task'].get('status'), 'images': len(images), 'shapes_before': len(snapshot['annotations'].get('shapes', [])), 'shapes_after': sum(len(image.shapes) for image in images), 'duplicates_removed': dict(removed), 'per_image': [{'name': image.name, 'shapes': dict(Counter(shape.label for shape in image.shapes)), 'tags': {tag.label: tag.attributes for tag in image.tags}} for image in images], 'human_review_completed': False}
    return images, summary


def export_xml(images):
    root = ET.fromstring(to_xml(images))
    meta = ET.Element('meta')
    task = ET.SubElement(meta, 'task')
    ET.SubElement(task, 'name').text = 'Road v1.0 local exercise draft'
    ET.SubElement(task, 'size').text = str(len(images))
    ET.SubElement(task, 'mode').text = 'annotation'
    labels = ET.SubElement(task, 'labels')
    for definition in raw_labels():
        label = ET.SubElement(labels, 'label')
        for field in ('name', 'color', 'type'):
            ET.SubElement(label, field).text = definition.get(field, '')
        attributes = ET.SubElement(label, 'attributes')
        for spec in definition.get('attributes', []):
            entry = ET.SubElement(attributes, 'attribute')
            for field in ('name', 'mutable', 'input_type', 'default_value'):
                value = spec.get(field, '')
                ET.SubElement(entry, field).text = str(value).lower() if isinstance(value, bool) else str(value)
            ET.SubElement(entry, 'values').text = '\n'.join(spec.get('values', []))
    root.insert(1, meta)
    for element, image in zip(root.findall('image'), images):
        for child, item in zip(element, image.shapes + image.tags):
            child.set('source', getattr(item, 'source', 'manual'))
    ET.indent(root)
    return ET.tostring(root, encoding='utf-8', xml_declaration=True)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--front-snapshot', type=Path, required=True)
    parser.add_argument('--fisheye-snapshot', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--name', required=True)
    args = parser.parse_args(argv)
    if not args.name.isalnum() or not args.name.isascii():
        raise ValueError('Submission name must contain only ASCII letters and digits')
    targets = [args.out / (args.name + '-' + kind + '.zip') for kind in ('front', 'fisheye')]
    summary_path = args.out / 'conversion-summary.json'
    if any(path.exists() for path in targets + [summary_path]):
        raise FileExistsError('Refusing to overwrite existing exercise artifacts')
    outputs = [convert_snapshot(json.loads(path.read_text(encoding='utf-8'))) for path in (args.front_snapshot, args.fisheye_snapshot)]
    args.out.mkdir(parents=True, exist_ok=True)
    for target, (images, _) in zip(targets, outputs):
        with zipfile.ZipFile(target, 'x', zipfile.ZIP_DEFLATED) as archive:
            archive.writestr('annotations.xml', export_xml(images))
    summary_path.write_text(json.dumps({'front': outputs[0][1], 'fisheye': outputs[1][1]}, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({key: {'images': summary['images'], 'shapes': summary['shapes_after'], 'duplicates_removed': summary['duplicates_removed']} for key, (_, summary) in zip(('front', 'fisheye'), outputs)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
