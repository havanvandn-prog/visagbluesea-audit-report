import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('Keyword Planner/kw-summary-v4-audited.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== METADATA ===")
for k in ['schema_version', 'auditor_skill', 'forecast_contract', 'account_mode', 'business_name', 'target_website', 'currency', 'period', 'days_in_period', 'geo', 'network']:
    print(f"{k}: {data.get(k)}")

print("\n=== AUDIT SUMMARY ===")
print(json.dumps(data.get('audit_summary'), ensure_ascii=False, indent=2))

units = data.get('forecast_units', [])
print(f"\nTotal forecast units: {len(units)}")

enabled_units = [u for u in units if u.get('launch_status') == 'ENABLED' or u.get('enabled') is True]
print(f"Enabled units: {len(enabled_units)}")

print("\n=== ENABLED UNITS ===")
for u in enabled_units:
    print(f"- Campaign: {u.get('campaign')} | AdGroup: {u.get('adgroup')} | KW count: {len(u.get('keywords', []))} | CPC: {u.get('expected_cpc')} | Budget: {u.get('allocated_budget')} | Clicks: {u.get('forecast_clicks')} | Leads: {u.get('forecast_leads')}")

print("\n=== ALL CAMPAIGNS ===")
campaigns = set(u.get('campaign') for u in units)
for c in sorted(campaigns):
    c_units = [u for u in units if u.get('campaign') == c]
    c_enabled = [u for u in c_units if u.get('launch_status') == 'ENABLED' or u.get('enabled') is True]
    print(f"Campaign: {c} | Total AdGroups: {len(c_units)} | Enabled: {len(c_enabled)}")
