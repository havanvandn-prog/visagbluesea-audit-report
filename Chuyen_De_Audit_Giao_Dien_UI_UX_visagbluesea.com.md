# CHUYÊN ĐỀ THẨM ĐỊNH TRẢI NGHIỆM GIAO DIỆN (UI/UX AUDIT)
## HỆ THỐNG WEBSITE TƯ VẤN ĐỊNH CƯ & VISA CAO CẤP — VISAGBLUESEA.COM

> **Đơn vị thẩm định:** Chuyên gia Trải nghiệm Người dùng & Tối ưu Tỷ lệ Chuyển đổi (CRO Specialist)  
> **Website đối soát:** [https://www.visagbluesea.com/](https://www.visagbluesea.com/)  
> **Thời điểm thẩm định:** Tháng 10/2026  
> **Trọng tâm đánh giá:** Khả năng sẵn sàng tiếp nhận lượng truy cập trả phí (Google Ads), mức độ giữ chân khách hàng và loại bỏ các điểm nghẽn cản trở chuyển đổi trên cả máy tính (Desktop) và điện thoại di động (Mobile).

---

## 1. TỔNG QUAN HIỆN TRẠNG TRẢI NGHIỆM NGƯỜI DÙNG

Website **GBlueSea** hoạt động trong phân khúc dịch vụ cao cấp có giá trị vòng đời khách hàng lớn (AOV từ 50 triệu VNĐ đến các chương trình đầu tư di trú định cư từ 500,000 USD đến 800,000 USD như EB-5 Mỹ, Golden Visa Hy Lạp/Síp). Đối tượng khách hàng mục tiêu là các nhà đầu tư, chủ doanh nghiệp và phụ huynh có tài chính tốt, yêu cầu rất khắt khe về **tính minh bạch, sự chuyên nghiệp và độ tin cậy tuyệt đối**.

Tuy nhiên, khảo sát thực tế phát hiện website đang vận hành trên nền tảng Wix với nhiều điểm nghẽn thiết kế chưa được hoàn thiện, các đoạn văn bản mẫu của giao diện ngoại quốc chưa được biên tập, và luồng liên hệ trên điện thoại di động chưa được tối ưu hóa cho hành vi người dùng Việt Nam.

---

## 2. BẢN ĐỔ 7 TRỤ CỘT TRẢI NGHIỆM GIAO DIỆN (DESKTOP & MOBILE)

```
                            TRẢI NGHIỆM UI/UX GBLUESEA
                                       │
     ┌──────────────┬──────────────┼──────────────┬──────────────┐
     ↓              ↓              ↓              ↓              ↓
1. Header &    2. Hero Banner 3. Bố Cục Lưới 4. Vùng Chạm   5. Biểu Mẫu
   Điều Hướng     & Tương Phản    & Hình Ảnh     Ngón Cái       Liên Hệ
  (3 Hotline       (Thiếu CTA      (Lỗi Mẫu       (Thiếu         (Ma Sát
   Rối Mắt)        Chính)          CAPS TITLE)    Sticky Bar)    Tách Họ Tên)
```

---

### TRỤ CỘT 1: HEADER & THANH ĐIỀU HƯỚNG (NAVIGATION UX)
- **Hiện trạng thực tế:**
  1. Header hiển thị cùng lúc 3 số điện thoại với định dạng không thống nhất: `Call now:`, `0901830827` và `+358458691902` (số Phần Lan). Chữ `Call now:` là liên kết số thứ nhất (`tel:+84-0932797164`) nhưng không hiển thị rõ số khiến người dùng bối rối.
  2. Người dùng không phân biệt được số nào là Hotline tư vấn tại Việt Nam, số nào là hỗ trợ qua Zalo và số nào dành cho khách hàng quốc tế.
  3. Menu dịch vụ phân tầng phức tạp, các đường dẫn còn lẫn lộn giữa tiếng Anh và tiếng Việt (`/us-green-card-eb-5`, `/eu-golden-visa`, `/study-in-australia`).
- **Tác động kinh doanh:** Khách hàng muốn gọi điện ngay nhưng không biết bấm vào đâu; gây cảm giác lộn xộn, thiếu chuyên nghiệp của một tổ chức tư vấn quốc tế.
- **Giải pháp xử lý:**
  - Chuẩn hóa cụm liên hệ Header thành 2 điểm chạm dứt khoát:
    * **Hotline Việt Nam (24/7):** `0901.830.827` (nổi bật với biểu tượng điện thoại rung nhẹ).
    * **Tư Vấn Zalo Trực Tiếp:** `0901.830.827` (nút màu xanh Zalo chuẩn nhận diện).
  - Thu gọn số văn phòng quốc tế (Mỹ, Phần Lan) vào menu con "Hệ Thống Văn Phòng Toàn Cầu".

---

### TRỤ CỘT 2: KHU VỰC HERO BANNER & TƯƠNG PHẢN THỊ GIÁC (WCAG 2.1)
- **Hiện trạng thực tế:**
  1. Trang chủ không có một câu thông điệp định vị giá trị (Value Proposition) sắc nét. Thẻ H1 bị gán cho cụm từ mờ nhạt: *"Các dịch vụ nổi bật"*.
  2. Khối văn bản giới thiệu dài 4 dòng bị gán nhầm thành thẻ `<h1>` thứ hai, gây rối loạn thứ bậc thị giác.
  3. Thiếu nút kêu gọi hành động trọng tâm (Primary CTA) có độ tương phản cao ở màn hình đầu tiên (Above the fold).
- **Tác động kinh doanh:** Khách hàng nhấp vào từ quảng cáo Google Ads mất 3–5 giây đầu tiên mà không nắm được ngay GBlueSea mang lại giải pháp gì vượt trội so với các đơn vị di trú khác.
- **Giải pháp xử lý:**
  - Thiết kế lại Hero Banner với thông điệp mạnh mẽ:
    * **Tiêu đề chính (H1):** *"Tư Vấn Định Cư, Đầu Tư & Visa Toàn Cầu — Tỷ Lệ Đậu Hồ Sơ 99.2%"*.
    * **Tiêu đề phụ:** *"Đồng hành cùng hơn 5,300+ gia đình Việt hiện thực hóa giấc mơ định cư Mỹ (EB-5), Síp, Hy Lạp và Du học Quốc tế. Đội ngũ luật sư di trú trực tiếp thụ lý hồ sơ."*
    * **Cặp nút hành động kép:** Nút 1 `[Nhận Thẩm Định Hồ Sơ Miễn Phí]` (Màu xanh Emerald `#01a915`) + Nút 2 `[Hotline 24/7: 0901.830.827]`.

---

### TRỤ CỘT 3: BỐ CỤC LƯỚI & NỘI DUNG MẪU CHƯA THAY THẾ (LAYOUT & CONTENT HYGIENE)
- **Hiện trạng thực tế:**
  1. Xuất hiện tiêu đề văn bản mẫu tiếng Anh chưa được chỉnh sửa: **`CAPS TITLE`** (nằm ngay trên trang chủ).
  2. Phần số liệu thành tựu hiển thị thô sơ: **`17       5347      235`** bị dồn cục vào thẻ H2, các con số đứng riêng không có nhãn đơn vị rõ ràng (17 Quốc Gia, 5.347 Khách Hàng, 235 Hồ Sơ Định Cư).
  3. Trang con `/study-in-australia` (Du học Úc) nhưng khối tin tức phía dưới lại hiển thị bài về Phần Lan, Canada và bài thi SAT của Mỹ, làm loãng trọng tâm tìm kiếm của phụ huynh.
- **Tác động kinh doanh:** Khách hàng nghi ngờ tính chuyên nghiệp của doanh nghiệp; cảm giác website chưa hoàn thiện hoặc bỏ hoang.
- **Giải pháp xử lý:**
  - Xóa bỏ 100% các khối chữ mẫu (Placeholder) như `CAPS TITLE`.
  - Thiết kế lại khối **Executive Stat Cards** thành 3 thẻ chỉ số sang trọng:
    * Thẻ 1: **17+** Quốc gia đối tác di trú hàng đầu.
    * Thẻ 2: **5,300+** Khách hàng định cư & du học thành công.
    * Thẻ 3: **15+ Năm** Kinh nghiệm luật sư di trú quốc tế.
  - Phân loại bài viết liên quan đúng theo quốc gia của từng trang đích.

---

### TRỤ CỘT 4: VÙNG CHẠM NGÓN TAY TRÊN DI ĐỘNG (MOBILE THUMB ZONE & STICKY BAR)
- **Hiện trạng thực tế:**
  1. Hơn 75% lưu lượng tìm kiếm Google Ads ngành Visa/Di trú đến từ điện thoại di động (Mobile Search).
  2. Tuy nhiên, website hoàn toàn **KHÔNG CÓ THANH HÀNH ĐỘNG CỐ ĐỊNH Ở ĐÁY MÀN HÌNH (Sticky Action Bar)**.
  3. Khách hàng khi cuộn xem thông tin chi tiết về điều kiện visa phải cuộn ngược hàng chục màn hình lên đầu trang để tìm số điện thoại gọi tư vấn.
- **Tác động kinh doanh:** Gây mất dấu khách hàng tiềm năng ngay ở khoảnh khắc họ phát sinh nhu cầu liên hệ cao nhất.
- **Giải pháp xử lý:**
  - Bổ sung thanh nút bấm cố định dưới đáy màn hình trên thiết bị di động (`fixed bottom-0 left-0 right-0 z-50`):
    * **Nút Trái (50%):** `[📞 Gọi Hotline 24/7]` (Màu xanh Emerald `#01a915`).
    * **Nút Phải (50%):** `[💬 Chat Zalo Thẩm Định]` (Màu xanh Zalo `#0068ff`).
  - Thiết kế chiều cao chuẩn 56px, vùng chạm ngón tay cái tối thiểu 44px × 44px, có đệm khoảng trống an toàn dưới đáy (Safe Area Inset).

---

### TRỤ CỘT 5: BIỂU MẪU LIÊN HỆ & MA SÁT TÂM LÝ (FORM COGNITIVE FRICTION)
- **Hiện trạng thực tế:**
  1. Form tư vấn hiện tại chia tách thành 2 ô riêng biệt: `Tên` và `Họ`. Đây là tư duy form kiểu phương Tây (First Name / Last Name), hoàn toàn không phù hợp với thói quen gõ tên của người Việt Nam.
  2. Bắt buộc nhập `Email`. Đa số khách hàng tìm kiếm visa/du học trên điện thoại muốn nhận báo giá hoặc tư vấn hồ sơ nhanh qua số điện thoại/Zalo thay vì kiểm tra email.
  3. Thiếu hộp chọn nhanh dịch vụ đang quan tâm (Định cư Mỹ, Golden Visa Châu Âu, Du học Úc/Canada...) khiến đội ngũ kinh doanh khó phân loại dữ liệu khi khách gửi yêu cầu.
  4. Thiếu lời cam kết bảo mật thông tin tài chính và thời gian phản hồi.
- **Tác động kinh doanh:** Tỷ lệ bỏ ngang form đăng ký (Drop-off Rate) ước tính lên tới 60–70%.
- **Giải pháp xử lý:**
  - Tinh giản form xuống còn **3 trường duy nhất**:
    1. *Họ và tên* (Gộp 1 ô duy nhất).
    2. *Số điện thoại / Zalo* (Có kiểm tra tính hợp lệ của số điện thoại Việt Nam 10 chữ số).
    3. *Chương trình quan tâm* (Menu thả xuống: Định Cư Mỹ EB-5 | Golden Visa Hy Lạp/Síp | Visa Du Học | Visa Lao Động).
  - Bổ sung ghi chú an tâm: *"Bảo mật thông tin khách hàng 100% theo tiêu chuẩn quốc tế • Chuyên viên liên hệ hỗ trợ trong vòng 15 phút"*.

---

### TRỤ CỘT 6: THỨ BẬC THỊ GIÁC & LỖI BẢN MẪU NGOẠI QUỐC (TYPOGRAPHY & LANGUAGE HYGIENE)
- **Hiện trạng thực tế:**
  1. Trang **Định cư Mỹ EB-5** (`/us-green-card-eb-5`) có thẻ H1 hiển thị chữ: **`Acerca de`** (tiếng Tây Ban Nha có nghĩa là "Giới thiệu").
  2. Trang **Định cư Châu Âu Golden Visa** (`/eu-golden-visa`) hoàn toàn **KHÔNG CÓ THẺ H1**.
  3. Trang nhân bản rác lọt vào sitemap: `/copy-of-malta-investment-visa-1` mang tiêu đề *"Các Khóa Học | GBlueSea"* và thẻ H1 cũng là `"Acerca de"`.
- **Tác động kinh doanh:**
  - Đối với khách hàng đầu tư EB-5 (khoản tiền đầu tư tối thiểu 800,000 USD ~ 20 tỷ VNĐ), việc nhìn thấy chữ tiếng Tây Ban Nha vỡ mẫu làm suy sụp hoàn toàn niềm tin vào tính pháp lý và quy mô quốc tế của doanh nghiệp.
  - Đối với Google Ads, điểm chất lượng trang đích (Landing Page Experience) bị đánh giá Thấp, khiến giá thầu CPC bị đẩy lên cao vô lý.
- **Giải pháp xử lý:**
  - Rà soát xóa sạch 100% các từ ngữ tiếng nước ngoài còn sót lại từ theme mẫu.
  - Đặt lại thẻ H1 chuẩn xác, đồng bộ giữa từ khóa quảng cáo và tiêu đề trang đích:
    * Trang EB-5: `<h1>Đầu Tư Định Cư Mỹ EB-5 — Nhận Thẻ Xanh Cho Cả Gia Đình</h1>`
    * Trang Golden Visa: `<h1>Chương Trình Golden Visa Châu Âu: Định Cư Hy Lạp & Síp</h1>`

---

### TRỤ CỘT 7: CHÂN TRANG & TÍN HIỆU TÍN NHIỆM (FOOTER & TRUST SIGNALS)
- **Hiện trạng thực tế:**
  1. Chân trang chưa thể hiện rõ Giấy phép hoạt động tư vấn du học / di trú do cơ quan nhà nước có thẩm quyền cấp.
  2. Chưa có bản đồ chỉ đường và địa chỉ rõ ràng của các trụ sở chính tại TP. Hồ Chí Minh, Hà Nội, Đà Nẵng, cũng như các văn phòng đại diện tại Mỹ, Hy Lạp, Phần Lan.
  3. Thiếu logo liên kết mạng xã hội chính thức và mã số doanh nghiệp.
- **Tác động kinh doanh:** Khách hàng không tìm thấy cơ sở pháp lý vững chắc trước khi quyết định ký hợp đồng tư vấn dịch vụ giá trị lớn.
- **Giải pháp xử lý:**
  - Chuẩn hóa chân trang với 4 cột thông tin rõ ràng:
    * Cột 1: Thông tin pháp nhân Công ty TNHH Tư Vấn GBlueSea, Giấy phép ĐKKD, Giấy phép tư vấn di trú.
    * Cột 2: Danh mục dịch vụ di trú trọng điểm.
    * Cột 3: Hệ thống văn phòng trong nước & quốc tế kèm bản đồ Google Maps xác thực.
    * Cột 4: Chứng nhận bảo mật, chính sách cam kết hoàn phí nếu không đạt kết quả và liên kết mạng xã hội.

---

## 3. MA TRẬN 14 KHU VỰC ĐÁNH GIÁ CHI TIẾT

| STT | Vị Trí Giao Diện | Hiện Trạng Ghi Nhận | Mức Độ Rủi Ro | Hành Động Kỹ Thuật Đề Xuất |
|:---:|:---|:---|:---:|:---|
| 1 | **Header Topbar** | Chứa 3 số điện thoại không có nhãn phân biệt, chữ "Call now:" bị mất số | **P0 (Khẩn cấp)** | Rút gọn còn 1 Hotline chính + 1 Zalo, gắn nhãn rõ ràng |
| 2 | **Menu Điều Hướng** | URL lẫn lộn slug tiếng Anh, menu cấp 2 khó bấm trên di động | **P1 (Cao)** | Thiết kế lại Mega Menu chuẩn tiếng Việt, tối ưu phân nhóm |
| 3 | **Hero Banner Trang Chủ** | H1 là "Các dịch vụ nổi bật", thiếu CTA chuyển đổi chính | **P0 (Khẩn cấp)** | Thay H1 thành định vị di trú toàn cầu, thêm nút Thẩm Định Hồ Sơ |
| 4 | **Khối Thành Tựu** | Số liệu dồn cục `17 5347 235`, tiêu đề rác `CAPS TITLE` | **P0 (Khẩn cấp)** | Xóa `CAPS TITLE`, dựng 3 Card thống kê số liệu sang trọng |
| 5 | **Trang Con EB-5** | Thẻ H1 hiển thị chữ tiếng Tây Ban Nha `Acerca de` | **P0 (Khẩn cấp)** | Sửa ngay H1 thành "Đầu Tư Định Cư Mỹ EB-5 — Nhận Thẻ Xanh" |
| 6 | **Trang Con Golden Visa**| Khuyết hoàn toàn thẻ tiêu đề H1 | **P1 (Cao)** | Bổ sung thẻ H1 chuẩn từ khóa Golden Visa Hy Lạp & Síp |
| 7 | **Trang Nhân Bản Rác** | Tồn tại URL `/copy-of-malta-investment-visa-1` nội dung lộn xộn | **P0 (Khẩn cấp)** | Xóa trang nhân bản hoặc thiết lập 301 Redirect về trang chính |
| 8 | **Biểu Mẫu Tư Vấn** | Tách riêng ô Tên và Họ, bắt buộc email, không có cam kết bảo mật | **P0 (Khẩn cấp)** | Gộp thành 3 trường (Họ tên, SĐT Zalo, Nhu cầu), thêm cam kết 15 phút |
| 9 | **Thanh Nút Bấm Di Động** | Hoàn toàn không có Sticky Action Bar ở đáy màn hình | **P0 (Khẩn cấp)** | Lập trình thanh cố định 2 nút [Gọi Hotline] + [Chat Zalo] |
| 10 | **Trang Liên Hệ** | Có tới 4 form nhúng chồng chéo trên 1 trang do lỗi thiết kế Wix | **P1 (Cao)** | Gom lại duy nhất 1 form chuẩn, tích hợp bản đồ văn phòng |
| 11 | **Tốc Độ Tải Nền Tảng** | Nền tảng Wix tải mã HTML ban đầu nặng 1.22 MB, nhiều script nặng | **P1 (Cao)** | Tối ưu nén ảnh WebP, dọn dẹp các widget bên thứ ba không dùng |
| 12 | **Đo Lường Sự Kiện** | Chưa gắn thẻ Google Ads Conversion cho Form và Click Hotline/Zalo | **P0 (Khẩn cấp)** | Cài đặt đầy đủ Trigger GTM cho lượt gửi form và nhấp số điện thoại |
| 13 | **Khối Tin Tức Liên Quan**| Nội dung tin tức không khớp với dịch vụ của trang đích | **P2 (Trung bình)** | Cấu hình lọc bài viết theo chuyên mục quốc gia tương ứng |
| 14 | **Chân Trang (Footer)** | Thiếu giấy phép kinh doanh di trú, thiếu bản đồ chi nhánh | **P1 (Cao)** | Bổ sung đầy đủ thông tin pháp lý, địa chỉ 5 văn phòng toàn cầu |

---

## 4. CHECKLIST BÀN GIAO CHO ĐỘI NGŨ THIẾT KẾ & LẬP TRÌNH

### Danh Mục Công Việc Ưu Tiên Xử Lý Ngay (Trong 48 Giờ Đầu):
- [ ] **Sửa lỗi văn bản:** Xóa bỏ chữ `CAPS TITLE` trên trang chủ; thay thế chữ `Acerca de` trên trang EB-5 và các trang khóa học.
- [ ] **Khắc phục tiêu đề H1:** Thiết lập duy nhất 1 thẻ H1 cho mỗi trang đích; gỡ bỏ thẻ H1 khỏi đoạn văn bản dài 4 dòng ở trang chủ.
- [ ] **Tối ưu Form liên hệ:** Đổi form thành 3 trường tinh gọn (Họ tên, SĐT/Zalo, Dịch vụ cần tư vấn); bổ sung dòng cam kết bảo mật.
- [ ] **Thêm Mobile Sticky Bar:** Cài đặt thanh cố định chân trang hiển thị nút [Gọi Ngay: 0901.830.827] và [Nhắn Zalo 24/7] trên mọi thiết bị di động.
- [ ] **Gắn mã đo lường:** Cấu hình sự kiện chuyển đổi Google Ads (GTM Conversion Tag) cho cả 2 hành vi: Bấm gửi Form và Bấm gọi Hotline/Zalo.
