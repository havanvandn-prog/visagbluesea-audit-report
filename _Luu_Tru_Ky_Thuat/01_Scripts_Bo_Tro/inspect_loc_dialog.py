import sys, time
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    page = browser.contexts[0].pages[0]
    
    # 1. Click 'Bao gồm' next to Hồ Chí Minh
    target_btn = page.locator('material-button:has-text("Bao gồm"), button:has-text("Bao gồm"), div[role="button"]:has-text("Bao gồm")').first
    if target_btn.is_visible():
        print('Clicking Bao gồm...')
        target_btn.click()
        time.sleep(1)
        
    # 2. Click delete/close on Việt Nam
    # Let's see the targeted locations list in dialog
    # It has 'Việt Nam' with a delete icon next to it
    del_vn = page.locator('div:has-text("Việt Nam") material-button:has(material-icon:has-text("close")), tr:has-text("Việt Nam") material-button').first
    if del_vn.is_visible():
        print('Deleting Việt Nam...')
        del_vn.click()
        time.sleep(1)
    else:
        # Try finding close button next to Việt Nam
        vn_row = page.locator('*:has-text("Việt Nam quốc gia") material-button, *:has-text("Việt Nam") button').first
        if vn_row.is_visible():
            print('Clicking vn_row button...')
            vn_row.click()
            time.sleep(1)
            
    # 3. Click 'Lưu'
    save_btn = page.locator('material-button:has-text("Lưu"), button:has-text("Lưu"), div[role="button"]:has-text("Lưu")').last
    print('Clicking Lưu...')
    save_btn.click()
    time.sleep(4)
    
    print('Dialog saved! Checking location pill on main page...')
    pill = page.locator('div[role="button"]:has-text("location_on"), div:has-text("location_on")').last
    print('Current location pill:', pill.inner_text().strip().replace('\n', ' '))
