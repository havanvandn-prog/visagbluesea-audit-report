import sys

skill_path = r"C:\Users\ADMIN\.gemini\config\skills\10-google-ads-plan-v2-ggads\SKILL.md"

with open(skill_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update STEP 1 with CPC Dispersion Guard
step1_target = "## ⚡ STEP 1 — Campaign mix (Rẽ nhánh theo mode)"
step1_replacement = """## ⚡ STEP 1 — Campaign mix (Rẽ nhánh theo mode)

### 1.0 — ĐIỀU KHOẢN KHÓA CỨNG: CÁCH LY CHIẾN DỊCH THEO BIÊN ĐỘ CPC (CPC DISPERSION GUARD & ANTI-CANNIBALIZATION)

Đây là quy tắc cấu trúc sống còn để triệt tiêu "bẫy nuốt ngân sách" của chiến lược giá thầu **Maximize Clicks**:

1. **Giới hạn chênh lệch tối đa trong 1 Campaign ($\le 2.0\\times$):**
   - Các nhóm từ khóa nằm chung 1 Campaign chỉ được có mức CPC chênh lệch tối đa **1.8x – 2.0x**.
   - **Công thức kiểm định:**
     $$\\text{Tỷ Lệ Chênh Lệch CPC} = \\frac{\\text{CPC Nhóm Cao Nhất}}{\\text{CPC Nhóm Thấp Nhất}} \\le 2.0$$
   - Nếu $\\text{Tỷ Lệ Chênh Lệch} > 2.0 \\implies$ **BẮT BUỘC TÁCH THÀNH 2 CAMPAIGN ĐỘC LẬP**.

2. **Phân tách 2 tầng Campaign thực chiến:**
   - **Campaign High-CPC (Săn Lead Nóng - BOFU):** Chứa các nhóm từ khóa chốt đơn ("Lắp đặt, đăng ký, thuê dịch vụ, mua ngay, đầu tư di trú..."). Cấp ngân sách riêng biệt và đặt Max CPC Cap cao ($1.25\\times$ CPC thị trường).
   - **Campaign Mid/Low-CPC (Khảo sát / Cân nhắc - MOFU/TOFU):** Chứa các từ khóa hỏi giá, gói cước, điều kiện, so sánh, thủ tục ("Bảng giá, gói cước, điều kiện, so sánh..."). Đặt trần Max CPC thấp, bảo vệ ngân sách không bị đội chi phí và không cướp ngân sách của nhóm High-CPC.

3. **Triệt tiêu xung đột giá thầu khi dùng Maximize Clicks:**
   - Tuyệt đối cấm để từ khóa CPC rẻ (dưới 10.000 ₫) chạy chung bình ngân sách với từ khóa CPC đắt (trên 30.000 ₫).
   - Trong Maximize Clicks, giới hạn Max CPC và ngân sách ngày chỉ đặt được ở cấp Campaign. Nếu để chung, thuật toán sẽ dồn 100% tiền vào từ khóa rẻ để tối đa số click, làm từ khóa đắt bị 0% hiển thị (hoặc nếu nâng trần thì từ khóa rẻ ngốn sạch tiền trước khi từ khóa đắt kịp đấu giá)."""

if step1_target in content:
    content = content.replace(step1_target, step1_replacement, 1)
    print("STEP 1 updated successfully.")
else:
    print("WARNING: step1_target not found!")

# 2. Update STEP 2 with Max CPC Cap formula
step2_old = """Tuần 1–4  : Maximize Clicks + Max CPC Cap (CPC TB × 120%)
             → Thu thập click data, không ép conv khi chưa có signal"""

step2_new = """Tuần 1–4  : Maximize Clicks + Max CPC Cap theo từng Campaign cách ly:
             - Campaign High-CPC   : Max CPC Cap = CPC TB dải nhóm × 125%
             - Campaign Mid/Low-CPC: Max CPC Cap = CPC TB dải nhóm × 125%
             (Tuyệt đối không dùng 1 mức trần cào bằng cho toàn bộ tài khoản)
             → Thu thập click data, không ép conv khi chưa có signal"""

if step2_old in content:
    content = content.replace(step2_old, step2_new, 1)
    print("STEP 2 updated successfully.")
else:
    print("WARNING: step2_old not found!")

# 3. Update STEP 6 with hard blocker
risk_old = """- `ad_groups_missing_cpc > 0` → BLOCK push — nhắc điền trước
- Lead về nhưng Sale không chốt được hợp đồng ➔ Cần audit quy trình chăm sóc Lead/báo giá"""

risk_new = """- `campaign_cpc_dispersion > 2.0` mà không được tách riêng Campaign ➔ BLOCK KẾ HOẠCH — bắt buộc tách riêng Campaign High-CPC và Campaign Mid/Low-CPC để chống bóp nghẹt hiển thị.
- `ad_groups_missing_cpc > 0` → BLOCK push — nhắc điền trước
- Lead về nhưng Sale không chốt được hợp đồng ➔ Cần audit quy trình chăm sóc Lead/báo giá"""

if risk_old in content:
    content = content.replace(risk_old, risk_new, 1)
    print("STEP 6 updated successfully.")
else:
    print("WARNING: risk_old not found!")

with open(skill_path, "w", encoding="utf-8") as f:
    f.write(content)

print("SKILL.md for 10-google-ads-plan-v2-ggads updated successfully!")
