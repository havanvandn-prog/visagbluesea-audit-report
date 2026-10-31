import sys
import os
import json
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

os.makedirs("Bang_Chung_Hinh_Anh", exist_ok=True)
os.makedirs("_Luu_Tru_Ky_Thuat/02_Screenshots_Debug_Va_Khao_Sat", exist_ok=True)

TARGET_PAGES = [
    {"name": "homepage", "url": "https://www.visagbluesea.com"},
    {"name": "eb5", "url": "https://www.visagbluesea.com/us-green-card-eb-5"},
    {"name": "golden_visa", "url": "https://www.visagbluesea.com/eu-golden-visa"},
    {"name": "study_au", "url": "https://www.visagbluesea.com/study-in-australia"},
    {"name": "contact", "url": "https://www.visagbluesea.com/contact-us"},
    {"name": "cloned_malta", "url": "https://www.visagbluesea.com/copy-of-malta-investment-visa-1"}
]

print("Starting browser...", flush=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    # 1. Desktop Context
    desktop_context = browser.new_context(
        viewport={"width": 1440, "height": 900},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    )
    desktop_page = desktop_context.new_page()

    # 2. Mobile Context (iPhone 14 / 390x844)
    mobile_context = browser.new_context(
        viewport={"width": 390, "height": 844},
        is_mobile=True,
        has_touch=True,
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    )
    mobile_page = mobile_context.new_page()

    page_data = {}

    for item in TARGET_PAGES:
        name = item["name"]
        url = item["url"]
        print(f"\nProcessing {name}: {url}", flush=True)
        
        # Desktop
        try:
            desktop_page.goto(url, wait_until="domcontentloaded", timeout=25000)
            desktop_page.wait_for_timeout(4000) # wait for Wix JS to render
            
            # Viewport screenshot
            desktop_shot = f"Bang_Chung_Hinh_Anh/desktop_{name}_view.png"
            desktop_page.screenshot(path=desktop_shot)
            print(f"  -> Saved {desktop_shot}", flush=True)
            
            # Fullpage screenshot
            desktop_full = f"_Luu_Tru_Ky_Thuat/02_Screenshots_Debug_Va_Khao_Sat/desktop_{name}_full.png"
            desktop_page.screenshot(path=desktop_full, full_page=True)
            print(f"  -> Saved {desktop_full}", flush=True)
            
            # Extract info
            info = desktop_page.evaluate('''() => {
                const h1s = Array.from(document.querySelectorAll('h1')).map(e => e.innerText.trim());
                const h2s = Array.from(document.querySelectorAll('h2')).map(e => e.innerText.trim());
                const forms = Array.from(document.querySelectorAll('form')).map(f => ({
                    action: f.action,
                    inputs: Array.from(f.querySelectorAll('input, select, textarea')).map(i => i.placeholder || i.name || i.type)
                }));
                const ctas = Array.from(document.querySelectorAll('button, a.button, a[role="button"], a[href^="tel:"], a[href*="zalo"]')).map(c => ({
                    text: c.innerText.trim(),
                    href: c.getAttribute('href') || '',
                    tag: c.tagName
                })).filter(c => c.text.length > 0 || c.href.length > 0);
                
                return {
                    title: document.title,
                    h1s,
                    h2s,
                    forms,
                    ctas: ctas.slice(0, 20),
                    bodyLength: document.body.innerText.length
                };
            }''')
            page_data[name] = info
            print(f"  Title: {info['title']}", flush=True)
            print(f"  H1s: {info['h1s']}", flush=True)
            print(f"  Forms: {len(info['forms'])}", flush=True)
            print(f"  CTAs: {len(info['ctas'])}", flush=True)
            
        except Exception as e:
            print(f"  Desktop Error on {url}: {e}", flush=True)

        # Mobile
        try:
            mobile_page.goto(url, wait_until="domcontentloaded", timeout=25000)
            mobile_page.wait_for_timeout(3500)
            
            mobile_shot = f"Bang_Chung_Hinh_Anh/mobile_{name}_view.png"
            mobile_page.screenshot(path=mobile_shot)
            print(f"  -> Saved {mobile_shot}", flush=True)
            
            mobile_full = f"_Luu_Tru_Ky_Thuat/02_Screenshots_Debug_Va_Khao_Sat/mobile_{name}_full.png"
            mobile_page.screenshot(path=mobile_full, full_page=True)
            print(f"  -> Saved {mobile_full}", flush=True)
            
        except Exception as e:
            print(f"  Mobile Error on {url}: {e}", flush=True)

    # Inspect mobile navigation & floating buttons specifically on homepage
    try:
        print("\nInspecting mobile menu...", flush=True)
        mobile_page.goto("https://www.visagbluesea.com", wait_until="domcontentloaded", timeout=25000)
        mobile_page.wait_for_timeout(3500)
        
        # Click mobile hamburger menu
        menu_btn = mobile_page.locator('button[aria-label*="menu" i], [data-hook="mobile-nav-toggle"], [data-testid="toggle-button"], button:has(svg)').first
        if menu_btn.is_visible():
            menu_btn.click()
            mobile_page.wait_for_timeout(1500)
            mobile_menu_shot = "Bang_Chung_Hinh_Anh/mobile_homepage_menu_open.png"
            mobile_page.screenshot(path=mobile_menu_shot)
            print(f"  -> Saved {mobile_menu_shot}", flush=True)
    except Exception as e:
        print(f"  Mobile menu click error: {e}", flush=True)

    browser.close()

with open('_Luu_Tru_Ky_Thuat/03_Du_Lieu_Tam_Va_Test/rendered_page_data.json', 'w', encoding='utf-8') as f:
    json.dump(page_data, f, ensure_ascii=False, indent=2)

print("\nHoàn tất bóc tách dữ liệu và chụp ảnh màn hình!", flush=True)
