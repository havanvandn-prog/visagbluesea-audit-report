import sys
import pandas as pd
from test_classification import df_classified

sys.stdout.reconfigure(encoding='utf-8')

print("Loaded df_classified successfully!")
print("Shape:", df_classified.shape)
print("Columns:", df_classified.columns.tolist())
print("\nLớp triển khai counts:")
print(df_classified['lop_trien_khai'].value_counts())
print("\nSample Core row:")
print(df_classified[df_classified['lop_trien_khai'] == 'CỐT LÕI'].iloc[0])
