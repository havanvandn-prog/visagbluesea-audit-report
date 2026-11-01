import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

profile_dir = Path(r"C:\Users\ADMIN\.google_ads_automation_profile")
out_screenshot = Path(r"_Luu_Tru_Ky_Thuat\02_Screenshots_Debug_Va_Khao_Sat\google_ads_campaigns_real.png")
out_screenshot.parent.mkdir(parents=True, exist_ok=True)
out_dom = Path(r"_Luu_Tru_Ky_Thuat\03_Du_Lieu_Tam_Va_Test\real_google_ads_dom.html")
out_dom.parent.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    try:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=str(profile_dir),
            headless=True,
            channel="chrome",
            args=["--start-maximized", "--no-sandbox"]
        )
        page = browser.pages[0] if browser.pages else browser.new_page()
        page.set_viewport_size({"width": 1920, "height": 1080})
        
        print("Navigating to https://ads.google.com/aw/campaigns...")
        page.goto("https://ads.google.com/aw/campaigns", timeout=45000, wait_until="domcontentloaded")
        time.sleep(5)
        print("Current URL:", page.url)
        
        if "selectaccount" in page.url:
            print("Selecting account...")
            page.wait_for_selector("material-list-item, [role='link'], tr.account-row, a[href*='aw/campaigns']", timeout=10000)
            account_btn = page.query_selector("material-list-item, [role='link'], tr.account-row, a[href*='aw/campaigns']")
            if account_btn:
                account_btn.click()
                print("Clicked account. Waiting for campaigns page to load...")
                time.sleep(12)
        
        print("URL after load:", page.url)
        print("Page Title:", page.title())
        page.screenshot(path=str(out_screenshot), full_page=False)
        print("Screenshot saved to:", out_screenshot)
        
        with open(out_dom, "w", encoding="utf-8") as f:
            f.write(page.content())
        print(f"DOM dumped to {out_dom}")
        
        browser.close()
    except Exception as e:
        print("Error:", e)

