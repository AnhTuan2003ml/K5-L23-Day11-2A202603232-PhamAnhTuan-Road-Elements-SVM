# Báo cáo kết quả — Road Elements & SVM, Ngày 11

Học viên: Phạm Anh Tuấn — Mã học viên: 2A202603232.

Tôi tự gán nhãn trên máy khác rồi tải hai file CVAT XML lên task 33 và 34. Tôi export lại trực tiếp từ CVAT sau lần nhập để kiểm tra đúng dữ liệu đang lưu trên máy chủ. Lần export này được thực hiện ngày 21/11/2026.

## 1. Nguồn và phạm vi

Task 33 là front, 16 ảnh; task 34 là fisheye, 12 ảnh. Hai task có tổng cộng 28 ảnh, 194 shape và 112 tag. Snapshot API ghi 145 shape/64 tag ở front và 49 shape/48 tag ở fisheye. XML export lần lượt có 209 và 97 phần tử annotation nếu tính cả tag; số shape không bao gồm tag.

Project metadata trong XML nguồn có tên project/người sở hữu khác. Thông tin đó chỉ mô tả project xuất file, không xác định ai đã tạo annotation. Tôi xác nhận annotation là do tôi tự gán trước khi tải lên.

## 2. Thống kê theo lớp

| Task | Ảnh | lane | road_curb | crosswalk | drivable | traffic_light | traffic_sign | Shape | Tag |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Front, task 33 | 16 | 46 | 12 | 6 | 32 | 22 | 27 | 145 | 64 |
| Fisheye, task 34 | 12 | 8 | 13 | 13 | 12 | 2 | 1 | 49 | 48 |
| Tổng | 28 | 54 | 25 | 19 | 44 | 24 | 28 | 194 | 112 |

Mỗi ảnh có bốn tag camera, timeofday, weather và source. Tôi giữ riêng hai nhóm ảnh front/fisheye như hai task hiện có trên CVAT.

## 3. Kết quả lint trên export mới

Tôi chạy `road_check lint` trực tiếp trên hai ZIP vừa export. Kết quả: **28 ảnh, 31 cảnh báo** gồm 9 nặng, 17 chính và 5 nhẹ. Toàn bộ đầu ra được lưu tại `out/cvat_export_20261121T1018/lint-revision4.txt`.

| Ảnh | Nội dung lint cần rà |
| --- | --- |
| A02, A03, A14 | Hướng polyline lane |
| A04, A08, A09, A10, A11, A14, A16, B07 | Nhiều polyline trùng position; kiểm tra vạch đứt hoặc gán trùng |
| A05, A06, A07, A09, A14 | Thiếu position L1/R1 theo luật lint |
| A15 | Box biển thấp hơn 8 px; mức nhẹ |
| B02, B04 | Gợi ý edge_zone cho đèn/biển |
| B03, B04, B10, B11 | Camera tag khác gợi ý suy ra từ tên file |
| B07, B08 | Lane camera bên hông cần position=other |

Đây là cảnh báo tự kiểm để chỉ vị trí cần xem lại, không phải kết luận coach xác nhận annotation sai. Tôi chưa so với ground truth nên không báo precision, recall, IoU hoặc điểm chất lượng.

## 4. File export và tính toàn vẹn

| Task | File export | Ảnh | Shape | Tag | SHA-256 |
| --- | --- | ---: | ---: | ---: | --- |
| 33 | phamanhtuan-front.zip | 16 | 145 | 64 | fd4c6818c39b6d8d8f8b820fd4afd4ad9362a63cfdb7dc360db59760d8ac7c39 |
| 34 | phamanhtuan-fisheye.zip | 12 | 49 | 48 | d4b507fb146c982ef63e1242a470870a83afbe8fd72ce8790fcbe9235a24a40 |

Cả hai ZIP được export từ CVAT theo định dạng CVAT for images 1.1, không kèm ảnh. XML mở được và tên ảnh tương ứng với hai nhóm task.

## 5. QC và trạng thái

Tôi đã kiểm tra số lượng, schema file và chạy lint. Tôi chưa có QC chéo từ học viên khác, miễn trừ của coach hoặc ground truth độc lập. Vì vậy trạng thái hiện tại là **đã nhập và kiểm tra cấu trúc; còn các mục lint cần rà; chưa có xác nhận Release**. Lint không tự chấm độ chính xác thị giác.

## 6. Tự đánh giá

Tôi xem các cảnh báo position thiếu, hướng polyline, position trùng và camera tag là những mục cần mở ảnh kiểm trực tiếp. Một cảnh báo có thể là gợi ý cần xem xét thay vì lỗi thực tế, ví dụ một vị trí lane không có vạch nhìn thấy. Tôi không sửa annotation chỉ để làm cho lint hết cảnh báo nếu ảnh không hỗ trợ quyết định đó.

Các kiểm thử checker trước đây chạy trên fixture tổng hợp chỉ xác nhận công cụ hoạt động; chúng không phải điểm annotation của tôi. Trong lần chạy này, kết quả được báo cáo là lint của hai bản export mới.

## 7. Kết luận

Tôi xác nhận hai task đang chứa annotation do tôi tự gán trên máy khác và tải lên. Export mới phản ánh 194 shape, 112 tag trên 28 ảnh. Lint phát hiện 31 cảnh báo cần rà; chưa có ground truth hay QC chéo để định lượng chất lượng. Hai ZIP, checksum và đầu ra lint được lưu trong `out/cvat_export_20261121T1018/`.
