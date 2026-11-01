import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    page = browser.contexts[0].pages[0]
    print('Current page title:', page.title())
    print('Current URL:', page.url)
    
    # Check visible texts on the page
    for el in page.locator('material-button, button, div[role="alert"], .error, .toast').all():
        if el.is_visible():
            t = el.inner_text().strip().replace('\n', ' ')
            if t:
                print('Elem:', el.evaluate('el => el.tagName'), 'text=', t[:80])
