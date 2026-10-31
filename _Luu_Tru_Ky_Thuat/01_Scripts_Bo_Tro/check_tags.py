import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

FILES_TO_CHECK = [
    "Bao_Cao_Trinh_Bay_Khach_Hang_visagbluesea.com.html",
    "index.html",
    "Bao_Cao_Ky_Thuat_Noi_Bo_visagbluesea.com.html"
]

all_passed = True

for filepath in FILES_TO_CHECK:
    print(f"\nChecking tags for: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Simple tag balance check for key structural tags
    tags = ['div', 'section', 'main', 'header', 'aside', 'table', 'tbody', 'thead', 'tr', 'td', 'th', 'ul', 'li', 'p', 'h1', 'h2', 'h3', 'h4', 'span', 'a', 'button']
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Check with html.parser
    errors = 0
    for tag in tags:
        # count occurrences of <tag and </tag in text (ignoring self-closing)
        open_count = html.lower().count(f"<{tag} ") + html.lower().count(f"<{tag}>")
        close_count = html.lower().count(f"</{tag}>")
        if open_count != close_count:
            print(f"  [MISMATCH] <{tag}>: opened {open_count} times, closed {close_count} times (diff = {open_count - close_count})")
            errors += 1
            all_passed = False
    
    if errors == 0:
        print(f"  -> Total errors: 0, Unclosed tags: 0. PERFECT BALANCE!")
    else:
        print(f"  -> Total errors: {errors}")

if all_passed:
    print("\n[GATE 3 PASSED] All HTML reports passed tag balance verification!")
else:
    print("\n[GATE 3 FAILED] Please fix mismatched tags.")
