import sys

sys.stdout.reconfigure(encoding='utf-8')
skill_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\SKILL.md'

with open(skill_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Mini Icon Rail to Single Unified Sidebar in Section 7
old_mini_rail = """     * **Thanh điều hướng (Sidebar/Mini Rail):** Cố định bên trái hoặc thanh điều hướng bo tròn chuẩn Easy AI, BẮT BUỘC mang tông màu thương hiệu Emerald Green (`#01a915`), tuyệt đối KHÔNG dùng màu xanh dương hoặc xám lạc quẻ.
     * **Desktop:** Mini Icon Rail (60px cố định bên trái) với tooltip trượt ngang + Header Topbar (56px) tinh gọn + Container Max-width 1280px căn giữa.
     * **Mobile:** Bottom Navigation Bar Native (`fixed bottom-0 z-40 bg-white/95 backdrop-blur-md`) + Fixed Sticky Action Bar hỗ trợ Thumb Zone (Gọi Ngay + Zalo Báo Giá 24/7)."""

new_sidebar_spec = """     * **Thanh điều hướng (Single Unified Sidebar 270px):** Cố định bên trái chuẩn Easy AI SaaS, BẮT BUỘC mang tông màu thương hiệu Emerald Green (`#01a915`).
     * **Desktop:** 1 Sidebar duy nhất (w-[270px] cố định bên trái) tích hợp trực tiếp Icon trước tên từng đề mục, không dùng Mini Rail 60px phân tách + Header Topbar (56px) sticky tinh gọn + Container Max-width 1280px lùi lề `md:ml-[270px]`. Chân sidebar sạch sẽ, tuyệt đối không chèn box helper hay card thừa.
     * **Mobile:** Mobile Floating Quick-Nav Bar (`fixed bottom-3 left-3 right-3 z-40 md:hidden`) với 4-5 nút chuyển mục nhanh và nút cuộn lên đầu trang, hỗ trợ safe-area-inset-bottom."""

if old_mini_rail in text:
    text = text.replace(old_mini_rail, new_sidebar_spec)
    print("Updated Desktop sidebar spec in SKILL.md successfully!")
else:
    print("Warning: old_mini_rail not found in SKILL.md!")

# 2. Update File 2 description in Lớp 1 to enforce 5-section master template
old_file2_intro = """2. **File 2 — Bản Trình Bày Khách Hàng (`Bao_Cao_Trinh_Bay_Khach_Hang_{domain}.html`):**
   - Dành cho khách hàng, chủ doanh nghiệp, ban giám đốc (người không chuyên kỹ thuật).
   - **BẮT BUỘC TÍCH HỢP TRỌN BỘ 2 PHẦN KIẾN TRÚC & BLUEPRINT GIẢI PHÁP:**
     * **Mục Kiến Trúc Sitemap Mục Tiêu & Ma Trận Xử Lý URL:** Trình bày chi tiết bảng ánh xạ URL cũ → Hành động (Giữ/301/Tạo mới) → URL mới → Intent → Mục tiêu chuyển đổi.
     * **Mục Cấu Trúc Section Chi Tiết Toàn Bộ 5–8 Trang Lõi (Blueprint Section-by-Section):** Trình bày trực quan, cuộn dọc liên tục (Continuous Layout), bóc tách từng section kèm copywriter mẫu và thành phần UX.
     * **Tư Vấn Tối Ưu Chi Phí Thiết Kế:** Phân loại rõ ràng trang nào nên dựng dạng Landing Page (custom CRO cao) và trang nào chỉ cần dựng theo template Bài Viết Chuẩn SEO (dynamic post) để tối ưu ngân sách cho khách hàng.
     * **Định vị RFQ Hub:** Làm rõ sự khác biệt giữa Trang Chi Tiết Sản Phẩm (datasheet tra cứu) và Trung Tâm Báo Giá Dự Án (RFQ Hub - điểm chốt đơn B2B tối hậu)."""

new_file2_intro = """2. **File 2 — Bản Trình Bày Khách Hàng (`Bao_Cao_Trinh_Bay_Khach_Hang_{domain}.html`):**
   - Dành cho khách hàng, chủ doanh nghiệp, ban giám đốc (người không chuyên kỹ thuật).
   - **BỘ KHUNG 5 MỤC CHUẨN HÓA CỐ ĐỊNH (THE 5-SECTION MASTER TEMPLATE):**
     * **Mục 1: Bức Tranh Tổng Thể (Executive KPI Stat Cards):** 4 chỉ số cấp cao (CVR hiện tại, Mục tiêu sau tối ưu, Lỗi chặn P0 khẩn cấp, % Tiết kiệm chi phí Ads).
     * **Mục 2: Các Điểm Nghẽn Thất Thoát & Đối Sánh Trực Quan (Trước / Sau):** Tích hợp trực tiếp khối ảnh đối sánh Hiện trạng (❌) vs Đề xuất (✨) vào ngay bên dưới từng Card Điểm nghẽn P0 tương ứng. Không tách thành mục độc lập. Bắt buộc rà soát lỗi Cụm nút liên hệ nổi (Floating Contact Bar) đè chữ trên Desktop.
     * **Mục 3: Bảng Tổng Hợp Khuyến Nghị Theo Thứ Tự Ưu Tiên (P0 – P2):** Phân cấp P0 (Khẩn), P1 (Cần sớm), P2 (Nâng cao). Desktop hiển thị Table kèm bộ lọc tab; Mobile tự động chuyển thành Card Stack với nút "Soi lỗi" dạng pill min-h-[36px].
     * **Mục 4: Kiến Trúc Sitemap Mục Tiêu & Định Vị Trung Tâm Báo Giá (RFQ Hub):** Bản đồ Sitemap phân nhóm rõ ràng và mô hình RFQ Hub chốt khách VIP. TUYỆT ĐỐI KHÔNG đưa bảng ma trận URL mapping (301/410) vào mục này.
     * **Mục 5: Cấu Trúc Bố Cục Từng Khối (Blueprint Section-by-Section chuẩn CRO):** Blueprint 7 khối chuẩn tối ưu chuyển đổi kèm copy mẫu, form đăng ký và cam kết dịch vụ.
   - **TUYỆT ĐỐI KHÔNG đưa phần tư vấn hay khuyến nghị vận hành Google Ads vào trang này:** Toàn bộ phần chiến lược Google Ads (Plan, Từ khóa, Ngân sách) sẽ xuất ở bộ tài liệu/báo cáo Google Ads riêng biệt."""

if old_file2_intro in text:
    text = text.replace(old_file2_intro, new_file2_intro)
    print("Updated File 2 5-section master template in SKILL.md successfully!")
else:
    print("Warning: old_file2_intro not found in SKILL.md!")

with open(skill_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved SKILL.md successfully!")
