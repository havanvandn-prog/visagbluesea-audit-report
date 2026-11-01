import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

excel_path = 'Keyword Planner/03_Phan_Tich_Tu_Khoa_V4_visagbluesea.xlsx'
df_active = pd.read_excel(excel_path, sheet_name='Tổng Hợp', skiprows=3)

# Inspect what is inside STAG_DichVu_Visa_QuocTe_TongHop_CỐT and other TongHop groups
tonghop_groups = df_active[df_active['B. NHÓM QUẢNG CÁO'].str.contains('TongHop', case=False, na=False)]['B. NHÓM QUẢNG CÁO'].unique()

print(f"Total TongHop groups: {len(tonghop_groups)}")
for g in tonghop_groups:
    sub = df_active[df_active['B. NHÓM QUẢNG CÁO'] == g]
    kws = sub['E. TỪ KHÓA'].tolist()
    print(f"\nGroup: {g} ({len(kws)} kws, Vol={sub['G. LƯỢNG TÌM KIẾM'].sum()}):")
    for k in kws:
        print(f"  - {k}")
