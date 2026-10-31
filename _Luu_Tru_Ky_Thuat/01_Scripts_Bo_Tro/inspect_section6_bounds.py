import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Khuyến Nghị Vận Hành Chiến Dịch Google Search Ads')
start = text.rfind('<section', 0, idx)
end = text.find('</section>', idx) + len('</section>')

print("START:", start)
print("END:", end)
print("--- START SNIPPET ---")
print(text[start:start+350])
print("--- END SNIPPET ---")
print(text[end-350:end])
