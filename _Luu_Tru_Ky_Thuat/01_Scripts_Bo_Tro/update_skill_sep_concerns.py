import sys

sys.stdout.reconfigure(encoding='utf-8')
skill_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\SKILL.md'

with open(skill_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = """     + **Đẩy thông tin Google Ads xuống dưới cùng:** Vì Google Ads chỉ là phương án mở rộng/thêm, toàn bộ thông tin và lưu ý về Google Ads trong file HTML gửi khách hàng BẮT BUỘC phải được đẩy xuống mục mở rộng ở DƯỚI CÙNG của báo cáo, nhường toàn bộ phần đầu cho Sức khỏe Website, Trải nghiệm người dùng (UI/UX), Tối ưu chuyển đổi và Nền tảng SEO."""

replacement = """     + **Tách bạch Báo cáo Website CRO và Báo cáo Chiến Lược Google Ads (Separation of Concerns Directive):**
       - Khi nhiệm vụ là tối ưu website/landing page trước khi chạy ads, bản trình bày khách hàng (`Bao_Cao_Trinh_Bay_Khach_Hang_{domain}.html`) BẮT BUỘC tập trung 100% vào năng lực chuyển đổi của website (Bức Tranh Tổng Thể, Điểm Nghẽn Chuyển Đổi, Bảng Khuyến Nghị Ưu Tiên, Sitemap & RFQ Hub, Blueprint Section-by-Section).
       - **TUYỆT ĐỐI KHÔNG đưa phần tư vấn hay khuyến nghị vận hành chiến dịch Google Ads vào trang này** nếu người dùng phân tách tài liệu. Toàn bộ phần chiến lược Google Ads (Plan, Từ khóa, Ngân sách, Phân nhóm, Phủ định) sẽ được trình bày ở bộ tài liệu/báo cáo Google Ads riêng biệt."""

if target in text:
    text = text.replace(target, replacement, 1)
    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated SKILL.md with Separation of Concerns Directive successfully!")
else:
    print("Target not found in SKILL.md!")
