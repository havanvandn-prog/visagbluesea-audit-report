import sys
import time
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

html_file = Path("Google_Ads_Dashboard_Chuyen_Doi.html").resolve()
clone_shot = Path(r"_Luu_Tru_Ky_Thuat\02_Screenshots_Debug_Va_Khao_Sat\clone_screenshot.png")
target_shot = Path(r"C:\Users\ADMIN\.gemini\antigravity\brain\38c1b87a-0391-4409-94c9-3e9563c23cb2\.user_uploaded\media_1793516369190_2addd489.png")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.goto(html_file.as_uri())
    time.sleep(2)
    page.screenshot(path=str(clone_shot))
    browser.close()

print(f"Clone screenshot saved to: {clone_shot}")

# Compare dimensions
im_clone = Image.open(clone_shot)
im_target = Image.open(target_shot)
print(f"Clone size: {im_clone.size}, Target size: {im_target.size}")
