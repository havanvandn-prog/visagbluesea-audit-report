import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Điểm Nghẽn 05')
start_div = text.rfind('<div class="finding-card', 0, idx)
print("Start div of Card 5:", text[start_div:start_div+100])

# Find the end of this card:
# After "Hậu quả: Máy học Ads mất dấu", let's see what comes next
idx_end = text.find('Hậu quả: Máy học Ads mất dấu', idx)
print("After Hau qua:", text[idx_end:idx_end+200])
