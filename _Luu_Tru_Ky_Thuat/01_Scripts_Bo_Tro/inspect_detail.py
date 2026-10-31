import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

def print_section(sec_id):
    pattern = rf'<section[^>]*id="{sec_id}".*?(?=<section|\Z)'
    m = re.search(pattern, text, re.DOTALL)
    if m:
        return m.group(0)
    return ""

print("=== SIDEBAR SNIPPET ===")
aside_m = re.search(r'<aside.*?</aside>', text, re.DOTALL)
if aside_m:
    print(aside_m.group(0)[:1500])

print("\n=== SECTION TONG QUAN STATS ===")
s1 = print_section('tong-quan')
stats = re.findall(r'<div class="text-[^"]*font-bold[^"]*">([^<]+)</div>\s*<div class="text-[^"]*text-slate-[^"]*">([^<]+)</div>', s1)
for s in stats:
    print(" Stat:", s)

print("\n=== SECTION DIEM NGHEN HEADER & FILTERS ===")
s2 = print_section('diem-nghen-chuyen-doi')
header_s2 = s2[:s2.find('id="findings-container"')]
print(header_s2)

print("\n=== SECTION BANG UU TIEN HEADER & FILTERS ===")
s4 = print_section('bang-uu-tien-p0-p3')
header_s4 = s4[:s4.find('<table')]
print(header_s4)

print("\n=== TABLE ROWS IN SECTION 4 ===")
table_m = re.search(r'<tbody.*?</tbody>', s4, re.DOTALL)
if table_m:
    rows = re.findall(r'<tr[^>]*>.*?</tr>', table_m.group(0), re.DOTALL)
    print(f"Total rows: {len(rows)}")
    for r in rows:
        cols = re.findall(r'<td[^>]*>(.*?)</td>', r, re.DOTALL)
        clean_cols = [re.sub(r'<[^>]+>', '', c).strip() for c in cols]
        print("  Row:", clean_cols[:3])

print("\n=== MOBILE CARDS IN SECTION 4 ===")
mobile_cards_m = re.search(r'id="mobile-action-cards".*?</div>\s*</div>\s*</div>', s4, re.DOTALL)
if mobile_cards_m:
    m_cards = re.findall(r'<div class="bg-white rounded-lg p-3.*?</div>\s*</div>', mobile_cards_m.group(0), re.DOTALL)
    print(f"Total mobile cards: {len(m_cards)}")
    for mc in m_cards:
        code = re.search(r'text-slate-900">([^<]+)</span>', mc)
        title = re.search(r'<h4[^>]*>([^<]+)</h4>', mc)
        c_str = code.group(1).strip() if code else ""
        t_str = title.group(1).strip() if title else ""
        print(f"  MC: {c_str} - {t_str}")
