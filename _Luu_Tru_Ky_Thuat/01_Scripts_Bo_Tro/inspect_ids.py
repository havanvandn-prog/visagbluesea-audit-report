import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html', 'r', encoding='utf-8') as f:
    text = f.read()

ids = re.findall(r'<section[^>]*id="([^"]+)"', text)
print("Sections found:", ids)

# Also check any div with id
div_ids = re.findall(r'<div[^>]*id="([^"]+)"', text)
print("Divs with id:", div_ids[:15])

# Find occurrences of 'Chưa Cài Đặt Thẻ Đo Lường' and its surroundings
idx = text.find('Chưa Cài Đặt Thẻ Đo Lường')
if idx != -1:
    print("\nSurrounding of 'Chưa Cài Đặt Thẻ Đo Lường':")
    print(text[max(0, idx-200):min(len(text), idx+400)])

# Find occurrences of F-TRK-01
for m in re.finditer(r'F-TRK-01', text):
    start = max(0, m.start() - 150)
    end = min(len(text), m.end() + 250)
    print("\nOccurrence of F-TRK-01:")
    print(text[start:end])
