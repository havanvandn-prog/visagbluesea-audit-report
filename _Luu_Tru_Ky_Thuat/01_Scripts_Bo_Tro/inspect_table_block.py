import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Ma Trận Xử Lý')
start = text.rfind('<div class="mt-6 bg-white', 0, idx)
end = text.find('</table>', idx)
end = text.find('</div>', end)
end = text.find('</div>', end + 6) + 6

print("START:", start)
print("END:", end)
print("--- SNIPPET ---")
print(text[start:end])
