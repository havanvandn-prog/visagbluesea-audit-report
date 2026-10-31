import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("Original length of bien_tap_cau_chu.py:", len(content))

# 1. Update Sidebar Badges & Tooltips
# Mini rail:
content = content.replace(
    'title="Điểm Nghẽn Thất Thoát">\n        <i data-lucide="alert-octagon" class="w-5 h-5 text-red-500"></i>\n        <span class="absolute left-full ml-3 px-2.5 py-1 bg-slate-900 text-white text-[11px] font-semibold rounded-md shadow-md whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-50">\n          2. Điểm Nghẽn Thất Thoát (5 P0)\n        </span>',
    'title="Điểm Nghẽn Thất Thoát">\n        <i data-lucide="alert-octagon" class="w-5 h-5 text-red-500"></i>\n        <span class="absolute left-full ml-3 px-2.5 py-1 bg-slate-900 text-white text-[11px] font-semibold rounded-md shadow-md whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-50">\n          2. Điểm Nghẽn Thất Thoát (4 P0)\n        </span>'
)
content = content.replace(
    'title="Bảng Ưu Tiên Xử Lý">\n        <i data-lucide="list-checks" class="w-5 h-5"></i>\n        <span class="absolute left-full ml-3 px-2.5 py-1 bg-slate-900 text-white text-[11px] font-semibold rounded-md shadow-md whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-50">\n          4. Bảng Ưu Tiên Xử Lý (10 Mục)\n        </span>',
    'title="Bảng Ưu Tiên Xử Lý">\n        <i data-lucide="list-checks" class="w-5 h-5"></i>\n        <span class="absolute left-full ml-3 px-2.5 py-1 bg-slate-900 text-white text-[11px] font-semibold rounded-md shadow-md whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-50">\n          4. Bảng Ưu Tiên Xử Lý (9 Mục)\n        </span>'
)

# Sub-sidebar badges:
content = re.sub(
    r'<a href="#diem-nghen-chuyen-doi"[^>]*>.*?<span class="[^"]*">(\d+\s*P0)</span>',
    lambda m: m.group(0).replace(m.group(1), '4 P0'),
    content,
    flags=re.DOTALL
)
content = re.sub(
    r'<a href="#bang-uu-tien-p0-p3"[^>]*>.*?<span class="[^"]*">(\d+\s*Mục)</span>',
    lambda m: m.group(0).replace(m.group(1), '9 Mục'),
    content,
    flags=re.DOTALL
)

# 2. Update Section 1 Stat Cards
content = re.sub(
    r'<div class="text-2xl font-bold text-red-600">\s*\d+\s*Điểm Nghẽn\s*</div>',
    '<div class="text-2xl font-bold text-red-600">4 Điểm Nghẽn</div>',
    content
)

# 3. Update Section 2 Filters & Remove Card 05
old_s2_filters = """          <!-- Interactive Filter Tabs -->
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
          </div>"""

new_s2_filters = """          <!-- Interactive Filter Tabs -->
          <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1">
            <button onclick="filterFindings('all', this)" class="filter-pill active px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              Tất Cả (4)
            </button>
            <button onclick="filterFindings('ui', this)" class="filter-pill px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              Giao Diện & Mobile (4)
            </button>
          </div>"""

if old_s2_filters in content:
    content = content.replace(old_s2_filters, new_s2_filters)
    print("Updated Section 2 Filters successfully!")
else:
    print("Warning: old_s2_filters not found, checking regex...")
    content = re.sub(
        r'<button onclick="filterFindings\(\'all\', this\)"[^>]*>.*?Tất Cả \(\d+\).*?</button>\s*<button onclick="filterFindings\(\'ui\', this\)"[^>]*>.*?Giao Diện & Mobile \(\d+\).*?</button>\s*<button onclick="filterFindings\(\'trk\', this\)"[^>]*>.*?Hạ Tầng Đo Lường \(\d+\).*?</button>',
        """<button onclick="filterFindings('all', this)" class="filter-pill active px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              Tất Cả (4)
            </button>
            <button onclick="filterFindings('ui', this)" class="filter-pill px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              Giao Diện & Mobile (4)
            </button>""",
        content,
        flags=re.DOTALL
    )

# Remove Card 05 (GTM Tag) from Section 2
card5_pattern = r'<!-- Vấn Đề 5: GTM Tracking Google Ads -->\s*<div class="finding-card card-hover bg-white rounded-xl p-4 sm:p-5 border border-slate-200 shadow-2xs space-y-3" data-cat="trk">.*?</div>\s*</div>\s*(?=<!-- Vấn Đề|\Z|</div>\s*</section>)'
# Let's inspect exact card 5 text to remove cleanly
s2_idx = content.find('id="diem-nghen-chuyen-doi"')
card5_start = content.find('<!-- Vấn Đề 5: GTM Tracking Google Ads -->', s2_idx)
if card5_start != -1:
    # Find closing div of this finding card
    # Each card has 3 opening divs and 3 closing divs
    # Let's find next comment or end of findings-container
    next_anchor = content.find('</div>\n      </section>', card5_start)
    if next_anchor != -1:
        # Check if there's any closing div right before end of section
        card5_end = next_anchor
        content = content[:card5_start] + content[card5_end:]
        print("Removed Card 05 from Section 2 successfully!")
else:
    print("Warning: Card 5 comment not found directly!")

# 4. Update Section 4: Title, Filters, Table Rows, Mobile Cards
content = content.replace(
    'Danh mục 10 hạng mục kỹ thuật cần xử lý (Hiển thị dạng Card trên Mobile, Bảng trên Desktop).',
    'Danh mục 9 hạng mục kỹ thuật cần xử lý (Hiển thị dạng Card trên Mobile, Bảng trên Desktop).'
)

old_s4_filters = """          <!-- Bộ lọc ưu tiên P0 / P1 / P2 cho bảng -->
          <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1">
            <button onclick="filterTablePriority('all', this)" class="table-filter-btn active px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-slate-900 text-white whitespace-nowrap shrink-0">
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
            </button>
          </div>"""

new_s4_filters = """          <!-- Bộ lọc ưu tiên P0 / P1 / P2 cho bảng -->
          <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1">
            <button onclick="filterTablePriority('all', this)" class="table-filter-btn active px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-slate-900 text-white whitespace-nowrap shrink-0">
              Tất Cả (9)
            </button>
            <button onclick="filterTablePriority('P0', this)" class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0">
              P0 Khẩn Cấp (4)
            </button>
            <button onclick="filterTablePriority('P1', this)" class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0">
              P1 Ưu Tiên Cao (4)
            </button>
            <button onclick="filterTablePriority('P2', this)" class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0">
              P2 Trung Bình (1)
            </button>
          </div>"""

if old_s4_filters in content:
    content = content.replace(old_s4_filters, new_s4_filters)
    print("Updated Section 4 Filters successfully!")
else:
    print("Warning: old_s4_filters not found, using regex...")
    content = re.sub(
        r'<button onclick="filterTablePriority\(\'all\', this\)"[^>]*>.*?Tất Cả \(\d+\).*?</button>\s*<button onclick="filterTablePriority\(\'P0\', this\)"[^>]*>.*?P0 Khẩn Cấp \(\d+\).*?</button>',
        """<button onclick="filterTablePriority('all', this)" class="table-filter-btn active px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-slate-900 text-white whitespace-nowrap shrink-0">
              Tất Cả (9)
            </button>
            <button onclick="filterTablePriority('P0', this)" class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0">
              P0 Khẩn Cấp (4)
            </button>""",
        content,
        flags=re.DOTALL
    )

# Remove Table Row F-TRK-01
tbl_row_old = """              <tr class="table-row-item hover:bg-slate-50" data-prio="P0">
                <td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">05</td>
                <td class="p-3 font-semibold text-slate-900">Chưa gắn thẻ đo lường Google Ads (F-TRK-01)</td>
                <td class="p-3 text-slate-600">GTM chưa cấu hình ghi nhận chuyển đổi lượt gọi và gửi form</td>
                <td class="p-3 text-slate-800">Tạo Conversion Action trong Google Ads và kích hoạt GTM</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><span class="text-slate-400">GTM Snippet</span></td>
              </tr>"""

if tbl_row_old in content:
    content = content.replace(tbl_row_old + "\n", "")
    print("Removed Table row F-TRK-01 successfully!")
else:
    print("Warning: tbl_row_old exact match not found!")
    # regex fallback
    content = re.sub(r'<tr class="table-row-item[^"]*" data-prio="P0">\s*<td[^>]*>05</td>\s*<td[^>]*>[^<]*F-TRK-01.*?</tr>\s*', '', content, flags=re.DOTALL)

# Re-number remaining table rows 06 -> 05, 07 -> 06, 08 -> 07, 09 -> 08, 10 -> 09
content = content.replace(
    '<td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">06</td>\n                <td class="p-3 font-semibold text-slate-900">Tiêu đề mẫu "CAPS TITLE" (F-UI-05)</td>',
    '<td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">05</td>\n                <td class="p-3 font-semibold text-slate-900">Tiêu đề mẫu "CAPS TITLE" (F-UI-05)</td>'
)
content = content.replace(
    '<td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">07</td>\n                <td class="p-3 font-semibold text-slate-900">Số liệu thành tựu dồn cục "17 5347 235" (F-UI-06)</td>',
    '<td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">06</td>\n                <td class="p-3 font-semibold text-slate-900">Số liệu thành tựu dồn cục "17 5347 235" (F-UI-06)</td>'
)
content = content.replace(
    '<td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">08</td>\n                <td class="p-3 font-semibold text-slate-900">Thiếu Trung Tâm Báo Phí RFQ Hub (F-CRO-01)</td>',
    '<td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">07</td>\n                <td class="p-3 font-semibold text-slate-900">Thiếu Trung Tâm Báo Phí RFQ Hub (F-CRO-01)</td>'
)
content = content.replace(
    '<td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">09</td>\n                <td class="p-3 font-semibold text-slate-900">Mã nguồn Wix nặng 1.22 MB (F-TEC-01)</td>',
    '<td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">08</td>\n                <td class="p-3 font-semibold text-slate-900">Mã nguồn Wix nặng 1.22 MB (F-TEC-01)</td>'
)
content = content.replace(
    '<td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">10</td>\n                <td class="p-3 font-semibold text-slate-900">Tin tức chéo không khớp trang đích (F-UI-07)</td>',
    '<td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">09</td>\n                <td class="p-3 font-semibold text-slate-900">Tin tức chéo không khớp trang đích (F-UI-07)</td>'
)

# Remove Mobile Card F-TRK-01
mobile_card_pattern = r'<!-- Card \d+ -->\s*<div class="mobile-card-item[^"]*" data-prio="P0">\s*<div class="flex items-center justify-between">\s*<span class="font-mono font-bold text-xs text-slate-900">F-TRK-01</span>.*?</div>\s*</div>'
if re.search(mobile_card_pattern, content, re.DOTALL):
    content = re.sub(mobile_card_pattern, '', content, flags=re.DOTALL)
    print("Removed Mobile Card F-TRK-01 successfully!")
else:
    # Try exact snippet search
    m_idx = content.find('F-TRK-01')
    if m_idx != -1:
        # find enclosing mobile-card-item
        mc_start = content.rfind('<div class="mobile-card-item', 0, m_idx)
        # find comment before if exists
        comm_start = content.rfind('<!-- Card', 0, mc_start)
        if comm_start != -1 and mc_start - comm_start < 50:
            start_pos = comm_start
        else:
            start_pos = mc_start
        # find end of card
        end_pos = content.find('</div>\n          </div>', m_idx)
        if end_pos != -1:
            end_pos += len('</div>\n          </div>')
            content = content[:start_pos] + content[end_pos:]
            print("Removed Mobile Card F-TRK-01 via index slicing!")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated bien_tap_cau_chu.py!")
