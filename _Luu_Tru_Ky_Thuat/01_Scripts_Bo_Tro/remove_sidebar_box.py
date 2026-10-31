import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

target_box = """      <!-- Thẩm định độc lập card -->
      <div class="mt-auto bg-white rounded-xl p-3.5 border border-slate-200/80 shadow-2xs space-y-2">
        <div class="flex items-center gap-2 text-slate-900 font-bold text-xs">
          <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600 shrink-0"></i>
          <span>Thẩm Định Độc Lập</span>
        </div>
        <p class="text-[11px] text-slate-500 leading-relaxed">
          Tài liệu đánh giá kỹ thuật trung lập gửi Ban Giám Đốc trước khi duyệt ngân sách quảng cáo.
        </p>
      </div>"""

if target_box in text:
    text = text.replace(target_box, "")
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Removed helper card box from bien_tap_cau_chu.py successfully!")
else:
    print("Warning: target_box exact match not found! Checking fallback regex...")
    import re
    pattern = r'\s*<!-- Thẩm định độc lập card -->\s*<div class="mt-auto bg-white rounded-xl.*?</div>\s*</div>'
    if re.search(pattern, text, re.DOTALL):
        text = re.sub(pattern, "", text, flags=re.DOTALL)
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print("Removed helper card box via regex fallback!")
    else:
        print("Could not find helper card box!")
