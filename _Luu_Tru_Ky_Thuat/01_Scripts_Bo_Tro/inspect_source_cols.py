import openpyxl
import sys
sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.load_workbook('Keyword Planner/04_Kiem_Dinh_Va_Tai_Cau_Truc_Keyword_visagbluesea.xlsx', data_only=True)

sheets_to_check = ['Tổng Hợp', 'Từ Khóa Chạy Ngay (Cốt Lõi)', 'MUA HÀNG (BOFU)', 'CÂN NHẮC (MOFU)', 'QUAN TÂM (TOFU)', 'Từ Khóa Phủ Định', 'Quyết Định Không Triển Khai']

for sname in sheets_to_check:
    if sname in wb.sheetnames:
        sheet = wb[sname]
        print(f"\n=== Sheet: {sname} ===")
        # Find header row
        for r in range(1, 10):
            row_vals = [sheet.cell(row=r, column=c).value for c in range(1, 25)]
            if any(row_vals):
                print(f"Row {r}: {[v for v in row_vals if v is not None][:12]}")
                if any('TỪ KHÓA' in str(v).upper() or 'CHIẾN DỊCH' in str(v).upper() for v in row_vals if v):
                    break
