import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Search for 14, 6, 3, or other numbers associated with counts
patterns = [
    r'(\d+\s*hạng mục)',
    r'(\d+\s*Mục)',
    r'(\d+\s*mục)',
    r'(\d+\s*Điểm Nghẽn)',
    r'(\d+\s*điểm nghẽn)',
    r'(\d+\s*P0)',
    r'(\d+\s*P1)',
    r'(\d+\s*P2)',
    r'(\d+\s*Cặp)',
    r'(\d+\s*cặp)',
    r'Tất Cả \(\d+\)',
    r'P0 [^\(]*\(\d+\)',
    r'P1 [^\(]*\(\d+\)',
    r'P2 [^\(]*\(\d+\)',
]

for p in patterns:
    matches = re.findall(p, text, re.IGNORECASE)
    if matches:
        print(f"Pattern {p}: {set(matches)}")
