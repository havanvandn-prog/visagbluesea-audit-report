import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

s2 = text[text.find('id="diem-nghen-chuyen-doi"'):text.find('id="doi-sanh-truoc-sau"')]
print("Finding cards in Section 2:")
import re
titles = re.findall(r'<h3 class="[^"]*">([^<]+)</h3>', s2)
for t in titles:
    print(" -", t)
