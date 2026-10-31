import os
import sys
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = "https://www.visagbluesea.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

os.makedirs("_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro", exist_ok=True)
os.makedirs("_Luu_Tru_Ky_Thuat/02_Screenshots_Debug_Va_Khao_Sat", exist_ok=True)
os.makedirs("_Luu_Tru_Ky_Thuat/03_Du_Lieu_Tam_Va_Test", exist_ok=True)
os.makedirs("Bang_Chung_Hinh_Anh", exist_ok=True)

print("--- 1. KIỂM TRA ROBOTS.TXT & SITEMAP ---")
try:
    r_robots = requests.get(f"{BASE_URL}/robots.txt", headers=HEADERS, timeout=10)
    print(f"robots.txt status: {r_robots.status_code}")
    print("robots.txt content:")
    print(r_robots.text[:500])
except Exception as e:
    print(f"Lỗi robots.txt: {e}")

try:
    r_sitemap = requests.get(f"{BASE_URL}/sitemap_index.xml", headers=HEADERS, timeout=10)
    print(f"sitemap_index.xml status: {r_sitemap.status_code}")
    if r_sitemap.status_code != 200:
        r_sitemap = requests.get(f"{BASE_URL}/sitemap.xml", headers=HEADERS, timeout=10)
        print(f"sitemap.xml status: {r_sitemap.status_code}")
    print("Sitemap preview:")
    print(r_sitemap.text[:500])
except Exception as e:
    print(f"Lỗi sitemap: {e}")

print("\n--- 2. PHÂN TÍCH TRANG CHỦ ---")
r_home = requests.get(BASE_URL, headers=HEADERS, timeout=15)
soup = BeautifulSoup(r_home.text, 'html.parser')

title = soup.find('title')
meta_desc = soup.find('meta', attrs={'name': 'description'})
h1s = soup.find_all('h1')
h2s = soup.find_all('h2')
canonical = soup.find('link', attrs={'rel': 'canonical'})

print(f"Title: {title.text if title else 'KHÔNG CÓ'}")
print(f"Meta Description: {meta_desc.get('content') if meta_desc else 'KHÔNG CÓ'}")
print(f"Canonical: {canonical.get('href') if canonical else 'KHÔNG CÓ'}")
print(f"Số lượng H1: {len(h1s)}")
for i, h in enumerate(h1s, 1):
    print(f"  H1 #{i}: {h.text.strip()}")
print(f"Số lượng H2: {len(h2s)}")
for i, h in enumerate(h2s[:10], 1):
    print(f"  H2 #{i}: {h.text.strip()}")

# Forms & Inputs
forms = soup.find_all('form')
print(f"\nSố lượng Form: {len(forms)}")
for i, f in enumerate(forms, 1):
    action = f.get('action', '')
    method = f.get('method', '')
    inputs = f.find_all(['input', 'select', 'textarea'])
    names = [inp.get('name') or inp.get('placeholder') or inp.get('type') for inp in inputs]
    print(f"  Form #{i}: action={action}, method={method}, inputs={names}")

# Tel links & Zalo
tel_links = soup.find_all('a', href=lambda href: href and 'tel:' in href)
print(f"\nSố lượng liên kết tel:: {len(tel_links)}")
for a in tel_links:
    print(f"  Tel: {a.get('href')} | Text: {a.text.strip()}")

zalo_links = soup.find_all('a', href=lambda href: href and 'zalo' in href.lower())
print(f"\nSố lượng liên kết Zalo: {len(zalo_links)}")
for a in zalo_links:
    print(f"  Zalo: {a.get('href')} | Text: {a.text.strip()}")

# Tracking Scripts
scripts = soup.find_all('script')
tracking_found = []
for s in scripts:
    src = s.get('src', '')
    content = s.text
    if 'gtm.js' in src or 'googletagmanager.com' in src or 'GTM-' in content:
        tracking_found.append(('GTM', src[:100] or content[:100]))
    if 'gtag' in content or 'UA-' in content or 'G-' in content or 'google-analytics.com' in src:
        tracking_found.append(('GA4 / gtag', src[:100] or content[:100]))
    if 'fbevents.js' in src or 'fbq(' in content:
        tracking_found.append(('Facebook Pixel', src[:100] or content[:100]))
    if 'clarity.ms' in src or 'clarity' in content:
        tracking_found.append(('Microsoft Clarity', src[:100] or content[:100]))
    if 'hotjar' in src or 'hotjar' in content:
        tracking_found.append(('Hotjar', src[:100] or content[:100]))

print(f"\nTracking Scripts tìm thấy: {len(tracking_found)}")
for t, detail in tracking_found:
    print(f"  {t}: {detail.strip().replace(chr(10), ' ')}")

# Schema JSON-LD
schemas = soup.find_all('script', type='application/ld+json')
print(f"\nSố lượng Schema JSON-LD: {len(schemas)}")
for i, s in enumerate(schemas, 1):
    try:
        data = json.loads(s.text)
        print(f"  Schema #{i}: @type = {data.get('@type') or [x.get('@type') for x in data.get('@graph', [])] if isinstance(data, dict) else 'List'}")
    except Exception as e:
        print(f"  Schema #{i} parse error: {e}")

# Internal Links
links = soup.find_all('a', href=True)
internal_links = set()
for a in links:
    href = a['href']
    full_url = urljoin(BASE_URL, href)
    parsed = urlparse(full_url)
    if parsed.netloc == urlparse(BASE_URL).netloc:
        clean_url = full_url.split('#')[0].rstrip('/')
        if clean_url:
            internal_links.add(clean_url)

print(f"\nTổng số internal URLs tìm thấy trên trang chủ: {len(internal_links)}")
with open('_Luu_Tru_Ky_Thuat/03_Du_Lieu_Tam_Va_Test/internal_links.json', 'w', encoding='utf-8') as f:
    json.dump(list(internal_links), f, ensure_ascii=False, indent=2)

print("Đã lưu danh sách links vào internal_links.json")
