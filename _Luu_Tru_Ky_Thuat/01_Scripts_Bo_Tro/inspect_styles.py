import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

style_m = re.search(r'<style>.*?</style>', text, re.DOTALL)
if style_m:
    styles = style_m.group(0)
    for line in styles.splitlines():
        if any(k in line for k in ['sub-nav-item', 'rail-btn', 'sidebar']):
            print(line)
