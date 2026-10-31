import sys

sys.stdout.reconfigure(encoding='utf-8')
skill_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\SKILL.md'

with open(skill_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update early mention of URL matrix around index 6610
target_url_matrix = """     - **Mục Kiến Trúc Sitemap Mục Tiêu & Ma Trận Xử Lý URL:** Bảng ánh xạ URL cũ → Hành động (Giữ / 301 Redirect / Tạo mới / Gộp) → URL mới → Search Intent → Mục tiêu chuyển đổi."""
replacement_url_matrix = """     - **Mục Kiến Trúc Sitemap Mục Tiêu & Định Vị Trung Tâm Báo Giá (RFQ Hub):** Bản đồ Sitemap phân nhóm dịch vụ chuẩn và mô hình RFQ Hub chốt đơn khách VIP (TUYỆT ĐỐI KHÔNG đưa bảng ma trận URL kỹ thuật 301/410 vào bản này; toàn bộ bảng ma trận kỹ thuật 100% chỉ lưu trong Sheet 4 File Excel và Báo Cáo Kỹ Thuật Nội Bộ cho Dev)."""

if target_url_matrix in text:
    text = text.replace(target_url_matrix, replacement_url_matrix, 1)
    print("Updated early URL matrix mention in SKILL.md!")
else:
    print("Warning: target_url_matrix not found in SKILL.md!")

# 2. Add Floating Contact Bar check in LUỒNG 1 around index 18250
target_tracking_rule = """    * ⛔ **CẤM ĐƯA LỖI THIẾU TRACKING ADS / GTM LÀM ĐIỂM NGHẼN WEBSITE TRƯỚC HỢP ĐỒNG:** Giai đoạn audit trước khi nhận dự án, website chưa chạy Ads thì việc chưa cài thẻ theo dõi chuyển đổi Google Ads (GTM Tag) là điều hiển nhiên. TUYỆT ĐỐI KHÔNG đưa vào làm lỗi chặn P0 của website trong bản trình bày khách hàng. Thiết lập tracking thuộc về kế hoạch triển khai kỹ thuật sau khi ký hợp tác."""
replacement_tracking_rule = """    * ⛔ **CẤM ĐƯA LỖI THIẾU TRACKING ADS / GTM LÀM ĐIỂM NGHẼN WEBSITE TRƯỚC HỢP ĐỒNG:** Giai đoạn audit trước khi nhận dự án, website chưa chạy Ads thì việc chưa cài thẻ theo dõi chuyển đổi Google Ads (GTM Tag) là điều hiển nhiên. TUYỆT ĐỐI KHÔNG đưa vào làm lỗi chặn P0 của website trong bản trình bày khách hàng. Thiết lập tracking thuộc về kế hoạch triển khai kỹ thuật sau khi ký hợp tác.
    * ⛔ **BẮT BUỘC SOI VÀ ĐƯA LỖI CỤM NÚT LIÊN HỆ NỔI (FLOATING CONTACT BAR) ĐÈ CHỮ TRÊN DESKTOP VÀO P0:** Khi audit giao diện desktop, bắt buộc rà soát xem cụm widget Zalo/Hotline/WhatsApp nổi bên trái hoặc phải màn hình có bị đè lên tiêu đề H1 hay văn bản giới thiệu chính không. Nếu có, đây là lỗi chặn P0 khẩn cấp bắt buộc chụp ảnh bằng chứng và đưa lên Card 1 của Mục 2."""

if target_tracking_rule in text:
    text = text.replace(target_tracking_rule, replacement_tracking_rule, 1)
    print("Added Floating Contact Bar check in LUỒNG 1!")
else:
    print("Warning: target_tracking_rule not found in SKILL.md!")

# 3. Add Master Skeleton Template Enforcement under File 2
target_file2_header = """2. **File 2 — Bản Trình Bày Khách Hàng (`Bao_Cao_Trinh_Bay_Khach_Hang_{domain}.html`):**
   - Dành cho khách hàng, chủ doanh nghiệp, ban giám đốc (người không chuyên kỹ thuật).
   - **BỘ KHUNG 5 MỤC CHUẨN HÓA CỐ ĐỊNH (THE 5-SECTION MASTER TEMPLATE):**"""

replacement_file2_header = """2. **File 2 — Bản Trình Bày Khách Hàng (`Bao_Cao_Trinh_Bay_Khach_Hang_{domain}.html`):**
   - Dành cho khách hàng, chủ doanh nghiệp, ban giám đốc (người không chuyên kỹ thuật).
   - **🔒 KHÓA CỨNG MẪU KHUNG HTML GỐC (MASTER SKELETON TEMPLATE ENFORCEMENT):**
     * **Tập tin khung chuẩn:** `website-audit-core/templates/template_client_presentation_master.html`.
     * **Quy tắc tuyệt đối:** AI BẮT BUỘC đọc và kế thừa 100% từ file `template_client_presentation_master.html` khi render file HTML báo cáo khách hàng.
     * **CẤM TỰ Ý CODE LẠI HTML TỪ ĐẦU:** Chỉ được phép thay thế nội dung dữ liệu động (Tên thương hiệu, Domain, Ảnh chụp, Bảng điểm nghẽn, Sitemap, Blueprint) vào các thẻ tương ứng. Giữ nguyên 100% cấu trúc thẻ `<header>` (sticky, zero CTA), thẻ `<aside>` (Single Sidebar 270px, icon Lucide, không box helper chân trang), class typography `<h2>` (không viên nhộng), hệ thống Lightbox và thanh Mobile Floating Quick-Nav bar.
   - **BỘ KHUNG 5 MỤC CHUẨN HÓA CỐ ĐỊNH (THE 5-SECTION MASTER TEMPLATE):**"""

if target_file2_header in text:
    text = text.replace(target_file2_header, replacement_file2_header, 1)
    print("Added Master Skeleton Template Enforcement under File 2!")
else:
    print("Warning: target_file2_header not found in SKILL.md!")

with open(skill_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated SKILL.md successfully!")
