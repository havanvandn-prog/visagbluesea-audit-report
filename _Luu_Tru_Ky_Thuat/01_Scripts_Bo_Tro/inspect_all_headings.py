import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

for i, sid in enumerate(['tong-quan', 'diem-nghen-chuyen-doi', 'bang-uu-tien-p0-p3', 'kien-truc-sitemap', 'blueprint-sections', 'luu-y-google-ads'], 1):
    m = re.search(rf'<section[^>]*id="{sid}".*?(?=<section|\Z)', text, re.DOTALL)
    if m:
        sec_text = m.group(0)
        h12 = re.search(r'<h[12][^>]*>(.*?)</h[12]>', sec_text, re.DOTALL)
        clean_title = re.sub(r'<[^>]+>', '', h12.group(1)).strip() if h12 else "NO HEADING"
        print(f"Section {i} [{sid}]: {clean_title}")
