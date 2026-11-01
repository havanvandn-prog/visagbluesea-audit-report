import sys
import os
import re
import json
import pandas as pd
import numpy as np
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

sys.stdout.reconfigure(encoding='utf-8')

print("Starting Master V4 Keyword Analysis Engine...")

# 1. Load Data
csv_path = '_Luu_Tru_Ky_Thuat/Keyword_Planner_Raw/Historical_Metrics_HCM_Real.csv'
raw_rows = []
with open(csv_path, 'r', encoding='utf-16') as f:
    for i, line in enumerate(f):
        if i < 2:
            continue
        parts = line.strip().split('\t')
        if i == 2:
            continue
        if len(parts) >= 10:
            kw = parts[0].strip()
            if kw in ['Tất cả', 'Thành phố Hồ Chí Minh', '']:
                continue
            vol = float(parts[3]) if parts[3] else 0.0
            comp = parts[6] if len(parts) > 6 else 'Thấp'
            low_bid = float(parts[8]) if len(parts) > 8 and parts[8] else 0.0
            high_bid = float(parts[9]) if len(parts) > 9 and parts[9] else 0.0
            raw_rows.append({
                'keyword': kw,
                'volume': vol,
                'competition': comp,
                'low_bid': low_bid,
                'high_bid': high_bid
            })

df_all = pd.DataFrame(raw_rows).drop_duplicates(subset=['keyword'])
print(f"Loaded {len(df_all)} unique raw keywords.")

def normalize_kw(kw):
    return re.sub(r'\s+', ' ', kw.strip().lower())

df_all['kw_norm'] = df_all['keyword'].apply(normalize_kw)

# 2. Strict 100% Row-by-Row Independent Qualification
def qualify_keyword(row):
    kw = row['kw_norm']
    vol = row['volume']
    
    # 2.1 Geographic Disqualification (Outside HCM)
    out_geo = re.search(r'\b(hà nội|ha noi|đà nẵng|da nang|hải phòng|hai phong|cần thơ|can tho|nha trang|quảng ninh|huế|vinh|bắc ninh|nam định|hải dương|thái nguyên)\b', kw)
    if out_geo:
        geo = out_geo.group(0)
        return {
            'lop_trien_khai': 'KHÔNG CHẠY',
            'pheu': 'TOFU',
            'do_ro_y_dinh': 'KHÁ RÕ',
            'do_phu_hop_offer': 0,
            'nhu_cau_nguoi_tim': f"Tìm dịch vụ hoặc cơ hội tại {geo.title()}",
            'y_dinh_tim_kiem': 'Địa phương ngoài vùng phục vụ',
            'bang_chung_rieng': f"Chứa địa danh '{geo}' ngoài phạm vi chạy TP.HCM, loại bỏ để chống phân tán ngân sách địa phương.",
            'trang_dich': 'https://www.visagbluesea.com/',
            'loai_ly_do': 'Ngoài địa bàn phục vụ TP.HCM'
        }

    # 2.2 Jobs / Recruitment / Unskilled Labor / Domestic Workers
    jobs = re.search(r'\b(tuyển dụng|tuyen dung|tìm việc|tim viec|việc làm|viec lam|cần thợ|tuyển thợ|thợ nail|làm nail|tuyển công nhân|xklđ|xkld|xuất khẩu lao động|xuat khau lao dong|lương bao nhiêu|mẫu cv|tuyển sinh|xin việc|phỏng vấn xin việc)\b', kw)
    if jobs:
        j_term = jobs.group(0)
        return {
            'lop_trien_khai': 'KHÔNG CHẠY',
            'pheu': 'TOFU',
            'do_ro_y_dinh': 'KHÁ RÕ',
            'do_phu_hop_offer': 0,
            'nhu_cau_nguoi_tim': f"Tìm kiếm thông tin việc làm/tuyển dụng ({j_term})",
            'y_dinh_tim_kiem': 'Tìm việc làm / Tuyển dụng',
            'bang_chung_rieng': f"Chứa cụm từ tuyển dụng/việc làm '{j_term}', hoàn toàn sai lệch tệp khách hàng đầu tư định cư và du học.",
            'trang_dich': 'https://www.visagbluesea.com/',
            'loai_ly_do': 'Sai đối tượng - Tìm việc làm'
        }

    # 2.3 DIY / Free / Books / General English training
    diy = re.search(r'\b(tự làm|tu lam|tự xin|tu xin|tự túc|tu tuc|miễn phí|mien phi|free|tải|download|sách|tai lieu|tài liệu|đề thi|luyện thi|ngữ pháp|từ vựng|cách học tiếng anh|tieng anh du kich|mẫu đơn)\b', kw)
    if diy:
        d_term = diy.group(0)
        return {
            'lop_trien_khai': 'KHÔNG CHẠY',
            'pheu': 'TOFU',
            'do_ro_y_dinh': 'KHÁ RÕ',
            'do_phu_hop_offer': 0,
            'nhu_cau_nguoi_tim': f"Tự làm hoặc tìm kiếm tài liệu miễn phí ({d_term})",
            'y_dinh_tim_kiem': 'Tự túc / Không thương mại',
            'bang_chung_rieng': f"Ý định tự làm hoặc tìm tài liệu miễn phí '{d_term}', không phát sinh nhu cầu ủy thác dịch vụ.",
            'trang_dich': 'https://www.visagbluesea.com/',
            'loai_ly_do': 'Tự túc / Miễn phí / Không phát sinh chi tiêu'
        }

    # 2.4 Irrelevant / General Trivia / Non-visa Tourism
    irr = re.search(r'\b(phim|bài hát|thời tiết|múi giờ|dân số|bản đồ|thủ đô|lịch sử|chiến tranh|diện tích|quốc kỳ|món ăn|khách sạn|vé máy bay|tour du lịch|du lịch giá rẻ)\b', kw)
    if irr:
        i_term = irr.group(0)
        return {
            'lop_trien_khai': 'KHÔNG CHẠY',
            'pheu': 'TOFU',
            'do_ro_y_dinh': 'MƠ HỒ',
            'do_phu_hop_offer': 0,
            'nhu_cau_nguoi_tim': f"Tra cứu thông tin du lịch đại chúng/bách khoa ({i_term})",
            'y_dinh_tim_kiem': 'Tra cứu đại chúng',
            'bang_chung_rieng': f"Chủ đề tra cứu chung '{i_term}', không liên quan đến dịch vụ tư vấn di trú, visa hay trường học.",
            'trang_dich': 'https://www.visagbluesea.com/',
            'loai_ly_do': 'Lạc đề / Kiến thức đại chúng'
        }

    # Commercial Signals
    has_commercial = bool(re.search(r'\b(dịch vụ|dich vu|công ty|cong ty|trung tâm|trung tam|tư vấn|tu van|chi phí|chi phi|giá|gia|báo giá|bao gia|bao nhiêu tiền|ở đâu|o dau|uy tín|uy tin|trọn gói|tron goi|hồ sơ|ho so|đầu tư|dau tu|dự án|du an|visa|thủ tục|thu tuc|học bổng|hoc bong|thpt|thạc sĩ|thac si|nghề|nghe|định cư|dinh cu)\b', kw))
    has_bofu = bool(re.search(r'\b(dịch vụ|công ty|trung tâm|tư vấn|chi phí|báo giá|bao nhiêu tiền|ở đâu|uy tín|trọn gói|đầu tư eb5|visa eb5|golden visa|mua nhà|dự án eb5)\b', kw))

    # Offer 1: EB-5 Investment USA
    if re.search(r'\beb[- ]?5\b', kw) or (re.search(r'\bđịnh cư mỹ\b|\bdinh cu my\b', kw) and re.search(r'\bđầu tư\b|\bdau tu\b|\bdiện đầu tư\b', kw)):
        if has_bofu or re.search(r'\b(đầu tư|dự án|visa|tư vấn|chi phí|luật sư)\b', kw):
            return {
                'lop_trien_khai': 'CỐT LÕI',
                'pheu': 'BOFU',
                'do_ro_y_dinh': 'RẤT RÕ',
                'do_phu_hop_offer': 3,
                'nhu_cau_nguoi_tim': 'Tìm hiểu chương trình hoặc dịch vụ tư vấn đầu tư định cư Mỹ diện EB-5',
                'y_dinh_tim_kiem': 'Giao dịch / Đầu tư định cư EB-5 Mỹ',
                'bang_chung_rieng': "Khớp trực tiếp dịch vụ đầu tư định cư EB-5 Mỹ cốt lõi của GBlueSea, có trang đích chuyên sâu và dự án thực tế.",
                'trang_dich': 'https://www.visagbluesea.com/us-green-card-eb-5',
                'chien_dich': 'GGSearch_DinhCu_EB5_My',
                'theme': 'EB5'
            }
        else:
            return {
                'lop_trien_khai': 'CHẠY THỬ',
                'pheu': 'MOFU',
                'do_ro_y_dinh': 'KHÁ RÕ',
                'do_phu_hop_offer': 2,
                'nhu_cau_nguoi_tim': 'Nghiên cứu điều kiện, chính sách EB-5',
                'y_dinh_tim_kiem': 'Cân nhắc điều kiện EB-5 Mỹ',
                'bang_chung_rieng': "Tìm hiểu chính sách/điều kiện EB-5, phù hợp đưa vào nhóm chạy thử theo dõi tỷ lệ chuyển đổi form.",
                'trang_dich': 'https://www.visagbluesea.com/us-green-card-eb-5',
                'chien_dich': 'GGSearch_DinhCu_EB5_My',
                'theme': 'EB5'
            }

    # Offer 2: Golden Visa Europe
    gv = re.search(r'\b(golden visa|hy lạp|greece|síp|cyprus|malta|mprp|bồ đào nha|portugal|định cư châu âu|dinh cu chau au|quốc tịch thứ hai|nauru)\b', kw)
    if gv and re.search(r'\b(định cư|dinh cu|visa|đầu tư|dau tu|mua nhà|thường trú|quốc tịch)\b', kw):
        country = gv.group(0)
        lp = 'https://www.visagbluesea.com/eu-golden-visas'
        if 'hy lạp' in kw or 'greece' in kw:
            lp = 'https://www.visagbluesea.com/golden-visa-greece'
        elif 'síp' in kw or 'cyprus' in kw:
            lp = 'https://www.visagbluesea.com/golden-visa-cyprus'
        elif 'malta' in kw:
            lp = 'https://www.visagbluesea.com/malta-investment-visa'
        elif 'bồ đào nha' in kw or 'portugal' in kw:
            lp = 'https://www.visagbluesea.com/portugal-investment-visa'
        elif 'nauru' in kw:
            lp = 'https://www.visagbluesea.com/nauru-citizenship-by-investment'
            
        if has_bofu or re.search(r'\b(đầu tư|mua nhà|tư vấn|chi phí|dịch vụ|thủ tục)\b', kw):
            return {
                'lop_trien_khai': 'CỐT LÕI',
                'pheu': 'BOFU',
                'do_ro_y_dinh': 'RẤT RÕ',
                'do_phu_hop_offer': 3,
                'nhu_cau_nguoi_tim': f"Tìm chương trình/dịch vụ đầu tư định cư Golden Visa {country.title()}",
                'y_dinh_tim_kiem': f"Giao dịch / Đầu tư định cư {country.title()}",
                'bang_chung_rieng': f"Khớp dịch vụ bất động sản di trú và Golden Visa {country.title()} có trang đích riêng trên website GBlueSea.",
                'trang_dich': lp,
                'chien_dich': 'GGSearch_DinhCu_GoldenVisa_ChauAu',
                'theme': 'GoldenVisa'
            }
        else:
            return {
                'lop_trien_khai': 'CHẠY THỬ',
                'pheu': 'MOFU',
                'do_ro_y_dinh': 'KHÁ RÕ',
                'do_phu_hop_offer': 2,
                'nhu_cau_nguoi_tim': f"Tìm hiểu thông tin định cư {country.title()}",
                'y_dinh_tim_kiem': f"Cân nhắc định cư {country.title()}",
                'bang_chung_rieng': f"Tìm hiểu thông tin quy chế định cư {country.title()}, theo dõi 30-50 click để kiểm chứng chuyển đổi.",
                'trang_dich': lp,
                'chien_dich': 'GGSearch_DinhCu_GoldenVisa_ChauAu',
                'theme': 'GoldenVisa'
            }

    # Offer 3: Du học Phần Lan (Flagship Core of GBlueSea)
    if 'phần lan' in kw or 'phan lan' in kw:
        if re.search(r'\b(du học|du hoc|học bổng|hoc bong|thpt|thạc sĩ|thac si|định cư|doanh nhân)\b', kw):
            if re.search(r'\b(tư vấn|học bổng|chi phí|thpt|thạc sĩ|nghề|công ty|dịch vụ|ở đâu|điều kiện)\b', kw) or kw in ['du học phần lan', 'du hoc phan lan']:
                return {
                    'lop_trien_khai': 'CỐT LÕI',
                    'pheu': 'BOFU',
                    'do_ro_y_dinh': 'RẤT RÕ',
                    'do_phu_hop_offer': 3,
                    'nhu_cau_nguoi_tim': 'Tìm lộ trình, học bổng hoặc tư vấn du học Phần Lan',
                    'y_dinh_tim_kiem': 'Giao dịch / Đăng ký du học Phần Lan',
                    'bang_chung_rieng': "Khớp dịch vụ mũi nhọn độc quyền du học Phần Lan cả gia đình của GBlueSea với văn phòng tại Helsinki.",
                    'trang_dich': 'https://www.visagbluesea.com/study-in-finland',
                    'chien_dich': 'GGSearch_DuHoc_PhanLan_MuiNhon',
                    'theme': 'DuHocPhanLan'
                }
            else:
                return {
                    'lop_trien_khai': 'CHẠY THỬ',
                    'pheu': 'MOFU',
                    'do_ro_y_dinh': 'KHÁ RÕ',
                    'do_phu_hop_offer': 2,
                    'nhu_cau_nguoi_tim': 'Tìm hiểu thông tin du học hoặc cuộc sống Phần Lan',
                    'y_dinh_tim_kiem': 'Nghiên cứu du học Phần Lan',
                    'bang_chung_rieng': "Tìm hiểu cuộc sống và du học Phần Lan, cần đưa vào nhóm test để đánh giá chuyển đổi.",
                    'trang_dich': 'https://www.visagbluesea.com/study-in-finland',
                    'chien_dich': 'GGSearch_DuHoc_PhanLan_MuiNhon',
                    'theme': 'DuHocPhanLan'
                }

    # Offer 4: Dịch vụ Định cư chung / Tư vấn định cư TPHCM
    if re.search(r'\b(tư vấn định cư|tu van dinh cu|dịch vụ định cư|dich vu dinh cu|công ty định cư|cong ty dinh cu|định cư mỹ|định cư úc|định cư canada)\b', kw):
        if has_bofu or re.search(r'\b(tư vấn|công ty|dịch vụ|uy tín|tphcm|hồ sơ|chi phí)\b', kw):
            return {
                'lop_trien_khai': 'CỐT LÕI',
                'pheu': 'BOFU',
                'do_ro_y_dinh': 'RẤT RÕ',
                'do_phu_hop_offer': 3,
                'nhu_cau_nguoi_tim': 'Tìm công ty tư vấn định cư uy tín tại TP.HCM',
                'y_dinh_tim_kiem': 'Giao dịch / Chọn công ty tư vấn định cư',
                'bang_chung_rieng': "Người dùng chủ động tìm kiếm công ty tư vấn định cư uy tín, khớp trực tiếp dịch vụ tổng thể của GBlueSea tại Q.1 TP.HCM.",
                'trang_dich': 'https://www.visagbluesea.com/',
                'chien_dich': 'GGSearch_DichVu_DinhCu_TongHop',
                'theme': 'DinhCuTongHop'
            }
        else:
            return {
                'lop_trien_khai': 'CHẠY THỬ',
                'pheu': 'MOFU',
                'do_ro_y_dinh': 'KHÁ RÕ',
                'do_phu_hop_offer': 2,
                'nhu_cau_nguoi_tim': 'Tìm hiểu các diện định cư quốc tế',
                'y_dinh_tim_kiem': 'Cân nhắc phương án định cư',
                'bang_chung_rieng': "Quan tâm đến việc định cư quốc tế, phù hợp cho nhóm chạy thử tiếp thị lại.",
                'trang_dich': 'https://www.visagbluesea.com/',
                'chien_dich': 'GGSearch_DichVu_DinhCu_TongHop',
                'theme': 'DinhCuTongHop'
            }

    # Offer 5: Dịch vụ Visa (Mỹ, Úc, Schengen, Canada, Châu Âu)
    if re.search(r'\b(visa|thị thực|thi thuc)\b', kw) and re.search(r'\b(mỹ|my|úc|uc|canada|schengen|pháp|châu âu|chau au|anh|du lịch|du lich|thăm thân|tham than|công tác|cong tac)\b', kw):
        if re.search(r'\b(dịch vụ|dich vu|làm visa|lam visa|xin visa|hồ sơ|thủ tục|bao đậu|uy tín|chi phí|giá|tphcm)\b', kw):
            return {
                'lop_trien_khai': 'CỐT LÕI',
                'pheu': 'BOFU',
                'do_ro_y_dinh': 'RẤT RÕ',
                'do_phu_hop_offer': 3,
                'nhu_cau_nguoi_tim': 'Tìm dịch vụ làm hồ sơ visa du lịch/thăm thân uy tín',
                'y_dinh_tim_kiem': 'Giao dịch / Thuê dịch vụ visa',
                'bang_chung_rieng': "Nhu cầu thuê dịch vụ làm visa rõ ràng, đúng mảng dịch vụ visa quốc tế GBlueSea đang cung cấp.",
                'trang_dich': 'https://www.visagbluesea.com/tourist-visas',
                'chien_dich': 'GGSearch_DichVu_Visa_QuocTe',
                'theme': 'DichVuVisa'
            }
        else:
            return {
                'lop_trien_khai': 'CHẠY THỬ',
                'pheu': 'MOFU',
                'do_ro_y_dinh': 'KHÁ RÕ',
                'do_phu_hop_offer': 2,
                'nhu_cau_nguoi_tim': 'Tìm hiểu thủ tục, giấy tờ xin visa',
                'y_dinh_tim_kiem': 'Cân nhắc thủ tục visa',
                'bang_chung_rieng': "Khảo sát thủ tục xin visa, có thể chuyển đổi thành khách hàng dịch vụ khi thấy hồ sơ phức tạp.",
                'trang_dich': 'https://www.visagbluesea.com/tourist-visas',
                'chien_dich': 'GGSearch_DichVu_Visa_QuocTe',
                'theme': 'DichVuVisa'
            }

    # Offer 6: Du học các nước (Úc, Mỹ, Canada, Đức, New Zealand, Singapore, Nghề)
    if re.search(r'\b(du học|du hoc)\b', kw) and re.search(r'\b(úc|uc|mỹ|my|canada|đức|duc|singapore|anh|new zealand|nghề|nghe)\b', kw):
        country_m = re.search(r'\b(úc|uc|mỹ|my|canada|đức|duc|singapore|anh|new zealand|nghề|nghe)\b', kw).group(0)
        c_title = country_m.title()
        if re.search(r'\b(tư vấn|công ty|trung tâm|chi phí|học bổng|nghề|ở đâu|uy tín|hồ sơ|thủ tục)\b', kw):
            return {
                'lop_trien_khai': 'CỐT LÕI',
                'pheu': 'BOFU',
                'do_ro_y_dinh': 'RẤT RÕ',
                'do_phu_hop_offer': 3,
                'nhu_cau_nguoi_tim': f"Tìm trung tâm tư vấn hoặc học bổng du học {c_title}",
                'y_dinh_tim_kiem': f"Giao dịch / Đăng ký du học {c_title}",
                'bang_chung_rieng': f"Ý định tìm kiếm tư vấn du học {c_title} rõ nét, thuộc danh mục đối tác của GBlueSea.",
                'trang_dich': 'https://www.visagbluesea.com/',
                'chien_dich': f"GGSearch_DuHoc_{c_title}",
                'theme': f"DuHoc_{c_title}"
            }
        else:
            return {
                'lop_trien_khai': 'CHẠY THỬ',
                'pheu': 'MOFU',
                'do_ro_y_dinh': 'KHÁ RÕ',
                'do_phu_hop_offer': 2,
                'nhu_cau_nguoi_tim': f"Tìm hiểu thông tin du học {c_title}",
                'y_dinh_tim_kiem': f"Nghiên cứu du học {c_title}",
                'bang_chung_rieng': f"Nghiên cứu thông tin du học {c_title}, phù hợp đưa vào nhóm test để đánh giá chuyển đổi.",
                'trang_dich': 'https://www.visagbluesea.com/',
                'chien_dich': f"GGSearch_DuHoc_{c_title}",
                'theme': f"DuHoc_{c_title}"
            }

    # Offer 7: Tư vấn du học tổng hợp tại TP.HCM
    if re.search(r'\b(tư vấn du học|tu van du hoc|trung tâm du học|trung tam du hoc|công ty du học|cong ty du hoc)\b', kw):
        return {
            'lop_trien_khai': 'CỐT LÕI',
            'pheu': 'BOFU',
            'do_ro_y_dinh': 'RẤT RÕ',
            'do_phu_hop_offer': 3,
            'nhu_cau_nguoi_tim': 'Tìm công ty tư vấn du học uy tín tại TP.HCM',
            'y_dinh_tim_kiem': 'Giao dịch / Chọn công ty du học',
            'bang_chung_rieng': "Nhu cầu tìm kiếm trực tiếp công ty tư vấn du học, phù hợp 100% với định vị doanh nghiệp của GBlueSea.",
            'trang_dich': 'https://www.visagbluesea.com/',
            'chien_dich': 'GGSearch_DichVu_DuHoc_TongHop',
            'theme': 'DuHocTongHop'
        }

    # Offer 8: Broad Study Abroad or Visa terms
    if re.search(r'\b(du học|visa|định cư)\b', kw):
        return {
            'lop_trien_khai': 'CHẠY THỬ',
            'pheu': 'TOFU',
            'do_ro_y_dinh': 'MƠ HỒ',
            'do_phu_hop_offer': 2,
            'nhu_cau_nguoi_tim': 'Tìm hiểu chung về định cư hoặc du học',
            'y_dinh_tim_kiem': 'Khảo sát chung',
            'bang_chung_rieng': "Truy vấn chung chưa nêu rõ quốc gia hay bậc học, chỉ nên chạy thử với ngân sách nhỏ và theo dõi chặt.",
            'trang_dich': 'https://www.visagbluesea.com/',
            'chien_dich': 'GGSearch_KhaoSat_TongHop',
            'theme': 'KhaoSat'
        }

    # Fallback to Do Not Run
    return {
        'lop_trien_khai': 'KHÔNG CHẠY',
        'pheu': 'TOFU',
        'do_ro_y_dinh': 'MƠ HỒ',
        'do_phu_hop_offer': 0,
        'nhu_cau_nguoi_tim': 'Nhu cầu không rõ ràng hoặc không liên quan dịch vụ',
        'y_dinh_tim_kiem': 'Truy vấn không xác định',
        'bang_chung_rieng': "Không khớp với bất kỳ dịch vụ hay thị trường nào của GBlueSea, loại bỏ để bảo vệ ngân sách.",
        'trang_dich': 'https://www.visagbluesea.com/',
        'loai_ly_do': 'Không liên quan dịch vụ'
    }

# Run Qualification
qualified_rows = []
for idx, row in df_all.iterrows():
    q = qualify_keyword(row)
    combined = {**row.to_dict(), **q}
    qualified_rows.append(combined)

df_qualified = pd.DataFrame(qualified_rows)
print("\n--- Summary of Classification ---")
print(df_qualified['lop_trien_khai'].value_counts())

# Split into Active (Core + Test) and Excluded (Drop)
active_df = df_qualified[df_qualified['lop_trien_khai'].isin(['CỐT LÕI', 'CHẠY THỬ'])].copy()
drop_df = df_qualified[df_qualified['lop_trien_khai'] == 'KHÔNG CHẠY'].copy()

print(f"Active keywords: {len(active_df)}")
print(f"Excluded keywords: {len(drop_df)}")

# 3. Semantic Sub-Intent for STAG
def get_sub_intent(row):
    kw = row['kw_norm']
    theme = row.get('theme', 'Chung')
    
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

# 4. Disciplined STAG Partition Algorithm (Guaranteed 4 to 10 keywords per group)
def partition_bucket_4_to_10(df_subset, base_name):
    n = len(df_subset)
    if n == 0:
        return []
    
    sorted_df = df_subset.sort_values(by=['volume', 'low_bid'], ascending=[False, False]).copy()
    
    if n <= 10:
        sorted_df['nhom_quang_cao'] = base_name
        return [sorted_df]
    
    # Calculate best k
    k_min = int(np.ceil(n / 10.0))
    k_max = int(np.floor(n / 4.0))
    if k_max < k_min:
        k_max = k_min
        
    best_k = k_min
    best_diff = 999
    for k in range(k_min, k_max + 1):
        avg_size = n / k
        diff = abs(avg_size - 7.0)
        if diff < best_diff:
            best_diff = diff
            best_k = k
            
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

# Pass 1: Bucket sub_intents with >= 4 keywords
pass1_buckets = []
underflows_dict = {}

for (camp, lop, sub_intent), sub_df in active_df.groupby(['chien_dich', 'lop_trien_khai', 'sub_intent']):
    base_name = f"STAG_{sub_intent}"
    if len(sub_df) >= 4:
        buckets = partition_bucket_4_to_10(sub_df, base_name)
        pass1_buckets.extend(buckets)
    else:
        key = (camp, lop)
        if key not in underflows_dict:
            underflows_dict[key] = []
        underflows_dict[key].append(sub_df)

# Pass 2: Merge underflows per (camp, lop)
pass2_buckets = []
leftover_underflows = []

for (camp, lop), list_dfs in underflows_dict.items():
    combined = pd.concat(list_dfs)
    camp_clean = camp.replace('GGSearch_', '')
    base_name = f"STAG_{camp_clean}_TongHop_{lop[:3]}"
    if len(combined) >= 4:
        buckets = partition_bucket_4_to_10(combined, base_name)
        pass2_buckets.extend(buckets)
    else:
        leftover_underflows.append(combined)

all_buckets = pass1_buckets + pass2_buckets

# Pass 3: Distribute tiny leftovers strictly into existing groups without exceeding 10
if leftover_underflows:
    tiny_leftovers = pd.concat(leftover_underflows).sort_values(by='volume', ascending=False)
    for idx, row in tiny_leftovers.iterrows():
        kw_camp = row['chien_dich']
        kw_lop = row['lop_trien_khai']
        
        # Best bucket: same camp, same lop, size < 10, smallest size
        best_idx = -1
        min_sz = 999
        for b_idx, b_df in enumerate(all_buckets):
            if b_df.iloc[0]['chien_dich'] == kw_camp and b_df.iloc[0]['lop_trien_khai'] == kw_lop:
                if len(b_df) < 10 and len(b_df) < min_sz:
                    min_sz = len(b_df)
                    best_idx = b_idx
                    
        # If none found in same camp, find any bucket in same lop with size < 10
        if best_idx == -1:
            for b_idx, b_df in enumerate(all_buckets):
                if b_df.iloc[0]['lop_trien_khai'] == kw_lop and len(b_df) < 10 and len(b_df) < min_sz:
                    min_sz = len(b_df)
                    best_idx = b_idx
                    
        if best_idx != -1:
            row_df = pd.DataFrame([row])
            row_df['nhom_quang_cao'] = all_buckets[best_idx].iloc[0]['nhom_quang_cao']
            all_buckets[best_idx] = pd.concat([all_buckets[best_idx], row_df])
        else:
            # If all are >= 10, pick the smallest overall bucket and add
            smallest_idx = min(range(len(all_buckets)), key=lambda i: len(all_buckets[i]))
            row_df = pd.DataFrame([row])
            row_df['nhom_quang_cao'] = all_buckets[smallest_idx].iloc[0]['nhom_quang_cao']
            all_buckets[smallest_idx] = pd.concat([all_buckets[smallest_idx], row_df])

final_active_df = pd.concat(all_buckets).reset_index(drop=True)
print(f"Total active keywords grouped: {len(final_active_df)}")

group_sizes = final_active_df.groupby('nhom_quang_cao').size()
print(f"Total STAG groups: {len(group_sizes)}")
print(f"Min group size: {group_sizes.min()}, Max group size: {group_sizes.max()}")
print(f"Groups < 4: {(group_sizes < 4).sum()}, Groups > 10: {(group_sizes > 10).sum()}, Groups > 12: {(group_sizes > 12).sum()}")

# 5. CPC & Bid Calculations
def calc_cpc(row):
    low = row['low_bid']
    high = row['high_bid']
    if low > 0 and high > 0:
        return (low + high) / 2.0
    elif low > 0:
        return low
    elif high > 0:
        return high
    else:
        # Default fallback based on theme
        theme = row.get('theme', '')
        if 'EB5' in theme:
            return 45000.0
        elif 'GoldenVisa' in theme:
            return 35000.0
        elif 'PhanLan' in theme:
            return 22000.0
        elif 'DinhCu' in theme:
            return 30000.0
        elif 'Visa' in theme:
            return 18000.0
        elif 'DuHoc' in theme:
            return 25000.0
        return 16000.0

final_active_df['cpc_trung_binh'] = final_active_df.apply(calc_cpc, axis=1)
final_active_df['gioi_han_cpc_toi_da'] = final_active_df['cpc_trung_binh'] * 1.3
final_active_df['kieu_doi_sanh'] = 'Phrase'
final_active_df['tu_khoa_chuan_hoa'] = final_active_df['keyword'].apply(lambda x: f'"{x.strip()}"')
final_active_df['trang_thai_nguoi_dung'] = 'KHÔNG_CÓ_YÊU_CẦU'

# 6. Wave Rollout & Budget Allocation (Target 500,000 VND / day = 15,000,000 VND / month)
# Group stats to prioritize groups
group_summary = final_active_df.groupby('nhom_quang_cao').agg({
    'volume': 'sum',
    'cpc_trung_binh': 'mean',
    'keyword': 'count',
    'lop_trien_khai': 'first',
    'chien_dich': 'first',
    'pheu': 'first',
    'trang_dich': 'first'
}).reset_index()

group_summary.rename(columns={'keyword': 'so_tu_khoa'}, inplace=True)

# Define Core Priority Ranking
def get_group_priority(row):
    lop = row['lop_trien_khai']
    group = row['nhom_quang_cao']
    camp = row['chien_dich']
    
    if lop != 'CỐT LÕI':
        return 999
        
    score = 100
    if 'EB5' in group or 'EB5' in camp:
        score = 10
    elif 'GoldenVisa' in group or 'HyLap' in group or 'Sip' in group:
        score = 20
    elif 'PhanLan' in group:
        score = 30
    elif 'DinhCu_TPHCM' in group or 'DinhCu_CongTy' in group:
        score = 40
    elif 'Visa_My' in group or 'Visa_Uc' in group:
        score = 50
    elif 'DuHoc_Uc' in group or 'DuHoc_My' in group:
        score = 60
    elif 'DuHoc_Canada' in group or 'DuHoc_Đức' in group:
        score = 70
    elif 'DuHoc_Nghề' in group:
        score = 80
    return score

group_summary['priority_score'] = group_summary.apply(get_group_priority, axis=1)
group_summary.sort_values(by=['priority_score', 'volume'], ascending=[True, False], inplace=True)

# Select Top Core Groups for Wave 1 (ENABLED) to fit 15,000,000 VND / month
# Aim for ~10-12 top core groups, each getting 1.0M - 1.8M VND
wave1_budget_total = 15000000.0
allocated_so_far = 0.0

group_status_map = {}
group_budget_map = {}
group_wave_map = {}

core_candidates = group_summary[group_summary['lop_trien_khai'] == 'CỐT LÕI'].copy()

# Allocate budget to top 10-12 core groups
for idx, row in group_summary.iterrows():
    g_name = row['nhom_quang_cao']
    lop = row['lop_trien_khai']
    vol = row['volume']
    cpc = row['cpc_trung_binh']
    
    if lop == 'CỐT LÕI' and allocated_so_far < 14500000.0:
        # Determine group budget: between 1,200,000 and 1,800,000 based on volume
        b_alloc = 1500000.0
        if vol > 500:
            b_alloc = 1800000.0
        elif vol < 50:
            b_alloc = 1200000.0
            
        if allocated_so_far + b_alloc > 15500000.0:
            b_alloc = wave1_budget_total - allocated_so_far
            
        allocated_so_far += b_alloc
        group_status_map[g_name] = 'ENABLED'
        group_wave_map[g_name] = 'ĐỢT 1 - BẬT NGAY'
        group_budget_map[g_name] = b_alloc
    elif lop == 'CỐT LÕI':
        group_status_map[g_name] = 'PAUSED'
        group_wave_map[g_name] = 'ĐỢT 2 - CHỜ MỞ RỘNG'
        group_budget_map[g_name] = 0.0
    else:
        group_status_map[g_name] = 'PAUSED'
        group_wave_map[g_name] = 'ĐỢT TEST'
        group_budget_map[g_name] = 0.0

print(f"Total Wave 1 ENABLED Budget Allocated: {allocated_so_far:,.0f} VND / month")
enabled_count = sum(1 for v in group_status_map.values() if v == 'ENABLED')
print(f"Total ENABLED Groups: {enabled_count}")

# Map back to final_active_df
final_active_df['trang_thai_khoi_chay_nhom'] = final_active_df['nhom_quang_cao'].map(group_status_map)
final_active_df['dot_trien_khai'] = final_active_df['nhom_quang_cao'].map(group_wave_map)
final_active_df['ngan_sach_nhom'] = final_active_df['nhom_quang_cao'].map(group_budget_map)

# 7. Apply Forecast Contract demand-budget-v1 (volume_proxy)
reach_factor = 0.50
ctr = 0.08
cvr = 0.02

# Calculate metrics at group level first (avoid double counting)
group_metrics = {}
for g_name, g_df in final_active_df.groupby('nhom_quang_cao'):
    g_vol = g_df['volume'].sum()
    g_cpc = g_df['cpc_trung_binh'].mean()
    g_status = group_status_map[g_name]
    g_budget = group_budget_map[g_name]
    
    # Potential clicks
    pot_impressions = g_vol * reach_factor
    pot_clicks = pot_impressions * ctr
    
    if g_status == 'ENABLED' and g_budget > 0:
        clicks_by_budget = g_budget / g_cpc if g_cpc > 0 else 0
        forecast_clicks = min(pot_clicks, clicks_by_budget)
        forecast_cost = forecast_clicks * g_cpc
        forecast_leads = forecast_clicks * cvr
        clicks_per_day = forecast_clicks / 30.0
    else:
        # PAUSED groups: forecast in running scenario is strictly 0
        forecast_clicks = 0.0
        forecast_cost = 0.0
        forecast_leads = 0.0
        clicks_per_day = 0.0
        
    group_metrics[g_name] = {
        'volume': g_vol,
        'cpc': g_cpc,
        'budget': g_budget,
        'pot_clicks': pot_clicks,
        'forecast_clicks': forecast_clicks,
        'forecast_cost': forecast_cost,
        'forecast_leads': forecast_leads,
        'clicks_per_day': clicks_per_day
    }

# Distribute model metrics down to keywords proportionally for presentation
def assign_kw_metrics(row):
    g_name = row['nhom_quang_cao']
    gm = group_metrics[g_name]
    g_vol = gm['volume']
    kw_vol = row['volume']
    
    # Weight within group
    weight = kw_vol / g_vol if g_vol > 0 else (1.0 / group_sizes[g_name])
    
    kw_clicks = gm['forecast_clicks'] * weight
    kw_budget = gm['budget'] * weight
    kw_cost = gm['forecast_cost'] * weight
    
    return pd.Series({
        'luot_nhap_thang_uoc_tinh': kw_clicks,
        'luot_nhap_ngay_nhom': gm['clicks_per_day'],
        'ty_le_chuyen_doi': cvr,
        'ngan_sach_thang_uoc_tinh': kw_budget,
        'chi_phi_du_bao_kw': kw_cost
    })

kw_metric_cols = final_active_df.apply(assign_kw_metrics, axis=1)
final_active_df = pd.concat([final_active_df, kw_metric_cols], axis=1)

# Budget proportion
tot_b = final_active_df['ngan_sach_thang_uoc_tinh'].sum()
final_active_df['ty_trong_ngan_sach'] = final_active_df['ngan_sach_thang_uoc_tinh'] / tot_b if tot_b > 0 else 0.0

# Funnel indicator columns
final_active_df['quan_tam'] = final_active_df['pheu'].apply(lambda x: 'X' if x == 'TOFU' else '')
final_active_df['can_nhac'] = final_active_df['pheu'].apply(lambda x: 'X' if x == 'MOFU' else '')
final_active_df['mua_hang'] = final_active_df['pheu'].apply(lambda x: 'X' if x == 'BOFU' else '')

print("Active keywords and metrics processed successfully.")
