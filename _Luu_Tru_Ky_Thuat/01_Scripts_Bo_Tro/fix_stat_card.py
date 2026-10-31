import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

old_stat = '<span class="text-2xl sm:text-3xl font-black text-red-600 block">5 Điểm Nghẽn</span>'
new_stat = '<span class="text-2xl sm:text-3xl font-black text-red-600 block">4 Điểm Nghẽn</span>'

if old_stat in text:
    text = text.replace(old_stat, new_stat)
    print("Replaced 5 Điểm Nghẽn with 4 Điểm Nghẽn in bien_tap_cau_chu.py!")
else:
    print("Warning: old_stat not found!")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

# Also update Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html and index.html
with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    html = f.read()

if old_stat in html:
    html = html.replace(old_stat, new_stat)
    with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'w', encoding='utf-8') as f:
        f.write(html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced in HTML files too!")
