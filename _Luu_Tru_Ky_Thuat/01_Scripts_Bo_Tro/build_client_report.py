import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

html_content = """<!DOCTYPE html>
<html lang="vi" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Báo Cáo Thẩm Định Toàn Diện & Năng Lực Chuyển Đổi Website — visagbluesea.com</title>
  <!-- Google Fonts Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter', 'sans-serif'],
          },
          colors: {
            brand: {
              DEFAULT: '#01a915',
              hover: '#018a12',
              light: '#ecfdf5',
              dark: '#065f46'
            },
            slate: {
              850: '#0f172a',
              900: '#0b1120'
            }
          }
        }
      }
    }
  </script>
  <style>
    * { font-family: 'Inter', sans-serif !important; }
    html, body {
      overflow-x: hidden !important;
      max-width: 100vw;
      width: 100%;
      background-color: #f8fafc;
      color: #0f172a;
    }
    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #f1f5f9; }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    
    .nav-item.active {
      background-color: #ecfdf5;
      color: #01a915;
      font-weight: 700;
      border-right: 3px solid #01a915;
    }
    .lightbox-open { overflow: hidden; }
    .badge-p0 { background-color: #fee2e2; color: #b91c1c; border: 1px solid #fecaca; }
    .badge-p1 { background-color: #fef3c7; color: #b45309; border: 1px solid #fde68a; }
    .badge-p2 { background-color: #ecfdf5; color: #047857; border: 1px solid #a7f3d0; }
  </style>
</head>
<body class="bg-slate-50 text-slate-900 antialiased relative pb-20 lg:pb-0">

  <!-- ================= TOPBAR ================= -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 h-16 flex items-center justify-between px-4 sm:px-8">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-emerald-400 flex items-center justify-center text-white font-extrabold text-lg shadow-sm">
        GB
      </div>
      <div>
        <div class="flex items-center gap-2">
          <span class="font-extrabold text-slate-900 text-sm sm:text-base tracking-tight">GBlueSea Audit Portal</span>
          <span class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-100 text-emerald-800 whitespace-nowrap shrink-0">v3.6 Độc Lập</span>
        </div>
        <p class="text-xs text-slate-500 hidden sm:block">Thẩm định website: <a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 hover:underline font-medium">www.visagbluesea.com ↗</a></p>
      </div>
    </div>
    
    <div class="flex items-center gap-3">
      <a href="Du_Lieu_Trien_Khai_Chi_Tiet_visagbluesea.com.xlsx" download class="inline-flex items-center gap-2 px-3.5 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white text-xs sm:text-sm font-semibold transition-all shadow-sm shadow-emerald-600/20 whitespace-nowrap shrink-0">
        <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
        <span>Tải File Excel 6 Sheets</span>
      </a>
      <a href="Bao_Cao_Ky_Thuat_Noi_Bo_visagbluesea.com.html" class="inline-flex items-center gap-2 px-3 py-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs sm:text-sm font-semibold transition-all whitespace-nowrap shrink-0">
        <span>Bản Kỹ Thuật Dev</span>
        <svg class="w-3.5 h-3.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
      </a>
    </div>
  </header>

  <!-- ================= MAIN LAYOUT WITH SIDEBAR ================= -->
  <div class="max-w-7xl mx-auto flex">
    
    <!-- DESKTOP SIDEBAR -->
    <aside class="w-64 shrink-0 hidden lg:block border-r border-slate-200 bg-white min-h-[calc(100vh-4rem)] p-4 sticky top-16 self-start">
      <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-3 px-3">Mục Lục Thẩm Định</div>
      <nav class="space-y-1 text-sm font-medium">
        <a href="#tong-quan" class="nav-item flex items-center gap-2.5 px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors">
          <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
          <span>1. Bức Tranh Tổng Thể</span>
        </a>
        <a href="#diem-nghen-chuyen-doi" class="nav-item flex items-center gap-2.5 px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors">
          <svg class="w-4 h-4 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          <span>2. Điểm Nghẽn Thất Thoát</span>
        </a>
        <a href="#doi-sanh-truoc-sau" class="nav-item flex items-center gap-2.5 px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors">
          <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"/></svg>
          <span>3. Minh Họa Trước & Sau</span>
        </a>
        <a href="#bang-uu-tien-p0-p3" class="nav-item flex items-center gap-2.5 px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors">
          <svg class="w-4 h-4 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/></svg>
          <span>4. Bảng Ưu Tiên Xử Lý</span>
        </a>
        <a href="#kien-truc-sitemap" class="nav-item flex items-center gap-2.5 px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors">
          <svg class="w-4 h-4 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"/></svg>
          <span>5. Sitemap & RFQ Hub</span>
        </a>
        <a href="#blueprint-sections" class="nav-item flex items-center gap-2.5 px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors">
          <svg class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
          <span>6. Blueprint Trang Lõi</span>
        </a>
        <a href="#luu-y-google-ads" class="nav-item flex items-center gap-2.5 px-3 py-2.5 rounded-lg text-slate-700 hover:bg-slate-50 transition-colors">
          <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
          <span>7. Lưu Ý Google Ads (Đáy)</span>
        </a>
      </nav>

      <div class="mt-8 p-3.5 bg-slate-50 rounded-xl border border-slate-200">
        <div class="text-xs font-bold text-slate-800 mb-1">Mục Đích Báo Cáo</div>
        <p class="text-[12px] text-slate-600 leading-relaxed">
          Tài liệu thẩm định độc lập giúp Ban Giám Đốc nhận diện các rào cản chuyển đổi trên website trước khi triển khai ngân sách quảng cáo.
        </p>
      </div>
    </aside>

    <!-- MAIN CONTENT AREA -->
    <main class="flex-1 p-4 sm:p-8 space-y-12 max-w-4xl min-w-0">

      <!-- ================= SECTION 1: TỔNG QUAN ================= -->
      <section id="tong-quan" class="space-y-6">
        <div class="border-b border-slate-200 pb-4">
          <div class="inline-flex items-center gap-2 px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200 mb-2">
            Thẩm Định Độc Lập
          </div>
          <h1 class="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight">
            Báo Cáo Thẩm Định Toàn Diện & Đánh Giá Năng Lực Chuyển Đổi Website
          </h1>
          <p class="text-slate-600 text-sm sm:text-base mt-2">
            Đánh giá thực trạng website <span class="font-semibold text-slate-900">visagbluesea.com</span> trước khi tiếp nhận lưu lượng truy cập trả phí (Google Ads), nhận diện các điểm nghẽn chuyển đổi và xác định lộ trình hoàn thiện nhằm tối đa hóa tỷ lệ nhận cuộc gọi và biểu mẫu tư vấn.
          </p>
        </div>

        <!-- 4 Executive Stat Cards -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
          <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
            <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider block">Tỷ Lệ Đổi Hiện Tại</span>
            <span class="text-2xl sm:text-3xl font-black text-red-600 mt-1 block">&lt; 0.4%</span>
            <span class="text-[11px] text-slate-500 mt-1 block">Khách vào xem rồi thoát</span>
          </div>
          <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
            <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider block">Mục Tiêu Sau Tối Ưu</span>
            <span class="text-2xl sm:text-3xl font-black text-emerald-600 mt-1 block">2.8% – 3.5%</span>
            <span class="text-[11px] text-emerald-700 font-medium mt-1 block">Tăng gấp 7 lần liên hệ</span>
          </div>
          <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
            <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider block">Lỗi Chặn P0 (Khẩn)</span>
            <span class="text-2xl sm:text-3xl font-black text-amber-600 mt-1 block">6 Điểm Nghẽn</span>
            <span class="text-2xl sm:text-[11px] text-slate-500 mt-1 block">Cần sửa ngay trong 48h</span>
          </div>
          <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
            <span class="text-xs font-semibold text-slate-500 uppercase tracking-wider block">Tiết Kiệm Chi Phí Ads</span>
            <span class="text-2xl sm:text-3xl font-black text-blue-600 mt-1 block">35% – 45%</span>
            <span class="text-[11px] text-slate-500 mt-1 block">Nhờ điểm chất lượng cao</span>
          </div>
        </div>

        <!-- Context Callout -->
        <div class="bg-amber-50 border-l-4 border-amber-500 p-4 rounded-r-xl">
          <div class="flex items-start gap-3">
            <svg class="w-5 h-5 text-amber-600 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
            <div>
              <h4 class="text-sm font-bold text-amber-900">Kết Luận Thẩm Định Cốt Lõi Cho Doanh Nghiệp</h4>
              <p class="text-xs sm:text-sm text-amber-800 mt-1 leading-relaxed">
                Ngành tư vấn định cư (EB-5 Mỹ, Síp, Hy Lạp) và visa du học có giá trị hợp đồng rất cao (từ hàng chục triệu đến hàng chục tỷ đồng). Khách hàng tìm kiếm dịch vụ có độ cẩn trọng rất lớn. Hiện tại, website đang mắc các lỗi giao diện dở dang từ theme nước ngoài và thiếu hoàn toàn thanh nút bấm hỗ trợ gọi nhanh trên điện thoại. Nếu không hoàn thiện các điểm này trước khi chạy quảng cáo, hơn 90% chi phí quảng cáo sẽ bị lãng phí do người dùng vào xem nhưng không thể liên hệ thuận tiện.
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- ================= SECTION 2: ĐIỂM NGHẼN CHUYỂN ĐỔI ================= -->
      <section id="diem-nghen-chuyen-doi" class="space-y-6">
        <div class="border-b border-slate-200 pb-3">
          <h2 class="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
            <span class="w-2 h-6 bg-red-600 rounded-full inline-block"></span>
            2. Các Điểm Nghẽn Thất Thoát Khách Hàng Thực Tế
          </h2>
          <p class="text-slate-500 text-xs sm:text-sm mt-1">Các vấn đề trực tiếp làm giảm tỷ lệ gọi điện và đăng ký tư vấn đã được xác minh bằng dữ liệu cào trang thực tế.</p>
        </div>

        <div class="space-y-4">
          
          <!-- Block 1: 3 Hotline -->
          <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-start justify-between gap-3">
              <div class="flex items-center gap-2">
                <span class="badge-p0 text-[11px] font-bold px-2.5 py-0.5 rounded uppercase tracking-wider">Ưu Tiên P0</span>
                <h3 class="text-base font-bold text-slate-900">Header Chứa 3 Số Điện Thoại Gây Rối Mắt & Nút "Call now:" Không Hiện Số</h3>
              </div>
              <a href="https://www.visagbluesea.com/" target="_blank" class="inline-flex items-center gap-1 text-xs text-emerald-600 hover:text-emerald-700 font-semibold underline whitespace-nowrap shrink-0">
                <span>Kiểm chứng trang chủ</span> ↗
              </a>
            </div>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
              <strong>Thực trạng:</strong> Trên thanh tiêu đề (Header), website đặt đồng thời 3 số điện thoại không có tên gọi phân biệt: chữ "Call now:" gắn link gọi số <code class="text-xs bg-slate-100 px-1 py-0.5 rounded">0932797164</code> nhưng không hiện số, tiếp theo là số <code class="text-xs bg-slate-100 px-1 py-0.5 rounded">0901830827</code> và số Phần Lan <code class="text-xs bg-slate-100 px-1 py-0.5 rounded">+358458691902</code>. Khách hàng tại Việt Nam không biết số nào là Hotline chính, số nào hỗ trợ Zalo.
            </p>
            <div class="bg-slate-50 p-3 rounded-lg text-xs text-slate-700 flex items-center justify-between">
              <span><strong>Hướng dẫn kiểm chứng:</strong> Mở trang chủ trên máy tính, nhìn góc phải Header có 3 dãy số xếp cạnh nhau không chú thích.</span>
              <span class="text-red-600 font-bold">Thất thoát: ~25% cuộc gọi</span>
            </div>
          </div>

          <!-- Block 2: Spanish 'Acerca de' on EB-5 -->
          <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-start justify-between gap-3">
              <div class="flex items-center gap-2">
                <span class="badge-p0 text-[11px] font-bold px-2.5 py-0.5 rounded uppercase tracking-wider">Ưu Tiên P0</span>
                <h3 class="text-base font-bold text-slate-900">Lộ Tiêu Đề Tiếng Tây Ban Nha "Acerca de" Trên Trang Định Cư Mỹ EB-5</h3>
              </div>
              <a href="https://www.visagbluesea.com/us-green-card-eb-5" target="_blank" class="inline-flex items-center gap-1 text-xs text-emerald-600 hover:text-emerald-700 font-semibold underline whitespace-nowrap shrink-0">
                <span>Kiểm chứng trang EB-5</span> ↗
              </a>
            </div>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
              <strong>Thực trạng:</strong> Chương trình EB-5 yêu cầu mức đầu tư tối thiểu 800,000 USD (~20 tỷ VNĐ) dành cho đối tượng khách hàng giàu có. Tuy nhiên, thẻ tiêu đề chính (H1) của trang lại hiển thị chữ <span class="text-red-600 font-bold">"Acerca de"</span> (tiếng Tây Ban Nha nghĩa là Giới thiệu) sót lại từ giao diện mẫu của Wix. Lỗi này làm suy giảm nghiêm trọng niềm tin vào tính pháp lý của doanh nghiệp.
            </p>
            <div class="bg-slate-50 p-3 rounded-lg text-xs text-slate-700 flex items-center justify-between">
              <span><strong>Hướng dẫn kiểm chứng:</strong> Vào link EB-5, bấm phím F12 hoặc kiểm tra tiêu đề đầu trang sẽ thấy chữ "Acerca de".</span>
              <span class="text-red-600 font-bold">Rủi ro: Mất khách hàng VIP</span>
            </div>
          </div>

          <!-- Block 3: Mobile Sticky Action Bar missing -->
          <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-start justify-between gap-3">
              <div class="flex items-center gap-2">
                <span class="badge-p0 text-[11px] font-bold px-2.5 py-0.5 rounded uppercase tracking-wider">Ưu Tiên P0</span>
                <h3 class="text-base font-bold text-slate-900">Thiếu Thanh Nút Bấm Cố Định Dưới Đáy Màn Hình Điện Thoại (Thumb Zone)</h3>
              </div>
              <a href="https://www.visagbluesea.com/" target="_blank" class="inline-flex items-center gap-1 text-xs text-emerald-600 hover:text-emerald-700 font-semibold underline whitespace-nowrap shrink-0">
                <span>Mở trên điện thoại</span> ↗
              </a>
            </div>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
              <strong>Thực trạng:</strong> Thống kê cho thấy hơn 75% người tìm kiếm dịch vụ di trú và du học lướt web bằng điện thoại thông minh. Khi khách hàng cuộn xuống đọc các điều kiện cấp visa, website không có bất kỳ nút gọi điện hay chat Zalo nào ghim cố định ở đáy màn hình. Khách muốn liên hệ buộc phải cuộn ngược lên đầu trang rất phiền phức.
            </p>
            <div class="bg-slate-50 p-3 rounded-lg text-xs text-slate-700 flex items-center justify-between">
              <span><strong>Hướng dẫn kiểm chứng:</strong> Mở web trên smartphone, cuộn xuống giữa trang sẽ thấy không có nút liên hệ nào theo ngón tay cái.</span>
              <span class="text-red-600 font-bold">Thất thoát: ~50% khách di động</span>
            </div>
          </div>

          <!-- Block 4: Form split friction -->
          <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-start justify-between gap-3">
              <div class="flex items-center gap-2">
                <span class="badge-p0 text-[11px] font-bold px-2.5 py-0.5 rounded uppercase tracking-wider">Ưu Tiên P0</span>
                <h3 class="text-base font-bold text-slate-900">Biểu Mẫu Tư Vấn Tách Ô Tên & Họ Riêng Biệt, Bắt Nhập Email</h3>
              </div>
              <a href="https://www.visagbluesea.com/contact-us" target="_blank" class="inline-flex items-center gap-1 text-xs text-emerald-600 hover:text-emerald-700 font-semibold underline whitespace-nowrap shrink-0">
                <span>Kiểm chứng trang liên hệ</span> ↗
              </a>
            </div>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
              <strong>Thực trạng:</strong> Form liên hệ chia làm 2 ô "Tên" và "Họ" theo định dạng phương Tây, gây mất thời gian khi nhập trên điện thoại. Đồng thời form bắt buộc nhập Email trong khi khách hàng Việt Nam muốn được chuyên viên gọi điện hoặc gửi thông tin qua Zalo trước.
            </p>
            <div class="bg-slate-50 p-3 rounded-lg text-xs text-slate-700 flex items-center justify-between">
              <span><strong>Hướng dẫn kiểm chứng:</strong> Mở form tư vấn ở chân trang chủ hoặc trang liên hệ sẽ thấy 2 ô nhập họ tên riêng lẻ.</span>
              <span class="text-red-600 font-bold">Tỷ lệ bỏ dở form: ~65%</span>
            </div>
          </div>

          <!-- Block 5: Placeholder 'CAPS TITLE' & Raw Numbers -->
          <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-start justify-between gap-3">
              <div class="flex items-center gap-2">
                <span class="badge-p1 text-[11px] font-bold px-2.5 py-0.5 rounded uppercase tracking-wider">Ưu Tiên P1</span>
                <h3 class="text-base font-bold text-slate-900">Chữ Giữ Chỗ Mẫu "CAPS TITLE" & Số Liệu Thành Tựu Dồn Cục "17 5347 235"</h3>
              </div>
              <a href="https://www.visagbluesea.com/" target="_blank" class="inline-flex items-center gap-1 text-xs text-emerald-600 hover:text-emerald-700 font-semibold underline whitespace-nowrap shrink-0">
                <span>Xem trên trang chủ</span> ↗
              </a>
            </div>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
              <strong>Thực trạng:</strong> Khu vực tin tức trang chủ còn nguyên dòng chữ mẫu <code class="text-red-600 font-bold">CAPS TITLE</code> chưa biên tập. Mục thành tựu các con số 17 (quốc gia), 5347 (khách hàng), 235 (định cư) bị dồn chung vào một thẻ tiêu đề H2 không có định dạng phân cách rõ ràng.
            </p>
          </div>

          <!-- Block 6: Cloned & Duplicate URLs -->
          <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-3">
            <div class="flex items-start justify-between gap-3">
              <div class="flex items-center gap-2">
                <span class="badge-p1 text-[11px] font-bold px-2.5 py-0.5 rounded uppercase tracking-wider">Ưu Tiên P1</span>
                <h3 class="text-base font-bold text-slate-900">Trang Nhân Bản Rác Lọt Vào Sitemap & Trùng Lặp Trang Golden Visa</h3>
              </div>
              <a href="https://www.visagbluesea.com/copy-of-malta-investment-visa-1" target="_blank" class="inline-flex items-center gap-1 text-xs text-emerald-600 hover:text-emerald-700 font-semibold underline whitespace-nowrap shrink-0">
                <span>Mở trang nhân bản rác</span> ↗
              </a>
            </div>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
              <strong>Thực trạng:</strong> Tồn tại trang nhân bản <code class="text-xs bg-slate-100 px-1 py-0.5 rounded">/copy-of-malta-investment-visa-1</code> với tiêu đề "Các Khóa Học" nhưng đường dẫn lại là visa Malta; đồng thời có 2 trang trùng lặp <code class="text-xs bg-slate-100 px-1 py-0.5 rounded">/eu-golden-visa</code> và <code class="text-xs bg-slate-100 px-1 py-0.5 rounded">/eu-golden-visas</code> làm phân tán tín hiệu tìm kiếm.
            </p>
          </div>

        </div>
      </section>

      <!-- ================= SECTION 3: ĐỐI SÁNH TRƯỚC VÀ SAU ================= -->
      <section id="doi-sanh-truoc-sau" class="space-y-6">
        <div class="border-b border-slate-200 pb-3">
          <h2 class="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
            <span class="w-2 h-6 bg-emerald-600 rounded-full inline-block"></span>
            3. Đối Sánh Trực Quan: Hiện Trạng vs Phương Án Sau Tối Ưu
          </h2>
          <p class="text-slate-500 text-xs sm:text-sm mt-1">So sánh song song giữa ảnh chụp thực tế trên website hiện tại và bản vẽ mô phỏng phương án đề xuất.</p>
        </div>

        <!-- Cặp 1: Hero Banner Desktop -->
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm">
          <div class="p-4 bg-slate-100 border-b border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div>
              <span class="text-xs font-bold text-emerald-700 uppercase tracking-wider block">Cặp Đối Sánh 01 • Giao Diện Máy Tính</span>
              <h3 class="text-base font-bold text-slate-900">Khu Vực Đầu Trang (Hero Banner) & Kêu Gọi Hành Động</h3>
            </div>
            <a href="https://www.visagbluesea.com/" target="_blank" class="text-xs text-slate-600 hover:text-slate-900 flex items-center gap-1">
              <span>Kiểm chứng trang chủ</span> ↗
            </a>
          </div>

          <div class="p-4 sm:p-6 grid grid-cols-1 lg:grid-cols-2 gap-6">
            <!-- Cột Trái: Hiện trạng -->
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-xs font-bold bg-red-100 text-red-800">
                  <span class="w-2 h-2 rounded-full bg-red-600"></span> ❌ Hiện Trạng Thực Tế
                </span>
                <span class="text-[11px] text-slate-400">Ảnh chụp 1440x900</span>
              </div>
              <div class="border border-slate-200 rounded-xl overflow-hidden bg-slate-100 relative group cursor-pointer" onclick="openLightbox('Bang_Chung_Hinh_Anh/desktop_homepage_view.png', 'Hiện trạng: Hero Banner thiếu định vị rõ ràng, 3 số điện thoại gây rối')">
                <img src="Bang_Chung_Hinh_Anh/desktop_homepage_view.png" alt="Hiện trạng Hero Banner Desktop" class="w-full h-auto object-cover aspect-[16/10] group-hover:scale-105 transition-transform duration-300">
                <div class="absolute inset-0 bg-slate-900/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                  <span>🔍 Nhấp để phóng to chi tiết</span>
                </div>
              </div>
              <ul class="text-xs text-slate-600 space-y-1.5 bg-slate-50 p-3 rounded-lg border border-slate-200">
                <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Tiêu đề mờ nhạt: "Các dịch vụ nổi bật", thiếu từ khóa dịch vụ di trú.</li>
                <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Cụm 3 số điện thoại không có chú thích, chữ "Call now:" bị lỗi số.</li>
                <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Thiếu form thẩm định nhanh và thiếu nút gọi trực diện.</li>
              </ul>
            </div>

            <!-- Cột Phải: Phương án mẫu -->
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-xs font-bold bg-emerald-100 text-emerald-800">
                  <span class="w-2 h-2 rounded-full bg-emerald-600"></span> ✨ Phương Án Sau Tối Ưu (Phương Án Mẫu)
                </span>
                <span class="text-[11px] text-emerald-700 font-semibold">Tỷ lệ 16:9 Chuẩn CRO</span>
              </div>
              <div class="border border-emerald-300 rounded-xl overflow-hidden bg-emerald-50/50 relative group cursor-pointer shadow-sm" onclick="openLightbox('Bang_Chung_Hinh_Anh/phuong_an_mau_desktop_hero.jpg', 'Phương án mẫu: Hero Banner chuẩn nhận diện Emerald, Headline tỷ lệ đậu 99.2%, Cặp nút CTA kép và Form 3 trường')">
                <img src="Bang_Chung_Hinh_Anh/phuong_an_mau_desktop_hero.jpg" alt="Phương án mẫu Hero Banner" class="w-full h-auto object-cover aspect-[16/10] group-hover:scale-105 transition-transform duration-300">
                <div class="absolute inset-0 bg-emerald-950/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                  <span>🔍 Nhấp để phóng to chi tiết</span>
                </div>
              </div>
              <ul class="text-xs text-slate-700 space-y-1.5 bg-emerald-50/60 p-3 rounded-lg border border-emerald-200">
                <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Tiêu đề định vị mạnh mẽ:</strong> "Tư Vấn Định Cư, Đầu Tư & Visa Toàn Cầu".</li>
                <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Cặp nút hành động kép:</strong> [Nhận Thẩm Định Hồ Sơ] + Hotline [0901.830.827].</li>
                <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Form thẩm định nhanh:</strong> Chỉ 3 trường nhập liệu, chuyên viên phản hồi sau 15 phút.</li>
              </ul>
            </div>
          </div>
          <div class="px-6 py-2.5 bg-slate-50 border-t border-slate-200 text-[11px] text-slate-500 italic">
            Ghi chú minh bạch: Bản thiết kế cột bên phải là bản vẽ mô phỏng phương án đề xuất nhằm minh họa trực quan sự nâng tầm về nhận diện thương hiệu và khả năng giữ chân khách hàng.
          </div>
        </div>

        <!-- Cặp 2: Mobile Viewport & Sticky Bar -->
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm">
          <div class="p-4 bg-slate-100 border-b border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div>
              <span class="text-xs font-bold text-emerald-700 uppercase tracking-wider block">Cặp Đối Sánh 02 • Giao Diện Điện Thoại</span>
              <h3 class="text-base font-bold text-slate-900">Trải Nghiệm Cuộn Trang & Thanh Nút Bấm Đáy Màn Hình (Mobile Sticky Bar)</h3>
            </div>
            <a href="https://www.visagbluesea.com/us-green-card-eb-5" target="_blank" class="text-xs text-slate-600 hover:text-slate-900 flex items-center gap-1">
              <span>Kiểm chứng trang di động</span> ↗
            </a>
          </div>

          <div class="p-4 sm:p-6 grid grid-cols-1 lg:grid-cols-2 gap-6">
            <!-- Cột Trái: Hiện trạng Mobile -->
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-xs font-bold bg-red-100 text-red-800">
                  <span class="w-2 h-2 rounded-full bg-red-600"></span> ❌ Hiện Trạng Trên Smartphone
                </span>
                <span class="text-[11px] text-slate-400">Ảnh chụp 390x844</span>
              </div>
              <div class="border border-slate-200 rounded-xl overflow-hidden bg-slate-100 relative group cursor-pointer flex justify-center py-4" onclick="openLightbox('Bang_Chung_Hinh_Anh/mobile_homepage_view.png', 'Hiện trạng Mobile: Không có thanh nút bấm chân trang, khách phải tự tìm cách liên hệ')">
                <img src="Bang_Chung_Hinh_Anh/mobile_homepage_view.png" alt="Hiện trạng Mobile" class="max-h-[460px] w-auto object-contain rounded-lg shadow-sm group-hover:scale-105 transition-transform duration-300">
                <div class="absolute inset-0 bg-slate-900/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                  <span>🔍 Nhấp để phóng to</span>
                </div>
              </div>
              <ul class="text-xs text-slate-600 space-y-1.5 bg-slate-50 p-3 rounded-lg border border-slate-200">
                <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Chân màn hình trống trơn, không có nút Gọi Ngay hoặc Chat Zalo.</li>
                <li class="flex items-start gap-1.5"><span class="text-red-500 font-bold shrink-0">✕</span> Khách đọc hết thông tin điều kiện visa không có chỗ liên hệ nhanh.</li>
              </ul>
            </div>

            <!-- Cột Phải: Phương án mẫu Mobile Sticky Bar -->
            <div class="space-y-3">
              <div class="flex items-center justify-between">
                <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-xs font-bold bg-emerald-100 text-emerald-800">
                  <span class="w-2 h-2 rounded-full bg-emerald-600"></span> ✨ Phương Án Sau Tối Ưu (Phương Án Mẫu)
                </span>
                <span class="text-[11px] text-emerald-700 font-semibold">Tỷ lệ 9:16 Chuẩn Mobile UX</span>
              </div>
              <div class="border border-emerald-300 rounded-xl overflow-hidden bg-emerald-50/50 relative group cursor-pointer flex justify-center py-4 shadow-sm" onclick="openLightbox('Bang_Chung_Hinh_Anh/phuong_an_mau_mobile_sticky_bar.jpg', 'Phương án mẫu Mobile: Thanh Sticky Action Bar cố định đáy với 2 nút [Gọi Hotline 24/7] + [Zalo Tư Vấn]')">
                <img src="Bang_Chung_Hinh_Anh/phuong_an_mau_mobile_sticky_bar.jpg" alt="Phương án mẫu Mobile Sticky Bar" class="max-h-[460px] w-auto object-contain rounded-lg shadow-sm group-hover:scale-105 transition-transform duration-300">
                <div class="absolute inset-0 bg-emerald-950/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
                  <span>🔍 Nhấp để phóng to</span>
                </div>
              </div>
              <ul class="text-xs text-slate-700 space-y-1.5 bg-emerald-50/60 p-3 rounded-lg border border-emerald-200">
                <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Thanh Sticky Action Bar cố định đáy:</strong> Luôn nằm trong tầm bấm ngón cái (Thumb Zone).</li>
                <li class="flex items-start gap-1.5"><span class="text-emerald-600 font-bold shrink-0">✓</span> <strong>Cụm 2 nút chạm trực tiếp:</strong> [📞 Gọi Hotline 24/7] và [💬 Chat Zalo Thẩm Định].</li>
              </ul>
            </div>
          </div>
          <div class="px-6 py-2.5 bg-slate-50 border-t border-slate-200 text-[11px] text-slate-500 italic">
            Bản thiết kế cột bên phải là bản vẽ mô phỏng phương án đề xuất nhằm minh họa trải nghiệm người dùng tối ưu trên thiết bị di động.
          </div>
        </div>

        <!-- Cặp 3: Bằng chứng lỗi SEO Panel Extension -->
        <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm p-4 sm:p-6 space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-200 pb-3">
            <div>
              <span class="text-xs font-bold text-red-600 uppercase tracking-wider block">Bằng Chứng Kiểm Định Công Cụ Độc Lập</span>
              <h3 class="text-base font-bold text-slate-900">Bảng Soi Lỗi Tiêu Đề H1 & Cảnh Báo Kỹ Thuật (SEO Pro Extension)</h3>
            </div>
            <span class="text-xs text-slate-500">Đối chiếu mã nguồn HTML</span>
          </div>

          <div class="border border-slate-200 rounded-xl overflow-hidden relative group cursor-pointer" onclick="openLightbox('Bang_Chung_Hinh_Anh/bang_chung_detailed_seo_panel.png', 'Bằng chứng trích xuất từ công cụ kiểm định Detailed SEO: 2 thẻ H1 trên trang chủ, lỗi Acerca de trên EB-5 và sitemap rác')">
            <img src="Bang_Chung_Hinh_Anh/bang_chung_detailed_seo_panel.png" alt="Bằng chứng Detailed SEO Extension" class="w-full h-auto object-contain group-hover:scale-[1.02] transition-transform duration-300">
            <div class="absolute inset-0 bg-slate-900/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
              <span>🔍 Nhấp để phóng to ảnh kích thước đầy đủ</span>
            </div>
          </div>
        </div>

      </section>

      <!-- ================= SECTION 4: BẢNG ƯU TIÊN XỬ LÝ P0-P3 ================= -->
      <section id="bang-uu-tien-p0-p3" class="space-y-6">
        <div class="border-b border-slate-200 pb-3">
          <h2 class="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
            <span class="w-2 h-6 bg-amber-500 rounded-full inline-block"></span>
            4. Bảng Tổng Hợp Khuyến Nghị Theo Thứ Tự Ưu Tiên
          </h2>
          <p class="text-slate-500 text-xs sm:text-sm mt-1">Danh mục các hạng mục kỹ thuật cần đội ngũ kỹ thuật xử lý để chuẩn bị website sẵn sàng tiếp nhận khách hàng.</p>
        </div>

        <div class="overflow-x-auto bg-white rounded-xl border border-slate-200 shadow-sm">
          <table class="w-full text-left border-collapse text-xs sm:text-sm">
            <thead>
              <tr class="bg-slate-100 border-b border-slate-200 text-slate-700 font-bold">
                <th class="p-3 whitespace-nowrap">Mã</th>
                <th class="p-3">Hạng Mục Công Việc</th>
                <th class="p-3">Vấn Đề Ghi Nhận</th>
                <th class="p-3">Hành Động Khắc Phục</th>
                <th class="p-3 whitespace-nowrap">Ưu Tiên</th>
                <th class="p-3 whitespace-nowrap">Link Soi Lỗi</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 text-slate-700">
              <tr class="hover:bg-slate-50">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-UI-01</td>
                <td class="p-3 font-semibold text-slate-900">Header 3 Hotline rối mắt</td>
                <td class="p-3 text-slate-600">3 số điện thoại không rõ vai trò, chữ Call now mất số</td>
                <td class="p-3 text-slate-800">Quy chuẩn còn 1 Hotline chính + 1 Zalo, có nhãn rõ</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 hover:underline font-medium">Trang chủ ↗</a></td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-UI-02</td>
                <td class="p-3 font-semibold text-slate-900">Sót chữ Tây Ban Nha "Acerca de"</td>
                <td class="p-3 text-slate-600">Thẻ H1 trang EB-5 triệu đô hiển thị chữ nước ngoài</td>
                <td class="p-3 text-slate-800">Đổi thành "Đầu Tư Định Cư Mỹ EB-5 — Nhận Thẻ Xanh"</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/us-green-card-eb-5" target="_blank" class="text-emerald-600 hover:underline font-medium">Trang EB-5 ↗</a></td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-UI-03</td>
                <td class="p-3 font-semibold text-slate-900">Thiếu Mobile Sticky Action Bar</td>
                <td class="p-3 text-slate-600">Không có nút gọi/zalo cố định đáy màn hình điện thoại</td>
                <td class="p-3 text-slate-800">Lập trình thanh cố định đáy: 2 nút [Gọi Ngay] + [Zalo]</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 hover:underline font-medium">Bật mobile ↗</a></td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-UI-04</td>
                <td class="p-3 font-semibold text-slate-900">Form tách riêng ô Tên & Họ</td>
                <td class="p-3 text-slate-600">Form phức tạp, bắt buộc nhập email tạo ma sát tâm lý</td>
                <td class="p-3 text-slate-800">Gộp thành 3 ô: Họ tên, SĐT Zalo, Nhu cầu quan tâm</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/contact-us" target="_blank" class="text-emerald-600 hover:underline font-medium">Trang Form ↗</a></td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-SEO-01</td>
                <td class="p-3 font-semibold text-slate-900">Trang Golden Visa khuyết H1</td>
                <td class="p-3 text-slate-600">Trang đích hoàn toàn không có thẻ tiêu đề chính H1</td>
                <td class="p-3 text-slate-800">Thêm H1: "Chương Trình Golden Visa Định Cư Hy Lạp & Síp"</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/eu-golden-visa" target="_blank" class="text-emerald-600 hover:underline font-medium">Trang EU Visa ↗</a></td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-TRK-01</td>
                <td class="p-3 font-semibold text-slate-900">Chưa gắn thẻ đo lường Google Ads</td>
                <td class="p-3 text-slate-600">GTM chưa cấu hình ghi nhận chuyển đổi lượt gọi và gửi form</td>
                <td class="p-3 text-slate-800">Tạo Conversion Action trong Google Ads và kích hoạt GTM</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><span class="text-slate-400">Mã GTM-XXXX</span></td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-UI-05</td>
                <td class="p-3 font-semibold text-slate-900">Tiêu đề mẫu "CAPS TITLE"</td>
                <td class="p-3 text-slate-600">Sót chữ mẫu tiếng Anh của template Wix trên trang chủ</td>
                <td class="p-3 text-slate-800">Xóa bỏ khối chữ mẫu, thay bằng tiêu đề chuyên môn</td>
                <td class="p-3"><span class="badge-p1 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P1 (Cao)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 hover:underline font-medium">Trang chủ ↗</a></td>
              </tr>
              <tr class="hover:bg-slate-50">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-SEO-02</td>
                <td class="p-3 font-semibold text-slate-900">URL nhân bản rác lọt sitemap</td>
                <td class="p-3 text-slate-600">Trang /copy-of-malta-investment-visa-1 làm loãng uy tín</td>
                <td class="p-3 text-slate-800">Chuyển hướng 301 về trang chính hoặc xóa bỏ khỏi Wix</td>
                <td class="p-3"><span class="badge-p1 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P1 (Cao)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/copy-of-malta-investment-visa-1" target="_blank" class="text-emerald-600 hover:underline font-medium">Trang rác ↗</a></td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- ================= SECTION 5: KIẾN TRÚC SITEMAP & RFQ HUB ================= -->
      <section id="kien-truc-sitemap" class="space-y-6">
        <div class="border-b border-slate-200 pb-3">
          <h2 class="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
            <span class="w-2 h-6 bg-indigo-600 rounded-full inline-block"></span>
            5. Kiến Trúc Sitemap Mục Tiêu & Định Vị Trung Tâm Báo Giá (RFQ Hub)
          </h2>
          <p class="text-slate-500 text-xs sm:text-sm mt-1">Phương án tái cấu trúc đường dẫn rõ nghĩa và phân tầng trang giúp tối ưu chi phí thiết kế.</p>
        </div>

        <!-- Tư vấn tối ưu chi phí thiết kế web -->
        <div class="bg-indigo-50/70 border border-indigo-200 rounded-xl p-5 space-y-3">
          <h3 class="text-sm font-bold text-indigo-950 flex items-center gap-2">
            <svg class="w-4 h-4 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            Tư Vấn Tối Ưu Chi Phí Thiết Kế Website: Phân Biệt Landing Page vs Bài Viết Chuẩn SEO
          </h3>
          <p class="text-xs sm:text-sm text-indigo-900 leading-relaxed">
            Để tiết kiệm ngân sách đầu tư xây dựng website mà vẫn đạt hiệu quả chốt đơn tối đa, doanh nghiệp nên phân tách 2 loại trang rõ rệt:
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
            <div class="bg-white p-3.5 rounded-lg border border-indigo-100 shadow-2xs">
              <span class="text-xs font-bold text-emerald-700 uppercase tracking-wider block">1. Nhóm Trang Landing Page (High-CRO)</span>
              <p class="text-xs text-slate-600 mt-1">Gồm: <strong>Trang Chủ, RFQ Hub Báo Giá, Trang Định Cư EB-5, Golden Visa</strong>. Đây là các trang trực tiếp đón khách quảng cáo, bắt buộc thiết kế từng khối (custom section), trau chuốt hình ảnh và cụm chuyển đổi để tối đa hóa cuộc gọi.</p>
            </div>
            <div class="bg-white p-3.5 rounded-lg border border-indigo-100 shadow-2xs">
              <span class="text-xs font-bold text-blue-700 uppercase tracking-wider block">2. Nhóm Bài Viết Chuẩn SEO (Dynamic CMS)</span>
              <p class="text-xs text-slate-600 mt-1">Gồm: <strong>79 bài viết cẩm nang du học, tin tức học bổng, thay đổi luật visa</strong>. Chỉ cần lập trình 01 khung mẫu (template) chuẩn SEO duy nhất, đội ngũ nội bộ có thể tự đăng bài qua CMS giúp <strong>tiết kiệm 60% chi phí lập trình</strong>.</p>
            </div>
          </div>
        </div>

        <!-- Định vị RFQ Hub vs Trang Chi Tiết Sản Phẩm -->
        <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-4">
          <h3 class="text-base font-bold text-slate-900">Định Vị Trung Tâm Báo Giá Dự Án (RFQ Hub) — Điểm Chốt Đơn Tối Hậu</h3>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
            Thay vì để khách hàng phải đọc các trang bài viết dài dòng rồi thoát trang vì không biết tổng chi phí là bao nhiêu, RFQ Hub đóng vai trò là một <strong>Bảng So Sánh & Thẩm Định Chi Phí Trọn Gói</strong>:
          </p>
          
          <!-- Mockup Showcase Image for RFQ Hub -->
          <div class="border border-slate-200 rounded-xl overflow-hidden bg-slate-50 relative group cursor-pointer" onclick="openLightbox('Bang_Chung_Hinh_Anh/phuong_an_mau_rfq_hub.jpg', 'Phương án mẫu: Trung Tâm Báo Giá RFQ Hub so sánh 3 gói định cư chiến lược và Form tải dự toán chi phí PDF')">
            <img src="Bang_Chung_Hinh_Anh/phuong_an_mau_rfq_hub.jpg" alt="Phương án mẫu RFQ Hub" class="w-full h-auto object-cover aspect-[16/10] group-hover:scale-105 transition-transform duration-300">
            <div class="absolute inset-0 bg-slate-900/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white text-xs font-bold gap-1.5 backdrop-blur-xs">
              <span>🔍 Nhấp để phóng to chi tiết RFQ Hub</span>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
            <div class="p-3 bg-slate-50 rounded-lg border border-slate-200">
              <span class="font-bold text-slate-900 block mb-1">Mỹ EB-5 (Thẻ Xanh Cả Nhà)</span>
              <p class="text-slate-600">Đầu tư: 800,000 USD<br>Thời gian: 2 – 3 năm<br>Quyền lợi: Thường trú nhân Mỹ vĩnh viễn, học phí đại học công như người bản xứ.</p>
            </div>
            <div class="p-3 bg-slate-50 rounded-lg border border-slate-200">
              <span class="font-bold text-slate-900 block mb-1">Hy Lạp Golden Visa</span>
              <p class="text-slate-600">Đầu tư: 250,000 – 400,000 EUR<br>Thời gian: 3 – 6 tháng<br>Quyền lợi: Tự do đi lại 29 nước khối Schengen không cần xin visa.</p>
            </div>
            <div class="p-3 bg-slate-50 rounded-lg border border-slate-200">
              <span class="font-bold text-slate-900 block mb-1">Síp (Cyprus) PR</span>
              <p class="text-slate-600">Đầu tư: 300,000 EUR BĐS<br>Thời gian: 6 tháng<br>Quyền lợi: Thẻ thường trú nhân vĩnh viễn cho 3 thế hệ gia đình.</p>
            </div>
          </div>
        </div>

        <!-- Bảng ánh xạ URL Cũ sang Mới -->
        <div class="overflow-x-auto bg-white rounded-xl border border-slate-200 shadow-sm">
          <div class="p-3.5 bg-slate-100 border-b border-slate-200 font-bold text-xs text-slate-800">
            Ma Trận Xử Lý & Chuẩn Hóa Đường Dẫn (URL Mapping Matrix)
          </div>
          <table class="w-full text-left border-collapse text-xs">
            <thead>
              <tr class="bg-slate-50 border-b border-slate-200 text-slate-700 font-bold">
                <th class="p-3">Đường Dẫn Cũ</th>
                <th class="p-3">Hành Động Kỹ Thuật</th>
                <th class="p-3">Đường Dẫn Chuẩn Mới</th>
                <th class="p-3">Mục Tiêu Chuyển Đổi</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 text-slate-700">
              <tr>
                <td class="p-3 font-mono text-slate-600">/us-green-card-eb-5</td>
                <td class="p-3 font-semibold text-emerald-700">Giữ nguyên hoặc 301</td>
                <td class="p-3 font-mono text-slate-900">/dinh-cu-my-eb5</td>
                <td class="p-3">Điền form nhận lộ trình tài chính EB-5</td>
              </tr>
              <tr>
                <td class="p-3 font-mono text-slate-600">/eu-golden-visa vs /eu-golden-visas</td>
                <td class="p-3 font-semibold text-amber-700">Gộp 301 về 1 trang</td>
                <td class="p-3 font-mono text-slate-900">/golden-visa-chau-au</td>
                <td class="p-3">Tải cẩm nang so sánh thuế Síp vs Hy Lạp</td>
              </tr>
              <tr>
                <td class="p-3 font-mono text-slate-600">/golden-visa-greece & /greece-investment-visa</td>
                <td class="p-3 font-semibold text-amber-700">301 Redirect trang trùng</td>
                <td class="p-3 font-mono text-slate-900">/golden-visa-hy-lap</td>
                <td class="p-3">Đăng ký xem danh mục dự án BĐS Hy Lạp</td>
              </tr>
              <tr>
                <td class="p-3 font-mono text-slate-600">/copy-of-malta-investment-visa-1</td>
                <td class="p-3 font-semibold text-red-700">Xóa bỏ trang rác</td>
                <td class="p-3 font-mono text-slate-400">HTTP 410 Gone / 301 /malta</td>
                <td class="p-3">Triệt tiêu lỗi sitemap</td>
              </tr>
              <tr>
                <td class="p-3 font-mono text-slate-600">(Chưa có)</td>
                <td class="p-3 font-semibold text-blue-700">Xây dựng trang mới</td>
                <td class="p-3 font-mono text-slate-900">/trung-tam-bao-gia-rfq</td>
                <td class="p-3">Tải bảng dự toán chi phí trọn gói PDF</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- ================= SECTION 6: BLUEPRINT SECTIONS TRANG LÕI ================= -->
      <section id="blueprint-sections" class="space-y-6">
        <div class="border-b border-slate-200 pb-3">
          <h2 class="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
            <span class="w-2 h-6 bg-blue-600 rounded-full inline-block"></span>
            6. Cấu Trúc Bố Cục Từng Khối (Blueprint Section-by-Section)
          </h2>
          <p class="text-slate-500 text-xs sm:text-sm mt-1">Mô hình kiến trúc cuộn dọc liên tục (Continuous Layout) chuẩn quốc tế cho trang Landing Page đón quảng cáo.</p>
        </div>

        <div class="bg-white rounded-xl border border-slate-200 p-5 space-y-4 shadow-sm">
          <div class="space-y-3">
            <div class="flex items-center gap-3 p-3 bg-emerald-50 rounded-lg border border-emerald-200">
              <span class="w-7 h-7 rounded-full bg-emerald-600 text-white font-black text-xs flex items-center justify-center shrink-0">1</span>
              <div>
                <h4 class="text-xs sm:text-sm font-bold text-slate-900">Khối 1: Header Tối Giản & Thanh Định Vị Thương Hiệu (Top Bar)</h4>
                <p class="text-xs text-slate-600">Logo GBlueSea sắc nét • 1 Hotline tư vấn 24/7 (0901.830.827) • Nút Chat Zalo trực tiếp • Menu rút gọn dẫn đến các trang di trú chính.</p>
              </div>
            </div>

            <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-lg border border-slate-200">
              <span class="w-7 h-7 rounded-full bg-slate-800 text-white font-black text-xs flex items-center justify-center shrink-0">2</span>
              <div>
                <h4 class="text-xs sm:text-sm font-bold text-slate-900">Khối 2: Hero Banner — Tuyên Bố Giá Trị & Form Thẩm Định Nhanh</h4>
                <p class="text-xs text-slate-600">Headline định vị tỷ lệ đậu 99.2% • 3 Thẻ tín nhiệm (5,300+ Khách hàng, 15 năm kinh nghiệm, văn phòng 5 nước) • Form 3 trường nhận kết quả trong 15 phút.</p>
              </div>
            </div>

            <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-lg border border-slate-200">
              <span class="w-7 h-7 rounded-full bg-slate-800 text-white font-black text-xs flex items-center justify-center shrink-0">3</span>
              <div>
                <h4 class="text-xs sm:text-sm font-bold text-slate-900">Khối 3: Bảng So Sánh Quyền Lợi & Mức Đầu Tư 3 Chương Trình Chiến Lược</h4>
                <p class="text-xs text-slate-600">Đối chiếu trực diện: Mỹ EB-5 vs Hy Lạp vs Síp (Mức vốn, tiến độ thẻ xanh, điều kiện cư trú, quyền lợi gia đình) • Nút tải bảng dự toán PDF.</p>
              </div>
            </div>

            <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-lg border border-slate-200">
              <span class="w-7 h-7 rounded-full bg-slate-800 text-white font-black text-xs flex items-center justify-center shrink-0">4</span>
              <div>
                <h4 class="text-xs sm:text-sm font-bold text-slate-900">Khối 4: Hội Đồng Luật Sư Di Trú & Năng Lực Thụ Lý Hồ Sơ Thực Tế</h4>
                <p class="text-xs text-slate-600">Hình ảnh luật sư trưởng, mã số chứng chỉ hành nghề di trú quốc tế • Quy trình bảo lãnh an toàn vốn đầu tư và tiền thẩm định 3 vòng.</p>
              </div>
            </div>

            <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-lg border border-slate-200">
              <span class="w-7 h-7 rounded-full bg-slate-800 text-white font-black text-xs flex items-center justify-center shrink-0">5</span>
              <div>
                <h4 class="text-xs sm:text-sm font-bold text-slate-900">Khối 5: Câu Chuyện Thành Công & Bằng Chứng Visa Đã Được Cấp</h4>
                <p class="text-xs text-slate-600">Hình ảnh visa/thẻ xanh thực tế đã che thông tin nhạy cảm của khách hàng • Video phỏng vấn cảm nhận khách hàng nhận visa thành công.</p>
              </div>
            </div>

            <div class="flex items-center gap-3 p-3 bg-slate-50 rounded-lg border border-slate-200">
              <span class="w-7 h-7 rounded-full bg-slate-800 text-white font-black text-xs flex items-center justify-center shrink-0">6</span>
              <div>
                <h4 class="text-xs sm:text-sm font-bold text-slate-900">Khối 6: Chân Trang Pháp Lý & Bản Đồ 5 Trụ Sở Toàn Cầu</h4>
                <p class="text-xs text-slate-600">Giấy phép hoạt động tư vấn • Bản đồ Google Maps chỉ đường văn phòng TP.HCM, Hà Nội, Đà Nẵng, Mỹ và Hy Lạp • Cam kết bảo mật thông tin.</p>
              </div>
            </div>

            <div class="flex items-center gap-3 p-3 bg-emerald-100/70 rounded-lg border border-emerald-300">
              <span class="w-7 h-7 rounded-full bg-emerald-700 text-white font-black text-xs flex items-center justify-center shrink-0">★</span>
              <div>
                <h4 class="text-xs sm:text-sm font-bold text-emerald-950">Khối 7: Thanh Cố Định Đáy Màn Hình Di Động (Mobile Sticky Bar)</h4>
                <p class="text-xs text-emerald-900">2 Nút bấm lớn vừa ngón tay cái: [📞 Gọi Ngay: 0901.830.827] và [💬 Nhắn Zalo Tư Vấn 24/7].</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ================= SECTION 7: LƯU Ý GOOGLE ADS (Ở ĐÁY THEO QUY CHUẨN) ================= -->
      <section id="luu-y-google-ads" class="space-y-6 pt-6 border-t-2 border-slate-300">
        <div class="border-b border-slate-200 pb-3">
          <div class="inline-flex items-center gap-2 px-2.5 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-700 mb-2">
            Phần Mở Rộng Kỹ Thuật (Đặt Ở Đáy Báo Cáo)
          </div>
          <h2 class="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
            <span class="w-2 h-6 bg-emerald-600 rounded-full inline-block"></span>
            7. Khuyến Nghị Vận Hành Chiến Dịch Google Search Ads
          </h2>
          <p class="text-slate-500 text-xs sm:text-sm mt-1">Các lưu ý kỹ thuật chuyên sâu về cấu hình tài khoản, đối sánh từ khóa và đo lường trước khi khởi chạy chiến dịch.</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div class="bg-white p-4 rounded-xl border border-slate-200 space-y-2 shadow-2xs">
            <h4 class="text-sm font-bold text-slate-900 flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-emerald-600"></span>
              Phân Nhóm Từ Khóa Theo Ý Định (STAG Structure)
            </h4>
            <p class="text-xs text-slate-600 leading-relaxed">
              Tách bạch từng nhóm quảng cáo theo sản phẩm cụ thể: Nhóm EB-5 Mỹ riêng, Nhóm Golden Visa Hy Lạp riêng, Nhóm Du học Úc riêng. Tuyệt đối không gom chung vào 1 nhóm quảng cáo làm giảm điểm phù hợp (Ad Relevance).
            </p>
          </div>

          <div class="bg-white p-4 rounded-xl border border-slate-200 space-y-2 shadow-2xs">
            <h4 class="text-sm font-bold text-slate-900 flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-emerald-600"></span>
              Loại Bỏ Từ Khóa Rác Bằng Bộ Phủ Định Ngay Từ Đầu
            </h4>
            <p class="text-xs text-slate-600 leading-relaxed">
              Cài đặt danh sách phủ định cấp chiến dịch để chặn các lượt click tốn tiền không sinh ra khách: "miễn phí", "tự làm", "kinh nghiệm phỏng vấn", "diễn đàn webtretho", "lừa đảo", "việc làm chui".
            </p>
          </div>

          <div class="bg-white p-4 rounded-xl border border-slate-200 space-y-2 shadow-2xs">
            <h4 class="text-sm font-bold text-slate-900 flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-emerald-600"></span>
              Thiết Lập Đo Lường Chuyển Đổi Nâng Cao (Enhanced Conversions)
            </h4>
            <p class="text-xs text-slate-600 leading-relaxed">
              Gửi dữ liệu mã hóa (số điện thoại, email) của khách điền form về lại Google Ads để thuật toán Smart Bidding nhận diện đúng tệp khách hàng có tiềm lực tài chính thực sự.
            </p>
          </div>

          <div class="bg-white p-4 rounded-xl border border-slate-200 space-y-2 shadow-2xs">
            <h4 class="text-sm font-bold text-slate-900 flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-emerald-600"></span>
              Nguyên Tắc Bật Tắt Ngân Sách Theo Tiến Độ Sửa Web
            </h4>
            <p class="text-xs text-slate-600 leading-relaxed">
              Chỉ kích hoạt chiến dịch quảng cáo khi đã xử lý xong các lỗi P0 (sửa H1 Acerca de, gắn nút gọi di động và cấu hình tracking). Tránh việc đổ ngân sách vào trang đích đang bị lỗi gây cháy tiền mà không có cuộc gọi.
            </p>
          </div>
        </div>

        <div class="p-4 bg-emerald-50 rounded-xl border border-emerald-200 flex items-center justify-between">
          <div>
            <span class="font-bold text-xs sm:text-sm text-emerald-950 block">Dữ Liệu Hành Động Đã Sẵn Sàng Triển Khai</span>
            <span class="text-xs text-emerald-800">Toàn bộ 14 đầu việc kỹ thuật chi tiết đã được đóng gói trong file Excel đính kèm.</span>
          </div>
          <a href="Du_Lieu_Trien_Khai_Chi_Tiet_visagbluesea.com.xlsx" download class="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs rounded-lg shadow-sm whitespace-nowrap shrink-0">
            Tải Excel 6 Sheets
          </a>
        </div>
      </section>

    </main>
  </div>

  <!-- ================= MOBILE BOTTOM NAVIGATION ================= -->
  <div class="lg:hidden fixed bottom-0 left-0 right-0 z-40 bg-white/95 backdrop-blur-md border-t border-slate-200 px-4 py-2 flex items-center justify-around shadow-lg">
    <a href="#tong-quan" class="flex flex-col items-center gap-1 text-[11px] font-semibold text-slate-600 hover:text-emerald-600">
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
      <span>Tổng Quan</span>
    </a>
    <a href="#diem-nghen-chuyen-doi" class="flex flex-col items-center gap-1 text-[11px] font-semibold text-slate-600 hover:text-red-600">
      <svg class="w-5 h-5 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
      <span>Điểm Nghẽn</span>
    </a>
    <a href="#doi-sanh-truoc-sau" class="flex flex-col items-center gap-1 text-[11px] font-semibold text-slate-600 hover:text-emerald-600">
      <svg class="w-5 h-5 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"/></svg>
      <span>Trước & Sau</span>
    </a>
    <a href="#bang-uu-tien-p0-p3" class="flex flex-col items-center gap-1 text-[11px] font-semibold text-slate-600 hover:text-amber-600">
      <svg class="w-5 h-5 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/></svg>
      <span>Ưu Tiên</span>
    </a>
  </div>

  <!-- ================= LIGHTBOX MODAL ================= -->
  <div id="lightbox-modal" class="fixed inset-0 z-50 bg-slate-950/85 backdrop-blur-md hidden flex items-center justify-center p-4">
    <div class="relative max-w-5xl w-full max-h-[92vh] flex flex-col items-center">
      <button onclick="closeLightbox()" class="absolute -top-12 right-0 text-white hover:text-emerald-400 font-extrabold text-2xl p-2 cursor-pointer transition-colors">
        ✕ Đóng (Esc)
      </button>
      <div class="w-full overflow-auto max-h-[82vh] rounded-xl flex items-center justify-center bg-black/40 p-2">
        <img id="lightbox-img" src="" alt="Chi tiết ảnh" class="max-h-[80vh] w-auto max-w-full object-contain rounded-lg shadow-2xl">
      </div>
      <p id="lightbox-caption" class="text-white text-xs sm:text-sm text-center mt-3 font-medium bg-slate-900/80 px-4 py-2 rounded-full border border-slate-700 max-w-2xl"></p>
    </div>
  </div>

  <!-- JAVASCRIPT LOGIC -->
  <script>
    function openLightbox(src, caption) {
      const modal = document.getElementById('lightbox-modal');
      const img = document.getElementById('lightbox-img');
      const cap = document.getElementById('lightbox-caption');
      img.src = src;
      cap.innerText = caption || 'Chi tiết hình ảnh thẩm định';
      modal.classList.remove('hidden');
      document.body.classList.add('lightbox-open');
    }

    function closeLightbox() {
      const modal = document.getElementById('lightbox-modal');
      modal.classList.add('hidden');
      document.body.classList.remove('lightbox-open');
    }

    document.getElementById('lightbox-modal').addEventListener('click', function(e) {
      if (e.target === this) {
        closeLightbox();
      }
    });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        closeLightbox();
      }
    });
  </script>

</body>
</html>
"""

with open("Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html", "w", encoding="utf-8") as f:
    f.write(html_content)

# Duplicate to index.html at root for immediate browsing / GitHub Pages deployment
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Đã tạo thành công Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html và index.html")
