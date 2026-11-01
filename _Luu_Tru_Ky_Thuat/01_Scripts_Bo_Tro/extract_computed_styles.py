import json
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

profile_dir = Path(r"C:\Users\ADMIN\.google_ads_automation_profile")
out_json = Path(r"_Luu_Tru_Ky_Thuat\03_Du_Lieu_Tam_Va_Test\real_google_ads_computed_styles.json")

script = """
(() => {
    function getStyles(el) {
        if (!el) return null;
        const cs = window.getComputedStyle(el);
        return {
            tagName: el.tagName,
            className: el.className,
            fontFamily: cs.fontFamily,
            fontSize: cs.fontSize,
            fontWeight: cs.fontWeight,
            lineHeight: cs.lineHeight,
            color: cs.color,
            backgroundColor: cs.backgroundColor,
            borderColor: cs.borderColor,
            borderBottom: cs.borderBottom,
            borderRadius: cs.borderRadius,
            padding: cs.padding,
            margin: cs.margin,
            boxShadow: cs.boxShadow,
            height: cs.height,
            width: cs.width
        };
    }

    const report = {
        body: getStyles(document.body),
        appBar: getStyles(document.querySelector('awsm-app-bar, [role="banner"], header')),
        logoContainer: getStyles(document.querySelector('app-bar-logo-container, .logo-container')),
        leftRail: getStyles(document.querySelector('awsm-app-menus, .app-menus, nav, aside')),
        leftRailItem: getStyles(document.querySelector('awsm-app-menus material-button, nav a, .navigation-item')),
        tier2Sidebar: getStyles(document.querySelector('.sub-nav, .secondary-nav, [role="navigation"]')),
        activeTab: getStyles(document.querySelector('.selected-tab, [aria-selected="true"], .active-tab')),
        chartContainer: getStyles(document.querySelector('aplos-time-series-chart, .chart-container')),
        tableHeader: getStyles(document.querySelector('aw-header-cell, th, .header-cell')),
        tableRow: getStyles(document.querySelector('tr, .particle-table-row')),
        draftNoticeRow: getStyles(document.querySelector('.draft-row, [style*="background"]')),
        dateRangeBtn: getStyles(document.querySelector('.date-picker, [aria-label*="ngày"], [aria-label*="date"]'))
    };

    return report;
})()
"""

with sync_playwright() as p:
    try:
        browser = p.chromium.launch_persistent_context(
            user_data_dir=str(profile_dir),
            headless=True,
            channel="chrome",
            args=["--start-maximized", "--no-sandbox"]
        )
        page = browser.pages[0] if browser.pages else browser.new_page()
        page.goto("https://ads.google.com/aw/campaigns", timeout=45000, wait_until="networkidle")
        
        styles = page.evaluate(script)
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(styles, f, indent=2, ensure_ascii=False)
        print("Computed styles saved to:", out_json)
        browser.close()
    except Exception as e:
        print("Error:", e)
