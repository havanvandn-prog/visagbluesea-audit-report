import sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    page = browser.contexts[0].pages[0]
    
    # Click download icon if popup is not open
    popup = page.locator('*:has-text("Chỉ số trước đây của kế hoạch")').first
    if not popup.is_visible():
        btn = page.locator('material-button[aria-label="Tệp tải xuống của kế hoạch"]').first
        btn.click()
        time.sleep(1.5)
        
    csv_items = page.locator('material-select-item:has-text(".csv")').all()
    print('CSV items count:', len(csv_items))
    
    # The second .csv is "Chỉ số trước đây của kế hoạch"
    hist_csv = csv_items[1]
    target_file = Path("_Luu_Tru_Ky_Thuat/Keyword_Planner_Raw/Historical_Metrics_HCM_Real.csv")
    
    print('Clicking second .csv (Chỉ số trước đây của kế hoạch)...')
    with page.expect_download(timeout=60000) as dl_info:
        hist_csv.click()
        
    dl = dl_info.value
    dl.save_as(str(target_file))
    print(f'🎉 TẢI THÀNH CÔNG: {target_file} (Size: {target_file.stat().st_size} bytes)')
