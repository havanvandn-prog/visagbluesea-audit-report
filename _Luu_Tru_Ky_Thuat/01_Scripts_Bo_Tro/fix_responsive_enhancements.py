import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

# ==============================================================
# 1. FIX TABLE 2 (MA TRẬN URL) TRONG SECTION 4: THÊM OVERFLOW-X-AUTO
# ==============================================================
old_table2 = """          <div class="p-3.5 bg-slate-100 border-b border-slate-200 font-bold text-xs text-slate-800">
            Ma Trận Xử Lý & Chuẩn Hóa Đường Dẫn (URL Mapping Matrix)
          </div>
          <table class="w-full text-left border-collapse text-xs">"""

new_table2 = """          <div class="p-3.5 bg-slate-100 border-b border-slate-200 font-bold text-xs text-slate-800 flex items-center justify-between">
            <span>Ma Trận Xử Lý & Chuẩn Hóa Đường Dẫn (URL Mapping Matrix)</span>
            <span class="text-[10px] text-slate-400 font-normal md:hidden">← Cuộn ngang để xem đủ →</span>
          </div>
          <div class="overflow-x-auto no-scrollbar">
            <table class="w-full text-left border-collapse text-xs min-w-[600px]">"""

# Close the div after </table>
if old_table2 in text:
    text = text.replace(old_table2, new_table2, 1)
    # Find next </table> after new_table2
    idx_tbl2 = text.find(new_table2)
    idx_close_tbl = text.find('</table>', idx_tbl2)
    if idx_close_tbl != -1:
        text = text[:idx_close_tbl + len('</table>')] + '\n          </div>' + text[idx_close_tbl + len('</table>'):]
        print("Fixed Table 2 with overflow-x-auto container successfully!")
else:
    print("Warning: old_table2 not found!")

# ==============================================================
# 2. TỐI ƯU TOUCH TARGETS: FILTER PILLS VÀ VERIFICATION BUTTONS
# ==============================================================
# Nút filter trong Section 2
text = text.replace(
    'class="filter-pill active px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors"',
    'class="filter-pill active px-3.5 py-2 text-xs font-semibold rounded-xl border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors min-h-[38px] flex items-center"'
)
text = text.replace(
    'class="filter-pill px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors"',
    'class="filter-pill px-3.5 py-2 text-xs font-semibold rounded-xl border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors min-h-[38px] flex items-center"'
)

# Nút filter trong Section 3 (Table filter)
text = text.replace(
    'class="table-filter-btn active px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-slate-900 text-white whitespace-nowrap shrink-0"',
    'class="table-filter-btn active px-3.5 py-2 text-xs font-bold rounded-xl border border-slate-200 bg-slate-900 text-white whitespace-nowrap shrink-0 min-h-[38px] flex items-center"'
)
text = text.replace(
    'class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0"',
    'class="table-filter-btn px-3.5 py-2 text-xs font-bold rounded-xl border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 min-h-[38px] flex items-center"'
)

# Nâng cấp link kiểm chứng trong Card Header thành Nút bấm chạm ngón tay chuẩn
text = text.replace(
    'class="text-xs text-emerald-600 hover:text-emerald-700 flex items-center gap-1 font-semibold whitespace-nowrap"',
    'class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 text-emerald-700 text-xs font-bold border border-emerald-200 transition-colors shrink-0 min-h-[36px]"'
)

# ==============================================================
# 3. THÊM CHỈ BÁO ZOOM CẢM ỨNG (TOUCH INDICATOR) TRÊN ẢNH
# ==============================================================
# Thêm badge 'Chạm để phóng to' ở góc dưới ảnh để trên mobile người dùng biết là có thể bấm mở lightbox
old_zoom_overlay = """<div class="absolute inset-0 bg-slate-900/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                        <i data-lucide="maximize-2" class="w-4 h-4"></i>
                        <span>Nhấp để phóng to chi tiết</span>
                      </div>"""

new_zoom_overlay = """<div class="absolute inset-0 bg-slate-900/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                        <i data-lucide="maximize-2" class="w-4 h-4"></i>
                        <span>Nhấp để phóng to chi tiết</span>
                      </div>
                      <div class="absolute bottom-2 right-2 md:hidden px-2 py-1 bg-slate-900/75 text-white text-[10px] font-semibold rounded-md backdrop-blur-xs flex items-center gap-1 pointer-events-none">
                        <i data-lucide="zoom-in" class="w-3 h-3"></i> Chạm phóng to
                      </div>"""

text = text.replace(old_zoom_overlay, new_zoom_overlay)

old_zoom_emerald = """<div class="absolute inset-0 bg-emerald-950/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                        <i data-lucide="maximize-2" class="w-4 h-4"></i>
                        <span>Nhấp để phóng to chi tiết</span>
                      </div>"""

new_zoom_emerald = """<div class="absolute inset-0 bg-emerald-950/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                        <i data-lucide="maximize-2" class="w-4 h-4"></i>
                        <span>Nhấp để phóng to chi tiết</span>
                      </div>
                      <div class="absolute bottom-2 right-2 md:hidden px-2 py-1 bg-emerald-950/80 text-white text-[10px] font-semibold rounded-md backdrop-blur-xs flex items-center gap-1 pointer-events-none">
                        <i data-lucide="zoom-in" class="w-3 h-3"></i> Chạm phóng to
                      </div>"""

text = text.replace(old_zoom_emerald, new_zoom_emerald)

# ==============================================================
# 4. THÊM MOBILE FLOATING QUICK-NAV BAR (ĐIỀU HƯỚNG NHANH MOBILE)
# ==============================================================
mobile_nav_bar = """
  <!-- ================= MOBILE FLOATING QUICK-NAV BAR (CHỈ HIỆN TRÊN MOBILE/TABLET DỌC) ================= -->
  <div class="fixed bottom-3 left-3 right-3 z-40 md:hidden bg-white/95 backdrop-blur-md border border-slate-200/90 rounded-2xl shadow-xl p-1.5 flex items-center justify-between gap-1">
    <a href="#tong-quan" class="flex-1 py-1.5 px-1 rounded-xl text-center text-slate-600 hover:text-emerald-600 hover:bg-slate-50 transition-colors flex flex-col items-center justify-center gap-0.5">
      <i data-lucide="layout-dashboard" class="w-4 h-4"></i>
      <span class="text-[10px] font-bold tracking-tight">Tổng Quan</span>
    </a>
    <a href="#diem-nghen-chuyen-doi" class="flex-1 py-1.5 px-1 rounded-xl text-center text-slate-600 hover:text-red-600 hover:bg-slate-50 transition-colors flex flex-col items-center justify-center gap-0.5">
      <i data-lucide="alert-octagon" class="w-4 h-4 text-red-500"></i>
      <span class="text-[10px] font-bold tracking-tight">Điểm Nghẽn</span>
    </a>
    <a href="#bang-uu-tien-p0-p3" class="flex-1 py-1.5 px-1 rounded-xl text-center text-slate-600 hover:text-amber-600 hover:bg-slate-50 transition-colors flex flex-col items-center justify-center gap-0.5">
      <i data-lucide="list-checks" class="w-4 h-4 text-amber-500"></i>
      <span class="text-[10px] font-bold tracking-tight">Ưu Tiên (9)</span>
    </a>
    <a href="#kien-truc-sitemap" class="flex-1 py-1.5 px-1 rounded-xl text-center text-slate-600 hover:text-indigo-600 hover:bg-slate-50 transition-colors flex flex-col items-center justify-center gap-0.5">
      <i data-lucide="network" class="w-4 h-4 text-indigo-500"></i>
      <span class="text-[10px] font-bold tracking-tight">Sitemap</span>
    </a>
    <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" class="py-1.5 px-2 rounded-xl text-center text-slate-400 hover:text-slate-900 transition-colors flex flex-col items-center justify-center gap-0.5 border-l border-slate-100">
      <i data-lucide="arrow-up" class="w-4 h-4"></i>
      <span class="text-[10px] font-bold tracking-tight">Đầu Trang</span>
    </button>
  </div>
"""

# Thêm padding bottom cho body trên mobile để nội dung không bị che bởi Mobile Nav Bar
old_main_closing = "</main>"
new_main_closing = """  <div class="h-16 md:hidden"></div> <!-- Spacer for mobile floating nav -->
    </main>"""

if old_main_closing in text:
    text = text.replace(old_main_closing, new_main_closing, 1)

# Chèn mobile_nav_bar ngay trước </body>
if "MOBILE FLOATING QUICK-NAV BAR" not in text:
    text = text.replace("</body>", mobile_nav_bar + "\n</body>", 1)
    print("Added Mobile Floating Quick-Nav Bar successfully!")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated bien_tap_cau_chu.py with responsive optimizations!")
