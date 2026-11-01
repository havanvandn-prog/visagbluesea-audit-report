import sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    page = browser.contexts[0].pages[0]
    
    # Check download button
    dl_btn = page.locator('material-button:has-text("file_download"), button:has-text("file_download"), material-button[aria-label*="Tải xuống"], material-icon:has-text("file_download")').first
    print('Download button visible:', dl_btn.is_visible())
    dl_btn.click()
    time.sleep(2)
    
    # Check format options
    options = page.locator('material-select-item, [role="menuitem"], div[role="button"]').all()
    print('Options after click dl:')
    for o in options:
        if o.is_visible():
            t = o.inner_text().strip().replace('\n', ' ')
            if any(k in t.lower() for k in ['.csv', 'csv', 'trang tính', 'excel', '.xlsx']):
                print(' - Option:', o.evaluate('el => el.tagName'), 'text=', t)
