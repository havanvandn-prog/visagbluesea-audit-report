import sys, time
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    page = browser.contexts[0].pages[0]
    
    # 1. Click location pill
    loc_btn = page.locator('div[role="button"]:has-text("location_on")').first
    print('Clicking location pill...')
    loc_btn.click()
    time.sleep(2)
    
    modal = page.locator('.modal.visible').first
    print('Modal open:', modal.is_visible())
    
    # 2. Type Hồ Chí Minh
    inp = modal.locator('input').first
    inp.fill("Hồ Chí Minh")
    time.sleep(2)
    
    # 3. Click 'Mục tiêu' / 'Bao gồm'
    target_btn = page.locator('material-button:has-text("Bao gồm"), button:has-text("Bao gồm"), [role="button"]:has-text("Bao gồm")').first
    if target_btn.is_visible():
        print('Clicking Bao gồm for Hồ Chí Minh...')
        target_btn.click()
        time.sleep(1.5)
    else:
        print('Target button not visible!')
        
    # 4. Remove Việt Nam
    vn_remove = modal.locator('tr:has-text("Việt Nam quốc gia") i[aria-label*="Xóa"], tr:has-text("Việt Nam quốc gia") material-icon:has-text("cancel")').first
    if vn_remove.is_visible():
        print('Clicking remove VN...')
        vn_remove.click()
        time.sleep(1.5)
    else:
        print('VN remove button not visible!')
        
    # 5. Click Lưu
    save_btn = modal.locator('material-button:has-text("Lưu"), button:has-text("Lưu")').first
    print('Clicking Lưu...')
    save_btn.click()
    time.sleep(4)
    
    loc_btn_after = page.locator('div[role="button"]:has-text("location_on")').first
    print('Location pill after save:', loc_btn_after.inner_text().strip().replace('\n', ' '))
