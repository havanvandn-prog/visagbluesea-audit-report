import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Loading audited workbook...")
src_wb = openpyxl.load_workbook('Keyword Planner/04_Kiem_Dinh_Va_Tai_Cau_Truc_Keyword_visagbluesea.xlsx', data_only=False)
print("Source sheets:", src_wb.sheetnames)

with open('Keyword Planner/kw-summary-v4-audited.json', 'r', encoding='utf-8') as f:
    summary_data = json.load(f)

print("Building Plan V2 workbook...")
wb = openpyxl.Workbook()
# remove default sheet
wb.remove(wb.active)

# Color palettes
NAVY_HEADER = "1E3A8A"
EMERALD_HEADER = "065F46"
SLATE_HEADER = "1E293B"
BLUE_BG = "EFF6FF"
GREEN_BG = "ECFDF5"
YELLOW_BG = "FEF9C3"
GRAY_BG = "F1F5F9"
WHITE = "FFFFFF"

font_title = Font(name="Calibri", size=15, bold=True, color="1E3A8A")
font_subtitle = Font(name="Calibri", size=11, italic=True, color="475569")
font_sec_hdr = Font(name="Calibri", size=12, bold=True, color=WHITE)
font_tbl_hdr = Font(name="Calibri", size=10, bold=True, color=WHITE)
font_bold = Font(name="Calibri", size=10, bold=True)
font_regular = Font(name="Calibri", size=10)
font_italic = Font(name="Calibri", size=9, italic=True, color="64748B")

fill_navy = PatternFill(start_color=NAVY_HEADER, end_color=NAVY_HEADER, fill_type="solid")
fill_emerald = PatternFill(start_color=EMERALD_HEADER, end_color=EMERALD_HEADER, fill_type="solid")
fill_slate = PatternFill(start_color=SLATE_HEADER, end_color=SLATE_HEADER, fill_type="solid")
fill_blue = PatternFill(start_color=BLUE_BG, end_color=BLUE_BG, fill_type="solid")
fill_green = PatternFill(start_color=GREEN_BG, end_color=GREEN_BG, fill_type="solid")
fill_yellow = PatternFill(start_color=YELLOW_BG, end_color=YELLOW_BG, fill_type="solid")
fill_gray = PatternFill(start_color=GRAY_BG, end_color=GRAY_BG, fill_type="solid")

thin_border_side = Side(border_style="thin", color="CBD5E1")
thin_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
double_bottom_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=Side(border_style="double", color="1E3A8A"))

print("Script template ready.")
