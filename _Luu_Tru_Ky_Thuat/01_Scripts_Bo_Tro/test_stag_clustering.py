import sys
import os
import re
import pandas as pd
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

from test_classification import df_classified

def get_sub_intent(row):
    kw = row['kw_norm']
    theme = row.get('theme', 'Chung')
    pheu = row['pheu']
    lop = row['lop_trien_khai']
    
    # 1. EB5
    if theme == 'EB5':
        if re.search(r'\b(dự án|du an|trung tâm vùng|trung tam vung)\b', kw):
            return 'EB5_DuAn_TrungTamVung'
        elif re.search(r'\b(chi phí|chi phi|bao nhiêu tiền|bao nhieu tien|giá|gia)\b', kw):
            return 'EB5_ChiPhi_Gia'
        elif re.search(r'\b(visa|thị thực|thi thuc)\b', kw):
            return 'EB5_Visa_DauTu'
        elif re.search(r'\b(tư vấn|tu van|dịch vụ|dich vu|luật sư|luat su)\b', kw):
            return 'EB5_TuVan_DichVu'
        elif re.search(r'\b(điều kiện|dieu kien|thủ tục|thu tuc|hồ sơ|ho so)\b', kw):
            return 'EB5_DieuKien_ThuTuc'
        else:
            return 'EB5_DauTu_DinhCu'

    # 2. Golden Visa Europe
    if theme == 'GoldenVisa':
        if 'hy lạp' in kw or 'greece' in kw:
            if re.search(r'\b(mua nhà|bất động sản|bds)\b', kw):
                return 'GoldenVisa_HyLap_BDS'
            else:
                return 'GoldenVisa_HyLap_Chung'
        elif 'síp' in kw or 'cyprus' in kw:
            return 'GoldenVisa_Sip_Cyprus'
        elif 'malta' in kw:
            return 'GoldenVisa_Malta_MPRP'
        elif 'bồ đào nha' in kw or 'portugal' in kw:
            return 'GoldenVisa_BoDaoNha'
        elif 'nauru' in kw:
            return 'QuocTich_Nauru'
        else:
            return 'GoldenVisa_ChauAu_Chung'

    # 3. Du học Phần Lan
    if theme == 'DuHocPhanLan':
        if re.search(r'\b(học bổng|hoc bong)\b', kw):
            return 'PhanLan_HocBong'
        elif re.search(r'\b(thpt|cấp 3|cap 3|phổ thông|pho thong)\b', kw):
            return 'PhanLan_THPT_Cap3'
        elif re.search(r'\b(thạc sĩ|thac si|sau đại học|master)\b', kw):
            return 'PhanLan_ThacSi'
        elif re.search(r'\b(nghề|nghe|học nghề|hoc nghe)\b', kw):
            return 'PhanLan_HocNghe'
        elif re.search(r'\b(chi phí|chi phi|học phí|hoc phi)\b', kw):
            return 'PhanLan_ChiPhi_HocPhi'
        elif re.search(r'\b(tư vấn|tu van|công ty|cong ty|trung tâm|trung tam)\b', kw):
            return 'PhanLan_TuVan_DichVu'
        elif re.search(r'\b(điều kiện|dieu kien|ielts|yêu cầu|yeu cau|thủ tục|thu tuc)\b', kw):
            return 'PhanLan_DieuKien_ThuTuc'
        elif re.search(r'\b(định cư|dinh cu|doanh nhân|doanh nhan)\b', kw):
            return 'PhanLan_DinhCu_DoanhNhan'
        else:
            return 'PhanLan_DuHoc_Chung'

    # 4. Định cư tổng hợp
    if theme == 'DinhCuTongHop':
        if re.search(r'\b(tphcm|hồ chí minh|sài gòn)\b', kw):
            return 'DinhCu_TPHCM'
        elif re.search(r'\b(chi phí|chi phi|giá|bao nhiêu tiền)\b', kw):
            return 'DinhCu_ChiPhi'
        elif re.search(r'\b(mỹ|my)\b', kw):
            return 'DinhCu_My_Chung'
        elif re.search(r'\b(úc|uc)\b', kw):
            return 'DinhCu_Uc_Chung'
        elif re.search(r'\b(canada)\b', kw):
            return 'DinhCu_Canada_Chung'
        else:
            return 'DinhCu_CongTy_TuVan'

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
            return f'Visa_{target_country}_DichVu_TronGoi'
        elif re.search(r'\b(thủ tục|thu tuc|hồ sơ|ho so|xin visa|giấy tờ|giay to)\b', kw):
            return f'Visa_{target_country}_ThuTuc_HoSo'
        elif re.search(r'\b(du lịch|du lich)\b', kw):
            return f'Visa_{target_country}_DuLich'
        elif re.search(r'\b(thăm thân|tham than)\b', kw):
            return f'Visa_{target_country}_ThamThan'
        else:
            return f'Visa_{target_country}_ChiPhi_Gia'

    # 6. Du học các nước (Úc, Mỹ, Canada, Đức, Nghề...)
    if 'DuHoc' in theme:
        prefix = theme.replace('DuHoc_', '')
        if re.search(r'\b(học bổng|hoc bong)\b', kw):
            return f'{prefix}_HocBong'
        elif re.search(r'\b(chi phí|chi phi|học phí|hoc phi|giá)\b', kw):
            return f'{prefix}_ChiPhi_HocPhi'
        elif re.search(r'\b(tư vấn|tu van|công ty|cong ty|trung tâm|trung tam)\b', kw):
            return f'{prefix}_TuVan_DichVu'
        elif re.search(r'\b(điều kiện|dieu kien|thủ tục|thu tuc|hồ sơ|ho so|ielts)\b', kw):
            return f'{prefix}_DieuKien_ThuTuc'
        elif re.search(r'\b(thpt|cấp 3|thạc sĩ|master|nghề)\b', kw):
            return f'{prefix}_BacHoc_ChuyenSau'
        else:
            return f'{prefix}_DuHoc_Chung'

    return f'{theme}_Chung'

active_df = df_classified[df_classified['lop_trien_khai'].isin(['CỐT LÕI', 'CHẠY THỬ'])].copy()
active_df['sub_intent'] = active_df.apply(get_sub_intent, axis=1)

# Helper function to split a dataframe into chunks of size in [min_size, max_size]
def chunk_df_stag(df_sub, base_name, min_size=4, max_size=10):
    n = len(df_sub)
    if n == 0:
        return []
    
    sorted_df = df_sub.sort_values(by=['volume', 'low_bid'], ascending=[False, False]).copy()
    
    if n <= max_size:
        sorted_df['nhom_quang_cao'] = base_name
        return [sorted_df]
    
    # Calculate k chunks
    k = int(np.ceil(n / max_size))
    # Make sure n / k >= min_size if possible
    while k > 1 and (n / k) < min_size:
        k -= 1
        
    chunk_size = int(np.ceil(n / k))
    results = []
    for i in range(k):
        sub_chunk = sorted_df.iloc[i * chunk_size : (i + 1) * chunk_size].copy()
        if len(sub_chunk) > 0:
            sub_chunk['nhom_quang_cao'] = f"{base_name}_{i+1:02d}"
            results.append(sub_chunk)
    return results

# Grouping
all_stag_dfs = []
underflow_dict = {}

for (campaign, lop, sub_intent), sub_df in active_df.groupby(['chien_dich', 'lop_trien_khai', 'sub_intent']):
    base_name = f"STAG_{sub_intent}"
    if len(sub_df) < 4:
        key = (campaign, lop)
        if key not in underflow_dict:
            underflow_dict[key] = []
        underflow_dict[key].append(sub_df)
    else:
        chunks = chunk_df_stag(sub_df, base_name, min_size=4, max_size=10)
        all_stag_dfs.extend(chunks)

# Merge underflows
for (campaign, lop), dfs in underflow_dict.items():
    combined_under = pd.concat(dfs)
    camp_clean = campaign.replace('GGSearch_', '')
    base_name = f"STAG_{camp_clean}_TongHop_{lop[:3]}"
    chunks = chunk_df_stag(combined_under, base_name, min_size=4, max_size=10)
    all_stag_dfs.extend(chunks)

final_active_df = pd.concat(all_stag_dfs)
print(f"Total active keywords grouped: {len(final_active_df)}")

group_sizes = final_active_df.groupby('nhom_quang_cao').size()
print(f"Total STAG groups: {len(group_sizes)}")
print(f"Min group size: {group_sizes.min()}")
print(f"Max group size: {group_sizes.max()}")
print(f"Mean group size: {group_sizes.mean():.1f}")
print(f"Groups with size < 4: {(group_sizes < 4).sum()}")
print(f"Groups with size > 10: {(group_sizes > 10).sum()}")
print(f"Groups with size > 12: {(group_sizes > 12).sum()}")

if (group_sizes < 4).sum() > 0:
    print("\nUnderflow groups (<4):")
    print(group_sizes[group_sizes < 4])
