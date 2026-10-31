import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Chưa Cài Đặt Thẻ Đo Lường')
print("Find 'Chưa Cài Đặt Thẻ Đo Lường':", idx)
if idx != -1:
    print(text[max(0, idx-300):min(len(text), idx+600)])
