with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/build_v4_master_excel.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = "df_all['chien_dich'] = df_all['chien_dich'].fillna('GGSearch_Chung')"
replacement = """print("Columns in df_qual:", df_qual.columns.tolist())
if 'chien_dich' not in df_qual.columns:
    df_all['chien_dich'] = 'GGSearch_Chung'
else:
    df_all['chien_dich'] = df_all['chien_dich'].fillna('GGSearch_Chung')
if 'theme' not in df_qual.columns:
    df_all['theme'] = 'Chung'
else:
    df_all['theme'] = df_all['theme'].fillna('Chung')"""

assert target in text
text = text.replace(target, replacement)
with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/build_v4_master_excel.py', 'w', encoding='utf-8') as f:
    f.write(text)
