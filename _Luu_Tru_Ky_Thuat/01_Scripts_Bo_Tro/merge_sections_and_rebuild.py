import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Đọc toàn bộ nội dung hiện tại
script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

# ==========================================
# 1. CẬP NHẬT MINI ICON RAIL (60px) - 6 MỤC
# ==========================================
old_rail = re.search(r'<aside class="fixed top-14 left-0 bottom-0 w-\[60px\].*?</aside>', text, re.DOTALL)

new_rail = """<aside class="fixed top-14 left-0 bottom-0 w-[60px] bg-white border-r border-slate-200 hidden lg:flex flex-col items-center py-4 space-y-4 z-30">
      <a href="#tong-quan" class="rail-btn relative p-2.5 rounded-xl text-slate-600 hover:text-emerald-600 hover:bg-slate-50 transition-colors group flex items-center justify-center active" title="1. Bức Tranh Tổng Thể">
        <i data-lucide="layout-dashboard" class="w-5 h-5"></i>
        <span class="absolute left-full ml-3 px-2.5 py-1 bg-slate-900 text-white text-[11px] font-semibold rounded-md shadow-md whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-50">
          1. Bức Tranh Tổng Thể
        </span>
      </a>
      
      <a href="#diem-nghen-chuyen-doi" class="rail-btn relative p-2.5 rounded-xl text-slate-600 hover:text-red-600 hover:bg-slate-50 transition-colors group flex items-center justify-center" title="2. Điểm Nghẽn & Đối Sánh">
        <i data-lucide="alert-octagon" class="w-5 h-5 text-red-500"></i>
        <span class="absolute left-full ml-3 px-2.5 py-1 bg-slate-900 text-white text-[11px] font-semibold rounded-md shadow-md whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-50">
          2. Điểm Nghẽn & Đối Sánh (4 P0)
        </span>
      </a>

      <a href="#bang-uu-tien-p0-p3" class="rail-btn relative p-2.5 rounded-xl text-slate-600 hover:text-amber-600 hover:bg-slate-50 transition-colors group flex items-center justify-center" title="3. Bảng Ưu Tiên Xử Lý">
        <i data-lucide="list-checks" class="w-5 h-5"></i>
        <span class="absolute left-full ml-3 px-2.5 py-1 bg-slate-900 text-white text-[11px] font-semibold rounded-md shadow-md whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-50">
          3. Bảng Ưu Tiên Xử Lý (9 Mục)
        </span>
      </a>

      <a href="#kien-truc-sitemap" class="rail-btn relative p-2.5 rounded-xl text-slate-600 hover:text-indigo-600 hover:bg-slate-50 transition-colors group flex items-center justify-center" title="4. Sitemap & RFQ Hub">
        <i data-lucide="network" class="w-5 h-5"></i>
        <span class="absolute left-full ml-3 px-2.5 py-1 bg-slate-900 text-white text-[11px] font-semibold rounded-md shadow-md whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-50">
          4. Sitemap & RFQ Hub
        </span>
      </a>

      <a href="#blueprint-sections" class="rail-btn relative p-2.5 rounded-xl text-slate-600 hover:text-blue-600 hover:bg-slate-50 transition-colors group flex items-center justify-center" title="5. Blueprint Bố Cục Trang Lõi">
        <i data-lucide="layers" class="w-5 h-5"></i>
        <span class="absolute left-full ml-3 px-2.5 py-1 bg-slate-900 text-white text-[11px] font-semibold rounded-md shadow-md whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-50">
          5. Blueprint Bố Cục Trang Lõi
        </span>
      </a>

      <a href="#luu-y-google-ads" class="rail-btn relative p-2.5 rounded-xl text-slate-600 hover:text-emerald-600 hover:bg-slate-50 transition-colors group flex items-center justify-center" title="6. Lưu Ý Google Ads">
        <i data-lucide="target" class="w-5 h-5"></i>
        <span class="absolute left-full ml-3 px-2.5 py-1 bg-slate-900 text-white text-[11px] font-semibold rounded-md shadow-md whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none z-50">
          6. Lưu Ý Google Ads
        </span>
      </a>
    </aside>"""

if old_rail:
    text = text.replace(old_rail.group(0), new_rail, 1)
    print("Updated Mini Icon Rail successfully!")

# ==========================================
# 2. CẬP NHẬT SUB-SIDEBAR (280px) - 6 MỤC
# ==========================================
old_sub_sidebar = re.search(r'<aside class="fixed top-14 left-\[60px\] bottom-0 w-\[280px\].*?</aside>', text, re.DOTALL)

new_sub_sidebar = """<aside class="fixed top-14 left-[60px] bottom-0 w-[280px] bg-slate-50/70 border-r border-slate-200 hidden md:flex flex-col py-6 px-4 space-y-6 z-20">
      <div>
        <div class="flex items-center justify-between text-xs font-bold text-slate-400 uppercase tracking-wider px-2 mb-3">
          <span>Đề Mục Thẩm Định</span>
          <span class="px-2 py-0.5 rounded bg-slate-200/60 text-slate-600 text-[10px]">V3.6</span>
        </div>
        
        <nav class="space-y-1">
          <a href="#tong-quan" class="sub-nav-item flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-white hover:shadow-2xs transition-all active">
            <span class="flex items-center gap-2">
              <span class="font-bold text-emerald-600">1.</span>
              <span>Bức Tranh Tổng Thể</span>
            </span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-md bg-emerald-100 text-emerald-800 whitespace-nowrap">4 KPI</span>
          </a>

          <a href="#diem-nghen-chuyen-doi" class="sub-nav-item flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-white hover:shadow-2xs transition-all">
            <span class="flex items-center gap-2">
              <span class="font-bold text-red-600">2.</span>
              <span>Điểm Nghẽn & Đối Sánh</span>
            </span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-md bg-red-100 text-red-700 whitespace-nowrap">4 P0</span>
          </a>

          <a href="#bang-uu-tien-p0-p3" class="sub-nav-item flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-white hover:shadow-2xs transition-all">
            <span class="flex items-center gap-2">
              <span class="font-bold text-amber-600">3.</span>
              <span>Bảng Ưu Tiên Xử Lý</span>
            </span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-md bg-amber-100 text-amber-800 whitespace-nowrap">9 Mục</span>
          </a>

          <a href="#kien-truc-sitemap" class="sub-nav-item flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-white hover:shadow-2xs transition-all">
            <span class="flex items-center gap-2">
              <span class="font-bold text-indigo-600">4.</span>
              <span>Sitemap & RFQ Hub</span>
            </span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-md bg-indigo-100 text-indigo-800 whitespace-nowrap">5 Nhóm</span>
          </a>

          <a href="#blueprint-sections" class="sub-nav-item flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-white hover:shadow-2xs transition-all">
            <span class="flex items-center gap-2">
              <span class="font-bold text-blue-600">5.</span>
              <span>Blueprint Từng Khối</span>
            </span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-md bg-blue-100 text-blue-800 whitespace-nowrap">7 Khối</span>
          </a>

          <a href="#luu-y-google-ads" class="sub-nav-item flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-semibold text-slate-700 hover:bg-white hover:shadow-2xs transition-all">
            <span class="flex items-center gap-2">
              <span class="font-bold text-emerald-600">6.</span>
              <span>Lưu Ý Google Ads</span>
            </span>
            <span class="px-2 py-0.5 text-xs font-bold rounded-md bg-emerald-100 text-emerald-800 whitespace-nowrap">4 Trụ Cột</span>
          </a>
        </nav>
      </div>

      <!-- Thẩm định độc lập card -->
      <div class="mt-auto bg-white rounded-xl p-3.5 border border-slate-200/80 shadow-2xs space-y-2">
        <div class="flex items-center gap-2 text-slate-900 font-bold text-xs">
          <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600 shrink-0"></i>
          <span>Thẩm Định Độc Lập</span>
        </div>
        <p class="text-[11px] text-slate-500 leading-relaxed">
          Tài liệu đánh giá kỹ thuật trung lập gửi Ban Giám Đốc trước khi duyệt ngân sách quảng cáo.
        </p>
      </div>
    </aside>"""

if old_sub_sidebar:
    text = text.replace(old_sub_sidebar.group(0), new_sub_sidebar, 1)
    print("Updated Sub-Sidebar successfully!")

# ==========================================
# 3. DỰNG SECTION 2 HOÀN TOÀN MỚI: TÍCH HỢP TRỰC QUAN TRƯỚC/SAU VÀO 4 CARD P0
# ==========================================
new_section_2 = """<!-- ================= SECTION 2: ĐIỂM NGHẼN & ĐỐI SÁNH TRỰC QUAN (TRƯỚC / SAU) ================= -->
      <section id="diem-nghen-chuyen-doi" class="space-y-6">
        <div class="border-b border-slate-200 pb-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <h2 class="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
              <span class="w-2.5 h-6 bg-red-600 rounded-full inline-block"></span>
              2. Các Điểm Nghẽn Thất Thoát & Đối Sánh Trực Quan (Trước / Sau)
            </h2>
            <p class="text-slate-500 text-xs sm:text-sm mt-0.5">Phân tích thực tế kèm hình ảnh bằng chứng lỗi hiện tại và bản vẽ phương án đề xuất sau tối ưu.</p>
          </div>

          <!-- Interactive Filter Tabs -->
          <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1">
            <button onclick="filterFindings('all', this)" class="filter-pill active px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              Tất Cả (4 P0)
            </button>
            <button onclick="filterFindings('ui', this)" class="filter-pill px-3 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              Giao Diện & Mobile (4)
            </button>
          </div>
        </div>

        <div id="findings-container" class="space-y-6">

          <!-- ================= CARD 1: DESKTOP HERO & CỤM CONTACT ĐÈ CHỮ ================= -->
          <div class="finding-card bg-white rounded-2xl border border-slate-200 shadow-2xs overflow-hidden space-y-4" data-cat="ui">
            <!-- Header Card -->
            <div class="p-4 sm:p-5 bg-slate-50/80 border-b border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div class="flex items-center gap-2.5 flex-wrap">
                <span class="badge-p0 text-[11px] font-bold px-2.5 py-1 rounded whitespace-nowrap shrink-0">P0 Khẩn Cấp</span>
                <h3 class="text-sm sm:text-base font-bold text-slate-900">
                  Điểm Nghẽn 01: Cụm Nút Liên Hệ & Header Rối Mắt, Đè Lên Tiêu Đề Trên Desktop
                </h3>
              </div>
              <a href="https://www.visagbluesea.com/" target="_blank" class="text-xs text-emerald-600 hover:text-emerald-700 flex items-center gap-1 font-semibold whitespace-nowrap">
                <span>Soi trực tiếp trang chủ</span> <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
              </a>
            </div>

            <!-- Tóm Tắt Phân Tích Thực Tế -->
            <div class="px-4 sm:px-5 space-y-2 text-xs sm:text-sm text-slate-600 leading-relaxed">
              <p><strong>Vấn đề:</strong> Header hiển thị cùng lúc 3 số điện thoại không rõ phân biệt, nút "Call now:" bị ẩn mất số. Đặc biệt, cụm nút Zalo & WhatsApp nổi sườn trái bị định vị lệch, chèn ngang đè bẹp lên tiêu đề chính H1 và đoạn mở đầu trên màn hình máy tính.</p>
              <p><strong>Ảnh hưởng:</strong> Khiến khách hàng VIP (EB-5 20 tỷ) vừa vào đã thấy giao diện bị đè chữ méo mó; khách phân vân không biết bấm số nào, thất thoát ~35% cuộc gọi tư vấn.</p>
              <p><strong>Cách xử lý:</strong> Gỡ bỏ cụm nút nổi che chữ ở sườn trái; rút gọn Header còn 1 Hotline chính (0901.830.827) + 1 Zalo nổi bật, tích hợp cụm chuyển đổi kép (Form 3 bước mini + Hotline trực tiếp).</p>
            </div>

            <!-- Khối Đối Sánh Trực Quan Trước / Sau (Before / After) -->
            <div class="px-4 sm:px-5 pb-5">
              <div class="bg-slate-50 rounded-xl p-3 sm:p-4 border border-slate-200 space-y-4">
                <div class="flex items-center justify-between border-b border-slate-200 pb-2">
                  <span class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                    <i data-lucide="split" class="w-4 h-4 text-emerald-600"></i>
                    Đối Sánh Trực Quan: Hiện Trạng Thực Tế vs Phương Án Sau Tối Ưu
                  </span>
                  <span class="text-[11px] text-slate-400 italic">Nhấp vào hình để phóng to toàn màn hình</span>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
                  <!-- Cột Trái: Hiện trạng -->
                  <div class="space-y-2.5">
                    <div class="flex items-center justify-between">
                      <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-xs font-bold bg-red-100 text-red-800">
                        <span class="w-2 h-2 rounded-full bg-red-600"></span> ❌ Hiện Trạng Thực Tế (Ảnh Chụp)
                      </span>
                      <span class="text-[11px] text-slate-400">Desktop View</span>
                    </div>
                    <div class="border border-slate-200 rounded-xl overflow-hidden bg-white relative group cursor-pointer shadow-2xs" onclick="openLightbox('Bang_Chung_Hinh_Anh/desktop_homepage_view.png', 'Hiện trạng: Header 3 số điện thoại rối mắt, cụm widget Zalo nổi sườn trái đè ngang qua tiêu đề H1 và văn bản')">
                      <img src="Bang_Chung_Hinh_Anh/desktop_homepage_view.png" alt="Hiện trạng Header và Hero Desktop" class="w-full h-auto object-cover aspect-[16/10] group-hover:scale-105 transition-transform duration-300">
                      <div class="absolute inset-0 bg-slate-900/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                        <i data-lucide="maximize-2" class="w-4 h-4"></i>
                        <span>Nhấp để phóng to chi tiết</span>
                      </div>
                    </div>
                    <ul class="text-xs text-slate-600 space-y-1 bg-white p-3 rounded-lg border border-slate-200">
                      <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Cụm nút Zalo & WhatsApp nổi sườn trái đè trực tiếp lên chữ tiêu đề H1.</li>
                      <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Header dồn 3 số điện thoại không chú thích, chữ "Call now:" bị mất số.</li>
                      <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Thiếu form thẩm định nhanh và nút nhận tư vấn trực diện.</li>
                    </ul>
                  </div>

                  <!-- Cột Phải: Phương án mẫu -->
                  <div class="space-y-2.5">
                    <div class="flex items-center justify-between">
                      <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-xs font-bold bg-emerald-100 text-emerald-800">
                        <span class="w-2 h-2 rounded-full bg-emerald-600"></span> ✨ Phương Án Sau Tối Ưu (Phương Án Mẫu)
                      </span>
                      <span class="text-[11px] text-emerald-700 font-semibold">Tỷ lệ 16:9 Chuẩn CRO</span>
                    </div>
                    <div class="border border-emerald-300 rounded-xl overflow-hidden bg-white relative group cursor-pointer shadow-sm" onclick="openLightbox('Bang_Chung_Hinh_Anh/phuong_an_mau_desktop_hero.jpg', 'Phương án mẫu: Hero Banner chuẩn nhận diện Emerald, Headline định vị mạnh mẽ, Cặp nút CTA kép và Form 3 trường tinh gọn')">
                      <img src="Bang_Chung_Hinh_Anh/phuong_an_mau_desktop_hero.jpg" alt="Phương án mẫu Hero Banner" class="w-full h-auto object-cover aspect-[16/10] group-hover:scale-105 transition-transform duration-300">
                      <div class="absolute inset-0 bg-emerald-950/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                        <i data-lucide="maximize-2" class="w-4 h-4"></i>
                        <span>Nhấp để phóng to chi tiết</span>
                      </div>
                    </div>
                    <ul class="text-xs text-slate-700 space-y-1 bg-white p-3 rounded-lg border border-emerald-200">
                      <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Tiêu đề định vị mạnh mẽ:</strong> "Tư Vấn Định Cư, Đầu Tư & Visa Toàn Cầu".</li>
                      <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Cặp nút hành động kép:</strong> [Nhận Thẩm Định Hồ Sơ] + Hotline [0901.830.827].</li>
                      <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Form thẩm định mini:</strong> 3 trường nhập liệu mượt mà, phản hồi sau 15 phút.</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <!-- Footer Card -->
            <div class="px-4 sm:px-5 py-3 bg-slate-50 border-t border-slate-200 text-xs text-slate-700 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <span class="flex items-center gap-1.5"><i data-lucide="search" class="w-3.5 h-3.5 text-slate-500 shrink-0"></i> Mở trang chủ trên máy tính, quan sát góc trái và thanh Header.</span>
              <span class="text-red-600 font-bold whitespace-nowrap">Thất thoát: ~35% cuộc gọi tư vấn</span>
            </div>
          </div>


          <!-- ================= CARD 2: MOBILE THUMB ZONE & STICKY BAR ================= -->
          <div class="finding-card bg-white rounded-2xl border border-slate-200 shadow-2xs overflow-hidden space-y-4" data-cat="ui">
            <!-- Header Card -->
            <div class="p-4 sm:p-5 bg-slate-50/80 border-b border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div class="flex items-center gap-2.5 flex-wrap">
                <span class="badge-p0 text-[11px] font-bold px-2.5 py-1 rounded whitespace-nowrap shrink-0">P0 Khẩn Cấp</span>
                <h3 class="text-sm sm:text-base font-bold text-slate-900">
                  Điểm Nghẽn 02: Thiếu Thanh Nút Bấm Cố Định Dưới Đáy Màn Hình Điện Thoại (Thumb Zone)
                </h3>
              </div>
              <a href="https://www.visagbluesea.com/" target="_blank" class="text-xs text-emerald-600 hover:text-emerald-700 flex items-center gap-1 font-semibold whitespace-nowrap">
                <span>Kiểm tra trên di động</span> <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
              </a>
            </div>

            <!-- Tóm Tắt Phân Tích Thực Tế -->
            <div class="px-4 sm:px-5 space-y-2 text-xs sm:text-sm text-slate-600 leading-relaxed">
              <p><strong>Vấn đề:</strong> Website không có nút gọi điện hay Zalo cố định ở chân màn hình điện thoại khi khách hàng cuộn trang tìm hiểu thông tin.</p>
              <p><strong>Ảnh hưởng:</strong> Hơn 75% khách hàng dùng điện thoại; khi đọc hết điều kiện visa phải cuộn ngược lên đầu trang để tìm số, khiến 50% khách nản lòng và thoát trang.</p>
              <p><strong>Cách xử lý:</strong> Gắn thanh cố định đáy màn hình (Mobile Sticky Action Bar) gồm 2 nút lớn: [📞 Gọi Hotline 24/7: 0901.830.827] và [💬 Chat Zalo].</p>
            </div>

            <!-- Khối Đối Sánh Trực Quan Trước / Sau (Before / After) -->
            <div class="px-4 sm:px-5 pb-5">
              <div class="bg-slate-50 rounded-xl p-3 sm:p-4 border border-slate-200 space-y-4">
                <div class="flex items-center justify-between border-b border-slate-200 pb-2">
                  <span class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                    <i data-lucide="smartphone" class="w-4 h-4 text-emerald-600"></i>
                    Đối Sánh Trực Quan: Trải Nghiệm Lướt Web Trên Smartphone
                  </span>
                  <span class="text-[11px] text-slate-400 italic">Nhấp vào hình để phóng to chi tiết</span>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
                  <!-- Cột Trái: Hiện trạng Mobile -->
                  <div class="space-y-2.5">
                    <div class="flex items-center justify-between">
                      <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-xs font-bold bg-red-100 text-red-800">
                        <span class="w-2 h-2 rounded-full bg-red-600"></span> ❌ Hiện Trạng Trên Smartphone
                      </span>
                      <span class="text-[11px] text-slate-400">Mobile View 390x844</span>
                    </div>
                    <div class="border border-slate-200 rounded-xl overflow-hidden bg-white relative group cursor-pointer flex justify-center py-4 shadow-2xs" onclick="openLightbox('Bang_Chung_Hinh_Anh/mobile_homepage_view.png', 'Hiện trạng Mobile: Chân màn hình trống trơn, khách hàng cuộn dọc không có nút liên hệ')">
                      <img src="Bang_Chung_Hinh_Anh/mobile_homepage_view.png" alt="Hiện trạng Mobile" class="max-h-[380px] w-auto object-contain rounded-lg shadow-sm group-hover:scale-105 transition-transform duration-300">
                      <div class="absolute inset-0 bg-slate-900/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                        <i data-lucide="maximize-2" class="w-4 h-4"></i>
                        <span>Nhấp để phóng to</span>
                      </div>
                    </div>
                    <ul class="text-xs text-slate-600 space-y-1 bg-white p-3 rounded-lg border border-slate-200">
                      <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Chân màn hình hoàn toàn trống trơn, không có nút liên hệ nhanh.</li>
                      <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Khách đọc hết thông tin phải mất công cuộn ngược lên đầu trang.</li>
                    </ul>
                  </div>

                  <!-- Cột Phải: Phương án mẫu Mobile Sticky Bar -->
                  <div class="space-y-2.5">
                    <div class="flex items-center justify-between">
                      <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-xs font-bold bg-emerald-100 text-emerald-800">
                        <span class="w-2 h-2 rounded-full bg-emerald-600"></span> ✨ Phương Án Sau Tối Ưu (Phương Án Mẫu)
                      </span>
                      <span class="text-[11px] text-emerald-700 font-semibold">Tỷ lệ 9:16 Chuẩn Mobile UX</span>
                    </div>
                    <div class="border border-emerald-300 rounded-xl overflow-hidden bg-white relative group cursor-pointer flex justify-center py-4 shadow-sm" onclick="openLightbox('Bang_Chung_Hinh_Anh/phuong_an_mau_mobile_sticky_bar.jpg', 'Phương án mẫu Mobile: Thanh Sticky Action Bar cố định đáy với 2 nút [Gọi Hotline 24/7] + [Zalo Tư Vấn] hỗ trợ Thumb Zone')">
                      <img src="Bang_Chung_Hinh_Anh/phuong_an_mau_mobile_sticky_bar.jpg" alt="Phương án mẫu Mobile Sticky Bar" class="max-h-[380px] w-auto object-contain rounded-lg shadow-sm group-hover:scale-105 transition-transform duration-300">
                      <div class="absolute inset-0 bg-emerald-950/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                        <i data-lucide="maximize-2" class="w-4 h-4"></i>
                        <span>Nhấp để phóng to</span>
                      </div>
                    </div>
                    <ul class="text-xs text-slate-700 space-y-1 bg-white p-3 rounded-lg border border-emerald-200">
                      <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Thanh Sticky Bar cố định đáy:</strong> Luôn nằm trong tầm với ngón tay cái.</li>
                      <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Cụm 2 nút chạm trực tiếp:</strong> [📞 Gọi Hotline 24/7] và [💬 Chat Zalo Thẩm Định].</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <!-- Footer Card -->
            <div class="px-4 sm:px-5 py-3 bg-slate-50 border-t border-slate-200 text-xs text-slate-700 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <span class="flex items-center gap-1.5"><i data-lucide="smartphone" class="w-3.5 h-3.5 text-slate-500 shrink-0"></i> Mở web trên smartphone, cuộn xuống giữa trang không thấy nút liên hệ.</span>
              <span class="text-red-600 font-bold whitespace-nowrap">Thất thoát: ~50% khách hàng di động</span>
            </div>
          </div>


          <!-- ================= CARD 3: TRANG EB-5 & RFQ HUB ================= -->
          <div class="finding-card bg-white rounded-2xl border border-slate-200 shadow-2xs overflow-hidden space-y-4" data-cat="ui">
            <!-- Header Card -->
            <div class="p-4 sm:p-5 bg-slate-50/80 border-b border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div class="flex items-center gap-2.5 flex-wrap">
                <span class="badge-p0 text-[11px] font-bold px-2.5 py-1 rounded whitespace-nowrap shrink-0">P0 Khẩn Cấp</span>
                <h3 class="text-sm sm:text-base font-bold text-slate-900">
                  Điểm Nghẽn 03: Trang EB-5 Lộ Chữ Tiếng Tây Ban Nha "Acerca de" & Thiếu Phễu Dự Toán Chi Phí
                </h3>
              </div>
              <a href="https://www.visagbluesea.com/us-green-card-eb-5" target="_blank" class="text-xs text-emerald-600 hover:text-emerald-700 flex items-center gap-1 font-semibold whitespace-nowrap">
                <span>Soi trang EB-5</span> <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
              </a>
            </div>

            <!-- Tóm Tắt Phân Tích Thực Tế -->
            <div class="px-4 sm:px-5 space-y-2 text-xs sm:text-sm text-slate-600 leading-relaxed">
              <p><strong>Vấn đề:</strong> Trang EB-5 (khoản đầu tư 20 tỷ đồng) hiển thị tiêu đề tiếng Tây Ban Nha "Acerca de" do lỗi giao diện mẫu. Toàn trang chỉ có bài viết dài, thiếu bảng dự toán chi phí minh bạch và lộ trình nhận thẻ xanh.</p>
              <p><strong>Ảnh hưởng:</strong> Khiến nhà đầu tư VIP nghi ngờ năng lực pháp lý và sự chuyên nghiệp của doanh nghiệp; khách tò mò chi phí nhưng không tìm thấy thông tin nên thoát trang sang đối thủ.</p>
              <p><strong>Cách xử lý:</strong> Đổi tiêu đề thành "Đầu Tư Định Cư Mỹ EB-5 — Nhận Thẻ Xanh Cho Cả Gia Đình"; thiết lập Trung Tâm Báo Phí (RFQ Hub) cho phép chọn quốc gia và tải bảng dự toán chi phí chi tiết.</p>
            </div>

            <!-- Khối Đối Sánh Trực Quan Trước / Sau (Before / After) -->
            <div class="px-4 sm:px-5 pb-5">
              <div class="bg-slate-50 rounded-xl p-3 sm:p-4 border border-slate-200 space-y-4">
                <div class="flex items-center justify-between border-b border-slate-200 pb-2">
                  <span class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                    <i data-lucide="file-check-2" class="w-4 h-4 text-emerald-600"></i>
                    Đối Sánh Trực Quan: Trang Chi Tiết Dịch Vụ Định Cư vs Trung Tâm Báo Phí RFQ Hub
                  </span>
                  <span class="text-[11px] text-slate-400 italic">Nhấp vào hình để phóng to chi tiết</span>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
                  <!-- Cột Trái: Hiện trạng EB-5 -->
                  <div class="space-y-2.5">
                    <div class="flex items-center justify-between">
                      <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-xs font-bold bg-red-100 text-red-800">
                        <span class="w-2 h-2 rounded-full bg-red-600"></span> ❌ Hiện Trạng Trang EB-5
                      </span>
                      <span class="text-[11px] text-slate-400">Desktop 1440x900</span>
                    </div>
                    <div class="border border-slate-200 rounded-xl overflow-hidden bg-white relative group cursor-pointer shadow-2xs" onclick="openLightbox('Bang_Chung_Hinh_Anh/desktop_eb5_view.png', 'Hiện trạng: Trang EB-5 để sót chữ tiếng Tây Ban Nha Acerca de, nội dung thuần văn bản thiếu bảng dự toán')">
                      <img src="Bang_Chung_Hinh_Anh/desktop_eb5_view.png" alt="Hiện trạng Trang EB-5" class="w-full h-auto object-cover aspect-[16/10] group-hover:scale-105 transition-transform duration-300">
                      <div class="absolute inset-0 bg-slate-900/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                        <i data-lucide="maximize-2" class="w-4 h-4"></i>
                        <span>Nhấp để phóng to</span>
                      </div>
                    </div>
                    <ul class="text-xs text-slate-600 space-y-1 bg-white p-3 rounded-lg border border-slate-200">
                      <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Tiêu đề thẻ H1 hiển thị chữ tiếng Tây Ban Nha "Acerca de".</li>
                      <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Thiếu bảng dự toán chi phí đầu tư và lộ trình hoàn vốn minh bạch.</li>
                    </ul>
                  </div>

                  <!-- Cột Phải: Phương án mẫu RFQ Hub -->
                  <div class="space-y-2.5">
                    <div class="flex items-center justify-between">
                      <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-xs font-bold bg-emerald-100 text-emerald-800">
                        <span class="w-2 h-2 rounded-full bg-emerald-600"></span> ✨ Phương Án Sau Tối Ưu (Phương Án Mẫu)
                      </span>
                      <span class="text-[11px] text-emerald-700 font-semibold">Tỷ lệ 16:9 Chuẩn CRO</span>
                    </div>
                    <div class="border border-emerald-300 rounded-xl overflow-hidden bg-white relative group cursor-pointer shadow-sm" onclick="openLightbox('Bang_Chung_Hinh_Anh/phuong_an_mau_rfq_hub.jpg', 'Phương án mẫu RFQ Hub: Trung tâm dự toán chi phí định cư minh bạch, cho phép tải lộ trình thẻ xanh chi tiết')">
                      <img src="Bang_Chung_Hinh_Anh/phuong_an_mau_rfq_hub.jpg" alt="Phương án mẫu RFQ Hub" class="w-full h-auto object-cover aspect-[16/10] group-hover:scale-105 transition-transform duration-300">
                      <div class="absolute inset-0 bg-emerald-950/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                        <i data-lucide="maximize-2" class="w-4 h-4"></i>
                        <span>Nhấp để phóng to</span>
                      </div>
                    </div>
                    <ul class="text-xs text-slate-700 space-y-1 bg-white p-3 rounded-lg border border-emerald-200">
                      <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Tiêu đề chuẩn hóa 100% tiếng Việt:</strong> Khẳng định quyền lợi thẻ xanh Mỹ.</li>
                      <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Phễu RFQ Hub thông minh:</strong> Tải bảng dự toán chi phí chi tiết, thu thập lead VIP.</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <!-- Footer Card -->
            <div class="px-4 sm:px-5 py-3 bg-slate-50 border-t border-slate-200 text-xs text-slate-700 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <span class="flex items-center gap-1.5"><i data-lucide="search" class="w-3.5 h-3.5 text-slate-500 shrink-0"></i> Mở link EB-5, bấm F12 hoặc kiểm tra tiêu đề đầu trang sẽ thấy chữ "Acerca de".</span>
              <span class="text-red-600 font-bold whitespace-nowrap">Rủi ro: Mất niềm tin khách hàng VIP</span>
            </div>
          </div>


          <!-- ================= CARD 4: FORM TƯ VẤN ================= -->
          <div class="finding-card bg-white rounded-2xl border border-slate-200 shadow-2xs overflow-hidden space-y-4" data-cat="ui">
            <!-- Header Card -->
            <div class="p-4 sm:p-5 bg-slate-50/80 border-b border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div class="flex items-center gap-2.5 flex-wrap">
                <span class="badge-p0 text-[11px] font-bold px-2.5 py-1 rounded whitespace-nowrap shrink-0">P0 Khẩn Cấp</span>
                <h3 class="text-sm sm:text-base font-bold text-slate-900">
                  Điểm Nghẽn 04: Biểu Mẫu Tư Vấn Tách Ô Tên & Họ Riêng Biệt, Bắt Nhập Email
                </h3>
              </div>
              <a href="https://www.visagbluesea.com/contact-us" target="_blank" class="text-xs text-emerald-600 hover:text-emerald-700 flex items-center gap-1 font-semibold whitespace-nowrap">
                <span>Soi form liên hệ</span> <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
              </a>
            </div>

            <!-- Tóm Tắt Phân Tích Thực Tế -->
            <div class="px-4 sm:px-5 space-y-2 text-xs sm:text-sm text-slate-600 leading-relaxed">
              <p><strong>Vấn đề:</strong> Biểu mẫu tách riêng ô Họ và Tên, đồng thời bắt buộc nhập Email dù thói quen người Việt thích tư vấn nhanh qua Số điện thoại/Zalo.</p>
              <p><strong>Ảnh hưởng:</strong> Gây phiền toái khi gõ phím trên điện thoại, khiến 65% người dùng bỏ dở không gửi thông tin.</p>
              <p><strong>Cách xử lý:</strong> Rút gọn còn 3 ô: Họ tên, Số điện thoại/Zalo và Nhu cầu quan tâm. Chuyển Email thành tùy chọn không bắt buộc; cam kết gọi lại sau 15 phút.</p>
            </div>

            <!-- Khối Đối Sánh Trực Quan Trước / Sau (Before / After) -->
            <div class="px-4 sm:px-5 pb-5">
              <div class="bg-slate-50 rounded-xl p-3 sm:p-4 border border-slate-200 space-y-4">
                <div class="flex items-center justify-between border-b border-slate-200 pb-2">
                  <span class="text-xs font-bold text-slate-800 uppercase tracking-wider flex items-center gap-1.5">
                    <i data-lucide="form-input" class="w-4 h-4 text-emerald-600"></i>
                    Đối Sánh Trực Quan: Biểu Mẫu Hiện Tại vs Biểu Mẫu Đề Xuất Chuẩn CRO
                  </span>
                  <span class="text-[11px] text-slate-400 italic">Nhấp vào hình để phóng to chi tiết</span>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
                  <!-- Cột Trái: Hiện trạng Form -->
                  <div class="space-y-2.5">
                    <div class="flex items-center justify-between">
                      <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-xs font-bold bg-red-100 text-red-800">
                        <span class="w-2 h-2 rounded-full bg-red-600"></span> ❌ Hiện Trạng Biểu Mẫu
                      </span>
                      <span class="text-[11px] text-slate-400">Desktop Contact Page</span>
                    </div>
                    <div class="border border-slate-200 rounded-xl overflow-hidden bg-white relative group cursor-pointer shadow-2xs" onclick="openLightbox('Bang_Chung_Hinh_Anh/desktop_contact_view.png', 'Hiện trạng: Form tách rời First Name và Last Name, bắt buộc nhập Email tạo ma sát tâm lý')">
                      <img src="Bang_Chung_Hinh_Anh/desktop_contact_view.png" alt="Hiện trạng Form liên hệ" class="w-full h-auto object-cover aspect-[16/10] group-hover:scale-105 transition-transform duration-300">
                      <div class="absolute inset-0 bg-slate-900/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                        <i data-lucide="maximize-2" class="w-4 h-4"></i>
                        <span>Nhấp để phóng to</span>
                      </div>
                    </div>
                    <ul class="text-xs text-slate-600 space-y-1 bg-white p-3 rounded-lg border border-slate-200">
                      <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Tách riêng 2 ô "Họ" và "Tên" gây mất thời gian gõ phím.</li>
                      <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Bắt buộc nhập Email khiến khách ngại để lại thông tin.</li>
                    </ul>
                  </div>

                  <!-- Cột Phải: Phương án mẫu Form 3 trường -->
                  <div class="space-y-2.5">
                    <div class="flex items-center justify-between">
                      <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded text-xs font-bold bg-emerald-100 text-emerald-800">
                        <span class="w-2 h-2 rounded-full bg-emerald-600"></span> ✨ Phương Án Sau Tối Ưu (Phương Án Mẫu)
                      </span>
                      <span class="text-[11px] text-emerald-700 font-semibold">Tỷ lệ 16:10 Chuẩn Easy AI Form</span>
                    </div>
                    <div class="border border-emerald-300 rounded-xl p-4 bg-white shadow-sm flex flex-col justify-between min-h-[220px]">
                      <div class="space-y-3">
                        <div class="flex items-center justify-between pb-2 border-b border-slate-100">
                          <span class="text-xs font-extrabold text-slate-900">Biểu Mẫu Thẩm Định Hồ Sơ 15 Phút</span>
                          <span class="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded">Tối Giản 3 Ô</span>
                        </div>
                        <div class="space-y-2 text-xs">
                          <div class="p-2 rounded-lg bg-slate-50 border border-slate-200 text-slate-500 flex items-center justify-between">
                            <span>1. Họ và tên của bạn...</span>
                            <i data-lucide="user" class="w-3.5 h-3.5 text-slate-400"></i>
                          </div>
                          <div class="p-2 rounded-lg bg-slate-50 border border-slate-200 text-slate-500 flex items-center justify-between">
                            <span>2. Số điện thoại (Zalo nhận thẩm định)...</span>
                            <i data-lucide="phone" class="w-3.5 h-3.5 text-slate-400"></i>
                          </div>
                          <div class="p-2 rounded-lg bg-slate-50 border border-slate-200 text-slate-500 flex items-center justify-between">
                            <span>3. Quốc gia quan tâm (Mỹ EB-5, Síp, Úc...)...</span>
                            <i data-lucide="chevron-down" class="w-3.5 h-3.5 text-slate-400"></i>
                          </div>
                        </div>
                      </div>
                      <div class="pt-3">
                        <button class="w-full py-2.5 rounded-lg bg-[#01a915] text-white font-bold text-xs shadow-sm flex items-center justify-center gap-1.5">
                          <span>Nhận Kết Quả Thẩm Định Miễn Phí</span>
                          <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
                        </button>
                      </div>
                    </div>
                    <ul class="text-xs text-slate-700 space-y-1 bg-white p-3 rounded-lg border border-emerald-200">
                      <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Rút ngắn 3 trường:</strong> Họ tên, SĐT Zalo, Nhu cầu quan tâm.</li>
                      <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Cam kết phản hồi 15 phút:</strong> Giảm 65% tỷ lệ bỏ dở biểu mẫu.</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <!-- Footer Card -->
            <div class="px-4 sm:px-5 py-3 bg-slate-50 border-t border-slate-200 text-xs text-slate-700 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <span class="flex items-center gap-1.5"><i data-lucide="search" class="w-3.5 h-3.5 text-slate-500 shrink-0"></i> Mở form tư vấn ở chân trang chủ hoặc trang liên hệ có 2 ô nhập họ tên riêng lẻ.</span>
              <span class="text-red-600 font-bold whitespace-nowrap">Tỷ lệ bỏ dở form: ~65%</span>
            </div>
          </div>

        </div>
      </section>"""

# ==========================================
# 4. THAY THẾ SECTION 2 & XÓA SECTION 3 CŨ
# ==========================================
# Tìm từ đầu section 2 đến trước section bang-uu-tien-p0-p3
s2_start = text.find('<section id="diem-nghen-chuyen-doi"')
s4_start = text.find('<section id="bang-uu-tien-p0-p3"')

if s2_start != -1 and s4_start != -1:
    text = text[:s2_start] + new_section_2 + "\n\n      " + text[s4_start:]
    print("Replaced Section 2 and removed Section 3 successfully!")
else:
    print("Error: Could not locate Section 2 or Section 4 start!")

# ==========================================
# 5. ĐÁNH SỐ LẠI CÁC SECTION TIẾP THEO: 3, 4, 5, 6
# ==========================================
# Section Bang Uu Tien: 4. -> 3.
text = text.replace(
    '4. Bảng Tổng Hợp Khuyến Nghị Theo Thứ Tự Ưu Tiên',
    '3. Bảng Tổng Hợp Khuyến Nghị Theo Thứ Tự Ưu Tiên'
)
# Section Sitemap: 5. -> 4.
text = text.replace(
    '5. Kiến Trúc Sitemap Mục Tiêu & Định Vị Trung Tâm Báo Giá (RFQ Hub)',
    '4. Kiến Trúc Sitemap Mục Tiêu & Định Vị Trung Tâm Báo Giá (RFQ Hub)'
)
# Section Blueprint: 6. -> 5.
text = text.replace(
    '6. Blueprint Cấu Trúc Section Chi Tiết (5–8 Trang Lõi)',
    '5. Blueprint Cấu Trúc Section Chi Tiết (5–8 Trang Lõi)'
)
# Section Luu y Ads: 7. -> 6.
text = text.replace(
    '7. Các Lưu Ý Bắt Buộc Khi Triển Khai Chiến Dịch Google Search Ads',
    '6. Các Lưu Ý Bắt Buộc Khi Triển Khai Chiến Dịch Google Search Ads'
)

# Cập nhật Scrollspy Section IDs trong Javascript
old_scrollspy = """    // Scrollspy for Sidebars
    const sections = document.querySelectorAll('section[id]');
    const railBtns = document.querySelectorAll('.rail-btn');
    const subNavItems = document.querySelectorAll('.sub-nav-item');

    window.addEventListener('scroll', () => {
      let current = '';
      sections.forEach(section => {
        const sectionTop = section.offsetTop - 120;
        if (window.scrollY >= sectionTop) {
          current = section.getAttribute('id');
        }
      });

      railBtns.forEach(btn => {
        btn.classList.remove('active');
        if (btn.getAttribute('href') === `#${current}`) {
          btn.classList.add('active');
        }
      });

      subNavItems.forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('href') === `#${current}`) {
          item.classList.add('active');
        }
      });
    });"""

# Ensure scrollspy handles sections smoothly
if old_scrollspy in text:
    print("Scrollspy already present and dynamic!")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated bien_tap_cau_chu.py with merged Section 2!")
