import sys

sys.stdout.reconfigure(encoding='utf-8')
design_doc_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\website-audit-core\templates\client-report-design-system.md'

with open(design_doc_path, 'r', encoding='utf-8') as f:
    text = f.read()

old_header_spec = """### A. Header Cố Định Tinh Gọn (Sticky & Zero-Header-CTA Directive)
- **Vị trí:** Cố định đỉnh màn hình: `fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 h-14`.
- **Nội dung:** Duy nhất Logo nhận diện, Tên cổng portal, Link kiểm chứng website thực tế và Tag trạng thái "Thẩm Định Độc Lập".
- **Khóa cứng:** TUYỆT ĐỐI KHÔNG gắn nút CTA (nút tải Excel, nút xem bản kỹ thuật dev, nút liên hệ) trên Header."""

new_header_spec = """### A. Header Cố Định Tinh Gọn & Siêu Sạch (Sticky & Zero-Header-CTA & Zero-Status-Pill Directive)
- **Vị trí:** Cố định đỉnh màn hình: `fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 h-14`.
- **Nội dung:** Tối giản tuyệt đối, CHỈ gồm: Logo nhận diện thương hiệu (hình vuông bo tròn `rounded-xl`), Tên cổng portal (`font-extrabold`) và Link kiểm chứng website thực tế (`Đối soát: domain ↗`). Phía bên phải hiển thị tên domain tinh tế hoặc để trống thoáng đãng.
- **Khóa cứng cấm triệt để:** 
  1. TUYỆT ĐỐI KHÔNG gắn nút CTA (nút tải file, nút xem bản kỹ thuật dev, nút liên hệ).
  2. TUYỆT ĐỐI KHÔNG chèn các tag trạng thái râu ria, vô nghĩa (như 'Thẩm Định Độc Lập 2026', 'Active', 'Live', dot xanh animate-ping) làm rối mắt và biến giao diện thành mẫu AI generic (AI slop)."""

if old_header_spec in text:
    text = text.replace(old_header_spec, new_header_spec, 1)
    with open(design_doc_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated client-report-design-system.md successfully!")
else:
    print("Warning: old_header_spec not found in client-report-design-system.md!")
