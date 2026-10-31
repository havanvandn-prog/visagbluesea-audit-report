import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Inspect tables in sections 4, 5, 6
tables = re.findall(r'<table[^>]*>.*?</table>', text, re.DOTALL)
print(f"Total tables found: {len(tables)}")
for i, t in enumerate(tables, 1):
    # find parent div
    idx = text.find(t)
    parent_snippet = text[max(0, idx-150):idx]
    has_overflow = 'overflow-x-auto' in parent_snippet
    print(f"Table {i}: Parent has overflow-x-auto? {has_overflow}")
    print(f"   Parent snippet: {parent_snippet.strip()[-80:]}")

# Check Section 1 Stat Cards on mobile:
s1 = text[text.find('id="tong-quan"'):text.find('id="diem-nghen-chuyen-doi"')]
print("\nSection 1 Grid classes:", re.findall(r'class="[^"]*grid[^"]*"', s1))
