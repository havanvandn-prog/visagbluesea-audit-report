import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Section 1
s1 = text[text.find('id="tong-quan"'):text.find('id="diem-nghen-chuyen-doi"')]
print("=== SECTION 1 STAT CARDS ===")
for m in re.finditer(r'<div class="text-2xl font-bold[^"]*">([^<]+)</div>\s*<div class="text-xs[^"]*">([^<]+)</div>', s1):
    print(f"  {m.group(1).strip()}: {m.group(2).strip()}")

# Section 2
s2 = text[text.find('id="diem-nghen-chuyen-doi"'):text.find('id="doi-sanh-truoc-sau"')]
print("\n=== SECTION 2 FILTERS & CARDS ===")
filters = re.findall(r'<button onclick="filterFindings[^"]*" class="filter-pill[^"]*"[^>]*>([^<]+)</button>', s2)
print("  Filters:", [f.strip() for f in filters])
cards = re.findall(r'<div class="finding-card[^"]*"(.*?)</div>\s*</div>\s*</div>', s2, re.DOTALL)
print(f"  Total finding cards: {len(cards)}")
for i, c in enumerate(cards, 1):
    t = re.search(r'<h3 class="[^"]*">([^<]+)</h3>', c)
    print(f"   Card {i}: {t.group(1).strip() if t else 'No title'}")
