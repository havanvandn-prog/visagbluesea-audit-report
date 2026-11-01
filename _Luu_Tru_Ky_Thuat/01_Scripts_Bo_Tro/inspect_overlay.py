import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')
with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    page = browser.contexts[0].pages[0]
    for el in page.locator('div[role="button"]').all():
        if el.is_visible():
            txt = el.inner_text().strip().replace('\n', ' ')
            if 'location_on' in txt:
                print('Location button:', txt)
