import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

# find mobile cards in bien_tap_cau_chu.py
idx_mc = text.find('id="mobile-action-cards"')
if idx_mc != -1:
    print(text[idx_mc:idx_mc+5000])
