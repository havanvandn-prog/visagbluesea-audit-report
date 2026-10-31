import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Cập nhật CSS cho Single Unified Sidebar
old_css_snippet = """    .rail-btn.active {
      background-color: #ecfdf5;
      color: #01a915;
    }
    .rail-btn.active::before {
      content: '';
      position: absolute;
      left: 0;
      top: 6px;
      bottom: 6px;
      width: 3px;
      background-color: #01a915;
      border-top-right-radius: 3px;
      border-bottom-right-radius: 3px;
    }
    
    .nav-sub-item.active {
      background-color: #ecfdf5;
      color: #01a915;
      font-weight: 700;
    }"""

new_css_snippet = """    /* Single Unified Sidebar Active Style */
    .sidebar-nav-item.active {
      background-color: #ffffff;
      color: #01a915;
      font-weight: 700;
      box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
      border-left: 3px solid #01a915;
    }
    .sidebar-nav-item.active i {
      color: #01a915 !important;
    }"""

if old_css_snippet in text:
    text = text.replace(old_css_snippet, new_css_snippet, 1)
    print("Updated CSS successfully!")
else:
    print("Warning: old_css_snippet not found, using regex...")
    text = re.sub(r'\.rail-btn\.active\s*\{.*?\.nav-sub-item\.active\s*\{.*?\}', new_css_snippet, text, flags=re.DOTALL)

# 2. Xóa 2 aside cũ và thay bằng 1 Single Unified Sidebar
# Tìm từ đầu aside 1 đến hết aside 2
asides_pattern = r'<!-- 1\. DESKTOP MINI ICON RAIL.*?<!-- 2\. SUB-SIDEBAR.*?<!-- Thẩm định độc lập card -->\s*</div>\s*</aside>|<!-- 1\. DESKTOP MINI ICON RAIL.*?</aside>\s*<!-- 2\. SUB-SIDEBAR.*?</aside>|<aside class="fixed top-14 left-0 bottom-0 w-\[60px\].*?</aside>\s*<aside class="fixed top-14 left-\[60px\].*?</aside>'

single_sidebar_html = """<!-- ================= SINGLE UNIFIED SIDEBAR (GỘP ICON & TÊN ĐỀ MỤC) ================= -->
    <aside class="fixed top-14 left-0 bottom-0 w-[270px] bg-slate-50/90 backdrop-blur-md border-r border-slate-200 hidden md:flex flex-col py-6 px-3.5 space-y-4 z-30 overflow-y-auto no-scrollbar">
      <div>
        <div class="flex items-center justify-between text-xs font-bold text-slate-400 uppercase tracking-wider px-2 mb-3">
          <span>Đề Mục Thẩm Định</span>
          <span class="px-2 py-0.5 rounded bg-slate-200/60 text-slate-600 text-[10px]">V3.6</span>
        </div>
        
        <nav class="space-y-1.5">
          <!-- Mục 1 -->
          <a href="#tong-quan" class="sidebar-nav-item flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-white hover:shadow-2xs transition-all active">
            <span class="flex items-center gap-2.5 truncate">
              <i data-lucide="layout-dashboard" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span class="truncate">1. Bức Tranh Tổng Thể</span>
            </span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-md bg-emerald-100 text-emerald-800 whitespace-nowrap shrink-0">4 KPI</span>
          </a>

          <!-- Mục 2 -->
          <a href="#diem-nghen-chuyen-doi" class="sidebar-nav-item flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-white hover:shadow-2xs transition-all">
            <span class="flex items-center gap-2.5 truncate">
              <i data-lucide="alert-octagon" class="w-4 h-4 text-red-500 shrink-0"></i>
              <span class="truncate">2. Điểm Nghẽn & Đối Sánh</span>
            </span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-md bg-red-100 text-red-700 whitespace-nowrap shrink-0">4 P0</span>
          </a>

          <!-- Mục 3 -->
          <a href="#bang-uu-tien-p0-p3" class="sidebar-nav-item flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-white hover:shadow-2xs transition-all">
            <span class="flex items-center gap-2.5 truncate">
              <i data-lucide="list-checks" class="w-4 h-4 text-amber-500 shrink-0"></i>
              <span class="truncate">3. Bảng Ưu Tiên Xử Lý</span>
            </span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-md bg-amber-100 text-amber-800 whitespace-nowrap shrink-0">9 Mục</span>
          </a>

          <!-- Mục 4 -->
          <a href="#kien-truc-sitemap" class="sidebar-nav-item flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-white hover:shadow-2xs transition-all">
            <span class="flex items-center gap-2.5 truncate">
              <i data-lucide="network" class="w-4 h-4 text-indigo-500 shrink-0"></i>
              <span class="truncate">4. Sitemap & RFQ Hub</span>
            </span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-md bg-indigo-100 text-indigo-800 whitespace-nowrap shrink-0">5 Nhóm</span>
          </a>

          <!-- Mục 5 -->
          <a href="#blueprint-sections" class="sidebar-nav-item flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-white hover:shadow-2xs transition-all">
            <span class="flex items-center gap-2.5 truncate">
              <i data-lucide="layers" class="w-4 h-4 text-blue-500 shrink-0"></i>
              <span class="truncate">5. Blueprint Từng Khối</span>
            </span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-md bg-blue-100 text-blue-800 whitespace-nowrap shrink-0">7 Khối</span>
          </a>

          <!-- Mục 6 -->
          <a href="#luu-y-google-ads" class="sidebar-nav-item flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-white hover:shadow-2xs transition-all">
            <span class="flex items-center gap-2.5 truncate">
              <i data-lucide="target" class="w-4 h-4 text-emerald-600 shrink-0"></i>
              <span class="truncate">6. Lưu Ý Google Ads</span>
            </span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-md bg-emerald-100 text-emerald-800 whitespace-nowrap shrink-0">4 Trụ Cột</span>
          </a>
        </nav>
      </div>
    </aside>"""

# Tìm vị trí bắt đầu của aside 1 và kết thúc của aside 2
idx_aside1 = text.find('<aside class="fixed top-14 left-0 bottom-0 w-[60px]')
idx_aside2 = text.find('<aside class="fixed top-14 left-[60px]')
idx_aside2_end = text.find('</aside>', idx_aside2) + len('</aside>')

if idx_aside1 != -1 and idx_aside2 != -1:
    text = text[:idx_aside1] + single_sidebar_html + text[idx_aside2_end:]
    print("Replaced 2-tier sidebars with Single Unified Sidebar successfully!")
else:
    print("Could not find aside tags via exact string search, testing regex...")
    m = re.search(asides_pattern, text, re.DOTALL)
    if m:
        text = text[:m.start()] + single_sidebar_html + text[m.end():]
        print("Replaced sidebars via regex!")

# 3. Cập nhật thẻ <main>
# Thay lg:ml-[60px] xl:ml-[340px] bằng md:ml-[270px]
text = re.sub(
    r'<main class="([^"]*)lg:ml-\[60px\] xl:ml-\[340px\]([^"]*)">',
    r'<main class="\1md:ml-[270px]\2">',
    text
)
text = text.replace(
    '<main class="flex-1 p-3 sm:p-6 lg:p-8 space-y-10 max-w-[1280px] w-full min-w-0 lg:ml-[60px] xl:ml-[340px]">',
    '<main class="flex-1 p-3 sm:p-6 lg:p-8 space-y-10 max-w-[1280px] w-full min-w-0 md:ml-[270px]">'
)

# 4. Cập nhật Scrollspy Javascript
old_scrollspy = re.search(r'// Scrollspy for Sidebars.*?window\.addEventListener\(\'scroll\'.*?\}\);\s*\}\);', text, re.DOTALL)
new_scrollspy = """    // Scrollspy for Single Unified Sidebar
    const sections = document.querySelectorAll('section[id]');
    const sidebarNavItems = document.querySelectorAll('.sidebar-nav-item');

    window.addEventListener('scroll', () => {
      let current = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop - 120;
        if (window.scrollY >= sectionTop) {
          current = section.getAttribute('id');
        }
      });

      sidebarNavItems.forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('href') === `#${current}`) {
          item.classList.add('active');
        }
      });
    });"""

if old_scrollspy:
    text = text.replace(old_scrollspy.group(0), new_scrollspy, 1)
    print("Updated Scrollspy Javascript successfully!")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated bien_tap_cau_chu.py with Single Unified Sidebar!")
