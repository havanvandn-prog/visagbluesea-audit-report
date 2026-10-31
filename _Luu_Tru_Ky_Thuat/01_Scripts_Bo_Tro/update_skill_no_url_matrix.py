import sys

sys.stdout.reconfigure(encoding='utf-8')
skill_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\SKILL.md'

with open(skill_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = """     + **Responsive Mobile Guard 100%:** Tuyệt đối không để vỡ giao diện hay tràn ngang màn hình điện thoại khi khách mở xem trên smartphone."""

replacement = """     + **Responsive Mobile Guard 100%:** Tuyệt đối không để vỡ giao diện hay tràn ngang màn hình điện thoại khi khách mở xem trên smartphone.
     + **⛔ KHÓA CỨNG: TUYỆT ĐỐI KHÔNG ĐƯA MA TRẬN ÁNH XẠ ĐƯỜNG DẪN (URL MAPPING MATRIX) VÀ MÃ KỸ THUẬT VÀO BẢN TRÌNH BÀY KHÁCH HÀNG (ZERO-URL-MAPPING-MATRIX DIRECTIVE):**
       - Trên bản trình bày khách hàng (`Bao_Cao_Trinh_Bay_Khach_Hang_{domain}.html`): TUYỆT ĐỐI KHÔNG đính kèm bảng kỹ thuật "Ma Trận Xử Lý & Chuẩn Hóa Đường Dẫn" (URL Mapping Matrix) chứa các slug cũ/mới, mã HTTP (301 Redirect, 410 Gone, rewrite rule...).
       - **Lý do kinh doanh cốt lõi:** Khách hàng (Chủ doanh nghiệp, Ban Giám Đốc) hoàn toàn không hiểu và không quan tâm mã HTTP 301/410 hay slug kỹ thuật. Bảng này biến tài liệu chiến lược thành bảng code của lập trình viên, làm loãng sự chú ý khỏi 2 giá trị cốt lõi là Kiến Trúc Sitemap và Trung Tâm Báo Giá (RFQ Hub).
       - **Nơi lưu trữ chuẩn:** Bảng Ma Trận URL Mapping kỹ thuật 100% chỉ được lưu trong **Sheet 4 của File Excel (`Du_Lieu_Trien_Khai_Chi_Tiet_{domain}.xlsx`)** và **Báo Cáo Kỹ Thuật Nội Bộ (`Bao_Cao_Ky_Thuat_Noi_Bo_{domain}.html`)** để bàn giao cho đội ngũ Lập trình viên (Dev / Webmaster) thực thi."""

if target in text:
    text = text.replace(target, replacement, 1)
    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated SKILL.md with ZERO-URL-MAPPING-MATRIX DIRECTIVE successfully!")
else:
    print("Target not found in SKILL.md!")
