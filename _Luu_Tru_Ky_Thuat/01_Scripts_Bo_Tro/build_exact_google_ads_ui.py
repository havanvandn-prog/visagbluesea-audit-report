import os

html_code = '''<!DOCTYPE html>
<html lang="vi" class="h-full w-full">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chiến dịch - Google Ads</title>
  
  <!-- 1. Google Fonts: Google Sans & Roboto (Exact Google Ads Fonts) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Roboto:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Roboto+Mono:wght@400;500&display=swap" rel="stylesheet">
  
  <!-- 2. Google Material Symbols (Exact Google Ads Icons) -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />

  <!-- 3. Chart.js & SheetJS -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script src="https://cdn.sheetjs.com/xlsx-0.20.1/package/dist/xlsx.full.min.js"></script>

  <style>
    :root {
      --google-blue: #1a73e8;
      --google-blue-hover: #1765cc;
      --google-blue-light: #e8f0fe;
      --google-hairline: #dadce0;
      --google-surface: #ffffff;
      --google-surface-variant: #f8f9fa;
      --google-text-primary: #202124;
      --google-text-secondary: #5f6368;
      --google-red: #d93025;
      --google-green: #1e8e3e;
      --google-green-bg: #e6f4ea;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Roboto', 'Google Sans', system-ui, -apple-system, sans-serif;
      font-size: 13px;
      line-height: 20px;
      color: var(--google-text-primary);
      background-color: var(--google-surface);
      height: 100vh;
      width: 100vw;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
      user-select: none;
    }

    /* Material Symbols Base */
    .material-symbols-outlined {
      font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 20;
      font-size: 20px;
      line-height: 1;
      display: inline-block;
      vertical-align: middle;
      color: var(--google-text-secondary);
    }
    .material-symbols-outlined.fill-1 {
      font-variation-settings: 'FILL' 1, 'wght' 400, 'GRAD' 0, 'opsz' 20;
    }

    /* Scrollbars Google Style */
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: transparent;
    }
    ::-webkit-scrollbar-thumb {
      background: #dadce0;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #bdc1c6;
    }

    /* ========================================================= */
    /* TOP APP BAR (awsm-app-bar)                                */
    /* ========================================================= */
    .g-app-bar {
      height: 56px;
      border-bottom: 1px solid var(--google-hairline);
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px 0 0;
      flex-shrink: 0;
      z-index: 50;
    }

    .g-app-bar-left {
      display: flex;
      align-items: center;
    }

    .g-app-bar-view-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background-color: #1a73e8;
      color: #ffffff;
      border-radius: 4px;
      padding: 6px 12px;
      margin-left: 60px;
      font-family: 'Google Sans', sans-serif;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      border: none;
      transition: background 0.15s;
    }
    .g-app-bar-view-btn:hover {
      background-color: #1557b0;
    }
    .g-app-bar-view-btn .sub-text {
      font-size: 11px;
      font-weight: 400;
      color: #e8f0fe;
    }

    /* Alerts in Top Bar */
    .g-alert-banner {
      display: flex;
      align-items: center;
      gap: 16px;
      font-size: 12px;
    }
    .g-alert-item {
      display: flex;
      align-items: center;
      gap: 4px;
      color: var(--google-text-primary);
    }
    .g-alert-item .icon-warn {
      color: var(--google-red);
      font-size: 16px;
    }
    .g-alert-item a {
      color: #1a73e8;
      text-decoration: none;
      font-weight: 500;
      margin-left: 4px;
    }
    .g-alert-item a:hover {
      text-decoration: underline;
    }

    /* Right Icons (awsm-app-menus) */
    .g-app-bar-right {
      display: flex;
      align-items: center;
      gap: 2px;
    }
    .g-app-bar-icon-btn {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 52px;
      padding: 4px 10px;
      border-radius: 4px;
      cursor: pointer;
      color: var(--google-text-secondary);
      border: none;
      background: transparent;
      transition: background 0.15s;
    }
    .g-app-bar-icon-btn:hover {
      background-color: #f1f3f4;
      color: var(--google-text-primary);
    }
    .g-app-bar-icon-btn span.label {
      font-size: 10px;
      font-family: 'Google Sans', sans-serif;
      margin-top: 1px;
      line-height: 1;
    }

    /* Avatar */
    .g-user-avatar {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      overflow: hidden;
      margin-left: 8px;
      cursor: pointer;
      border: 1px solid var(--google-hairline);
    }
    .g-user-avatar img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    /* ========================================================= */
    /* LEFT RAIL NAVIGATION (Tier 1: 60px)                       */
    /* ========================================================= */
    .g-tier1-rail {
      width: 60px;
      background: #ffffff;
      border-right: 1px solid var(--google-hairline);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      padding: 8px 0 12px 0;
      flex-shrink: 0;
      z-index: 40;
    }

    .g-tier1-logo {
      margin-bottom: 8px;
      cursor: pointer;
    }

    .g-create-btn {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 44px;
      height: 44px;
      border-radius: 16px;
      background: #ffffff;
      border: 1px solid var(--google-hairline);
      box-shadow: 0 1px 3px rgba(60,64,67,0.2);
      cursor: pointer;
      margin-bottom: 12px;
      transition: box-shadow 0.2s, background 0.15s;
    }
    .g-create-btn:hover {
      box-shadow: 0 2px 6px rgba(60,64,67,0.3);
      background: #fafafa;
    }
    .g-create-btn span {
      font-size: 9px;
      color: var(--google-text-secondary);
      font-weight: 500;
      margin-top: -2px;
    }

    .g-tier1-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 52px;
      height: 52px;
      border-radius: 16px;
      margin-bottom: 4px;
      cursor: pointer;
      color: var(--google-text-secondary);
      transition: background 0.15s;
    }
    .g-tier1-item:hover {
      background-color: #f1f3f4;
    }
    .g-tier1-item.active {
      background-color: #1a73e8;
      color: #ffffff;
    }
    .g-tier1-item.active .material-symbols-outlined {
      color: #ffffff;
    }
    .g-tier1-item span.item-label {
      font-size: 9.5px;
      font-family: 'Google Sans', sans-serif;
      font-weight: 500;
      margin-top: 2px;
      line-height: 1;
    }

    .g-tier1-collapse {
      display: flex;
      flex-direction: column;
      align-items: center;
      color: var(--google-text-secondary);
      cursor: pointer;
      padding: 4px;
      border-radius: 8px;
    }
    .g-tier1-collapse:hover {
      background: #f1f3f4;
    }
    .g-tier1-collapse span {
      font-size: 9px;
      margin-top: 2px;
    }

    /* ========================================================= */
    /* TIER 2 SUB-SIDEBAR (200px)                                */
    /* ========================================================= */
    .g-tier2-sidebar {
      width: 200px;
      background: #ffffff;
      border-right: 1px solid var(--google-hairline);
      overflow-y: auto;
      flex-shrink: 0;
      padding: 8px 0;
      transition: width 0.2s, opacity 0.2s;
    }
    .g-tier2-sidebar.collapsed {
      width: 0;
      opacity: 0;
      padding: 0;
      overflow: hidden;
      border-right: none;
    }

    .g-tier2-nav-link {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 7px 16px 7px 20px;
      font-size: 13px;
      color: var(--google-text-primary);
      border-radius: 0 16px 16px 0;
      margin-right: 8px;
      cursor: pointer;
      font-family: 'Roboto', sans-serif;
      transition: background 0.1s;
    }
    .g-tier2-nav-link:hover {
      background-color: #f8f9fa;
    }
    .g-tier2-nav-link.active {
      background-color: #1a73e8;
      color: #ffffff;
      font-weight: 500;
    }
    .g-tier2-nav-link.active .material-symbols-outlined {
      color: #ffffff;
    }

    .g-tier2-sub-link {
      display: block;
      padding: 6px 16px 6px 36px;
      font-size: 12.5px;
      color: var(--google-text-primary);
      border-radius: 0 16px 16px 0;
      margin-right: 8px;
      cursor: pointer;
      transition: background 0.1s;
    }
    .g-tier2-sub-link:hover {
      background-color: #f8f9fa;
    }
    .g-tier2-sub-link.active {
      background-color: #1a73e8;
      color: #ffffff;
      font-weight: 500;
    }

    /* ========================================================= */
    /* MAIN WORKSPACE CONTENT                                    */
    /* ========================================================= */
    .g-main-container {
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      overflow-x: hidden;
      background: #ffffff;
    }

    /* Sub-header / View Header */
    .g-view-header {
      padding: 16px 24px 0 24px;
      flex-shrink: 0;
    }

    .g-page-title {
      font-family: 'Google Sans', sans-serif;
      font-size: 22px;
      font-weight: 400;
      color: var(--google-text-primary);
      margin-bottom: 8px;
    }

    .g-tabs-and-date-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--google-hairline);
    }

    .g-tab-group {
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .g-view-tab {
      padding: 10px 16px;
      font-size: 13px;
      font-family: 'Google Sans', sans-serif;
      font-weight: 500;
      color: var(--google-text-secondary);
      border-bottom: 3px solid transparent;
      cursor: pointer;
      transition: color 0.15s, border-color 0.15s;
    }
    .g-view-tab:hover {
      color: var(--google-text-primary);
    }
    .g-view-tab.active {
      color: #1a73e8;
      border-bottom-color: #1a73e8;
    }

    .g-date-controls {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      color: var(--google-text-secondary);
    }
    .g-date-btn {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 5px 10px;
      border: 1px solid var(--google-hairline);
      border-radius: 4px;
      background: #ffffff;
      font-size: 12px;
      color: var(--google-text-primary);
      cursor: pointer;
    }
    .g-date-btn:hover {
      background-color: #f8f9fa;
    }
    .g-date-nav {
      display: inline-flex;
      border: 1px solid var(--google-hairline);
      border-radius: 4px;
      overflow: hidden;
    }
    .g-date-nav-btn {
      padding: 4px 6px;
      background: #ffffff;
      border: none;
      cursor: pointer;
      color: var(--google-text-secondary);
      display: flex;
      align-items: center;
    }
    .g-date-nav-btn:hover {
      background: #f1f3f4;
    }
    .g-date-nav-btn:first-child {
      border-right: 1px solid var(--google-hairline);
    }

    /* ========================================================= */
    /* CHART CONTAINER (aplos-time-series-chart)                 */
    /* ========================================================= */
    .g-chart-section {
      padding: 12px 24px 0 24px;
      flex-shrink: 0;
    }

    .g-chart-toolbar {
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 16px;
      font-size: 12px;
      color: var(--google-text-secondary);
      margin-bottom: 4px;
    }
    .g-chart-tool-btn {
      display: flex;
      align-items: center;
      gap: 4px;
      background: none;
      border: none;
      cursor: pointer;
      color: var(--google-text-secondary);
      font-size: 12px;
      font-family: 'Roboto', sans-serif;
    }
    .g-chart-tool-btn:hover {
      color: var(--google-text-primary);
    }

    .g-chart-wrapper {
      position: relative;
      width: 100%;
      height: 190px;
    }

    /* Bottom Scrubber Timeline Bar */
    .g-timeline-scrubber {
      height: 16px;
      background: linear-gradient(90deg, #9bb8fd 0%, #b8ccfd 100%);
      border-radius: 8px;
      margin: 8px 0 16px 0;
    }

    /* ========================================================= */
    /* DATA TABLE (ess-table / ess-particle-table)               */
    /* ========================================================= */
    .g-table-container {
      padding: 0 24px 40px 24px;
      flex: 1;
      overflow-x: auto;
    }

    .g-ess-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
      font-family: 'Roboto', sans-serif;
    }

    .g-ess-table thead th {
      background-color: #ffffff;
      color: var(--google-text-secondary);
      font-weight: 500;
      padding: 8px 10px;
      border-top: 1px solid var(--google-hairline);
      border-bottom: 1px solid var(--google-hairline);
      text-align: right;
      white-space: nowrap;
      user-select: none;
    }
    .g-ess-table thead th.th-left {
      text-align: left;
    }
    .g-ess-table thead th.sortable:hover {
      background-color: #f1f3f4;
      cursor: pointer;
    }

    .g-ess-table tbody tr {
      transition: background 0.1s;
    }
    .g-ess-table tbody tr:hover {
      background-color: #f8f9fa;
    }

    .g-ess-table td {
      padding: 8px 10px;
      border-bottom: 1px solid #ebebeb;
      text-align: right;
      white-space: nowrap;
      color: #3c4043;
      font-variant-numeric: tabular-nums;
    }
    .g-ess-table td.td-left {
      text-align: left;
    }

    /* Draft Notification Row */
    .g-draft-row td {
      background-color: #e6f4ea !important;
      color: #1e8e3e !important;
      font-weight: 500;
      border-bottom: 1px solid #cce8d4 !important;
    }

    /* Conversion Sub-Rows */
    .g-sub-row td {
      background-color: #fafafa;
      color: #5f6368;
      font-size: 11.5px;
    }

    /* Sticky Footer Total Row */
    .g-total-row td {
      background-color: #f8f9fa !important;
      border-top: 2px solid var(--google-hairline) !important;
      border-bottom: 1px solid var(--google-hairline) !important;
      font-weight: 500;
      color: var(--google-text-primary);
    }

    /* Google Checkbox */
    .g-chk {
      width: 16px;
      height: 16px;
      accent-color: #1a73e8;
      cursor: pointer;
    }

    /* Status Circle */
    .g-status-dot {
      display: inline-block;
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background-color: #1e8e3e;
    }
  </style>
</head>
<body>

  <!-- ========================================================= -->
  <!-- 1. TOP APP BAR (awsm-app-bar)                             -->
  <!-- ========================================================= -->
  <header class="g-app-bar">
    <div class="g-app-bar-left">
      <!-- Blue Account Button -->
      <button id="btnViewMenu" onclick="toggleAccountModal()" class="g-app-bar-view-btn">
        <span class="material-symbols-outlined" style="font-size: 16px; color: #fff;">home</span>
        <div style="text-align: left;">
          <div id="topAccountTitle">Tất cả chiến dịch</div>
          <div id="topAccountSubtitle" class="sub-text">2 bộ lọc • 1 chiến dịch</div>
        </div>
        <span class="material-symbols-outlined" style="font-size: 18px; color: #fff;">expand_more</span>
      </button>
    </div>

    <!-- Center Alerts (Exact as screenshot) -->
    <div class="g-alert-banner">
      <div class="g-alert-item">
        <span class="material-symbols-outlined icon-warn">error</span>
        <span>Số dư sắp hết</span>
        <a href="#" onclick="showActionToast('Khắc phục vấn đề nạp tiền'); return false;">Khắc phục vấn đề</a>
      </div>
      <div class="g-alert-item">
        <span class="material-symbols-outlined icon-warn">error</span>
        <span>Bảo vệ tài khoản của bạn khỏi hoạt động trái phép</span>
        <a href="#" onclick="showActionToast('Bảo mật tài khoản'); return false;">Xem</a>
        <span class="material-symbols-outlined" style="font-size: 14px; cursor: pointer; margin-left: 4px;" onclick="this.parentElement.style.display='none'">close</span>
      </div>
    </div>

    <!-- Right Menu Icons (awsm-app-menus) -->
    <div class="g-app-bar-right">
      <button class="g-app-bar-icon-btn" onclick="showActionToast('Tìm kiếm')">
        <span class="material-symbols-outlined">search</span>
        <span class="label">Tìm kiếm</span>
      </button>

      <button class="g-app-bar-icon-btn" onclick="showActionToast('Giao diện')">
        <span class="material-symbols-outlined">responsive_layout</span>
        <span class="label">Giao diện</span>
      </button>

      <button class="g-app-bar-icon-btn" onclick="refreshData()">
        <span id="refreshIcon" class="material-symbols-outlined">refresh</span>
        <span class="label">Làm mới</span>
      </button>

      <button class="g-app-bar-icon-btn" onclick="showActionToast('Trợ giúp')">
        <span class="material-symbols-outlined">help_outline</span>
        <span class="label">Trợ giúp</span>
      </button>

      <div style="position: relative;">
        <button class="g-app-bar-icon-btn" onclick="showActionToast('Thông báo')">
          <span class="material-symbols-outlined">notifications</span>
          <span class="label">Thông báo</span>
        </button>
        <span style="position: absolute; top: 6px; right: 12px; width: 7px; height: 7px; background: #d93025; border-radius: 50%;"></span>
      </div>

      <div class="g-user-avatar" onclick="showActionToast('Tài khoản: havanvanpod@gmail.com')">
        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80" alt="Avatar">
      </div>
    </div>
  </header>

  <!-- ========================================================= -->
  <!-- 2. BODY SPLIT: TIER 1 + TIER 2 + MAIN CONTENT             -->
  <!-- ========================================================= -->
  <div style="display: flex; flex: 1; overflow: hidden;">

    <!-- 2.1 TIER 1 LEFT RAIL (60px) -->
    <aside class="g-tier1-rail">
      <div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
        <!-- Logo -->
        <div class="g-tier1-logo" onclick="location.reload()" title="Google Ads">
          <svg style="width: 28px; height: 28px;" viewBox="0 0 48 48" fill="none">
            <path d="M43.6 20.3L28.1 4.8C26.5 3.2 23.9 3.2 22.3 4.8L6.8 20.3C5.2 21.9 5.2 24.5 6.8 26.1L22.3 41.6C23.9 43.2 26.5 43.2 28.1 41.6L43.6 26.1C45.2 24.5 45.2 21.9 43.6 20.3Z" fill="#FBBC04"/>
            <path d="M12.4 34.4C10.8 32.8 10.8 30.2 12.4 28.6L27.9 13.1C29.5 11.5 32.1 11.5 33.7 13.1C35.3 14.7 35.3 17.3 33.7 18.9L18.2 34.4C16.6 36 14 36 12.4 34.4Z" fill="#4285F4"/>
            <circle cx="15.3" cy="31.5" r="3.5" fill="#34A853"/>
          </svg>
        </div>

        <!-- '+ Tạo' Button -->
        <div class="g-create-btn" onclick="showActionToast('Mở tạo chiến dịch mới')" title="Tạo">
          <svg style="width: 20px; height: 20px;" viewBox="0 0 24 24" fill="none">
            <path d="M12 5V19M5 12H19" stroke="#1a73e8" stroke-width="2.5" stroke-linecap="round"/>
          </svg>
          <span>Tạo</span>
        </div>

        <!-- 1. Chiến dịch (ACTIVE) -->
        <div class="g-tier1-item active">
          <span class="material-symbols-outlined">campaign</span>
          <span class="item-label">Chiến dịch</span>
        </div>

        <!-- 2. Mục tiêu -->
        <div class="g-tier1-item" onclick="showActionToast('Mục tiêu')">
          <span class="material-symbols-outlined">crisis_alert</span>
          <span class="item-label">Mục tiêu</span>
        </div>

        <!-- 3. Công cụ -->
        <div class="g-tier1-item" onclick="showActionToast('Công cụ')">
          <span class="material-symbols-outlined">build</span>
          <span class="item-label">Công cụ</span>
        </div>

        <!-- 4. Thanh toán -->
        <div class="g-tier1-item" onclick="showActionToast('Thanh toán')">
          <span class="material-symbols-outlined">payments</span>
          <span class="item-label">Thanh toán</span>
        </div>

        <!-- 5. Quản trị -->
        <div class="g-tier1-item" onclick="showActionToast('Quản trị')">
          <span class="material-symbols-outlined">settings</span>
          <span class="item-label">Quản trị</span>
        </div>
      </div>

      <!-- Bottom: '< Thu gọn' button -->
      <div id="btnCollapseSidebar" class="g-tier1-collapse" onclick="toggleSidebar()">
        <span id="collapseIcon" class="material-symbols-outlined" style="font-size: 16px;">chevron_left</span>
        <span>Thu gọn</span>
      </div>
    </aside>

    <!-- 2.2 TIER 2 SUB-SIDEBAR (200px) -->
    <aside id="tier2Sidebar" class="g-tier2-sidebar">
      <div class="g-tier2-nav-link" onclick="showActionToast('Tổng quan')">
        <span>Tổng quan</span>
      </div>

      <div class="g-tier2-nav-link" onclick="showActionToast('Đề xuất')">
        <span>Đề xuất</span>
      </div>

      <div class="g-tier2-nav-link" onclick="showActionToast('Thông tin chi tiết và báo cáo')">
        <span>Thông tin chi tiết và báo cáo</span>
        <span class="material-symbols-outlined" style="font-size: 18px;">expand_more</span>
      </div>

      <!-- Group Chiến dịch (Expanded) -->
      <div>
        <div class="g-tier2-nav-link" style="color: #1a73e8; font-weight: 500;">
          <span>Chiến dịch</span>
          <span class="material-symbols-outlined" style="font-size: 18px; color: #1a73e8;">expand_less</span>
        </div>
        <div>
          <div class="g-tier2-sub-link active">Chiến dịch</div>
          <div class="g-tier2-sub-link" onclick="showActionToast('Nhóm quảng cáo')">Nhóm quảng cáo</div>
          <div class="g-tier2-sub-link" onclick="showActionToast('Quảng cáo')">Quảng cáo</div>
          <div class="g-tier2-sub-link" onclick="showActionToast('Thử nghiệm')">Thử nghiệm</div>
          <div class="g-tier2-sub-link" onclick="showActionToast('Nhóm chiến dịch')">Nhóm chiến dịch</div>
        </div>
      </div>

      <div class="g-tier2-nav-link" onclick="showActionToast('Thành phần')">
        <span>Thành phần</span>
        <span class="material-symbols-outlined" style="font-size: 18px;">expand_more</span>
      </div>

      <div class="g-tier2-nav-link" onclick="showActionToast('Đối tượng, từ khoá và nội dung')">
        <span>Đối tượng, từ khoá và nội dung</span>
        <span class="material-symbols-outlined" style="font-size: 18px;">expand_more</span>
      </div>

      <div class="g-tier2-nav-link" onclick="showActionToast('Nhật ký thay đổi')">
        <span>Nhật ký thay đổi</span>
      </div>
    </aside>

    <!-- 2.3 MAIN CONTENT WORKSPACE -->
    <main class="g-main-container">

      <!-- View Header -->
      <div class="g-view-header">
        <h1 class="g-page-title">Chiến dịch</h1>

        <div class="g-tabs-and-date-row">
          <!-- Left Tabs -->
          <div class="g-tab-group">
            <div class="g-view-tab active">Chiến dịch</div>
            <div class="g-view-tab" onclick="showActionToast('Việc làm chưa đăng')">Việc làm chưa đăng</div>
            <div class="g-view-tab" onclick="showActionToast('Cài đặt')">Cài đặt</div>
          </div>

          <!-- Right Date Controls -->
          <div class="g-date-controls">
            <span>7 ngày qua</span>

            <div class="g-date-btn" onclick="toggleAccountModal()">
              <span id="dateDisplayLabel" style="font-weight: 500;">Tháng 10 25 – 31, 2026</span>
              <span class="material-symbols-outlined" style="font-size: 18px;">arrow_drop_down</span>
            </div>

            <div class="g-date-nav">
              <button class="g-date-nav-btn" onclick="showActionToast('Kỳ trước')">
                <span class="material-symbols-outlined" style="font-size: 16px;">chevron_left</span>
              </button>
              <button class="g-date-nav-btn" onclick="showActionToast('Kỳ sau')">
                <span class="material-symbols-outlined" style="font-size: 16px;">chevron_right</span>
              </button>
            </div>

            <a href="#" onclick="switchAccount('fec'); return false;" style="color: #1a73e8; text-decoration: none;">
              Hiện dữ liệu trong 30 ngày qua
            </a>
          </div>
        </div>
      </div>

      <!-- Chart Section -->
      <div class="g-chart-section">
        <div class="g-chart-toolbar">
          <button class="g-chart-tool-btn" onclick="showActionToast('Đổi chỉ số biểu đồ')">
            <span class="material-symbols-outlined">query_stats</span>
            <span>Chỉ số</span>
          </button>
          <button class="g-chart-tool-btn" onclick="showActionToast('Điều chỉnh')">
            <span class="material-symbols-outlined">tune</span>
            <span>Điều chỉnh</span>
          </button>
          <button class="g-chart-tool-btn" onclick="exportToExcel()" title="Tải xuống dữ liệu Excel (.xlsx)">
            <span class="material-symbols-outlined">download</span>
            <span>Tải xuống</span>
          </button>
          <button class="g-chart-tool-btn" onclick="toggleChartHeight()">
            <span class="material-symbols-outlined">open_in_full</span>
            <span>Mở rộng</span>
          </button>
        </div>

        <div id="chartBox" class="g-chart-wrapper">
          <canvas id="googleAdsCanvas"></canvas>
        </div>

        <!-- Scrubber bar -->
        <div class="g-timeline-scrubber"></div>
      </div>

      <!-- Table Section -->
      <div class="g-table-container">
        <table class="g-ess-table">
          <thead>
            <tr>
              <th style="width: 32px; text-align: center;"><input type="checkbox" class="g-chk"></th>
              <th style="width: 24px;"></th>
              <th class="th-left sortable" style="min-width: 280px;" onclick="showActionToast('Sắp xếp theo Chiến dịch')">
                <span>Chiến dịch</span>
                <span class="material-symbols-outlined" style="font-size: 14px; vertical-align: middle;">arrow_downward</span>
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
          <tbody>
            <!-- Draft Notice Row -->
            <tr class="g-draft-row">
              <td style="text-align: center;">
                <span class="material-symbols-outlined" style="font-size: 16px; color: #1e8e3e;">expand_more</span>
              </td>
              <td></td>
              <td class="td-left" colspan="13">
                <div style="display: flex; align-items: center; gap: 6px;">
                  <span class="material-symbols-outlined" style="font-size: 16px; color: #1e8e3e;">folder</span>
                  <span>Số bản nháp đang thực hiện: 0</span>
                </div>
              </td>
            </tr>

            <!-- Main Campaign Row -->
            <tr>
              <td style="text-align: center;"><input type="checkbox" class="g-chk"></td>
              <td style="text-align: center;"><span class="g-status-dot" title="Đang chạy"></span></td>
              <td class="td-left">
                <div style="display: flex; align-items: center; gap: 6px;">
                  <div style="width: 20px; height: 20px; background: #f1f3f4; border-radius: 2px; display: flex; align-items: center; justify-content: center;">
                    <span class="material-symbols-outlined" style="font-size: 13px;">search</span>
                  </div>
                  <span id="cName" style="color: #1a73e8; cursor: pointer;" onclick="showActionToast('Xem chi tiết chiến dịch')">
                    Lạc Hồng Viên - Search - 10/12/2025
                  </span>
                </div>
              </td>
              <td>
                <div style="display: inline-flex; align-items: center; gap: 4px;">
                  <span id="cBudget">330.000 đ/ngày</span>
                  <span class="material-symbols-outlined" style="font-size: 13px; cursor: pointer;">edit</span>
                </div>
              </td>
              <td>
                <span style="display: inline-block; width: 48px; height: 10px; background: #dadce0; border-radius: 2px;"></span>
              </td>
              <td id="cCost">1.527.885 đ</td>
              <td id="cImp">862</td>
              <td id="cClicks">128</td>
              <td id="cAvgCpc">11.937 đ</td>
              <td id="cCtr">14,85%</td>
              <td><a href="#" id="cOptScore" style="color: #1a73e8; text-decoration: underline;">93,6%</a></td>
              <td id="cConv" style="font-weight: 700; color: #202124;">5,00</td>
              <td id="cCpa">305.577 đ</td>
              <td id="cCvr">3,91%</td>
              <td>--</td>
            </tr>

            <!-- Conversion Action Sub-Rows (Indented exact match) -->
            <tr class="g-sub-row">
              <td></td>
              <td></td>
              <td class="td-left" style="padding-left: 36px;">Hoàn tất form đ/ký</td>
              <td>--</td>
              <td></td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td style="font-weight: 500; color: #202124;">1,00</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
            </tr>

            <tr class="g-sub-row">
              <td></td>
              <td></td>
              <td class="td-left" style="padding-left: 36px;">Click - Gọi</td>
              <td>--</td>
              <td></td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td style="font-weight: 500; color: #202124;">3,00</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
            </tr>

            <tr class="g-sub-row">
              <td></td>
              <td></td>
              <td class="td-left" style="padding-left: 36px;">Click - Zalo</td>
              <td>--</td>
              <td></td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td style="font-weight: 500; color: #202124;">1,00</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
            </tr>

            <tr class="g-sub-row">
              <td></td>
              <td></td>
              <td class="td-left" style="padding-left: 36px;">Click - Button nhận tư vấn</td>
              <td>--</td>
              <td></td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
              <td style="font-weight: 500; color: #202124;">0,00</td>
              <td>--</td>
              <td>--</td>
              <td>--</td>
            </tr>

            <!-- Total Row -->
            <tr class="g-total-row">
              <td style="text-align: center;">
                <span class="material-symbols-outlined" style="font-size: 16px;">expand_more</span>
              </td>
              <td></td>
              <td class="td-left" style="font-weight: 400; color: #5f6368;">
                <div style="display: flex; align-items: center; gap: 4px;">
                  <span>Tổng số: Tất cả chiến dịch, ngoại trừ những chiến dịch đã bị xoá trong chế độ xe...</span>
                  <span class="material-symbols-outlined" style="font-size: 14px;">info</span>
                </div>
              </td>
              <td>--</td>
              <td></td>
              <td id="tCost">1.527.885 đ</td>
              <td id="tImp">862</td>
              <td id="tClicks">128</td>
              <td id="tAvgCpc">11.937 đ</td>
              <td id="tCtr">14,85%</td>
              <td>--</td>
              <td id="tConv" style="font-weight: 700; color: #202124;">5,00</td>
              <td id="tCpa">305.577 đ</td>
              <td id="tCvr">3,91%</td>
              <td>--</td>
            </tr>
          </tbody>
        </table>
      </div>

    </main>
  </div>

  <!-- Account Selector Modal -->
  <div id="accountModal" style="display: none; position: fixed; top: 58px; left: 70px; width: 340px; background: #fff; border: 1px solid #dadce0; border-radius: 8px; box-shadow: 0 4px 16px rgba(60,64,67,0.2); z-index: 100; padding: 12px;">
    <div style="font-size: 11px; font-weight: 500; color: #5f6368; text-transform: uppercase; margin-bottom: 8px;">
      Chọn tài khoản Google Ads
    </div>

    <div style="display: flex; flex-direction: column; gap: 6px;">
      <div onclick="switchAccount('lachongvien')" style="padding: 8px 10px; border-radius: 6px; border: 1px solid #dadce0; cursor: pointer; display: flex; justify-content: space-between; align-items: center;" onmouseover="this.style.background='#f1f3f4'" onmouseout="this.style.background='#fff'">
        <div>
          <div style="font-weight: 500; color: #202124;">Lạc Hồng Viên - Search</div>
          <div style="font-size: 11px; color: #5f6368;">7 ngày qua • 5 chuyển đổi • 1.527.885 ₫</div>
        </div>
        <span style="font-size: 11px; color: #1a73e8; font-weight: 700;">Ảnh gốc</span>
      </div>

      <div onclick="switchAccount('fec')" style="padding: 8px 10px; border-radius: 6px; border: 1px solid #dadce0; cursor: pointer; display: flex; justify-content: space-between; align-items: center;" onmouseover="this.style.background='#f1f3f4'" onmouseout="this.style.background='#fff'">
        <div>
          <div style="font-weight: 500; color: #202124;">FEC Explorer – Du Học Hè</div>
          <div style="font-size: 11px; color: #5f6368;">30 ngày qua • 180 leads • 16.820.000 ₫</div>
        </div>
        <span style="font-size: 11px; color: #1e8e3e; font-weight: 700;">Case 04</span>
      </div>

      <div onclick="switchAccount('visa')" style="padding: 8px 10px; border-radius: 6px; border: 1px solid #dadce0; cursor: pointer; display: flex; justify-content: space-between; align-items: center;" onmouseover="this.style.background='#f1f3f4'" onmouseout="this.style.background='#fff'">
        <div>
          <div style="font-weight: 500; color: #202124;">Tập đoàn Định cư GBlueSea</div>
          <div style="font-size: 11px; color: #5f6368;">30 ngày qua • 248 leads • 34.850.000 ₫</div>
        </div>
        <span style="font-size: 11px; color: #9334e6; font-weight: 700;">Visa</span>
      </div>
    </div>
  </div>

  <!-- Toast -->
  <div id="gToast" style="display: none; position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background: #202124; color: #ffffff; padding: 8px 16px; border-radius: 4px; font-size: 12px; z-index: 200; box-shadow: 0 2px 6px rgba(0,0,0,0.3);">
    <span id="gToastMsg">Thao tác thành công.</span>
  </div>

  <script>
    const DATA_CONFIG = {
      lachongvien: {
        title: "Tất cả chiến dịch",
        subtitle: "2 bộ lọc • 1 chiến dịch",
        date: "Tháng 10 25 – 31, 2026",
        name: "Lạc Hồng Viên - Search - 10/12/2025",
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
        labels: ["25 thg 10, 2026", "26 thg 10", "27 thg 10", "28 thg 10", "29 thg 10", "30 thg 10", "31 thg 10, 2026"],
        values: [215000, 245000, 274585, 260000, 150000, 235000, 210000],
        tooltipTitle: "Thứ 3, 27 thg 10, 2026"
      },
      fec: {
        title: "FEC Explorer – Trại Hè Quốc Tế",
        subtitle: "1 bộ lọc • 7 chiến dịch",
        date: "Tháng 7 18 – Tháng 8 16, 2026",
        name: "FEC Explorer — Trại Hè Quốc Tế 6 Quốc Gia",
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
        labels: ["18/7", "22/7", "26/7", "30/7", "3/8", "7/8", "11/8", "16/8"],
        values: [560000, 680000, 720000, 590000, 610000, 640000, 710000, 580000],
        tooltipTitle: "Thứ 5, 30 thg 7, 2026"
      },
      visa: {
        title: "Tập đoàn Định cư GBlueSea",
        subtitle: "3 bộ lọc • 6 chiến dịch",
        date: "01/10/2026 – 31/10/2026",
        name: "GGSearch_DinhCu_EB5_My_ToanQuoc",
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
        labels: ["Tuần 1", "Tuần 2", "Tuần 3", "Tuần 4"],
        values: [8400000, 9200000, 8900000, 8350000],
        tooltipTitle: "Tuần 2, Tháng 10 2026"
      }
    };

    let activeKey = 'lachongvien';
    let chartObj = null;

    document.addEventListener("DOMContentLoaded", function() {
      applyData(activeKey);
    });

    function toggleSidebar() {
      const sidebar = document.getElementById("tier2Sidebar");
      sidebar.classList.toggle("collapsed");
      const icon = document.getElementById("collapseIcon");
      icon.innerText = sidebar.classList.contains("collapsed") ? "chevron_right" : "chevron_left";
    }

    function toggleAccountModal() {
      const modal = document.getElementById("accountModal");
      modal.style.display = modal.style.display === "none" ? "block" : "none";
    }

    function switchAccount(key) {
      activeKey = key;
      document.getElementById("accountModal").style.display = "none";
      applyData(key);
      showActionToast(`Đã chuyển sang tài khoản: ${DATA_CONFIG[key].title}`);
    }

    function applyData(key) {
      const d = DATA_CONFIG[key];

      document.getElementById("topAccountTitle").innerText = d.title;
      document.getElementById("topAccountSubtitle").innerText = d.subtitle;
      document.getElementById("dateDisplayLabel").innerText = d.date;

      document.getElementById("cName").innerText = d.name;
      document.getElementById("cBudget").innerText = d.budget;
      document.getElementById("cCost").innerText = d.cost;
      document.getElementById("cImp").innerText = d.imp;
      document.getElementById("cClicks").innerText = d.clicks;
      document.getElementById("cAvgCpc").innerText = d.avgCpc;
      document.getElementById("cCtr").innerText = d.ctr;
      document.getElementById("cOptScore").innerText = d.optScore;
      document.getElementById("cConv").innerText = d.conv;
      document.getElementById("cCpa").innerText = d.cpa;
      document.getElementById("cCvr").innerText = d.cvr;

      document.getElementById("tCost").innerText = d.cost;
      document.getElementById("tImp").innerText = d.imp;
      document.getElementById("tClicks").innerText = d.clicks;
      document.getElementById("tAvgCpc").innerText = d.avgCpc;
      document.getElementById("tCtr").innerText = d.ctr;
      document.getElementById("tConv").innerText = d.conv;
      document.getElementById("tCpa").innerText = d.cpa;
      document.getElementById("tCvr").innerText = d.cvr;

      renderChart(d);
    }

    function renderChart(d) {
      const ctx = document.getElementById("googleAdsCanvas").getContext("2d");
      if (chartObj) chartObj.destroy();

      chartObj = new Chart(ctx, {
        type: 'line',
        data: {
          labels: d.labels,
          datasets: [{
            data: d.values,
            borderColor: '#1a73e8',
            borderWidth: 1.8,
            pointRadius: 2.5,
            pointHoverRadius: 5,
            pointBackgroundColor: '#1a73e8',
            pointBorderColor: '#ffffff',
            pointBorderWidth: 1,
            tension: 0.3,
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
              bodyColor: '#202124',
              borderColor: '#dadce0',
              borderWidth: 1,
              titleFont: { family: 'Google Sans', size: 12, weight: '500' },
              bodyFont: { family: 'Google Sans', size: 15, weight: '700' },
              padding: 10,
              cornerRadius: 6,
              displayColors: false,
              callbacks: {
                title: function(items) {
                  return items[0].dataIndex === 2 ? d.tooltipTitle : items[0].label;
                },
                label: function(item) {
                  return `Chi phí\\n- ${item.parsed.y.toLocaleString('vi-VN')} đ`;
                }
              }
            }
          },
          scales: {
            x: {
              grid: { display: false },
              ticks: {
                color: '#5f6368',
                font: { family: 'Roboto', size: 11 },
                maxTicksLimit: 2,
                callback: function(val, index) {
                  if (index === 0) return d.labels[0];
                  if (index === d.labels.length - 1) return d.labels[d.labels.length - 1];
                  return '';
                }
              }
            },
            y: {
              grid: { color: '#f1f3f4', drawBorder: false },
              ticks: {
                color: '#5f6368',
                font: { family: 'Roboto', size: 11 },
                stepSize: 200000,
                callback: function(val) {
                  return val === 0 ? '0 đ' : val.toLocaleString('vi-VN') + ' đ';
                }
              }
            }
          }
        }
      });
    }

    function toggleChartHeight() {
      const box = document.getElementById("chartBox");
      if (box.style.height === "320px") {
        box.style.height = "190px";
      } else {
        box.style.height = "320px";
      }
      chartObj.resize();
    }

    function refreshData() {
      const icon = document.getElementById("refreshIcon");
      icon.style.animation = "spin 0.6s linear";
      setTimeout(() => {
        icon.style.animation = "none";
        applyData(activeKey);
        showActionToast("Đã đồng bộ dữ liệu mới nhất");
      }, 600);
    }

    function showActionToast(msg) {
      const toast = document.getElementById("gToast");
      document.getElementById("gToastMsg").innerText = msg;
      toast.style.display = "block";
      setTimeout(() => { toast.style.display = "none"; }, 2500);
    }

    function exportToExcel() {
      const d = DATA_CONFIG[activeKey];
      const wb = XLSX.utils.book_new();
      const ws = XLSX.utils.json_to_sheet([{
        "Chiến dịch": d.name,
        "Ngân sách": d.budget,
        "Chi phí": d.cost,
        "Lượt hiển thị": d.imp,
        "Lần nhấp": d.clicks,
        "CPC Tr.bình": d.avgCpc,
        "CTR": d.ctr,
        "Điểm tối ưu": d.optScore,
        "Lượt chuyển đổi": d.conv,
        "CPA": d.cpa,
        "CVR": d.cvr
      }]);
      XLSX.utils.book_append_sheet(wb, ws, "Google_Ads_Report");
      XLSX.writeFile(wb, `Bao_Cao_${activeKey}.xlsx`);
      showActionToast("Đã xuất file Excel (.xlsx) chuẩn doanh nghiệp");
    }
  </script>
</body>
</html>
'''

with open("Google_Ads_Dashboard_Chuyen_Doi.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("Saved exact Google Ads replica to Google_Ads_Dashboard_Chuyen_Doi.html")
