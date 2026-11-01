import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/build_v4_master_excel.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect qualify_keyword definition in build_v4_master_excel.py
start_idx = text.find("def qualify_keyword(row):")
end_idx = text.find("df_all = df_all.reset_index(drop=True)")

fn_text = text[start_idx:end_idx]
print(f"Length of qualify_keyword: {len(fn_text)}")
for m in re.finditer(r"'([a-z_]+)':", fn_text):
    print(m.group(1), end=', ')
print()
