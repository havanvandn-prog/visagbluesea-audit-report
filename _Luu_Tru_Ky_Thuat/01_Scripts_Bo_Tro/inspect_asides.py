import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Inspect aside tags and main padding
asides = re.findall(r'<aside.*?</aside>', text, re.DOTALL)
print(f"Total aside tags found: {len(asides)}")
for i, a in enumerate(asides, 1):
    print(f"\n--- ASIDE {i} ---")
    print(a[:300])

main_tag = re.search(r'<main[^>]*>', text)
if main_tag:
    print("\n--- MAIN TAG ---")
    print(main_tag.group(0))
