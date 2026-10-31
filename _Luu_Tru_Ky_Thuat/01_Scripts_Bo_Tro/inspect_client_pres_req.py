import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\SKILL.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect Section Client Presentation requirements
idx = text.find('Bản Trình Bày Khách Hàng')
if idx != -1:
    print(text[idx:idx+2000])
