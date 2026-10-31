import sys

sys.stdout.reconfigure(encoding='utf-8')

rule_path = r'C:\Users\ADMIN\.gemini\config\rules\quy-chuan-audit-google-ads-khong-dua-seo.md'
with open(rule_path, 'r', encoding='utf-8') as f:
    text = f.read()

sidebar_rule = """
---

## 6. Điều Khoản Khóa Cứng: Cấu Trúc Sidebar Đơn Nhất Hóa (Single Unified Sidebar Directive)

### A. Quy định bắt buộc đối với thanh điều hướng Desktop
- **CẤM chia tách thành 2 Sidebar song song (Mini Rail 60px + Sub-Sidebar 280px):** Tuyệt đối không dùng mô hình 2-tier sidebar khiến màn hình bị chiếm dụng tới 340px bề ngang và gây phân mảnh thị giác.
- **BẮT BUỘC dùng 1 Sidebar đơn nhất (Single Unified Sidebar):**
  - Chiều rộng cố định: `w-[260px]` hoặc `w-[270px]`.
  - Cấu trúc từng mục điều hướng: **[Icon nhận diện] + [Số thứ tự & Tên đề mục] + [Badge số đếm]**.
  - Phần thân nội dung (`<main>`): Lùi đúng lề `md:ml-[270px]` để giải phóng tối đa không gian cho bảng biểu và các khối ảnh đối sánh Before/After hiển thị rộng rãi, sắc nét.
"""

if "Single Unified Sidebar Directive" not in text:
    text += sidebar_rule
    with open(rule_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated rule file with Single Unified Sidebar Directive successfully!")
else:
    print("Rule already contains Single Unified Sidebar Directive!")
