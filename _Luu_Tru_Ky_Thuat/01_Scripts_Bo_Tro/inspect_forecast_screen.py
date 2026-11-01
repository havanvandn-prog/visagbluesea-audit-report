import sys, time
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    page = browser.contexts[0].pages[0]
    
    print('Current page title:', page.title())
    print('Current URL:', page.url)
    
    # Check all buttons
    btns = page.locator('button, material-button, div[role="button"]')
    print('Button count:', btns.count())
    for i in range(btns.count()):
        btn = btns.nth(i)
        if btn.is_visible():
            txt = btn.inner_text().strip().replace('\n', ' ')
            if txt:
                print(f'{i}: tag={btn.evaluate("el => el.tagName")}, text={txt}')
