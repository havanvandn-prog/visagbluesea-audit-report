import sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    page = browser.contexts[0].pages[0]
    
    csv_item = page.locator('material-select-item:has-text(".csv")').first
    target_file = Path("_Luu_Tru_Ky_Thuat/Keyword_Planner_Raw/test_group_01.csv")
    target_file.parent.mkdir(parents=True, exist_ok=True)
    
    print('Clicking .csv with expect_download...')
    with page.expect_download(timeout=30000) as dl_info:
        csv_item.click()
    
    dl = dl_info.value
    dl.save_as(str(target_file))
    print('Download saved to:', target_file, 'Size:', target_file.stat().st_size)
