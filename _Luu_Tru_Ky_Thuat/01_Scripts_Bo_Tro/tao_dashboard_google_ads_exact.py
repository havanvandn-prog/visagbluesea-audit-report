import os

html_content = '''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chiến dịch — Google Ads</title>
  
  <!-- Google Fonts: Google Sans & Roboto -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&family=Roboto:wght@400;500;700&family=Roboto+Mono:wght@400;500&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  
  <!-- SheetJS CDN -->
  <script src="https://cdn.sheetjs.com/xlsx-0.20.1/package/dist/xlsx.full.min.js"></script>

  <style>
    * {
      box-sizing: border-box;
    }
    body {
      background-color: #ffffff;
      color: #202124;
      font-family: 'Google Sans', 'Roboto', system-ui, -apple-system, sans-serif;
      margin: 0;
      padding: 0;
      overflow-x: hidden;
      font-size: 13px;
      -webkit-font-smoothing: antialiased;
    }

    /* Google Ads Specific Palette */
    :root {
      --google-blue: #1a73e8;
      --google-blue-hover: #1557b0;
      --google-blue-light: #e8f0fe;
      --google-gray-border: #dadce0;
      --google-gray-bg: #f8f9fa;
      --google-gray-text: #5f6368;
      --google-dark-text: #202124;
      --google-red: #d93025;
      --google-green: #1e8e3e;
      --google-green-bg: #e6f4ea;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
      width: 7px;
      height: 7px;
    }
    ::-webkit-scrollbar-track {
      background: #f1f3f4;
    }
    ::-webkit-scrollbar-thumb {
      background: #c1c3c7;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #9aa0a6;
    }

    /* Tier 1 Rail Navigation Styles */
    .tier1-btn {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 52px;
      padding: 8px 2px;
      border-radius: 16px;
      cursor: pointer;
      color: #5f6368;
      text-decoration: none;
      transition: background 0.15s, color 0.15s;
      margin-bottom: 6px;
    }
    .tier1-btn:hover {
      background-color: #f1f3f4;
      color: #202124;
    }
    .tier1-btn.active {
      background-color: #1a73e8;
      color: #ffffff !important;
    }
    .tier1-btn.active svg {
      color: #ffffff !important;
      stroke: #ffffff !important;
    }
    .tier1-btn span {
      font-size: 10px;
      margin-top: 4px;
      line-height: 1.1;
      text-align: center;
      font-weight: 500;
    }

    /* Tier 2 Sidebar Navigation */
    .tier2-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 7px 16px;
      font-size: 12.5px;
      color: #3c4043;
      cursor: pointer;
      border-radius: 0 16px 16px 0;
      margin-right: 8px;
      transition: background 0.15s;
    }
    .tier2-item:hover {
      background-color: #f8f9fa;
      color: #202124;
    }
    .tier2-item.active {
      background-color: #1a73e8;
      color: #ffffff;
      font-weight: 500;
    }
    .tier2-subitem {
      display: block;
      padding: 6px 16px 6px 32px;
      font-size: 12.5px;
      color: #3c4043;
      cursor: pointer;
      border-radius: 0 16px 16px 0;
      margin-right: 8px;
      transition: background 0.15s;
    }
    .tier2-subitem:hover {
      background-color: #f8f9fa;
      color: #202124;
    }
    .tier2-subitem.active {
      background-color: #1a73e8;
      color: #ffffff;
      font-weight: 500;
    }

    /* Tabs Bar */
    .g-tab {
      padding: 10px 16px;
      font-size: 13px;
      color: #5f6368;
      font-weight: 500;
      border-bottom: 3px solid transparent;
      cursor: pointer;
      transition: color 0.15s, border-color 0.15s;
    }
    .g-tab:hover {
      color: #202124;
    }
    .g-tab.active {
      color: #1a73e8;
      border-bottom-color: #1a73e8;
    }

    /* Table Styles */
    .g-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
    }
    .g-table th {
      background-color: #ffffff;
      color: #5f6368;
      font-weight: 500;
      padding: 8px 10px;
      border-top: 1px solid #dadce0;
      border-bottom: 1px solid #dadce0;
      text-align: right;
      white-space: nowrap;
      user-select: none;
    }
    .g-table th.th-left {
      text-align: left;
    }
    .g-table td {
      padding: 8px 10px;
      border-bottom: 1px solid #ebebeb;
      text-align: right;
      white-space: nowrap;
      color: #3c4043;
    }
    .g-table td.td-left {
      text-align: left;
    }
    .g-table tr:hover td {
      background-color: #f8f9fa;
    }

    /* Checkbox Google style */
    .g-checkbox {
      width: 15px;
      height: 15px;
      border: 1.5px solid #5f6368;
      border-radius: 2px;
      cursor: pointer;
      accent-color: #1a73e8;
    }

    /* Chart Scrubber Bar */
    .chart-scrubber-bar {
      height: 18px;
      background: linear-gradient(90deg, #9bb8fd 0%, #b8ccfd 100%);
      border-radius: 9px;
      margin: 12px 0 6px 0;
    }
  </style>
</head>
<body class="flex h-screen w-screen overflow-hidden bg-white select-none">

  <!-- ============================================================== -->
  <!-- 1. TIER 1 SLIM LEFT RAIL (60px)                                -->
  <!-- ============================================================== -->
  <aside class="w-[60px] bg-white border-r border-[#dadce0] flex flex-col items-center py-2.5 justify-between shrink-0 z-30">
    <div class="flex flex-col items-center w-full">
      
      <!-- Google Ads Geometric Logo -->
      <div class="mb-3 cursor-pointer" onclick="location.reload()" title="Google Ads">
        <svg class="w-8 h-8" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M43.6 20.3L28.1 4.8C26.5 3.2 23.9 3.2 22.3 4.8L6.8 20.3C5.2 21.9 5.2 24.5 6.8 26.1L22.3 41.6C23.9 43.2 26.5 43.2 28.1 41.6L43.6 26.1C45.2 24.5 45.2 21.9 43.6 20.3Z" fill="#FBBC04"/>
          <path d="M12.4 34.4C10.8 32.8 10.8 30.2 12.4 28.6L27.9 13.1C29.5 11.5 32.1 11.5 33.7 13.1C35.3 14.7 35.3 17.3 33.7 18.9L18.2 34.4C16.6 36 14 36 12.4 34.4Z" fill="#4285F4"/>
          <circle cx="15.3" cy="31.5" r="3.5" fill="#34A853"/>
        </svg>
      </div>

      <!-- '+ Tạo' Pill Button (Google Floating style) -->
      <button onclick="showActionToast('Mở trình tạo Chiến dịch mới')" class="flex flex-col items-center justify-center w-11 h-11 bg-white hover:shadow-md border border-[#dadce0] rounded-2xl mb-3 transition shadow-sm" title="Tạo mới">
        <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none">
          <path d="M12 5V19M5 12H19" stroke="#1a73e8" stroke-width="2.5" stroke-linecap="round"/>
        </svg>
        <span class="text-[9px] text-[#5f6368] font-medium -mt-0.5">Tạo</span>
      </button>

      <!-- Navigation Icons List -->
      <nav class="flex flex-col items-center w-full">
        <!-- 1. Chiến dịch (ACTIVE) -->
        <a href="#campaigns" class="tier1-btn active" title="Chiến dịch">
          <svg class="w-5 h-5 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M3 11l19-9-9 19-2-8-8-2z"/>
          </svg>
          <span>Chiến dịch</span>
        </a>

        <!-- 2. Mục tiêu -->
        <a href="#goals" onclick="showActionToast('Mục tiêu')" class="tier1-btn" title="Mục tiêu">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"/>
            <circle cx="12" cy="12" r="6"/>
            <circle cx="12" cy="12" r="2"/>
          </svg>
          <span>Mục tiêu</span>
        </a>

        <!-- 3. Công cụ -->
        <a href="#tools" onclick="showActionToast('Công cụ')" class="tier1-btn" title="Công cụ">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
          </svg>
          <span>Công cụ</span>
        </a>

        <!-- 4. Thanh toán -->
        <a href="#billing" onclick="showActionToast('Thanh toán')" class="tier1-btn" title="Thanh toán">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="5" width="20" height="14" rx="2"/>
            <line x1="2" y1="10" x2="22" y2="10"/>
          </svg>
          <span>Thanh toán</span>
        </a>

        <!-- 5. Quản trị -->
        <a href="#admin" onclick="showActionToast('Quản trị')" class="tier1-btn" title="Quản trị">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="3"/>
            <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/>
          </svg>
          <span>Quản trị</span>
        </a>
      </nav>
    </div>

    <!-- Bottom: '< Thu gọn' button -->
    <button id="btnCollapseTier2" class="flex flex-col items-center justify-center p-1 text-[#5f6368] hover:text-[#202124] transition w-full" title="Thu gọn/Mở rộng">
      <svg id="collapseIcon" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polyline points="15 18 9 12 15 6"></polyline>
      </svg>
      <span class="text-[9px] mt-0.5">Thu gọn</span>
    </button>
  </aside>

  <!-- ============================================================== -->
  <!-- 2. TIER 2 SIDEBAR NAVIGATION (210px)                           -->
  <!-- ============================================================== -->
  <aside id="tier2Sidebar" class="w-[210px] bg-white border-r border-[#dadce0] flex flex-col py-3 overflow-y-auto shrink-0 select-none transition-all duration-200">
    <div class="space-y-0.5">
      <div class="tier2-item" onclick="showActionToast('Tổng quan')">
        <span>Tổng quan</span>
      </div>

      <div class="tier2-item" onclick="showActionToast('Đề xuất')">
        <span>Đề xuất</span>
      </div>

      <div class="tier2-item" onclick="showActionToast('Thông tin chi tiết và báo cáo')">
        <span>Thông tin chi tiết và báo cáo</span>
        <svg class="w-3.5 h-3.5 text-[#5f6368]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
      </div>

      <!-- Chiến dịch (Tree Group) -->
      <div>
        <div class="tier2-item flex items-center justify-between font-medium text-[#202124]">
          <span class="text-blue-700">Chiến dịch</span>
          <svg class="w-3.5 h-3.5 text-[#5f6368]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="18 15 12 9 6 15"/></svg>
        </div>
        <div class="mt-0.5">
          <a class="tier2-subitem active">Chiến dịch</a>
          <a class="tier2-subitem" onclick="showActionToast('Nhóm quảng cáo')">Nhóm quảng cáo</a>
          <a class="tier2-subitem" onclick="showActionToast('Quảng cáo')">Quảng cáo</a>
          <a class="tier2-subitem" onclick="showActionToast('Thử nghiệm')">Thử nghiệm</a>
          <a class="tier2-subitem" onclick="showActionToast('Nhóm chiến dịch')">Nhóm chiến dịch</a>
        </div>
      </div>

      <div class="tier2-item" onclick="showActionToast('Thành phần')">
        <span>Thành phần</span>
        <svg class="w-3.5 h-3.5 text-[#5f6368]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
      </div>

      <div class="tier2-item" onclick="showActionToast('Đối tượng, từ khoá và nội dung')">
        <span>Đối tượng, từ khoá và nội dung</span>
        <svg class="w-3.5 h-3.5 text-[#5f6368]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
      </div>

      <div class="tier2-item" onclick="showActionToast('Nhật ký thay đổi')">
        <span>Nhật ký thay đổi</span>
      </div>
    </div>
  </aside>

  <!-- ============================================================== -->
  <!-- 3. MAIN CONTENT WORKSPACE (HEADER + CHART + TABLE)             -->
  <!-- ============================================================== -->
  <main class="flex-1 flex flex-col h-screen overflow-y-auto bg-white">

    <!-- 3.1 TOP BAR HEADER (Search, Account Pill, Alerts, Tools) -->
    <header class="h-[54px] border-b border-[#dadce0] px-4 flex items-center justify-between shrink-0 bg-white">
      
      <!-- Left: Blue Account Pill -->
      <div class="flex items-center gap-2">
        <button id="btnAccountSwitcher" onclick="toggleAccountMenu()" class="flex items-center gap-2 bg-[#1a73e8] hover:bg-[#1557b0] text-white px-3 py-1.5 rounded text-xs font-medium shadow-sm transition">
          <div class="text-left">
            <div id="accNameDisplay" class="font-semibold text-xs leading-none flex items-center gap-1">
              <span>Tất cả chiến dịch</span>
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
            </div>
            <div id="accSubDisplay" class="text-[10px] text-blue-100 font-normal mt-0.5">2 bộ lọc • 1 chiến dịch</div>
          </div>
        </button>
      </div>

      <!-- Center: Warning Alerts (Exactly as in User Screenshot!) -->
      <div class="hidden xl:flex items-center gap-4 text-xs">
        <!-- Alert 1 -->
        <div class="flex items-center gap-1.5 text-[#d93025]">
          <svg class="w-4 h-4 shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          <span>Số dư sắp hết</span>
          <a href="#" class="text-[#1a73e8] hover:underline font-medium">Khắc phục vấn đề</a>
        </div>

        <!-- Alert 2 -->
        <div class="flex items-center gap-1.5 text-[#202124]">
          <svg class="w-4 h-4 text-[#d93025] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          <span>Bảo vệ tài khoản của bạn khỏi hoạt động trái phép</span>
          <a href="#" class="text-[#1a73e8] hover:underline font-medium">Xem</a>
          <button class="text-[#5f6368] hover:text-[#202124] ml-1">✕</button>
        </div>
      </div>

      <!-- Right: Action Icons (Search, View, Refresh, Help, Notifications, Avatar) -->
      <div class="flex items-center gap-4 text-[#5f6368]">
        <!-- Tìm kiếm -->
        <button onclick="showActionToast('Tìm kiếm')" class="flex flex-col items-center hover:text-[#202124]">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <span class="text-[9px] mt-0.5">Tìm kiếm</span>
        </button>

        <!-- Giao diện -->
        <button onclick="showActionToast('Giao diện')" class="flex flex-col items-center hover:text-[#202124]">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="9" y1="3" x2="9" y2="21"/></svg>
          <span class="text-[9px] mt-0.5">Giao diện</span>
        </button>

        <!-- Làm mới -->
        <button onclick="refreshData()" class="flex flex-col items-center hover:text-[#202124]">
          <svg id="refreshIcon" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"/><path d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"/></svg>
          <span class="text-[9px] mt-0.5">Làm mới</span>
        </button>

        <!-- Trợ giúp -->
        <button onclick="showActionToast('Trợ giúp')" class="flex flex-col items-center hover:text-[#202124]">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
          <span class="text-[9px] mt-0.5">Trợ giúp</span>
        </button>

        <!-- Thông báo -->
        <div class="relative">
          <button onclick="showActionToast('Thông báo')" class="flex flex-col items-center hover:text-[#202124]">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
            <span class="text-[9px] mt-0.5">Thông báo</span>
          </button>
          <span class="absolute top-0 right-1 w-2 h-2 bg-[#d93025] rounded-full"></span>
        </div>

        <!-- Avatar -->
        <div class="w-7 h-7 rounded-full overflow-hidden border border-[#dadce0] cursor-pointer">
          <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80" class="w-full h-full object-cover" alt="User">
        </div>
      </div>
    </header>

    <!-- 3.2 SUB-HEADER: TITLE, TABS & DATE CONTROLS -->
    <div class="px-6 pt-4 pb-0 shrink-0">
      <h1 class="text-[22px] font-normal text-[#202124] tracking-tight mb-2">Chiến dịch</h1>
      
      <div class="flex flex-col md:flex-row md:items-center justify-between border-b border-[#dadce0]">
        
        <!-- Tabs -->
        <div class="flex items-center space-x-1">
          <div class="g-tab active">Chiến dịch</div>
          <div class="g-tab" onclick="showActionToast('Việc làm chưa đăng')">Việc làm chưa đăng</div>
          <div class="g-tab" onclick="showActionToast('Cài đặt')">Cài đặt</div>
        </div>

        <!-- Date Range Controls (Exact Match Screenshot!) -->
        <div class="flex items-center gap-3 py-2 text-xs">
          <span class="text-[#5f6368]">7 ngày qua</span>
          
          <button onclick="showActionToast('Chọn khoảng thời gian')" class="flex items-center gap-1.5 px-2.5 py-1 bg-white border border-[#dadce0] rounded hover:bg-[#f8f9fa] text-[#202124]">
            <span id="dateDisplayLabel" class="font-medium">Tháng 10 25 – 31, 2026</span>
            <svg class="w-3.5 h-3.5 text-[#5f6368]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </button>

          <div class="flex items-center border border-[#dadce0] rounded overflow-hidden">
            <button onclick="showActionToast('Kỳ trước')" class="px-1.5 py-1 hover:bg-[#f1f3f4] border-r border-[#dadce0] text-[#5f6368]">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg>
            </button>
            <button onclick="showActionToast('Kỳ sau')" class="px-1.5 py-1 hover:bg-[#f1f3f4] text-[#5f6368]">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"/></svg>
            </button>
          </div>

          <a href="#" onclick="switchAccount('fec'); return false;" class="text-[#1a73e8] hover:underline text-xs">
            Hiện dữ liệu trong 30 ngày qua
          </a>
        </div>
      </div>
    </div>

    <!-- 3.3 CHART SECTION (EXACT GOOGLE ADS CHART & TOOLTIP) -->
    <div class="px-6 py-3 shrink-0">
      <!-- Chart Controls Top Right -->
      <div class="flex items-center justify-end gap-5 text-xs text-[#5f6368] mb-1">
        <button onclick="showActionToast('Đổi chỉ số biểu đồ')" class="flex items-center gap-1 hover:text-[#202124]">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 17v-4M12 17V7M17 17v-8"/></svg>
          <span>Chỉ số</span>
        </button>

        <button onclick="showActionToast('Điều chỉnh')" class="flex items-center gap-1 hover:text-[#202124]">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/></svg>
          <span>Điều chỉnh</span>
        </button>

        <button onclick="exportToExcel()" class="flex items-center gap-1 hover:text-[#202124]" title="Tải xuống dữ liệu Excel">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          <span>Tải xuống</span>
        </button>

        <button onclick="toggleChartExpand()" class="flex items-center gap-1 hover:text-[#202124]">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>
          <span>Mở rộng</span>
        </button>
      </div>

      <!-- Chart Container with Tooltip Mock -->
      <div id="chartContainer" class="relative w-full h-[180px]">
        <canvas id="exactGoogleAdsChart"></canvas>
      </div>

      <!-- Blue Scrubber Timeline Pill -->
      <div class="chart-scrubber-bar"></div>
    </div>

    <!-- 3.4 DATA TABLE (EXACT CLONE OF USER SCREENSHOT) -->
    <div class="px-6 pb-8 flex-1 overflow-x-auto">
      <table class="g-table">
        <thead>
          <tr>
            <th class="w-8 text-center"><input type="checkbox" class="g-checkbox"></th>
            <th class="w-6"></th>
            <th class="th-left min-w-[280px]">
              <span class="inline-flex items-center gap-1 cursor-pointer">
                Chiến dịch <span class="text-xs">↓</span>
              </span>
            </th>
            <th>Ngân sách</th>
            <th>Trạng thái</th>
            <th>Chi phí</th>
            <th>Lượt hiển thị</th>
            <th>Lần nhấp</th>
            <th>CPC Tr.bình</th>
            <th>CTR</th>
            <th>Điểm tối ưu hoá</th>
            <th>Lượt chuyển đổi</th>
            <th>Chi phí / ch.đổi</th>
            <th>Tỷ lệ chuyển đổi</th>
            <th>Tất cả chuyển đổi</th>
          </tr>
        </thead>
        <tbody id="tableBody">
          
          <!-- 1. Draft Notice Row (Green Background #e6f4ea) -->
          <tr class="bg-[#e6f4ea] hover:bg-[#d8eedd] transition">
            <td class="text-center">
              <svg class="w-3.5 h-3.5 text-[#1e8e3e] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
            </td>
            <td></td>
            <td class="td-left text-[#1e8e3e] font-medium" colspan="13">
              <div class="flex items-center gap-2">
                <svg class="w-4 h-4 text-[#1e8e3e]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>
                <span>Số bản nháp đang thực hiện: 0</span>
              </div>
            </td>
          </tr>

          <!-- 2. Campaign Primary Row -->
          <tr id="mainCampaignRow" class="hover:bg-[#f8f9fa] transition font-medium">
            <td class="text-center"><input type="checkbox" class="g-checkbox"></td>
            <td class="text-center">
              <!-- Green Active Status Circle -->
              <span class="inline-block w-2.5 h-2.5 rounded-full bg-[#1e8e3e]" title="Đang chạy"></span>
            </td>
            <td class="td-left font-normal text-[#202124]">
              <div class="flex items-center gap-2">
                <div class="w-5 h-5 rounded bg-[#f1f3f4] flex items-center justify-center shrink-0">
                  <svg class="w-3 h-3 text-[#5f6368]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                </div>
                <span id="campName" class="text-[#1a73e8] hover:underline cursor-pointer">
                  Lạc Hồng Viên - Search - 10/12/2025
                </span>
              </div>
            </td>
            <td class="text-[#3c4043]">
              <div class="inline-flex items-center gap-1.5">
                <span id="campBudget">330.000 đ/ngày</span>
                <svg class="w-3 h-3 text-[#5f6368] cursor-pointer" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
              </div>
            </td>
            <td>
              <span class="inline-block w-12 h-2.5 bg-[#dadce0] rounded-sm"></span>
            </td>
            <td id="campCost" class="font-normal">1.527.885 đ</td>
            <td id="campImp">862</td>
            <td id="campClicks">128</td>
            <td id="campAvgCpc">11.937 đ</td>
            <td id="campCtr">14,85%</td>
            <td>
              <a href="#" id="campOptScore" class="text-[#1a73e8] underline">93,6%</a>
            </td>
            <td id="campConv" class="font-bold text-[#202124]">5,00</td>
            <td id="campCpa">305.577 đ</td>
            <td id="campCvr">3,91%</td>
            <td id="campAllConv">--</td>
          </tr>

          <!-- 3. Indented Conversion Action Rows (Exact Screenshot Detail!) -->
          <tr class="text-[#5f6368] text-[11px] bg-[#fafafa]">
            <td></td>
            <td></td>
            <td class="td-left pl-10 text-[#3c4043]">Hoàn tất form đ/ký</td>
            <td>--</td>
            <td></td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td class="font-medium text-[#202124]">1,00</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
          </tr>

          <tr class="text-[#5f6368] text-[11px] bg-[#fafafa]">
            <td></td>
            <td></td>
            <td class="td-left pl-10 text-[#3c4043]">Click - Gọi</td>
            <td>--</td>
            <td></td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td class="font-medium text-[#202124]">3,00</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
          </tr>

          <tr class="text-[#5f6368] text-[11px] bg-[#fafafa]">
            <td></td>
            <td></td>
            <td class="td-left pl-10 text-[#3c4043]">Click - Zalo</td>
            <td>--</td>
            <td></td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td class="font-medium text-[#202124]">1,00</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
          </tr>

          <tr class="text-[#5f6368] text-[11px] bg-[#fafafa]">
            <td></td>
            <td></td>
            <td class="td-left pl-10 text-[#3c4043]">Click - Button nhận tư vấn</td>
            <td>--</td>
            <td></td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
            <td class="font-medium text-[#202124]">0,00</td>
            <td>--</td>
            <td>--</td>
            <td>--</td>
          </tr>

          <!-- 4. Sticky Bottom Total Row -->
          <tr class="bg-[#f8f9fa] border-t-2 border-[#dadce0] font-bold text-[#202124]">
            <td class="text-center">
              <svg class="w-3.5 h-3.5 text-[#5f6368] mx-auto" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
            </td>
            <td></td>
            <td class="td-left font-normal text-[#5f6368]">
              <div class="flex items-center gap-1.5 truncate max-w-sm" title="Tổng số: Tất cả chiến dịch, ngoại trừ những chiến dịch đã bị xoá trong chế độ xem này">
                <span>Tổng số: Tất cả chiến dịch, ngoại trừ những chiến dịch đã bị xoá trong chế độ xe...</span>
                <svg class="w-3.5 h-3.5 text-[#5f6368] shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
              </div>
            </td>
            <td>--</td>
            <td></td>
            <td id="totCost" class="font-medium">1.527.885 đ</td>
            <td id="totImp" class="font-medium">862</td>
            <td id="totClicks" class="font-medium">128</td>
            <td id="totAvgCpc" class="font-medium">11.937 đ</td>
            <td id="totCtr" class="font-medium">14,85%</td>
            <td class="font-medium">--</td>
            <td id="totConv" class="font-bold text-[#202124]">5,00</td>
            <td id="totCpa" class="font-medium">305.577 đ</td>
            <td id="totCvr" class="font-medium">3,91%</td>
            <td id="totAllConv" class="font-medium">--</td>
          </tr>

        </tbody>
      </table>
    </div>

  </main>

  <!-- ============================================================== -->
  <!-- 4. ACCOUNT SWITCHER MODAL / POPUP                              -->
  <!-- ============================================================== -->
  <div id="accountMenuModal" class="hidden fixed top-14 left-20 bg-white border border-[#dadce0] rounded-xl shadow-xl z-50 w-80 p-3">
    <div class="text-xs font-semibold text-[#5f6368] mb-2 uppercase tracking-wider">Chuyển tài khoản Google Ads</div>
    <div class="space-y-1.5">
      <button onclick="switchAccount('lachongvien')" class="w-full text-left p-2.5 rounded-lg border hover:bg-blue-50 hover:border-blue-300 transition flex items-center justify-between">
        <div>
          <div class="font-semibold text-xs text-[#202124]">Lạc Hồng Viên - Search</div>
          <div class="text-[11px] text-[#5f6368]">7 ngày qua • 5 chuyển đổi • 1.527.885 ₫</div>
        </div>
        <span class="text-xs text-blue-600 font-bold">✓ Ảnh mẫu</span>
      </button>

      <button onclick="switchAccount('fec')" class="w-full text-left p-2.5 rounded-lg border hover:bg-blue-50 hover:border-blue-300 transition flex items-center justify-between">
        <div>
          <div class="font-semibold text-xs text-[#202124]">FEC Explorer – Du Học Hè</div>
          <div class="text-[11px] text-[#5f6368]">30 ngày qua • 180 leads • 16.820.000 ₫</div>
        </div>
        <span class="text-xs text-emerald-600 font-bold">Case 04</span>
      </button>

      <button onclick="switchAccount('visa')" class="w-full text-left p-2.5 rounded-lg border hover:bg-blue-50 hover:border-blue-300 transition flex items-center justify-between">
        <div>
          <div class="font-semibold text-xs text-[#202124]">Tập đoàn Định cư GBlueSea</div>
          <div class="text-[11px] text-[#5f6368]">30 ngày qua • 248 leads • 34.850.000 ₫</div>
        </div>
        <span class="text-xs text-purple-600 font-bold">Visa</span>
      </button>
    </div>
  </div>

  <!-- Toast Notification -->
  <div id="toast" class="fixed bottom-6 left-1/2 transform -translate-x-1/2 bg-[#202124] text-white px-4 py-2 rounded-lg shadow-lg text-xs hidden z-50">
    <span id="toastMsg">Thao tác thành công.</span>
  </div>

  <!-- ============================================================== -->
  <!-- 5. JAVASCRIPT: LOGIC & CHART ENGINE                            -->
  <!-- ============================================================== -->
  <script>
    const ACCOUNTS = {
      lachongvien: {
        name: "Tất cả chiến dịch",
        sub: "2 bộ lọc • 1 chiến dịch",
        dateDisplay: "Tháng 10 25 – 31, 2026",
        campName: "Lạc Hồng Viên - Search - 10/12/2025",
        budget: "330.000 đ/ngày",
        cost: "1.527.885 đ",
        imp: "862",
        clicks: "128",
        avgCpc: "11.937 đ",
        ctr: "14,85%",
        optScore: "93,6%",
        conv: "5,00",
        cpa: "305.577 đ",
        cvr: "3,91%",
        chartLabels: ["25 thg 10", "26 thg 10", "27 thg 10", "28 thg 10", "29 thg 10", "30 thg 10", "31 thg 10, 2026"],
        chartData: [210000, 245000, 274585, 260000, 150000, 235000, 210000],
        chartTooltipDay: "Thứ 3, 27 thg 10, 2026",
        chartTooltipVal: "274.585 đ"
      },
      fec: {
        name: "FEC Explorer – Trại Hè Quốc Tế",
        sub: "1 bộ lọc • 7 chiến dịch",
        dateDisplay: "Tháng 7 18 – Tháng 8 16, 2026",
        campName: "FEC Explorer — Trại Hè Quốc Tế 6 Quốc Gia",
        budget: "800.000 đ/ngày",
        cost: "16.820.000 đ",
        imp: "15.800",
        clicks: "1.390",
        avgCpc: "12.101 đ",
        ctr: "8,80%",
        optScore: "94,8%",
        conv: "180,00",
        cpa: "93.445 đ",
        cvr: "12,95%",
        chartLabels: ["18/7", "22/7", "26/7", "30/7", "3/8", "7/8", "11/8", "16/8"],
        chartData: [560000, 680000, 720000, 590000, 610000, 640000, 710000, 580000],
        chartTooltipDay: "Thứ 5, 30 thg 7, 2026",
        chartTooltipVal: "590.000 đ"
      },
      visa: {
        name: "Tập đoàn Định cư GBlueSea",
        sub: "3 bộ lọc • 6 chiến dịch",
        dateDisplay: "01/10/2026 – 31/10/2026",
        campName: "GGSearch_DinhCu_EB5_My_ToanQuoc",
        budget: "1.200.000 đ/ngày",
        cost: "34.850.000 đ",
        imp: "48.920",
        clicks: "3.635",
        avgCpc: "9.587 đ",
        ctr: "7,43%",
        optScore: "91,8%",
        conv: "248,00",
        cpa: "140.524 đ",
        cvr: "6,82%",
        chartLabels: ["Tuần 1", "Tuần 2", "Tuần 3", "Tuần 4"],
        chartData: [8400000, 9200000, 8900000, 8350000],
        chartTooltipDay: "Tuần 2, Tháng 10 2026",
        chartTooltipVal: "9.200.000 đ"
      }
    };

    let activeAccountKey = 'lachongvien';
    let chartInstance = null;

    document.addEventListener("DOMContentLoaded", function() {
      renderCurrentAccount();

      // Collapse Tier 2 button
      document.getElementById("btnCollapseTier2").addEventListener("click", function() {
        const tier2 = document.getElementById("tier2Sidebar");
        tier2.classList.toggle("hidden");
        const icon = document.getElementById("collapseIcon");
        if (tier2.classList.contains("hidden")) {
          icon.innerHTML = '<polyline points="9 18 15 12 9 6"></polyline>';
        } else {
          icon.innerHTML = '<polyline points="15 18 9 12 15 6"></polyline>';
        }
      });
    });

    function toggleAccountMenu() {
      const modal = document.getElementById("accountMenuModal");
      modal.classList.toggle("hidden");
    }

    function switchAccount(key) {
      activeAccountKey = key;
      document.getElementById("accountMenuModal").classList.add("hidden");
      renderCurrentAccount();
      showActionToast(`Đã chuyển sang tài khoản: ${ACCOUNTS[key].name}`);
    }

    function renderCurrentAccount() {
      const acc = ACCOUNTS[activeAccountKey];

      document.getElementById("accNameDisplay").innerHTML = `${acc.name} <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>`;
      document.getElementById("accSubDisplay").innerText = acc.sub;
      document.getElementById("dateDisplayLabel").innerText = acc.dateDisplay;

      document.getElementById("campName").innerText = acc.campName;
      document.getElementById("campBudget").innerText = acc.budget;
      document.getElementById("campCost").innerText = acc.cost;
      document.getElementById("campImp").innerText = acc.imp;
      document.getElementById("campClicks").innerText = acc.clicks;
      document.getElementById("campAvgCpc").innerText = acc.avgCpc;
      document.getElementById("campCtr").innerText = acc.ctr;
      document.getElementById("campOptScore").innerText = acc.optScore;
      document.getElementById("campConv").innerText = acc.conv;
      document.getElementById("campCpa").innerText = acc.cpa;
      document.getElementById("campCvr").innerText = acc.cvr;

      document.getElementById("totCost").innerText = acc.cost;
      document.getElementById("totImp").innerText = acc.imp;
      document.getElementById("totClicks").innerText = acc.clicks;
      document.getElementById("totAvgCpc").innerText = acc.avgCpc;
      document.getElementById("totCtr").innerText = acc.ctr;
      document.getElementById("totConv").innerText = acc.conv;
      document.getElementById("totCpa").innerText = acc.cpa;
      document.getElementById("totCvr").innerText = acc.cvr;

      renderChart(acc);
    }

    function renderChart(acc) {
      const ctx = document.getElementById("exactGoogleAdsChart").getContext("2d");

      if (chartInstance) {
        chartInstance.destroy();
      }

      chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: acc.chartLabels,
          datasets: [{
            data: acc.chartData,
            borderColor: '#1a73e8',
            borderWidth: 2,
            pointBackgroundColor: '#1a73e8',
            pointRadius: 3,
            pointHoverRadius: 6,
            tension: 0.35,
            fill: false
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              enabled: true,
              backgroundColor: '#ffffff',
              titleColor: '#202124',
              bodyColor: '#3c4043',
              borderColor: '#dadce0',
              borderWidth: 1,
              titleFont: { family: 'Google Sans', size: 12, weight: '500' },
              bodyFont: { family: 'Google Sans', size: 14, weight: '700' },
              padding: 12,
              cornerRadius: 8,
              boxShadow: '0 4px 12px rgba(60,64,67,0.15)',
              displayColors: false,
              callbacks: {
                title: function(context) {
                  return context[0].label.includes('27') ? acc.chartTooltipDay : context[0].label;
                },
                label: function(context) {
                  return `Chi phí\n- ${context.parsed.y.toLocaleString('vi-VN')} đ`;
                }
              }
            }
          },
          scales: {
            x: {
              grid: { display: false },
              ticks: { color: '#5f6368', font: { family: 'Google Sans', size: 11 } }
            },
            y: {
              grid: { color: '#f1f3f4' },
              ticks: {
                color: '#5f6368',
                font: { family: 'Google Sans', size: 11 },
                callback: function(val) {
                  return val === 0 ? '0 đ' : val.toLocaleString('vi-VN') + ' đ';
                }
              }
            }
          }
        }
      });
    }

    function showActionToast(msg) {
      const toast = document.getElementById("toast");
      document.getElementById("toastMsg").innerText = msg;
      toast.classList.remove("hidden");
      setTimeout(() => toast.classList.add("hidden"), 2500);
    }

    function refreshData() {
      const icon = document.getElementById("refreshIcon");
      icon.classList.add("animate-spin");
      setTimeout(() => {
        icon.classList.remove("animate-spin");
        renderCurrentAccount();
        showActionToast("Đã đồng bộ dữ liệu mới nhất từ Google Ads");
      }, 500);
    }

    function exportToExcel() {
      const acc = ACCOUNTS[activeAccountKey];
      const wb = XLSX.utils.book_new();

      const data = [
        {
          "Chiến dịch": acc.campName,
          "Ngân sách": acc.budget,
          "Chi phí": acc.cost,
          "Lượt hiển thị": acc.imp,
          "Lần nhấp": acc.clicks,
          "CPC Tr.bình": acc.avgCpc,
          "CTR": acc.ctr,
          "Điểm tối ưu hoá": acc.optScore,
          "Lượt chuyển đổi": acc.conv,
          "Chi phí / ch.đổi": acc.cpa,
          "Tỷ lệ chuyển đổi": acc.cvr
        }
      ];

      const ws = XLSX.utils.json_to_sheet(data);
      XLSX.utils.book_append_sheet(wb, ws, "Chien_Dich");
      XLSX.writeFile(wb, `Bao_Cao_Google_Ads_${activeAccountKey}.xlsx`);
      showActionToast("Đã xuất file Excel (.xlsx) chuẩn doanh nghiệp.");
    }

    function toggleChartExpand() {
      const container = document.getElementById("chartContainer");
      if (container.classList.contains("h-[180px]")) {
        container.classList.remove("h-[180px]");
        container.classList.add("h-[340px]");
      } else {
        container.classList.remove("h-[340px]");
        container.classList.add("h-[180px]");
      }
      chartInstance.resize();
    }
  </script>
</body>
</html>
'''

output_path = "Google_Ads_Dashboard_Chuyen_Doi.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Updated {output_path} successfully. Size: {len(html_content)} bytes.")
