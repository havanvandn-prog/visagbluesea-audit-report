import sys
import os
import asyncio
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')

VIEWPORTS = [
    {"name": "desktop_1440", "width": 1440, "height": 900},
    {"name": "desktop_1280", "width": 1280, "height": 800},
    {"name": "tablet_land_1024", "width": 1024, "height": 768},
    {"name": "tablet_port_768", "width": 768, "height": 1024},
    {"name": "mobile_large_430", "width": 430, "height": 932},
    {"name": "mobile_std_390", "width": 390, "height": 844},
    {"name": "mobile_small_375", "width": 375, "height": 812},
    {"name": "mobile_android_360", "width": 360, "height": 800},
]

HTML_PATH = os.path.abspath("Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html")
OUTPUT_DIR = os.path.abspath("_Luu_Tru_Ky_Thuat/02_Screenshots_Debug_Va_Khao_Sat")
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def run_audit():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        print("=== BẮT ĐẦU AUDIT RESPONSIVE CHUYÊN SÂU ===")
        print(f"File kiểm tra: {HTML_PATH}")
        
        all_issues = []

        for vp in VIEWPORTS:
            context = await browser.new_context(
                viewport={"width": vp["width"], "height": vp["height"]},
                device_scale_factor=1
            )
            page = await context.new_page()
            await page.goto(f"file:///{HTML_PATH}")
            await page.wait_for_load_state("networkidle")
            # Wait for lucide icons to render
            await page.wait_for_timeout(1000)

            # 1. Kiểm tra Overflow-X
            overflow_check = await page.evaluate('''() => {
                const docWidth = document.documentElement.offsetWidth;
                const windowWidth = window.innerWidth;
                const scrollWidth = document.documentElement.scrollWidth;
                const hasOverflow = scrollWidth > windowWidth;
                
                // Tìm các element vượt quá windowWidth
                const overflowingElements = [];
                const allElements = document.querySelectorAll('*');
                allElements.forEach(el => {
                    const rect = el.getBoundingClientRect();
                    if (rect.right > windowWidth + 1) { // 1px margin
                        overflowingElements.push({
                            tag: el.tagName,
                            id: el.id,
                            class: (el.getAttribute('class') || '').substring(0, 100),
                            rect: { right: Math.round(rect.right), width: Math.round(rect.width) }
                        });
                    }
                });

                return {
                    windowWidth,
                    scrollWidth,
                    hasOverflow,
                    overflowingElements: overflowingElements.slice(0, 5) // lấy top 5
                };
            }''')

            # 2. Kiểm tra Header hiển thị
            header_check = await page.evaluate('''() => {
                const header = document.querySelector('header');
                if (!header) return null;
                const rect = header.getBoundingClientRect();
                return {
                    height: Math.round(rect.height),
                    width: Math.round(rect.width),
                    overflowing: rect.right > window.innerWidth
                };
            }''')

            # 3. Kiểm tra Touch targets (Nút bấm trên mobile < 36px)
            touch_targets = await page.evaluate('''() => {
                const smallButtons = [];
                if (window.innerWidth <= 430) {
                    const clickables = document.querySelectorAll('button, a, input, select');
                    clickables.forEach(btn => {
                        const style = window.getComputedStyle(btn);
                        if (style.display !== 'none' && style.visibility !== 'hidden') {
                            const rect = btn.getBoundingClientRect();
                            if (rect.width > 0 && rect.height > 0 && (rect.width < 32 || rect.height < 32)) {
                                smallButtons.push({
                                    text: (btn.innerText || btn.getAttribute('aria-label') || btn.tagName).trim().substring(0, 30),
                                    w: Math.round(rect.width),
                                    h: Math.round(rect.height),
                                    tag: btn.tagName
                                });
                            }
                        }
                    });
                }
                return smallButtons.slice(0, 5);
            }''')

            # Chụp ảnh màn hình viewport
            screenshot_path = os.path.join(OUTPUT_DIR, f"responsive_{vp['name']}.png")
            await page.screenshot(path=screenshot_path, full_page=False)

            status = "PASS"
            reasons = []
            if overflow_check["hasOverflow"]:
                status = "FAIL"
                reasons.append(f"Tràn ngang ({overflow_check['scrollWidth']}px > {overflow_check['windowWidth']}px)")
            
            print(f"\n[{status}] Viewport: {vp['name']} ({vp['width']}x{vp['height']})")
            if reasons:
                for r in reasons:
                    print(f"  ❌ {r}")
                if overflow_check["overflowingElements"]:
                    print("  -> Elements gây tràn viền:")
                    for el in overflow_check["overflowingElements"]:
                        print(f"     - <{el['tag']}> id='{el['id']}' class='{el['class']}' (right={el['rect']['right']}px)")
                all_issues.append({"vp": vp["name"], "overflow": overflow_check})
            else:
                print(f"  ✓ Không bị tràn viền ngang (scrollWidth: {overflow_check['scrollWidth']}px == {overflow_check['windowWidth']}px)")

            if touch_targets and vp['width'] <= 430:
                print(f"  ⚠️ Cảnh báo touch target nhỏ ({len(touch_targets)} nút):")
                for tb in touch_targets:
                    print(f"     - {tb['tag']} '{tb['text']}': {tb['w']}x{tb['h']}px")

            await context.close()

        await browser.close()
        print("\n=== HOÀN TẤT AUDIT ===")

if __name__ == "__main__":
    asyncio.run(run_audit())
