import sys
import os
import re
import pandas as pd
import numpy as np

sys.stdout.reconfigure(encoding='utf-8')

csv_path = '_Luu_Tru_Ky_Thuat/Keyword_Planner_Raw/Historical_Metrics_HCM_Real.csv'

# Load data
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

df = pd.DataFrame(raw_rows).drop_duplicates(subset=['keyword'])
print(f"Total loaded: {len(df)} unique keywords")

# Helper normalization
def normalize_kw(kw):
    return re.sub(r'\s+', ' ', kw.strip().lower())

df['kw_norm'] = df['keyword'].apply(normalize_kw)

# Classify keywords
def classify_keyword(row):
    kw = row['kw_norm']
    vol = row['volume']
    low_bid = row['low_bid']
    high_bid = row['high_bid']
    
    # 1. Negative & Disqualification Filters (Lớp 3)
    # 1.1 Out of Target Geo (Outside HCM)
    out_geo_match = re.search(r'\b(hà nội|ha noi|đà nẵng|da nang|hải phòng|hai phong|cần thơ|can tho|nha trang|quảng ninh|huế|vinh|bắc ninh|nam định)\b', kw)
    if out_geo_match:
        geo_name = out_geo_match.group(0)
        return {
            'lop_trien_khai': 'KHÔNG CHẠY',
            'pheu': 'TOFU',
            'do_ro_y_dinh': 'KHÁ RÕ',
            'do_phu_hop_offer': 0,
            'nhu_cau_nguoi_tim': f'Tìm kiếm dịch vụ/thông tin tại khu vực {geo_name.title()}',
            'y_dinh_tim_kiem': 'Tìm kiếm ngoài vùng phục vụ',
            'bang_chung_rieng': f"Chứa địa danh '{geo_name}' nằm ngoài khu vực mục tiêu TP.HCM của chiến dịch, gây lãng phí ngân sách.",
            'trang_dich': 'https://www.visagbluesea.com/',
            'loai_ly_do': 'Ngoài khu vực phục vụ'
        }
    
    # 1.2 Jobs, Recruitment, Labor workers (XKLD, nails, etc.)
    jobs_match = re.search(r'\b(tuyển dụng|tuyen dung|tìm việc|tim viec|việc làm|viec lam|cần thợ|tuyển thợ|thợ nail|làm nail|tuyển công nhân|xklđ|xkld|xuất khẩu lao động|xuat khau lao dong|lương bao nhiêu|mẫu cv|tuyển sinh|xin việc)\b', kw)
    if jobs_match:
        job_term = jobs_match.group(0)
        return {
            'lop_trien_khai': 'KHÔNG CHẠY',
            'pheu': 'TOFU',
            'do_ro_y_dinh': 'KHÁ RÕ',
            'do_phu_hop_offer': 0,
            'nhu_cau_nguoi_tim': f'Tìm kiếm cơ hội việc làm/tuyển dụng liên quan đến {job_term}',
            'y_dinh_tim_kiem': 'Tìm việc làm / Tuyển dụng',
            'bang_chung_rieng': f"Chứa cụm từ tuyển dụng/việc làm '{job_term}', sai hoàn toàn chân dung khách hàng dịch vụ định cư/du học.",
            'trang_dich': 'https://www.visagbluesea.com/',
            'loai_ly_do': 'Sai đối tượng - Tìm việc làm'
        }

    # 1.3 Free, DIY, Books, Exam preparation, English learning
    diy_match = re.search(r'\b(tự làm|tu lam|tự xin|tu xin|tự túc|tu tuc|miễn phí|mien phi|free|tải|download|sách|tai lieu|tài liệu|đề thi|luyện thi|ngữ pháp|từ vựng|cách học tiếng anh|tieng anh du kich|mẫu đơn)\b', kw)
    if diy_match:
        diy_term = diy_match.group(0)
        return {
            'lop_trien_khai': 'KHÔNG CHẠY',
            'pheu': 'TOFU',
            'do_ro_y_dinh': 'KHÁ RÕ',
            'do_phu_hop_offer': 0,
            'nhu_cau_nguoi_tim': f'Tự làm thủ tục hoặc tìm tài liệu miễn phí ({diy_term})',
            'y_dinh_tim_kiem': 'Tự làm / Tìm kiếm miễn phí',
            'bang_chung_rieng': f"Chứa ý định tự túc/tài liệu miễn phí '{diy_term}', không có nhu cầu sử dụng dịch vụ tư vấn có phí.",
            'trang_dich': 'https://www.visagbluesea.com/',
            'loai_ly_do': 'Tự làm / Miễn phí / Không thương mại'
        }

    # 1.4 General Trivia, Entertainment, Irrelevant topics
    irrelevant_match = re.search(r'\b(phim|bài hát|thời tiết|múi giờ|dân số|bản đồ|thủ đô|lịch sử|chiến tranh|diện tích|quốc kỳ|món ăn|khách sạn|vé máy bay|tour du lịch|du lịch giá rẻ)\b', kw)
    if irrelevant_match:
        irr_term = irrelevant_match.group(0)
        return {
            'lop_trien_khai': 'KHÔNG CHẠY',
            'pheu': 'TOFU',
            'do_ro_y_dinh': 'MƠ HỒ',
            'do_phu_hop_offer': 0,
            'nhu_cau_nguoi_tim': f'Tra cứu kiến thức bách khoa/du lịch tự do ({irr_term})',
            'y_dinh_tim_kiem': 'Tra cứu thông tin chung',
            'bang_chung_rieng': f"Thuộc chủ đề bách khoa/tra cứu phi thương mại '{irr_term}', không phát sinh chuyển đổi dịch vụ di trú.",
            'trang_dich': 'https://www.visagbluesea.com/',
            'loai_ly_do': 'Lạc đề / Kiến thức chung'
        }

    # 2. Qualified Commercial Keywords (Lớp 1 & Lớp 2)
    # Detect Commercial Indicators
    has_commercial = bool(re.search(r'\b(dịch vụ|dich vu|công ty|cong ty|trung tâm|trung tam|tư vấn|tu van|chi phí|chi phi|giá|gia|báo giá|bao gia|bao nhiêu tiền|ở đâu|o dau|uy tín|uy tin|trọn gói|tron goi|hồ sơ|ho so|đầu tư|dau tu|dự án|du an|visa|thủ tục|thu tuc|học bổng|hoc bong|thpt|thạc sĩ|thac si|nghề|nghe|định cư|dinh cu)\b', kw))
    has_bofu = bool(re.search(r'\b(dịch vụ|công ty|trung tâm|tư vấn|chi phí|báo giá|bao nhiêu tiền|ở đâu|uy tín|trọn gói|đầu tư eb5|visa eb5|golden visa|mua nhà|dự án eb5)\b', kw))
    
    # 2.1 EB-5 Investment USA
    if re.search(r'\beb[- ]?5\b', kw) or (re.search(r'\bđịnh cư mỹ\b|\bdinh cu my\b', kw) and re.search(r'\bđầu tư\b|\bdau tu\b|\bdiện đầu tư\b', kw)):
        if has_bofu or re.search(r'\b(đầu tư|dự án|visa|tư vấn|chi phí|luật sư)\b', kw):
            return {
                'lop_trien_khai': 'CỐT LÕI',
                'pheu': 'BOFU',
                'do_ro_y_dinh': 'RẤT RÕ',
                'do_phu_hop_offer': 3,
                'nhu_cau_nguoi_tim': 'Tìm hiểu chương trình hoặc dịch vụ tư vấn đầu tư định cư Mỹ diện EB-5',
                'y_dinh_tim_kiem': 'Giao dịch / Thuê dịch vụ đầu tư EB-5',
                'bang_chung_rieng': f"Truy vấn trực tiếp chương trình đầu tư EB-5 Mỹ khớp 100% dịch vụ trọng tâm trị giá cao của GBlueSea.",
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
                'nhu_cau_nguoi_tim': 'Tìm hiểu thông tin, điều kiện diện EB-5',
                'y_dinh_tim_kiem': 'Nghiên cứu / Cân nhắc điều kiện EB-5',
                'bang_chung_rieng': f"Tìm hiểu kiến thức/điều kiện chương trình EB-5, phù hợp nuôi dưỡng chuyển đổi qua Landing Page chuyên sâu.",
                'trang_dich': 'https://www.visagbluesea.com/us-green-card-eb-5',
                'chien_dich': 'GGSearch_DinhCu_EB5_My',
                'theme': 'EB5'
            }

    # 2.2 Golden Visa Europe (Hy Lạp, Síp, Malta, Bồ Đào Nha, Châu Âu)
    gv_match = re.search(r'\b(golden visa|hy lạp|greece|síp|cyprus|malta|mprp|bồ đào nha|portugal|định cư châu âu|dinh cu chau au|quốc tịch thứ hai|nauru)\b', kw)
    if gv_match and re.search(r'\b(định cư|dinh cu|visa|đầu tư|dau tu|mua nhà|thường trú|quốc tịch)\b', kw):
        country = gv_match.group(0)
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
                'nhu_cau_nguoi_tim': f'Tìm chương trình hoặc đơn vị tư vấn định cư đầu tư Golden Visa ({country})',
                'y_dinh_tim_kiem': f'Giao dịch / Định cư đầu tư {country.title()}',
                'bang_chung_rieng': f"Khớp dịch vụ bất động sản di trú và Golden Visa {country.title()} có trang đích riêng trên website.",
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
                'nhu_cau_nguoi_tim': f'Tìm hiểu thông tin định cư tại {country}',
                'y_dinh_tim_kiem': f'Nghiên cứu định cư {country.title()}',
                'bang_chung_rieng': f"Khảo sát thông tin định cư {country.title()}, đưa vào nhóm test để đánh giá tỷ lệ điền form.",
                'trang_dich': lp,
                'chien_dich': 'GGSearch_DinhCu_GoldenVisa_ChauAu',
                'theme': 'GoldenVisa'
            }

    # 2.3 Du học Phần Lan (Flagship Core of GBlueSea)
    if 'phần lan' in kw or 'phan lan' in kw:
        if re.search(r'\b(du học|du hoc|học bổng|hoc bong|thpt|thạc sĩ|thac si|định cư|doanh nhân)\b', kw):
            if re.search(r'\b(tư vấn|học bổng|chi phí|thpt|thạc sĩ|nghề|công ty|dịch vụ|ở đâu|điều kiện)\b', kw) or kw in ['du học phần lan', 'du hoc phan lan']:
                return {
                    'lop_trien_khai': 'CỐT LÕI',
                    'pheu': 'BOFU',
                    'do_ro_y_dinh': 'RẤT RÕ',
                    'do_phu_hop_offer': 3,
                    'nhu_cau_nguoi_tim': 'Tìm lộ trình, học bổng hoặc tư vấn du học Phần Lan',
                    'y_dinh_tim_kiem': 'Giao dịch / Đăng ký tư vấn du học Phần Lan',
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
                    'bang_chung_rieng': "Tìm hiểu thông tin du học Phần Lan, cần chạy thử để đo lường mức độ quan tâm.",
                    'trang_dich': 'https://www.visagbluesea.com/study-in-finland',
                    'chien_dich': 'GGSearch_DuHoc_PhanLan_MuiNhon',
                    'theme': 'DuHocPhanLan'
                }

    # 2.4 Dịch vụ Định cư chung / Tư vấn định cư TPHCM
    if re.search(r'\b(tư vấn định cư|tu van dinh cu|dịch vụ định cư|dich vu dinh cu|công ty định cư|cong ty dinh cu|định cư mỹ|định cư úc|định cư canada)\b', kw):
        if has_bofu or re.search(r'\b(tư vấn|công ty|dịch vụ|uy tín|tphcm|hồ sơ|chi phí)\b', kw):
            return {
                'lop_trien_khai': 'CỐT LÕI',
                'pheu': 'BOFU',
                'do_ro_y_dinh': 'RẤT RÕ',
                'do_phu_hop_offer': 3,
                'nhu_cau_nguoi_tim': 'Tìm công ty tư vấn định cư uy tín tại TP.HCM',
                'y_dinh_tim_kiem': 'Giao dịch / Tìm đơn vị tư vấn định cư',
                'bang_chung_rieng': "Người dùng tìm kiếm trực tiếp đơn vị tư vấn định cư chuyên nghiệp, khớp trực tiếp dịch vụ tổng thể của GBlueSea tại Q1 TPHCM.",
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
                'nhu_cau_nguoi_tim': 'Tìm hiểu các diện định cư nước ngoài',
                'y_dinh_tim_kiem': 'Cân nhắc lộ trình định cư',
                'bang_chung_rieng': "Quan tâm đến việc định cư nước ngoài nói chung, thuộc tệp tiềm năng cần tiếp thị lại.",
                'trang_dich': 'https://www.visagbluesea.com/',
                'chien_dich': 'GGSearch_DichVu_DinhCu_TongHop',
                'theme': 'DinhCuTongHop'
            }

    # 2.5 Dịch vụ Visa (Du lịch, Thăm thân, Công tác, Schengen, Mỹ, Úc, Canada)
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

    # 2.6 Du học các nước (Úc, Mỹ, Canada, Đức, New Zealand, Singapore, Du học nghề)
    if re.search(r'\b(du học|du hoc)\b', kw) and re.search(r'\b(úc|uc|mỹ|my|canada|đức|duc|singapore|anh|new zealand|nghề|nghe)\b', kw):
        country_match = re.search(r'\b(úc|uc|mỹ|my|canada|đức|duc|singapore|anh|new zealand|nghề|nghe)\b', kw).group(0)
        if re.search(r'\b(tư vấn|công ty|trung tâm|chi phí|học bổng|nghề|ở đâu|uy tín|hồ sơ|thủ tục)\b', kw):
            return {
                'lop_trien_khai': 'CỐT LÕI',
                'pheu': 'BOFU',
                'do_ro_y_dinh': 'RẤT RÕ',
                'do_phu_hop_offer': 3,
                'nhu_cau_nguoi_tim': f'Tìm trung tâm tư vấn hoặc thông tin chi phí du học {country_match.title()}',
                'y_dinh_tim_kiem': f'Giao dịch / Đăng ký tư vấn du học {country_match.title()}',
                'bang_chung_rieng': f"Ý định tìm kiếm dịch vụ tư vấn du học {country_match.title()} rõ nét, thuộc danh mục đối tác của GBlueSea.",
                'trang_dich': 'https://www.visagbluesea.com/',
                'chien_dich': f'GGSearch_DuHoc_{country_match.title()}',
                'theme': f'DuHoc_{country_match.title()}'
            }
        else:
            return {
                'lop_trien_khai': 'CHẠY THỬ',
                'pheu': 'MOFU',
                'do_ro_y_dinh': 'KHÁ RÕ',
                'do_phu_hop_offer': 2,
                'nhu_cau_nguoi_tim': f'Tìm hiểu thông tin du học {country_match.title()}',
                'y_dinh_tim_kiem': f'Nghiên cứu du học {country_match.title()}',
                'bang_chung_rieng': f"Nghiên cứu thông tin du học {country_match.title()}, phù hợp đưa vào nhóm test để đánh giá chuyển đổi.",
                'trang_dich': 'https://www.visagbluesea.com/',
                'chien_dich': f'GGSearch_DuHoc_{country_match.title()}',
                'theme': f'DuHoc_{country_match.title()}'
            }

    # 2.7 Tư vấn du học chung tại TP.HCM
    if re.search(r'\b(tư vấn du học|tu van du hoc|trung tâm du học|trung tam du hoc|công ty du học|cong ty du hoc)\b', kw):
        return {
            'lop_trien_khai': 'CỐT LÕI',
            'pheu': 'BOFU',
            'do_ro_y_dinh': 'RẤT RÕ',
            'do_phu_hop_offer': 3,
            'nhu_cau_nguoi_tim': 'Tìm công ty tư vấn du học uy tín tại TP.HCM',
            'y_dinh_tim_kiem': 'Giao dịch / Chọn công ty tư vấn du học',
            'bang_chung_rieng': "Nhu cầu tìm kiếm trực tiếp công ty tư vấn du học, phù hợp 100% với định vị doanh nghiệp của GBlueSea.",
            'trang_dich': 'https://www.visagbluesea.com/',
            'chien_dich': 'GGSearch_DichVu_DuHoc_TongHop',
            'theme': 'DuHocTongHop'
        }

    # 2.8 General Broad Visa or Study Abroad terms without country
    if re.search(r'\b(du học|visa|định cư)\b', kw):
        return {
            'lop_trien_khai': 'CHẠY THỬ',
            'pheu': 'TOFU',
            'do_ro_y_dinh': 'MƠ HỒ',
            'do_phu_hop_offer': 2,
            'nhu_cau_nguoi_tim': 'Tìm kiếm chung về định cư hoặc du học',
            'y_dinh_tim_kiem': 'Khảo sát thông tin diện rộng',
            'bang_chung_rieng': "Truy vấn chung chưa nêu rõ quốc gia hay bậc học, chỉ nên chạy thử với ngân sách nhỏ và theo dõi chặt.",
            'trang_dich': 'https://www.visagbluesea.com/',
            'chien_dich': 'GGSearch_KhaoSat_TongHop',
            'theme': 'KhaoSat'
        }

    # Default fallback to Do Not Run
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

# Run classification on dataframe
classified_rows = []
for idx, row in df.iterrows():
    c_res = classify_keyword(row)
    combined = {**row.to_dict(), **c_res}
    classified_rows.append(combined)

df_classified = pd.DataFrame(classified_rows)

print("\n--- Summary of Classification ---")
print(df_classified['lop_trien_khai'].value_counts())
print("\n--- Summary of Phễu ---")
print(df_classified['pheu'].value_counts())

core_df = df_classified[df_classified['lop_trien_khai'] == 'CỐT LÕI']
test_df = df_classified[df_classified['lop_trien_khai'] == 'CHẠY THỬ']
drop_df = df_classified[df_classified['lop_trien_khai'] == 'KHÔNG CHẠY']

print(f"\nCore keywords: {len(core_df)}, total volume: {core_df['volume'].sum():,.0f}")
print(f"Test keywords: {len(test_df)}, total volume: {test_df['volume'].sum():,.0f}")
print(f"Drop keywords: {len(drop_df)}, total volume: {drop_df['volume'].sum():,.0f}")

print("\nTop Core campaigns/themes:")
print(core_df['chien_dich'].value_counts())
