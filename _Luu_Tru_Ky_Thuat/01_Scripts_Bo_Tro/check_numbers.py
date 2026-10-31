import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

print("=== SIDEBAR NAV ITEMS ===")
nav_items = re.findall(r'<a href="([^"]+)" class="nav-sub-item[^"]*"[^>]*>(.*?)</a>', text, re.DOTALL)
for href, content in nav_items:
    clean = re.sub(r'<[^>]+>', ' ', content).strip()
    clean = ' '.join(clean.split())
    print(f"{href} -> {clean}")

print("\n=== SECTION 2 FINDING CARDS ===")
cards = re.findall(r'<div class="finding-card[^"]*"[^>]*>(.*?)</div>\s*</div>\s*</div>', text, re.DOTALL)
# Or find h3 inside finding-card
h3s = re.findall(r'<div class="finding-card[^"]*".*?<h3[^>]*>(.*?)</h3>', text, re.DOTALL)
for idx, h in enumerate(h3s):
    print(f"Card {idx+1}: {h.strip()}")

print("\n=== SECTION 3 BEFORE/AFTER PAIRS ===")
caps = re.findall(r'(CẶP ĐỐI SÁNH \d+[^<]*)', text)
for c in caps:
    print(c)

print("\n=== SECTION 4 TABLE ROWS (FINDING IDS) ===")
rows = re.findall(r'<tr class="table-row-item[^"]*"[^>]*>\s*<td[^>]*>([^<]+)</td>\s*<td[^>]*>([^<]+)</td>', text)
for idx, (fid, title) in enumerate(rows):
    print(f"Row {idx+1}: {fid} | {title}")

print("\n=== SECTION 4 MOBILE CARDS (FINDING IDS) ===")
m_cards = re.findall(r'<div class="mobile-card-item[^"]*"[^>]*>.*?<span class="font-mono font-bold text-xs text-slate-900">([^<]+)</span>.*?<h4[^>]*>([^<]+)</h4>', text, re.DOTALL)
for idx, (fid, title) in enumerate(m_cards):
    print(f"Mobile Card {idx+1}: {fid} | {title}")

print("\n=== SECTION 5 ITEMS ===")
s5_blocks = re.findall(r'<span class="text-xs font-bold [^"]* uppercase tracking-wider block mb-1">([^<]+)</span>', text)
for b in s5_blocks:
    print(b)

print("\n=== SECTION 6 BLUEPRINT SECTIONS ===")
s6_sections = re.findall(r'(\d+\.\s*Khối [^<]+)', text)
for s in s6_sections:
    print(s)

print("\n=== SECTION 7 PILLARS ===")
s7_pillars = re.findall(r'(Trụ Cột \d+[^<]*)', text)
for p in s7_pillars:
    print(p)
