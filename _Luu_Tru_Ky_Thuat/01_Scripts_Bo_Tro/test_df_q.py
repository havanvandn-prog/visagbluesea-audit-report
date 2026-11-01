import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

# Let's run a test on the first 100 rows
from build_v4_master_excel import df_all, qualify_keyword

print(f"df_all initial length: {len(df_all)}")
rows = [qualify_keyword(row) for idx, row in df_all.head(50).iterrows()]
df_q = pd.DataFrame(rows)
print("Columns in df_q for first 50 rows:", df_q.columns.tolist())

# Run on all
rows_all = [qualify_keyword(row) for idx, row in df_all.iterrows()]
df_q_all = pd.DataFrame(rows_all)
print("Columns in df_q_all:", df_q_all.columns.tolist())
print("Value counts of lop_trien_khai:")
print(df_q_all['lop_trien_khai'].value_counts())
if 'chien_dich' in df_q_all.columns:
    print("chien_dich is present! Not null count:", df_q_all['chien_dich'].notna().sum())
else:
    print("chien_dich is NOT in df_q_all!")
