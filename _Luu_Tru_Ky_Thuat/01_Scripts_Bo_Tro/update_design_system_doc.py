import sys

sys.stdout.reconfigure(encoding='utf-8')
design_doc_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\website-audit-core\templates\client-report-design-system.md'

new_content = """# CLIENT REPORT DESIGN SYSTEM — EASY AI MASTER SPEC (V3.6)

## 1. Mục Tiêu Cốt Lõi
Bản Trình Bày Khách Hàng (`Bao_Cao_Trinh_Bay_Khach_Hang_{domain}.html`) là tài liệu thẩm định độc lập chuẩn doanh nghiệp cao cấp dành cho Chủ doanh nghiệp và Ban Giám Đốc. Báo cáo tập trung 100% vào năng lực chuyển đổi website (CRO, UI/UX, Bố cục, Điểm nghẽn, Sitemap & Blueprint) trước khi chạy tiếp thị trả phí.

---

## 2. Quy Chuẩn Khung Mẫu Bắt Buộc (Mandatory Master Template)
- **Tập tin khung chuẩn:** `website-audit-core/templates/template_client_presentation_master.html`.
- **Nguyên tắc khóa cứng:** Mọi dự án audit website BẮT BUỘC sử dụng tập tin khung mẫu này để render dữ liệu. TUYỆT ĐỐI KHÔNG tự ý code lại HTML từ đầu hoặc thay đổi class CSS layout.

---

## 3. Quy Chuẩn Giao Diện Desktop (Header, Sidebar & Typography)

### A. Header Cố Định Tinh Gọn (Sticky & Zero-Header-CTA Directive)
- **Vị trí:** Cố định đỉnh màn hình: `fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 h-14`.
- **Nội dung:** Duy nhất Logo nhận diện, Tên cổng portal, Link kiểm chứng website thực tế và Tag trạng thái "Thẩm Định Độc Lập".
- **Khóa cứng:** TUYỆT ĐỐI KHÔNG gắn nút CTA (nút tải Excel, nút xem bản kỹ thuật dev, nút liên hệ) trên Header.

### B. 1 Sidebar Duy Nhất (Single Unified Sidebar 270px)
- **Cấu trúc:** 1 thanh Sidebar duy nhất cố định bên trái rộng 270px (`fixed top-14 left-0 bottom-0 w-[270px] bg-slate-50/80 border-r border-slate-200 p-3`).
- **Nội dung:** Gộp icon Lucide trực tiếp vào trước tên từng đề mục: `[Icon Lucide] [Số thứ tự + Tên mục] [Badge số lượng]`.
- **Nội dung chính:** Lùi lề chính xác `md:ml-[270px]`.
- **Khóa cứng:** Xóa bỏ hoàn toàn Mini Rail 60px phân tách. Chân Sidebar tuyệt đối không chèn box helper hay card thừa ("Thẩm Định Độc Lập" ở chân sidebar).

### C. Tiêu Đề Section Thuần Khiết (No-Heading-Accent-Bar Directive)
- **Typography:** `text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight`.
- **Khóa cứng:** TUYỆT ĐỐI KHÔNG chèn thanh gạch màu hay viên nhộng bo tròn (`<span class="w-2.5 h-6 bg-... rounded-full"></span>`) đứng trước `<h2>`.

---

## 4. Bộ Khung 5 Mục Cốt Lõi Khóa Cứng (The 5-Section Master Template)
1. **Mục 1 — Bức Tranh Tổng Thể (Executive KPI Stat Cards):** 4 chỉ số cấp cao (CVR hiện tại, Mục tiêu sau tối ưu, Lỗi chặn P0 khẩn cấp, % Tiết kiệm chi phí Ads).
2. **Mục 2 — Các Điểm Nghẽn Thất Thoát & Đối Sánh Trực Quan (Trước / Sau):** Tích hợp trực tiếp khối ảnh Hiện trạng (❌) vs Đề xuất (✨) vào ngay bên dưới từng Card Điểm nghẽn P0 tương ứng. Không tách thành mục độc lập. Bắt buộc rà soát lỗi Cụm nút liên hệ nổi (Floating Contact Bar) đè chữ trên Desktop.
3. **Mục 3 — Bảng Tổng Hợp Khuyến Nghị Theo Thứ Tự Ưu Tiên (P0 – P2):** Phân cấp P0 (Khẩn), P1 (Cần sớm), P2 (Nâng cao). Desktop hiển thị Table kèm bộ lọc tab; Mobile tự động chuyển thành Card Stack với nút "Soi lỗi" dạng pill min-h-[36px].
4. **Mục 4 — Kiến Trúc Sitemap Mục Tiêu & Định Vị Trung Tâm Báo Giá (RFQ Hub):** Bản đồ Sitemap phân nhóm rõ ràng và mô hình RFQ Hub chốt khách VIP. TUYỆT ĐỐI KHÔNG đưa bảng ma trận URL mapping (301/410) vào mục này.
5. **Mục 5 — Cấu Trúc Bố Cục Từng Khối (Blueprint Section-by-Section chuẩn CRO):** Blueprint 7 khối chuẩn tối ưu chuyển đổi kèm copy mẫu, form đăng ký và cam kết dịch vụ.

---

## 5. Tách Bạch Báo Cáo (Separation of Concerns Directive)
- **Không đưa mục vận hành Google Ads vào trang này:** Toàn bộ phần chiến lược Google Ads (Plan, Từ khóa, Ngân sách, Phân nhóm, Phủ định) sẽ được trình bày ở bộ tài liệu/báo cáo Google Ads riêng biệt.
- **Không đưa bảng kỹ thuật URL Mapping (301, 410) vào trang này:** Toàn bộ bảng ma trận chuyển hướng URL 100% chỉ lưu trong **Sheet 4 File Excel** và **Báo Cáo Kỹ Thuật Nội Bộ cho Dev**.

---

## 6. Trải Nghiệm Mobile & Cảm Ứng (/UI-kiem-tra-reponsive)
- Nút bấm và touch targets trên mobile phải $\ge 36px$ hoặc $38px$ (nâng cấp link "Soi lỗi" thành nút pill).
- Mobile Floating Quick-Nav Bar (`fixed bottom-3 left-3 right-3 z-40 md:hidden`) với các nút chuyển mục nhanh và nút cuộn lên đầu trang, tích hợp chuẩn `safe-area-inset-bottom`.
- Bổ sung nhãn trực quan **"🔍 Chạm phóng to"** ở góc dưới các ảnh để người dùng mobile biết có thể chạm mở Lightbox.
- Bảng dữ liệu nhiều cột bắt buộc bọc trong container `overflow-x-auto no-scrollbar` kèm chỉ báo vuốt ngang.
"""

with open(design_doc_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated client-report-design-system.md successfully!")
