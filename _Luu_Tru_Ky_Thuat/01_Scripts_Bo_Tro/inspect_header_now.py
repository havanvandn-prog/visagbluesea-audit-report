import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

header_m = re.search(r'<header.*?</header>', text, re.DOTALL)
if header_m:
    print(header_m.group(0))
