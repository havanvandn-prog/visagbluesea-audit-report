import sys
import os
import re
import pandas as pd
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

from test_classification import df_classified

active_df = df_classified[df_classified['lop_trien_khai'].isin(['CỐT LÕI', 'CHẠY THỬ'])].copy()

# Detailed semantic sub intent
def get_sub_intent(row):
    kw = row['kw_norm']
    theme = row.get('theme', 'Chung')
    
    # 1. EB5
    if theme == 'EB5':
        if re.search(r'\b(dự án|du an|trung tâm vùng|trung tam vung)\b', kw):
            return 'EB5_DuAn'
        elif re.search(r'\b(chi phí|chi phi|bao nhiêu tiền|bao nhieu tien|giá|gia)\b', kw):
            return 'EB5_ChiPhi'
        elif re.search(r'\b(visa|thị thực|thi thuc)\b', kw):
            return 'EB5_Visa'
        elif re.search(r'\b(tư vấn|tu van|dịch vụ|dich vu|luật sư|luat su)\b', kw):
            return 'EB5_TuVan'
        elif re.search(r'\b(điều kiện|dieu kien|thủ tục|thu tuc|hồ sơ|ho so)\b', kw):
            return 'EB5_DieuKien'
        else:
            return 'EB5_DauTu_DinhCu'

    # 2. Golden Visa Europe
    if theme == 'GoldenVisa':
        if 'hy lạp' in kw or 'greece' in kw:
            if re.search(r'\b(mua nhà|bất động sản|bds)\b', kw):
                return 'GoldenVisa_HyLap_BDS'
            else:
                return 'GoldenVisa_HyLap'
        elif 'síp' in kw or 'cyprus' in kw:
            return 'GoldenVisa_Sip'
        elif 'malta' in kw:
            return 'GoldenVisa_Malta'
        elif 'bồ đào nha' in kw or 'portugal' in kw:
            return 'GoldenVisa_BoDaoNha'
        elif 'nauru' in kw:
            return 'QuocTich_Nauru'
        else:
            return 'GoldenVisa_ChauAu'

    # 3. Du học Phần Lan
    if theme == 'DuHocPhanLan':
        if re.search(r'\b(học bổng|hoc bong)\b', kw):
            return 'PhanLan_HocBong'
        elif re.search(r'\b(thpt|cấp 3|cap 3|phổ thông|pho thong)\b', kw):
            return 'PhanLan_THPT'
        elif re.search(r'\b(thạc sĩ|thac si|sau đại học|master)\b', kw):
            return 'PhanLan_ThacSi'
        elif re.search(r'\b(nghề|nghe|học nghề|hoc nghe)\b', kw):
            return 'PhanLan_HocNghe'
        elif re.search(r'\b(chi phí|chi phi|học phí|hoc phi)\b', kw):
            return 'PhanLan_ChiPhi'
        elif re.search(r'\b(tư vấn|tu van|công ty|cong ty|trung tâm|trung tam)\b', kw):
            return 'PhanLan_TuVan'
        elif re.search(r'\b(điều kiện|dieu kien|ielts|yêu cầu|yeu cau|thủ tục|thu tuc)\b', kw):
            return 'PhanLan_DieuKien'
        elif re.search(r'\b(định cư|dinh cu|doanh nhân|doanh nhan)\b', kw):
            return 'PhanLan_DinhCu'
        else:
            return 'PhanLan_DuHoc'

    # 4. Định cư tổng hợp
    if theme == 'DinhCuTongHop':
        if re.search(r'\b(tphcm|hồ chí minh|sài gòn)\b', kw):
            return 'DinhCu_TPHCM'
        elif re.search(r'\b(chi phí|chi phi|giá|bao nhiêu tiền)\b', kw):
            return 'DinhCu_ChiPhi'
        elif re.search(r'\b(mỹ|my)\b', kw):
            return 'DinhCu_My'
        elif re.search(r'\b(úc|uc)\b', kw):
            return 'DinhCu_Uc'
        elif re.search(r'\b(canada)\b', kw):
            return 'DinhCu_Canada'
        else:
            return 'DinhCu_CongTy'

    # 5. Dịch vụ Visa
    if theme == 'DichVuVisa':
        target_country = 'Chung'
        if 'mỹ' in kw or 'my' in kw:
            target_country = 'My'
        elif 'úc' in kw or 'uc' in kw:
            target_country = 'Uc'
        elif 'canada' in kw:
            target_country = 'Canada'
        elif 'schengen' in kw or 'pháp' in kw or 'châu âu' in kw or 'chau au' in kw:
            target_country = 'Schengen'
        
        if re.search(r'\b(dịch vụ|dich vu|làm visa|lam visa|bao đậu|uy tín|tphcm)\b', kw):
            return f'Visa_{target_country}_DichVu'
        elif re.search(r'\b(thủ tục|thu tuc|hồ sơ|ho so|xin visa|giấy tờ|giay to)\b', kw):
            return f'Visa_{target_country}_ThuTuc'
        elif re.search(r'\b(du lịch|du lich)\b', kw):
            return f'Visa_{target_country}_DuLich'
        elif re.search(r'\b(thăm thân|tham than)\b', kw):
            return f'Visa_{target_country}_ThamThan'
        else:
            return f'Visa_{target_country}_ChiPhi'

    # 6. Du học các nước (Úc, Mỹ, Canada, Đức, Nghề...)
    if 'DuHoc' in theme:
        prefix = theme.replace('DuHoc_', '')
        if re.search(r'\b(học bổng|hoc bong)\b', kw):
            return f'{prefix}_HocBong'
        elif re.search(r'\b(chi phí|chi phi|học phí|hoc phi|giá)\b', kw):
            return f'{prefix}_ChiPhi'
        elif re.search(r'\b(tư vấn|tu van|công ty|cong ty|trung tâm|trung tam)\b', kw):
            return f'{prefix}_TuVan'
        elif re.search(r'\b(điều kiện|dieu kien|thủ tục|thu tuc|hồ sơ|ho so|ielts)\b', kw):
            return f'{prefix}_DieuKien'
        elif re.search(r'\b(thpt|cấp 3|thạc sĩ|master|nghề)\b', kw):
            return f'{prefix}_BacHoc'
        else:
            return f'{prefix}_DuHoc'

    return f'{theme}_Chung'

active_df['sub_intent'] = active_df.apply(get_sub_intent, axis=1)

# Perfect partition algorithm: splits N elements into k buckets such that every bucket size is in [4, 10]
def partition_into_stag_buckets(df_subset, base_name):
    n = len(df_subset)
    if n == 0:
        return []
    
    sorted_df = df_subset.sort_values(by=['volume', 'low_bid'], ascending=[False, False]).copy()
    
    if n <= 10:
        sorted_df['nhom_quang_cao'] = base_name
        return [sorted_df]
    
    # We want each bucket to have size between 4 and 10, ideally 6 to 8
    # Try k from ceil(n/10) to floor(n/4)
    k_min = int(np.ceil(n / 10.0))
    k_max = int(np.floor(n / 4.0))
    
    # Pick target bucket size around 7
    best_k = k_min
    best_diff = 999
    for k in range(k_min, k_max + 1):
        avg_size = n / k
        diff = abs(avg_size - 7.0)
        if diff < best_diff:
            best_diff = diff
            best_k = k
            
    # Split into best_k buckets evenly
    # Sizes of buckets will be either q or q+1
    q, r = divmod(n, best_k)
    sizes = [q + 1 if i < r else q for i in range(best_k)]
    
    results = []
    start = 0
    for idx, sz in enumerate(sizes):
        sub_chunk = sorted_df.iloc[start : start + sz].copy()
        sub_chunk['nhom_quang_cao'] = f"{base_name}_{idx+1:02d}"
        results.append(sub_chunk)
        start += sz
        
    return results

# Two-pass clustering:
# Pass 1: Cluster groups that have >= 4 keywords
# Accumulate underflow keywords (< 4) by campaign and lop_trien_khai
pass1_results = []
underflows_by_camp_lop = {}

for (camp, lop, sub_intent), sub_df in active_df.groupby(['chien_dich', 'lop_trien_khai', 'sub_intent']):
    base_name = f"STAG_{sub_intent}"
    if len(sub_df) >= 4:
        buckets = partition_into_stag_buckets(sub_df, base_name)
        pass1_results.extend(buckets)
    else:
        key = (camp, lop)
        if key not in underflows_by_camp_lop:
            underflows_by_camp_lop[key] = []
        underflows_by_camp_lop[key].append(sub_df)

# Pass 2: Handle underflows per (campaign, lop)
pass2_results = []
leftover_underflows = []

for (camp, lop), list_dfs in underflows_by_camp_lop.items():
    combined_camp_lop = pd.concat(list_dfs)
    camp_clean = camp.replace('GGSearch_', '')
    base_name = f"STAG_{camp_clean}_TongHop_{lop[:3]}"
    if len(combined_camp_lop) >= 4:
        buckets = partition_into_stag_buckets(combined_camp_lop, base_name)
        pass2_results.extend(buckets)
    else:
        leftover_underflows.append(combined_camp_lop)

# Pass 3: If there are still tiny leftovers (<4 across campaign), merge them with existing groups in the same campaign!
all_so_far = pass1_results + pass2_results

if leftover_underflows:
    tiny_leftover_df = pd.concat(leftover_underflows)
    print(f"Tiny leftovers needing merge with existing groups: {len(tiny_leftover_df)}")
    
    # We can append these leftovers to the smallest existing group in the same campaign (as long as size <= 10)
    for idx, row in tiny_leftover_df.iterrows():
        kw_camp = row['chien_dich']
        kw_lop = row['lop_trien_khai']
        
        # Find best existing bucket
        best_bucket_idx = -1
        min_size = 999
        for b_idx, b_df in enumerate(all_so_far):
            if b_df.iloc[0]['chien_dich'] == kw_camp and b_df.iloc[0]['lop_trien_khai'] == kw_lop:
                if len(b_df) < 10 and len(b_df) < min_size:
                    min_size = len(b_df)
                    best_bucket_idx = b_idx
        
        if best_bucket_idx != -1:
            row_df = pd.DataFrame([row])
            row_df['nhom_quang_cao'] = all_so_far[best_bucket_idx].iloc[0]['nhom_quang_cao']
            all_so_far[best_bucket_idx] = pd.concat([all_so_far[best_bucket_idx], row_df])
        else:
            # Fallback to any group in same lop
            for b_idx, b_df in enumerate(all_so_far):
                if b_df.iloc[0]['lop_trien_khai'] == kw_lop and len(b_df) < 10:
                    row_df = pd.DataFrame([row])
                    row_df['nhom_quang_cao'] = b_df.iloc[0]['nhom_quang_cao']
                    all_so_far[b_idx] = pd.concat([b_df, row_df])
                    break

final_df = pd.concat(all_so_far)
print(f"\nFinal active keywords grouped: {len(final_df)}")

group_sizes = final_df.groupby('nhom_quang_cao').size()
print(f"Total STAG groups: {len(group_sizes)}")
print(f"Min group size: {group_sizes.min()}")
print(f"Max group size: {group_sizes.max()}")
print(f"Mean group size: {group_sizes.mean():.1f}")
print(f"Groups with size < 4: {(group_sizes < 4).sum()}")
print(f"Groups with size > 10: {(group_sizes > 10).sum()}")
print(f"Groups with size > 12: {(group_sizes > 12).sum()}")
