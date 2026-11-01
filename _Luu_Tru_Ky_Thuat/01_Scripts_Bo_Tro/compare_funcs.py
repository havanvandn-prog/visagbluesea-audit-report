import sys
from test_classification import classify_keyword
from build_v4_master_excel import qualify_keyword
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

test_row = {
    'kw_norm': 'định cư mỹ eb5',
    'volume': 390.0,
    'low_bid': 25000.0,
    'high_bid': 80000.0
}

res1 = classify_keyword(test_row)
res2 = qualify_keyword(test_row)

print("test_classification result:")
print(res1)
print("\nbuild_v4_master_excel result:")
print(res2)
