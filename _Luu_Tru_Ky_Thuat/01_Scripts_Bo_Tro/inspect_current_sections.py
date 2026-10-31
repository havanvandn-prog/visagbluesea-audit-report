import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("Current length:", len(text))
print("Sections present:")
import re
for m in re.finditer(r'<section[^>]*id="([^"]+)"', text):
    print(" -", m.group(1))
