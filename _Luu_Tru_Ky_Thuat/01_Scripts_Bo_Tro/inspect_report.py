import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- SIDEBAR BADGES ---")
for m in re.finditer(r'<span class="[^"]*(?:badge|rounded-md|rounded-full)[^"]*">([^<]+)</span>', text):
    val = m.group(1).strip()
    if any(k in val for k in ['P0', 'Mục', 'KPI', 'Cặp', 'Khối', 'Cột', 'Nhóm']):
        print(' -', val)

print("\n--- SECTION 1 STAT CARDS ---")
s1_m = re.search(r'id="buc-tranh".*?(?=id="diem-nghen")', text, re.DOTALL)
if s1_m:
    for m in re.finditer(r'<div class="text-2xl font-bold[^"]*">([^<]+)</div>\s*<div class="text-xs[^"]*">([^<]+)</div>', s1_m.group(0)):
        print(f" {m.group(1).strip()}: {m.group(2).strip()}")

print("\n--- SECTION 2 ---")
s2_m = re.search(r'id="diem-nghen".*?(?=id="doi-sanh")', text, re.DOTALL)
if s2_m:
    s2 = s2_m.group(0)
    filters = re.findall(r'<button class="filter-pill[^"]*"[^>]*>([^<]+)</button>', s2)
    print(" Filters:", filters)
    cards = re.findall(r'<div class="card-hover bg-white rounded-xl.*?</div>\s*</div>\s*</div>', s2, re.DOTALL)
    print(f" Cards count: {len(cards)}")
    for i, c in enumerate(cards, 1):
        title = re.search(r'<h3 class="[^"]*">([^<]+)</h3>', c)
        t_str = title.group(1).strip() if title else "No title"
        print(f"  Card {i}: {t_str}")

print("\n--- SECTION 4 ---")
s4_m = re.search(r'id="bang-uu-tien".*?(?=id="sitemap-rfq")', text, re.DOTALL)
if s4_m:
    s4 = s4_m.group(0)
    title4 = re.search(r'<h2 class="[^"]*">([^<]+)</h2>', s4)
    print(" Title:", title4.group(1).strip() if title4 else "")
    filters4 = re.findall(r'<button class="filter-pill[^"]*"[^>]*>([^<]+)</button>', s4)
    print(" Filters:", filters4)
    rows = re.findall(r'<tr class="border-b[^"]*" data-level="([^"]+)">.*?<td class="px-5 py-3.5[^"]*font-semibold[^"]*">([^<]+)</td>.*?<td class="px-5 py-3.5 font-medium[^"]*">([^<]+)</td>', s4, re.DOTALL)
    print(f" Table Rows ({len(rows)}):")
    for r in rows:
        print(f"  STT {r[1].strip()}: [{r[0]}] {r[2].strip()}")
    
    m_cards = re.findall(r'<div class="p-4 rounded-xl border border-gray-200.*?<div class="text-xs font-bold text-gray-400">([^<]+)</div>.*?<div class="text-sm font-bold text-gray-900">([^<]+)</div>', s4, re.DOTALL)
    print(f" Mobile Cards ({len(m_cards)}):")
    for mc in m_cards:
        print(f"  {mc[0].strip()}: {mc[1].strip()}")
