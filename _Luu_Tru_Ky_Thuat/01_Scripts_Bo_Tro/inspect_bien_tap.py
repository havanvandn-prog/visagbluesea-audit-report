import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("File size:", len(text))
print("Occurrences of F-TRK-01 in bien_tap_cau_chu.py:", text.count("F-TRK-01"))
print("Occurrences of GTM Tag:", text.count("GTM Tag"))
