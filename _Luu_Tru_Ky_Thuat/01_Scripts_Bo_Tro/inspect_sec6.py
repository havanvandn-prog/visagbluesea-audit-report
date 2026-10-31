import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="luu-y-google-ads"')
print(text[idx:idx+2500])
