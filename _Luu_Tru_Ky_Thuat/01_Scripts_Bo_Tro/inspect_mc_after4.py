import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx4 = text.find('F-UI-04', text.find('id="mobile-action-cards"'))
print(text[idx4:idx4+2000])
