import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<span class="[^"]*rounded-full[^"]*"[^>]*></span>', text)
print(f"Total colored pill/bar spans found: {len(matches)}")
for m in matches:
    print(" -", m)

# Find in headings
heading_matches = re.findall(r'<h2[^>]*>.*?<span class="[^"]*rounded-full[^"]*"></span>.*?</h2>', text, re.DOTALL)
print(f"\nTotal in H2 headings: {len(heading_matches)}")
for hm in heading_matches:
    print(" Heading:", hm.strip()[:100])
