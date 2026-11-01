with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/build_v4_master_excel.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the flawed assignment with clean concat
old_snippet = """qualified_rows = [qualify_keyword(row) for idx, row in df_all.iterrows()]
for idx, q in enumerate(qualified_rows):
    for k, v in q.items():
        df_all.at[idx, k] = v

active_df = df_all[df_all['lop_trien_khai'].isin(['CỐT LÕI', 'CHẠY THỬ'])].copy()
drop_df = df_all[df_all['lop_trien_khai'] == 'KHÔNG CHẠY'].copy()"""

new_snippet = """df_all = df_all.reset_index(drop=True)
qualified_rows = [qualify_keyword(row) for idx, row in df_all.iterrows()]
df_qual = pd.DataFrame(qualified_rows)
df_all = pd.concat([df_all, df_qual], axis=1)
df_all['chien_dich'] = df_all['chien_dich'].fillna('GGSearch_Chung')
df_all['theme'] = df_all['theme'].fillna('Chung')

active_df = df_all[df_all['lop_trien_khai'].isin(['CỐT LÕI', 'CHẠY THỬ'])].copy().reset_index(drop=True)
drop_df = df_all[df_all['lop_trien_khai'] == 'KHÔNG CHẠY'].copy().reset_index(drop=True)"""

assert old_snippet in content, "old_snippet not found in build_v4_master_excel.py"
content = content.replace(old_snippet, new_snippet)

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/build_v4_master_excel.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated build_v4_master_excel.py successfully!")
