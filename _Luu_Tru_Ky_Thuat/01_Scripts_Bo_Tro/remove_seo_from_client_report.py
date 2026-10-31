import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

script_path = "_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py"

with open(script_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update badges & labels in Sub-sidebar & Rail
text = text.replace(
    '<span class="text-[10px] bg-red-100 text-red-800 font-bold px-2 py-0.5 rounded whitespace-nowrap shrink-0">6 P0</span>',
    '<span class="text-[10px] bg-red-100 text-red-800 font-bold px-2 py-0.5 rounded whitespace-nowrap shrink-0">5 P0</span>'
)
text = text.replace(
    '<span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded whitespace-nowrap shrink-0">3 Cặp</span>',
    '<span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded whitespace-nowrap shrink-0">2 Cặp</span>'
)
text = text.replace(
    '<span class="text-[10px] bg-amber-100 text-amber-800 font-bold px-2 py-0.5 rounded whitespace-nowrap shrink-0">14 Mục</span>',
    '<span class="text-[10px] bg-amber-100 text-amber-800 font-bold px-2 py-0.5 rounded whitespace-nowrap shrink-0">10 Mục</span>'
)

# Rail tooltips
text = text.replace('2. Điểm Nghẽn Thất Thoát (P0)', '2. Điểm Nghẽn Thất Thoát (5 P0)')
text = text.replace('3. Đối Sánh Trước & Sau', '3. Đối Sánh Trước & Sau (2 Cặp)')
text = text.replace('4. Bảng Ưu Tiên Xử Lý (14 Mục)', '4. Bảng Ưu Tiên Xử Lý (10 Mục)')

# Stat card
text = text.replace('<span class="text-2xl sm:text-3xl font-black text-red-600 block">6 Điểm Nghẽn</span>', '<span class="text-2xl sm:text-3xl font-black text-red-600 block">5 Điểm Nghẽn</span>')

# Filter buttons Section 2
old_filter_sec2 = '''          <!-- Interactive Filter Tabs -->
          <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1">
            <button onclick="filterFindings('all', this)" class="filter-pill active px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              Tất Cả (6)
            </button>
            <button onclick="filterFindings('ui', this)" class="filter-pill px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              Giao Diện & Mobile (4)
            </button>
            <button onclick="filterFindings('tech', this)" class="filter-pill px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              SEO & Tracking (2)
            </button>
          </div>'''

new_filter_sec2 = '''          <!-- Interactive Filter Tabs -->
          <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1">
            <button onclick="filterFindings('all', this)" class="filter-pill active px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              Tất Cả (5)
            </button>
            <button onclick="filterFindings('ui', this)" class="filter-pill px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              Giao Diện & Mobile (4)
            </button>
            <button onclick="filterFindings('trk', this)" class="filter-pill px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              Hạ Tầng Đo Lường (1)
            </button>
          </div>'''

text = text.replace(old_filter_sec2, new_filter_sec2)

# Remove Finding 5 (F-SEO-01) from Section 2
f_seo_01_card = re.search(r'<!-- Finding 5: Khuyết thẻ H1 trên trang chiến lược -->.*?</div>\s*<!-- Finding 6:', text, re.DOTALL)
if f_seo_01_card:
    text = text.replace(f_seo_01_card.group(0), '<!-- Finding 5: ')
    print("Removed Finding 5 (F-SEO-01) from Section 2 successfully")
else:
    print("WARNING: Finding 5 regex not matched")

# Update Finding 6 (now Finding 5): change data-cat from "tech" to "trk"
text = text.replace('<!-- Finding 6: Mất dấu chuyển đổi quảng cáo -->\n        <div class="finding-card bg-white p-4 sm:p-5 rounded-xl border border-slate-200 shadow-2xs space-y-3 border-l-4 border-l-red-500" data-cat="tech">',
                    '<!-- Finding 5: Mất dấu chuyển đổi quảng cáo -->\n        <div class="finding-card bg-white p-4 sm:p-5 rounded-xl border border-slate-200 shadow-2xs space-y-3 border-l-4 border-l-red-500" data-cat="trk">')

# Remove Cặp 3 (SEO Panel Extension) from Section 3
seo_panel_cap3 = re.search(r'<!-- Cặp 3: Bằng chứng lỗi SEO Panel Extension -->.*?</section>', text, re.DOTALL)
if seo_panel_cap3:
    # Replace with just </section>
    text = text.replace(seo_panel_cap3.group(0), '</section>')
    print("Removed Cặp 3 (SEO Panel) from Section 3 successfully")
else:
    print("WARNING: Cặp 3 regex not matched")

# Update Section 4 Filter buttons: 10 items total
old_sec4_filter = '''            <button onclick="filterTablePriority('all', this)" class="table-filter-btn active px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-slate-900 text-white whitespace-nowrap shrink-0">
              Tất Cả (14)
            </button>
            <button onclick="filterTablePriority('P0', this)" class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0">
              P0 Khẩn Cấp (6)
            </button>
            <button onclick="filterTablePriority('P1', this)" class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0">
              P1 Ưu Tiên Cao (5)
            </button>
            <button onclick="filterTablePriority('P2', this)" class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0">
              P2 Trung Bình (3)
            </button>'''

new_sec4_filter = '''            <button onclick="filterTablePriority('all', this)" class="table-filter-btn active px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-slate-900 text-white whitespace-nowrap shrink-0">
              Tất Cả (10)
            </button>
            <button onclick="filterTablePriority('P0', this)" class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0">
              P0 Khẩn Cấp (5)
            </button>
            <button onclick="filterTablePriority('P1', this)" class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0">
              P1 Ưu Tiên Cao (4)
            </button>
            <button onclick="filterTablePriority('P2', this)" class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0">
              P2 Trung Bình (1)
            </button>'''

text = text.replace(old_sec4_filter, new_sec4_filter)

# Remove F-SEO-01 row from Table
text = re.sub(r'<tr class="table-row-item hover:bg-slate-50" data-prio="P0">\s*<td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-SEO-01</td>.*?</tr>\s*', '', text, flags=re.DOTALL)

# Remove F-SEO-02 row from Table
text = re.sub(r'<tr class="table-row-item hover:bg-slate-50" data-prio="P1">\s*<td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-SEO-02</td>.*?</tr>\s*', '', text, flags=re.DOTALL)

# Remove F-SEO-03 row from Table
text = re.sub(r'<tr class="table-row-item hover:bg-slate-50" data-prio="P2">\s*<td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-SEO-03</td>.*?</tr>\s*', '', text, flags=re.DOTALL)

# Remove F-SEO-04 row from Table
text = re.sub(r'<tr class="table-row-item hover:bg-slate-50" data-prio="P2">\s*<td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-SEO-04</td>.*?</tr>\s*', '', text, flags=re.DOTALL)

# Update F-TEC-01 description to focus on Google Ads Landing Page speed
old_f_tec_01 = '''              <tr class="table-row-item hover:bg-slate-50" data-prio="P1">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-TEC-01</td>
                <td class="p-3 font-semibold text-slate-900">Mã nguồn Wix nặng 1.22 MB</td>
                <td class="p-3 text-slate-600">HTML tĩnh chiếm 61% giới hạn 2MB cào của Googlebot</td>
                <td class="p-3 text-slate-800">Tắt các widget Wix không dùng, nén toàn bộ ảnh sang WebP</td>
                <td class="p-3"><span class="badge-p1 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P1 (Cao)</span></td>
                <td class="p-3 whitespace-nowrap"><span class="text-slate-400">Toàn site</span></td>
              </tr>'''

new_f_tec_01 = '''              <tr class="table-row-item hover:bg-slate-50" data-prio="P1">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-TEC-01</td>
                <td class="p-3 font-semibold text-slate-900">Mã nguồn Wix nặng 1.22 MB</td>
                <td class="p-3 text-slate-600">Mã nguồn nặng làm chậm tốc độ tải trang trên điện thoại, ảnh hưởng điểm trang đích Google Ads</td>
                <td class="p-3 text-slate-800">Tắt các widget thừa, nén ảnh WebP để tăng tốc độ trang đích dưới 2.5 giây</td>
                <td class="p-3"><span class="badge-p1 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P1 (Cao)</span></td>
                <td class="p-3 whitespace-nowrap"><span class="text-slate-400">Toàn site</span></td>
              </tr>'''

text = text.replace(old_f_tec_01, new_f_tec_01)

# Remove F-SEO-01 from Mobile Card Stack
old_mobile_card_5 = re.search(r'<!-- Card 5 -->\s*<div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P0">\s*<div class="flex items-center justify-between">\s*<span class="font-mono font-bold text-xs text-slate-900">F-SEO-01</span>.*?</div>\s*</div>', text, re.DOTALL)
if old_mobile_card_5:
    text = text.replace(old_mobile_card_5.group(0), '')
    print("Removed F-SEO-01 from Mobile Card Stack successfully")
else:
    print("WARNING: Mobile Card F-SEO-01 regex not matched")

# Update Section 5 heading & text (no mention of SEO)
text = text.replace(
    'Tư Vấn Tối Ưu Chi Phí Thiết Kế Website: Phân Biệt Landing Page vs Bài Viết Chuẩn SEO',
    'Tư Vấn Tối Ưu Chi Phí Thiết Kế Website: Phân Biệt Landing Page Chốt Đơn vs Bài Viết Thông Tin CMS'
)
text = text.replace(
    '<span class="text-xs font-bold text-blue-700 uppercase tracking-wider block mb-1">2. Nhóm Bài Viết Chuẩn SEO (Tin Tức CMS)</span>',
    '<span class="text-xs font-bold text-blue-700 uppercase tracking-wider block mb-1">2. Nhóm Bài Viết Thông Tin & Cẩm Nang (CMS Post)</span>'
)

with open(script_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated bien_tap_cau_chu.py successfully!")
