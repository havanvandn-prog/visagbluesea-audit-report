import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    page = browser.contexts[0].pages[0]
    print('Current URL:', page.url)
    
    # Check left sidebar and tabs
    for el in page.locator('a, material-list-item, div[role="tab"]').all():
        if el.is_visible():
            t = el.inner_text().strip().replace('\n', ' ')
            href = el.get_attribute('href')
            print('Nav:', t, '| href=', href)
