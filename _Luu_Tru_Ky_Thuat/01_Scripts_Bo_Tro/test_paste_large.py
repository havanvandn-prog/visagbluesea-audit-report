import sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

sys.path.append(r'C:\Users\ADMIN\.gemini\config\skills\download-keyword-planner (ggads)\scripts')
from auto_keyword_planner import parse_keyword_planner_file, normalize_keyword

sys.stdout.reconfigure(encoding='utf-8')

# Read deduplicated keywords
staging_dir = Path('_Luu_Tru_Ky_Thuat/Keyword_Planner_Raw')
files = sorted(list(staging_dir.glob('Raw_*.csv')))
seen = set()
unique_kws = []
for p in files:
    rows = parse_keyword_planner_file(p)
    for r in rows:
        kw = r.get('Keyword')
        if kw:
            n = normalize_keyword(kw)
            if n and n not in seen:
                seen.add(n)
                unique_kws.append(kw)

print(f'Total unique keywords to paste: {len(unique_kws)}')

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:9222')
    page = browser.contexts[0].pages[0]
    
    # Check textarea
    tx = page.locator('textarea').first
    if not tx.is_visible():
        btn = page.get_by_text("Nhận thông tin dự đoán", exact=False).first
        if btn.is_visible():
            btn.click(force=True)
            time.sleep(2)
            
    print('Textarea is visible:', tx.is_visible())
    
    # Set value using evaluate
    kw_text = "\n".join(unique_kws)
    print(f'Setting {len(unique_kws)} keywords via JS evaluate ({len(kw_text)} chars)...')
    tx.evaluate('(el, val) => { el.value = val; el.dispatchEvent(new Event("input", { bubbles: true })); el.dispatchEvent(new Event("change", { bubbles: true })); }', kw_text)
    time.sleep(2)
    print('Textarea value length:', len(tx.input_value()))
    
    # Find start button
    start_btn = page.locator('material-button:has-text("B\\u0103\\u0301t \\u0111\\u00e2\\u0300u"), material-button:has-text("Bắt đầu"), button:has-text("Bắt đầu")').first
    if not start_btn.is_visible():
        for i in range(page.locator('material-button').count()):
            mb = page.locator('material-button').nth(i)
            if mb.is_visible() and 'Bắt đầu' in mb.evaluate('el => el.textContent.normalize("NFC")'):
                start_btn = mb
                break
                
    print('Start button visible:', start_btn.is_visible(), 'text:', start_btn.inner_text().strip())
    start_btn.click(force=True)
    time.sleep(8)
    print('Navigated URL:', page.url)
