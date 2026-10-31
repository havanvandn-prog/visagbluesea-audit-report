import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove Sidebar Item 6
sidebar_item_6 = """          <!-- Mục 6 -->
          <a href="#luu-y-google-ads" class="sidebar-nav-item flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-white hover:shadow-2xs transition-all">
            <span class="flex items-center gap-2.5 truncate">
              <i data-lucide="target" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span class="truncate">6. Lưu Ý Google Ads</span>
            </span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-md bg-emerald-100 text-emerald-800 whitespace-nowrap shrink-0">4 Trụ Cột</span>
          </a>"""

if sidebar_item_6 in text:
    text = text.replace(sidebar_item_6, "")
    print("Removed Sidebar Item 6 successfully!")
else:
    print("Warning: sidebar_item_6 not found!")

# 2. Remove Section 6
idx_sec = text.find('Khuyến Nghị Vận Hành Chiến Dịch Google Search Ads')
if idx_sec != -1:
    idx_start = text.rfind('<!--', 0, idx_sec)
    idx_end = text.find('</section>', idx_sec) + len('</section>')
    sec6_block = text[idx_start:idx_end]
    print(f"Found Section 6 block (length {len(sec6_block)})")
    text = text.replace(sec6_block, "")
    print("Removed Section 6 successfully!")
else:
    print("Warning: Section 6 heading not found!")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved bien_tap_cau_chu.py successfully!")
