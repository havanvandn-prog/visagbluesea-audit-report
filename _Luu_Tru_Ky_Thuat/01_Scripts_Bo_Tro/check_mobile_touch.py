import sys
import os
import asyncio
from playwright.async_api import async_playwright

sys.stdout.reconfigure(encoding='utf-8')
HTML_PATH = os.path.abspath('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html')

async def check():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 360, 'height': 800})
        await page.goto(f'file:///{HTML_PATH}')
        await page.wait_for_load_state('networkidle')
        await page.wait_for_timeout(1000)
        
        small = await page.evaluate('''() => {
            const list = [];
            document.querySelectorAll('button, a, input, select').forEach(el => {
                const style = window.getComputedStyle(el);
                if (style.display !== 'none' && style.visibility !== 'hidden') {
                    const rect = el.getBoundingClientRect();
                    if (rect.width > 0 && rect.height > 0 && (rect.width < 36 || rect.height < 36)) {
                        list.push({
                            text: (el.innerText || el.getAttribute('aria-label') || el.tagName).trim().substring(0, 40),
                            w: Math.round(rect.width),
                            h: Math.round(rect.height),
                            tag: el.tagName,
                            class: (el.getAttribute('class') || '').substring(0, 80)
                        });
                    }
                }
            });
            return list;
        }''')
        print(f'Total small touch targets: {len(small)}')
        for item in small:
            print(f"- {item['tag']} '{item['text']}': {item['w']}x{item['h']} | {item['class']}")
        await browser.close()

asyncio.run(check())
