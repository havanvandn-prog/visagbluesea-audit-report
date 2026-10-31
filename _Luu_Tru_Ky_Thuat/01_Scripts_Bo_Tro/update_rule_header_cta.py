import sys

sys.stdout.reconfigure(encoding='utf-8')

rule_path = r'C:\Users\ADMIN\.gemini\config\rules\quy-chuan-audit-google-ads-khong-dua-seo.md'
with open(rule_path, 'r', encoding='utf-8') as f:
    text = f.read()

cta_rule = """
---

## 4. Điều Khoản Khóa Cứng: Thanh Header Sạch Sẽ, Không Gắn CTA (Zero-Header-CTA Directive)

### A. Quy định bắt buộc đối với thanh Header trên bản trình bày khách hàng
- Trên thanh Header cố định (`<header class="fixed top-0...">`) của file trình bày khách hàng (`Bao_Cao_Trinh_Bay_Khach_Hang_*.html`):
  - **CẤM gắn nút chuyển sang file kỹ thuật nội bộ Dev:** Tuyệt đối không để nút như `Bản Kỹ Thuật Dev`, `Báo Cáo Kỹ Thuật Nội Bộ` hay link dẫn sang file dev/agency.
  - **CẤM gắn nút kêu gọi hành động (CTA) hoặc nút tải file trên Header:** Không chèn nút `Tải File Excel`, `Tải Báo Cáo`, `Đặt Lịch Hẹn` hay bất kỳ nút CTA nào lên thanh Header cố định.

### B. Lý do chuyên môn & Trải nghiệm người dùng
- Bản trình bày khách hàng là tài liệu kiểm toán, thẩm định độc lập. Đưa nút Dev là vi phạm bảo mật/phân tách nội bộ.
- Các nút CTA trên Header cố định chiếm diện tích, làm phân mảnh sự chú ý và dễ gây lỗi tràn viền hoặc nhảy dòng trên màn hình hẹp/mobile.
- Thanh Header chỉ hiển thị nhận diện thương hiệu tinh gọn: Logo thương hiệu, Tên cổng thẩm định, Tên website đối soát và Nhãn trạng thái `Thẩm Định Độc Lập`.
"""

if "Zero-Header-CTA Directive" not in text:
    text += cta_rule
    with open(rule_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated rule file with Zero-Header-CTA Directive successfully!")
else:
    print("Rule already contains Zero-Header-CTA Directive!")
