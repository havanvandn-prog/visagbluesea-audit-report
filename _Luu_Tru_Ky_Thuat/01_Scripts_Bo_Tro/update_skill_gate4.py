import sys

sys.stdout.reconfigure(encoding='utf-8')
skill_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\SKILL.md'

with open(skill_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = """   - **Cổng 3 — Kiểm Định Cân Bằng Thẻ HTML & Chống Vỡ Layout (Anti-Broken Layout Gatekeeper):**
     * Trước khi đóng gói hoặc deploy, AI BẮT BUỘC chạy script kiểm định cân bằng thẻ HTML (`check_tags.py`).
     * Đối soát 100% số lượng thẻ mở và đóng (`<div>`, `<section>`, `<main>`), đảm bảo không có thẻ đóng dư thừa hay thiếu sót làm vỡ layout flex/grid ngang trên màn hình desktop. Báo cáo chỉ được coi là đạt chuẩn khi kết quả kiểm tra báo: `Total errors: 0, Unclosed tags: 0`."""

replacement = """   - **Cổng 3 — Kiểm Định Cân Bằng Thẻ HTML & Chống Vỡ Layout (Anti-Broken Layout Gatekeeper):**
     * Trước khi đóng gói hoặc deploy, AI BẮT BUỘC chạy script kiểm định cân bằng thẻ HTML (`check_tags.py`).
     * Đối soát 100% số lượng thẻ mở và đóng (`<div>`, `<section>`, `<main>`), đảm bảo không có thẻ đóng dư thừa hay thiếu sót làm vỡ layout flex/grid ngang trên màn hình desktop. Báo cáo chỉ được coi là đạt chuẩn khi kết quả kiểm tra báo: `Total errors: 0, Unclosed tags: 0`.
   - **Cổng 4 — Kiểm Định Chuẩn Mực Bố Cục Desktop & Báo Cáo 5 Mục (Layout Linter Gate):**
     * BẮT BUỘC chạy script kiểm định `verify_client_presentation_layout.py` trên bản trình bày khách hàng trước khi bàn giao.
     * **Tiêu chuẩn vượt cổng (Pass Criteria):**
       1. Header: Ghim cố định `fixed top-0`, TUYỆT ĐỐI không có button/link CTA hay nút tải file.
       2. Sidebar: 1 Sidebar duy nhất `w-[270px]`, lùi lề `md:ml-[270px]`, không có box helper thừa ở chân sidebar.
       3. Typography H2: Không chứa thanh gạch màu hay viên nhộng bo tròn (`span class="w-2.5 h-6 rounded-full"`).
       4. Cấu trúc: Đúng 5 mục chuẩn, TUYỆT ĐỐI không có bảng kỹ thuật URL Mapping 301/410 và không có mục vận hành Google Ads.
     * Kết quả bắt buộc: `✅ [LAYOUT GATE PASSED]`. Nếu vi phạm, AI phải tự động sửa ngay trước khi hoàn tất."""

if target in text:
    text = text.replace(target, replacement, 1)
    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added Cổng 4 to SKILL.md successfully!")
else:
    print("Target not found in SKILL.md!")
