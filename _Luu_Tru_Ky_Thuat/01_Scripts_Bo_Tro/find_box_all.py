import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

for fpath in glob.glob('*.html') + glob.glob('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/*.py'):
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'Tài liệu đánh giá kỹ thuật trung lập' in content:
            print(f"Found in: {fpath}")
    except Exception:
        pass
