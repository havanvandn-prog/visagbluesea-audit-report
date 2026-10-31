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
        
        cards = await page.evaluate('''() => {
            const list = [];
            document.querySelectorAll('#tong-quan .grid > div').forEach(card => {
                const rect = card.getBoundingClientRect();
                list.push({
                    text: card.innerText.replace(/\\n+/g, ' | ').substring(0, 50),
                    w: Math.round(rect.width),
                    h: Math.round(rect.height)
                });
            });
            return list;
        }''')
        print('Section 1 stat cards on 360px:')
        for c in cards:
            print(f"  - {c['w']}x{c['h']} | {c['text']}")
        await browser.close()

asyncio.run(check())
