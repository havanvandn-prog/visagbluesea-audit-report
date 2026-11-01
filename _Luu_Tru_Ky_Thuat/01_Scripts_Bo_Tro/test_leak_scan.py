import sys
import os
import re
import json
import pandas as pd
import numpy as np
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

sys.stdout.reconfigure(encoding='utf-8')

print("Starting Skill 07.1 Post-Audit Engine...")

# 1. Load Data from V4 Master Excel
excel_v4_path = 'Keyword Planner/03_Phan_Tich_Tu_Khoa_V4_visagbluesea.xlsx'
df_active_raw = pd.read_excel(excel_v4_path, sheet_name='Tổng Hợp', skiprows=3)
df_drop_raw = pd.read_excel(excel_v4_path, sheet_name='Quyết Định Không Triển Khai', skiprows=3)

print(f"Loaded from V4: Active = {len(df_active_raw)} rows, Drop = {len(df_drop_raw)} rows.")

# 2. AUDIT STEP 1: Scan for Leaked Junk (Quy tắc 6)
# Check for recruitment/job seeking phrases that slipped through
job_keywords_mask = df_active_raw['E. TỪ KHÓA'].str.contains(
    r'(tuyển dụng|tuyen dung|tìm việc|tim viec|việc làm|viec lam|cần thợ|tuyển thợ|thợ nail|làm nail|tuyển công nhân|xklđ|xkld|xuất khẩu lao động|nhân viên tư vấn|chuyên viên tư vấn|chuyên gia tư vấn|tuyển cộng tác viên|tuyen nhan vien|tuyển tư vấn|cách tư vấn du học|mẫu cv|xin việc)',
    case=False, na=False
)

leaked_jobs = df_active_raw[job_keywords_mask].copy()
print(f"Detected leaked job/recruitment keywords: {len(leaked_jobs)}")

# Check for non-target destinations (Korea, Japan, China, etc. that GBlueSea doesn't focus on)
other_dest_mask = df_active_raw['E. TỪ KHÓA'].str.contains(
    r'(du học hàn|du học nhật|du học trung quốc|du học đài loan|du học nga|du học philippines)',
    case=False, na=False
)
leaked_dest = df_active_raw[other_dest_mask].copy()
print(f"Detected other irrelevant destinations: {len(leaked_dest)}")

# Exclude leaked keywords from active list and move to drop
all_leaked_mask = job_keywords_mask | other_dest_mask
df_new_drops = df_active_raw[all_leaked_mask].copy()
df_active_clean = df_active_raw[~all_leaked_mask].copy().reset_index(drop=True)

print(f"Remaining clean active keywords: {len(df_active_clean)}")
print(f"Newly disqualified keywords: {len(df_new_drops)}")
