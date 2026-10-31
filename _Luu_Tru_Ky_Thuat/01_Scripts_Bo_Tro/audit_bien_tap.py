import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- 1. F-TRK-01 occurrences:", text.count("F-TRK-01"))
print("--- 2. GTM / Thẻ đo lường occurrences:", text.count("Chưa Cài Đặt Thẻ Đo Lường"))
print("--- 3. Điểm Nghẽn 05 occurrences:", text.count("Điểm Nghẽn 05"))

# Sidebar badges
print("\n--- 4. Sidebar Items:")
for m in re.finditer(r'<a href="#([^"]+)"[^>]*>.*?<span[^>]*>([^<]+)</span>.*?</a>', text, re.DOTALL):
    href = m.group(1)
    val = re.sub(r'\s+', ' ', m.group(2)).strip()
    if any(k in href for k in ['diem-nghen', 'bang-uu-tien', 'tong-quan']):
        print(f"  {href}: {val}")

# Also check rail tooltips
print("\n--- 5. Rail Tooltips:")
for m in re.finditer(r'title="([^"]+)">.*?<span class="absolute[^"]*">\s*([^<]+)\s*</span>', text, re.DOTALL):
    print(f"  {m.group(1)} -> {m.group(2).strip()}")

# Section 1 stat card
print("\n--- 6. Section 1 Stats:")
s1_m = re.search(r'id="tong-quan".*?(?=id="diem-nghen")', text, re.DOTALL)
if s1_m:
    for m in re.finditer(r'<div class="text-2xl font-bold[^"]*">([^<]+)</div>\s*<div class="text-xs[^"]*">([^<]+)</div>', s1_m.group(0)):
        print(f"  {m.group(1).strip()}: {m.group(2).strip()}")

# Section 2 cards & filters
print("\n--- 7. Section 2 Cards & Filters:")
s2_m = re.search(r'id="diem-nghen-chuyen-doi".*?(?=id="doi-sanh")', text, re.DOTALL)
if s2_m:
    s2 = s2_m.group(0)
    filters = re.findall(r'<button class="filter-pill[^"]*"[^>]*>([^<]+)</button>', s2)
    print("  Filters:", [f.strip() for f in filters])
    cards = re.findall(r'<div class="finding-card[^"]*"(.*?)</div>\s*</div>\s*</div>', s2, re.DOTALL)
    print(f"  Total finding cards: {len(cards)}")
    for i, c in enumerate(cards, 1):
        t = re.search(r'<h3 class="[^"]*">([^<]+)</h3>', c)
        print(f"   Card {i}: {t.group(1).strip() if t else 'No title'}")

# Section 4 table rows & mobile cards
print("\n--- 8. Section 4 Rows & Mobile Cards:")
s4_m = re.search(r'id="bang-uu-tien-p0-p3".*?(?=id="kien-truc-sitemap")', text, re.DOTALL)
if s4_m:
    s4 = s4_m.group(0)
    p_desc = re.search(r'<p class="text-slate-500 text-xs sm:text-sm mt-0.5">([^<]+)</p>', s4)
    print("  Sub-heading:", p_desc.group(1).strip() if p_desc else "")
    filters4 = re.findall(r'<button class="table-filter-btn[^"]*"[^>]*>([^<]+)</button>', s4)
    print("  Filters:", [f.strip() for f in filters4])
    
    rows = re.findall(r'<tr class="table-row-item[^"]*" data-prio="([^"]+)">.*?<td class="p-3 font-bold[^"]*">([^<]+)</td>.*?<td class="p-3 font-semibold[^"]*">([^<]+)</td>', s4, re.DOTALL)
    print(f"  Table rows ({len(rows)}):")
    for r in rows:
        print(f"   STT {r[1].strip()}: [{r[0]}] {r[2].strip()}")
        
    mcards = re.findall(r'<div class="mobile-card-item[^"]*" data-prio="([^"]+)".*?<span class="font-mono font-bold[^"]*">([^<]+)</span>.*?<h4 class="font-bold[^"]*">([^<]+)</h4>', s4, re.DOTALL)
    print(f"  Mobile cards ({len(mcards)}):")
    for mc in mcards:
        print(f"   [{mc[0]}] {mc[1].strip()}: {mc[2].strip()}")
