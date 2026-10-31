import sys
import json
import requests
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = "https://www.visagbluesea.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

# Fetch sitemap.xml
r = requests.get(f"{BASE_URL}/sitemap.xml", headers=HEADERS, timeout=10)
root = ET.fromstring(r.text)
namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

sub_sitemaps = [loc.text for loc in root.findall('ns:sitemap/ns:loc', namespaces)]
print(f"Tổng số sub-sitemaps: {len(sub_sitemaps)}")
all_urls = []
for sm in sub_sitemaps:
    print(f"Fetching sub-sitemap: {sm}")
    try:
        r_sm = requests.get(sm, headers=HEADERS, timeout=10)
        sm_root = ET.fromstring(r_sm.text)
        urls = [loc.text for loc in sm_root.findall('ns:url/ns:loc', namespaces)]
        print(f"  -> {len(urls)} URLs")
        all_urls.extend(urls)
    except Exception as e:
        print(f"  -> Lỗi: {e}")

print(f"\nTổng số URLs từ sitemap: {len(all_urls)}")
with open('_Luu_Tru_Ky_Thuat/03_Du_Lieu_Tam_Va_Test/all_sitemap_urls.json', 'w', encoding='utf-8') as f:
    json.dump(all_urls, f, ensure_ascii=False, indent=2)

for u in all_urls[:30]:
    print(f" - {u}")
