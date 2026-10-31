import sys

sys.stdout.reconfigure(encoding='utf-8')

skill_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\SKILL.md'
with open(skill_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = """     + **⛔ CẤM ĐƯA BOX 'THẨM ĐỊNH ĐỘC LẬP' VÀO CHÂN SIDEBAR (NO-SIDEBAR-HELPER-CARD DIRECTIVE):**"""

replacement = """     + **⛔ CẤU TRÚC SIDEBAR ĐƠN NHẤT HÓA (SINGLE UNIFIED SIDEBAR DIRECTIVE):**
       - Trên giao diện máy tính (Desktop): TUYỆT ĐỐI KHÔNG chia tách thành 2 thanh Sidebar song song (Mini Rail 60px + Sub-Sidebar 280px).
       - BẮT BUỘC gộp Icon nhận diện trực tiếp vào từng tên đề mục trong DUY NHẤT 1 thanh Sidebar (`w-[270px]`): Cấu trúc từng dòng là `[Icon] [Số thứ tự + Tên đề mục] [Badge số đếm]`.
       - Container nội dung chính (`<main>`): Đặt lề lùi `md:ml-[270px]`, giúp giải phóng thêm 70px - 80px không gian bề ngang cho các bảng dữ liệu và khối ảnh đối sánh Before/After.
     + **⛔ CẤM ĐƯA BOX 'THẨM ĐỊNH ĐỘC LẬP' VÀO CHÂN SIDEBAR (NO-SIDEBAR-HELPER-CARD DIRECTIVE):**"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated SKILL.md with SINGLE UNIFIED SIDEBAR DIRECTIVE successfully!")
else:
    print("Target not found in SKILL.md!")
