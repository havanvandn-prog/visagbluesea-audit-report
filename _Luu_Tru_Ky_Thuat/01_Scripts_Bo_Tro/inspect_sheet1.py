import openpyxl
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.load_workbook('Keyword Planner/04_Kiem_Dinh_Va_Tai_Cau_Truc_Keyword_visagbluesea.xlsx', data_only=True)

# Inspect Sheet 01_Báo Cáo Kiểm Định & Đợt Bật
sheet1 = wb['01_Báo Cáo Kiểm Định & Đợt Bật']
print("--- SHEET 1 ROWS ---")
for r in range(1, 40):
    row_vals = [sheet1.cell(row=r, column=c).value for c in range(1, 15)]
    if any(row_vals):
        print(f"R{r}: {row_vals}")

# Inspect Du Lieu Du Bao
if 'Du Lieu Du Bao' in wb.sheetnames:
    sheet_db = wb['Du Lieu Du Bao']
    print("\n--- DU LIEU DU BAO ROWS ---")
    for r in range(1, 25):
        row_vals = [sheet_db.cell(row=r, column=c).value for c in range(1, 15)]
        if any(row_vals):
            print(f"R{r}: {row_vals}")
