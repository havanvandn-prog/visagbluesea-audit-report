import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

skill_path = r"C:\Users\ADMIN\.gemini\config\skills\07-keyword-analysis-v4-ggads-chatgpt-toi-uu\SKILL.md"

with open(skill_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Section 0
old_sec0 = """1. SÀNG LỌC 100% TỪ KHÓA THÔ ĐỘC LẬP TỪNG DÒNG (RESEARCH WIDE - QUALIFY STRICTLY)
2. PHÂN TẦNG 3 LỚP RẠCH RÒI:
   ├── LỚP 1: TỪ KHÓA CỐT LÕI — ƯU TIÊN CHẠY (CORE PRECISION)
   ├── LỚP 2: TỪ KHÓA TIỀM NĂNG — CHẠY THỬ / THEO DÕI (CONTROLLED TESTING)
   └── LỚP 3: TỪ KHÓA KHÔNG NÊN CHẠY (DO NOT RUN - BUDGET PROTECTION)
3. CHIA NHÓM QUẢNG CÁO STAG CHUẨN KỶ LUẬT (4 – 10 TỪ KHÓA / NHÓM):
   └── Chạm mốc 10 từ khóa là tự động rà soát ngắt nhóm mới, tuyệt đối không gom bừa > 12 từ.
4. CHỌN NHÓM BẬT THEO NGÂN SÁCH VÀ NHU CẦU TÌM KIẾM:
   ├── ĐỢT 1 (ENABLED - BẬT NGAY): Top nhóm Cốt lõi dễ chốt đơn nhất vừa khít Ngân sách ngày
   ├── ĐỢT 2 (PAUSED - CHỜ MỞ RỘNG): Nhóm Cốt lõi chuẩn nhưng để tạm dừng chờ tăng ngân sách
   └── ĐỢT TEST (PAUSED - QUỸ TEST): Nhóm Chạy thử có kiểm soát
5. XUẤT MASTER EXCEL 11 SHEETS & BÀN GIAO SẴN SÀNG CHO SKILL /07.1 KIỂM ĐỊNH HẬU PHƯƠNG"""

new_sec0 = """1. SÀNG LỌC 100% TỪ KHÓA THÔ ĐỘC LẬP TỪNG DÒNG (RESEARCH WIDE - QUALIFY STRICTLY)
2. PHÂN TẦNG 3 LỚP RẠCH RÒI:
   ├── LỚP 1: TỪ KHÓA CỐT LÕI — ƯU TIÊN CHẠY (CORE PRECISION)
   ├── LỚP 2: TỪ KHÓA TIỀM NĂNG — CHẠY THỬ / THEO DÕI (CONTROLLED TESTING)
   └── LỚP 3: TỪ KHÓA KHÔNG NÊN CHẠY (DO NOT RUN - BUDGET PROTECTION)
3. CHIA NHÓM QUẢNG CÁO STAG CHUẨN KỶ LUẬT (4 – 10 TỪ KHÓA / NHÓM):
   └── Chạm mốc 10 từ khóa là tự động rà soát ngắt nhóm mới, tuyệt đối không gom bừa > 12 từ.
4. CÁCH LY CHIẾN DỊCH THEO BIÊN ĐỘ CPC (H. CPC THẤP & I. CPC CAO ≤ 2.0x):
   └── Chống bẫy nuốt ngân sách Maximize Clicks: Cấm nhồi từ khóa rẻ (dưới 10k) chung Campaign với từ khóa chốt đơn đắt (trên 30k).
5. CHỌN NHÓM BẬT THEO NGÂN SÁCH VÀ NHU CẦU TÌM KIẾM (WAVE ROLLOUT):
   ├── ĐỢT 1 (ENABLED - BẬT NGAY): Top nhóm Cốt lõi dễ chốt đơn nhất vừa khít Ngân sách ngày
   ├── ĐỢT 2 (PAUSED - CHỜ MỞ RỘNG): Nhóm Cốt lõi chuẩn nhưng để tạm dừng chờ tăng ngân sách
   └── ĐỢT TEST (PAUSED - QUỸ TEST): Nhóm Chạy thử có kiểm soát
6. XUẤT MASTER EXCEL 11 SHEETS & BÀN GIAO SẴN SÀNG CHO SKILL /07.1 KIỂM ĐỊNH HẬU PHƯƠNG"""

# Replace in content regardless of CRLF or LF
content = content.replace(old_sec0.replace('\n', '\r\n'), new_sec0.replace('\n', '\r\n'))
content = content.replace(old_sec0, new_sec0)

# 2. Add Section 4B
sec4b_text = """

---

# 4B. QUY TẮC CÁCH LY CHIẾN DỊCH THEO BIÊN ĐỘ CPC (CPC DISPERSION GUARD & ANTI-CANNIBALIZATION)

Đây là điều khoản kỹ thuật khóa cứng nhằm triệt tiêu hoàn toàn "bẫy nuốt ngân sách" của chiến lược giá thầu **Maximize Clicks (Tối đa hóa lượt nhấp có giới hạn giá thầu)**:

### 1. Bản Chất Vấn Đề (Hiện Tượng Nuốt Ngân Sách Chéo):
* Trong Google Search Ads, **Giới hạn giá thầu CPC tối đa (Max CPC Bid Limit)** và **Ngân sách ngày (Daily Budget)** được quản lý ở **Cấp Chiến Dịch (Campaign Level)**.
* Nếu gom chung các nhóm từ khóa có giá thầu chênh lệch lớn vào cùng một Campaign:
  * **Nếu đặt Max CPC thấp (để tiết kiệm):** Các từ khóa có ý định mua hàng nóng (BOFU: Đăng ký, lắp đặt, thuê dịch vụ, đầu tư EB-5...) có mức CPC sàn thị trường cao sẽ bị bóp nghẹt hoàn toàn, tỷ lệ hiển thị rớt về 0% vì không đủ điều kiện tham gia phiên đấu giá.
  * **Nếu đặt Max CPC cao (để cứu từ khóa BOFU):** Thuật toán Maximize Clicks sẽ ưu tiên hút toàn bộ ngân sách ngày vào các từ khóa rẻ (5.000 ₫ – 10.000 ₫) để đạt chỉ tiêu số lượng nhấp chuột nhiều nhất $\\rightarrow$ Ngân sách cạn kiệt trước khi nhóm BOFU chốt đơn kịp đấu giá.

### 2. Quy Tắc Khóa Cứng Biên Độ CPC Cấp Campaign ($\\le 2.0\\times$):
$$\\text{Tỷ Lệ Chênh Lệch CPC} = \\frac{\\text{CPC Trung Bình Nhóm Cao Nhất}}{\\text{CPC Trung Bình Nhóm Thấp Nhất}} \\le 2.0$$

* **Ngưỡng an toàn ($\\le 2.0\\times$):** Các nhóm từ khóa có mức CPC chênh lệch không quá 2.0 lần được phép nằm chung một Campaign.
* **Còi báo động đỏ (> 2.0x):** Nếu mức CPC giữa các nhóm chênh lệch vượt quá **2.0 lần** $\\rightarrow$ **BẮT BUỘC TÁCH THÀNH 2 CHIẾN DỊCH ĐỘC LẬP**:
  * **Campaign High-CPC (Săn Khách Nóng - BOFU):** Tập trung các từ khóa chốt đơn (Lắp đặt, đăng ký, thuê dịch vụ, mua ngay, đầu tư). Cấp ngân sách riêng biệt và đặt Max CPC Cap cao ($1.25\\times$ mức đấu thầu đầu trang).
  * **Campaign Mid/Low-CPC (Khảo Sát / Cân Nhắc - MOFU/TOFU):** Tập trung các từ khóa hỏi bảng giá, điều kiện, so sánh, quy trình. Đặt trần Max CPC thấp để gom traffic giá rẻ mà không làm ảnh hưởng đến nhóm High-CPC.

### 3. Công Thức Đặt Giới Hạn CPC Tối Đa (Cột K. GIỚI HẠN CPC TỐI ĐA):
$$\\text{Max CPC Cap (Campaign)} = \\text{CPC Trung Bình Dự Kiến của Dải Nhóm} \\times 1.25$$
*(Tuyệt đối không dùng chung một mức trần Max CPC cào bằng cho toàn bộ tài khoản).*"""

# Insert after Section 4 (before Section 5)
target_before_sec5 = "# 5. CHỌN ĐỢT BẬT THEO NGÂN SÁCH VÀ NHU CẦU"
if target_before_sec5 in content:
    content = content.replace(target_before_sec5, sec4b_text.strip() + "\n\n---\n\n" + target_before_sec5)
else:
    print("Warning: target_before_sec5 not found directly")

# 3. Add to Section 8: Hard Block Conditions
sec8_target = "* **Lỗi Gom Bừa Nhóm:** Có nhóm chứa **> 12 từ khóa** hoặc gom từ 2 biến thể sản phẩm khác nhau trở lên."
sec8_addition = """* **Lỗi Gom Bừa Nhóm:** Có nhóm chứa **> 12 từ khóa** hoặc gom từ 2 biến thể sản phẩm khác nhau trở lên.
* **Lỗi Xung Đột Biên Độ CPC (CPC Cannibalization):** Trong cùng 1 Campaign có các nhóm từ khóa chênh lệch CPC bình quân > 2.0x, gây nguy cơ bóp nghẹt hiển thị của từ khóa chốt đơn (BOFU) khi chạy Maximize Clicks."""

content = content.replace(sec8_target, sec8_addition)

with open(skill_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated SKILL.md for 07-keyword-analysis-v4-ggads-chatgpt-toi-uu successfully!")
