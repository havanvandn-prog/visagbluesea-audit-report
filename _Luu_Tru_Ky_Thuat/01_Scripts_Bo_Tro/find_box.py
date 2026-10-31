import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'Tài liệu đánh giá kỹ thuật trung lập', text)]
print("Matches in bien_tap_cau_chu.py:", matches)
for pos in matches:
    print(text[max(0, pos-150):min(len(text), pos+300)])
    print("-" * 50)
