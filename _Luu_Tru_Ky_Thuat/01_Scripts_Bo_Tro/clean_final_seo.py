import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = None
end_idx = None
for idx, line in enumerate(lines):
    if '<!-- Card 5: Missing H1 Golden Visa -->' in line:
        start_idx = idx
    if '<!-- Card 6: Tracking Missing -->' in line:
        end_idx = idx

print(f'start_idx: {start_idx}, end_idx: {end_idx}')
if start_idx is not None and end_idx is not None:
    lines = lines[:start_idx] + lines[end_idx:]

for idx, line in enumerate(lines):
    if '<!-- Card 6: Tracking Missing -->' in line:
        lines[idx] = '          <!-- Card 5: Tracking Missing -->\n'
    if 'data-cat="tech,tracking"' in line:
        lines[idx] = line.replace('data-cat="tech,tracking"', 'data-cat="trk"')

with open(script_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Cleaned final SEO block successfully!')
