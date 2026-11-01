import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('_Luu_Tru_Ky_Thuat/Keyword_Planner_Raw/Historical_Metrics_HCM_Real.csv', 'r', encoding='utf-16') as f:
    for i in range(15):
        line = f.readline()
        if i == 2:
            cols = line.strip().split('\t')
            print(f"Header columns ({len(cols)}):")
            for idx, c in enumerate(cols):
                print(f"  {idx}: {c}")
        elif i > 4 and i < 10:
            parts = line.strip().split('\t')
            print(f"Row {i}: KW='{parts[0]}', Searches='{parts[3] if len(parts)>3 else ''}', Comp='{parts[6] if len(parts)>6 else ''}', Low='{parts[8] if len(parts)>8 else ''}', High='{parts[9] if len(parts)>9 else ''}'")
