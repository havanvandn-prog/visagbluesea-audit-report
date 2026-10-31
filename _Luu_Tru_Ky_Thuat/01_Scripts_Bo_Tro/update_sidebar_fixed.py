import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

script_path = "_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py"

with open(script_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update rail sidebar to fixed
old_rail = '''    <!-- 1. GLOBAL MINI ICON RAIL (60px fixed bên trái) -->
    <aside class="w-[60px] shrink-0 bg-white border-r border-slate-200 hidden lg:flex flex-col items-center py-4 space-y-4 sticky top-14 h-[calc(100vh-3.5rem)] self-start z-30">'''

new_rail = '''    <!-- 1. GLOBAL MINI ICON RAIL (60px fixed bên trái) -->
    <aside class="fixed top-14 left-0 bottom-0 w-[60px] bg-white border-r border-slate-200 hidden lg:flex flex-col items-center py-4 space-y-4 z-30">'''

# 2. Update sub-sidebar to fixed 280px, anti-line-wrapping, zero truncate
old_sub = '''    <!-- 2. CONTEXTUAL SUB-SIDEBAR (220px desktop) -->
    <aside class="w-56 shrink-0 bg-white border-r border-slate-200 hidden xl:block p-4 sticky top-14 h-[calc(100vh-3.5rem)] self-start overflow-y-auto">
      <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-3 px-2 flex items-center justify-between">
        <span>Đề Mục Thẩm Định</span>
        <span class="bg-slate-100 text-slate-600 px-1.5 py-0.5 rounded text-[10px]">v3.6</span>
      </div>
      <nav class="space-y-1 text-xs font-medium">
        <a href="#tong-quan" class="nav-sub-item flex items-center justify-between px-2.5 py-2 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors active">
          <span class="truncate">1. Bức Tranh Tổng Thể</span>
          <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.5 rounded">4 KPI</span>
        </a>
        <a href="#diem-nghen-chuyen-doi" class="nav-sub-item flex items-center justify-between px-2.5 py-2 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors">
          <span class="truncate">2. Điểm Nghẽn Thất Thoát</span>
          <span class="text-[10px] bg-red-100 text-red-800 font-bold px-1.5 py-0.5 rounded">6 P0</span>
        </a>
        <a href="#doi-sanh-truoc-sau" class="nav-sub-item flex items-center justify-between px-2.5 py-2 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors">
          <span class="truncate">3. Đối Sánh Trước/Sau</span>
          <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.5 rounded">3 Cặp</span>
        </a>
        <a href="#bang-uu-tien-p0-p3" class="nav-sub-item flex items-center justify-between px-2.5 py-2 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors">
          <span class="truncate">4. Bảng Ưu Tiên Xử Lý</span>
          <span class="text-[10px] bg-amber-100 text-amber-800 font-bold px-1.5 py-0.5 rounded">14 Mục</span>
        </a>
        <a href="#kien-truc-sitemap" class="nav-sub-item flex items-center justify-between px-2.5 py-2 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors">
          <span class="truncate">5. Sitemap & RFQ Hub</span>
          <span class="text-[10px] bg-indigo-100 text-indigo-800 font-bold px-1.5 py-0.5 rounded">5 Nhóm</span>
        </a>
        <a href="#blueprint-sections" class="nav-sub-item flex items-center justify-between px-2.5 py-2 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors">
          <span class="truncate">6. Blueprint Sections</span>
          <span class="text-[10px] bg-blue-100 text-blue-800 font-bold px-1.5 py-0.5 rounded">7 Khối</span>
        </a>
        <a href="#luu-y-google-ads" class="nav-sub-item flex items-center justify-between px-2.5 py-2 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors">
          <span class="truncate">7. Lưu Ý Google Ads</span>
          <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.5 rounded">4 Trụ Cột</span>
        </a>
      </nav>

      <div class="mt-8 p-3 bg-slate-50 rounded-xl border border-slate-200 text-[11px] text-slate-600 space-y-2">
        <div class="font-bold text-slate-800 flex items-center gap-1.5">
          <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-600"></i>
          <span>Thẩm Định Độc Lập</span>
        </div>
        <p class="leading-relaxed text-[11px] text-slate-500">
          Tài liệu đánh giá kỹ thuật trung lập gửi Ban Giám Đốc trước khi duyệt ngân sách quảng cáo.
        </p>
      </div>
    </aside>'''

new_sub = '''    <!-- 2. CONTEXTUAL SUB-SIDEBAR (280px fixed bên cạnh Rail - Chống nhảy chữ & Ghim cố định) -->
    <aside class="fixed top-14 left-[60px] bottom-0 w-[280px] bg-white border-r border-slate-200 hidden xl:flex flex-col p-3 z-20 overflow-y-auto">
      <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-3 px-2 flex items-center justify-between shrink-0">
        <span>Đề Mục Thẩm Định</span>
        <span class="bg-slate-100 text-slate-600 px-1.5 py-0.5 rounded text-[10px]">v3.6</span>
      </div>
      <nav class="space-y-1 text-xs font-medium">
        <a href="#tong-quan" class="nav-sub-item flex items-center justify-between px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors active gap-2">
          <span class="whitespace-nowrap font-medium text-slate-800 text-xs">1. Bức Tranh Tổng Thể</span>
          <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded whitespace-nowrap shrink-0">4 KPI</span>
        </a>
        <a href="#diem-nghen-chuyen-doi" class="nav-sub-item flex items-center justify-between px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors gap-2">
          <span class="whitespace-nowrap font-medium text-slate-800 text-xs">2. Điểm Nghẽn Thất Thoát</span>
          <span class="text-[10px] bg-red-100 text-red-800 font-bold px-2 py-0.5 rounded whitespace-nowrap shrink-0">6 P0</span>
        </a>
        <a href="#doi-sanh-truoc-sau" class="nav-sub-item flex items-center justify-between px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors gap-2">
          <span class="whitespace-nowrap font-medium text-slate-800 text-xs">3. Đối Sánh Trước/Sau</span>
          <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded whitespace-nowrap shrink-0">3 Cặp</span>
        </a>
        <a href="#bang-uu-tien-p0-p3" class="nav-sub-item flex items-center justify-between px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors gap-2">
          <span class="whitespace-nowrap font-medium text-slate-800 text-xs">4. Bảng Ưu Tiên Xử Lý</span>
          <span class="text-[10px] bg-amber-100 text-amber-800 font-bold px-2 py-0.5 rounded whitespace-nowrap shrink-0">14 Mục</span>
        </a>
        <a href="#kien-truc-sitemap" class="nav-sub-item flex items-center justify-between px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors gap-2">
          <span class="whitespace-nowrap font-medium text-slate-800 text-xs">5. Sitemap & RFQ Hub</span>
          <span class="text-[10px] bg-indigo-100 text-indigo-800 font-bold px-2 py-0.5 rounded whitespace-nowrap shrink-0">5 Nhóm</span>
        </a>
        <a href="#blueprint-sections" class="nav-sub-item flex items-center justify-between px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors gap-2">
          <span class="whitespace-nowrap font-medium text-slate-800 text-xs">6. Blueprint Sections</span>
          <span class="text-[10px] bg-blue-100 text-blue-800 font-bold px-2 py-0.5 rounded whitespace-nowrap shrink-0">7 Khối</span>
        </a>
        <a href="#luu-y-google-ads" class="nav-sub-item flex items-center justify-between px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors gap-2">
          <span class="whitespace-nowrap font-medium text-slate-800 text-xs">7. Lưu Ý Google Ads</span>
          <span class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded whitespace-nowrap shrink-0">4 Trụ Cột</span>
        </a>
      </nav>

      <div class="mt-auto pt-4 border-t border-slate-200 shrink-0">
        <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs">
          <div class="flex items-center gap-1.5 font-bold text-slate-800 mb-1">
            <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-600 shrink-0"></i>
            <span class="whitespace-nowrap">Thẩm Định Độc Lập</span>
          </div>
          <p class="leading-relaxed text-[11px] text-slate-500">
            Tài liệu đánh giá kỹ thuật trung lập gửi Ban Giám Đốc trước khi duyệt ngân sách quảng cáo.
          </p>
        </div>
      </div>
    </aside>'''

# 3. Update main workspace margin to accommodate fixed sidebars
old_main = '''    <!-- 3. MAIN WORKSPACE (Max-width 1280px Grid 70/30) -->
    <main class="flex-1 p-3 sm:p-6 lg:p-8 space-y-10 max-w-[1280px] w-full mx-auto min-w-0">'''

new_main = '''    <!-- 3. MAIN WORKSPACE (Max-width 1280px Grid 70/30 - Offset for Fixed Sidebars) -->
    <main class="flex-1 p-3 sm:p-6 lg:p-8 space-y-10 max-w-[1280px] w-full min-w-0 lg:ml-[60px] xl:ml-[340px]">'''

# 4. Add Scrollspy in JS
old_js_end = '''    function filterTablePriority(prio, btn) {'''

new_js_scrollspy = '''    // Scrollspy for Sidebars
    const sections = document.querySelectorAll('section[id]');
    const railBtns = document.querySelectorAll('.rail-btn');
    const subNavItems = document.querySelectorAll('.nav-sub-item');

    function updateActiveNav() {
      const scrollY = window.pageYOffset + 140;
      sections.forEach(sec => {
        const secTop = sec.offsetTop;
        const secHeight = sec.offsetHeight;
        const id = sec.getAttribute('id');
        if (scrollY >= secTop && scrollY < secTop + secHeight) {
          railBtns.forEach(btn => {
            if (btn.getAttribute('href') === '#' + id) {
              btn.classList.add('active');
            } else {
              btn.classList.remove('active');
            }
          });
          subNavItems.forEach(item => {
            if (item.getAttribute('href') === '#' + id) {
              item.classList.add('active');
            } else {
              item.classList.remove('active');
            }
          });
        }
      });
    }
    window.addEventListener('scroll', updateActiveNav, { passive: true });
    window.addEventListener('load', updateActiveNav);

    function filterTablePriority(prio, btn) {'''

if old_rail in code:
    code = code.replace(old_rail, new_rail)
    print("Replaced old_rail successfully")
else:
    print("WARNING: old_rail not found")

if old_sub in code:
    code = code.replace(old_sub, new_sub)
    print("Replaced old_sub successfully")
else:
    print("WARNING: old_sub not found")

if old_main in code:
    code = code.replace(old_main, new_main)
    print("Replaced old_main successfully")
else:
    print("WARNING: old_main not found")

if old_js_end in code:
    code = code.replace(old_js_end, new_js_scrollspy)
    print("Added scrollspy JS successfully")
else:
    print("WARNING: old_js_end not found")

with open(script_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated bien_tap_cau_chu.py successfully!")
