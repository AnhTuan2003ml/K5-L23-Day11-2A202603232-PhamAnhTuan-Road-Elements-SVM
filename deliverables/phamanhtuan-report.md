# Báo cáo cá nhân — Ngày 11 · Road Elements & SVM

**Phạm Anh Tuấn · 2A202603232**

Road v1.0 · Revision 1

**Kết quả QC: PASS sau khi áp dụng ngoại lệ A05 đã được QC xác nhận.** Bộ ZIP cục bộ gồm 20 ảnh bắt buộc, 174 shape và 80 tag. Lint ghi nhận **2 cảnh báo nặng QC1-02**, cùng ở A05. Sau khi áp dụng ngoại lệ, không còn cảnh báo nào cần xử lý trong kết quả lint.

## 1. Kiểm project và nguồn nhãn

Bộ file dựa trên export từ task 33/34. Hai mươi ảnh A01–A12 và B01–B08 dùng nhãn và tag từ bộ ZIP của Nguyễn Thanh Phong. Sau khi rà ảnh gốc, A10 được bỏ một box biển dưới 8 px theo guideline. Phạm vi bàn giao chỉ gồm phần bắt buộc.

Bộ ZIP có sáu nhãn theo Road v1.0 và đủ bốn tag camera, timeofday, weather và source trên cả 20 ảnh. Trong CVAT, bấm **N** để kết thúc polyline. Khi đặt tag ảnh, chọn kiểu **Tag** và điền thuộc tính `value`. [Hướng dẫn CVAT](../docs/huong_dan_cvat_bang_hinh.md)

## 2. Số lượng nhãn

| Lô | Ảnh | lane | road_curb | crosswalk | drivable | traffic_light | traffic_sign | Tổng shape |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Front | 12 | 33 | 3 | 5 | 24 | 29 | 32 | 126 |
| Fisheye | 8 | 9 | 7 | 9 | 11 | 7 | 5 | 48 |

## 3. Cảnh báo theo ảnh

| Mã | Mức | Số | Ảnh | Kết quả rà |
| --- | --- | ---: | --- | --- |
| QC1-02 | Nặng | 2 | A05 | Ảnh gốc không thấy vạch sơn L1/R1. QC đã xác nhận ngoại lệ cho cả hai cảnh báo, theo thông tin học viên cung cấp. |

[Log lint cục bộ](../out/core_only_20261121T082351069886Z/lint.txt)

## 4. Phiếu QC1 nhận được

Học viên báo QC đã xác nhận ngoại lệ QC1-02 cho A05 (L1 và R1). Chưa có phiếu QC1 đầy đủ hoặc quyết định Release lưu trong repo. Phiếu kiểm lô Nguyễn Thanh Phong cũng đề xuất Hold tại A05. [Phiếu kiểm lô Nguyễn Thanh Phong](phamanhtuan-qc1-for-nguyenthanhphong.md)

## 5. Kiểm file bàn giao

| File | Mở lại | Shape ảnh 1 / ảnh 2 trong XML | Ảnh đủ 4 tag |
| --- | --- | --- | ---: |
| phamanhtuan-front.zip | Có | A01: 8 / A02: 5 | 12/12 |
| phamanhtuan-fisheye.zip | Có | B01: 5 / B02: 8 | 8/8 |

Hai ZIP chứa `annotations.xml` theo định dạng CVAT for images 1.1. Đã tải hai ZIP và manifest từ Drive để đối chiếu. SHA-256 của cả ba file khớp bản cục bộ đã kiểm. [Thư mục D11 trên Google Drive](https://drive.google.com/drive/folders/1vTJRBtQC7eHw4MEU_ozNQ13UDO2WnfEr?usp=sharing)

| Tệp đã tải lên | Dung lượng | Kết quả đối chiếu |
| --- | ---: | --- |
| [phamanhtuan-front.zip](https://drive.google.com/file/d/1tjiuO92_LmluXl-08S0TrNh4urACsyN5/view?usp=drivesdk) | 8.695 byte | Khớp SHA-256 |
| [phamanhtuan-fisheye.zip](https://drive.google.com/file/d/1Ck6B9MsJxagNOhawAuxFbuOmfERp2GjA/view?usp=drivesdk) | 6.315 byte | Khớp SHA-256 |
| [phamanhtuan-manifest.json](https://drive.google.com/file/d/1NmYrQvMPgLUSOSeJ0n6shrJpm267VDIV/view?usp=drivesdk) | 1.328 byte | Khớp SHA-256, revision 1 |

## 6. Minh chứng

Thư mục Drive hiện có hai ZIP và manifest. Các ảnh chụp dưới đây là minh chứng thao tác trên CVAT của bản ứng viên trước. Ảnh chụp tab Labels, ảnh front và fisheye khớp revision 1, cùng xác nhận job `completed` cho bộ 20 ảnh, chưa có trong hồ sơ.

- [Project CVAT trước khi nhập bản ứng viên](../out/d11_submission_20261121/candidate/assets/cvat-project-before-import.png)
- [Ảnh front sau khi nhập bản ứng viên](../out/d11_submission_20261121/candidate/assets/cvat-front-after-import.png)
- [Ảnh fisheye sau khi nhập bản ứng viên](../out/d11_submission_20261121/candidate/assets/cvat-fisheye-after-import.png)

Đoạn polyline dưới đây trích từ `annotations.xml` của ảnh A01 trong ZIP front revision 1.

```xml
<polyline label="lane" source="manual" occluded="0" points="1280.00,705.90;461.40,509.60" z_order="0">
  <attribute name="position">R2</attribute>
  <attribute name="style">solid</attribute>
  <attribute name="color">yellow</attribute>
  <attribute name="kind">single</attribute>
</polyline>
```

## 7. Tự đánh giá

Đã rà A05 và ghi nhận ngoại lệ QC đã xác nhận vì ảnh không thấy vạch phân làn. Gán vạch suy đoán ở đây có thể làm model học ranh giới làn sai. Lint chạy trên hai ZIP hiện tại. Lần kiểm tra công cụ trước khi đóng gói đạt 38/38 test và selftest PASS trên dữ liệu tổng hợp. Chưa đối chiếu với ground truth của coach.

## 8. Row-anchor (tùy chọn)

Không thực hiện.
