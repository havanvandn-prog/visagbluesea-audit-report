import sys
sys.stdout.reconfigure(encoding='utf-8')

for script in ['fix_sticky_header.py', 'update_numbers_correctly.py']:
    print(f"=== {script} ===")
    try:
        with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/' + script, 'r', encoding='utf-8') as f:
            print(f.read()[:1000])
    except Exception as e:
        print(f"Error: {e}")
