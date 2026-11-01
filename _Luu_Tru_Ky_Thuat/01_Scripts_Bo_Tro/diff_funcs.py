import sys
import difflib

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/test_classification.py', 'r', encoding='utf-8') as f:
    text1 = f.read()

with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/build_v4_master_excel.py', 'r', encoding='utf-8') as f:
    text2 = f.read()

start1 = text1.find("def classify_keyword(row):")
end1 = text1.find("# Run classification on dataframe")

start2 = text2.find("def qualify_keyword(row):")
end2 = text2.find("df_all = df_all.reset_index(drop=True)")

fn1 = text1[start1:end1].splitlines(keepends=True)
fn2 = text2[start2:end2].splitlines(keepends=True)

diff = list(difflib.unified_diff(fn1, fn2, fromfile='test_class', tofile='build_v4'))
print(f"Diff lines: {len(diff)}")
for line in diff[:30]:
    print(line, end='')
