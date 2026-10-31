import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Verify Header:
# - fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 h-14
# - NO buttons, NO CTA
header_block = html[html.find('<header'):html.find('</header>')]
assert '<button' not in header_block, "Header must not have button!"
assert 'download' not in header_block, "Header must not have download link!"
assert 'fixed top-0' in header_block, "Header must be fixed top-0!"

# 2. Verify Sidebar:
# - fixed top-14 left-0 bottom-0 w-[270px]
# - md:ml-[270px] on main
# - No helper card in sidebar
sidebar_block = html[html.find('<aside'):html.find('</aside>')]
assert 'w-[270px]' in sidebar_block, "Sidebar must be w-[270px]!"
assert 'Thẩm Định Độc Lập\n          Tài liệu đánh giá' not in sidebar_block, "No helper card in sidebar!"
assert 'md:ml-[270px]' in html, "Main must have md:ml-[270px]!"

# 3. Verify H2 Headings:
# - Pure typography, no w-2.5 h-6 accent pill
h2_matches = re.findall(r'<h2[^>]*>.*?</h2>', html, re.DOTALL)
for h in h2_matches:
    assert 'w-2.5' not in h, f"H2 must not have accent pill: {h}"
    assert '<span' not in h, f"H2 must be pure typography: {h}"

print("All layout rules verified 100% PASS!")

# Write template file
template_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\website-audit-core\templates\template_client_presentation_master.html'
with open(template_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Saved template_client_presentation_master.html ({len(html)} bytes) successfully!")
