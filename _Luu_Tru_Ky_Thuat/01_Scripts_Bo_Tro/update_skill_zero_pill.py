import sys

sys.stdout.reconfigure(encoding='utf-8')
skill_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\SKILL.md'

with open(skill_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Header spec under Zero-Header-CTA Directive
target_header = """       - **Quy chuẩn Header:** Thanh Header chỉ giữ lại nhận diện thương hiệu tinh gọn: Logo thương hiệu, Tên cổng thẩm định, Link đối soát website và Tag trạng thái 'Thẩm Định Độc Lập'."""
replacement_header = """       - **Quy chuẩn Header (Zero-CTA & Zero-Status-Pill Directive):** Thanh Header siêu sạch, tối giản tuyệt đối: CHỈ giữ lại nhận diện thương hiệu gồm Logo thương hiệu, Tên cổng thẩm định và Link đối soát website (`Đối soát: domain ↗`). TUYỆT ĐỐI KHÔNG chèn thêm các tag trạng thái vô nghĩa (như 'Thẩm Định Độc Lập', '2026', 'Active', 'Live', dot xanh animate-ping) làm rối mắt và mang dáng dấp AI generic."""

if target_header in text:
    text = text.replace(target_header, replacement_header, 1)
    print("Updated Header rule in SKILL.md successfully!")
else:
    print("Warning: target_header not found in SKILL.md!")

# 2. Update Cổng 4 in SKILL.md
target_gate4 = """       1. Header: Ghim cố định `fixed top-0`, TUYỆT ĐỐI không có button/link CTA hay nút tải file."""
replacement_gate4 = """       1. Header: Ghim cố định `fixed top-0`, TUYỆT ĐỐI không có button/link CTA hay nút tải file, TUYỆT ĐỐI không có tag trạng thái râu ria vô nghĩa (như 'Thẩm Định Độc Lập', dot ping xanh animate-ping)."""

if target_gate4 in text:
    text = text.replace(target_gate4, replacement_gate4, 1)
    print("Updated Cổng 4 in SKILL.md successfully!")
else:
    print("Warning: target_gate4 not found in SKILL.md!")

with open(skill_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved SKILL.md successfully!")
