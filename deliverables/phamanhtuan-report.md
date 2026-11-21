# Báo cáo cá nhân — Ngày 11

Họ tên: Phạm Anh Tuấn. Mã học viên: 2A202603232.

Phiên bản CVAT: 2.82.1. Guideline: Road v1.0. Revision: 4. Thời điểm export: xem `export-receipt.json`.

## 1. Kiểm project

| Mục | Kết quả | Ghi chú |
| --- | --- | --- |
| 6 label và kiểu | Đối chiếu đúng schema Road v1.0 | lane, road_curb, crosswalk, drivable, traffic_light, traffic_sign |
| Thuộc tính | Có trong export theo schema task | Lint không đánh giá độ chính xác thị giác |
| 4 tag ảnh | Đủ 4 tag trên 28 ảnh | camera, timeofday, weather, source |

Tôi tự gán nhãn trên máy khác và nhập vào CVAT task front và fisheye. Tôi export lại trực tiếp từ task 33/34 để lập báo cáo này.

## 2. Số lượng đã gán

| Task | Ảnh | lane | road_curb | crosswalk | drivable | traffic_light | traffic_sign |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| front | 16 | 46 | 12 | 6 | 32 | 22 | 27 |
| fisheye | 12 | 8 | 13 | 13 | 12 | 2 | 1 |

Tổng: 28 ảnh, 194 shape và 112 tag.

## 3. Bảng ca khó và cảnh báo

Lint trên hai ZIP mới ghi nhận 31 cảnh báo: 9 nặng, 17 chính, 5 nhẹ. Ảnh cần rà gồm A02, A03, A04, A05, A06, A07, A08, A09, A10, A11, A14, A15, A16, B02, B03, B04, B07, B08, B10 và B11. Chi tiết theo mã QC nằm trong `../out/cvat_export_20261121T1018/lint-revision4.txt`.

Các nhóm cảnh báo chính: hướng polyline; thiếu hoặc trùng position lane; kích thước box biển; edge_zone; camera tag; và position=other cho camera bên hông. Đây là gợi ý tự kiểm, không phải kết luận của coach.

## 4. Phiếu QC 1 nhận được

Tôi chưa nhận được bài của học viên được ghép hoặc phiếu QC trả về. Vì vậy chưa có số lỗi, quyết định hay xác nhận Release. File chờ dữ liệu được đặt tên `phamanhtuan-qc1-for-peer-pending.md`; file này chưa thay thế phiếu QC chéo đã hoàn thành.

## 5. Kiểm file export

| File | Mở lại được | Ảnh | Shape | Tag camera |
| --- | --- | ---: | ---: | --- |
| phamanhtuan-front.zip | Có | 16 | 145 | Có |
| phamanhtuan-fisheye.zip | Có | 12 | 49 | Có |

Hai ZIP là CVAT for images 1.1, không kèm ảnh. SHA-256 và số byte được ghi trong `phamanhtuan-manifest.json` và `export-receipt.json`. Lint tạo manifest revision 4; còn 31 cảnh báo.

## 6. Ảnh chụp màn hình và XML

Ảnh chụp task sau nhập được giữ trong thư mục cục bộ `out/d11_submission_20261121/candidate/assets/`. Một đoạn XML lane có trong `phamanhtuan-front.zip`. Ảnh dữ liệu không được đưa vào gói bàn giao.

## 7. Tự đánh giá

Tôi cần rà các lane trùng position, hướng polyline và camera tag mà lint nêu. Tôi chưa so với ground truth, chưa có QC chéo và không tuyên bố precision, recall, IoU hoặc điểm accuracy. Selftest checker dùng dữ liệu tổng hợp, không phải điểm bài làm.

## 8. Hoạt động row-anchor (tùy chọn)

Tôi chưa đối chiếu polyline với bài của học viên được ghép nên không có số chênh lệch hai bên. Phân tích độc lập row-anchor trước đây nằm trong hồ sơ truy vết cục bộ, không tính là QC chéo.

## Kết luận

Bản revision 4 phản ánh dữ liệu hiện có trên task 33/34: 194 shape và 112 tag. Lint có 31 cảnh báo cần rà; chưa có xác nhận coach hoặc QC chéo nên trạng thái chưa Release.
