import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

s3 = text[text.find('id="bang-uu-tien-p0-p3"'):text.find('id="kien-truc-sitemap"')]
h2 = re.search(r'<h2[^>]*>(.*?)</h2>', s3, re.DOTALL)
if h2:
    print("Section 3 H2 Raw:", repr(h2.group(1).strip()))
