import json
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

profile_dir = Path(r"C:\Users\ADMIN\.google_ads_automation_profile")

with sync_playwright() as p:
    try:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=str(profile_dir),
            headless=True,
            channel="chrome",
            args=["--start-maximized", "--no-sandbox"]
        )
        page = browser.pages[0] if browser.pages else browser.new_page()
        page.goto("https://ads.google.com/aw/campaigns", timeout=45000, wait_until="domcontentloaded")
        page.wait_for_selector("ess-table, aplos-time-series-chart, awsm-app-bar", timeout=20000)
        
        info = page.evaluate("""
        (() => {
            function getProps(selector) {
                const el = document.querySelector(selector);
                if (!el) return null;
                const cs = window.getComputedStyle(el);
                return {
                    tag: el.tagName,
                    classes: el.className,
                    bg: cs.backgroundColor,
                    color: cs.color,
                    fontFamily: cs.fontFamily,
                    fontSize: cs.fontSize,
                    fontWeight: cs.fontWeight,
                    lineHeight: cs.lineHeight,
                    height: cs.height,
                    width: cs.width,
                    padding: cs.padding,
                    border: cs.border,
                    borderBottom: cs.borderBottom,
                    boxShadow: cs.boxShadow
                };
            }

            return {
                appBar: getProps('awsm-app-bar'),
                appMenus: getProps('awsm-app-menus'),
                chart: getProps('aplos-time-series-chart'),
                table: getProps('ess-table'),
                headerCell: getProps('ess-table .header-row, ess-table th, ess-table [role="columnheader"]'),
                dataRow: getProps('ess-table [role="row"]:not([role="rowheader"]), ess-table tr'),
                navItemActive: getProps('.navigation-item.active, [aria-selected="true"], .selected')
            };
        })()
        """)
        
        print(json.dumps(info, indent=2, ensure_ascii=False))
        browser.close()
    except Exception as e:
        print("Error:", e)
