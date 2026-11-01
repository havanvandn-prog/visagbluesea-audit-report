import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

# Check raw CSV directly first
csv_path = '_Luu_Tru_Ky_Thuat/Keyword_Planner_Raw/Historical_Metrics_HCM_Real.csv'
try:
    with open(csv_path, 'r', encoding='utf-16') as f:
        lines = [f.readline() for _ in range(10)]
    print("CSV encoding: utf-16")
except:
    with open(csv_path, 'r', encoding='utf-8') as f:
        lines = [f.readline() for _ in range(10)]
    print("CSV encoding: utf-8")

for i, l in enumerate(lines):
    print(f"Line {i}: {l.strip()[:100]}")

# Also check how excel was written
excel_path = 'Keyword Planner/01_Bao_Cao_Nghien_Cuu_Va_Du_Doan_Keyword_Planner.xlsx'
wb = pd.ExcelFile(excel_path)
print("Sheet names:", wb.sheet_names)
df_head = pd.read_excel(excel_path, sheet_name='So_Lieu_Lich_Su_Va_Du_Doan', nrows=15)
print("\nFirst 15 rows of Excel:")
print(df_head)
