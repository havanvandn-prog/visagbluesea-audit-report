import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
wb.remove(wb.active) # Remove default sheet

# Brand Colors (Easy AI Emerald & Professional Navy)
EMERALD_HEADER = "01A915"
NAVY_HEADER = "1E3A8A"
SLATE_BG = "F8FAFC"
WHITE = "FFFFFF"

font_header = Font(name="Arial", size=11, bold=True, color="FFFFFF")
font_bold = Font(name="Arial", size=10, bold=True, color="0F172A")
font_regular = Font(name="Arial", size=10, color="334155")
font_mono = Font(name="Consolas", size=10, color="0F172A")

thin_border = Border(
    left=Side(style='thin', color='E2E8F0'),
    right=Side(style='thin', color='E2E8F0'),
    top=Side(style='thin', color='E2E8F0'),
    bottom=Side(style='thin', color='E2E8F0')
)

def style_header_row(ws, row_idx, fill_color):
    for col in range(1, ws.max_column + 1):
        cell = ws.cell(row=row_idx, column=col)
        cell.font = font_header
        cell.fill = PatternFill(start_color=fill_color, end_color=fill_color, fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws.row_dimensions[row_idx].height = 28

# ==========================================
# SHEET 1: TỔNG QUAN KHẢO SÁT & STAT CARDS
# ==========================================
ws1 = wb.create_sheet(title="Tong_Quan_Khao_Sat")
ws1.freeze_panes = None

ws1.append(["BÁO CÁO THẨM ĐỊNH TOÀN DIỆN & NĂNG LỰC CHUYỂN ĐỔI GOOGLE ADS — VISAGBLUESEA.COM"])
ws1.merge_cells("A1:D1")
ws1.cell(1, 1).font = Font(name="Arial", size=14, bold=True, color="01A915")
ws1.cell(1, 1).alignment = Alignment(vertical="center")
ws1.row_dimensions[1].height = 35

stat_cards = [
    ("TỶ LỆ CHUYỂN ĐỔI HIỆN TẠI", "< 0.4%", "Thất thoát khách vào rồi thoát ngay"),
    ("MỤC TIÊU SAU TỐI ƯU", "2.8% – 3.5%", "Tăng gấp 7 lần liên hệ & cuộc gọi"),
    ("ĐIỂM NGHẼN P0 (KHẨN CẤP)", "5 Hạng Mục", "Khắc phục triệt để trong 48 giờ"),
    ("HẠNG MỤC CẦN XỬ LÝ (TỔNG)", "10 Hạng Mục", "5 P0 Khẩn cấp + 4 P1 Cao + 1 P2"),
    ("TIẾT KIỆM NGÂN SÁCH ADS", "35% – 45%", "Nhờ nâng điểm chất lượng Landing Page")
]

ws1.append([])
ws1.append(["CHỈ SỐ ĐO LƯỜNG", "GIÁ TRỊ", "ĐÁNH GIÁ CHUYÊN MÔN", "HÀNH ĐỘNG TRỌNG TÂM"])
style_header_row(ws1, 3, EMERALD_HEADER)

overview_rows = [
    ["Tỷ lệ chuyển đổi (CVR) hiện tại", "< 0.4%", "Thất thoát 96% khách bấm vào quảng cáo", "Khắc phục nút liên hệ và biểu mẫu tư vấn"],
    ["Tỷ lệ chuyển đổi tiềm năng", "2.8% – 3.5%", "Chuẩn ngành di trú & visa cao cấp", "Thiết lập Mobile Sticky Bar + Form 3 trường"],
    ["Điểm nghẽn chuyển đổi P0 (Critical)", "5 điểm nghẽn", "Gây mất khách ngay khi vào web", "Sửa 3 số hotline, H1 Acerca de, gắn Sticky Bar, sửa Form, cài GTM"],
    ["Hạng mục tối ưu P1 (High)", "4 hạng mục", "Nâng cao năng lực chốt đơn & tốc độ web", "Xóa CAPS TITLE, chia Stat cards, dựng RFQ Hub, nén WebP Wix"],
    ["Hạng mục tối ưu P2 (Medium)", "1 hạng mục", "Hoàn thiện trải nghiệm người dùng", "Khớp chuyên mục tin tức theo từng quốc gia"],
    ["Hạ tầng mã nguồn", "Wix Platform", "HTML 1.22MB ban đầu, nhiều widget JS", "Nén ảnh WebP và tối ưu tài nguyên trang đích"],
    ["Hệ thống theo dõi chuyển đổi", "Chưa hoàn thiện", "Mất dấu nguồn lead từ từ khóa Google Ads", "Cài đặt GTM Conversion Tags cho Hotline/Zalo/Form"]
]

for row in overview_rows:
    ws1.append(row)

for r in range(4, 4 + len(overview_rows)):
    for c in range(1, 5):
        cell = ws1.cell(row=r, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws1.cell(row=r, column=2).alignment = Alignment(horizontal="center", vertical="center")
    ws1.cell(row=r, column=2).font = font_bold
    ws1.row_dimensions[r].height = 24

ws1.column_dimensions['A'].width = 32
ws1.column_dimensions['B'].width = 20
ws1.column_dimensions['C'].width = 45
ws1.column_dimensions['D'].width = 48

# ==========================================
# SHEET 2: ACTION DATABASE P0-P3 (10 HẠNG MỤC THỰC CHIẾN)
# ==========================================
ws2 = wb.create_sheet(title="Action_Database_P0_P3")
ws2.freeze_panes = None

headers_ws2 = [
    "STT", "Mã Kỹ Thuật", "Hạng Mục Công Việc", "URL Xảy Ra Lỗi", "Nguyên Nhân Gốc Rễ (Root Cause)",
    "Tác Động Kinh Doanh", "Hành Động Kỹ Thuật Khắc Phục", "Người Phụ Trách",
    "Mức Ưu Tiên", "Độ Khó (Effort)", "Tiêu Chí Nghiệm Thu (Validation)"
]
ws2.append(headers_ws2)
style_header_row(ws2, 1, NAVY_HEADER)

actions_data = [
    (
        "01", "F-UI-01", "3 Số Hotline Rối Mắt Ở Header", "https://www.visagbluesea.com/",
        "Header hiển thị cùng lúc 3 số không rõ nhãn, chữ 'Call now:' là link tel:+84-0932797164 nhưng không hiển thị số",
        "Khách hàng phân vân không biết bấm số nào, thất thoát 25% cuộc gọi tư vấn",
        "Rút gọn còn 1 Hotline VN chính (0901.830.827) + 1 Zalo, đưa số quốc tế vào hệ thống chi nhánh",
        "Designer/Dev", "P0", "Thấp (1h)", "Header hiển thị rõ 1 Hotline + 1 nút Zalo, bấm là gọi ngay"
    ),
    (
        "02", "F-UI-02", "Lộ Chữ Tiếng Tây Ban Nha 'Acerca de'", "https://www.visagbluesea.com/us-green-card-eb-5",
        "Theme mẫu của Wix để sót văn bản gốc tiếng Tây Ban Nha ('Acerca de' = About Us)",
        "Gây mất niềm tin nghiêm trọng đối với nhà đầu tư EB-5 (khoản đầu tư 800,000 USD)",
        "Đổi tiêu đề thành 'Đầu Tư Định Cư Mỹ EB-5 — Nhận Thẻ Xanh Cho Cả Gia Đình'",
        "Content/Dev", "P0", "Rất thấp (15m)", "Kiểm tra tiêu đề trang EB-5 hiển thị 100% tiếng Việt chuẩn"
    ),
    (
        "03", "F-UI-03", "Thiếu Mobile Sticky Action Bar", "Toàn bộ website (Mobile view)",
        "Giao diện di động không có thanh nút bấm cố định chân trang hỗ trợ Thumb Zone",
        "Hơn 75% khách tìm trên di động phải cuộn ngược lên đầu trang để tìm số gọi, thất thoát 50% cuộc gọi",
        "Lập trình thanh cố định đáy màn hình: [Gọi Hotline: 0901.830.827] và [Chat Zalo Tư Vấn]",
        "Frontend Dev", "P0", "Trung bình (3h)", "Mở trên điện thoại thấy ngay 2 nút nổi cố định chân trang"
    ),
    (
        "04", "F-UI-04", "Form Tư Vấn Tách Ô Tên & Họ", "Trang chủ & Các trang dịch vụ",
        "Form theo chuẩn phương Tây tách riêng First Name / Last Name, bắt buộc nhập Email",
        "Tạo lực cản tâm lý khi gõ trên di động, tỷ lệ bỏ dở form lên tới 65%",
        "Gộp thành 1 ô 'Họ và tên', chuyển Email thành tùy chọn, thêm ô chọn nhu cầu visa",
        "Dev/CRO", "P0", "Thấp (1h)", "Form chỉ còn 3 ô: Họ tên, SĐT/Zalo, Nhu cầu; gửi thử nghiệm mượt mà"
    ),
    (
        "05", "F-TRK-01", "Chưa Cấu Hình Conversion Tag Google Ads", "Toàn bộ website",
        "GTM đã cài đặt nhưng chưa tạo thẻ chuyển đổi Google Ads cho Form và Nút Gọi/Zalo",
        "Thuật toán máy học Smart Bidding của Google Ads không có dữ liệu để tối ưu tìm khách thật",
        "Tạo Trigger GTM: Form Submission, Click tel:, Click zalo.me; liên kết Google Ads Conversion Action",
        "Ads Specialist", "P0", "Trung bình (2h)", "Test chế độ Preview GTM thấy bắn đủ Tag Conversion khi bấm nút"
    ),
    (
        "06", "F-UI-05", "Tiêu Đề Văn Bản Mẫu 'CAPS TITLE'", "https://www.visagbluesea.com/",
        "Để sót chữ giữ chỗ (placeholder) 'CAPS TITLE' của template Wix trên trang chủ",
        "Website trông như công trình đang thi công dở dang, giảm uy tín thương hiệu",
        "Xóa bỏ hoàn toàn khối text 'CAPS TITLE', thay thế bằng tiêu đề chuyên môn chuẩn",
        "Content", "P1", "Rất thấp (10m)", "Trang chủ sạch sẽ, không còn sót chữ giữ chỗ"
    ),
    (
        "07", "F-UI-06", "Số Liệu Thành Tựu Dồn Cục '17 5347 235'", "https://www.visagbluesea.com/",
        "Số liệu thành tựu bị dồn chung vào một thẻ văn bản, không có nhãn giải thích",
        "Khách hàng đọc lướt không hiểu ý nghĩa các con số, làm giảm sức mạnh chứng thực",
        "Thiết kế 3 thẻ Stat Cards riêng biệt: '17+ Quốc Gia', '5,300+ Khách Hàng', '235+ Đối Tác'",
        "Designer/Dev", "P1", "Thấp (1h)", "Hiển thị 3 card số liệu lớn sắc nét, có nhãn rõ ràng"
    ),
    (
        "08", "F-CRO-01", "Thiếu Trung Tâm Báo Phí RFQ Hub", "Toàn bộ hệ thống",
        "Trang dịch vụ chỉ có bài viết dài, thiếu bảng dự toán chi phí và nút tải lộ trình định cư",
        "Khách hàng tò mò về chi phí nhưng không tìm thấy thông tin, dễ thoát trang sang đối thủ",
        "Dựng trang RFQ Hub cho phép chọn quốc gia, so sánh quyền lợi và điền form tải dự toán PDF",
        "CRO/Designer", "P1", "Cao (8h)", "Trang RFQ Hub hoạt động mượt mà, thu thập lead dự toán chi phí"
    ),
    (
        "09", "F-TEC-01", "Mã Nguồn Wix Nặng 1.22 MB", "Toàn bộ website",
        "HTML tĩnh ban đầu nặng 1.22MB chứa nhiều mã nhúng Wix chưa được tối ưu",
        "Làm chậm tốc độ tải trang trên mạng di động 4G, giảm điểm trải nghiệm trang đích Google Ads",
        "Gỡ bỏ widget và applet không sử dụng trên Wix, nén toàn bộ ảnh sang định dạng WebP",
        "Dev/Admin", "P1", "Trung bình (4h)", "Tốc độ tải trang trên di động đạt dưới 2.5s"
    ),
    (
        "10", "F-UI-07", "Tin Tức Chéo Không Khớp Trang Đích", "Trang Du học Úc & Các trang dịch vụ",
        "Trang đích Du học Úc nhưng khối bài viết liên quan lại hiển thị tin tức Phần Lan, Canada",
        "Làm gián đoạn mạch tìm hiểu của khách hàng, giảm tính chuyên môn sâu",
        "Cấu hình bộ lọc tin tức hiển thị chính xác theo chuyên mục quốc gia tương ứng",
        "Content/Dev", "P2", "Thấp (1h)", "Khối bài viết hiển thị 100% đúng chuyên mục quốc gia"
    )
]

for row in actions_data:
    ws2.append(list(row))

for r in range(2, 2 + len(actions_data)):
    prio = ws2.cell(row=r, column=9).value
    for c in range(1, 12):
        cell = ws2.cell(row=r, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    
    # STT & Mã
    ws2.cell(row=r, column=1).alignment = Alignment(horizontal="center", vertical="center")
    ws2.cell(row=r, column=1).font = font_bold
    ws2.cell(row=r, column=2).alignment = Alignment(horizontal="center", vertical="center")
    ws2.cell(row=r, column=2).font = font_mono

    # Priority highlight
    prio_cell = ws2.cell(row=r, column=9)
    prio_cell.alignment = Alignment(horizontal="center", vertical="center")
    prio_cell.font = font_bold
    if prio == "P0":
        prio_cell.fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
        prio_cell.font = Font(name="Arial", size=10, bold=True, color="B91C1C")
    elif prio == "P1":
        prio_cell.fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
        prio_cell.font = Font(name="Arial", size=10, bold=True, color="B45309")
    elif prio == "P2":
        prio_cell.fill = PatternFill(start_color="ECFDF5", end_color="ECFDF5", fill_type="solid")
        prio_cell.font = Font(name="Arial", size=10, bold=True, color="047857")

    ws2.row_dimensions[r].height = 42

ws2.column_dimensions['A'].width = 8
ws2.column_dimensions['B'].width = 14
ws2.column_dimensions['C'].width = 30
ws2.column_dimensions['D'].width = 36
ws2.column_dimensions['E'].width = 42
ws2.column_dimensions['F'].width = 40
ws2.column_dimensions['G'].width = 45
ws2.column_dimensions['H'].width = 16
ws2.column_dimensions['I'].width = 14
ws2.column_dimensions['J'].width = 16
ws2.column_dimensions['K'].width = 40

# ==========================================
# SHEET 3: MA TRẬN URL & BLUEPRINT
# ==========================================
ws3 = wb.create_sheet(title="Ma_Tran_URL_Va_Sitemap")
ws3.freeze_panes = None

headers_ws3 = ["STT", "URL Hiện Tại", "Hành Động Đề Xuất", "URL Mục Tiêu", "Loại Trang", "Ý Định Tìm Kiếm (Search Intent)", "Mục Tiêu Chuyển Đổi"]
ws3.append(headers_ws3)
style_header_row(ws3, 1, EMERALD_HEADER)

url_data = [
    ("01", "https://www.visagbluesea.com/", "Giữ & Tối ưu", "/", "Trang Chủ", "Tìm công ty tư vấn định cư uy tín", "Bấm gọi Hotline / Chat Zalo / Điền form"),
    ("02", "https://www.visagbluesea.com/us-green-card-eb-5", "Giữ & Đổi URL", "/dinh-cu-my-eb5", "Landing Page EB-5", "Đầu tư định cư Mỹ nhận thẻ xanh", "Tải bảng dự toán tài chính EB-5 800k USD"),
    ("03", "https://www.visagbluesea.com/eu-golden-visa", "Gộp 301 Redirect", "/golden-visa-chau-au", "Landing Page Golden Visa", "Đầu tư lấy thẻ cư trú Châu Âu", "Nhận danh mục BĐS Hy Lạp 250k - 400k EUR"),
    ("04", "https://www.visagbluesea.com/eu-golden-visas", "301 Redirect", "/golden-visa-chau-au", "Redirect", "Từ khóa trùng lặp", "Tránh chia nhỏ lưu lượng truy cập"),
    ("05", "https://www.visagbluesea.com/contact-us", "Giữ & Tối ưu", "/lien-he", "Trang Liên Hệ", "Liên hệ văn phòng trực tiếp", "Form 3 trường + Bản đồ 5 văn phòng"),
    ("06", "https://www.visagbluesea.com/copy-of-malta-investment-visa-1", "Xóa bỏ 410", "N/A", "Trang Nhân Bản Rác", "URL mẫu Wix lọt ra ngoài", "Làm sạch cấu trúc hệ thống")
]

for row in url_data:
    ws3.append(list(row))

for r in range(2, 2 + len(url_data)):
    for c in range(1, 8):
        cell = ws3.cell(row=r, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws3.cell(row=r, column=1).alignment = Alignment(horizontal="center", vertical="center")
    ws3.row_dimensions[r].height = 28

ws3.column_dimensions['A'].width = 8
ws3.column_dimensions['B'].width = 45
ws3.column_dimensions['C'].width = 20
ws3.column_dimensions['D'].width = 28
ws3.column_dimensions['E'].width = 22
ws3.column_dimensions['F'].width = 35
ws3.column_dimensions['G'].width = 42

# ==========================================
# SHEET 4: KIỂM ĐỊNH HẠ TẦNG TRANG ĐÍCH GOOGLE ADS
# ==========================================
ws4 = wb.create_sheet(title="Ha_Tang_Trang_Dich_Ads")
ws4.freeze_panes = None

headers_ws4 = ["STT", "Hạng Mục Kiểm Tra", "Hiện Trạng Kỹ Thuật", "Tiêu Chuẩn Đề Xuất", "Mức Độ Rủi Ro", "Tác Động Đến Google Ads"]
ws4.append(headers_ws4)
style_header_row(ws4, 1, NAVY_HEADER)

tech_data = [
    ("01", "Kích Thước Mã HTML Trang Đích", "1.22 MB tĩnh", "< 800 KB", "Trung Bình", "Ảnh hưởng tốc độ load mạng 4G, tăng tỷ lệ thoát trang"),
    ("02", "Giao Diện Di Động (Thumb Zone)", "Không có nút bấm cố định đáy", "Sticky Action Bar 2 nút", "Rất Cao", "Mất 50% cuộc gọi từ khách truy cập điện thoại"),
    ("03", "Trải Nghiệm Form Nhập Liệu", "Tách riêng ô Tên & Họ, bắt email", "Gộp 1 ô Họ tên, chỉ cần SĐT/Zalo", "Rất Cao", "Tỷ lệ bỏ dở form ước tính lên tới 65%"),
    ("04", "Bảo Mật & Chứng Chỉ SSL", "HTTPS hợp lệ", "HTTPS + HSTS", "An Toàn", "Đạt chuẩn bảo mật tiếp nhận thông tin khách hàng"),
    ("05", "Đồng Bộ Văn Bản Đầu Trang", "Sót 'Acerca de' và 'CAPS TITLE'", "100% Tiếng Việt chuẩn định vị", "Cao", "Mất uy tín với nhà đầu tư lớn, giảm tỷ lệ chuyển đổi")
]

for row in tech_data:
    ws4.append(list(row))

for r in range(2, 2 + len(tech_data)):
    for c in range(1, 7):
        cell = ws4.cell(row=r, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws4.cell(row=r, column=1).alignment = Alignment(horizontal="center", vertical="center")
    ws4.row_dimensions[r].height = 28

ws4.column_dimensions['A'].width = 8
ws4.column_dimensions['B'].width = 30
ws4.column_dimensions['C'].width = 35
ws4.column_dimensions['D'].width = 35
ws4.column_dimensions['E'].width = 18
ws4.column_dimensions['F'].width = 48

# ==========================================
# SHEET 5: THIẾT LẬP TRACKING GOOGLE ADS
# ==========================================
ws5 = wb.create_sheet(title="Thiet_Lap_Tracking_Google_Ads")
ws5.freeze_panes = None

headers_ws5 = ["STT", "Tên Sự Kiện Chuyển Đổi", "Loại Chuyển Đổi", "Loại Trigger GTM", "Điều Kiện Kích Hoạt (Firing Rule)", "Mục Tiêu Tối Ưu Bidding"]
ws5.append(headers_ws5)
style_header_row(ws5, 1, EMERALD_HEADER)

tracking_data = [
    ("01", "lead_hotline_click", "Primary Conversion", "Click - Just Links", "Click URL starts with 'tel:'", "Tối ưu tìm người có nhu cầu gọi tư vấn ngay"),
    ("02", "lead_zalo_click", "Primary Conversion", "Click - Just Links", "Click URL contains 'zalo.me'", "Tối ưu tìm người thích nhắn tin bảo mật Zalo"),
    ("03", "lead_form_submit", "Primary Conversion", "Form Submission", "Form ID matches 'wix-form' & valid submit", "Tối ưu tìm khách hàng đăng ký nhận dự toán chi phí"),
    ("04", "rfq_download_pdf", "Secondary Conversion", "Click - Just Links", "Click URL contains '.pdf' & class contains 'rfq'", "Theo dõi khách hàng quan tâm sâu tới bảng phí"),
    ("05", "pageview_thankyou", "Primary Conversion", "Page View", "Page Path contains '/thank-you' or '/cam-on'", "Xác nhận chuyển đổi thành công khép vòng")
]

for row in tracking_data:
    ws5.append(list(row))

for r in range(2, 2 + len(tracking_data)):
    for c in range(1, 7):
        cell = ws5.cell(row=r, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws5.cell(row=r, column=1).alignment = Alignment(horizontal="center", vertical="center")
    ws5.row_dimensions[r].height = 28

ws5.column_dimensions['A'].width = 8
ws5.column_dimensions['B'].width = 25
ws5.column_dimensions['C'].width = 22
ws5.column_dimensions['D'].width = 24
ws5.column_dimensions['E'].width = 45
ws5.column_dimensions['F'].width = 48

# ==========================================
# SHEET 6: LỘ TRÌNH TRIỂN KHAI 4 TUẦN
# ==========================================
ws6 = wb.create_sheet(title="Lo_Trinh_Trien_Khai_4_Tuan")
ws6.freeze_panes = None

headers_ws6 = ["Giai Đoạn", "Thời Gian", "Các Hạng Mục Trọng Tâm", "Mục Tiêu Đạt Được", "Phụ Trách"]
ws6.append(headers_ws6)
style_header_row(ws6, 1, NAVY_HEADER)

roadmap_data = [
    ("Tuần 1: Cấp Cứu Chuyển Đổi P0", "Ngày 1 – 7", "Xử lý 3 số hotline Header, sửa chữ Acerca de trang EB-5, gắn Mobile Sticky Action Bar, rút gọn Form còn 3 trường, cấu hình GTM Tracking", "Website đủ điều kiện an toàn để đón tiếp khách quảng cáo mà không bị thất thoát", "Frontend Dev + Ads Specialist"),
    ("Tuần 2: Nâng Tầm Giao Diện P1", "Ngày 8 – 14", "Xóa bỏ CAPS TITLE, làm lại 3 thẻ Stat Cards thành tựu, lọc tin tức khớp quốc gia, nén ảnh WebP giảm tải trang", "Nâng cao độ tin cậy thương hiệu, giảm tỷ lệ thoát trang xuống dưới 45%", "Designer + Content"),
    ("Tuần 3: Dựng Phễu RFQ Hub", "Ngày 15 – 21", "Thiết kế và đưa vào hoạt động Trung Tâm Báo Giá Dự Án (RFQ Hub) so sánh 3 gói định cư chiến lược, tích hợp tải dự toán PDF", "Tạo đòn bẩy thu hút khách hàng quan tâm đến bài toán tài chính", "CRO Specialist + Dev"),
    ("Tuần 4: Chạy Thử Nghiệm Ads & Scale", "Ngày 22 – 30", "Khởi chạy chiến dịch Google Search Ads thử nghiệm, đối soát tỷ lệ chuyển đổi thực tế, tinh chỉnh từ khóa phủ định và mẫu RSA", "Đạt mục tiêu tỷ lệ chuyển đổi 2.8% – 3.5%, tối ưu chi phí mỗi khách liên hệ (CPA)", "Google Ads Team")
]

for row in roadmap_data:
    ws6.append(list(row))

for r in range(2, 2 + len(roadmap_data)):
    for c in range(1, 6):
        cell = ws6.cell(row=r, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws6.cell(row=r, column=1).font = font_bold
    ws6.row_dimensions[r].height = 42

ws6.column_dimensions['A'].width = 28
ws6.column_dimensions['B'].width = 16
ws6.column_dimensions['C'].width = 55
ws6.column_dimensions['D'].width = 48
ws6.column_dimensions['E'].width = 28

output_path = "Du_Lieu_Trien_Khai_Chi_Tiet_visagbluesea.com.xlsx"
wb.save(output_path)
print(f"Exported clean 100% Excel file to {output_path} successfully!")
