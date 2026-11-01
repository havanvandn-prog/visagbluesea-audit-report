import sys

sys.stdout.reconfigure(encoding='utf-8')
rule_path = r'C:\Users\ADMIN\.gemini\config\rules\business-first-language.md'

with open(rule_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = """- Xây dựng SaaS/UI: dùng nhãn, nút bấm và hướng dẫn ngắn, rõ hành động. Thông báo lỗi cần nói điều gì đã xảy ra và người dùng nên làm gì tiếp theo. Phân biệt nội dung cho khách hàng với tài liệu kỹ thuật dành cho lập trình viên."""

replacement = """- Xây dựng SaaS/UI: dùng nhãn, nút bấm và hướng dẫn ngắn, rõ hành động. Thông báo lỗi cần nói điều gì đã xảy ra và người dùng nên làm gì tiếp theo. Phân biệt nội dung cho khách hàng với tài liệu kỹ thuật dành cho lập trình viên.
- Không tạo các tag trạng thái hoặc badge trang trí vô nghĩa (Zero AI Slop Badges): Tuyệt đối không thêm các viên nhộng giả lập live status như "Thẩm Định Độc Lập 2026", "Active", "Live" kèm hiệu ứng nhấp nháy (dot animate-ping) trên thanh Header. Giữ giao diện tinh gọn, sạch sẽ, chỉ hiển thị thông tin nhận diện cốt lõi."""

if target in text:
    text = text.replace(target, replacement, 1)
    with open(rule_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated business-first-language.md successfully!")
else:
    print("Warning: target not found in business-first-language.md!")
