import openpyxl
import sys
sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.load_workbook('Keyword Planner/04_Kiem_Dinh_Va_Tai_Cau_Truc_Keyword_visagbluesea.xlsx', data_only=True)
sheet = wb['01_Báo Cáo Kiểm Định & Đợt Bật']

# find table 2
rows = []
start = False
for r in range(1, 550):
    val = sheet.cell(row=r, column=1).value
    if val == 'STT':
        start = True
        continue
    if start:
        stt = sheet.cell(row=r, column=1).value
        if stt is None:
            break
        camp = sheet.cell(row=r, column=2).value
        group = sheet.cell(row=r, column=3).value
        status = sheet.cell(row=r, column=4).value
        wave = sheet.cell(row=r, column=5).value
        kw_cnt = sheet.cell(row=r, column=6).value
        vol = sheet.cell(row=r, column=7).value
        cpc = sheet.cell(row=r, column=8).value
        click = sheet.cell(row=r, column=9).value
        budget = sheet.cell(row=r, column=10).value
        rsa = sheet.cell(row=r, column=11).value
        url = sheet.cell(row=r, column=12).value
        rows.append({
            'stt': stt, 'camp': camp, 'group': group, 'status': status,
            'wave': wave, 'kw_cnt': kw_cnt, 'vol': vol, 'cpc': cpc,
            'click': click, 'budget': budget, 'rsa': rsa, 'url': url
        })

print(f"Total groups in Table 2: {len(rows)}")
enabled = [r for r in rows if r['status'] == 'ENABLED']
print(f"Enabled groups: {len(enabled)}")
for r in enabled:
    print(f"STT {r['stt']}: Camp={r['camp']} | Group={r['group']} | CPC={r['cpc']:,.0f} | Vol={r['vol']} | Budget={r['budget']:,.0f} | Click/d={r['click']:.2f}")

camps = set(r['camp'] for r in rows)
print(f"\nTotal Campaigns in Audited Table: {len(camps)}")
for c in sorted(camps):
    c_rows = [r for r in rows if r['camp'] == c]
    c_en = [r for r in c_rows if r['status'] == 'ENABLED']
    print(f"- {c}: {len(c_rows)} groups ({len(c_en)} enabled)")
