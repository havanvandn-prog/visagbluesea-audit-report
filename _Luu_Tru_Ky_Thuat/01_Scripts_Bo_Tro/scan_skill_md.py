import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
skill_path = r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\SKILL.md'
with open(skill_path, 'r', encoding='utf-8') as f:
    text = f.read()

keywords = [
    'Mini Rail',
    'Mini Icon Rail',
    'GTM Snippet',
    'GTM Tag',
    'Ma Trận Xử Lý URL',
    'URL Mapping Matrix',
    'Khuyến Nghị Vận Hành Chiến Dịch Google Search Ads',
    'Lưu Ý Google Ads',
    'viên nhộng',
    'w-2.5 h-6',
    'Bao_Cao_Trinh_Bay_Khach_Hang',
    'Cổng 4'
]

for kw in keywords:
    matches = list(re.finditer(re.escape(kw), text, re.IGNORECASE))
    print(f'Keyword "{kw}": {len(matches)} occurrences')
    for m in matches[:3]:
        idx = m.start()
        snippet = text[max(0, idx-40):min(len(text), idx+100)].replace('\n', ' ')
        print(f'   - At {idx}: {snippet}')
