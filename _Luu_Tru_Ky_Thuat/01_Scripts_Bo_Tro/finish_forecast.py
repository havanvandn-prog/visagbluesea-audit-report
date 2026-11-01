import sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    page = browser.contexts[0].pages[0]
    
    print('Current URL:', page.url)
    
    # 1. Location handling
    loc_btn = page.locator('div[role="button"]:has(i:has-text("location_on")), div:has(i:has-text("location_on"))').last
    loc_text = loc_btn.inner_text().strip().replace('\n', ' ')
    print('Current location pill:', loc_text)
    
    if "Việt Nam" in loc_text or "Hồ Chí Minh" not in loc_text:
        print('Setting target location to Hồ Chí Minh only...')
        loc_btn.click()
        time.sleep(2)
        modal = page.locator('.modal.visible').first
        if modal.is_visible():
            search_box = modal.locator('input').first
            search_box.fill("Hồ Chí Minh")
            time.sleep(2)
            target_btn = page.locator('material-button:has-text("Bao gồm"), button:has-text("Bao gồm")').first
            if target_btn.is_visible():
                print('Clicking Bao gồm...')
                target_btn.click()
                time.sleep(1.5)
            # Remove Việt Nam nếu có
            vn_remove = modal.locator('tr:has-text("Việt Nam quốc gia") i[aria-label*="Xóa"], tr:has-text("Việt Nam quốc gia") material-icon:has-text("cancel")').first
            if vn_remove.is_visible():
                print('Removing Việt Nam...')
                vn_remove.click()
                time.sleep(1.5)
            # Click Lưu
            save_btn = modal.locator('material-button:has-text("Lưu"), button:has-text("Lưu")').first
            print('Clicking Lưu...')
            save_btn.click()
            time.sleep(4)
            
            loc_btn_after = page.locator('div[role="button"]:has(i:has-text("location_on")), div:has(i:has-text("location_on"))').last
            print('Location pill after save:', loc_btn_after.inner_text().strip().replace('\n', ' '))

    # 2. Download historical metrics file
    print('📥 Finding Download button...')
    dl_btn = page.locator('material-button:has(material-icon:has-text("file_download"))').first
    dl_btn.click()
    time.sleep(2)
    
    fmt_item = page.locator('material-select-item:has-text(".csv")').first
    target_file = Path("_Luu_Tru_Ky_Thuat/Keyword_Planner_Raw/Historical_Metrics_HCM.csv")
    
    print('Clicking .csv with expect_download...')
    with page.expect_download(timeout=60000) as dl_info:
        fmt_item.click()
        
    dl = dl_info.value
    dl.save_as(str(target_file))
    print(f'🎉 Tải thành công Số liệu lịch sử HCM -> {target_file} (Size: {target_file.stat().st_size} bytes)')
