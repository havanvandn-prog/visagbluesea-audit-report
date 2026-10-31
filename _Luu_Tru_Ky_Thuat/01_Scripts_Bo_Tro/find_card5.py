import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Check Card 5 in Section 2
idx5 = text.find('Điểm Nghẽn 05')
if idx5 != -1:
    print("Found 'Điểm Nghẽn 05' at", idx5)
    print("--- SNIPPET ---")
    print(text[max(0, idx5-200):min(len(text), idx5+1200)])
else:
    print("NOT found 'Điểm Nghẽn 05'")
    # Search for 'Chưa Cài Đặt Thẻ Đo Lường'
    idx_gtm = text.find('Chưa Cài Đặt Thẻ Đo Lường')
    if idx_gtm != -1:
        print("Found 'Chưa Cài Đặt Thẻ Đo Lường' at", idx_gtm)
        print(text[max(0, idx_gtm-200):min(len(text), idx_gtm+1200)])

# Check Section 4 Table row 05 / F-TRK-01
idx_tbl = text.find('F-TRK-01')
if idx_tbl != -1:
    print("\n--- FOUND F-TRK-01 in Table/Mobile ---")
    print(text[max(0, idx_tbl-200):min(len(text), idx_tbl+1000)])
