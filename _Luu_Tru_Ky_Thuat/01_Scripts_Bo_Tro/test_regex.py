import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

kw = 'định cư mỹ eb5'

print("Regex checks on kw:")
print("1. out_geo:", bool(re.search(r'\b(hà nội|ha noi|đà nẵng|da nang|hải phòng|hai phong|cần thơ|can tho|nha trang|quảng ninh|huế|vinh|bắc ninh|nam định|hải dương|thái nguyên)\b', kw)))
print("2. jobs:", bool(re.search(r'\b(tuyển dụng|tuyen dung|tìm việc|tim viec|việc làm|viec lam|cần thợ|tuyển thợ|thợ nail|làm nail|tuyển công nhân|xklđ|xkld|xuất khẩu lao động|xuat khau lao dong|lương bao nhiêu|mẫu cv|tuyển sinh|xin việc|phỏng vấn xin việc)\b', kw)))
print("3. diy:", bool(re.search(r'\b(tự làm|tu lam|tự xin|tu xin|tự túc|tu tuc|miễn phí|mien phi|free|tải|download|sách|tai lieu|tài liệu|đề thi|luyện thi|ngữ pháp|từ vựng|cách học tiếng anh|tieng anh du kich|mẫu đơn)\b', kw)))
print("4. irr:", bool(re.search(r'\b(phim|bài hát|thời tiết|múi giờ|dân số|bản đồ|thủ đô|lịch sử|chiến tranh|diện tích|quốc kỳ|món ăn|khách sạn|vé máy bay|tour du lịch|du lịch giá rẻ)\b', kw)))

print("EB5 match 1:", bool(re.search(r'\beb[- ]?5\b', kw)))
print("EB5 match 2:", bool(re.search(r'\bđịnh cư mỹ\b|\bdinh cu my\b', kw) and re.search(r'\bđầu tư\b|\bdau tu\b|\bdiện đầu tư\b', kw)))

# What is in build_v4_master_excel.py for EB5?
with open('_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/build_v4_master_excel.py', 'r', encoding='utf-8') as f:
    text = f.read()

eb5_idx = text.find("# EB-5")
print("\nCode around # EB-5:")
print(text[eb5_idx:eb5_idx+400])
