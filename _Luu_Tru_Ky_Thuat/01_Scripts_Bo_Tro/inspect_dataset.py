import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

# Read historical metrics CSV
csv_path = '_Luu_Tru_Ky_Thuat/Keyword_Planner_Raw/Historical_Metrics_HCM_Real.csv'
rows = []
with open(csv_path, 'r', encoding='utf-16') as f:
    for i, line in enumerate(f):
        if i < 2:
            continue
        parts = line.strip().split('\t')
        if i == 2:
            headers = parts
            continue
        if len(parts) >= 10:
            kw = parts[0].strip()
            if kw in ['Tất cả', 'Thành phố Hồ Chí Minh', '']:
                continue
            vol = float(parts[3]) if parts[3] else 0.0
            comp = parts[6] if len(parts) > 6 else ''
            low_bid = float(parts[8]) if len(parts) > 8 and parts[8] else 0.0
            high_bid = float(parts[9]) if len(parts) > 9 and parts[9] else 0.0
            rows.append({
                'keyword': kw,
                'volume': vol,
                'competition': comp,
                'low_bid': low_bid,
                'high_bid': high_bid
            })

df = pd.DataFrame(rows)
print(f"Loaded {len(df)} unique keywords with metrics.")
print(f"Total search volume in HCM: {df['volume'].sum():,.0f}")
print(f"Keywords with volume > 0: {(df['volume'] > 0).sum()}")
print(f"Keywords with bid data: {((df['low_bid'] > 0) | (df['high_bid'] > 0)).sum()}")

# Inspect some samples across themes
themes = ['eb5', 'định cư', 'golden visa', 'phần lan', 'du học úc', 'du học mỹ', 'visa úc', 'visa mỹ', 'lao động', 'việc làm', 'hà nội', 'miễn phí']
for t in themes:
    cnt = df['keyword'].str.contains(t, case=False, na=False).sum()
    vol_t = df[df['keyword'].str.contains(t, case=False, na=False)]['volume'].sum()
    print(f"Theme '{t}': {cnt} keywords, total volume = {vol_t:,.0f}")
