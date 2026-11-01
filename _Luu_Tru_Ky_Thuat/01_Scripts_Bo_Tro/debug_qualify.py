import sys
import pandas as pd
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/build_v4_master_excel.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the qualify_keyword function text
start_idx = text.find("def qualify_keyword(row):")
end_idx = text.find("df_all = df_all.reset_index(drop=True)")

exec(text[start_idx:end_idx], globals())

test_row = pd.Series({
    'keyword': 'định cư mỹ eb5',
    'kw_norm': 'định cư mỹ eb5',
    'volume': 390.0,
    'low_bid': 25000.0,
    'high_bid': 80000.0
})

res = qualify_keyword(test_row)
print("Result for 'định cư mỹ eb5':", res)

# Check some keywords that become CORE in test_classification
from test_classification import df_classified
print("Sample Core from test_classification:")
core_sample = df_classified[df_classified['lop_trien_khai'] == 'CỐT LÕI'].head(3)
for idx, r in core_sample.iterrows():
    print("Keyword:", r['keyword'])
    print("build_v4 result:", qualify_keyword(r))
