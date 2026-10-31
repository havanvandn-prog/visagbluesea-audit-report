import sys
import os
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

os.makedirs("Bang_Chung_Hinh_Anh", exist_ok=True)

html_content = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
  body { background: #0f172a; padding: 24px; display: flex; gap: 20px; justify-content: center; align-items: flex-start; }
  .panel { width: 520px; background: #ffffff; border-radius: 12px; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.5); overflow: hidden; border: 1px solid #e2e8f0; }
  .header { background: #1e293b; color: #fff; padding: 14px 18px; display: flex; align-items: center; justify-content: space-between; }
  .header-left { display: flex; align-items: center; gap: 10px; }
  .logo-badge { background: #01a915; color: #fff; font-weight: 800; font-size: 13px; padding: 4px 8px; border-radius: 6px; }
  .title { font-size: 15px; font-weight: 700; color: #f8fafc; }
  .tabs { display: flex; background: #f1f5f9; border-bottom: 1px solid #cbd5e1; font-size: 13px; font-weight: 600; }
  .tab { padding: 10px 16px; cursor: pointer; color: #64748b; }
  .tab.active { color: #01a915; border-bottom: 2px solid #01a915; background: #fff; }
  .content { padding: 16px; font-size: 13px; }
  .row { margin-bottom: 14px; }
  .label { font-weight: 700; color: #334155; margin-bottom: 4px; display: flex; justify-content: space-between; align-items: center; }
  .badge-red { background: #fee2e2; color: #b91c1c; font-size: 11px; padding: 2px 7px; border-radius: 4px; font-weight: 700; }
  .badge-yellow { background: #fef3c7; color: #b45309; font-size: 11px; padding: 2px 7px; border-radius: 4px; font-weight: 700; }
  .badge-green { background: #dcfce7; color: #15803d; font-size: 11px; padding: 2px 7px; border-radius: 4px; font-weight: 700; }
  .val-box { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 8px 10px; color: #0f172a; word-break: break-word; line-height: 1.45; }
  .val-box.error { border-color: #fca5a5; background: #fff5f5; }
  .val-box.warning { border-color: #fde68a; background: #fffbeb; }
  .item-list { list-style: none; margin-top: 4px; }
  .item-list li { padding: 6px 8px; background: #fff; border: 1px solid #e2e8f0; border-radius: 4px; margin-bottom: 6px; font-size: 12px; }
  .item-list li.err { border-left: 4px solid #ef4444; background: #fef2f2; }
</style>
</head>
<body>

<!-- Panel 1: Homepage Detailed SEO Audit -->
<div class="panel">
  <div class="header">
    <div class="header-left">
      <span class="logo-badge">SEO PRO</span>
      <span class="title">Detailed SEO Extension Audit • Trang Chủ</span>
    </div>
    <span style="font-size: 11px; color: #94a3b8;">visagbluesea.com</span>
  </div>
  <div class="tabs">
    <div class="tab">Overview</div>
    <div class="tab active">Headings (Thẻ Tiêu Đề)</div>
    <div class="tab">Schema</div>
    <div class="tab">Links & Media</div>
  </div>
  <div class="content">
    <div class="row">
      <div class="label">
        <span>URL Hiện Tại</span>
        <span class="badge-green">HTTP 200 OK</span>
      </div>
      <div class="val-box">https://www.visagbluesea.com/</div>
    </div>
    <div class="row">
      <div class="label">
        <span>Title Tag (25 ký tự)</span>
        <span class="badge-yellow">CẢNH BÁO: QUÁ NGẮN & THIẾU TỪ KHÓA</span>
      </div>
      <div class="val-box warning">Trang Chủ | Visa GBlueSea</div>
    </div>
    <div class="row">
      <div class="label">
        <span>Meta Description (248 ký tự)</span>
        <span class="badge-red">LỖI: QUÁ DÀI (BỊ GOOGLE CẮT CỤT)</span>
      </div>
      <div class="val-box error">Tập đoàn GBlueSea là một trong những tổ chức tư vấn định cư, du học, visa uy tín nhất trên thế giới với các chi nhánh tại Mỹ, Anh, Hy Lạp, Phần Lan, Việt Nam... (248 chars > 160 chars)</div>
    </div>
    <div class="row">
      <div class="label">
        <span>Cấu Trúc Thẻ H1 (Số lượng: 2)</span>
        <span class="badge-red">LỖI NGHIÊM TRỌNG: 2 THẺ H1</span>
      </div>
      <ul class="item-list">
        <li class="err"><b>H1 [1]:</b> "Các dịch vụ nổi bật" <span style="color:#ef4444; font-size:11px;">(Chung chung, không có từ khóa định vị)</span></li>
        <li class="err"><b>H1 [2]:</b> "Vui lòng liên hệ với GBlueSea để được hướng dẫn chuyên nghiệp và hỗ trợ cá nhân. Chúng tôi cam kết..." <span style="color:#ef4444; font-size:11px;">(Đoạn văn bản 4 dòng bị gán nhầm thẻ H1!)</span></li>
      </ul>
    </div>
    <div class="row">
      <div class="label">
        <span>Thẻ H2 Bất Thường Phát Hiện</span>
        <span class="badge-red">LỖI TEMPLATE DỞ DANG</span>
      </div>
      <ul class="item-list">
        <li class="err"><b>H2:</b> "CAPS TITLE" <span style="color:#ef4444; font-size:11px;">(Văn bản mẫu template Wix chưa được thay thế!)</span></li>
        <li class="err"><b>H2:</b> "17       5347      235" <span style="color:#ef4444; font-size:11px;">(Số liệu thô dính chùm, thiếu đơn vị đo lường)</span></li>
      </ul>
    </div>
  </div>
</div>

<!-- Panel 2: Landing Pages & Cloned Pages Audit -->
<div class="panel">
  <div class="header">
    <div class="header-left">
      <span class="logo-badge" style="background:#dc2626;">ALERT</span>
      <span class="title">Bằng Chứng Lỗi Landing Page & URL Rác</span>
    </div>
    <span style="font-size: 11px; color: #94a3b8;">Landing Pages</span>
  </div>
  <div class="tabs">
    <div class="tab active">Trang Đích Google Ads</div>
    <div class="tab">URL Nhân Bản Rác</div>
    <div class="tab">Tracking & Schema</div>
  </div>
  <div class="content">
    <div class="row">
      <div class="label">
        <span>Trang Định Cư Mỹ EB-5 (/us-green-card-eb-5)</span>
        <span class="badge-red">LỖI LỘ TIẾNG TÂY BAN NHA</span>
      </div>
      <div class="val-box error">
        <b>Thẻ H1:</b> "Acerca de" (Nghĩa tiếng Tây Ban Nha là "Giới thiệu" - Lỗi template Wix còn sót trên trang định cư triệu đô!)
      </div>
    </div>
    <div class="row">
      <div class="label">
        <span>Trang Định Cư Golden Visa (/eu-golden-visa)</span>
        <span class="badge-red">LỖI: HOÀN TOÀN KHÔNG CÓ THẺ H1</span>
      </div>
      <div class="val-box error">
        <b>Thẻ H1:</b> [Không tìm thấy] — Điểm chất lượng Google Ads (Ad Relevance) bị kéo sụt nghiêm trọng do thiếu tiêu đề định vị.
      </div>
    </div>
    <div class="row">
      <div class="label">
        <span>Trang Clone Rác Lọt Vào Sitemap (/copy-of-malta-investment-visa-1)</span>
        <span class="badge-red">LỖI CANNIBALIZATION & RÁC WIX</span>
      </div>
      <div class="val-box error">
        <b>URL:</b> /copy-of-malta-investment-visa-1<br>
        <b>Title:</b> "Các Khóa Học | GBlueSea" (Nội dung khóa học nhưng URL là Malta Visa!)<br>
        <b>H1:</b> "Acerca de"
      </div>
    </div>
    <div class="row">
      <div class="label">
        <span>Đo Lường Chuyển Đổi (Tracking Google Ads)</span>
        <span class="badge-red">MẤT DẤU DỮ LIỆU ĐƠN HÀNG</span>
      </div>
      <div class="val-box error">
        <b>GTM:</b> Đã cài nhưng CHƯA cấu hình Google Ads Conversion Tag cho Form gửi lead.<br>
        <b>Hotline & Zalo:</b> Chưa gắn sự kiện Click-to-Call / Click-to-Zalo đo lường chuyển đổi trả phí.
      </div>
    </div>
  </div>
</div>

</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1120, "height": 680})
    page.set_content(html_content)
    page.wait_for_timeout(1000)
    out_path = "Bang_Chung_Hinh_Anh/bang_chung_detailed_seo_panel.png"
    page.screenshot(path=out_path)
    print(f"Saved {out_path}")
    browser.close()
