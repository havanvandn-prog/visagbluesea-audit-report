import sys

sys.stdout.reconfigure(encoding='utf-8')

rule_path = r'C:\Users\ADMIN\.gemini\config\rules\quy-chuan-audit-google-ads-khong-dua-seo.md'
with open(rule_path, 'r', encoding='utf-8') as f:
    text = f.read()

pill_rule = """
---

## 7. Điều Khoản Khóa Cứng: Cấm Chèn Thanh Gạch Màu / Viên Nhộng Trước Tiêu Đề Section (No-Heading-Accent-Bar Directive)

### A. Quy định bắt buộc đối với tiêu đề Section (Heading H2)
- Trên tiêu đề của các Section (`<h2>`):
  - **TUYỆT ĐỐI CẤM chèn các thanh gạch màu dọc, viên nhộng bo tròn** (như `<span class="w-2.5 h-6 bg-red-600 rounded-full inline-block"></span>` hay các màu amber, indigo, blue, emerald) đứng trước số thứ tự và tên đề mục.
  - Tiêu đề Section phải hiển thị thuần typography sạch sẽ, chỉ dùng font chữ đậm sắc nét (`text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight`).

### B. Lý do chuyên môn & Thẩm mỹ giao diện
- Các "cục" màu này là tàn dư thiết kế lỗi thời, tạo cảm giác chắp vá, vướng mắt và làm rối loạn tầm nhìn khi người dùng quét nhanh nội dung.
- Thiết kế hiện đại Easy AI ưu tiên sự thanh thoát, liền mạch và tập trung 100% vào nội dung chữ.
"""

if "No-Heading-Accent-Bar Directive" not in text:
    text += pill_rule
    with open(rule_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated rule file with No-Heading-Accent-Bar Directive successfully!")
else:
    print("Rule already contains No-Heading-Accent-Bar Directive!")
