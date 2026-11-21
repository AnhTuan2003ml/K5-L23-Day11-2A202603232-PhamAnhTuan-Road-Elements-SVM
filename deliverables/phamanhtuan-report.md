# Báo cáo cá nhân — Ngày 11 · Road Elements & SVM

Họ tên: Phạm Anh Tuấn — Mã học viên: 2A202603232
CVAT: 2.82.1. Guideline: Road v1.0. Revision dự kiến: 1.
Thời điểm đóng gói cục bộ: 2026-11-21T01:57:16.066515+00:00. Đã đồng bộ bản ứng viên vào task 33/34 sau khi được người dùng duyệt; chưa nộp cho coach, chưa có lần Rework chính thức.

**Trạng thái: bản ứng viên có AI hỗ trợ, chưa đủ điều kiện Release.** Còn 7 cảnh báo QC1-02 chưa có miễn trừ của coach. Chưa có bài của bạn được ghép để thực hiện QC chéo. Không dùng nhãn chuẩn của coach; không coi kết quả tự kiểm tổng hợp là điểm bài thực tế.

## 1. Kiểm project

| Mục | Kết quả | Ghi chú |
| --- | --- | --- |
| 6 label, đúng kiểu | Đã đối chiếu taxonomy Road v1.0 | L1/R1 thuộc lane trong bài lab này |
| Thuộc tính và giá trị | File xuất có schema Road v1.0; lint không báo thiếu thuộc tính | Giá trị do AI hỗ trợ rà ảnh, chưa được xác nhận bởi người kiểm độc lập |
| 4 tag ảnh | Đủ 112 tag / 28 ảnh | Camera theo hậu tố FV/RV/MVL/MVR; thời gian và thời tiết đối chiếu ảnh |
| Chia task | Chưa đúng cấu trúc 4 task | CVAT hiện có front 16 ảnh và fisheye 12 ảnh; bảng dưới tách core/extra theo slot |
| Job completed | Chưa | Không tự đánh dấu hoàn thành khi QC chưa kết thúc |

Kết thúc polyline trong CVAT: đóng công cụ vẽ bằng phím hoàn tất hiển thị trên giao diện (thường nhấn N hoặc double-click); cần kiểm lại trên phiên bản 2.82.1. Tag ảnh dùng label kiểu Tag, một thuộc tính select tên value. Hai ZIP trong deliverables được xuất trực tiếp từ CVAT bằng API dataset/export, định dạng CVAT for images 1.1, save_images=false. Đã đọc lại ZIP và đối chiếu toàn bộ hình học/thuộc tính/tag với bản ứng viên đã nhập; không chỉ so số lượng.

## 2. Số lượng đã gán trong bản ứng viên

| Task | Ảnh | lane | road_curb | crosswalk | drivable | traffic_light | traffic_sign |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| front | 12 | 30 | 14 | 5 | 21 | 42 | 40 |
| front-extra | 4 | 10 | 1 | 3 | 7 | 17 | 20 |
| fisheye | 8 | 2 | 2 | 4 | 3 | 2 | 0 |
| fisheye-extra | 4 | 0 | 0 | 4 | 1 | 0 | 0 |

Đây là số lượng hình, không phải số lượng nhãn đã được coach xác nhận đúng. B11 chỉ có tag: không biến các vạch ô đỗ thành lane. B06/B08 không thêm lane khi chỉ thấy vạch ngựa vằn. Các vùng fisheye theo đường cong trên ảnh gốc, chưa có chứng cứ sai số ≤5 px so với GT.

## 3. Bảng ca khó

| Ảnh | Nhãn | Phân vân giữa | Đã chọn | Lý do |
| --- | --- | --- | --- | --- |
| A05 | lane / lane | Không thấy vạch hay bị mô hình bỏ sót | Chưa tự miễn QC1-02 | chưa có L1 (bỏ qua nếu thật sự không thấy vạch); cần coach kiểm ảnh |
| A05 | lane / lane | Không thấy vạch hay bị mô hình bỏ sót | Chưa tự miễn QC1-02 | chưa có R1 (bỏ qua nếu thật sự không thấy vạch); cần coach kiểm ảnh |
| A06 | lane / lane | Không thấy vạch hay bị mô hình bỏ sót | Chưa tự miễn QC1-02 | chưa có R1 (bỏ qua nếu thật sự không thấy vạch); cần coach kiểm ảnh |
| A07 | lane / lane | Không thấy vạch hay bị mô hình bỏ sót | Chưa tự miễn QC1-02 | chưa có L1 (bỏ qua nếu thật sự không thấy vạch); cần coach kiểm ảnh |
| A10 | lane / lane | Không thấy vạch hay bị mô hình bỏ sót | Chưa tự miễn QC1-02 | chưa có R1 (bỏ qua nếu thật sự không thấy vạch); cần coach kiểm ảnh |
| A12 | lane / lane | Không thấy vạch hay bị mô hình bỏ sót | Chưa tự miễn QC1-02 | chưa có R1 (bỏ qua nếu thật sự không thấy vạch); cần coach kiểm ảnh |
| A14 | lane / lane | Không thấy vạch hay bị mô hình bỏ sót | Chưa tự miễn QC1-02 | chưa có R1 (bỏ qua nếu thật sự không thấy vạch); cần coach kiểm ảnh |
| A03 | lane | Đoạn khuất / điểm dừng thật | Chờ kiểm riêng occluded | Không chứng nhận độ chính xác từ kiểm tra định dạng |
| A08/A15 | traffic_sign | Một box nhiều tấm / biển phụ riêng | Cần rà box ghép | Tách đúng từng tấm theo Road v1.0 trước khi nộp |
| A07/A10/A13 | weather | Overcast / rain | rain | Mặt đường ướt rõ; không chỉ dựa độ sáng |
| A11/A14 | timeofday | day / dusk / night | dusk / night | Đối chiếu toàn cảnh |
| B11 | lane | Vạch ô đỗ / vạch làn | Không gán lane | Ô đỗ người khuyết tật không phải ranh giới làn |
| B03 | lane | Cung cong / đoạn thẳng | Polyline nhiều điểm | Cần kiểm lại từng điểm và endpoint ở tỷ lệ 100% |

## 4. Phiếu QC 1 nhận được

Chưa có tên bạn được ghép, file của bạn đó hoặc phiếu QC trả về. Không tạo tên người kiểm, số lỗi hoặc quyết định giả. Mẫu chờ nằm ở phamanhtuan-qc1-PENDING.md. Chưa có phản hồi Rework chính thức để ghi nhận.

## 5. Kiểm file xuất

| File | Mở lại được? | Shape ảnh 1 (file / CVAT) | Shape ảnh 2 (file / CVAT) | Camera trong XML? |
| --- | --- | --- | --- | --- |
| phamanhtuan-front.zip | Có, đã đọc lại | 9 / 9 | 5 / 5 | Có |
| phamanhtuan-fisheye.zip | Có, đã đọc lại | 1 / 1 | 2 / 2 | Có |

Cả hai ZIP chỉ chứa annotations.xml, không kèm ảnh. Manifest có SHA-256, revision và contains_images=false. Lint còn 7 cảnh báo nặng QC1-02, không có cảnh báo thuộc tính/định dạng khác. Lint không đo độ chính xác với GT và không phải điểm chấm.

## 6. Minh chứng

- Ảnh project trước nhập được giữ cục bộ trong out/d11_submission_20261121/candidate/assets/cvat-project-before-import.png, không đưa lên GitHub.
- Ảnh front và fisheye B03 sau nhập được giữ cục bộ trong out/d11_submission_20261121/candidate/assets/, không đưa ảnh dữ liệu lên GitHub.
- XML nằm trong hai ZIP; mỗi shape khai báo source=auto nếu do AI tạo. Snapshot và các bản baseline/draft/reviewed được giữ để truy vết.
- Công cụ: SELFTEST PASS trên dữ liệu tổng hợp; 38 test repo đạt. Tự kiểm 78/78 chỉ là kiểm tra checker trên GT tổng hợp, **không phải điểm của Phạm Anh Tuấn**.

## 7. Dự thảo tự đánh giá để học viên xác nhận

Các lỗi nổi bật trong bản cũ: nhiều shape trùng, đảo chiều một số lane, nhầm ngựa vằn/ô đỗ thành lane, thiếu thuộc tính và nhận quảng cáo thành biển giao thông. Đã loại bản sao hoàn toàn, dùng một lượt dự đoán front, loại 5 nhãn quảng cáo/chữ mặt đường và 3 box chồng gần trùng sau rà crop, sửa các pedestrian signal bị nhận thành biển, bổ sung 5 đường lane nhìn thấy trên ảnh. Giữ các trường hợp chưa chắc trong bảng ca khó; không tự miễn lỗi chỉ để lint sạch.

Sai position hoặc nối vạch sai khiến model học ranh giới làn sai. Điểm đầu/điểm cuối sai cũng làm sai các đích row-anchor, dù file XML hợp lệ. Chưa có số đo GT để khẳng định sai số 5 px hoặc IoU đạt ngưỡng của lab.

## 8. Bài buffer row-anchor

A01, R1, kết quả nội suy từ chính file ứng viên:

| polyline | y=720 | y=680 | y=640 | y=600 | y=560 |
| --- | ---: | ---: | ---: | ---: | ---: |
| lane#3@(709,719) | không có làn | 655.1 | 599.5 | 543.9 | 488.3 |


1. Với hai điểm (x1,y1), (x2,y2), nội suy x(y)=x1+(x2-x1)*(y-y1)/(y2-y1). Nếu dừng sớm ở đầu xa 40 px, các hàng trong [y_min,y_min+40) mất đích; phải xét khoảng y cụ thể, không mặc định cả 5 hàng thay đổi. Nếu cắt đầu gần từ y=719 xuống 679 thì hàng 680 mất đích; hàng 720 vốn đã ngoài polyline.
2. Chưa có polyline của bạn được ghép nên chưa thể tính chênh lệch ở 720/560. Cần slide 25 để xác nhận đáp án LKA theo bài giảng; không thay số hoặc kết luận bài giảng bằng dữ liệu tự tạo.
3. Đảo chiều một polyline đơn điệu không đổi công thức nội suy theo đoạn, nhưng vi phạm quy tắc gần→xa, bị lint cảnh báo QC1-04 và có thể gây lỗi cho pipeline dùng điểm đầu làm vị trí gần xe.

## Việc còn phải hoàn tất

- Kiểm 7 cảnh báo QC1-02, sửa khi có vạch thật; coach xác nhận ngoại lệ khi thực sự không thấy.
- Rà đầy đủ vị trí, style/color/kind, occluded, vùng direct/alternative, box biển phụ và màu đèn ở tỷ lệ gốc; chưa chứng nhận điểm tự động hay sai số GT.
- Đã được duyệt và nhập nhãn vào task 33/34; ảnh minh chứng và số lượng file/UI đã đối chiếu. Cấu trúc hiện vẫn là hai task, chưa tạo/tách thêm task core/extra.
- Nhận bài của bạn được ghép, thực hiện QC1 thật, xử lý phản hồi và chỉ đánh dấu completed khi đủ điều kiện.

## Đồng bộ CVAT đã được phê duyệt

Task 33: HTTP 200, 210 shape và 64 tag; task 34: HTTP 200, 18 shape và 48 tag. Đọc lại khớp đầy đủ hình học/thuộc tính; kiểm lại sau khi mở giao diện vẫn đúng số lượng. Nguồn shape trên CVAT là auto. Không thay đổi schema, không đánh dấu job completed.

Bản sao trước nhập và payload nằm tại `cvat_sync_20261121T020023377086Z` ở thư mục cha. Task 33 trước nhập có 1.294 shape; task 34 trước nhập chưa có shape. Thay thế annotation được thực hiện sau phê duyệt của người dùng, không xóa bản sao gốc. Kết quả đối chiếu: quality-review.json; bản đọc lại đầy đủ giữ cục bộ trong out/d11_submission_20261121/candidate/cvat-readback-after-ui.json.

## Bản xuất trực tiếp từ CVAT dùng cho commit

Thời điểm export UTC: 2026-11-21T02:07:25.050254+00:00. Tên file, số byte và SHA-256 nằm trong export-receipt.json và phamanhtuan-manifest.json. Cả hai ZIP không chứa ảnh. Đây vẫn là bản chưa Release: 7 cảnh báo L1/R1 chưa được miễn, QC chéo chưa thực hiện và job chưa completed. Không coi commit/push là đã nộp hoặc được coach chấp nhận.
