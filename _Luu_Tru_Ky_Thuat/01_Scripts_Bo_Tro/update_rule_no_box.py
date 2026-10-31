import sys

sys.stdout.reconfigure(encoding='utf-8')

rule_path = r'C:\Users\ADMIN\.gemini\config\rules\quy-chuan-audit-google-ads-khong-dua-seo.md'
with open(rule_path, 'r', encoding='utf-8') as f:
    text = f.read()

box_rule = """
---

## 5. Điều Khoản Khóa Cứng: Cấm Đưa Box "Thẩm Định Độc Lập" Vào Chân Sidebar (No-Sidebar-Helper-Card Directive)

### A. Quy định bắt buộc đối với thanh Sidebar (Sub-Sidebar)
- Trên thanh menu điều hướng bên trái (`<aside class="... w-[280px] ...">`) của bản trình bày khách hàng:
  - **TUYỆT ĐỐI CẤM đính kèm card/box "Thẩm Định Độc Lập"** (chứa nội dung: *"Tài liệu đánh giá kỹ thuật trung lập gửi Ban Giám Đốc trước khi duyệt ngân sách quảng cáo"*).
  - Không thêm bất kỳ box helper, tooltip cố định, ghi chú hay khung thông tin nào ở chân Sidebar (`mt-auto`).

### B. Lý do chuyên môn & Trải nghiệm giao diện
- Đây là nội dung thừa (developer noise), làm rác không gian thị giác và gây cảm giác giáo điều.
- Thanh Sidebar phải được giữ sạch sẽ 100%, chỉ hiển thị danh mục các đề mục điều hướng kèm badge đếm số lượng tinh gọn chuẩn Easy AI SaaS.
"""

if "No-Sidebar-Helper-Card Directive" not in text:
    text += box_rule
    with open(rule_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated rule file with No-Sidebar-Helper-Card Directive successfully!")
else:
    print("Rule already contains No-Sidebar-Helper-Card Directive!")
