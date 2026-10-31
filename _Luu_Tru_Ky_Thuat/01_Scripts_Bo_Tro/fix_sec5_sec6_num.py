import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '6. Cấu Trúc Bố Cục Từng Khối (Blueprint Section-by-Section)',
    '5. Cấu Trúc Bố Cục Từng Khối (Blueprint Section-by-Section)'
)

text = text.replace(
    '7. Khuyến Nghị Vận Hành Chiến Dịch Google Search Ads',
    '6. Khuyến Nghị Vận Hành Chiến Dịch Google Search Ads'
)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed heading numbers 5 and 6 in bien_tap_cau_chu.py!")
