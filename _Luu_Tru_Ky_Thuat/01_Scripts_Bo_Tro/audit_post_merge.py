import sys
import re
import os

sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("=== 1. SECTIONS AUDIT ===")
sections = re.findall(r'<section[^>]*id="([^"]+)"', text)
print(f"Total sections ({len(sections)}):", sections)

print("\n=== 2. SIDEBAR SUB-NAV AUDIT ===")
for m in re.finditer(r'<a href="#([^"]+)" class="sub-nav-item[^"]*">.*?<span class="font-bold[^"]*">(\d+\.)</span>\s*<span>([^<]+)</span>.*?<span class="[^"]*badge[^"]*">([^<]+)</span>', text, re.DOTALL):
    print(f"  {m.group(2)} {m.group(3)} [{m.group(1)}] -> Badge: {m.group(4)}")

print("\n=== 3. SECTION 2 CARDS & IMAGES AUDIT ===")
s2 = text[text.find('id="diem-nghen-chuyen-doi"'):text.find('id="bang-uu-tien-p0-p3"')]
cards = re.findall(r'<div class="finding-card[^"]*"(.*?)<!-- Footer Card -->', s2, re.DOTALL)
print(f"Total finding cards in Section 2: {len(cards)}")
for i, c in enumerate(cards, 1):
    t = re.search(r'<h3 class="[^"]*">([^<]+)</h3>', c)
    imgs = re.findall(r'<img[^>]*src="([^"]+)"', c)
    print(f" Card {i}: {t.group(1).strip() if t else ''}")
    print(f"   Images ({len(imgs)}): {imgs}")
    for img_path in imgs:
        if not os.path.exists(img_path):
            print(f"   [ERROR] Image not found: {img_path}")
        else:
            print(f"   [OK] Image exists: {img_path} ({os.path.getsize(img_path)} bytes)")

print("\n=== 4. SECTION 3 (BANG UU TIEN) AUDIT ===")
s3 = text[text.find('id="bang-uu-tien-p0-p3"'):text.find('id="kien-truc-sitemap"')]
h2 = re.search(r'<h2 class="[^"]*">([^<]+)</h2>', s3)
print("Section 3 Header:", h2.group(1).strip() if h2 else "")
table_rows = re.findall(r'<tr class="table-row-item[^"]*" data-prio="([^"]+)">.*?<td class="p-3 font-bold[^"]*">([^<]+)</td>.*?<td class="p-3 font-semibold[^"]*">([^<]+)</td>', s3, re.DOTALL)
print(f"Total Table Rows: {len(table_rows)}")
for r in table_rows:
    print(f"  STT {r[1].strip()}: [{r[0]}] {r[2].strip()}")

m_cards = re.findall(r'<div class="mobile-card-item[^"]*" data-prio="([^"]+)".*?<span class="font-mono font-bold[^"]*">([^<]+)</span>.*?<h4 class="font-bold[^"]*">([^<]+)</h4>', s3, re.DOTALL)
print(f"Total Mobile Cards: {len(m_cards)}")

print("\n=== 5. CHECK F-TRK-01 & GTM TAG REMNANTS ===")
print("F-TRK-01 count:", text.count("F-TRK-01"))
print("Điểm Nghẽn 05 count:", text.count("Điểm Nghẽn 05"))
