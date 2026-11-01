with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/kiem_dinh_keyword_07_1.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect enforce_size_4_to_10 definition
old_fn = """# Re-check group sizes: ensure all in [4, 10]
def enforce_size_4_to_10(df_in):
    final_dfs = []
    for g_name, g_df in df_in.groupby('B. NHÓM QUẢNG CÁO'):
        n = len(g_df)
        if n <= 10:
            final_dfs.append(g_df)
        else:
            k = int(np.ceil(n / 8.0))
            q, r = divmod(n, k)
            sizes = [q + 1 if i < r else q for i in range(k)]
            start = 0
            for i, sz in enumerate(sizes):
                sub = g_df.iloc[start : start + sz].copy()
                sub['B. NHÓM QUẢNG CÁO'] = f"{g_name}_{i+1:02d}"
                final_dfs.append(sub)
                start += sz
    return pd.concat(final_dfs).reset_index(drop=True)

df_active = enforce_size_4_to_10(df_active)"""

new_fn = """# Re-check group sizes: strictly enforce all in [4, 10] without any group < 4
def enforce_size_4_to_10(df_in):
    # Pass 1: split groups > 10
    buckets = []
    underflow_rows = []
    
    for g_name, g_df in df_in.groupby('B. NHÓM QUẢNG CÁO'):
        n = len(g_df)
        if n < 4:
            underflow_rows.append(g_df)
        elif n <= 10:
            buckets.append(g_df)
        else:
            k = int(np.ceil(n / 8.0))
            q, r = divmod(n, k)
            sizes = [q + 1 if i < r else q for i in range(k)]
            start = 0
            for i, sz in enumerate(sizes):
                sub = g_df.iloc[start : start + sz].copy()
                sub['B. NHÓM QUẢNG CÁO'] = f"{g_name}_{i+1:02d}"
                buckets.append(sub)
                start += sz
                
    # Pass 2: Merge underflows into sibling buckets in same campaign where len < 10
    if underflow_rows:
        underflow_df = pd.concat(underflow_rows).sort_values(by='G. LƯỢNG TÌM KIẾM', ascending=False)
        for idx, row in underflow_df.iterrows():
            kw_camp = row['A. CHIẾN DỊCH']
            
            # Find best sibling bucket: same camp, size < 10, smallest size
            best_idx = -1
            min_sz = 999
            for b_idx, b_df in enumerate(buckets):
                if b_df.iloc[0]['A. CHIẾN DỊCH'] == kw_camp:
                    if len(b_df) < 10 and len(b_df) < min_sz:
                        min_sz = len(b_df)
                        best_idx = b_idx
                        
            if best_idx == -1:
                # Find any bucket with size < 10
                for b_idx, b_df in enumerate(buckets):
                    if len(b_df) < 10 and len(b_df) < min_sz:
                        min_sz = len(b_df)
                        best_idx = b_idx
                        
            if best_idx != -1:
                row_df = pd.DataFrame([row])
                row_df['B. NHÓM QUẢNG CÁO'] = buckets[best_idx].iloc[0]['B. NHÓM QUẢNG CÁO']
                buckets[best_idx] = pd.concat([buckets[best_idx], row_df])
            else:
                # Append to smallest
                smallest_idx = min(range(len(buckets)), key=lambda i: len(buckets[i]))
                row_df = pd.DataFrame([row])
                row_df['B. NHÓM QUẢNG CÁO'] = buckets[smallest_idx].iloc[0]['B. NHÓM QUẢNG CÁO']
                buckets[smallest_idx] = pd.concat([buckets[smallest_idx], row_df])
                
    return pd.concat(buckets).reset_index(drop=True)

df_active = enforce_size_4_to_10(df_active)"""

assert old_fn in text, "old_fn not found"
text = text.replace(old_fn, new_fn)

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/kiem_dinh_keyword_07_1.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("kiem_dinh_keyword_07_1.py patched successfully!")
