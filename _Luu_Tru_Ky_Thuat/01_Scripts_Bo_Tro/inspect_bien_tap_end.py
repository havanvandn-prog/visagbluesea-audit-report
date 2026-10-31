import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Last 30 lines of bien_tap_cau_chu.py:")
print("".join(lines[-30:]))
