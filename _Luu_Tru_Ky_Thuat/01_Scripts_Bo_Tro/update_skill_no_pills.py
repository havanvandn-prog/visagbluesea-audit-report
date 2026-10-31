import sys

sys.stdout.reconfigure(encoding='utf-8')

skill_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\SKILL.md'
with open(skill_path, 'r', encoding='utf-8') as f:
    text = f.read()

target = """     + **⛔ CẤU TRÚC SIDEBAR ĐƠN NHẤT HÓA (SINGLE UNIFIED SIDEBAR DIRECTIVE):**"""

replacement = """     + **⛔ TUYỆT ĐỐI KHÔNG DÙNG THANH GẠCH MÀU / VIÊN NHỘNG TRƯỚC TIÊU ĐỀ (NO-HEADING-ACCENT-BAR DIRECTIVE):**
       - Trên các tiêu đề chính của từng Section (`<h2>`): TUYỆT ĐỐI KHÔNG chèn các viên nhộng/thanh gạch màu dọc (`<span class="w-2.5 h-6 bg-... rounded-full"></span>`) đứng trước số thứ tự.
       - **Lý do:** Các khối màu này làm vướng mắt, lỗi thời và phá vỡ sự liền mạch của chữ. Tiêu đề đề mục bắt buộc để dạng typography thuần khiết (`text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight`).
     + **⛔ CẤU TRÚC SIDEBAR ĐƠN NHẤT HÓA (SINGLE UNIFIED SIDEBAR DIRECTIVE):**"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated SKILL.md with NO-HEADING-ACCENT-BAR DIRECTIVE successfully!")
else:
    print("Target not found in SKILL.md!")
