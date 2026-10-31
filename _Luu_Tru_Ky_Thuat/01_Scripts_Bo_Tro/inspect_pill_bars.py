import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'<span class="w-2\.5 h-6[^"]*"></span>', text):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 100)
    print("Match:", text[start:end])
