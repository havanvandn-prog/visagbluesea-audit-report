import sys

sys.stdout.reconfigure(encoding='utf-8')

skill_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\SKILL.md'
with open(skill_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = """   - **Quy tắc biên soạn vàng:**
     + **Rút ngắn câu từ:**"""

replacement = """   - **Quy tắc biên soạn vàng:**
     + **⛔ KHÓA CỨNG: THANH HEADER SẠCH SẼ, TUYỆT ĐỐI KHÔNG GẮN NÚT CTA (ZERO-HEADER-CTA DIRECTIVE):**
       - Trên thanh Header cố định (Top Header) của bản trình bày khách hàng (`Bao_Cao_Trinh_Bay_Khach_Hang_{domain}.html`): TUYỆT ĐỐI KHÔNG đính kèm bất kỳ nút kêu gọi hành động (CTA), nút tải file hay nút điều hướng kỹ thuật nào (như 'Tải File Excel', 'Bản Kỹ Thuật Dev').
       - **Lý do chuyên môn:** Bản trình bày gửi khách là tài liệu thẩm định độc lập. Đưa nút 'Bản Kỹ Thuật Dev' là vi phạm nghiêm trọng tính bảo mật và phân tách tài liệu nội bộ; còn nút tải file hay nút CTA trên Header làm rối mắt, che khuất tầm nhìn và gây xao nhãng người đọc khi cuộn trang.
       - **Quy chuẩn Header:** Thanh Header chỉ giữ lại nhận diện thương hiệu tinh gọn: Logo thương hiệu, Tên cổng thẩm định, Link đối soát website và Tag trạng thái 'Thẩm Định Độc Lập'.
     + **Rút ngắn câu từ:**"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated SKILL.md with ZERO-HEADER-CTA DIRECTIVE successfully!")
else:
    print("Target not found in SKILL.md!")
