import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update header from sticky top-0 to fixed top-0 left-0 right-0 z-50
old_header = '<header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 h-14 flex items-center justify-between px-3 sm:px-6 shadow-2xs">'
new_header = '<header class="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 h-14 flex items-center justify-between px-3 sm:px-6 shadow-2xs">'

if old_header in content:
    content = content.replace(old_header, new_header)
    print("Replaced header with fixed successfully!")
else:
    print("WARNING: old_header not found!")

# 2. Add pt-14 to app shell container so content starts cleanly below fixed header
old_shell = '<div class="flex min-h-[calc(100vh-3.5rem)]">'
new_shell = '<div class="flex min-h-screen pt-14">'

if old_shell in content:
    content = content.replace(old_shell, new_shell)
    print("Replaced shell with pt-14 successfully!")
else:
    print("WARNING: old_shell not found!")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated bien_tap_cau_chu.py successfully!")
