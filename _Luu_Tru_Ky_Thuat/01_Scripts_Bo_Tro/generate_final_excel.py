import os
import sys
from pathlib import Path

# Add scripts directory
sys.path.append(r"C:\Users\ADMIN\.gemini\config\skills\download-keyword-planner (ggads)\scripts")
from auto_keyword_planner import (
    parse_keyword_planner_file,
    normalize_keyword,
    export_master_excel
)

sys.stdout.reconfigure(encoding="utf-8")

output_dir = Path("./Keyword Planner")
staging_dir = Path("_Luu_Tru_Ky_Thuat/Keyword_Planner_Raw")

# 1. Collect all 23 raw files and deduplicate while tagging origin seed groups
raw_files = sorted(list(staging_dir.glob("Raw_*.csv")))
print(f"📁 Tìm thấy {len(raw_files)} tệp dữ liệu thô từ 23 nhóm Seed Keywords:")

group_files = {}
for p in raw_files:
    # Extract group name from file name: Raw_01. Đầu tư định cư Mỹ EB-5_1793466832.csv
    parts = p.stem.split("_")
    if len(parts) >= 2:
        grp_name = parts[1]
    else:
        grp_name = p.stem
    group_files[grp_name] = p
    print(f"  • {grp_name}: {p.name}")

seen_normalized = set()
unique_keywords = []
master_rows = []

for grp_name, file_path in group_files.items():
    rows = parse_keyword_planner_file(file_path)
    for r in rows:
        kw = r.get("Keyword", "").strip()
        if not kw or kw.lower() in ["keyword", "từ khóa", "tổng cộng", "total", "tất cả"]:
            continue
        norm = normalize_keyword(kw)
        if norm and norm not in seen_normalized:
            seen_normalized.add(norm)
            unique_keywords.append(kw)
            r["_Seed_Group"] = grp_name
            r["_Original_KW"] = kw
            master_rows.append(r)

print(f"\n✨ TỔNG TỪ KHÓA ĐỘC NHẤT ĐÃ ĐƯỢC LỌC TRÙNG: {len(unique_keywords)} từ khóa")

# 2. Historical Metrics file for Hồ Chí Minh
historical_file = staging_dir / "Historical_Metrics_HCM_Real.csv"
if not historical_file.exists():
    print(f"❌ Không tìm thấy file {historical_file}")
    sys.exit(1)

print(f"📊 Đang gắn số liệu lượng tìm kiếm thực tế và dải giá thầu tại Hồ Chí Minh...")

# 3. Export Master Excel
locations = ["Thành phố Hồ Chí Minh"]
final_excel = export_master_excel(
    output_dir=output_dir,
    historical_file=historical_file,
    unique_keywords=unique_keywords,
    master_rows=master_rows,
    target_locations=locations
)

print(f"\n🎉 XUẤT MASTER EXCEL THÀNH CÔNG: {final_excel.resolve()}")
print(f"📁 Kích thước file: {final_excel.stat().st_size} bytes")
