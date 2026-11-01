import sys
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect the groups with size > 10 in build_v4_master_excel
with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/build_v4_master_excel.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find where final_active_df is assembled
# Right after: final_active_df = pd.concat(all_buckets).reset_index(drop=True)
# We can insert a post-processing rebalance loop:
fix_code = """
# Post-processing rebalance loop: strictly enforce size in [4, 10]
def rebalance_stag_groups(df_in):
    rebalanced_dfs = []
    for g_name, g_df in df_in.groupby('nhom_quang_cao'):
        n = len(g_df)
        if n <= 10:
            rebalanced_dfs.append(g_df)
        else:
            # Split into 2 or more buckets of size in [4, 10]
            k = int(np.ceil(n / 8.0))
            q, r = divmod(n, k)
            sizes = [q + 1 if i < r else q for i in range(k)]
            start = 0
            for i, sz in enumerate(sizes):
                sub_df = g_df.iloc[start : start + sz].copy()
                sub_df['nhom_quang_cao'] = f"{g_name}_{i+1:02d}"
                rebalanced_dfs.append(sub_df)
                start += sz
    return pd.concat(rebalanced_dfs).reset_index(drop=True)

final_active_df = rebalance_stag_groups(final_active_df)
"""

print("Inserting rebalance logic...")
target_pos = "final_active_df = pd.concat(all_buckets).reset_index(drop=True)"
if target_pos in text:
    new_text = text.replace(target_pos, target_pos + fix_code)
    with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/build_v4_master_excel.py', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("build_v4_master_excel.py patched with rebalance logic!")
else:
    print("Target position not found!")
