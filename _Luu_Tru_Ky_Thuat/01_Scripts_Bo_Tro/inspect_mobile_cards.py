import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="mobile-action-cards"')
if idx != -1:
    print(text[idx:idx+2500])
