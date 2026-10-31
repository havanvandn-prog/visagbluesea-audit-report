import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

target_cta_block = """    <!-- Right: Action Buttons -->
    <div class="flex items-center gap-2 sm:gap-3">
      <a href="Du_Lieu_Trien_Khai_Chi_Tiet_visagbluesea.com.xlsx" download class="inline-flex items-center gap-1.5 px-3 py-1.5 sm:px-3.5 sm:py-2 rounded-lg bg-[#01a915] hover:bg-[#018a12] text-white text-xs font-bold transition-all shadow-sm shadow-emerald-600/20 whitespace-nowrap shrink-0 min-h-[36px] sm:min-h-[38px]">
        <i data-lucide="file-spreadsheet" class="w-3.5 h-3.5 sm:w-4 sm:h-4 shrink-0"></i>
        <span>Tải File Excel 6 Sheets</span>
      </a>
      <a href="Bao_Cao_Ky_Thuat_Noi_Bo_visagbluesea.com.html" class="inline-flex items-center gap-1.5 px-3 py-1.5 sm:px-3 sm:py-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold transition-all whitespace-nowrap shrink-0 border border-slate-200 min-h-[36px] sm:min-h-[38px]">
        <i data-lucide="code" class="w-3.5 h-3.5 shrink-0 text-slate-600"></i>
        <span class="hidden sm:inline">Bản Kỹ Thuật</span> Dev
        <i data-lucide="chevron-right" class="w-3 h-3 shrink-0"></i>
      </a>
    </div>"""

clean_header_right = """    <!-- Right: Clean Status Info (No CTA on Header) -->
    <div class="hidden sm:flex items-center gap-2 text-xs font-semibold text-slate-400">
      <span>Báo Cáo Thẩm Định Độc Lập</span>
    </div>"""

if target_cta_block in text:
    text = text.replace(target_cta_block, clean_header_right)
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Removed Header CTAs from bien_tap_cau_chu.py successfully!")
else:
    print("Warning: target_cta_block not found in bien_tap_cau_chu.py!")
