import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\ADMIN\.gemini\config\skills\kiem-tra-web-ggads-va-seo (Chatgpt)\SKILL.md', 'r', encoding='utf-8') as f:
    text = f.read()

# search for Client Presentation or Header or CTA
for m in re.finditer(r'(?:header|cta|client presentation|bản trình bày)', text, re.IGNORECASE):
    start = max(0, m.start() - 100)
    end = min(len(text), m.end() + 200)
    print("Match at", m.start())
    print(text[start:end])
    print("-" * 50)
