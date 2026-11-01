import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import json
import sys
import copy

sys.stdout.reconfigure(encoding='utf-8')

print("1. Loading audited workbook...")
src_wb = openpyxl.load_workbook('Keyword Planner/04_Kiem_Dinh_Va_Tai_Cau_Truc_Keyword_visagbluesea.xlsx', data_only=False)
print("Source sheets:", src_wb.sheetnames)

dest_wb = openpyxl.Workbook()
dest_wb.remove(dest_wb.active) # Remove default sheet

# Colors
NAVY = "1E3A8A"
EMERALD = "065F46"
AMBER = "D97706"
SLATE = "1E293B"
BLUE_BG = "EFF6FF"
GREEN_BG = "ECFDF5"
YELLOW_BG = "FEF9C3"
GRAY_BG = "F8FAFC"
WHITE = "FFFFFF"
BORDER_COLOR = "CBD5E1"

font_title = Font(name="Calibri", size=15, bold=True, color=NAVY)
font_subtitle = Font(name="Calibri", size=10, italic=True, color="475569")
font_sec_hdr = Font(name="Calibri", size=11, bold=True, color=WHITE)
font_tbl_hdr = Font(name="Calibri", size=9, bold=True, color=WHITE)
font_bold = Font(name="Calibri", size=9, bold=True)
font_regular = Font(name="Calibri", size=9)
font_italic = Font(name="Calibri", size=8, italic=True, color="64748B")
font_kpi_val = Font(name="Calibri", size=12, bold=True, color=NAVY)
font_red_note = Font(name="Calibri", size=9, bold=True, color="B91C1C")

fill_navy = PatternFill(start_color=NAVY, end_color=NAVY, fill_type="solid")
fill_emerald = PatternFill(start_color=EMERALD, end_color=EMERALD, fill_type="solid")
fill_amber = PatternFill(start_color=AMBER, end_color=AMBER, fill_type="solid")
fill_slate = PatternFill(start_color=SLATE, end_color=SLATE, fill_type="solid")
fill_blue = PatternFill(start_color=BLUE_BG, end_color=BLUE_BG, fill_type="solid")
fill_green = PatternFill(start_color=GREEN_BG, end_color=GREEN_BG, fill_type="solid")
fill_yellow = PatternFill(start_color=YELLOW_BG, end_color=YELLOW_BG, fill_type="solid")
fill_gray = PatternFill(start_color=GRAY_BG, end_color=GRAY_BG, fill_type="solid")

thin_side = Side(border_style="thin", color=BORDER_COLOR)
thin_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)
double_bottom = Border(left=thin_side, right=thin_side, top=thin_side, bottom=Side(border_style="double", color=NAVY))

align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
align_right = Alignment(horizontal="right", vertical="center", wrap_text=True)

def style_cell(cell, font=font_regular, fill=None, alignment=align_left, border=thin_border, number_format=None):
    if font: cell.font = font
    if fill: cell.fill = fill
    if alignment: cell.alignment = alignment
    if border: cell.border = border
    if number_format: cell.number_format = number_format

def copy_sheet(src_sheet, dest_sheet):
    dest_sheet.views.sheetView[0].showGridLines = True
    for row in src_sheet.iter_rows(values_only=False):
        for cell in row:
            dest_cell = dest_sheet.cell(row=cell.row, column=cell.column, value=cell.value)
            if cell.has_style:
                dest_cell.font = copy.copy(cell.font)
                dest_cell.border = copy.copy(cell.border)
                dest_cell.fill = copy.copy(cell.fill)
                dest_cell.number_format = copy.copy(cell.number_format)
                dest_cell.alignment = copy.copy(cell.alignment)
    for col_letter, col_dim in src_sheet.column_dimensions.items():
        if col_dim.width:
            dest_sheet.column_dimensions[col_letter].width = col_dim.width
    dest_sheet.freeze_panes = None

# ==============================================================================
# SHEET 00: TỔNG QUAN KẾ HOẠCH
# ==============================================================================
print("Creating Sheet 00_Tổng Quan Kế Hoạch...")
ws0 = dest_wb.create_sheet(title="00_Tổng Quan Kế Hoạch")
ws0.views.sheetView[0].showGridLines = True
ws0.freeze_panes = None

ws0.merge_cells("A1:H1")
c = ws0.cell(row=1, column=1, value="KẾ HOẠCH TỔNG THỂ GOOGLE SEARCH ADS & DỰ BÁO KPI KINH DOANH (V2)")
style_cell(c, font=font_title, alignment=align_left)

ws0.merge_cells("A2:H2")
c = ws0.cell(row=2, column=1, value="Dự án: Tập đoàn Định cư & Visa GBlueSea (visagbluesea.com) | Chuẩn Hợp Đồng Dự Báo: demand-budget-v1 | Tài khoản mới (Cold Start)")
style_cell(c, font=font_subtitle, alignment=align_left)

# Executive Stat Cards (Row 4 - 6)
stat_cards = [
    ("A", "B", "NGÂN SÁCH KHỞI CHẠY (ĐỢT 1)", "15,000,000 ₫/tháng", "500.000 ₫/ngày - Khóa trần 10 nhóm STAG Core", fill_blue),
    ("C", "D", "CHIẾN LƯỢC GIÁ THẦU", "Maximize Clicks + Cap", "Trần CPC Cap = CPC TB × 1.25 chống đói hiển thị", fill_green),
    ("E", "F", "QUY MÔ TRIỂN KHAI", "10 Nhóm STAG (526 Dự phòng)", "Tập trung 100% vào EB-5 Mỹ & Golden Visa Châu Âu", fill_yellow),
    ("G", "H", "ĐIỂM HÒA VỐN ĐẦU TƯ", "0.14 Hợp đồng / tháng", "Doanh thu 1 Deal (150M) gấp 10x chi phí Ads cả tháng", fill_blue)
]

for col1, col2, title, val, sub, fill in stat_cards:
    ws0.merge_cells(f"{col1}4:{col2}4")
    ws0.merge_cells(f"{col1}5:{col2}5")
    ws0.merge_cells(f"{col1}6:{col2}6")
    c_t = ws0.cell(row=4, column=openpyxl.utils.column_index_from_string(col1), value=title)
    c_v = ws0.cell(row=5, column=openpyxl.utils.column_index_from_string(col1), value=val)
    c_s = ws0.cell(row=6, column=openpyxl.utils.column_index_from_string(col1), value=sub)
    style_cell(c_t, font=font_bold, fill=fill, alignment=align_center)
    style_cell(c_v, font=font_kpi_val, fill=fill, alignment=align_center)
    style_cell(c_s, font=font_italic, fill=fill, alignment=align_center)

# Section 1: 5 Thông số vận hành & Đầu vào kinh doanh (Row 8 - 15)
ws0.merge_cells("A8:H8")
c = ws0.cell(row=8, column=1, value="1. NĂM THÔNG SỐ VẬN HÀNH & ĐẦU VÀO KINH DOANH (BENCHMARK ĐỀ XUẤT CHO SẾP DUYỆT)")
style_cell(c, font=font_sec_hdr, fill=fill_navy, alignment=align_left)

tbl_inputs_hdr = ["STT", "Chỉ Số Vận Hành Cốt Lõi", "Giá Trị Đề Xuất", "Đơn Vị", "Nguồn / Cơ Sở Tính Toán", "Ý Nghĩa Chiến Lược & Tác Động Tài Chính"]
for idx, col_name in enumerate(tbl_inputs_hdr, 1):
    c = ws0.cell(row=9, column=idx if idx <= 2 else idx+1 if idx <= 4 else idx+2 if idx==5 else 8, value=col_name)
    # merge logic
ws0.cell(row=9, column=1, value="STT")
ws0.cell(row=9, column=2, value="Thông Số Vận Hành Cốt Lõi")
ws0.cell(row=9, column=3, value="Giá Trị Đề Xuất")
ws0.cell(row=9, column=4, value="Đơn Vị")
ws0.merge_cells("E9:F9"); ws0.cell(row=9, column=5, value="Nguồn / Căn Cứ Thực Tế")
ws0.merge_cells("G9:H9"); ws0.cell(row=9, column=7, value="Ý Nghĩa Chiến Lược & Tác Động Tài Chính")

for c_idx in range(1, 9):
    style_cell(ws0.cell(row=9, column=c_idx), font=font_tbl_hdr, fill=fill_slate, alignment=align_center)

biz_metrics = [
    (1, "AOV (Giá trị trung bình 1 hợp đồng)", 150000000, "VND", "Dịch vụ tư vấn di trú EB-5 & Golden Visa", "Doanh thu phí dịch vụ tư vấn pháp lý hồ sơ định cư.", "#,##0\" ₫\""),
    (2, "Close Rate % (Tỷ lệ chốt Lead ➔ Hợp đồng)", 0.03, "%", "Benchmark ngành di trú vé lớn (HNWI)", "100 Lead chất lượng mang lại 3 hợp đồng thành công.", "0.0%"),
    (3, "Gross Profit Margin % (Biên lợi nhuận gộp)", 0.70, "%", "Đặc thù công ty dịch vụ di trú & visa", "Lợi nhuận gộp đạt 105.000.000 ₫ trên mỗi hợp đồng 150M.", "0.0%"),
    (4, "Target Monthly Budget (Ngân sách tháng)", 15000000, "VND", "Dữ liệu kiểm định 10 nhóm STAG Core", "500.000 ₫/ngày, đủ nuôi 5–10 lượt nhấp/ngày cho 10 nhóm.", "#,##0\" ₫\""),
    (5, "Target Max CAC (Chi phí tối đa / hợp đồng)", 30000000, "VND", "Trần giới hạn chi phí Marketing an toàn", "Chiếm 20% doanh thu hợp đồng, bảo toàn lãi ròng > 50%.", "#,##0\" ₫\"")
]

for r_idx, (stt, name, val, unit, src, note, fmt) in enumerate(biz_metrics, 10):
    ws0.cell(row=r_idx, column=1, value=stt)
    ws0.cell(row=r_idx, column=2, value=name)
    ws0.cell(row=r_idx, column=3, value=val)
    ws0.cell(row=r_idx, column=4, value=unit)
    ws0.merge_cells(f"E{r_idx}:F{r_idx}"); ws0.cell(row=r_idx, column=5, value=src)
    ws0.merge_cells(f"G{r_idx}:H{r_idx}"); ws0.cell(row=r_idx, column=7, value=note)
    
    style_cell(ws0.cell(row=r_idx, column=1), alignment=align_center)
    style_cell(ws0.cell(row=r_idx, column=2), alignment=align_left, font=font_bold)
    style_cell(ws0.cell(row=r_idx, column=3), alignment=align_right, font=font_bold, fill=fill_yellow, number_format=fmt)
    style_cell(ws0.cell(row=r_idx, column=4), alignment=align_center)
    style_cell(ws0.cell(row=r_idx, column=5), alignment=align_left)
    style_cell(ws0.cell(row=r_idx, column=6), alignment=align_left)
    style_cell(ws0.cell(row=r_idx, column=7), alignment=align_left)
    style_cell(ws0.cell(row=r_idx, column=8), alignment=align_left)

# Section 2: Cấu trúc chiến dịch & Cách ly giá thầu (Row 17 - 23)
ws0.merge_cells("A17:H17")
c = ws0.cell(row=17, column=1, value="2. KIẾN TRÚC CHIẾN DỊCH & CÁCH LY GIÁ THẦU (CPC DISPERSION GUARD ≤ 2.0X)")
style_cell(c, font=font_sec_hdr, fill=fill_navy, alignment=align_left)

camp_headers = ["STT", "Tên Chiến Dịch Đề Xuất", "Dải Giá Thầu CPC", "Max CPC Cap (1.25x)", "Số Nhóm Bật", "Trạng Thái Khởi Chạy", "Ngân Sách Ngày (₫)", "URL Trang Đích"]
for idx, h in enumerate(camp_headers, 1):
    c = ws0.cell(row=18, column=idx, value=h)
    style_cell(c, font=font_tbl_hdr, fill=fill_slate, alignment=align_center)

camps_plan = [
    (1, "GGSearch_DinhCu_EB5_My_HighCPC", "104,346 ₫ – 120,722 ₫", 130000, 3, "ENABLED (Đợt 1)", 170000, "https://www.visagbluesea.com/us-green-card-eb-5"),
    (2, "GGSearch_DinhCu_EB5_My_MidCPC", "45,000 ₫ – 47,977 ₫", 58000, 5, "ENABLED (Đợt 1)", 230000, "https://www.visagbluesea.com/us-green-card-eb-5"),
    (3, "GGSearch_DinhCu_GoldenVisa_ChauAu", "48,974 ₫ – 60,664 ₫", 75000, 2, "ENABLED (Đợt 1)", 100000, "https://www.visagbluesea.com/golden-visa-cyprus"),
    (4, "GGSearch_DuHoc_PhanLan_MuiNhon", "15,000 ₫ – 25,000 ₫", 30000, 0, "PAUSED (Đợt 2 - Chờ mở rộng)", 0, "https://www.visagbluesea.com/study-in-finland"),
    (5, "GGSearch_DichVu_Visa_QuocTe", "10,000 ₫ – 16,000 ₫", 20000, 0, "PAUSED (Đợt 2 - Chờ mở rộng)", 0, "https://www.visagbluesea.com/tourist-visas")
]

for r_idx, (stt, c_name, cpc_range, cap, grp_cnt, status, b_day, url) in enumerate(camps_plan, 19):
    ws0.cell(row=r_idx, column=1, value=stt)
    ws0.cell(row=r_idx, column=2, value=c_name)
    ws0.cell(row=r_idx, column=3, value=cpc_range)
    ws0.cell(row=r_idx, column=4, value=cap)
    ws0.cell(row=r_idx, column=5, value=grp_cnt)
    ws0.cell(row=r_idx, column=6, value=status)
    ws0.cell(row=r_idx, column=7, value=b_day)
    ws0.cell(row=r_idx, column=8, value=url)
    
    style_cell(ws0.cell(row=r_idx, column=1), alignment=align_center)
    style_cell(ws0.cell(row=r_idx, column=2), alignment=align_left, font=font_bold)
    style_cell(ws0.cell(row=r_idx, column=3), alignment=align_center)
    style_cell(ws0.cell(row=r_idx, column=4), alignment=align_right, font=font_bold, number_format="#,##0\" ₫\"")
    style_cell(ws0.cell(row=r_idx, column=5), alignment=align_center)
    style_cell(ws0.cell(row=r_idx, column=6), alignment=align_center, fill=fill_green if "ENABLED" in status else fill_yellow)
    style_cell(ws0.cell(row=r_idx, column=7), alignment=align_right, font=font_bold, number_format="#,##0\" ₫\"")
    style_cell(ws0.cell(row=r_idx, column=8), alignment=align_left)

# Section 3: Bảng Ánh Xạ Sheet (Row 26 - 35)
ws0.merge_cells("A26:H26")
c = ws0.cell(row=26, column=1, value="3. BẢNG ÁNH XẠ CÁC SHEET & PHẠM VI ĐỒNG BỘ DỮ LIỆU")
style_cell(c, font=font_sec_hdr, fill=fill_navy, alignment=align_left)

sheet_map = [
    ("00_Tổng Quan Kế Hoạch", "Điều hành", "Executive Summary, 5 thông số vận hành & Cấu trúc chiến dịch cách ly giá thầu."),
    ("01_Dự Báo KPI & Hiệu Quả Đầu Tư", "Tài chính", "Mô hình 3 kịch bản, phân tích hòa vốn, lộ trình 3 tháng theo hợp đồng demand-budget-v1."),
    ("02_Ngân Sách & Forecast Campaign", "Chiến dịch", "Bảng phân bổ ngân sách chi tiết 10 nhóm STAG Core và các nhóm mở rộng."),
    ("03_Tổng Hợp Keyword", "Dữ liệu sạch", "Toàn bộ 3.635 từ khóa đã kiểm định, bảo toàn 100% cột CPC min và CPC max."),
    ("04_Từ Khóa Cốt Lõi", "Dữ liệu sạch", "Danh sách từ khóa Cốt Lõi (Core Precision) ưu tiên ngân sách cao nhất."),
    ("05_Từ Khóa Chạy Thử", "Dữ liệu sạch", "Danh sách từ khóa Chạy Thử (Controlled Testing) có điều kiện nâng/hạ cấp."),
    ("06_MUA HÀNG (BOFU)", "Phễu chuyển đổi", "Phân nhóm từ khóa có ý định mua hàng / đăng ký dịch vụ nóng nhất."),
    ("07_CÂN NHẮC (MOFU)", "Phễu chuyển đổi", "Phân nhóm từ khóa so sánh, tìm hiểu điều kiện và bảng giá."),
    ("08_QUAN TÂM (TOFU)", "Phễu chuyển đổi", "Phân nhóm từ khóa nhận thức diện rộng phục vụ Remarketing."),
    ("09_Từ Khóa Phủ Định", "Bảo vệ ngân sách", "Bộ lọc phủ định rác ngành, từ khóa tuyển dụng việc làm, tránh click ảo."),
    ("10_Quyết Định Không Triển Khai", "Bảo vệ ngân sách", "Bảng kiểm toán 2.623 từ khóa bị loại bỏ kèm lý do chi tiết."),
    ("11_Lịch Triển Khai", "Thực thi", "Lộ trình hành động chi tiết từ Ngày 0 (Setup) đến Tuần 9+ (Scale)."),
    ("12_Rủi Ro & Dự Phòng", "Kiểm soát rủi ro", "Ma trận 5 rủi ro cốt lõi ngành di trú & phương án ứng phó.")
]

ws0.cell(row=27, column=1, value="STT")
ws0.merge_cells("B27:C27"); ws0.cell(row=27, column=2, value="Tên Sheet Trong File")
ws0.cell(row=27, column=4, value="Phân Loại")
ws0.merge_cells("E27:H27"); ws0.cell(row=27, column=5, value="Nội Dung Nghiệp Vụ & Phạm Vi Đồng Bộ")
for c_idx in range(1, 9):
    style_cell(ws0.cell(row=27, column=c_idx), font=font_tbl_hdr, fill=fill_slate, alignment=align_center)

for idx, (s_name, s_type, s_desc) in enumerate(sheet_map, 1):
    r_idx = 27 + idx
    ws0.cell(row=r_idx, column=1, value=idx)
    ws0.merge_cells(f"B{r_idx}:C{r_idx}"); ws0.cell(row=r_idx, column=2, value=s_name)
    ws0.cell(row=r_idx, column=4, value=s_type)
    ws0.merge_cells(f"E{r_idx}:H{r_idx}"); ws0.cell(row=r_idx, column=5, value=s_desc)
    
    style_cell(ws0.cell(row=r_idx, column=1), alignment=align_center)
    style_cell(ws0.cell(row=r_idx, column=2), alignment=align_left, font=font_bold)
    style_cell(ws0.cell(row=r_idx, column=3), alignment=align_left)
    style_cell(ws0.cell(row=r_idx, column=4), alignment=align_center)
    style_cell(ws0.cell(row=r_idx, column=5), alignment=align_left)
    style_cell(ws0.cell(row=r_idx, column=6), alignment=align_left)
    style_cell(ws0.cell(row=r_idx, column=7), alignment=align_left)
    style_cell(ws0.cell(row=r_idx, column=8), alignment=align_left)

col_widths_ws0 = {'A': 6, 'B': 30, 'C': 22, 'D': 18, 'E': 18, 'F': 18, 'G': 25, 'H': 35}
for col_letter, width in col_widths_ws0.items():
    ws0.column_dimensions[col_letter].width = width

print("Sheet 00 completed.")
# ==============================================================================
# SHEET 01: DỰ BÁO KPI & HIỆU QUẢ ĐẦU TƯ
# ==============================================================================
print("Creating Sheet 01_Dự Báo KPI & Hiệu Quả Đầu Tư...")
ws1 = dest_wb.create_sheet(title="01_Dự Báo KPI & Hiệu Quả Đầu Tư")
ws1.views.sheetView[0].showGridLines = True
ws1.freeze_panes = None

ws1.merge_cells("A1:G1")
c = ws1.cell(row=1, column=1, value="MÔ HÌNH DỰ BÁO TÀI CHÍNH & HIỆU QUẢ ĐẦU TƯ GOOGLE ADS (DEMAND-BUDGET-V1)")
style_cell(c, font=font_title, alignment=align_left)

ws1.merge_cells("A2:G2")
c = ws1.cell(row=2, column=1, value="Toàn bộ kết quả phụ thuộc 100% bằng công thức Excel sống. Thay đổi thông số đầu vào ở ô màu vàng để mô phỏng lại toàn bộ phễu.")
style_cell(c, font=font_subtitle, alignment=align_left)

# Table 1: 3 Kịch Bản Kinh Doanh
ws1.merge_cells("A4:G4")
c = ws1.cell(row=4, column=1, value="1. MA TRẬN DỰ BÁO 3 KỊCH BẢN KINH DOANH (THÁNG 1 - KHỞI ĐỘNG)")
style_cell(c, font=font_sec_hdr, fill=fill_navy, alignment=align_left)

headers_kpi = ["STT", "Chỉ Số Đo Lường Phễu Chuyển Đổi", "Đơn Vị", "Kịch Bản Thận Trọng", "Kịch Bản Tiêu Chuẩn (Core)", "Kịch Bản Thuận Lợi", "Công Thức Excel / Ghi Chú"]
for idx, h in enumerate(headers_kpi, 1):
    c = ws1.cell(row=5, column=idx, value=h)
    style_cell(c, font=font_tbl_hdr, fill=fill_slate, alignment=align_center)

# Rows definition for Table 1
# Row numbers in Excel will be 6 to 30
kpi_rows_data = [
    # (stt, name, unit, fmt, v_cautious, v_standard, v_favorable, formula_note, is_input)
    (1, "Tổng Lưu Lượng Tìm Kiếm Thị Trường HCM (Volume)", "Lượt/tháng", "#,##0", 2090, 2090, 2090, "Dữ liệu thực từ Google Keyword Planner cho 10 nhóm Core", True),
    (2, "Hệ Số Tiếp Cận Thị Trường (Reach Factor - R)", "%", "0.0%", 0.30, 0.50, 0.70, "Tỷ lệ hiển thị giả định trước giới hạn ngân sách (demand-budget-v1)", True),
    (3, "Lượt Hiển Thị Tiềm Năng (Impressions)", "Lượt", "#,##0", "=D6*D7", "=E6*E7", "=F6*F7", "= Volume × Reach Factor", False),
    (4, "Tỷ Lệ Nhấp Chuột Dự Kiến (CTR)", "%", "0.0%", 0.06, 0.08, 0.10, "Benchmark Search Ads vị trí đầu trang ngành di trú cao cấp", True),
    (5, "Lượt Nhấp Chuột Tiềm Năng", "Lượt", "0.0", "=D8*D9", "=E8*E9", "=F8*F9", "= Impressions × CTR", False),
    (6, "Giá Thầu CPC Thực Trả Dự Kiến", "VND", "#,##0\" ₫\"", 85000, 74477, 65000, "CPC bình quân có trọng số của 10 nhóm STAG Core", True),
    (7, "Ngân Sách Được Cấp (Allocated Budget)", "VND", "#,##0\" ₫\"", 15000000, 15000000, 15000000, "Khóa trần ngân sách 500k/ngày theo kế hoạch khởi chạy Đợt 1", True),
    (8, "Khả Năng Mua Click Theo Ngân Sách", "Lượt", "0.0", "=D12/D11", "=E12/E11", "=F12/F11", "= Ngân Sách / CPC Thực Trả", False),
    (9, "LƯỢT NHẤP DỰ BÁO (FORECAST CLICKS)", "Lượt/tháng", "0.0", "=MIN(D10,D13)", "=MIN(E10,E13)", "=MIN(F10,F13)", "= MIN(Click Tiềm Năng, Click Theo Ngân Sách)", False),
    (10, "Lượt Nhấp Dự Báo / Ngày", "Lượt/ngày", "0.00", "=D14/30", "=E14/30", "=F14/30", "= Click Tháng / 30 ngày", False),
    (11, "CHI PHÍ DỰ BÁO TIÊU ĐƯỢC (FORECAST COST)", "VND", "#,##0\" ₫\"", "=D14*D11", "=E14*E11", "=F14*F11", "= Click Dự Báo × CPC Thực Trả", False),
    (12, "Ngân Sách Chưa Dự Kiến Tiêu", "VND", "#,##0\" ₫\"", "=MAX(0,D12-D16)", "=MAX(0,E12-E16)", "=MAX(0,F12-F16)", "= Ngân Sách Cấp - Chi Phí Dự Báo (do volume hẹp)", False),
    (13, "Tỷ Lệ Chuyển Đổi Thành Lead (CVR)", "%", "0.0%", 0.015, 0.020, 0.030, "Khách bấm gọi Hotline / nhắn Zalo / điền form thẩm định", True),
    (14, "SỐ LƯỢNG LEAD DỰ BÁO (LEADS)", "Khách", "0.00", "=D14*D18", "=E14*E18", "=F14*F18", "= Click Dự Báo × CVR", False),
    (15, "Chi Phí Trên Mỗi Lead (CPA Dự Báo)", "VND", "#,##0\" ₫\"", "=IF(D19>0,D16/D19,0)", "=IF(E19>0,E16/E19,0)", "=IF(F19>0,F16/F19,0)", "= Chi Phí Dự Báo / Số Leads", False),
    (16, "Tỷ Lệ Chốt Hợp Đồng (Close Rate %)", "%", "0.0%", 0.020, 0.030, 0.045, "Tỷ lệ từ Lead thành Hợp đồng ký kết dịch vụ tư vấn di trú", True),
    (17, "SỐ HỢP ĐỒNG KÝ KẾT DỰ KIẾN (DEALS)", "Hợp đồng", "0.00", "=D19*D21", "=E19*E21", "=F19*F21", "= Leads × Close Rate", False),
    (18, "Chi Phí Khách Hàng (CAC Dự Báo)", "VND", "#,##0\" ₫\"", "=IF(D22>0,D16/D22,0)", "=IF(E22>0,E16/E22,0)", "=IF(F22>0,F16/F22,0)", "= Chi Phí Dự Báo / Số Deals", False),
    (19, "Doanh Thu Trung Bình 1 Hợp Đồng (AOV)", "VND", "#,##0\" ₫\"", 150000000, 150000000, 150000000, "Phí dịch vụ tư vấn hồ sơ di trú EB-5 & Golden Visa", True),
    (20, "TỔNG DOANH THU DỰ KIẾN (REVENUE)", "VND", "#,##0\" ₫\"", "=D22*D24", "=E22*E24", "=F22*F24", "= Số Hợp Đồng × AOV", False),
    (21, "Biên Lợi Nhuận Gộp (Gross Margin)", "%", "0.0%", 0.70, 0.70, 0.70, "Biên lãi gộp dịch vụ tư vấn sau chi phí nhân sự xử lý", True),
    (22, "Lợi Nhuận Gộp Trước Ads (Gross Profit)", "VND", "#,##0\" ₫\"", "=D25*D26", "=E25*E26", "=F25*F26", "= Doanh Thu × Gross Margin", False),
    (23, "LỢI NHUẬN SAU CHI PHÍ ADS (CONTRIBUTION)", "VND", "#,##0\" ₫\"", "=D27-D16", "=E27-E16", "=F27-F16", "= Lợi Nhuận Gộp - Chi Phí Dự Báo Ads", False),
    (24, "Tỷ Suất Doanh Thu / Chi Phí Ads (ROAS)", "Lần", "0.00\"x\"", "=IF(D16>0,D25/D16,0)", "=IF(E16>0,E25/E16,0)", "=IF(F16>0,F25/F16,0)", "= Doanh Thu / Chi Phí Dự Báo Ads", False),
    (25, "Tỷ Suất Lợi Nhuận Gộp / Chi Phí Ads (POAS)", "Lần", "0.00\"x\"", "=IF(D16>0,D27/D16,0)", "=IF(E16>0,E27/E16,0)", "=IF(F16>0,F27/F16,0)", "= Lợi Nhuận Gộp / Chi Phí Dự Báo Ads", False)
]

for idx, (stt, name, unit, fmt, vc, vs, vf, formula_note, is_input) in enumerate(kpi_rows_data, 6):
    ws1.cell(row=idx, column=1, value=stt)
    ws1.cell(row=idx, column=2, value=name)
    ws1.cell(row=idx, column=3, value=unit)
    ws1.cell(row=idx, column=4, value=vc)
    ws1.cell(row=idx, column=5, value=vs)
    ws1.cell(row=idx, column=6, value=vf)
    ws1.cell(row=idx, column=7, value=formula_note)
    
    style_cell(ws1.cell(row=idx, column=1), alignment=align_center)
    style_cell(ws1.cell(row=idx, column=2), alignment=align_left, font=font_bold if ("LƯỢT NHẤP" in name or "CHI PHÍ" in name or "SỐ LƯỢNG" in name or "SỐ HỢP ĐỒNG" in name or "TỔNG DOANH THU" in name or "LỢI NHUẬN SAU" in name) else font_regular)
    style_cell(ws1.cell(row=idx, column=3), alignment=align_center)
    
    for c_idx, val in [(4, vc), (5, vs), (6, vf)]:
        cell = ws1.cell(row=idx, column=c_idx)
        cell_font = font_bold if not is_input else font_regular
        cell_fill = fill_yellow if is_input else (fill_green if idx in [14, 16, 21, 23, 26, 28] else fill_gray)
        style_cell(cell, font=cell_font, fill=cell_fill, alignment=align_right, number_format=fmt)
    
    style_cell(ws1.cell(row=idx, column=7), alignment=align_left, font=font_italic)

# Table 2: Phân Tích Điểm Hòa Vốn (Row 33 - 39)
ws1.merge_cells("A32:G32")
c = ws1.cell(row=32, column=1, value="2. PHÂN TÍCH ĐIỂM HÒA VỐN QUẢNG CÁO (BREAK-EVEN ANALYSIS)")
style_cell(c, font=font_sec_hdr, fill=fill_navy, alignment=align_left)

be_headers = ["STT", "Chỉ Tiêu Điểm Hòa Vốn", "Đơn Vị", "Công Thức Xác Định", "Giá Trị Hòa Vốn (Kịch Bản Chuẩn)", "Đánh Giá Khả Thi Thực Tế", "Ghi Chú Nghiệp Vụ"]
for idx, h in enumerate(be_headers, 1):
    c = ws1.cell(row=33, column=idx, value=h)
    style_cell(c, font=font_tbl_hdr, fill=fill_slate, alignment=align_center)

be_rows = [
    (1, "Doanh Thu Cần Đạt Để Hòa Vốn Chi Phí Ads", "VND", "=E16/E26", "#,##0\" ₫\"", "Cực kỳ khả thi", "Chỉ cần 8,24 triệu doanh thu là hòa vốn chi phí Ads tháng!"),
    (2, "Số Hợp Đồng Tối Thiểu Để Hòa Vốn (Deals)", "Hợp đồng", "=E16/(E24*E26)", "0.00", "0.06 Hợp đồng", "Chưa tới 1/10 hợp đồng 150M đã đủ bù đắp toàn bộ chi phí Ads."),
    (3, "Số Lượng Lead Tối Thiểu Cần Có Để Hòa Vốn", "Khách", "=(E16/(E24*E26))/E21", "0.00", "1.83 Leads", "Chỉ cần đạt ~2 leads chất lượng trong tháng là nắm chắc hòa vốn."),
    (4, "Chi Phí Tối Đa Cho 1 Hợp Đồng (Max CAC Trần)", "VND", "=E24*E26", "#,##0\" ₫\"", "105.000.000 ₫", "Giới hạn trần để chiến dịch không bị lỗ vốn nghiệp vụ.")
]

for idx, (stt, name, unit, formula, fmt, assess, note) in enumerate(be_rows, 34):
    ws1.cell(row=idx, column=1, value=stt)
    ws1.cell(row=idx, column=2, value=name)
    ws1.cell(row=idx, column=3, value=unit)
    ws1.cell(row=idx, column=4, value=formula)
    ws1.cell(row=idx, column=5, value=assess)
    ws1.cell(row=idx, column=6, value=note)
    ws1.merge_cells(f"F{idx}:G{idx}")
    
    style_cell(ws1.cell(row=idx, column=1), alignment=align_center)
    style_cell(ws1.cell(row=idx, column=2), alignment=align_left, font=font_bold)
    style_cell(ws1.cell(row=idx, column=3), alignment=align_center)
    style_cell(ws1.cell(row=idx, column=4), alignment=align_right, font=font_bold, fill=fill_green, number_format=fmt)
    style_cell(ws1.cell(row=idx, column=5), alignment=align_center, font=font_bold)
    style_cell(ws1.cell(row=idx, column=6), alignment=align_left)
    style_cell(ws1.cell(row=idx, column=7), alignment=align_left)

col_widths_ws1 = {'A': 6, 'B': 38, 'C': 14, 'D': 22, 'E': 24, 'F': 22, 'G': 40}
for col_letter, width in col_widths_ws1.items():
    ws1.column_dimensions[col_letter].width = width

print("Sheet 01 completed.")
# ==============================================================================
# SHEET 02: NGÂN SÁCH & FORECAST CAMPAIGN
# ==============================================================================
print("Creating Sheet 02_Ngân Sách & Forecast Campaign...")
ws2 = dest_wb.create_sheet(title="02_Ngân Sách & Forecast Campaign")
ws2.views.sheetView[0].showGridLines = True
ws2.freeze_panes = None

ws2.merge_cells("A1:P1")
c = ws2.cell(row=1, column=1, value="PHÂN BỔ NGÂN SÁCH CHI TIẾT & DỰ BÁO CẤP NHÓM STAG (DEMAND-BUDGET-V1)")
style_cell(c, font=font_title, alignment=align_left)

ws2.merge_cells("A2:P2")
c = ws2.cell(row=2, column=1, value="Khóa cứng 10 nhóm STAG Cốt Lõi (Đợt 1) nuôi đủ 5–10 clicks/nhóm/ngày. Áp dụng giới hạn Max CPC Cap = CPC TB × 1.25.")
style_cell(c, font=font_subtitle, alignment=align_left)

ws2.merge_cells("A4:P4")
c = ws2.cell(row=4, column=1, value="1. DANH SÁCH 10 NHÓM STAG CỐT LÕI KHỞI CHẠY (ĐỢT 1 - BẬT NGAY)")
style_cell(c, font=font_sec_hdr, fill=fill_navy, alignment=align_left)

headers_stag = [
    "STT", "Chiến Dịch", "Tên Nhóm STAG", "Trạng Thái", "Đợt Bật", 
    "Số KW", "Volume HCM", "CPC TB (₫)", "Max CPC Cap (₫)", "Click/Ngày Dự Báo", 
    "Ngân Sách Ngày (₫)", "Ngân Sách Tháng (₫)", "Chi Phí Dự Báo (₫)", "Leads Dự Báo", 
    "Tiêu Đề RSA Mẫu (≤30 ký tự)", "URL Trang Đích"
]

for idx, h in enumerate(headers_stag, 1):
    c = ws2.cell(row=5, column=idx, value=h)
    style_cell(c, font=font_tbl_hdr, fill=fill_slate, alignment=align_center)

stag_10_data = [
    (1, "GGSearch_DinhCu_EB5_My_HighCPC", "STAG_EB5_DauTu_DinhCu_01_02", "ENABLED", "ĐỢT 1 - BẬT NGAY", 7, 640, 104345.79, "=H6*1.25", 0.58, 60000, 1800000, 1800000, 0.35, "Đầu Tư Định Cư Mỹ EB-5", "https://www.visagbluesea.com/us-green-card-eb-5"),
    (2, "GGSearch_DinhCu_EB5_My_HighCPC", "STAG_EB5_DauTu_DinhCu_01_01", "ENABLED", "ĐỢT 1 - BẬT NGAY", 8, 600, 74476.63, "=H7*1.25", 0.80, 60000, 1800000, 1787439, 0.48, "Đầu Tư Định Cư Mỹ EB-5", "https://www.visagbluesea.com/us-green-card-eb-5"),
    (3, "GGSearch_DinhCu_GoldenVisa_ChauAu", "STAG_GoldenVisa_Sip", "ENABLED", "ĐỢT 1 - BẬT NGAY", 8, 340, 60663.63, "=H8*1.25", 0.45, 50000, 1500000, 825025, 0.27, "Định Cư Síp Diện Đầu Tư", "https://www.visagbluesea.com/golden-visa-cyprus"),
    (4, "GGSearch_DinhCu_GoldenVisa_ChauAu", "STAG_GoldenVisa_HyLap_BDS_DauTu", "ENABLED", "ĐỢT 1 - BẬT NGAY", 6, 140, 48973.92, "=H9*1.25", 0.19, 50000, 1500000, 274254, 0.11, "Golden Visa Hy Lạp Mua Nhà", "https://www.visagbluesea.com/golden-visa-greece"),
    (5, "GGSearch_DinhCu_EB5_My_HighCPC", "STAG_EB5_DauTu_DinhCu_02_01", "ENABLED", "ĐỢT 1 - BẬT NGAY", 7, 110, 120721.64, "=H10*1.25", 0.15, 50000, 1500000, 531175, 0.09, "Đầu Tư Định Cư Mỹ EB-5", "https://www.visagbluesea.com/us-green-card-eb-5"),
    (6, "GGSearch_DinhCu_EB5_My_MidCPC", "STAG_EB5_DauTu_DinhCu_02_02", "ENABLED", "ĐỢT 1 - BẬT NGAY", 7, 90, 47976.57, "=H11*1.25", 0.12, 50000, 1500000, 172716, 0.07, "Đầu Tư Định Cư Mỹ EB-5", "https://www.visagbluesea.com/us-green-card-eb-5"),
    (7, "GGSearch_DinhCu_EB5_My_MidCPC", "STAG_EB5_DauTu_DinhCu_03_01", "ENABLED", "ĐỢT 1 - BẬT NGAY", 7, 70, 45578.00, "=H12*1.25", 0.09, 50000, 1500000, 127618, 0.06, "Đầu Tư Định Cư Mỹ EB-5", "https://www.visagbluesea.com/us-green-card-eb-5"),
    (8, "GGSearch_DinhCu_EB5_My_MidCPC", "STAG_EB5_DauTu_DinhCu_04", "ENABLED", "ĐỢT 1 - BẬT NGAY", 7, 70, 45000.00, "=H13*1.25", 0.09, 50000, 1500000, 126000, 0.06, "Đầu Tư Định Cư Mỹ EB-5", "https://www.visagbluesea.com/us-green-card-eb-5"),
    (9, "GGSearch_DinhCu_EB5_My_MidCPC", "STAG_EB5_DauTu_DinhCu_03_02", "ENABLED", "ĐỢT 1 - BẬT NGAY", 7, 40, 45000.00, "=H14*1.25", 0.05, 40000, 1200000, 72000, 0.03, "Đầu Tư Định Cư Mỹ EB-5", "https://www.visagbluesea.com/us-green-card-eb-5"),
    (10, "GGSearch_DinhCu_EB5_My_MidCPC", "STAG_EB5_DauTu_DinhCu_05", "ENABLED", "ĐỢT 1 - BẬT NGAY", 7, 30, 45000.00, "=H15*1.25", 0.04, 40000, 1200000, 54000, 0.02, "Đầu Tư Định Cư Mỹ EB-5", "https://www.visagbluesea.com/us-green-card-eb-5")
]

for idx, row_val in enumerate(stag_10_data, 6):
    for c_idx, val in enumerate(row_val, 1):
        cell = ws2.cell(row=idx, column=c_idx, value=val)
        if c_idx in [1]: style_cell(cell, alignment=align_center)
        elif c_idx in [2, 3]: style_cell(cell, alignment=align_left, font=font_bold)
        elif c_idx in [4]: style_cell(cell, alignment=align_center, font=font_bold, fill=fill_green)
        elif c_idx in [5]: style_cell(cell, alignment=align_center)
        elif c_idx in [6, 7]: style_cell(cell, alignment=align_right, number_format="#,##0")
        elif c_idx in [8, 9]: style_cell(cell, alignment=align_right, font=font_bold, number_format="#,##0\" ₫\"")
        elif c_idx in [10]: style_cell(cell, alignment=align_right, number_format="0.00")
        elif c_idx in [11, 12, 13]: style_cell(cell, alignment=align_right, font=font_bold, fill=fill_yellow if c_idx==12 else None, number_format="#,##0\" ₫\"")
        elif c_idx in [14]: style_cell(cell, alignment=align_right, font=font_bold, fill=fill_green, number_format="0.00")
        elif c_idx in [15, 16]: style_cell(cell, alignment=align_left)

# Total Row
ws2.cell(row=16, column=1, value="TỔNG")
ws2.cell(row=16, column=2, value="10 Nhóm STAG Khởi Chạy")
ws2.cell(row=16, column=3, value="")
ws2.cell(row=16, column=4, value="10 ENABLED")
ws2.cell(row=16, column=5, value="ĐỢT 1")
ws2.cell(row=16, column=6, value="=SUM(F6:F15)")
ws2.cell(row=16, column=7, value="=SUM(G6:G15)")
ws2.cell(row=16, column=8, value="=AVERAGE(H6:H15)")
ws2.cell(row=16, column=9, value="=AVERAGE(I6:I15)")
ws2.cell(row=16, column=10, value="=SUM(J6:J15)")
ws2.cell(row=16, column=11, value="=SUM(K6:K15)")
ws2.cell(row=16, column=12, value="=SUM(L6:L15)")
ws2.cell(row=16, column=13, value="=SUM(M6:M15)")
ws2.cell(row=16, column=14, value="=SUM(N6:N15)")
ws2.cell(row=16, column=15, value="Toàn bộ nhóm đạt chuẩn STAG 100%")
ws2.cell(row=16, column=16, value="")

for c_idx in range(1, 17):
    cell = ws2.cell(row=16, column=c_idx)
    fmt = "#,##0\" ₫\"" if c_idx in [8, 9, 11, 12, 13] else ("0.00" if c_idx in [10, 14] else ("#,##0" if c_idx in [6, 7] else None))
    style_cell(cell, font=font_bold, fill=fill_blue, border=double_bottom, number_format=fmt, alignment=align_right if c_idx in [6,7,8,9,10,11,12,13,14] else align_center)

col_widths_ws2 = {
    'A': 6, 'B': 32, 'C': 32, 'D': 14, 'E': 18, 
    'F': 10, 'G': 14, 'H': 15, 'I': 16, 'J': 16, 
    'K': 18, 'L': 20, 'M': 20, 'N': 14, 'O': 28, 'P': 42
}
for col_letter, width in col_widths_ws2.items():
    ws2.column_dimensions[col_letter].width = width

print("Sheet 02 completed.")

# ==============================================================================
# COPYING AUDITED KEYWORD SHEETS (Sheets 03 - 10)
# ==============================================================================
sheet_copy_mapping = [
    ("Tổng Hợp", "03_Tổng Hợp Keyword"),
    ("Từ Khóa Chạy Ngay (Cốt Lõi)", "04_Từ Khóa Cốt Lõi"),
    ("Từ Khóa Chạy Thử (Theo Dõi)", "05_Từ Khóa Chạy Thử"),
    ("MUA HÀNG (BOFU)", "06_MUA HÀNG (BOFU)"),
    ("CÂN NHẮC (MOFU)", "07_CÂN NHẮC (MOFU)"),
    ("QUAN TÂM (TOFU)", "08_QUAN TÂM (TOFU)"),
    ("Từ Khóa Phủ Định", "09_Từ Khóa Phủ Định"),
    ("Quyết Định Không Triển Khai", "10_Quyết Định Không Triển Khai")
]

for src_name, dest_name in sheet_copy_mapping:
    if src_name in src_wb.sheetnames:
        print(f"Copying {src_name} -> {dest_name}...")
        dest_sheet = dest_wb.create_sheet(title=dest_name)
        copy_sheet(src_wb[src_name], dest_sheet)
    else:
        print(f"Warning: Sheet {src_name} not found in source workbook!")

# ==============================================================================
# SHEET 11: LỊCH TRIỂN KHAI
# ==============================================================================
print("Creating Sheet 11_Lịch Triển Khai...")
ws11 = dest_wb.create_sheet(title="11_Lịch Triển Khai")
ws11.views.sheetView[0].showGridLines = True
ws11.freeze_panes = None

ws11.merge_cells("A1:G1")
c = ws11.cell(row=1, column=1, value="LỘ TRÌNH KÍCH HOẠT & VẬN HÀNH CHIẾN DỊCH GOOGLE ADS (NGÀY 0 ➔ TUẦN 9+)")
style_cell(c, font=font_title, alignment=align_left)

ws11.merge_cells("A2:G2")
c = ws11.cell(row=2, column=1, value="Quy trình 5 giai đoạn kỷ luật cao: Chuẩn bị ➔ Khởi động ➔ Tối ưu hàng ngày ➔ Máy học chuyển đổi ➔ Mở rộng quy mô.")
style_cell(c, font=font_subtitle, alignment=align_left)

timeline_headers = ["STT", "Giai Đoạn / Mốc Thời Gian", "Hạng Mục Triển Khai Chính", "Chiến Lược Giá Thầu & Ngân Sách", "Chỉ Số Kiểm Soát (Gate KPIs)", "Người Thực Hiện", "Trạng Thái"]
for idx, h in enumerate(timeline_headers, 1):
    c = ws11.cell(row=4, column=idx, value=h)
    style_cell(c, font=font_tbl_hdr, fill=fill_slate, alignment=align_center)

timeline_steps = [
    (1, "Ngày 0: Pre-Launch Setup", "Setup cấu trúc 10 nhóm STAG ở trạng thái PAUSED trên Google Ads. Cài đặt GTM tracking Hotline, Zalo, Form, Tracking Guard chống click ảo <10s.", "Chưa kích hoạt chi tiêu", "Test bắn chuyển đổi GTM 100% khớp, không trùng lặp.", "Google Ads Specialist", "Sẵn sàng"),
    (2, "Tuần 1: Khởi Động Đợt 1 (Cold Start)", "Chuyển trạng thái 10 nhóm STAG Core sang ENABLED. Áp dụng cách ly Campaign High-CPC vs Mid-CPC.", "Maximize Clicks + Max CPC Cap (1.25x). Ngân sách 500k/ngày.", "Tỷ lệ hiển thị đạt > 50%, CPC thực ≤ Max CPC Cap.", "Ads Lead", "Chờ Sếp duyệt"),
    (3, "Tuần 2–3: Daily Search Terms Audit", "Mở Báo cáo Cụm từ tìm kiếm hàng ngày. Phủ định ngay các biến thể rác (tuyển dụng, việc làm, khách cũ tìm hotline). Tinh chỉnh tiêu đề RSA.", "Giữ nguyên Maximize Clicks. Chưa ép Smart Bidding.", "CTR ≥ 6%, Tỷ lệ Search Terms sạch ≥ 90%.", "Auditor / Ads Team", "Kế hoạch"),
    (4, "Tuần 4: Đánh Giá Tín Hiệu Chuyển Đổi", "Rà soát lượng Lead thu về. Nếu đạt ≥ 15–30 chuyển đổi hợp lệ trong tháng, chuẩn bị chuyển sang Maximize Conversions.", "Maximize Conversions (không đặt Target CPA vội để máy học).", "CVR ≥ 2.0%, CPA thực tế ≤ 3.500.000 ₫/lead.", "Ads Manager", "Kế hoạch"),
    (5, "Tuần 5–8: Mở Rộng Đợt 2 (Wave 2 Expansion)", "Bật tiếp các nhóm Cốt lõi Đợt 2: Du học Phần Lan mũi nhọn, Visa các nước (Úc, Schengen, Mỹ). Bổ sung ngân sách lên 30M/tháng.", "Tách Campaign du học riêng với mức CPC 20k–30k. Áp dụng tCPA.", "Nuôi đủ 5–10 clicks/nhóm/ngày cho các nhóm mới bật.", "Ads Team", "Kế hoạch"),
    (6, "Tuần 9+: Scale Ngân Sách & Dominate", "Đạt ngưỡng ≥ 50 chuyển đổi/tháng: Áp dụng Target CPA = CPA thực × 110%. Mở rộng Remarketing Search Ads (RLSA) và PMax.", "Target CPA / Target ROAS. Tăng ngân sách 50M–100M.", "POAS ≥ 3.0x, Doanh thu hợp đồng tăng trưởng ổn định.", "Board & Ads Lead", "Kế hoạch")
]

for idx, (stt, phase, task, bid_strat, kpi_gate, owner, status) in enumerate(timeline_steps, 5):
    ws11.cell(row=idx, column=1, value=stt)
    ws11.cell(row=idx, column=2, value=phase)
    ws11.cell(row=idx, column=3, value=task)
    ws11.cell(row=idx, column=4, value=bid_strat)
    ws11.cell(row=idx, column=5, value=kpi_gate)
    ws11.cell(row=idx, column=6, value=owner)
    ws11.cell(row=idx, column=7, value=status)
    
    style_cell(ws11.cell(row=idx, column=1), alignment=align_center)
    style_cell(ws11.cell(row=idx, column=2), alignment=align_left, font=font_bold)
    style_cell(ws11.cell(row=idx, column=3), alignment=align_left)
    style_cell(ws11.cell(row=idx, column=4), alignment=align_left)
    style_cell(ws11.cell(row=idx, column=5), alignment=align_left, font=font_italic)
    style_cell(ws11.cell(row=idx, column=6), alignment=align_center)
    style_cell(ws11.cell(row=idx, column=7), alignment=align_center, fill=fill_green if status=="Sẵn sàng" else fill_yellow)

col_widths_ws11 = {'A': 6, 'B': 24, 'C': 38, 'D': 35, 'E': 32, 'F': 20, 'G': 16}
for col_letter, width in col_widths_ws11.items():
    ws11.column_dimensions[col_letter].width = width

print("Sheet 11 completed.")

# ==============================================================================
# SHEET 12: RỦI RO & DỰ PHÒNG
# ==============================================================================
print("Creating Sheet 12_Rủi Ro & Dự Phòng...")
ws12 = dest_wb.create_sheet(title="12_Rủi Ro & Dự Phòng")
ws12.views.sheetView[0].showGridLines = True
ws12.freeze_panes = None

ws12.merge_cells("A1:F1")
c = ws12.cell(row=1, column=1, value="MA TRẬN RỦI RO & KẾ HOẠCH DỰ PHÒNG BẢO VỆ NGÂN SÁCH (RISK MANAGEMENT)")
style_cell(c, font=font_title, alignment=align_left)

ws12.merge_cells("A2:F2")
c = ws12.cell(row=2, column=1, value="Nhận diện 5 rủi ro chí mạng của ngành di trú & visa cao cấp và cơ chế khóa chốt phòng thủ ngay từ đầu.")
style_cell(c, font=font_subtitle, alignment=align_left)

risk_headers = ["STT", "Rủi Ro Nhận Diện", "Mức Độ Rủi Ro", "Nguyên Nhân Cốt Lõi", "Cơ Chế Khóa Chốt Phòng Thủ", "Kế Hoạch Khắc Phục Khi Xảy Ra"]
for idx, h in enumerate(risk_headers, 1):
    c = ws12.cell(row=4, column=idx, value=h)
    style_cell(c, font=font_tbl_hdr, fill=fill_slate, alignment=align_center)

risks_data = [
    (1, "Click ảo / Đối thủ phá hoại ngân sách", "CAO", "Ngành di trú có CPC cao (50k–120k), đối thủ hoặc bot có thể cố tình nhấp chuột làm cạn tiền.", "Khóa cứng Tracking Guard chỉ ghi nhận chuyển đổi khi ở lại trang >10s. Cài Cloudflare Turnstile cho form liên hệ.", "Trích xuất IP nghi vấn hàng ngày từ web log, đưa ngay vào danh sách loại trừ IP trên Google Ads."),
    (2, "Bóp nghẹt hiển thị vì đặt Max CPC quá thấp", "CAO", "Chiến lược Maximize Clicks có trần giá thầu: nếu đặt trần < CPC sàn đấu giá, tỷ lệ hiển thị rớt về 0%.", "Áp dụng quy tắc CPC Dispersion Guard: Max CPC Cap = CPC TB × 1.25. Tách riêng Campaign High-CPC (130k) vs Mid-CPC (58k).", "Nâng nhẹ trần Max CPC thêm 15% sau 48h nếu impression = 0."),
    (3, "Thiếu volume do chỉ nhắm khu vực TP.HCM", "TRUNG BÌNH", "Các từ khóa hẹp EB-5 và Golden Visa có lượng tìm kiếm tại HCM ~2.000 lượt/tháng, có thể không tiêu hết ngân sách.", "Tập trung tối đa vào độ chính xác (Precision First). Phần ngân sách chưa tiêu không mất đi mà bảo toàn vốn an toàn.", "Sau 2 tuần, nếu muốn tiêu thêm, mở rộng sang Đợt 2 (Du học Phần Lan mũi nhọn) hoặc mở bán kính chạy ra Hà Nội & Toàn quốc."),
    (4, "Lead về nhưng không chốt được hợp đồng", "CAO", "Khách hàng di trú có chu kỳ cân nhắc 3–12 tháng. Nếu Sale chỉ gọi tư vấn chung chung mà không chứng minh được năng lực pháp lý sẽ mất khách.", "Website phải có 'Bộ Thẩm Định Hồ Sơ 1-1 Cùng Luật Sư'. Minh bạch quy trình tiền thẩm định 3 vòng và cấu trúc an toàn vốn.", "Audit quy trình tư vấn của Sales; cung cấp bản lộ trình di trú cá nhân hóa cho khách trong vòng 24 giờ."),
    (5, "Vi phạm chính sách Google Ads về dịch vụ tài chính/di trú", "TRUNG BÌNH", "Google quét gắt gao các cam kết về thẻ xanh, cam kết định cư 100% hoặc hoàn vốn đầu tư.", "Mẫu quảng cáo RSA tuyệt đối không dùng từ 'Cam kết 100% có thẻ xanh' hay 'Bảo đảm lợi nhuận'. Chỉ dùng: 'Đồng Hành Pháp Lý', 'Tiền Thẩm Định 3 Vòng'.", "Nếu bị disapproved mẫu quảng cáo nào, chỉnh sửa từ ngữ ngay trong 2 giờ và yêu cầu xem xét lại.")
]

for idx, (stt, r_name, r_lvl, r_cause, r_guard, r_fix) in enumerate(risks_data, 5):
    ws12.cell(row=idx, column=1, value=stt)
    ws12.cell(row=idx, column=2, value=r_name)
    ws12.cell(row=idx, column=3, value=r_lvl)
    ws12.cell(row=idx, column=4, value=r_cause)
    ws12.cell(row=idx, column=5, value=r_guard)
    ws12.cell(row=idx, column=6, value=r_fix)
    
    style_cell(ws12.cell(row=idx, column=1), alignment=align_center)
    style_cell(ws12.cell(row=idx, column=2), alignment=align_left, font=font_bold)
    style_cell(ws12.cell(row=idx, column=3), alignment=align_center, font=font_bold, fill=fill_yellow if r_lvl=="CAO" else fill_green)
    style_cell(ws12.cell(row=idx, column=4), alignment=align_left)
    style_cell(ws12.cell(row=idx, column=5), alignment=align_left, font=font_bold)
    style_cell(ws12.cell(row=idx, column=6), alignment=align_left, font=font_italic)

col_widths_ws12 = {'A': 6, 'B': 28, 'C': 15, 'D': 35, 'E': 40, 'F': 40}
for col_letter, width in col_widths_ws12.items():
    ws12.column_dimensions[col_letter].width = width

print("Sheet 12 completed.")

# Copy Sheet 13: Biên Bản Chuyển Nhóm
if "02_Biên Bản Chuyển Nhóm" in src_wb.sheetnames:
    print("Copying 02_Biên Bản Chuyển Nhóm -> 13_Biên Bản Chuyển Nhóm...")
    ws13 = dest_wb.create_sheet(title="13_Biên Bản Chuyển Nhóm")
    copy_sheet(src_wb["02_Biên Bản Chuyển Nhóm"], ws13)

# Save Workbook
out_path_root = "Google_Ads_Plan_V2_GBlueSea_202611.xlsx"
out_path_kp = "Keyword Planner/Google_Ads_Plan_V2_GBlueSea_202611.xlsx"

print(f"Saving workbook to {out_path_root} and {out_path_kp}...")
dest_wb.save(out_path_root)
dest_wb.save(out_path_kp)
print("SUCCESS: Plan V2 Workbook generated successfully!")
