import sys
import os

# Let's inspect line 400-450 of build_v4_master_excel.py
with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/build_v4_master_excel.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(350, min(420, len(lines))):
    print(f"{i+1}: {lines[i]}", end='')
