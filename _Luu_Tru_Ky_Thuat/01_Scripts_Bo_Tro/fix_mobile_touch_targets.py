import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace mobile card "Soi lỗi ↗" link with a prominent touch target button
old_link = 'class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>'
new_link = 'class="inline-flex items-center justify-center gap-1 px-3 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 text-emerald-700 text-xs font-bold border border-emerald-200 transition-colors shrink-0 min-h-[36px] min-w-[72px]">Soi lỗi ↗</a>'

if old_link in text:
    count = text.count(old_link)
    text = text.replace(old_link, new_link)
    print(f"Replaced {count} instances of Soi lỗi link with touch-friendly button!")
else:
    print("Warning: old_link not found!")

# Also ensure safe-area-inset is included in mobile nav bar
old_nav_class = 'class="fixed bottom-3 left-3 right-3 z-40 md:hidden bg-white/95 backdrop-blur-md border border-slate-200/90 rounded-2xl shadow-xl p-1.5 flex items-center justify-between gap-1"'
new_nav_class = 'class="fixed bottom-3 left-3 right-3 z-40 md:hidden bg-white/95 backdrop-blur-md border border-slate-200/90 rounded-2xl shadow-xl p-1.5 flex items-center justify-between gap-1 pb-[max(0.375rem,env(safe-area-inset-bottom))]"'

if old_nav_class in text:
    text = text.replace(old_nav_class, new_nav_class)
    print("Added safe-area-inset-bottom to Mobile Nav Bar!")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated bien_tap_cau_chu.py successfully!")
