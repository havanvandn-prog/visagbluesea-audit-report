import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

s3 = text[text.find('id="doi-sanh-truoc-sau"'):text.find('id="bang-uu-tien-p0-p3"')]
print(s3[6500:])
