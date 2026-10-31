import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

s1 = text[text.find('id="tong-quan"'):text.find('id="diem-nghen-chuyen-doi"')]
print("Section 1 Stat Cards HTML:")
print(s1[:2000])
