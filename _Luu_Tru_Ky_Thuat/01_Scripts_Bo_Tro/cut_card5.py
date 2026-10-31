import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Điểm Nghẽn 05')
start_div = text.rfind('<div class="finding-card', 0, idx)

# Find the end of this card
marker = 'Hậu quả: Máy học Ads mất dấu</span>\n            </div>\n          </div>'
idx_marker = text.find(marker, idx)
if idx_marker != -1:
    end_div = idx_marker + len(marker)
    # Remove card 5
    text = text[:start_div] + text[end_div:]
    print("Cut Card 5 successfully!")
else:
    print("Error: Marker not found!")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved bien_tap_cau_chu.py after cutting Card 5!")
