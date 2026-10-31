import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/update_excel_zero_seo.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

old_s4_rows = """before_after_rows = [
    (
        "01", "Khu Vực Đầu Trang (Hero Banner)",
        "3 số hotline rối mắt; chữ 'Call now:' mất số; không có form nhanh; headline bị dồn cục.",
        "1 Hotline chính (0901.830.827) + 1 Zalo; Cụm chuyển đổi kép: Nút nhận thẩm định & Form 3 bước mini.",
        "Tăng 45% tỷ lệ click gọi ngay và điền form trong 5 giây đầu tiên"
    ),
    (
        "02", "Trải Nghiệm Điện Thoại (Mobile)",
        "Không có nút liên hệ cố định chân trang; khách phải lướt lên đầu tìm số; form dài bắt nhập email.",
        "Thanh Mobile Sticky Bar cố định đáy: [Gọi 24/7] + [Chat Zalo]; Form 3 ô chạm ngón tay cái mượt mà.",
        "Giảm 60% tỷ lệ thoát trang di động, tăng 2.5 lần cuộc gọi từ người dùng smartphone"
    ),
    (
        "03", "Trang Chi Tiết EB-5 / Định Cư",
        "Sót chữ Tây Ban Nha 'Acerca de'; nội dung thuần văn bản; thiếu báo giá; không có phễu RFQ.",
        "Tiêu đề chuẩn hóa 100% tiếng Việt; Phễu RFQ Hub tải dự toán chi phí chi tiết kèm lộ trình hồ sơ.",
        "Loại bỏ 100% rủi ro mất niềm tin nhà đầu tư VIP 800k USD"
    )
]"""

new_s4_rows = """before_after_rows = [
    (
        "01", "Khu Vực Đầu Trang (Hero Banner)",
        "3 số hotline rối mắt; cụm nút Zalo/WhatsApp nổi đè lên chữ tiêu đề H1; chữ 'Call now:' mất số; thiếu form nhanh.",
        "1 Hotline chính (0901.830.827) + 1 Zalo; Cụm chuyển đổi kép: Nút nhận thẩm định & Form 3 bước mini.",
        "Tăng 45% tỷ lệ click gọi ngay và điền form trong 5 giây đầu tiên"
    ),
    (
        "02", "Trải Nghiệm Điện Thoại (Mobile)",
        "Không có nút liên hệ cố định chân trang; khách phải lướt lên đầu tìm số; form dài bắt nhập email.",
        "Thanh Mobile Sticky Bar cố định đáy: [Gọi 24/7] + [Chat Zalo]; Form 3 ô chạm ngón tay cái mượt mà.",
        "Giảm 60% tỷ lệ thoát trang di động, tăng 2.5 lần cuộc gọi từ người dùng smartphone"
    ),
    (
        "03", "Trang Chi Tiết EB-5 / Định Cư",
        "Sót chữ Tây Ban Nha 'Acerca de'; nội dung thuần văn bản; thiếu báo giá; không có phễu RFQ.",
        "Tiêu đề chuẩn hóa 100% tiếng Việt; Phễu RFQ Hub tải dự toán chi phí chi tiết kèm lộ trình hồ sơ.",
        "Loại bỏ 100% rủi ro mất niềm tin nhà đầu tư VIP 800k USD"
    ),
    (
        "04", "Biểu Mẫu Tư Vấn (Contact Form)",
        "Tách riêng 2 ô Họ và Tên riêng biệt; bắt buộc nhập Email tạo ma sát tâm lý khi thao tác trên điện thoại.",
        "Rút gọn còn 3 ô: Họ tên, Số điện thoại/Zalo, Nhu cầu quan tâm; cam kết chuyên viên gọi lại sau 15 phút.",
        "Giảm 65% tỷ lệ bỏ dở form, tăng gấp 2 lần lượng lead thu về"
    )
]"""

if old_s4_rows in text:
    text = text.replace(old_s4_rows, new_s4_rows, 1)
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated Sheet 4 in update_excel_zero_seo.py successfully!")
else:
    print("Warning: old_s4_rows not found!")
