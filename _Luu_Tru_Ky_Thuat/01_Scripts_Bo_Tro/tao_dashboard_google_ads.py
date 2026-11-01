import os
import json

html_content = '''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Google Ads — FEC Explorer Trại Hè Quốc Tế | Báo Cáo Chuyển Đổi 180 Leads, CVR 12.95%, CPA 93.445 đ</title>
  
  <!-- Google Fonts: Google Sans, Inter & Roboto Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Inter:wght@400;500;600;700&family=Roboto+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  
  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  
  <!-- SheetJS CDN (Export XLSX) -->
  <script src="https://cdn.sheetjs.com/xlsx-0.20.1/package/dist/xlsx.full.min.js"></script>

  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Google Sans"', 'Inter', 'system-ui', 'sans-serif'],
            mono: ['"Roboto Mono"', 'monospace'],
          },
          colors: {
            google: {
              blue: '#1a73e8',
              blueDark: '#1557b0',
              blueLight: '#e8f0fe',
              green: '#1e8e3e',
              greenLight: '#e6f4ea',
              red: '#d93025',
              redLight: '#fce8e6',
              yellow: '#f9ab00',
              yellowLight: '#fef7e0',
              orange: '#e37400',
              gray50: '#f8f9fa',
              gray100: '#f1f3f4',
              gray200: '#e8eaed',
              gray300: '#dadce0',
              gray500: '#5f6368',
              gray700: '#3c4043',
              gray900: '#202124',
            }
          }
        }
      }
    }
  </script>

  <style>
    body {
      background-color: #f8f9fa;
      color: #202124;
      font-family: 'Google Sans', 'Inter', system-ui, sans-serif;
      -webkit-font-smoothing: antialiased;
    }
    
    /* Custom Scrollbar Google Style */
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: #f1f3f4;
    }
    ::-webkit-scrollbar-thumb {
      background: #dadce0;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #bdc1c6;
    }

    /* Google Toggle Switch */
    .g-switch {
      position: relative;
      display: inline-block;
      width: 32px;
      height: 18px;
    }
    .g-switch input {
      opacity: 0;
      width: 0;
      height: 0;
    }
    .g-slider {
      position: absolute;
      cursor: pointer;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: #bdc1c6;
      transition: .2s;
      border-radius: 18px;
    }
    .g-slider:before {
      position: absolute;
      content: "";
      height: 14px;
      width: 14px;
      left: 2px;
      bottom: 2px;
      background-color: white;
      transition: .2s;
      border-radius: 50%;
      box-shadow: 0 1px 3px rgba(0,0,0,0.3);
    }
    input:checked + .g-slider {
      background-color: #1a73e8;
    }
    input:checked + .g-slider:before {
      transform: translateX(14px);
    }

    /* Tab active highlight */
    .nav-item-active {
      background-color: #e8f0fe;
      color: #1a73e8;
      font-weight: 600;
    }
    .nav-item-active i, .nav-item-active svg {
      color: #1a73e8 !important;
    }

    /* Metric card active top border */
    .metric-card-active-blue {
      border-top: 4px solid #1a73e8 !important;
      background: #ffffff;
      box-shadow: 0 1px 3px 0 rgba(60,64,67,.3), 0 4px 8px 3px rgba(60,64,67,.15);
    }
    .metric-card-active-orange {
      border-top: 4px solid #e37400 !important;
      background: #ffffff;
      box-shadow: 0 1px 3px 0 rgba(60,64,67,.3), 0 4px 8px 3px rgba(60,64,67,.15);
    }

    /* Print styles */
    @media print {
      .no-print { display: none !important; }
      body { background: #fff !important; }
      .print-full { width: 100% !important; margin: 0 !important; padding: 0 !important; }
    }
  </style>
</head>
<body class="min-h-screen flex flex-col antialiased select-none">

  <!-- ============================================================== -->
  <!-- 1. TOP HEADER: GOOGLE ADS OFFICIAL NAV BAR                     -->
  <!-- ============================================================== -->
  <header class="bg-white border-b border-google-gray300 h-16 flex items-center justify-between px-4 sticky top-0 z-40 select-none shadow-sm">
    <!-- Left: Hamburger & Logo -->
    <div class="flex items-center gap-4">
      <button id="btnToggleSidebar" class="p-2 rounded-full hover:bg-google-gray100 text-google-gray700 transition" title="Ẩn/hiện thanh điều hướng">
        <i data-lucide="menu" class="w-5 h-5"></i>
      </button>

      <!-- Google Ads Logo -->
      <div class="flex items-center gap-2 cursor-pointer" onclick="location.reload()" title="Trang tổng quan Google Ads">
        <svg class="w-7 h-7" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M43.6 20.3L28.1 4.8C26.5 3.2 23.9 3.2 22.3 4.8L6.8 20.3C5.2 21.9 5.2 24.5 6.8 26.1L22.3 41.6C23.9 43.2 26.5 43.2 28.1 41.6L43.6 26.1C45.2 24.5 45.2 21.9 43.6 20.3Z" fill="#FBBC04"/>
          <path d="M12.4 34.4C10.8 32.8 10.8 30.2 12.4 28.6L27.9 13.1C29.5 11.5 32.1 11.5 33.7 13.1C35.3 14.7 35.3 17.3 33.7 18.9L18.2 34.4C16.6 36 14 36 12.4 34.4Z" fill="#4285F4"/>
          <circle cx="15.3" cy="31.5" r="3.5" fill="#34A853"/>
        </svg>
        <span class="text-xl font-normal text-google-gray700 tracking-tight flex items-center">
          <span class="font-medium text-google-gray900 mr-1">Google</span>Ads
        </span>
      </div>
    </div>

    <!-- Center: Global Search Bar -->
    <div class="hidden md:flex items-center flex-1 max-w-xl mx-8">
      <div class="relative w-full">
        <span class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-google-gray500">
          <i data-lucide="search" class="w-4 h-4"></i>
        </span>
        <input 
          type="text" 
          id="globalSearchInput"
          placeholder="Tìm kiếm chiến dịch trại hè, nhóm quảng cáo, từ khóa... (Gõ '/' để tìm)"
          class="w-full pl-10 pr-12 py-2 bg-google-gray100 hover:bg-google-gray200/70 focus:bg-white border border-transparent focus:border-google-blue rounded-lg text-sm transition outline-none text-google-gray900 placeholder-google-gray500 shadow-inner"
        >
        <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
          <kbd class="px-1.5 py-0.5 text-xs text-google-gray500 bg-white border border-google-gray300 rounded shadow-sm font-mono">/</kbd>
        </div>
      </div>
    </div>

    <!-- Right: Case Selection, Account Switcher & Tools -->
    <div class="flex items-center gap-2">
      <!-- Mode Toggle Switcher -->
      <div class="hidden lg:flex items-center bg-google-gray100 p-1 rounded-lg border border-google-gray300 text-xs">
        <button id="btnModeFec" onclick="switchDataMode('fec')" class="px-3 py-1 rounded font-medium transition bg-white text-google-blue shadow-sm">
          🎓 FEC Explorer (180 Leads - Case 04)
        </button>
        <button id="btnModeVisa" onclick="switchDataMode('visa')" class="px-3 py-1 rounded font-medium transition text-google-gray700 hover:text-google-gray900">
          💼 Visa GBlueSea
        </button>
        <button id="btnModeEcom" onclick="switchDataMode('ecommerce')" class="px-3 py-1 rounded font-medium transition text-google-gray700 hover:text-google-gray900">
          🛒 E-Commerce
        </button>
      </div>

      <!-- Account Switcher Pill -->
      <div class="relative">
        <button id="btnAccountMenu" class="flex items-center gap-2 px-3 py-1.5 rounded-lg border border-google-gray300 hover:bg-google-gray100 transition text-left">
          <div class="w-2.5 h-2.5 rounded-full bg-google-green animate-pulse"></div>
          <div>
            <div id="accountNameDisplay" class="text-xs font-semibold text-google-gray900 leading-tight truncate max-w-[140px] md:max-w-[200px]">
              FEC Explorer Official
            </div>
            <div id="accountCidDisplay" class="text-[10px] text-google-gray500 font-mono">CID: 318-729-6641</div>
          </div>
          <i data-lucide="chevron-down" class="w-3.5 h-3.5 text-google-gray500 ml-1"></i>
        </button>
      </div>

      <!-- Action Buttons -->
      <div class="flex items-center gap-1 border-l border-google-gray300 pl-2">
        <!-- Export Excel -->
        <button onclick="exportToExcel()" class="p-2 rounded-full hover:bg-google-gray100 text-google-gray700 transition" title="Xuất báo cáo Excel (.xlsx)">
          <i data-lucide="file-spreadsheet" class="w-5 h-5 text-emerald-600"></i>
        </button>

        <!-- Print -->
        <button onclick="window.print()" class="p-2 rounded-full hover:bg-google-gray100 text-google-gray700 transition" title="In báo cáo">
          <i data-lucide="printer" class="w-5 h-5"></i>
        </button>

        <!-- Refresh -->
        <button onclick="refreshDataWithAnimation()" class="p-2 rounded-full hover:bg-google-gray100 text-google-gray700 transition" title="Làm mới dữ liệu">
          <i id="refreshIcon" data-lucide="refresh-cw" class="w-5 h-5"></i>
        </button>

        <!-- Avatar -->
        <div class="w-8 h-8 rounded-full bg-emerald-600 text-white flex items-center justify-center font-bold text-xs ml-1 shadow-sm">
          FE
        </div>
      </div>
    </div>
  </header>

  <!-- ============================================================== -->
  <!-- 2. MAIN LAYOUT: SIDEBAR + CONTENT AREA                         -->
  <!-- ============================================================== -->
  <div class="flex-1 flex overflow-hidden">

    <!-- LEFT SIDEBAR: GOOGLE ADS NAVIGATION -->
    <aside id="mainSidebar" class="w-60 bg-white border-r border-google-gray300 flex flex-col justify-between transition-all duration-200 select-none z-30 shrink-0">
      <div class="py-2 overflow-y-auto">
        <!-- Section Header -->
        <div class="px-4 py-2 text-[11px] font-semibold text-google-gray500 uppercase tracking-wider sidebar-text">
          Điều hướng tài khoản
        </div>

        <nav class="space-y-0.5 px-2">
          <a href="#overview" onclick="setActiveNav(this, 'overview')" class="nav-link nav-item-active flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm text-google-gray700 hover:bg-google-gray100 transition">
            <i data-lucide="layout-dashboard" class="w-5 h-5 shrink-0"></i>
            <span class="sidebar-text font-medium">Tổng quan</span>
          </a>

          <a href="#campaigns" onclick="setActiveNav(this, 'campaigns')" class="nav-link flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm text-google-gray700 hover:bg-google-gray100 transition">
            <i data-lucide="layers" class="w-5 h-5 shrink-0 text-google-gray500"></i>
            <span class="sidebar-text">Chiến dịch</span>
            <span id="activeCampaignBadge" class="ml-auto bg-google-blueLight text-google-blue font-semibold text-xs px-2 py-0.5 rounded-full sidebar-text">7</span>
          </a>

          <a href="#adgroups" onclick="setActiveNav(this, 'adgroups')" class="nav-link flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm text-google-gray700 hover:bg-google-gray100 transition">
            <i data-lucide="folder-tree" class="w-5 h-5 shrink-0 text-google-gray500"></i>
            <span class="sidebar-text">Nhóm quảng cáo</span>
          </a>

          <a href="#keywords" onclick="setActiveNav(this, 'keywords')" class="nav-link flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm text-google-gray700 hover:bg-google-gray100 transition">
            <i data-lucide="key" class="w-5 h-5 shrink-0 text-google-gray500"></i>
            <span class="sidebar-text">Từ khóa & Cụm từ</span>
          </a>

          <a href="#conversions" onclick="setActiveNav(this, 'conversions')" class="nav-link flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm text-google-gray700 hover:bg-google-gray100 transition">
            <i data-lucide="target" class="w-5 h-5 shrink-0 text-google-green"></i>
            <span class="sidebar-text font-medium text-google-gray900">Lượt chuyển đổi</span>
            <span class="ml-auto w-2 h-2 rounded-full bg-google-green"></span>
          </a>

          <a href="#landingpages" onclick="setActiveNav(this, 'landingpages')" class="nav-link flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm text-google-gray700 hover:bg-google-gray100 transition">
            <i data-lucide="globe" class="w-5 h-5 shrink-0 text-google-gray500"></i>
            <span class="sidebar-text">Trang đích CRO</span>
          </a>

          <a href="#audiences" onclick="setActiveNav(this, 'audiences')" class="nav-link flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm text-google-gray700 hover:bg-google-gray100 transition">
            <i data-lucide="users" class="w-5 h-5 shrink-0 text-google-gray500"></i>
            <span class="sidebar-text">Đối tượng phụ huynh</span>
          </a>

          <a href="#settings" onclick="setActiveNav(this, 'settings')" class="nav-link flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm text-google-gray700 hover:bg-google-gray100 transition">
            <i data-lucide="settings" class="w-5 h-5 shrink-0 text-google-gray500"></i>
            <span class="sidebar-text">Cài đặt chiến dịch</span>
          </a>
        </nav>
      </div>

      <!-- Bottom Account Summary Card -->
      <div class="p-3 border-t border-google-gray300 sidebar-text">
        <div class="bg-google-gray50 border border-google-gray200 rounded-lg p-2.5">
          <div class="text-[11px] text-google-gray500 font-medium flex items-center justify-between">
            <span>Ngân sách 30 ngày</span>
            <span class="text-google-green font-semibold">Tối ưu CPA</span>
          </div>
          <div class="mt-1.5 flex items-center justify-between text-xs font-semibold text-google-gray900">
            <span id="sidebarCostDisplay">16.820.000 ₫</span>
            <span class="text-google-gray500 font-normal">/ 20.000.000 ₫</span>
          </div>
          <div class="w-full bg-google-gray200 rounded-full h-1.5 mt-2 overflow-hidden">
            <div id="sidebarBudgetBar" class="bg-google-green h-1.5 rounded-full" style="width: 84.1%"></div>
          </div>
        </div>
      </div>
    </aside>

    <!-- RIGHT CONTENT: DASHBOARD WORKSPACE -->
    <main class="flex-1 overflow-y-auto p-4 md:p-6 space-y-6">

      <!-- ============================================================== -->
      <!-- CASE STUDY STRATEGIC BANNER (EXACT REPLICA OF USER IMAGE)      -->
      <!-- ============================================================== -->
      <div id="caseStudyBanner" class="bg-white rounded-xl border border-emerald-200 p-5 shadow-sm relative overflow-hidden">
        <div class="absolute top-0 left-0 w-1.5 h-full bg-emerald-600"></div>

        <div class="flex flex-col lg:flex-row lg:items-start justify-between gap-5">
          <div class="flex-1">
            <div class="flex items-center gap-2 flex-wrap text-xs font-bold uppercase tracking-wider text-emerald-700 mb-1">
              <span>CASE 04 • GIÁO DỤC QUỐC TẾ & DU HỌC HÈ HIGH-TICKET</span>
              <span class="bg-emerald-50 text-emerald-700 border border-emerald-300 px-2 py-0.5 rounded font-mono">
                CPA: 93.445 đ
              </span>
              <span class="bg-blue-50 text-google-blue border border-blue-300 px-2 py-0.5 rounded font-mono">
                CVR: 12,95%
              </span>
            </div>
            
            <h2 class="text-lg md:text-xl font-bold text-google-gray900 mt-1">
              FEC Explorer – 180 Phụ Huynh Đăng Ký, CVR Kỷ Lục 12,95%, CPA 93.445 đ
            </h2>

            <!-- 3 Core Intervention Pillars -->
            <div class="mt-3.5 space-y-2 text-xs text-google-gray700">
              <div class="font-semibold text-google-gray900 flex items-center gap-1.5 text-emerald-800">
                <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600"></i>
                CHIẾN LƯỢC CAN THIỆP CỐT LÕI:
              </div>
              <ul class="space-y-1.5 pl-6 list-disc marker:text-emerald-600">
                <li>
                  <strong>Tách Landing Page chuyên biệt:</strong> Không dùng web trung tâm chung nhiều khóa học gây loãng; tập trung duy nhất vào giải pháp du học hè 6 quốc gia (Mỹ, Úc, Canada, Anh, Nhật/Hàn, Sing-Mã).
                </li>
                <li>
                  <strong>Form đăng ký 4 trường chuẩn CRO:</strong> Phụ huynh chọn ngay quốc gia mong muốn; nút "Đăng Ký Ngay" to rõ, tối ưu tuyệt đối trên màn hình điện thoại.
                </li>
                <li>
                  <strong>Google Search STAG ngách cao:</strong> Phân cụm từ khóa chuẩn ý định theo nước; phủ định triệt để học bổng đại học, du học tự túc dài hạn, thủ tục visa xuất khẩu.
                </li>
              </ul>
            </div>
          </div>

          <!-- Testimonial Quote Box -->
          <div class="w-full lg:w-80 bg-amber-50/70 border border-amber-200 rounded-lg p-3 text-xs shrink-0 flex flex-col justify-between">
            <div>
              <div class="font-semibold text-amber-900 flex items-center gap-1.5 mb-1.5">
                <i data-lucide="sparkles" class="w-4 h-4 text-amber-600"></i>
                Phản hồi từ Quản lý Tuyển sinh FEC:
              </div>
              <p class="text-google-gray700 italic leading-relaxed">
                "Landing Page mới giúp đội tư vấn chốt tour nhẹ nhàng hơn hẳn. Phụ huynh để lại form là đã chọn sẵn quốc gia và hiểu rõ lịch trình, tỷ lệ nghe máy và đặt cọc giữ chỗ tăng vượt kỳ vọng."
              </p>
            </div>
            <div class="mt-2 pt-2 border-t border-amber-200/60 text-[11px] text-amber-800 font-medium flex items-center justify-between">
              <span>Trang đích: fecexplorer.edu.vn</span>
              <span class="text-emerald-700 font-bold">180 Đăng Ký</span>
            </div>
          </div>
        </div>
      </div>

      <!-- ============================================================== -->
      <!-- 3. TOP ACTION BAR: BREADCRUMBS, DATE PICKER & QUICK FILTERS    -->
      <!-- ============================================================== -->
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white p-4 rounded-xl border border-google-gray300 shadow-sm">
        
        <!-- Breadcrumb & Title -->
        <div>
          <div class="flex items-center gap-2 text-xs text-google-gray500 mb-1">
            <span>Tất cả chiến dịch</span>
            <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
            <span class="text-google-gray700 font-medium">Báo cáo hiệu suất Google Ads</span>
          </div>
          <h1 id="pageMainHeading" class="text-xl md:text-2xl font-bold text-google-gray900 flex items-center gap-2.5">
            Tỷ Lệ Chuyển Đổi Kỷ Lục 12,95%, CPA 93.445 đ
            <span id="headingBadge" class="text-xs font-semibold bg-emerald-50 text-emerald-700 border border-emerald-300 px-2.5 py-0.5 rounded-full">
              180 Chuyển Đổi
            </span>
          </h1>
        </div>

        <!-- Date Range Selector Pill with Popover -->
        <div class="relative">
          <button 
            id="btnDateRangePicker" 
            onclick="toggleDatePickerPopover()"
            class="flex items-center gap-3 px-4 py-2 bg-white hover:bg-google-gray50 border border-google-gray300 rounded-lg shadow-sm text-sm font-medium text-google-gray700 transition"
          >
            <i data-lucide="calendar" class="w-4 h-4 text-google-blue"></i>
            <span id="dateRangeLabel">Tháng 7 18 – Tháng 8 16, 2026 (30 ngày qua)</span>
            <i data-lucide="chevron-down" class="w-4 h-4 text-google-gray500 ml-1"></i>
          </button>

          <!-- DATE PICKER POPOVER MODAL -->
          <div 
            id="datePickerPopover" 
            class="hidden absolute right-0 mt-2 w-80 md:w-96 bg-white border border-google-gray300 rounded-xl shadow-xl z-50 p-4 transition-all"
          >
            <div class="text-xs font-semibold text-google-gray500 uppercase tracking-wider mb-2">Khoảng thời gian</div>
            <div class="grid grid-cols-2 gap-1.5 text-sm mb-4">
              <button onclick="setDateRange('today')" class="preset-date-btn text-left px-3 py-1.5 rounded hover:bg-google-gray100 text-google-gray700">Hôm nay</button>
              <button onclick="setDateRange('yesterday')" class="preset-date-btn text-left px-3 py-1.5 rounded hover:bg-google-gray100 text-google-gray700">Hôm qua</button>
              <button onclick="setDateRange('7days')" class="preset-date-btn text-left px-3 py-1.5 rounded hover:bg-google-gray100 text-google-gray700">7 ngày qua</button>
              <button onclick="setDateRange('14days')" class="preset-date-btn text-left px-3 py-1.5 rounded hover:bg-google-gray100 text-google-gray700">14 ngày qua</button>
              <button onclick="setDateRange('30days')" class="preset-date-btn active-preset text-left px-3 py-1.5 rounded bg-google-blueLight text-google-blue font-semibold">30 ngày qua (T7 18 - T8 16)</button>
              <button onclick="setDateRange('this_month')" class="preset-date-btn text-left px-3 py-1.5 rounded hover:bg-google-gray100 text-google-gray700">Tháng này</button>
              <button onclick="setDateRange('last_month')" class="preset-date-btn text-left px-3 py-1.5 rounded hover:bg-google-gray100 text-google-gray700">Tháng trước</button>
              <button onclick="setDateRange('all_time')" class="preset-date-btn text-left px-3 py-1.5 rounded hover:bg-google-gray100 text-google-gray700">Toàn thời gian</button>
            </div>

            <div class="border-t border-google-gray200 pt-3 mb-3">
              <div class="text-xs font-semibold text-google-gray500 mb-2">So với kỳ trước</div>
              <div class="text-xs text-google-gray700 bg-google-gray100 p-2 rounded border border-google-gray200 font-mono">
                Tháng 6 18 – Tháng 7 17, 2026
              </div>
            </div>

            <!-- Compare Checkbox -->
            <div class="flex items-center gap-2 mb-4">
              <input type="checkbox" id="compareCheckbox" checked class="w-4 h-4 text-google-blue rounded border-google-gray300">
              <label for="compareCheckbox" class="text-xs text-google-gray700 cursor-pointer">Bật so sánh số liệu với kỳ trước</label>
            </div>

            <div class="flex items-center justify-end gap-2 border-t border-google-gray200 pt-3">
              <button onclick="toggleDatePickerPopover()" class="px-3 py-1.5 text-xs text-google-gray700 hover:bg-google-gray100 rounded font-medium">Hủy</button>
              <button onclick="setDateRange('30days')" class="px-4 py-1.5 text-xs bg-google-blue text-white hover:bg-google-blueDark rounded font-medium shadow-sm">Áp dụng</button>
            </div>
          </div>
        </div>
      </div>

      <!-- ============================================================== -->
      <!-- 4. GOOGLE ADS EXECUTIVE SCORECARDS (EXACT MATCH 4 STAT CARDS)  -->
      <!-- ============================================================== -->
      <div>
        <div class="flex items-center justify-between mb-2">
          <div class="text-xs font-semibold text-google-gray500 uppercase tracking-wider flex items-center gap-1.5">
            <i data-lucide="line-chart" class="w-4 h-4 text-google-blue"></i>
            Chỉ số cốt lõi (Bấm chọn 2 thẻ để đổi đường vẽ trên biểu đồ)
          </div>
          <div class="text-xs text-google-gray500 hidden sm:block">
            <span class="inline-block w-3 h-3 bg-[#1a73e8] rounded-full mr-1 align-middle"></span>Đường 1 (Xanh)
            <span class="inline-block w-3 h-3 bg-[#e37400] rounded-full mr-1 ml-3 align-middle"></span>Đường 2 (Cam)
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <!-- Card 1: 180 Phụ Huynh Đăng Ký (Active Blue) -->
          <div 
            id="metricCard1" 
            onclick="selectMetricForChart(1, 'conversions')" 
            class="metric-card metric-card-active-blue bg-white rounded-xl p-4 border border-google-gray300 transition-all cursor-pointer relative hover:shadow-md"
          >
            <div class="flex items-center justify-between text-google-gray500 text-xs font-medium mb-1">
              <span id="metricCardLabel1" class="flex items-center gap-1">
                Lượt phụ huynh đăng ký
                <i data-lucide="chevron-down" class="w-3 h-3"></i>
              </span>
              <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-blue-50 text-google-blue border border-blue-200">
                Đường 1 (Xanh)
              </span>
            </div>
            <div id="metricValue1" class="text-2xl md:text-3xl font-bold text-emerald-700 tracking-tight my-1">
              180 Phụ Huynh
            </div>
            <div class="flex items-center gap-1.5 text-xs text-google-green font-medium">
              <i data-lucide="trending-up" class="w-4 h-4"></i>
              <span id="metricDiff1">+24.1%</span>
              <span class="text-google-gray500 font-normal">so với kỳ trước (145)</span>
            </div>
          </div>

          <!-- Card 2: Chi phí / Lead (CPA) 93.445 đ -->
          <div 
            id="metricCard2" 
            onclick="selectMetricForChart(2, 'cpa')" 
            class="metric-card metric-card-active-orange bg-white rounded-xl p-4 border border-google-gray300 transition-all cursor-pointer relative hover:shadow-md"
          >
            <div class="flex items-center justify-between text-google-gray500 text-xs font-medium mb-1">
              <span id="metricCardLabel2" class="flex items-center gap-1">
                Chi phí / Lead (CPA)
                <i data-lucide="chevron-down" class="w-3 h-3"></i>
              </span>
              <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-amber-50 text-google-orange border border-amber-200">
                Đường 2 (Cam)
              </span>
            </div>
            <div id="metricValue2" class="text-2xl md:text-3xl font-bold text-google-gray900 tracking-tight my-1 font-mono">
              93.445 đ
            </div>
            <div class="flex items-center gap-1.5 text-xs text-google-green font-medium">
              <i data-lucide="trending-down" class="w-4 h-4"></i>
              <span id="metricDiff2">-31.2%</span>
              <span class="text-google-gray500 font-normal">giảm chi phí mỗi phụ huynh</span>
            </div>
          </div>

          <!-- Card 3: Tỷ lệ chuyển đổi (CVR) 12,95% -->
          <div 
            id="metricCard3" 
            onclick="selectMetricForChart(1, 'cvr')" 
            class="metric-card bg-white rounded-xl p-4 border border-google-gray300 transition-all cursor-pointer relative hover:shadow-md"
          >
            <div class="flex items-center justify-between text-google-gray500 text-xs font-medium mb-1">
              <span id="metricCardLabel3" class="flex items-center gap-1">
                Tỷ lệ chuyển đổi (CVR)
                <i data-lucide="chevron-down" class="w-3 h-3"></i>
              </span>
              <span class="text-[10px] text-google-gray500">Bấm để vẽ</span>
            </div>
            <div id="metricValue3" class="text-2xl md:text-3xl font-bold text-google-blue tracking-tight my-1 font-mono">
              12,95%
            </div>
            <div class="flex items-center gap-1.5 text-xs text-google-green font-medium">
              <i data-lucide="trending-up" class="w-4 h-4"></i>
              <span id="metricDiff3">+4.15%</span>
              <span class="text-google-gray500 font-normal">tỷ lệ chốt tour kỷ lục</span>
            </div>
          </div>

          <!-- Card 4: Ngân sách Ads 30 ngày 16.820.000 đ -->
          <div 
            id="metricCard4" 
            onclick="selectMetricForChart(2, 'cost')" 
            class="metric-card bg-white rounded-xl p-4 border border-google-gray300 transition-all cursor-pointer relative hover:shadow-md"
          >
            <div class="flex items-center justify-between text-google-gray500 text-xs font-medium mb-1">
              <span id="metricCardLabel4" class="flex items-center gap-1">
                Ngân sách Ads 30 ngày
                <i data-lucide="chevron-down" class="w-3 h-3"></i>
              </span>
              <span class="text-[10px] text-google-gray500">Bấm để vẽ</span>
            </div>
            <div id="metricValue4" class="text-2xl md:text-3xl font-bold text-purple-700 tracking-tight my-1 font-mono">
              16.820.000 đ
            </div>
            <div class="flex items-center gap-1.5 text-xs text-google-green font-medium">
              <i data-lucide="check" class="w-4 h-4"></i>
              <span id="metricDiff4">100%</span>
              <span class="text-google-gray500 font-normal">đúng định mức phân bổ</span>
            </div>
          </div>
        </div>
      </div>

      <!-- ============================================================== -->
      <!-- 5. TIME-SERIES DUAL-AXIS INTERACTIVE CHART                     -->
      <!-- ============================================================== -->
      <div class="bg-white p-5 rounded-xl border border-google-gray300 shadow-sm">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4 pb-3 border-b border-google-gray200">
          <div>
            <h2 class="text-base font-semibold text-google-gray900 flex items-center gap-2">
              <span id="chartTitlePrimary" class="text-google-blue">Lượt phụ huynh đăng ký</span>
              <span class="text-google-gray500 font-normal">so với</span>
              <span id="chartTitleSecondary" class="text-google-orange">Chi phí / Lead (CPA)</span>
            </h2>
            <p class="text-xs text-google-gray500 mt-0.5">
              Diễn biến đăng ký hàng ngày và biến động CPA từ 18/07/2026 đến 16/08/2026
            </p>
          </div>

          <!-- Chart Controls: Day / Week / Month -->
          <div class="flex items-center bg-google-gray100 p-1 rounded-lg border border-google-gray300 text-xs">
            <button onclick="setChartGranularity('day')" id="btnGranularityDay" class="px-3 py-1 rounded font-medium transition bg-white text-google-gray900 shadow-sm">
              Ngày
            </button>
            <button onclick="setChartGranularity('week')" id="btnGranularityWeek" class="px-3 py-1 rounded font-medium transition text-google-gray700 hover:text-google-gray900">
              Tuần
            </button>
            <button onclick="setChartGranularity('month')" id="btnGranularityMonth" class="px-3 py-1 rounded font-medium transition text-google-gray700 hover:text-google-gray900">
              Tháng
            </button>
          </div>
        </div>

        <!-- Canvas -->
        <div class="relative w-full h-[320px] md:h-[380px]">
          <canvas id="googleAdsChart"></canvas>
        </div>
      </div>

      <!-- ============================================================== -->
      <!-- 6. CAMPAIGNS DATA TABLE (GOOGLE ADS INTERACTIVE STANDARD)      -->
      <!-- ============================================================== -->
      <div class="bg-white rounded-xl border border-google-gray300 shadow-sm overflow-hidden" id="campaignsSection">
        
        <!-- Table Action Bar -->
        <div class="p-4 border-b border-google-gray200 flex flex-col md:flex-row md:items-center justify-between gap-3 bg-white">
          <div class="flex items-center gap-3 flex-wrap">
            <!-- New Campaign Button -->
            <button onclick="showNewCampaignModal()" class="flex items-center gap-2 bg-google-blue hover:bg-google-blueDark text-white px-3.5 py-2 rounded-lg text-xs font-medium shadow-sm transition">
              <i data-lucide="plus" class="w-4 h-4"></i>
              Chiến dịch mới
            </button>

            <!-- Table Search -->
            <div class="relative">
              <span class="absolute inset-y-0 left-0 pl-2.5 flex items-center pointer-events-none text-google-gray500">
                <i data-lucide="search" class="w-3.5 h-3.5"></i>
              </span>
              <input 
                type="text" 
                id="campaignTableSearch" 
                onkeyup="filterCampaignTable()"
                placeholder="Lọc tên chiến dịch trại hè..." 
                class="pl-8 pr-3 py-1.5 border border-google-gray300 rounded-lg text-xs w-48 md:w-64 focus:border-google-blue outline-none"
              >
            </div>

            <!-- Filter Status Pill -->
            <div class="flex items-center bg-google-gray100 p-0.5 rounded-lg border border-google-gray300 text-xs">
              <button onclick="filterByStatus('all')" id="btnFilterAll" class="px-2.5 py-1 rounded font-medium bg-white text-google-gray900 shadow-sm">
                Tất cả (<span id="countAll">7</span>)
              </button>
              <button onclick="filterByStatus('enabled')" id="btnFilterEnabled" class="px-2.5 py-1 rounded font-medium text-google-gray700 hover:text-google-gray900">
                Đang bật (<span id="countEnabled">7</span>)
              </button>
              <button onclick="filterByStatus('paused')" id="btnFilterPaused" class="px-2.5 py-1 rounded font-medium text-google-gray700 hover:text-google-gray900">
                Tạm dừng (<span id="countPaused">0</span>)
              </button>
            </div>
          </div>

          <div class="flex items-center gap-2">
            <!-- Export Table to Excel Button -->
            <button onclick="exportToExcel()" class="flex items-center gap-1.5 px-3 py-1.5 border border-google-gray300 rounded-lg text-xs font-medium text-google-gray700 hover:bg-google-gray50 transition">
              <i data-lucide="download" class="w-3.5 h-3.5 text-emerald-600"></i>
              Tải Excel (.xlsx)
            </button>
          </div>
        </div>

        <!-- Bulk Actions Notification -->
        <div id="bulkActionBar" class="hidden bg-google-blueLight border-b border-blue-200 px-4 py-2 flex items-center justify-between text-xs text-google-blue font-medium">
          <div class="flex items-center gap-2">
            <span id="bulkSelectedCount">Đã chọn 2 chiến dịch</span>
            <span class="text-google-gray500">|</span>
            <button onclick="bulkToggleStatus(true)" class="hover:underline font-semibold">Bật tất cả</button>
            <button onclick="bulkToggleStatus(false)" class="hover:underline font-semibold ml-2">Tạm dừng tất cả</button>
          </div>
          <button onclick="clearBulkSelection()" class="text-google-gray500 hover:text-google-gray900">Bỏ chọn</button>
        </div>

        <!-- Scrollable Table -->
        <div class="overflow-x-auto max-h-[500px]">
          <table class="w-full text-left border-collapse text-xs select-text">
            <thead class="bg-google-gray50 border-b border-google-gray300 sticky top-0 z-20 text-google-gray700 font-semibold select-none">
              <tr>
                <th class="py-3 px-3 w-10 text-center">
                  <input type="checkbox" id="masterCheckbox" onchange="toggleSelectAllRows(this)" class="w-3.5 h-3.5 rounded border-google-gray300 text-google-blue">
                </th>
                <th class="py-3 px-3 w-28 cursor-pointer hover:bg-google-gray200/50" onclick="sortTable('status')">
                  Trạng thái <span id="sort_status">↕</span>
                </th>
                <th class="py-3 px-4 min-w-[250px] cursor-pointer hover:bg-google-gray200/50" onclick="sortTable('name')">
                  Chiến dịch (Quốc gia du học hè) <span id="sort_name">↕</span>
                </th>
                <th class="py-3 px-3 text-right cursor-pointer hover:bg-google-gray200/50" onclick="sortTable('budget')">
                  Ngân sách/ngày <span id="sort_budget">↕</span>
                </th>
                <th class="py-3 px-3 text-right cursor-pointer hover:bg-google-gray200/50" onclick="sortTable('optScore')">
                  Điểm tối ưu <span id="sort_optScore">↕</span>
                </th>
                <th class="py-3 px-3 text-right cursor-pointer hover:bg-google-gray200/50" onclick="sortTable('clicks')">
                  Lượt nhấp <span id="sort_clicks">↕</span>
                </th>
                <th class="py-3 px-3 text-right cursor-pointer hover:bg-google-gray200/50" onclick="sortTable('impressions')">
                  Lượt hiển thị <span id="sort_impressions">↕</span>
                </th>
                <th class="py-3 px-3 text-right cursor-pointer hover:bg-google-gray200/50" onclick="sortTable('ctr')">
                  CTR <span id="sort_ctr">↕</span>
                </th>
                <th class="py-3 px-3 text-right cursor-pointer hover:bg-google-gray200/50" onclick="sortTable('avgCpc')">
                  CPC TB <span id="sort_avgCpc">↕</span>
                </th>
                <th class="py-3 px-4 text-right cursor-pointer hover:bg-google-gray200/50 font-bold" onclick="sortTable('cost')">
                  Chi phí 30 ngày (₫) <span id="sort_cost">↕</span>
                </th>
                <th class="py-3 px-4 text-right cursor-pointer hover:bg-google-gray200/50 font-bold text-emerald-700" onclick="sortTable('conversions')">
                  Phụ huynh đăng ký <span id="sort_conversions">↕</span>
                </th>
                <th class="py-3 px-3 text-right cursor-pointer hover:bg-google-gray200/50 text-google-orange font-bold" onclick="sortTable('cpa')">
                  CPA (₫) <span id="sort_cpa">↕</span>
                </th>
                <th class="py-3 px-3 text-right cursor-pointer hover:bg-google-gray200/50 text-google-blue font-bold" onclick="sortTable('cvr')">
                  CVR (%) <span id="sort_cvr">↕</span>
                </th>
                <th class="py-3 px-4 text-right cursor-pointer hover:bg-google-gray200/50" onclick="sortTable('convValue')">
                  Doanh thu dự kiến <span id="sort_convValue">↕</span>
                </th>
                <th class="py-3 px-3 text-right cursor-pointer hover:bg-google-gray200/50" onclick="sortTable('roas')">
                  ROAS <span id="sort_roas">↕</span>
                </th>
              </tr>
            </thead>
            <tbody id="campaignTableBody" class="divide-y divide-google-gray200 bg-white">
              <!-- Dynamically populated via JS -->
            </tbody>
            <!-- Sticky Total Footer -->
            <tfoot class="bg-google-gray100 border-t-2 border-google-gray300 font-bold text-google-gray900 sticky bottom-0 z-20">
              <tr id="tableTotalRow">
                <td class="py-3 px-3 text-center">∑</td>
                <td class="py-3 px-3 text-google-gray700 font-semibold" colspan="2">
                  Tổng cộng: <span id="footerTotalCampaignsCount">7</span> chiến dịch hoạt động
                </td>
                <td class="py-3 px-3 text-right font-mono" id="footerTotalDailyBudget">800.000 ₫</td>
                <td class="py-3 px-3 text-right text-google-blue font-mono" id="footerAvgOptScore">94.8%</td>
                <td class="py-3 px-3 text-right font-mono" id="footerTotalClicks">1.390</td>
                <td class="py-3 px-3 text-right font-mono" id="footerTotalImpressions">15.800</td>
                <td class="py-3 px-3 text-right font-mono text-emerald-700" id="footerAvgCtr">8,80%</td>
                <td class="py-3 px-3 text-right font-mono" id="footerAvgCpc">12.101 ₫</td>
                <td class="py-3 px-4 text-right font-mono text-purple-700 font-bold" id="footerTotalCost">16.820.000 ₫</td>
                <td class="py-3 px-4 text-right font-mono text-emerald-700 font-bold text-sm" id="footerTotalConversions">180</td>
                <td class="py-3 px-3 text-right font-mono text-google-orange font-bold" id="footerAvgCpa">93.445 ₫</td>
                <td class="py-3 px-3 text-right font-mono text-google-blue font-bold text-sm" id="footerAvgCvr">12,95%</td>
                <td class="py-3 px-4 text-right font-mono" id="footerTotalValue">1.890.000.000 ₫</td>
                <td class="py-3 px-3 text-right font-mono text-google-green" id="footerAvgRoas">112.3x</td>
              </tr>
            </tfoot>
          </table>
        </div>
      </div>

      <!-- ============================================================== -->
      <!-- 7. FOUR DEEP CONVERSION BREAKDOWN WIDGETS                      -->
      <!-- ============================================================== -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        
        <!-- WIDGET 1: Conversion Actions Breakdown -->
        <div class="bg-white rounded-xl border border-google-gray300 p-4 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2 border-b border-google-gray200 mb-3">
              <h3 class="text-xs font-semibold uppercase tracking-wider text-google-gray700 flex items-center gap-1.5">
                <i data-lucide="check-circle-2" class="w-4 h-4 text-google-green"></i>
                Hành động chuyển đổi
              </h3>
              <span class="text-[11px] text-google-gray500">Tỷ trọng</span>
            </div>
            
            <div id="conversionActionsContainer" class="space-y-3">
              <!-- Dynamically populated -->
            </div>
          </div>
          <div class="pt-3 border-t border-google-gray100 text-[11px] text-google-gray500 flex justify-between items-center mt-3">
            <span>Form 4 trường CRO</span>
            <span class="text-emerald-700 font-semibold">Chiếm 73.3% Leads</span>
          </div>
        </div>

        <!-- WIDGET 2: Device Share (Donut Chart) -->
        <div class="bg-white rounded-xl border border-google-gray300 p-4 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2 border-b border-google-gray200 mb-3">
              <h3 class="text-xs font-semibold uppercase tracking-wider text-google-gray700 flex items-center gap-1.5">
                <i data-lucide="smartphone" class="w-4 h-4 text-google-blue"></i>
                Chuyển đổi theo thiết bị
              </h3>
              <span class="text-[11px] text-google-gray500">Thiết bị</span>
            </div>

            <div class="relative h-36 flex items-center justify-center my-1">
              <canvas id="deviceChart"></canvas>
            </div>

            <div id="deviceLegendContainer" class="mt-2 space-y-1 text-xs">
              <!-- Dynamically populated -->
            </div>
          </div>
          <div class="pt-2 border-t border-google-gray100 text-[11px] text-google-gray500 text-center mt-2">
            Phụ huynh lướt mobile chiếm ưu thế (78.5%)
          </div>
        </div>

        <!-- WIDGET 3: Top Converting Keywords -->
        <div class="bg-white rounded-xl border border-google-gray300 p-4 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2 border-b border-google-gray200 mb-3">
              <h3 class="text-xs font-semibold uppercase tracking-wider text-google-gray700 flex items-center gap-1.5">
                <i data-lucide="key" class="w-4 h-4 text-amber-500"></i>
                Top Từ khóa sinh chuyển đổi
              </h3>
              <span class="text-[11px] text-google-gray500">Đăng ký</span>
            </div>

            <div id="topKeywordsContainer" class="space-y-2 text-xs">
              <!-- Dynamically populated -->
            </div>
          </div>
          <div class="pt-3 border-t border-google-gray100 text-[11px] text-google-blue flex justify-between items-center mt-3 cursor-pointer hover:underline" onclick="scrollToKeywords()">
            <span>Phủ định rác học bổng & du học dài hạn</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </div>
        </div>

        <!-- WIDGET 4: Geo Locations Breakdown -->
        <div class="bg-white rounded-xl border border-google-gray300 p-4 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2 border-b border-google-gray200 mb-3">
              <h3 class="text-xs font-semibold uppercase tracking-wider text-google-gray700 flex items-center gap-1.5">
                <i data-lucide="map-pin" class="w-4 h-4 text-google-red"></i>
                Khu vực phụ huynh (Locations)
              </h3>
              <span class="text-[11px] text-google-gray500">Tỉnh thành</span>
            </div>

            <div id="geoLocationsContainer" class="space-y-2.5 text-xs">
              <!-- Dynamically populated -->
            </div>
          </div>
          <div class="pt-3 border-t border-google-gray100 text-[11px] text-google-gray500 flex justify-between items-center mt-3">
            <span>Hà Nội & TP.HCM (86.5%)</span>
            <span class="text-google-blue font-semibold">Tập trung cao</span>
          </div>
        </div>

      </div>

      <!-- ============================================================== -->
      <!-- 8. FOOTER NOTE & AUDIT CONFIRMATION                            -->
      <!-- ============================================================== -->
      <footer class="text-center text-xs text-google-gray500 py-4 border-t border-google-gray200 select-none">
        <p>Hệ thống mô phỏng Google Ads Dashboard chuẩn xác 100% dựa trên Case 04: FEC Explorer (fecexplorer.edu.vn).</p>
        <p class="mt-1">Thời gian thống kê: <strong>Tháng 7 18 – Tháng 8 16, 2026</strong> | 180 Phụ Huynh Đăng Ký | Ngân Sách: 16.820.000 đ | CPA: 93.445 đ | CVR: 12,95%.</p>
      </footer>

    </main>
  </div>

  <!-- ============================================================== -->
  <!-- 9. TOAST NOTIFICATION CONTAINER                                -->
  <!-- ============================================================== -->
  <div id="toastNotification" class="fixed bottom-6 left-1/2 transform -translate-x-1/2 bg-google-gray900 text-white px-5 py-2.5 rounded-lg shadow-xl text-xs font-medium hidden flex items-center gap-3 z-50">
    <span id="toastMessage">Đã nạp dữ liệu Case 04: FEC Explorer thành công.</span>
    <button onclick="hideToast()" class="text-google-blue hover:text-blue-300 font-bold ml-2">Đóng</button>
  </div>

  <!-- ============================================================== -->
  <!-- 10. JAVASCRIPT: LOGIC & INTERACTIVITY ENGINE                   -->
  <!-- ============================================================== -->
  <script>
    // -------------------------------------------------------------
    // DATA REPOSITORY: 3 MODES (FEC EXPLORER, VISA, E-COMMERCE)
    // -------------------------------------------------------------
    const DATASETS = {
      fec: {
        accountName: "FEC Explorer – Trại Hè Quốc Tế",
        cid: "318-729-6641",
        dateLabel: "Tháng 7 18 – Tháng 8 16, 2026 (30 ngày qua)",
        compareLabel: "So với: Tháng 6 18 – Tháng 7 17, 2026",
        pageHeading: "Tỷ Lệ Chuyển Đổi Kỷ Lục 12,95%, CPA 93.445 đ",
        badgeText: "180 Chuyển Đổi",
        metric1Name: "Lượt phụ huynh đăng ký",
        metric1Value: "180 Phụ Huynh",
        metric1Diff: "+24.1%",
        metric2Name: "Chi phí / Lead (CPA)",
        metric2Value: "93.445 đ",
        metric2Diff: "-31.2%",
        metric3Name: "Tỷ lệ chuyển đổi (CVR)",
        metric3Value: "12,95%",
        metric3Diff: "+4.15%",
        metric4Name: "Ngân sách Ads 30 ngày",
        metric4Value: "16.820.000 đ",
        metric4Diff: "100%",
        campaigns: [
          {
            id: 1,
            name: "GGSearch_TraiHe_My_USA",
            type: "Search",
            bidding: "Target CPA: 92k",
            status: true,
            dailyBudget: 200000,
            optScore: 96.2,
            clicks: 360,
            impressions: 3900,
            cost: 4416000,
            conversions: 48,
            value: 672000000,
          },
          {
            id: 2,
            name: "GGSearch_TraiHe_Uc_Australia",
            type: "Search",
            bidding: "Target CPA: 92k",
            status: true,
            dailyBudget: 1500000,
            optScore: 95.0,
            clicks: 290,
            impressions: 3250,
            cost: 3496000,
            conversions: 38,
            value: 494000000,
          },
          {
            id: 3,
            name: "GGSearch_TraiHe_Canada",
            type: "Search",
            bidding: "Tối đa hóa chuyển đổi",
            status: true,
            dailyBudget: 120000,
            optScore: 94.5,
            clicks: 220,
            impressions: 2500,
            cost: 2660000,
            conversions: 28,
            value: 336000000,
          },
          {
            id: 4,
            name: "GGSearch_TraiHe_Singapore_Malaysia",
            type: "Search",
            bidding: "Target CPA: 90k",
            status: true,
            dailyBudget: 100000,
            optScore: 95.8,
            clicks: 210,
            impressions: 2450,
            cost: 2340000,
            conversions: 26,
            value: 182000000,
          },
          {
            id: 5,
            name: "GGSearch_TraiHe_AnhQuoc_UK",
            type: "Search",
            bidding: "Target CPA: 100k",
            status: true,
            dailyBudget: 100000,
            optScore: 93.4,
            clicks: 150,
            impressions: 1700,
            cost: 2000000,
            conversions: 20,
            value: 260000000,
          },
          {
            id: 6,
            name: "GGSearch_TraiHe_NhatBan_HanQuoc",
            type: "Search",
            bidding: "Tối đa hóa chuyển đổi",
            status: true,
            dailyBudget: 80000,
            optScore: 92.1,
            clicks: 100,
            impressions: 1250,
            cost: 1200000,
            conversions: 12,
            value: 108000000,
          },
          {
            id: 7,
            name: "GGSearch_ThuongHieu_FEC_Explorer",
            type: "Search",
            bidding: "Target Impression Share",
            status: true,
            dailyBudget: 50000,
            optScore: 98.6,
            clicks: 60,
            impressions: 750,
            cost: 708000,
            conversions: 8,
            value: 96000000,
          }
        ],
        dailyConversions: [7, 5, 8, 4, 6, 7, 5, 9, 4, 6, 7, 5, 8, 4, 7, 5, 6, 8, 5, 5, 7, 6, 4, 7, 8, 5, 6, 5, 7, 4],
        dailyCosts: [645000, 480000, 720000, 390000, 560000, 650000, 490000, 810000, 385000, 560000, 655000, 485000, 735000, 395000, 660000, 475000, 555000, 740000, 485000, 485000, 650000, 565000, 390000, 660000, 735000, 490000, 560000, 485000, 645000, 404000],
        actions: [
          { name: "Form Đăng Ký Tư Vấn Trại Hè (fecexplorer.edu.vn)", count: 132, pct: 73.3, cpa: 88500, icon: "file-text" },
          { name: "Cuộc Gọi Hotline Tư Vấn Tuyển Sinh", count: 34, pct: 18.9, cpa: 102000, icon: "phone-call" },
          { name: "Nhắn Tin Zalo OA Nhận Lịch Trình Chi Tiết", count: 14, pct: 7.8, cpa: 118000, icon: "message-square" }
        ],
        keywords: [
          { kw: "trại hè quốc tế mỹ 2026", type: "Exact", conv: 32, cpa: 89000, cvr: 14.5 },
          { kw: "du học hè úc cho học sinh", type: "Exact", conv: 26, cpa: 91500, cvr: 13.8 },
          { kw: "trại hè tiếng anh canada", type: "Phrase", conv: 21, cpa: 94000, cvr: 12.9 },
          { kw: "du học hè singapore malaysia", type: "Phrase", conv: 19, cpa: 87000, cvr: 13.1 },
          { kw: "fec explorer trại hè", type: "Exact", conv: 16, cpa: 62000, cvr: 18.2 },
          { kw: "chi phí du học hè anh quốc", type: "Phrase", conv: 14, cpa: 98000, cvr: 12.2 }
        ],
        locations: [
          { name: "Hà Nội", pct: 48.5, conv: 87 },
          { name: "Hồ Chí Minh", pct: 38.0, conv: 68 },
          { name: "Đà Nẵng & Miền Trung", pct: 8.5, conv: 15 },
          { name: "Các tỉnh thành khác", pct: 5.0, conv: 10 }
        ],
        devices: [
          { label: "Thiết bị di động (Mobile)", pct: 78.5, color: "#1a73e8" },
          { label: "Máy tính để bàn (Desktop)", pct: 19.5, color: "#1e8e3e" },
          { label: "Máy tính bảng (Tablet)", pct: 2.0, color: "#f9ab00" }
        ]
      },

      visa: {
        accountName: "Tập đoàn Định cư & Visa GBlueSea",
        cid: "482-195-8832",
        dateLabel: "01/10/2026 – 31/10/2026 (30 ngày qua)",
        compareLabel: "So với: 01/09/2026 – 30/09/2026",
        pageHeading: "Báo Cáo Hiệu Quả Chiến Dịch Google Search — visagbluesea.com",
        badgeText: "248 Chuyển Đổi",
        metric1Name: "Lượt chuyển đổi (Hồ sơ tư vấn)",
        metric1Value: "248 Leads",
        metric1Diff: "+18.4%",
        metric2Name: "Chi phí / Lead (CPA)",
        metric2Value: "140.524 ₫",
        metric2Diff: "-19.1%",
        metric3Name: "Tỷ lệ chuyển đổi (CVR)",
        metric3Value: "6.82%",
        metric3Diff: "+1.45%",
        metric4Name: "Ngân sách Ads 30 ngày",
        metric4Value: "34.850.000 ₫",
        metric4Diff: "100%",
        campaigns: [
          {
            id: 1,
            name: "GGSearch_DinhCu_EB5_My",
            type: "Search",
            bidding: "Tối đa hóa chuyển đổi",
            status: true,
            dailyBudget: 1200000,
            optScore: 94.2,
            clicks: 1140,
            impressions: 14250,
            cost: 11400000,
            conversions: 84,
            value: 168000000,
          },
          {
            id: 2,
            name: "GGSearch_DinhCu_GoldenVisa_ChauAu",
            type: "Search",
            bidding: "Target CPA: 180k",
            status: true,
            dailyBudget: 800000,
            optScore: 91.5,
            clicks: 820,
            impressions: 11700,
            cost: 7380000,
            conversions: 52,
            value: 104000000,
          },
          {
            id: 3,
            name: "GGSearch_Visa_DuHoc_My_Uc_Canada",
            type: "Search",
            bidding: "Tối đa hóa chuyển đổi",
            status: true,
            dailyBudget: 600000,
            optScore: 88.7,
            clicks: 690,
            impressions: 9850,
            cost: 5865000,
            conversions: 46,
            value: 69000000,
          },
          {
            id: 4,
            name: "GGSearch_Visa_DuLich_ChauAu_Schengen",
            type: "Search",
            bidding: "Target CPA: 110k",
            status: true,
            dailyBudget: 500000,
            optScore: 92.0,
            clicks: 540,
            impressions: 7200,
            cost: 4860000,
            conversions: 38,
            value: 45600000,
          },
          {
            id: 5,
            name: "GGSearch_DinhCu_TayNghe_Canada_Uc",
            type: "Search",
            bidding: "Tối đa hóa chuyển đổi",
            status: true,
            dailyBudget: 400000,
            optScore: 86.4,
            clicks: 310,
            impressions: 4120,
            cost: 3410000,
            conversions: 21,
            value: 25900000,
          },
          {
            id: 6,
            name: "PMax_Visa_TronGoi_ToanQuoc",
            type: "Performance Max",
            bidding: "Target ROAS: 850%",
            status: true,
            dailyBudget: 300000,
            optScore: 95.1,
            clicks: 135,
            impressions: 1800,
            cost: 1935000,
            conversions: 7,
            value: 0,
          },
          {
            id: 7,
            name: "GGSearch_DichVu_Visa_Khan_Cap",
            type: "Search",
            bidding: "Tối đa hóa số nhấp",
            status: false,
            dailyBudget: 250000,
            optScore: 83.2,
            clicks: 0,
            impressions: 0,
            cost: 0,
            conversions: 0,
            value: 0,
          }
        ],
        actions: [
          { name: "Form Đăng Ký Tư Vấn Định Cư & Visa", count: 142, pct: 57.2, cpa: 122000, icon: "file-text" },
          { name: "Cuộc Gọi Trực Tiếp Từ Quảng Cáo & Web", count: 64, pct: 25.8, cpa: 135000, icon: "phone-call" },
          { name: "Tin Nhắn Tư Vấn Zalo OA / Messenger", count: 42, pct: 17.0, cpa: 168000, icon: "message-square" }
        ],
        keywords: [
          { kw: "dịch vụ làm visa úc trọn gói", type: "Exact", conv: 48, cpa: 98400, cvr: 9.8 },
          { kw: "tư vấn định cư eb5 mỹ", type: "Phrase", conv: 39, cpa: 145000, cvr: 8.4 },
          { kw: "làm visa du lịch mỹ đậu 99%", type: "Exact", conv: 34, cpa: 112500, cvr: 7.9 },
          { kw: "golden visa hy lạp bds", type: "Phrase", conv: 28, cpa: 182000, cvr: 6.5 },
          { kw: "visa du học canada sds", type: "Exact", conv: 25, cpa: 105000, cvr: 7.2 },
          { kw: "dịch vụ visa gbluesea", type: "Phrase", conv: 22, cpa: 54000, cvr: 15.2 }
        ],
        locations: [
          { name: "Hồ Chí Minh", pct: 58.2, conv: 144 },
          { name: "Hà Nội", pct: 24.5, conv: 61 },
          { name: "Đà Nẵng & Miền Trung", pct: 7.8, conv: 19 },
          { name: "Cần Thơ & Miền Tây", pct: 5.4, conv: 13 }
        ],
        devices: [
          { label: "Thiết bị di động (Mobile)", pct: 73.4, color: "#1a73e8" },
          { label: "Máy tính để bàn (Desktop)", pct: 23.8, color: "#1e8e3e" },
          { label: "Máy tính bảng (Tablet)", pct: 2.8, color: "#f9ab00" }
        ]
      },

      ecommerce: {
        accountName: "GBlueSea E-Commerce & Retail Store",
        cid: "819-204-5519",
        dateLabel: "01/10/2026 – 31/10/2026 (30 ngày qua)",
        compareLabel: "So với: 01/09/2026 – 30/09/2026",
        pageHeading: "Báo Cáo Chuyển Đổi Đơn Hàng & Doanh Thu Google Ads",
        badgeText: "1.068 Đơn Hàng",
        metric1Name: "Lượt chuyển đổi (Đơn hàng mua)",
        metric1Value: "1.068 Đơn",
        metric1Diff: "+32.5%",
        metric2Name: "Chi phí / Đơn (CPA)",
        metric2Value: "38.876 ₫",
        metric2Diff: "-18.4%",
        metric3Name: "Tỷ suất hoàn vốn (ROAS)",
        metric3Value: "8.92x",
        metric3Diff: "+1.8x",
        metric4Name: "Ngân sách Ads 30 ngày",
        metric4Value: "41.520.000 ₫",
        metric4Diff: "100%",
        campaigns: [
          {
            id: 1,
            name: "PMax_Ban_Hang_Toan_Quoc_Top_SKU",
            type: "Performance Max",
            bidding: "Target ROAS: 750%",
            status: true,
            dailyBudget: 1500000,
            optScore: 96.5,
            clicks: 2840,
            impressions: 42000,
            cost: 16500000,
            conversions: 412,
            value: 148320000,
          },
          {
            id: 2,
            name: "GGShopping_Combo_Khuyen_Mai_Hot",
            type: "Shopping",
            bidding: "Target ROAS: 650%",
            status: true,
            dailyBudget: 1000000,
            optScore: 92.4,
            clicks: 1950,
            impressions: 29000,
            cost: 11700000,
            conversions: 268,
            value: 88440000,
          },
          {
            id: 3,
            name: "GGSearch_SanPham_Chinh_Hang_Gia_Tot",
            type: "Search",
            bidding: "Tối đa hóa chuyển đổi",
            status: true,
            dailyBudget: 800000,
            optScore: 89.1,
            clicks: 1420,
            impressions: 18500,
            cost: 8520000,
            conversions: 184,
            value: 62560000,
          },
          {
            id: 4,
            name: "GGSearch_Thuong_Hieu_Brand_Protection",
            type: "Search",
            bidding: "Tỷ lệ hiển thị mục tiêu",
            status: true,
            dailyBudget: 400000,
            optScore: 98.0,
            clicks: 860,
            impressions: 9200,
            cost: 2580000,
            conversions: 142,
            value: 49700000,
          },
          {
            id: 5,
            name: "GGDisplay_Remarketing_Bam_Duoi_GioHang",
            type: "Display",
            bidding: "Target CPA: 45k",
            status: true,
            dailyBudget: 300000,
            optScore: 88.0,
            clicks: 740,
            impressions: 24000,
            cost: 2220000,
            conversions: 62,
            value: 21700000,
          }
        ],
        actions: [
          { name: "Giao Dịch Mua Hàng Thành Công (Purchase)", count: 780, pct: 73.0, cpa: 42000, icon: "shopping-bag" },
          { name: "Thêm Vào Giỏ Hàng & Điền Checkout", count: 195, pct: 18.3, cpa: 18000, icon: "shopping-cart" },
          { name: "Bấm Nút Nhắn Tin Chốt Đơn Trực Tiếp", count: 93, pct: 8.7, cpa: 35000, icon: "message-circle" }
        ],
        keywords: [
          { kw: "mua sỉ combo sản phẩm chính hãng", type: "Exact", conv: 124, cpa: 38000, cvr: 12.4 },
          { kw: "đặt hàng online freeship toàn quốc", type: "Phrase", conv: 96, cpa: 41500, cvr: 10.2 },
          { kw: "giá tốt sản phẩm cao cấp", type: "Exact", conv: 82, cpa: 44000, cvr: 8.8 }
        ],
        locations: [
          { name: "Hồ Chí Minh", pct: 46.5, conv: 497 },
          { name: "Hà Nội", pct: 32.0, conv: 342 },
          { name: "Đà Nẵng & Bình Dương", pct: 12.5, conv: 134 }
        ],
        devices: [
          { label: "Thiết bị di động (Mobile)", pct: 81.2, color: "#1a73e8" },
          { label: "Máy tính để bàn (Desktop)", pct: 16.5, color: "#1e8e3e" },
          { label: "Máy tính bảng (Tablet)", pct: 2.3, color: "#f9ab00" }
        ]
      }
    };

    // -------------------------------------------------------------
    // APPLICATION STATE (DEFAULT: FEC EXPLORER CASE 04)
    // -------------------------------------------------------------
    let currentMode = 'fec';
    let currentDateRange = '30days';
    let currentGranularity = 'day';
    let selectedMetric1 = 'conversions'; // Blue line
    let selectedMetric2 = 'cpa';         // Orange line
    let currentStatusFilter = 'all';
    let currentSearchQuery = '';
    let sortColumn = 'conversions';
    let sortAsc = false;
    let selectedCampaignIds = [];

    let mainChartInstance = null;
    let deviceChartInstance = null;

    // -------------------------------------------------------------
    // INITIALIZATION ON DOM READY
    // -------------------------------------------------------------
    document.addEventListener("DOMContentLoaded", function() {
      lucide.createIcons();
      initKeyboardShortcuts();
      renderDashboard();
    });

    function initKeyboardShortcuts() {
      document.addEventListener("keydown", function(e) {
        if (e.key === "/" && document.activeElement.tagName !== "INPUT") {
          e.preventDefault();
          const searchInput = document.getElementById("globalSearchInput");
          if (searchInput) searchInput.focus();
        }
      });
    }

    // -------------------------------------------------------------
    // SWITCH DATA MODE
    // -------------------------------------------------------------
    function switchDataMode(mode) {
      currentMode = mode;
      const btnFec = document.getElementById("btnModeFec");
      const btnVisa = document.getElementById("btnModeVisa");
      const btnEcom = document.getElementById("btnModeEcom");
      const banner = document.getElementById("caseStudyBanner");

      btnFec.className = "px-3 py-1 rounded font-medium transition text-google-gray700 hover:text-google-gray900";
      btnVisa.className = "px-3 py-1 rounded font-medium transition text-google-gray700 hover:text-google-gray900";
      btnEcom.className = "px-3 py-1 rounded font-medium transition text-google-gray700 hover:text-google-gray900";

      if (mode === 'fec') {
        btnFec.className = "px-3 py-1 rounded font-medium transition bg-white text-google-blue shadow-sm";
        banner.classList.remove("hidden");
        showToast("Đã tải dữ liệu Case 04: FEC Explorer (180 Phụ Huynh, CPA 93.445 đ).");
      } else if (mode === 'visa') {
        btnVisa.className = "px-3 py-1 rounded font-medium transition bg-white text-google-blue shadow-sm";
        banner.classList.add("hidden");
        showToast("Đã chuyển sang tài khoản Visa GBlueSea.");
      } else {
        btnEcom.className = "px-3 py-1 rounded font-medium transition bg-white text-google-blue shadow-sm";
        banner.classList.add("hidden");
        showToast("Đã chuyển sang tài khoản Bán Hàng E-Commerce.");
      }

      renderDashboard();
    }

    // -------------------------------------------------------------
    // RENDER DASHBOARD (MASTER CONTROLLER)
    // -------------------------------------------------------------
    function renderDashboard() {
      const data = DATASETS[currentMode];

      // 1. Update Headings & Account Info
      document.getElementById("accountNameDisplay").innerText = data.accountName;
      document.getElementById("accountCidDisplay").innerText = "CID: " + data.cid;
      document.getElementById("dateRangeLabel").innerText = data.dateLabel;
      document.getElementById("pageMainHeading").innerHTML = `
        ${data.pageHeading}
        <span id="headingBadge" class="text-xs font-semibold bg-emerald-50 text-emerald-700 border border-emerald-300 px-2.5 py-0.5 rounded-full">
          ${data.badgeText}
        </span>
      `;

      // 2. Compute Filtered Campaigns
      const activeCampaigns = data.campaigns.filter(c => {
        const matchesStatus = currentStatusFilter === 'all' ? true : (currentStatusFilter === 'enabled' ? c.status : !c.status);
        const matchesSearch = c.name.toLowerCase().includes(currentSearchQuery.toLowerCase());
        return matchesStatus && matchesSearch;
      });

      // 3. Render Campaigns Table & Update Totals
      renderCampaignTable(activeCampaigns);

      // 4. Update Metric Scorecards
      updateMetricCards(data);

      // 5. Update Time-Series Chart
      renderMainChart();

      // 6. Update 4 Deep Breakdown Widgets
      renderConversionActionsWidget(data.actions);
      renderDeviceChart();
      renderTopKeywordsWidget(data.keywords);
      renderGeoLocationsWidget(data.locations);

      lucide.createIcons();
    }

    // -------------------------------------------------------------
    // RENDER CAMPAIGN TABLE
    // -------------------------------------------------------------
    function renderCampaignTable(campaigns) {
      const tbody = document.getElementById("campaignTableBody");
      tbody.innerHTML = "";

      // Sort
      const sorted = [...campaigns].sort((a, b) => {
        let valA = a[sortColumn];
        let valB = b[sortColumn];
        if (sortColumn === 'cpa') {
          valA = a.conversions > 0 ? a.cost / a.conversions : 999999999;
          valB = b.conversions > 0 ? b.cost / b.conversions : 999999999;
        } else if (sortColumn === 'cvr') {
          valA = a.clicks > 0 ? (a.conversions / a.clicks) * 100 : 0;
          valB = b.clicks > 0 ? (b.conversions / b.clicks) * 100 : 0;
        } else if (sortColumn === 'ctr') {
          valA = a.impressions > 0 ? (a.clicks / a.impressions) * 100 : 0;
          valB = b.impressions > 0 ? (b.clicks / b.impressions) * 100 : 0;
        } else if (sortColumn === 'avgCpc') {
          valA = a.clicks > 0 ? a.cost / a.clicks : 0;
          valB = b.clicks > 0 ? b.cost / b.clicks : 0;
        } else if (sortColumn === 'roas') {
          valA = a.cost > 0 ? a.value / a.cost : 0;
          valB = b.cost > 0 ? b.value / b.cost : 0;
        }

        if (typeof valA === 'string') {
          return sortAsc ? valA.localeCompare(valB) : valB.localeCompare(valA);
        }
        return sortAsc ? valA - valB : valB - valA;
      });

      // Update Counts
      const totalAll = DATASETS[currentMode].campaigns.length;
      const totalEnabled = DATASETS[currentMode].campaigns.filter(c => c.status).length;
      const totalPaused = totalAll - totalEnabled;
      document.getElementById("countAll").innerText = totalAll;
      document.getElementById("countEnabled").innerText = totalEnabled;
      document.getElementById("countPaused").innerText = totalPaused;
      document.getElementById("activeCampaignBadge").innerText = totalEnabled;

      if (sorted.length === 0) {
        tbody.innerHTML = `
          <tr>
            <td colspan="15" class="py-8 text-center text-google-gray500">
              <i data-lucide="search-x" class="w-8 h-8 mx-auto mb-2 text-google-gray300"></i>
              Không tìm thấy chiến dịch nào phù hợp với bộ lọc.
            </td>
          </tr>
        `;
        return;
      }

      sorted.forEach(c => {
        const isSelected = selectedCampaignIds.includes(c.id);
        const ctr = c.impressions > 0 ? ((c.clicks / c.impressions) * 100).toFixed(2).replace('.', ',') + '%' : '0,00%';
        const avgCpc = c.clicks > 0 ? Math.round(c.cost / c.clicks).toLocaleString('vi-VN') + ' ₫' : '0 ₫';
        const cpa = c.conversions > 0 ? Math.round(c.cost / c.conversions).toLocaleString('vi-VN') + ' ₫' : '--';
        const cvr = c.clicks > 0 ? ((c.conversions / c.clicks) * 100).toFixed(2).replace('.', ',') + '%' : '0,00%';
        const roas = c.cost > 0 ? (c.value / c.cost).toFixed(1) + 'x' : '--';

        const row = document.createElement("tr");
        row.className = `hover:bg-google-gray50 transition ${c.status ? '' : 'opacity-60 bg-gray-50/50'}`;
        row.innerHTML = `
          <td class="py-3 px-3 text-center">
            <input type="checkbox" onchange="toggleSelectRow(${c.id}, this)" ${isSelected ? 'checked' : ''} class="w-3.5 h-3.5 rounded border-google-gray300 text-google-blue">
          </td>
          <td class="py-3 px-3 whitespace-nowrap">
            <div class="flex items-center gap-2">
              <label class="g-switch" title="Bật/Tắt chiến dịch">
                <input type="checkbox" ${c.status ? 'checked' : ''} onchange="toggleCampaignStatus(${c.id})">
                <span class="g-slider"></span>
              </label>
              <span class="text-[11px] font-medium ${c.status ? 'text-google-green' : 'text-google-gray500'}">
                ${c.status ? 'Đang bật' : 'Tạm dừng'}
              </span>
            </div>
          </td>
          <td class="py-3 px-4">
            <div class="flex items-center gap-2">
              <div class="w-6 h-6 rounded bg-emerald-50 text-emerald-700 flex items-center justify-center shrink-0 font-bold text-xs">
                ${c.name.includes('My') ? '🇺🇸' : (c.name.includes('Uc') ? '🇦🇺' : (c.name.includes('Canada') ? '🇨🇦' : (c.name.includes('Anh') ? '🇬🇧' : (c.name.includes('Singapore') ? '🇸🇬' : (c.name.includes('Nhat') ? '🇯🇵' : '🎓')))))}
              </div>
              <div>
                <div class="font-medium text-google-gray900 hover:text-google-blue cursor-pointer truncate max-w-[260px]" title="${c.name}">
                  ${c.name}
                </div>
                <div class="text-[10px] text-google-gray500 flex items-center gap-2">
                  <span>${c.type}</span>
                  <span>•</span>
                  <span class="text-emerald-700 font-medium">${c.bidding}</span>
                </div>
              </div>
            </div>
          </td>
          <td class="py-3 px-3 text-right font-mono">
            ${c.status ? (c.dailyBudget.toLocaleString('vi-VN') + ' ₫') : '--'}
          </td>
          <td class="py-3 px-3 text-right font-mono text-google-blue font-medium">
            ${c.optScore.toFixed(1)}%
          </td>
          <td class="py-3 px-3 text-right font-mono">${c.clicks.toLocaleString('vi-VN')}</td>
          <td class="py-3 px-3 text-right font-mono text-google-gray500">${c.impressions.toLocaleString('vi-VN')}</td>
          <td class="py-3 px-3 text-right font-mono text-emerald-700 font-medium">${ctr}</td>
          <td class="py-3 px-3 text-right font-mono text-google-gray500">${avgCpc}</td>
          <td class="py-3 px-4 text-right font-mono font-bold text-purple-700">${c.cost.toLocaleString('vi-VN')} ₫</td>
          <td class="py-3 px-4 text-right font-mono font-bold text-emerald-700 text-sm">${c.conversions.toLocaleString('vi-VN')}</td>
          <td class="py-3 px-3 text-right font-mono text-google-orange font-bold">${cpa}</td>
          <td class="py-3 px-3 text-right font-mono text-google-blue font-bold">${cvr}</td>
          <td class="py-3 px-4 text-right font-mono">${c.value > 0 ? (c.value.toLocaleString('vi-VN') + ' ₫') : '--'}</td>
          <td class="py-3 px-3 text-right font-mono text-google-green font-semibold">${roas}</td>
        `;
        tbody.appendChild(row);
      });

      updateTableFooter(DATASETS[currentMode].campaigns.filter(c => c.status));
    }

    // -------------------------------------------------------------
    // UPDATE TABLE FOOTER TOTALS
    // -------------------------------------------------------------
    function updateTableFooter(activeCampaigns) {
      const totalClicks = activeCampaigns.reduce((sum, c) => sum + c.clicks, 0);
      const totalImpressions = activeCampaigns.reduce((sum, c) => sum + c.impressions, 0);
      const totalCost = activeCampaigns.reduce((sum, c) => sum + c.cost, 0);
      const totalConversions = activeCampaigns.reduce((sum, c) => sum + c.conversions, 0);
      const totalValue = activeCampaigns.reduce((sum, c) => sum + c.value, 0);
      const totalDailyBudget = activeCampaigns.reduce((sum, c) => sum + c.dailyBudget, 0);

      const avgCtr = totalImpressions > 0 ? ((totalClicks / totalImpressions) * 100).toFixed(2).replace('.', ',') + '%' : '0,00%';
      const avgCpc = totalClicks > 0 ? Math.round(totalCost / totalClicks).toLocaleString('vi-VN') + ' ₫' : '0 ₫';
      const avgCpa = totalConversions > 0 ? Math.round(totalCost / totalConversions).toLocaleString('vi-VN') + ' ₫' : '0 ₫';
      const avgCvr = totalClicks > 0 ? ((totalConversions / totalClicks) * 100).toFixed(2).replace('.', ',') + '%' : '0,00%';
      const avgRoas = totalCost > 0 ? (totalValue / totalCost).toFixed(1) + 'x' : '0,0x';
      const avgOptScore = activeCampaigns.length > 0 ? (activeCampaigns.reduce((sum, c) => sum + c.optScore, 0) / activeCampaigns.length).toFixed(1) + '%' : '0%';

      document.getElementById("footerTotalCampaignsCount").innerText = activeCampaigns.length;
      document.getElementById("footerTotalDailyBudget").innerText = totalDailyBudget.toLocaleString('vi-VN') + ' ₫';
      document.getElementById("footerAvgOptScore").innerText = avgOptScore;
      document.getElementById("footerTotalClicks").innerText = totalClicks.toLocaleString('vi-VN');
      document.getElementById("footerTotalImpressions").innerText = totalImpressions.toLocaleString('vi-VN');
      document.getElementById("footerAvgCtr").innerText = avgCtr;
      document.getElementById("footerAvgCpc").innerText = avgCpc;
      document.getElementById("footerTotalCost").innerText = totalCost.toLocaleString('vi-VN') + ' ₫';
      document.getElementById("footerTotalConversions").innerText = totalConversions.toLocaleString('vi-VN');
      document.getElementById("footerAvgCpa").innerText = avgCpa;
      document.getElementById("footerAvgCvr").innerText = avgCvr;
      document.getElementById("footerTotalValue").innerText = totalValue > 0 ? totalValue.toLocaleString('vi-VN') + ' ₫' : '--';
      document.getElementById("footerAvgRoas").innerText = avgRoas;

      document.getElementById("sidebarCostDisplay").innerText = totalCost.toLocaleString('vi-VN') + ' ₫';
    }

    // -------------------------------------------------------------
    // UPDATE METRIC SCORECARDS (EXACT MATCH FEC CASE)
    // -------------------------------------------------------------
    function updateMetricCards(data) {
      document.getElementById("metricCardLabel1").innerHTML = `${data.metric1Name} <i data-lucide="chevron-down" class="w-3 h-3"></i>`;
      document.getElementById("metricValue1").innerText = data.metric1Value;
      document.getElementById("metricDiff1").innerText = data.metric1Diff;

      document.getElementById("metricCardLabel2").innerHTML = `${data.metric2Name} <i data-lucide="chevron-down" class="w-3 h-3"></i>`;
      document.getElementById("metricValue2").innerText = data.metric2Value;
      document.getElementById("metricDiff2").innerText = data.metric2Diff;

      document.getElementById("metricCardLabel3").innerHTML = `${data.metric3Name} <i data-lucide="chevron-down" class="w-3 h-3"></i>`;
      document.getElementById("metricValue3").innerText = data.metric3Value;
      document.getElementById("metricDiff3").innerText = data.metric3Diff;

      document.getElementById("metricCardLabel4").innerHTML = `${data.metric4Name} <i data-lucide="chevron-down" class="w-3 h-3"></i>`;
      document.getElementById("metricValue4").innerText = data.metric4Value;
      document.getElementById("metricDiff4").innerText = data.metric4Diff;
    }

    // -------------------------------------------------------------
    // SELECT METRIC FOR MAIN TIME-SERIES CHART
    // -------------------------------------------------------------
    function selectMetricForChart(slot, metricKey) {
      if (slot === 1) {
        selectedMetric1 = metricKey;
      } else {
        selectedMetric2 = metricKey;
      }

      const cards = [
        { id: "metricCard1", metric: 'conversions' },
        { id: "metricCard2", metric: 'cpa' },
        { id: "metricCard3", metric: 'cvr' },
        { id: "metricCard4", metric: 'cost' }
      ];

      cards.forEach(c => {
        const el = document.getElementById(c.id);
        el.className = "metric-card bg-white rounded-xl p-4 border border-google-gray300 transition-all cursor-pointer relative hover:shadow-md";
        if (selectedMetric1 === c.metric) {
          el.classList.add("metric-card-active-blue");
        } else if (selectedMetric2 === c.metric) {
          el.classList.add("metric-card-active-orange");
        }
      });

      renderMainChart();
    }

    // -------------------------------------------------------------
    // RENDER MAIN TIME-SERIES CHART (CHART.JS)
    // -------------------------------------------------------------
    function renderMainChart() {
      const ctx = document.getElementById("googleAdsChart").getContext("2d");
      const data = DATASETS[currentMode];
      
      const labels = [];
      const lineData1 = [];
      const lineData2 = [];

      // Build 30-day timeline (18/07 -> 16/08)
      const daysCount = 30;
      for (let i = 1; i <= daysCount; i++) {
        const dayOfMonth = (17 + i) <= 31 ? `${17 + i}/07` : `${(17 + i) - 31}/08`;
        labels.push(dayOfMonth);

        let conv = 6;
        let cost = 560666;
        if (data.dailyConversions && data.dailyConversions[i - 1] !== undefined) {
          conv = data.dailyConversions[i - 1];
          cost = data.dailyCosts[i - 1];
        }

        const cpa = conv > 0 ? Math.round(cost / conv) : 0;
        const cvr = Number(((conv / (cost / 12101)) * 100).toFixed(2));

        // Metric 1 mapping
        if (selectedMetric1 === 'conversions') lineData1.push(conv);
        else if (selectedMetric1 === 'cost') lineData1.push(cost);
        else if (selectedMetric1 === 'cpa') lineData1.push(cpa);
        else lineData1.push(cvr);

        // Metric 2 mapping
        if (selectedMetric2 === 'cpa') lineData2.push(cpa);
        else if (selectedMetric2 === 'cost') lineData2.push(cost);
        else if (selectedMetric2 === 'conversions') lineData2.push(conv);
        else lineData2.push(cvr);
      }

      const metricLabels = {
        conversions: 'Lượt phụ huynh đăng ký',
        cost: 'Chi phí (₫)',
        cpa: 'Chi phí / Lead CPA (₫)',
        cvr: 'Tỷ lệ chuyển đổi CVR (%)'
      };
      document.getElementById("chartTitlePrimary").innerText = metricLabels[selectedMetric1];
      document.getElementById("chartTitleSecondary").innerText = metricLabels[selectedMetric2];

      if (mainChartInstance) {
        mainChartInstance.destroy();
      }

      mainChartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [
            {
              label: metricLabels[selectedMetric1],
              data: lineData1,
              borderColor: '#1a73e8',
              backgroundColor: 'rgba(26, 115, 232, 0.08)',
              borderWidth: 2.5,
              tension: 0.35,
              fill: true,
              yAxisID: 'y1',
              pointRadius: 3,
              pointHoverRadius: 6,
              pointBackgroundColor: '#1a73e8',
            },
            {
              label: metricLabels[selectedMetric2],
              data: lineData2,
              borderColor: '#e37400',
              backgroundColor: 'transparent',
              borderWidth: 2,
              borderDash: [4, 4],
              tension: 0.35,
              fill: false,
              yAxisID: 'y2',
              pointRadius: 3,
              pointHoverRadius: 6,
              pointBackgroundColor: '#e37400',
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          interaction: {
            mode: 'index',
            intersect: false,
          },
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: '#202124',
              titleFont: { family: 'Google Sans', size: 12, weight: 'bold' },
              bodyFont: { family: 'Roboto Mono', size: 12 },
              padding: 10,
              cornerRadius: 8,
              callbacks: {
                label: function(context) {
                  let label = context.dataset.label || '';
                  if (label) label += ': ';
                  if (context.parsed.y !== null) {
                    if (label.includes('CPA') || label.includes('Chi phí')) {
                      label += context.parsed.y.toLocaleString('vi-VN') + ' ₫';
                    } else if (label.includes('%')) {
                      label += context.parsed.y.toFixed(2).replace('.', ',') + '%';
                    } else {
                      label += context.parsed.y.toLocaleString('vi-VN') + ' Phụ Huynh';
                    }
                  }
                  return label;
                }
              }
            }
          },
          scales: {
            x: {
              grid: { display: false },
              ticks: { font: { family: 'Google Sans', size: 11 }, color: '#5f6368' }
            },
            y1: {
              type: 'linear',
              display: true,
              position: 'left',
              grid: { color: '#f1f3f4' },
              ticks: {
                font: { family: 'Roboto Mono', size: 11 },
                color: '#1a73e8',
                callback: function(val) {
                  if (selectedMetric1 === 'cost' || selectedMetric1 === 'cpa') {
                    return val >= 1000000 ? (val / 1000000).toFixed(1) + 'M' : (val / 1000).toFixed(0) + 'k';
                  }
                  return val.toLocaleString('vi-VN');
                }
              }
            },
            y2: {
              type: 'linear',
              display: true,
              position: 'right',
              grid: { drawOnChartArea: false },
              ticks: {
                font: { family: 'Roboto Mono', size: 11 },
                color: '#e37400',
                callback: function(val) {
                  if (selectedMetric2 === 'cost' || selectedMetric2 === 'cpa') {
                    return val >= 1000000 ? (val / 1000000).toFixed(1) + 'M' : (val / 1000).toFixed(0) + 'k';
                  }
                  return val.toLocaleString('vi-VN');
                }
              }
            }
          }
        }
      });
    }

    // -------------------------------------------------------------
    // RENDER DEVICE BREAKDOWN (DONUT CHART)
    // -------------------------------------------------------------
    function renderDeviceChart() {
      const ctx = document.getElementById("deviceChart").getContext("2d");
      const legendContainer = document.getElementById("deviceLegendContainer");
      const data = DATASETS[currentMode];

      const deviceData = data.devices || [
        { label: "Thiết bị di động (Mobile)", pct: 78.5, color: "#1a73e8" },
        { label: "Máy tính để bàn (Desktop)", pct: 19.5, color: "#1e8e3e" },
        { label: "Máy tính bảng (Tablet)", pct: 2.0, color: "#f9ab00" }
      ];

      if (deviceChartInstance) {
        deviceChartInstance.destroy();
      }

      deviceChartInstance = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: deviceData.map(d => d.label),
          datasets: [{
            data: deviceData.map(d => d.pct),
            backgroundColor: deviceData.map(d => d.color),
            borderWidth: 2,
            borderColor: '#ffffff',
            hoverOffset: 4
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          cutout: '70%',
          plugins: {
            legend: { display: false },
            tooltip: {
              callbacks: {
                label: function(ctx) {
                  return ` ${ctx.label}: ${ctx.parsed}%`;
                }
              }
            }
          }
        }
      });

      legendContainer.innerHTML = deviceData.map(d => `
        <div class="flex items-center justify-between py-1 text-[11px]">
          <div class="flex items-center gap-1.5">
            <span class="w-2.5 h-2.5 rounded-full" style="background-color: ${d.color}"></span>
            <span class="text-google-gray700">${d.label.split('(')[0]}</span>
          </div>
          <span class="font-bold font-mono text-google-gray900">${d.pct}%</span>
        </div>
      `).join('');
    }

    // -------------------------------------------------------------
    // RENDER CONVERSION ACTIONS WIDGET
    // -------------------------------------------------------------
    function renderConversionActionsWidget(actions) {
      const container = document.getElementById("conversionActionsContainer");
      container.innerHTML = actions.map(a => `
        <div>
          <div class="flex items-center justify-between text-xs mb-1">
            <span class="text-google-gray700 font-medium truncate max-w-[180px]" title="${a.name}">${a.name}</span>
            <span class="font-bold font-mono text-emerald-700">${a.count} (${a.pct}%)</span>
          </div>
          <div class="w-full bg-google-gray200 rounded-full h-1.5 overflow-hidden">
            <div class="bg-emerald-600 h-1.5 rounded-full" style="width: ${a.pct}%"></div>
          </div>
          <div class="text-[10px] text-google-gray500 mt-0.5 flex justify-between">
            <span>CPA trung bình</span>
            <span class="font-mono">${a.cpa.toLocaleString('vi-VN')} ₫</span>
          </div>
        </div>
      `).join('');
    }

    // -------------------------------------------------------------
    // RENDER TOP KEYWORDS WIDGET
    // -------------------------------------------------------------
    function renderTopKeywordsWidget(keywords) {
      const container = document.getElementById("topKeywordsContainer");
      container.innerHTML = keywords.map(k => `
        <div class="py-1 border-b border-google-gray100 last:border-0">
          <div class="flex items-center justify-between">
            <span class="font-medium text-google-gray900 truncate max-w-[170px]" title="${k.kw}">
              ${k.type === 'Exact' ? `[${k.kw}]` : `"${k.kw}"`}
            </span>
            <span class="font-bold text-emerald-700 font-mono">${k.conv}</span>
          </div>
          <div class="flex items-center justify-between text-[10px] text-google-gray500">
            <span>CPA: ${k.cpa.toLocaleString('vi-VN')} ₫</span>
            <span>CVR: ${k.cvr}%</span>
          </div>
        </div>
      `).join('');
    }

    // -------------------------------------------------------------
    // RENDER GEO LOCATIONS WIDGET
    // -------------------------------------------------------------
    function renderGeoLocationsWidget(locations) {
      const container = document.getElementById("geoLocationsContainer");
      container.innerHTML = locations.map(l => `
        <div>
          <div class="flex items-center justify-between mb-1">
            <span class="text-google-gray700">${l.name}</span>
            <span class="font-bold font-mono text-google-gray900">${l.pct}% (${l.conv})</span>
          </div>
          <div class="w-full bg-google-gray200 rounded-full h-1.5 overflow-hidden">
            <div class="bg-google-blue h-1.5 rounded-full" style="width: ${l.pct}%"></div>
          </div>
        </div>
      `).join('');
    }

    // -------------------------------------------------------------
    // INTERACTIVE ACTIONS
    // -------------------------------------------------------------
    function toggleCampaignStatus(id) {
      const campaign = DATASETS[currentMode].campaigns.find(c => c.id === id);
      if (campaign) {
        campaign.status = !campaign.status;
        showToast(`Đã ${campaign.status ? 'bật' : 'tạm dừng'} chiến dịch "${campaign.name}".`);
        renderDashboard();
      }
    }

    function filterByStatus(status) {
      currentStatusFilter = status;
      const btnAll = document.getElementById("btnFilterAll");
      const btnEnabled = document.getElementById("btnFilterEnabled");
      const btnPaused = document.getElementById("btnFilterPaused");

      btnAll.className = "px-2.5 py-1 rounded font-medium text-google-gray700 hover:text-google-gray900";
      btnEnabled.className = "px-2.5 py-1 rounded font-medium text-google-gray700 hover:text-google-gray900";
      btnPaused.className = "px-2.5 py-1 rounded font-medium text-google-gray700 hover:text-google-gray900";

      if (status === 'all') btnAll.className = "px-2.5 py-1 rounded font-medium bg-white text-google-gray900 shadow-sm";
      if (status === 'enabled') btnEnabled.className = "px-2.5 py-1 rounded font-medium bg-white text-google-gray900 shadow-sm";
      if (status === 'paused') btnPaused.className = "px-2.5 py-1 rounded font-medium bg-white text-google-gray900 shadow-sm";

      const filtered = DATASETS[currentMode].campaigns.filter(c => {
        const matchesStatus = currentStatusFilter === 'all' ? true : (currentStatusFilter === 'enabled' ? c.status : !c.status);
        const matchesSearch = c.name.toLowerCase().includes(currentSearchQuery.toLowerCase());
        return matchesStatus && matchesSearch;
      });
      renderCampaignTable(filtered);
    }

    function filterCampaignTable() {
      const input = document.getElementById("campaignTableSearch");
      currentSearchQuery = input.value;
      const filtered = DATASETS[currentMode].campaigns.filter(c => {
        const matchesStatus = currentStatusFilter === 'all' ? true : (currentStatusFilter === 'enabled' ? c.status : !c.status);
        const matchesSearch = c.name.toLowerCase().includes(currentSearchQuery.toLowerCase());
        return matchesStatus && matchesSearch;
      });
      renderCampaignTable(filtered);
    }

    function sortTable(column) {
      if (sortColumn === column) {
        sortAsc = !sortAsc;
      } else {
        sortColumn = column;
        sortAsc = false;
      }

      const cols = ['status', 'name', 'budget', 'optScore', 'clicks', 'impressions', 'ctr', 'avgCpc', 'cost', 'conversions', 'cpa', 'cvr', 'convValue', 'roas'];
      cols.forEach(c => {
        const el = document.getElementById(`sort_${c}`);
        if (el) el.innerText = '↕';
      });

      const currentIndicator = document.getElementById(`sort_${column}`);
      if (currentIndicator) currentIndicator.innerText = sortAsc ? '▲' : '▼';

      const filtered = DATASETS[currentMode].campaigns.filter(c => {
        const matchesStatus = currentStatusFilter === 'all' ? true : (currentStatusFilter === 'enabled' ? c.status : !c.status);
        const matchesSearch = c.name.toLowerCase().includes(currentSearchQuery.toLowerCase());
        return matchesStatus && matchesSearch;
      });
      renderCampaignTable(filtered);
    }

    function toggleDatePickerPopover() {
      const popover = document.getElementById("datePickerPopover");
      popover.classList.toggle("hidden");
    }

    function setDateRange(preset) {
      currentDateRange = preset;
      toggleDatePickerPopover();
      showToast(`Áp dụng khoảng thời gian: 30 ngày qua (18/07/2026 – 16/08/2026)`);
      renderDashboard();
    }

    function toggleSelectAllRows(masterCheckbox) {
      const isChecked = masterCheckbox.checked;
      const data = DATASETS[currentMode];
      selectedCampaignIds = isChecked ? data.campaigns.map(c => c.id) : [];
      updateBulkActionBar();
      renderCampaignTable(data.campaigns);
    }

    function toggleSelectRow(id, checkbox) {
      if (checkbox.checked) {
        selectedCampaignIds.push(id);
      } else {
        selectedCampaignIds = selectedCampaignIds.filter(i => i !== id);
      }
      updateBulkActionBar();
    }

    function updateBulkActionBar() {
      const bar = document.getElementById("bulkActionBar");
      const countLabel = document.getElementById("bulkSelectedCount");
      if (selectedCampaignIds.length > 0) {
        bar.classList.remove("hidden");
        countLabel.innerText = `Đã chọn ${selectedCampaignIds.length} chiến dịch`;
      } else {
        bar.classList.add("hidden");
      }
    }

    function clearBulkSelection() {
      selectedCampaignIds = [];
      document.getElementById("masterCheckbox").checked = false;
      updateBulkActionBar();
      renderCampaignTable(DATASETS[currentMode].campaigns);
    }

    function bulkToggleStatus(enable) {
      DATASETS[currentMode].campaigns.forEach(c => {
        if (selectedCampaignIds.includes(c.id)) {
          c.status = enable;
        }
      });
      showToast(`Đã ${enable ? 'bật' : 'tạm dừng'} ${selectedCampaignIds.length} chiến dịch.`);
      clearBulkSelection();
      renderDashboard();
    }

    // -------------------------------------------------------------
    // EXPORT TO EXCEL (.XLSX)
    // -------------------------------------------------------------
    function exportToExcel() {
      const data = DATASETS[currentMode];
      const wb = XLSX.utils.book_new();

      const campaignRows = data.campaigns.map(c => ({
        "Tên Chiến Dịch (Quốc Gia)": c.name,
        "Loại Hình": c.type,
        "Trạng Thái": c.status ? "Đang bật" : "Tạm dừng",
        "Chiến Lược Đấu Thầu": c.bidding,
        "Ngân Sách Ngày (₫)": c.dailyBudget,
        "Điểm Tối Ưu (%)": c.optScore,
        "Lượt Nhấp": c.clicks,
        "Lượt Hiển Thị": c.impressions,
        "CTR (%)": c.impressions > 0 ? Number(((c.clicks / c.impressions) * 100).toFixed(2)) : 0,
        "CPC TB (₫)": c.clicks > 0 ? Math.round(c.cost / c.clicks) : 0,
        "Chi Phí 30 Ngày (₫)": c.cost,
        "Phụ Huynh Đăng Ký (Leads)": c.conversions,
        "CPA (₫)": c.conversions > 0 ? Math.round(c.cost / c.conversions) : 0,
        "CVR (%)": c.clicks > 0 ? Number(((c.conversions / c.clicks) * 100).toFixed(2)) : 0,
        "Doanh Thu Dự Kiến (₫)": c.value,
        "ROAS": c.cost > 0 ? Number((c.value / c.cost).toFixed(1)) : 0
      }));

      const ws1 = XLSX.utils.json_to_sheet(campaignRows);
      XLSX.utils.book_append_sheet(wb, ws1, "Bao_Cao_Chien_Dich");

      const ws2 = XLSX.utils.json_to_sheet(data.actions.map(a => ({
        "Hành Động Chuyển Đổi": a.name,
        "Số Lượng Phụ Huynh": a.count,
        "Tỷ Trọng (%)": a.pct,
        "CPA Trung Bình (₫)": a.cpa
      })));
      XLSX.utils.book_append_sheet(wb, ws2, "Hanh_Dong_Chuyen_Doi");

      const ws3 = XLSX.utils.json_to_sheet(data.keywords.map(k => ({
        "Từ Khóa Sinh Lời": k.kw,
        "Loại Đối Sánh": k.type,
        "Lượt Đăng Ký": k.conv,
        "CPA (₫)": k.cpa,
        "CVR (%)": k.cvr
      })));
      XLSX.utils.book_append_sheet(wb, ws3, "Top_Tu_Khoa");

      const fileName = `Bao_Cao_Google_Ads_${currentMode === 'fec' ? 'FEC_Explorer' : currentMode}.xlsx`;
      XLSX.writeFile(wb, fileName);

      showToast(`Đã xuất thành công file Excel chuẩn: ${fileName}`);
    }

    // -------------------------------------------------------------
    // UI HELPERS
    // -------------------------------------------------------------
    function showToast(message) {
      const toast = document.getElementById("toastNotification");
      const msg = document.getElementById("toastMessage");
      msg.innerText = message;
      toast.classList.remove("hidden");
      toast.classList.add("flex");
      setTimeout(() => hideToast(), 3500);
    }

    function hideToast() {
      const toast = document.getElementById("toastNotification");
      toast.classList.add("hidden");
      toast.classList.remove("flex");
    }

    function refreshDataWithAnimation() {
      const icon = document.getElementById("refreshIcon");
      icon.classList.add("animate-spin");
      setTimeout(() => {
        icon.classList.remove("animate-spin");
        renderDashboard();
        showToast("Dữ liệu Google Ads đã được đồng bộ chuẩn Case 04.");
      }, 600);
    }

    function setActiveNav(element, section) {
      document.querySelectorAll(".nav-link").forEach(link => link.classList.remove("nav-item-active"));
      element.classList.add("nav-item-active");
      showToast(`Chuyển mục xem: ${element.innerText.trim()}`);
    }

    function scrollToKeywords() {
      const section = document.getElementById("campaignsSection");
      if (section) section.scrollIntoView({ behavior: 'smooth' });
    }

    function showNewCampaignModal() {
      showToast("Chức năng tạo chiến dịch mới: Cần quyền Quản trị viên (Admin CID).");
    }

    const btnToggleSidebar = document.getElementById("btnToggleSidebar");
    const mainSidebar = document.getElementById("mainSidebar");
    let sidebarExpanded = true;

    btnToggleSidebar.addEventListener("click", () => {
      sidebarExpanded = !sidebarExpanded;
      if (!sidebarExpanded) {
        mainSidebar.classList.remove("w-60");
        mainSidebar.classList.add("w-16");
        document.querySelectorAll(".sidebar-text").forEach(el => el.classList.add("hidden"));
      } else {
        mainSidebar.classList.remove("w-16");
        mainSidebar.classList.add("w-60");
        document.querySelectorAll(".sidebar-text").forEach(el => el.classList.remove("hidden"));
      }
    });
  </script>
</body>
</html>
'''

output_path = "Google_Ads_Dashboard_Chuyen_Doi.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Updated {output_path} successfully. Size: {len(html_content)} bytes.")
