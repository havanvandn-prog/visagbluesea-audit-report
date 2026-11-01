import sys
from bs4 import BeautifulSoup

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open(r"_Luu_Tru_Ky_Thuat\03_Du_Lieu_Tam_Va_Test\real_google_ads_dom.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

print("=== HEADINGS ===")
for tag in soup.find_all(["h1", "h2", "h3", "span", "div"]):
    txt = tag.get_text(strip=True)
    if "Chiến dịch" in txt and len(txt) < 60:
        print(f"[{tag.name}] {txt}")

print("\n=== TABLES & DATA CONTAINERS ===")
for tag in soup.find_all(True):
    name = tag.name.lower()
    if "table" in name or "grid" in name or "chart" in name:
        print(f"<{tag.name} class='{' '.join(tag.get('class', []))}'>")

print("\n=== SVG ICONS ===")
svgs = soup.find_all("svg")
print(f"Found {len(svgs)} SVGs")
for s in svgs[:8]:
    viewbox = s.get("viewBox", "")
    classes = s.get("class", [])
    print(f"<svg viewBox='{viewbox}' class='{' '.join(classes)}'>")
