import sys

sys.stdout.reconfigure(encoding='utf-8')
rule_path = r'C:\Users\ADMIN\.gemini\config\rules\business-first-language.md'

with open(rule_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = """- Góc nhìn báo cáo gửi khách hàng: đóng vai trò là tài liệu thẩm định độc lập; tuyệt đối không đưa các câu hỏi hay băn khoăn nội bộ agency (như "có nên nhận chạy hay không", "rủi ro nếu nhận dự án") vào nội dung gửi khách. Tập trung đánh giá thực trạng website, các điểm nghẽn chuyển đổi và giải pháp hoàn thiện."""

replacement = """- Góc nhìn báo cáo gửi khách hàng: đóng vai trò là tài liệu thẩm định độc lập; tuyệt đối không đưa các câu hỏi hay băn khoăn nội bộ agency (như "có nên nhận chạy hay không", "rủi ro nếu nhận dự án") vào nội dung gửi khách. Tập trung đánh giá thực trạng website, các điểm nghẽn chuyển đổi và giải pháp hoàn thiện.
- Không đưa ma trận kỹ thuật (URL mapping, mã lỗi HTTP 301/410, rewrite rule) vào tài liệu gửi khách hàng: Người làm kinh doanh không hiểu và không quan tâm các mã chuyển hướng kỹ thuật này. Toàn bộ bảng ánh xạ đường dẫn URL kỹ thuật chỉ được lưu trong File Excel và Báo Cáo Kỹ Thuật Nội Bộ cho Lập trình viên (Dev)."""

if target in text:
    text = text.replace(target, replacement, 1)
    with open(rule_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated business-first-language.md successfully!")
else:
    print("Target not found in business-first-language.md!")
