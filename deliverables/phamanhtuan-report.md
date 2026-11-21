# Báo cáo cá nhân — Road Elements & SVM, Ngày 11

Họ tên: Phạm Anh Tuấn. Mã học viên: 2A202603232.

Tôi thực hiện gán nhãn theo Road v1.0 trên CVAT 2.82.1 với sự hỗ trợ của AI, sau đó rà ảnh, kiểm cấu trúc và xuất dữ liệu. Bản xuất revision 2 hiện có 228 shape và 112 tag trên 28 ảnh. Tôi giữ trạng thái chưa Release vì còn 7 cảnh báo thiếu position, chưa có QC chéo và chưa đo độ chính xác bằng nhãn chuẩn độc lập.

## 1. Project và cấu trúc dữ liệu

Tôi sử dụng project d11-road-2A202603232, task 33 cho 16 ảnh front và task 34 cho 12 ảnh fisheye. Schema gồm lane, road_curb, crosswalk, drivable, traffic_light, traffic_sign và bốn tag camera, timeofday, weather, source. Trong bài lab này, position L1/R1/L2/R2 thuộc lane.

Tôi đã đối chiếu schema và đọc lại annotation sau nhập. Các giá trị thuộc tính là kết quả gán nhãn có AI hỗ trợ; tính hợp lệ của chúng không chứng minh độ chính xác thị giác. Cấu trúc trên máy chủ vẫn gồm hai task; bốn dòng core/extra ở bảng thống kê là cách phân nhóm ảnh, không phải bốn task đã tạo. Hai job chưa được đánh dấu completed.

Tôi xuất trực tiếp bằng API CVAT, định dạng CVAT for images 1.1, không kèm ảnh. Sau khi mở giao diện, tôi đọc lại dữ liệu để kiểm số lượng và hình học, nhằm phát hiện annotation bị ghi trùng.

## 2. Thống kê annotation

| Nhóm ảnh | Ảnh | lane | road_curb | crosswalk | drivable | traffic_light | traffic_sign |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| front core | 12 | 30 | 14 | 5 | 21 | 42 | 40 |
| front extra | 4 | 10 | 1 | 3 | 7 | 17 | 20 |
| fisheye core | 8 | 2 | 2 | 4 | 3 | 2 | 0 |
| fisheye extra | 4 | 0 | 0 | 4 | 1 | 0 | 0 |

Tôi kiểm đủ bốn tag trên mỗi ảnh, tổng cộng 112 tag. B11 chỉ có tag vì các vạch ô đỗ không được tính là lane. Tôi không thêm lane cho B06/B08 chỉ dựa trên vạch ngựa vằn. Tôi giữ tọa độ ảnh fisheye gốc thay vì nắn thẳng đường cong.

## 3. Ca khó và cảnh báo còn lại

Tôi ghi nhận 7 cảnh báo QC1-02 trên 6 ảnh của task 33:

| Ảnh | Tên file | Frame | Position chưa có | Mở CVAT |
| --- | --- | ---: | --- | --- |
| A05 | A05_b2576c8c-2de20b8a.jpg | 4 | L1, R1 | [Kiểm ảnh](http://100.104.206.55:8080/tasks/33/jobs/33?frame=4) |
| A06 | A06_b8c66e31-37045eec.jpg | 5 | R1 | [Kiểm ảnh](http://100.104.206.55:8080/tasks/33/jobs/33?frame=5) |
| A07 | A07_b41ace08-c8468690.jpg | 6 | L1 | [Kiểm ảnh](http://100.104.206.55:8080/tasks/33/jobs/33?frame=6) |
| A10 | A10_b6ff1331-f6d3fba8.jpg | 9 | R1 | [Kiểm ảnh](http://100.104.206.55:8080/tasks/33/jobs/33?frame=9) |
| A12 | A12_c0f978fa-9b4e623f.jpg | 11 | R1 | [Kiểm ảnh](http://100.104.206.55:8080/tasks/33/jobs/33?frame=11) |
| A14 | A14_ca04d99f-c1282bb7.jpg | 13 | R1 | [Kiểm ảnh](http://100.104.206.55:8080/tasks/33/jobs/33?frame=13) |

Các cảnh báo trên phản ánh position chưa xuất hiện trong file. Chúng chưa đủ để kết luận có vạch thật bị bỏ sót. Tôi không tạo vạch suy đoán chỉ để xóa cảnh báo và chưa ghi nhận miễn trừ từ coach.

| Ca | Nhận xét và quyết định |
| --- | --- |
| A05 | Tôi chưa thấy căn cứ đủ chắc để bổ sung cả L1 và R1; hai cảnh báo vẫn được giữ. |
| A06, A09 | Tôi phát hiện cách cắt drivable theo mặt đường nhìn thấy có thể làm mất phần đường bị ô tô che. Theo Road v1.0, vùng lái phải biểu diễn phần đi được nếu đường trống, không khoét theo xe khác. |
| A03 | Đoạn khuất và điểm kết thúc lane còn cần đánh giá hình học độc lập; kiểm định dạng không xác nhận độ chính xác endpoint. |
| A08, A15 | Tôi ghi nhận nguy cơ gộp biển chính và biển phụ trong cùng box; chưa chứng nhận toàn bộ box đã đúng phạm vi. |
| A07, A10, A13 | Tôi gán weather=rain dựa trên toàn cảnh và dấu hiệu mặt đường ướt; giá trị này chưa có người kiểm độc lập xác nhận. |
| A11, A14 | Tôi lần lượt gán dusk và night sau khi đối chiếu toàn cảnh. |
| B03 | Tôi dùng polyline nhiều điểm để giữ độ cong fisheye; chưa đo sai số với GT. |
| B11 | Tôi loại cách hiểu vạch ô đỗ là ranh giới làn. |

Tôi đã sửa mã hậu xử lý trong repo CVAT agent để sử dụng đầu phát hiện xe sẵn có của YOLOPv2, khôi phục phần che khuất có giới hạn trong bao hình học của vùng đường và giữ khoảng cách với lane. Kiểm thử Docker đạt 57/57; suy luận A06/A09 chạy thành công và phát hiện lần lượt 8/7 vùng xe. Đây là kiểm chứng kỹ thuật, chưa phải đánh giá độ chính xác polygon. Tôi đã sửa hai polygon A06/A09 trên CVAT bằng cách rà ảnh và xuất lại ZIP front. Đối chiếu theo ID xác nhận chỉ hai polygon đổi tọa độ; tổng số shape và tag giữ nguyên. Việc sửa thủ công hai ảnh không chứng minh thuật toán tự động đã đạt độ chính xác tương đương.

## 4. QC chéo và trạng thái nghiệm thu

Tôi chưa có tên người được ghép, bài của người đó hoặc phiếu QC gửi lại. Vì vậy tôi chưa thực hiện và chưa tính tỷ lệ lỗi QC chéo. File phamanhtuan-qc1-PENDING.md ghi nhận trạng thái thiếu đầu vào này; đó không phải phiếu QC hoàn thành. Tôi chưa có phản hồi Rework chính thức hay quyết định Release của coach.

## 5. Kiểm file xuất và khả năng tái lập

| File | Đọc XML | Shape ảnh 1: file/CVAT | Shape ảnh 2: file/CVAT | Tag camera |
| --- | --- | --- | --- | --- |
| phamanhtuan-front.zip | Thành công | 9/9 | 5/5 | Có |
| phamanhtuan-fisheye.zip | Thành công | 1/1 | 2/2 | Có |

Tôi đối chiếu toàn bộ hình học, thuộc tính và tag với bản ứng viên, không chỉ đối chiếu tổng số. Mỗi ZIP chỉ chứa annotations.xml. Dung lượng, SHA-256 và thời điểm xuất được ghi trong export-receipt.json và phamanhtuan-manifest.json. Hai file không chứa ảnh.

Tôi kiểm thử công cụ của bài lab với 38 test đạt và SELFTEST PASS trên dữ liệu tổng hợp. Kết quả tổng hợp 78/78 kiểm tra hoạt động của checker, không phải điểm bài làm hay độ chính xác annotation của tôi. Kiểm cấu trúc còn 7 cảnh báo QC1-02 và không báo thiếu thuộc tính/định dạng khác.

## 6. Minh chứng và truy vết

Tôi lưu ảnh project trước nhập, ảnh front và ảnh fisheye B03 sau nhập ở thư mục cục bộ out/d11_submission_20261121/candidate/assets/. Tôi giữ ảnh dữ liệu ngoài GitHub theo điều kiện sử dụng dữ liệu. Snapshot baseline, draft, reviewed, candidate và bản sao trước nhập được lưu cục bộ để đối chiếu thay đổi.

Dưới đây là một polyline trích trực tiếp từ XML trong phamanhtuan-front.zip:

```xml
<polyline label="lane" source="auto" occluded="0" points="12.30,598.17;30.81,592.67;49.30,587.18;67.76,581.69;86.26,576.20;104.76,570.70;123.25,565.21;141.77,559.72;160.31,554.23;178.81,548.73;197.29,543.24;215.81,537.75;234.38,532.26;252.90,526.76;271.40,521.27;289.92,515.78;308.46,510.29;326.96,504.79;345.44,499.30" z_order="0">
      <attribute name="position">L2</attribute>
      <attribute name="style">solid</attribute>
      <attribute name="color">white</attribute>
      <attribute name="kind">single</attribute>
    </polyline>
```

Tôi giữ source=auto cho shape do AI hỗ trợ tạo. Lần nhập đã được duyệt trả HTTP 200 cho cả hai task; dữ liệu đọc lại gồm task 33 có 210 shape/64 tag và task 34 có 18 shape/48 tag. Tôi không thay đổi schema hoặc tự xác nhận job hoàn thành.

## 7. Tự đánh giá

Tôi nhận thấy các lỗi chính của bản trước gồm shape trùng, đảo chiều lane, nhận nhầm ngựa vằn hoặc ô đỗ thành lane, thiếu thuộc tính và nhận quảng cáo thành biển giao thông. Tôi đã loại bản sao hoàn toàn, rà crop để loại 5 nhãn quảng cáo/chữ mặt đường và 3 box chồng gần trùng, sửa một số pedestrian signal bị nhận thành biển và bổ sung 5 polyline lane có dấu vạch quan sát được.

Tôi đánh giá điểm yếu còn lại nằm ở suy luận hình học khi che khuất và kiểm chứng thuộc tính bằng ảnh. Việc ô tô làm mất drivable cho thấy mask mặt đường nhìn thấy chưa tương đương vùng có thể lái khi đường trống. Tôi đã bổ sung kiểm thử hồi quy cho khác biệt này nhưng chưa có so sánh trước/sau với GT. Vì vậy tôi chưa khẳng định cải thiện IoU, sai số không quá 5 px hoặc mức điểm cụ thể.

Sai position, nối nhầm vạch và cắt endpoint đều có thể tạo đích huấn luyện sai dù XML hợp lệ. Tôi giữ các hạn chế này trong kết luận thay vì coi số lượng shape hay lint sạch là bằng chứng chất lượng.

## 8. Phân tích row-anchor

Tôi nội suy lane R1 của A01 từ chính bản ứng viên:

| Polyline | y=720 | y=680 | y=640 | y=600 | y=560 |
| --- | ---: | ---: | ---: | ---: | ---: |
| lane#3, điểm gần (709,719) | Không có | 655.1 | 599.5 | 543.9 | 488.3 |

Tôi sử dụng x(y)=x1+(x2−x1)(y−y1)/(y2−y1) cho đoạn cắt hàng y. Hàng 720 nằm ngoài polyline hiện tại. Khi cắt đầu gần từ y=719 xuống 679, hàng 680 mất đích. Khi cắt đầu xa 40 px, chỉ các hàng nằm trong phần bị cắt mất đích; không thể mặc định cả năm hàng đều thay đổi.

Tôi chưa có polyline của người được ghép nên chưa tính chênh lệch tại 720 và 560. Về kỹ thuật, sai số ở hàng gần xe ảnh hưởng ước lượng độ lệch ngang, còn sai số phía xa ảnh hưởng hướng và độ cong dự báo; mức ảnh hưởng phụ thuộc bộ điều khiển. Đây là phân tích của tôi, chưa phải đáp án được đối chiếu với slide 25.

Đảo thứ tự điểm của polyline đơn điệu không đổi kết quả nội suy theo đoạn. Tuy nhiên, thao tác đó vi phạm quy tắc gần→xa, có thể gây cảnh báo QC1-04 và làm sai các bước xử lý giả định điểm đầu là đầu gần xe.

## Kết luận

Tôi đã xuất và kiểm lại bộ annotation revision 2, hoàn thành kiểm cấu trúc và ghi rõ các ca còn nghi vấn. Bản hiện tại chưa đủ điều kiện Release. Những phần chưa hoàn tất gồm đánh giá định lượng thuật toán che khuất, xác minh 7 cảnh báo position, tổ chức đủ bốn task theo yêu cầu và QC chéo khi có bài được ghép. Tôi chưa coi commit/push là nghiệm thu hoặc xác nhận chất lượng của coach.
