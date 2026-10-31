import sys

sys.stdout.reconfigure(encoding='utf-8')

skill_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\SKILL.md'
with open(skill_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = """     + **⛔ KHÓA CỨNG: THANH HEADER SẠCH SẼ, TUYỆT ĐỐI KHÔNG GẮN NÚT CTA (ZERO-HEADER-CTA DIRECTIVE):**"""

replacement = """     + **⛔ CẤM ĐƯA BOX 'THẨM ĐỊNH ĐỘC LẬP' VÀO CHÂN SIDEBAR (NO-SIDEBAR-HELPER-CARD DIRECTIVE):**
       - Trên thanh Sub-Sidebar (Menu điều hướng bên trái) của bản trình bày khách hàng: TUYỆT ĐỐI KHÔNG đính kèm box 'Thẩm Định Độc Lập' (chứa text: *"Tài liệu đánh giá kỹ thuật trung lập gửi Ban Giám Đốc trước khi duyệt ngân sách quảng cáo"*).
       - **Lý do chuyên môn:** Box này là thông tin thừa thãi (developer/agency noise), làm rối mắt thanh điều hướng, chiếm diện tích trên màn hình máy tính bảng và laptop. Thanh Sidebar chỉ phục vụ mục đích DUY NHẤT: hiển thị danh sách các đề mục thẩm định một cách sạch sẽ, thanh lịch theo chuẩn Easy AI SaaS.
     + **⛔ KHÓA CỨNG: THANH HEADER SẠCH SẼ, TUYỆT ĐỐI KHÔNG GẮN NÚT CTA (ZERO-HEADER-CTA DIRECTIVE):**"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated SKILL.md with NO-SIDEBAR-HELPER-CARD DIRECTIVE successfully!")
else:
    print("Target not found in SKILL.md!")
