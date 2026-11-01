import sys
import openpyxl
import pandas as pd
import re

sys.stdout.reconfigure(encoding='utf-8')

excel_path = 'Keyword Planner/03_Phan_Tich_Tu_Khoa_V4_visagbluesea.xlsx'

# Read sheet 'Tổng Hợp'
df_active = pd.read_excel(excel_path, sheet_name='Tổng Hợp', skiprows=3)
print(f"Loaded active keywords: {len(df_active)}")
print("Columns:", df_active.columns.tolist())

# Read sheet 'Quyết Định Không Triển Khai'
df_drop = pd.read_excel(excel_path, sheet_name='Quyết Định Không Triển Khai', skiprows=3)
print(f"Loaded excluded keywords: {len(df_drop)}")

# Check groups with 'TongHop' in name
tonghop_groups = df_active[df_active['B. NHÓM QUẢNG CÁO'].str.contains('TongHop', case=False, na=False)]['B. NHÓM QUẢNG CÁO'].unique()
print(f"\nGroups with 'TongHop' in name (Rule 9 violation): {len(tonghop_groups)}")
for g in tonghop_groups[:10]:
    print(f" - {g}")

# Check group size statistics
group_sizes = df_active.groupby('B. NHÓM QUẢNG CÁO').size()
print(f"\nGroup size stats: Min={group_sizes.min()}, Max={group_sizes.max()}, Total groups={len(group_sizes)}")
print(f"Groups > 10: {(group_sizes > 10).sum()}, Groups > 12: {(group_sizes > 12).sum()}, Groups < 4: {(group_sizes < 4).sum()}")

# Check Low Search Volume groups (< 20 volume)
group_vols = df_active.groupby('B. NHÓM QUẢNG CÁO')['G. LƯỢNG TÌM KIẾM'].sum()
lsv_groups = group_vols[group_vols < 20]
print(f"\nLow Search Volume groups (< 20 searches/month) (Rule 7): {len(lsv_groups)}")
for g, v in lsv_groups.head(10).items():
    print(f" - {g}: volume={v}")

# Check leakage of out-of-geo or jobs in active keywords
out_geo_active = df_active[df_active['E. TỪ KHÓA'].str.contains(r'\b(hà nội|đà nẵng|hải phòng|cần thơ|huế)\b', case=False, na=False)]
print(f"\nOut-of-geo leaks in active keywords (Rule 6): {len(out_geo_active)}")
if len(out_geo_active) > 0:
    print(out_geo_active[['E. TỪ KHÓA', 'B. NHÓM QUẢNG CÁO']].head())

jobs_active = df_active[df_active['E. TỪ KHÓA'].str.contains(r'\b(tuyển dụng|tìm việc|việc làm|thợ nail|cần thợ|xklđ)\b', case=False, na=False)]
print(f"\nJob/recruitment leaks in active keywords (Rule 6): {len(jobs_active)}")
if len(jobs_active) > 0:
    print(jobs_active[['E. TỪ KHÓA', 'B. NHÓM QUẢNG CÁO']].head())
