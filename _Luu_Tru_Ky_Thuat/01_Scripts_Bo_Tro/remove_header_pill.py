import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('<header')
end = text.find('</header>') + len('</header>')

new_header = """<header class="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 h-14 flex items-center justify-between px-3 sm:px-6 shadow-2xs">
    
    <!-- Left: Brand & Domain link (Clean, Zero Meaningless Status Pills) -->
    <div class="flex items-center gap-3">
      <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-emerald-600 to-emerald-400 flex items-center justify-center text-white font-extrabold text-sm shadow-sm shrink-0">
        GB
      </div>
      <div>
        <span class="font-extrabold text-slate-900 text-xs sm:text-sm tracking-tight block">GBlueSea Audit Portal</span>
        <span class="text-[11px] text-slate-500 hidden sm:inline">Đối soát: <a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 hover:underline font-medium">visagbluesea.com ↗</a></span>
      </div>
    </div>

    <!-- Right: Clean domain reference -->
    <div class="hidden sm:flex items-center gap-2 text-xs font-medium text-slate-400">
      <span>visagbluesea.com</span>
    </div>
  </header>"""

text = text[:start] + new_header + text[end:]
with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated header in bien_tap_cau_chu.py successfully!")
