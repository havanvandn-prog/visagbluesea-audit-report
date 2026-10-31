import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'index.html']:
    print(f"\n==========================================")
    print(f"VERIFYING FILE: {fname}")
    print(f"==========================================")
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()

    print("1. F-TRK-01 count:", text.count("F-TRK-01"))
    print("2. 'Chưa Cài Đặt Thẻ Đo Lường' count:", text.count("Chưa Cài Đặt Thẻ Đo Lường"))
    print("3. 'Điểm Nghẽn 05' count:", text.count("Điểm Nghẽn 05"))

    print("\n4. Sub-Sidebar Badges:")
    for m in re.finditer(r'<a href="#([^"]+)"[^>]*>.*?<span class="[^"]*">([^<]+)</span>.*?</a>', text, re.DOTALL):
        href = m.group(1)
        val = m.group(2).strip()
        if any(k in href for k in ['diem-nghen', 'bang-uu-tien']):
            print(f"  {href}: {val}")

    print("\n5. Rail Tooltips:")
    for m in re.finditer(r'title="([^"]+)">.*?<span class="absolute[^"]*">\s*([^<]+)\s*</span>', text, re.DOTALL):
        if any(k in m.group(1) for k in ['Điểm Nghẽn', 'Bảng Khuyến Nghị', 'Bảng Ưu Tiên']):
            print(f"  {m.group(1)} -> {m.group(2).strip()}")

    print("\n6. Section 1 Stat Cards:")
    s1_m = re.search(r'id="tong-quan".*?(?=id="diem-nghen")', text, re.DOTALL)
    if s1_m:
        for m in re.finditer(r'<div class="text-2xl font-bold[^"]*">([^<]+)</div>\s*<div class="text-xs[^"]*">([^<]+)</div>', s1_m.group(0)):
            print(f"  {m.group(1).strip()}: {m.group(2).strip()}")

    print("\n7. Section 2 Cards & Filters:")
    s2_m = re.search(r'id="diem-nghen-chuyen-doi".*?(?=id="doi-sanh")', text, re.DOTALL)
    if s2_m:
        s2 = s2_m.group(0)
        filters = re.findall(r'<button onclick="filterFindings[^"]*" class="filter-pill[^"]*"[^>]*>([^<]+)</button>', s2)
        print("  Filters:", [f.strip() for f in filters])
        cards = re.findall(r'<div class="finding-card[^"]*"(.*?)</div>\s*</div>\s*</div>', s2, re.DOTALL)
        print(f"  Total finding cards: {len(cards)}")
        for i, c in enumerate(cards, 1):
            t = re.search(r'<h3 class="[^"]*">([^<]+)</h3>', c)
            print(f"   Card {i}: {t.group(1).strip() if t else 'No title'}")

    print("\n8. Section 4 Rows & Mobile Cards:")
    s4_m = re.search(r'id="bang-uu-tien-p0-p3".*?(?=id="kien-truc-sitemap")', text, re.DOTALL)
    if s4_m:
        s4 = s4_m.group(0)
        p_desc = re.search(r'<p class="text-slate-500 text-xs sm:text-sm mt-0.5">([^<]+)</p>', s4)
        print("  Sub-heading:", p_desc.group(1).strip() if p_desc else "")
        filters4 = re.findall(r'<button onclick="filterTablePriority[^"]*" class="table-filter-btn[^"]*"[^>]*>([^<]+)</button>', s4)
        print("  Filters:", [f.strip() for f in filters4])
        
        rows = re.findall(r'<tr class="table-row-item[^"]*" data-prio="([^"]+)">.*?<td class="p-3 font-bold[^"]*">([^<]+)</td>.*?<td class="p-3 font-semibold[^"]*">([^<]+)</td>', s4, re.DOTALL)
        print(f"  Table rows ({len(rows)}):")
        for r in rows:
            print(f"   STT {r[1].strip()}: [{r[0]}] {r[2].strip()}")
            
        mcards = re.findall(r'<div class="mobile-card-item[^"]*" data-prio="([^"]+)".*?<span class="font-mono font-bold[^"]*">([^<]+)</span>.*?<h4 class="font-bold[^"]*">([^<]+)</h4>', s4, re.DOTALL)
        print(f"  Mobile cards ({len(mcards)}):")
        for mc in mcards:
            print(f"   [{mc[0]}] {mc[1].strip()}: {mc[2].strip()}")

print("\n--- ALL VERIFICATIONS FINISHED ---")
