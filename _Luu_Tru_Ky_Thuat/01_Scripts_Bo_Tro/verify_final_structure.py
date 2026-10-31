import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("=== SIDEBAR NAV ITEMS ===")
matches = re.finditer(r'<a href="#([^"]*)"[^>]*class="sidebar-nav-item[^"]*">.*?<span class="truncate">([^<]*)</span>', text, re.DOTALL)
for m in matches:
    print(f" - #{m.group(1)}: {m.group(2).strip()}")

print("\n=== SECTION HEADINGS (H2) ===")
h2_matches = re.finditer(r'<h2 class="[^"]*">\s*([^<]*?)\s*</h2>', text)
for m in h2_matches:
    print(f" - {m.group(1).strip()}")
