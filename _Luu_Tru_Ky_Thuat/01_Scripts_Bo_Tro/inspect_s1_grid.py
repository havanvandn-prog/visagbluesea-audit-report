import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

s1 = text[text.find('id="tong-quan"'):text.find('id="diem-nghen-chuyen-doi"')]
idx_grid = s1.find('grid-cols-2 sm:grid-cols-4')
print(s1[idx_grid:idx_grid+2500])
