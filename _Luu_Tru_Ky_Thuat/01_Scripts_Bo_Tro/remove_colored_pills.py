import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Remove all 5 pill bar spans and clean the h2 class
pill_pattern = r'\s*<span class="w-2\.5 h-6 bg-[^"]* rounded-full inline-block"></span>'
text = re.sub(pill_pattern, '', text)

# Clean h2 tag from 'flex items-center gap-2' if it has it
text = text.replace(
    '<h2 class="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight flex items-center gap-2">',
    '<h2 class="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight">'
)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Removed all colored pill bars from headings in bien_tap_cau_chu.py!")
