import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

grids = re.findall(r'class="[^"]*grid-cols[^"]*"', text)
print("Unique grid-cols classes:")
for g in set(grids):
    print(" -", g)
