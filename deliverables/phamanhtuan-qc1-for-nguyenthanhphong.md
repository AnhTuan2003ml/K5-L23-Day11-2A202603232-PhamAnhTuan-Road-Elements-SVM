# Phiếu QC 1 — Road v1.0

Lô được kiểm: Nguyễn Thanh Phong. Người yêu cầu kiểm: Phạm Anh Tuấn. Ngày kiểm: 2026-11-21. Revision theo manifest: 1.

Phạm vi: lint tự động toàn bộ 20 ảnh; kiểm tra trực quan tập trung A05 và A10 là hai ảnh lint gắn cờ. Đây là QC hỗ trợ bằng checker, chưa phải chứng nhận QC độc lập của học viên.

## Tổng hợp theo mã

| Mã | Mục được kiểm | Phát hiện | Mức |
| --- | --- | ---: | --- |
| QC1-01 | Camera tag | 0 | Nặng |
| QC1-02 | L1/R1 | 2 thiếu position ở A05 | Nặng |
| QC1-03 | Position | 0 | Nặng |
| QC1-04 | Tâm vạch, chiều, điểm dừng | 0 | Chính |
| QC1-05 | Vạch đứt, che | 0 | Chính |
| QC1-06 | Style, color, kind | 0 | Chính |
| QC1-07 | Vùng lái | 0 | Chính |
| QC1-08 | Đèn | 0 | Nặng/chính |
| QC1-09 | Facing, type, group, biển phụ | 0 | Chính |
| QC1-10 | Box nhỏ hơn 8 px | 1 ở A10 | Nhẹ |
| QC1-11 | Fisheye | 0 | Chính |
| QC1-12 | Định dạng file | 0 | Nhẹ/nặng |

## Danh sách phát hiện

| # | Mã | Ảnh | Nhãn | Mức | Nhận xét |
| --- | --- | --- | --- | --- | --- |
| 1 | QC1-02 | A05_b2576c8c-2de20b8a.jpg | lane | Nặng theo lint | Không có position L1/R1. Quan sát ảnh thấy đường phố có xe đỗ hai bên và không thấy rõ vạch sơn làn. Chưa kết luận bỏ sót; cần coach xác nhận ngoại lệ trước Release. |
| 2 | QC1-10 | A10_b6ff1331-f6d3fba8.jpg | traffic_sign | Nhẹ | Một box cao khoảng 7.2 px, dưới ngưỡng gợi ý 8 px. Lint ghi đây không phải lỗi bắt buộc; cần xem ở mức zoom gốc để xác nhận phạm vi box. |

## Quyết định

Lỗi nặng theo lint: 2 cảnh báo QC1-02; lỗi chính: 0; lỗi nhẹ: 1. Đề xuất: **Hold chờ coach xác nhận A05**. Không yêu cầu thêm lane nếu ảnh không có vạch nhìn thấy. Mục QC1-10 là khuyến nghị rà box, không phải căn cứ độc lập để trả Rework.

## Cơ sở và giới hạn

Tôi chạy `road_check lint` trên `nguyenthanhphong-front.zip` và `nguyenthanhphong-fisheye.zip`: 20 ảnh, 3 cảnh báo (2 nặng, 0 chính, 1 nhẹ). Hai ZIP mở được, không kèm ảnh, mỗi ảnh có đủ tag theo manifest. Lint không so ground truth; tôi chưa xác nhận precision, recall, IoU hay độ chính xác tổng thể. Bản đầy đủ của log ở `../out/day11_qc_nguyenthanhphong_20261121/lint.txt`.
