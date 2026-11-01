import openpyxl
import sys
sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.load_workbook('Keyword Planner/04_Kiem_Dinh_Va_Tai_Cau_Truc_Keyword_visagbluesea.xlsx', read_only=True)
print("Sheet names:", wb.sheetnames)

for name in wb.sheetnames:
    sheet = wb[name]
    row_iter = sheet.iter_rows(values_only=True)
    try:
        first_row = list(next(row_iter))
        print(f"Sheet: {name} | Row 1: {first_row[:10]}")
    except StopIteration:
        print(f"Sheet: {name} is empty")
