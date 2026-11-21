import copy
import xml.etree.ElementTree as ET

import pytest

from road_lab.prepare_submission import convert_snapshot, export_xml


def fixture():
    return {'task': {'id': 33, 'status': 'annotation'}, 'meta': {'start_frame': 0, 'frames': [{'name': 'A01_test.jpg', 'width': 100, 'height': 80}]}, 'labels': [{'id': 1, 'name': 'lane', 'attributes': [{'id': 9, 'name': 'position'}]}, {'id': 2, 'name': 'camera', 'attributes': [{'id': 10, 'name': 'value'}]}], 'annotations': {'shapes': [{'id': 1, 'label_id': 1, 'type': 'polyline', 'frame': 0, 'points': [10, 70, 30, 20], 'occluded': True, 'source': 'auto', 'attributes': [{'spec_id': 9, 'value': 'L1'}]}], 'tags': [{'id': 2, 'label_id': 2, 'frame': 0, 'source': 'manual', 'attributes': [{'spec_id': 10, 'value': 'front'}]}], 'tracks': []}}


def test_snapshot_mapping_preserves_names_attributes_occlusion_and_source():
    snapshot = fixture()
    original = copy.deepcopy(snapshot)
    images, summary = convert_snapshot(snapshot)
    assert images[0].name == 'A01_test.jpg'
    assert images[0].shapes[0].attributes == {'position': 'L1'}
    assert images[0].shapes[0].occluded
    assert images[0].tag_value('camera') == 'front'
    root = ET.fromstring(export_xml(images))
    assert root.find('image/polyline').get('source') == 'auto'
    assert root.find('image/tag').get('source') == 'manual'
    assert root.find('meta/task/labels') is not None
    assert summary['human_review_completed'] is False
    assert snapshot == original


def test_only_exact_duplicates_are_removed():
    snapshot = fixture()
    duplicate = dict(snapshot['annotations']['shapes'][0], id=99)
    snapshot['annotations']['shapes'].append(duplicate)
    snapshot['annotations']['shapes'].append(dict(duplicate, points=[11, 70, 30, 20]))
    images, summary = convert_snapshot(snapshot)
    assert len(images[0].shapes) == 2
    assert summary['duplicates_removed']['shapes'] == 1


@pytest.mark.parametrize('field,value', [('label_id', 999), ('frame', 10), ('frame', True), ('points', [0, 0, float('nan'), 2])])
def test_invalid_records_cannot_be_exported(field, value):
    snapshot = fixture()
    snapshot['annotations']['shapes'][0][field] = value
    with pytest.raises(ValueError):
        convert_snapshot(snapshot)


def test_tracks_are_rejected():
    snapshot = fixture()
    snapshot['annotations']['tracks'] = [{'id': 1}]
    with pytest.raises(ValueError):
        convert_snapshot(snapshot)
