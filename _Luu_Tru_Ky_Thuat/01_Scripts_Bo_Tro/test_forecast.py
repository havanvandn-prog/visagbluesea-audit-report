import sys, time
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    page = browser.contexts[0].pages[0]
    
    # Click start button with both decomposed and precomposed
    btn = page.locator('material-button:has-text("B\\u0103\\u0301t \\u0111\\u00e2\\u0300u"), material-button:has-text("Bắt đầu"), material-button:has-text("Get started")').first
    if not btn.is_visible():
        # Fallback to finding by javascript textContent NFC
        print('Trying JS NFC match...')
        for i in range(page.locator('material-button').count()):
            mb = page.locator('material-button').nth(i)
            if mb.is_visible() and 'Bắt đầu' in mb.evaluate('el => el.textContent.normalize("NFC")'):
                btn = mb
                break
                
    print('Found button:', btn.is_visible())
    btn.click()
    time.sleep(6)
    print('URL after click:', page.url)
    
    # Check tabs on the forecast page
    tabs = page.locator('material-tab-header, div[role="tab"], button, div')
    for i in range(tabs.count()):
        el = tabs.nth(i)
        if el.is_visible():
            txt = el.inner_text().strip().replace('\n', ' ')
            if any(k in txt.lower() for k in ['dự đoán', 'lịch sử', 'trước đây', 'historical', 'việt nam', 'hồ chí minh']):
                print(f'Tab/Pill {i}: tag={el.evaluate("el => el.tagName")}, text={txt[:60]}')
