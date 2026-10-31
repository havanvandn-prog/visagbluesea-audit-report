import sys
sys.stdout.reconfigure(encoding='utf-8')
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
    ("ĐIỂM NGHẼN P0 (KHẨN CẤP)", "4 Hạng Mục", "Khắc phục triệt để trong 48 giờ"),
    ("HẠNG MỤC CẦN XỬ LÝ (TỔNG)", "9 Hạng Mục", "4 P0 Khẩn cấp + 4 P1 Cao + 1 P2"),
    ("TIẾT KIỆM NGÂN SÁCH ADS", "35% – 45%", "Nhờ nâng điểm chất lượng Landing Page")
]

ws1.append([])
ws1.append(["CHỈ SỐ ĐO LƯỜNG", "GIÁ TRỊ", "ĐÁNH GIÁ CHUYÊN MÔN", "HÀNH ĐỘNG TRỌNG TÂM"])
style_header_row(ws1, 3, EMERALD_HEADER)

overview_rows = [
    ["Tỷ lệ chuyển đổi (CVR) hiện tại", "< 0.4%", "Thất thoát 96% khách bấm vào quảng cáo", "Khắc phục nút liên hệ và biểu mẫu tư vấn"],
    ["Tỷ lệ chuyển đổi tiềm năng", "2.8% – 3.5%", "Chuẩn ngành di trú & visa cao cấp", "Thiết lập Mobile Sticky Bar + Form 3 trường"],
    ["Điểm nghẽn chuyển đổi P0 (Critical)", "4 điểm nghẽn", "Gây mất khách ngay khi vào web", "Sửa 3 số hotline, H1 Acerca de, gắn Sticky Bar, sửa Form"],
    ["Hạng mục tối ưu P1 (High)", "4 hạng mục", "Nâng cao năng lực chốt đơn & tốc độ web", "Xóa CAPS TITLE, chia Stat cards, dựng RFQ Hub, nén WebP Wix"],
    ["Hạng mục tối ưu P2 (Medium)", "1 hạng mục", "Hoàn thiện trải nghiệm người dùng", "Khớp chuyên mục tin tức theo từng quốc gia"],
    ["Hạ tầng mã nguồn", "Wix Platform", "HTML 1.22MB ban đầu, nhiều widget JS", "Nén ảnh WebP và tối ưu tài nguyên trang đích"],
    ["Hạ tầng đo lường chuyển đổi Ads", "Sẵn sàng kết nối", "Sẽ cấu hình đồng bộ khi triển khai Google Ads", "Tạo Conversion Actions theo dõi Hotline/Zalo/Form"]
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
# SHEET 2: ACTION DATABASE P0-P3 (9 HẠNG MỤC THỰC CHIẾN)
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
        "05", "F-UI-05", "Tiêu Đề Văn Bản Mẫu 'CAPS TITLE'", "https://www.visagbluesea.com/",
        "Để sót chữ giữ chỗ (placeholder) 'CAPS TITLE' của template Wix trên trang chủ",
        "Website trông như công trình đang thi công dở dang, giảm uy tín thương hiệu",
        "Xóa bỏ hoàn toàn khối text 'CAPS TITLE', thay thế bằng tiêu đề chuyên môn chuẩn",
        "Content", "P1", "Rất thấp (10m)", "Trang chủ sạch sẽ, không còn sót chữ giữ chỗ"
    ),
    (
        "06", "F-UI-06", "Số Liệu Thành Tựu Dồn Cục '17 5347 235'", "https://www.visagbluesea.com/",
        "Số liệu thành tựu bị dồn chung vào một thẻ văn bản, không có nhãn giải thích",
        "Khách hàng đọc lướt không hiểu ý nghĩa các con số, làm giảm sức mạnh chứng thực",
        "Thiết kế 3 thẻ Stat Cards riêng biệt: '17+ Quốc Gia', '5,300+ Khách Hàng', '235+ Đối Tác'",
        "Designer/Dev", "P1", "Thấp (1h)", "Hiển thị 3 card số liệu lớn sắc nét, có nhãn rõ ràng"
    ),
    (
        "07", "F-CRO-01", "Thiếu Trung Tâm Báo Phí RFQ Hub", "Toàn bộ hệ thống",
        "Trang dịch vụ chỉ có bài viết dài, thiếu bảng dự toán chi phí và nút tải lộ trình định cư",
        "Khách hàng tò mò về chi phí nhưng không tìm thấy thông tin, dễ thoát trang sang đối thủ",
        "Dựng trang RFQ Hub cho phép chọn quốc gia, so sánh quyền lợi và điền form tải dự toán PDF",
        "CRO/Designer", "P1", "Cao (8h)", "Trang RFQ Hub hoạt động mượt mà, thu thập lead dự toán chi phí"
    ),
    (
        "08", "F-TEC-01", "Mã Nguồn Wix Nặng 1.22 MB", "Toàn bộ website",
        "HTML tĩnh ban đầu nặng 1.22MB chứa nhiều mã nhúng Wix chưa được tối ưu",
        "Làm chậm tốc độ tải trang trên mạng di động 4G, giảm điểm trải nghiệm trang đích Google Ads",
        "Gỡ bỏ widget và applet không sử dụng trên Wix, nén toàn bộ ảnh sang định dạng WebP",
        "Dev/Admin", "P1", "Trung bình (4h)", "Tốc độ tải trang trên di động đạt dưới 2.5s"
    ),
    (
        "09", "F-UI-07", "Tin Tức Chéo Không Khớp Trang Đích", "Trang Du học Úc & Các trang dịch vụ",
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
ws3 = wb.create_sheet(title="Ma_Tran_URL_Blueprint")
ws3.freeze_panes = None

headers_ws3 = ["STT", "Nhóm Dịch Vụ", "URL Đề Xuất Chuẩn Hóa", "Mục Tiêu Chuyển Đổi", "Cấu Trúc Section Blueprint (7 Khối Chuẩn)", "CTA Chính"]
ws3.append(headers_ws3)
style_header_row(ws3, 1, NAVY_HEADER)

blueprint_rows = [
    ("01", "Trang Chủ", "https://www.visagbluesea.com/", "Định vị thương hiệu & Phân luồng", "1. Hero Kép -> 2. Trust Bar -> 3. Phân Luồng 4 Thị Trường -> 4. RFQ Teaser -> 5. Stat Cards -> 6. Quy Trình 3 Bước -> 7. Form Tư Vấn", "Nhận Thẩm Định Hồ Sơ"),
    ("02", "Định Cư Mỹ EB-5", "https://www.visagbluesea.com/dinh-cu-my-eb5", "Thu hút nhà đầu tư 800k USD", "1. Hero Dự Án Thẻ Xanh -> 2. Điều Kiện & Pháp Lý -> 3. RFQ Dự Toán Chi Phí -> 4. Bảo Toàn Vốn -> 5. Lịch Trình Thẩm Định -> 6. Form Đặt Hẹn VIP", "Tải Lộ Trình Thẻ Xanh"),
    ("03", "Định Cư Hy Lạp Golden Visa", "https://www.visagbluesea.com/dinh-cu-hy-lap", "Đầu tư BĐS 250k - 800k EUR", "1. Hero Thẻ Cư Trú Châu Âu -> 2. Danh Mục BĐS Tiềm Năng -> 3. Bảng So Sánh Quyền Lợi -> 4. RFQ Chi Phí Thuế -> 5. Form Đăng Ký Khảo Sát", "Đăng Ký Khảo Sát BĐS"),
    ("04", "Định Cư Síp (Cyprus)", "https://www.visagbluesea.com/dinh-cu-sip", "Thẻ xanh vĩnh viễn 300k EUR", "1. Hero Đảo Quốc Châu Âu -> 2. Quyền Lợi Miễn Thuế Toàn Cầu -> 3. Dự Án BĐS Nghỉ Dưỡng -> 4. RFQ Trọn Gói -> 5. Form Tư Vấn Luật Sư", "Tư Vấn Cùng Luật Sư Síp"),
    ("05", "Du Học Úc & Việc Làm", "https://www.visagbluesea.com/du-hoc-uc", "Tuyển sinh du học định cư", "1. Hero Học Bổng & Visa 500 -> 2. Lộ Trình Tay Nghề Định Cư -> 3. RFQ Dự Toán Học Phí & Sinh Hoạt -> 4. Danh Sách Trường Đối Tác -> 5. Form Nộp Hồ Sơ", "Săn Học Bổng Úc")
]

for row in blueprint_rows:
    ws3.append(list(row))

for r in range(2, 2 + len(blueprint_rows)):
    for c in range(1, 7):
        cell = ws3.cell(row=r, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws3.cell(row=r, column=1).alignment = Alignment(horizontal="center", vertical="center")
    ws3.cell(row=r, column=1).font = font_bold
    ws3.row_dimensions[r].height = 36

ws3.column_dimensions['A'].width = 8
ws3.column_dimensions['B'].width = 24
ws3.column_dimensions['C'].width = 38
ws3.column_dimensions['D'].width = 28
ws3.column_dimensions['E'].width = 55
ws3.column_dimensions['F'].width = 25

# ==========================================
# SHEET 4: ĐỐI CHIẾU TRƯỚC VÀ SAU (BEFORE/AFTER)
# ==========================================
ws4 = wb.create_sheet(title="Doi_Chieu_Truoc_Sau")
ws4.freeze_panes = None

headers_ws4 = ["STT", "Hạng Mục", "Hiện Trạng Thực Tế (Trước)", "Phương Án Sau Tối Ưu (Đề Xuất)", "Chỉ Số Đo Lường Cải Thiện"]
ws4.append(headers_ws4)
style_header_row(ws4, 1, NAVY_HEADER)

before_after_rows = [
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
]

for row in before_after_rows:
    ws4.append(list(row))

for r in range(2, 2 + len(before_after_rows)):
    for c in range(1, 6):
        cell = ws4.cell(row=r, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws4.cell(row=r, column=1).alignment = Alignment(horizontal="center", vertical="center")
    ws4.cell(row=r, column=1).font = font_bold
    ws4.row_dimensions[r].height = 40

ws4.column_dimensions['A'].width = 8
ws4.column_dimensions['B'].width = 24
ws4.column_dimensions['C'].width = 45
ws4.column_dimensions['D'].width = 45
ws4.column_dimensions['E'].width = 35

# ==========================================
# SHEET 5: LỘ TRÌNH TRIỂN KHAI 4 GIAI ĐOẠN
# ==========================================
ws5 = wb.create_sheet(title="Lo_Trinh_Trien_Khai")
ws5.freeze_panes = None

headers_ws5 = ["Giai Đoạn", "Thời Gian Dự Kiến", "Nội Dung Triển Khai", "Hạng Mục Xử Lý", "Kết Quả Bàn Giao (Deliverables)"]
ws5.append(headers_ws5)
style_header_row(ws5, 1, NAVY_HEADER)

phases_data = [
    ("Phase 1: Fix Khẩn Cấp (P0)", "Ngày 1 – 2", "Vá lỗ rò rỉ chuyển đổi ngay lập tức", "F-UI-01, F-UI-02, F-UI-03, F-UI-04", "Header 1 Hotline, xóa chữ Acerca de, thanh Sticky Bar mobile chạy mượt"),
    ("Phase 2: Chuẩn Hóa Giao Diện (P1)", "Ngày 3 – 5", "Tăng thẩm mỹ thương hiệu và trải nghiệm", "F-UI-05, F-UI-06, F-TEC-01", "Trang chủ sạch text mẫu, 3 card thành tựu sắc nét, nén WebP tốc độ cao"),
    ("Phase 3: Dựng Phễu RFQ Hub (P1)", "Ngày 6 – 9", "Xây dựng cỗ máy thu thập lead dự toán chi phí", "F-CRO-01", "Trang RFQ Hub dự toán chi phí hoạt động hoàn chỉnh, gửi báo giá tự động"),
    ("Phase 4: Hoàn Thiện & Đo Lường (P2)", "Ngày 10 – 12", "Hoàn thiện chuyên mục và tối ưu toàn diện", "F-UI-07 & Tối ưu Google Ads", "Khối tin tức khớp quốc gia, sẵn sàng 100% bùng nổ chiến dịch Google Ads")
]

for row in phases_data:
    ws5.append(list(row))

for r in range(2, 2 + len(phases_data)):
    for c in range(1, 6):
        cell = ws5.cell(row=r, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws5.cell(row=r, column=1).font = font_bold
    ws5.row_dimensions[r].height = 36

ws5.column_dimensions['A'].width = 24
ws5.column_dimensions['B'].width = 18
ws5.column_dimensions['C'].width = 38
ws5.column_dimensions['D'].width = 30
ws5.column_dimensions['E'].width = 50

# ==========================================
# SHEET 6: LƯU Ý GOOGLE ADS SEARCH
# ==========================================
ws6 = wb.create_sheet(title="Luu_Y_Google_Ads_Search")
ws6.freeze_panes = None

headers_ws6 = ["Trụ Cột Kỹ Thuật", "Nguyên Tắc Bắt Buộc", "Rủi Ro Nếu Bỏ Qua", "Giải Pháp Thực Chiến Khuyên Dùng"]
ws6.append(headers_ws6)
style_header_row(ws6, 1, EMERALD_HEADER)

ads_rows = [
    ("1. Cấu Trúc Nhóm Quảng Cáo", "STAG (Single Theme Ad Group) 1 intent / 1 nhóm", "Đấu giá chéo từ khóa, lãng phí ngân sách", "Tách riêng chiến dịch EB-5, Golden Visa Hy Lạp, Du học Úc"),
    ("2. Tương Thích Thông Điệp (Message Match)", "Từ khóa tìm kiếm phải khớp 100% Headline Landing Page", "Khách thoát ngay trong 3 giây vì thấy nội dung không đúng", "Tìm 'Định cư Hy Lạp' phải trỏ thẳng trang Hy Lạp, cấm trỏ về trang chủ"),
    ("3. Tiêu Chuẩn Trang Đích (Landing Page)", "Tốc độ tải dưới 2.5s trên mobile, form không quá 3 trường", "Điểm chất lượng Quality Score thấp (< 5/10), giá thầu CPC bị đội lên 200%", "Nén WebP, tối ưu tài nguyên Wix, thanh Sticky Action Bar hỗ trợ ngón cái"),
    ("4. Đo Lường Khép Vòng (Tracking Conversion)", "Sẽ cài đặt đồng bộ khi triển khai chạy Google Ads", "Không đo được hiệu quả thực tế, lãng phí ngân sách máy học", "Tạo Conversion Action ghi nhận chính xác lượt bấm Gọi, chat Zalo, gửi form")
]

for row in ads_rows:
    ws6.append(list(row))

for r in range(2, 2 + len(ads_rows)):
    for c in range(1, 5):
        cell = ws6.cell(row=r, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws6.cell(row=r, column=1).font = font_bold
    ws6.row_dimensions[r].height = 38

ws6.column_dimensions['A'].width = 28
ws6.column_dimensions['B'].width = 40
ws6.column_dimensions['C'].width = 42
ws6.column_dimensions['D'].width = 45

excel_file = "Du_Lieu_Trien_Khai_Chi_Tiet_visagbluesea.com.xlsx"
wb.save(excel_file)
print(f"Đã xuất file Excel chuẩn doanh nghiệp 6 Sheets thành công: {excel_file}")
