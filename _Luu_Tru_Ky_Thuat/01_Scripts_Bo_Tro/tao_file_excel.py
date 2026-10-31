import os
import sys
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.Workbook()
# remove default sheet
wb.remove(wb.active)

# Color palettes
NAVY_HEADER = "1E3A8A"
EMERALD_HEADER = "065F46"
AMBER_HEADER = "D97706"
GRAY_HEADER = "334155"
WHITE = "FFFFFF"
LIGHT_BLUE = "EFF6FF"
LIGHT_GREEN = "ECFDF5"
LIGHT_RED = "FEF2F2"
LIGHT_YELLOW = "FEFCE8"

font_title = Font(name="Calibri", size=15, bold=True, color="1E3A8A")
font_subtitle = Font(name="Calibri", size=11, italic=True, color="475569")
font_stat_num = Font(name="Calibri", size=18, bold=True, color="065F46")
font_stat_label = Font(name="Calibri", size=10, bold=True, color="64748B")
font_header = Font(name="Calibri", size=11, bold=True, color=WHITE)
font_bold = Font(name="Calibri", size=11, bold=True)
font_regular = Font(name="Calibri", size=11)
font_red_bold = Font(name="Calibri", size=11, bold=True, color="DC2626")
font_amber_bold = Font(name="Calibri", size=11, bold=True, color="D97706")
font_green_bold = Font(name="Calibri", size=11, bold=True, color="059669")

thin_border = Border(
    left=Side(style='thin', color='CBD5E1'),
    right=Side(style='thin', color='CBD5E1'),
    top=Side(style='thin', color='CBD5E1'),
    bottom=Side(style='thin', color='CBD5E1')
)

def style_header_row(ws, row_idx, bg_color=NAVY_HEADER):
    fill = PatternFill(start_color=bg_color, end_color=bg_color, fill_type="solid")
    for cell in ws[row_idx]:
        cell.font = font_header
        cell.fill = fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
    ws.row_dimensions[row_idx].height = 28

# ==========================================
# SHEET 1: TỔNG QUAN KHẢO SÁT
# ==========================================
ws1 = wb.create_sheet(title="Tong_Quan_Khao_Sat")
ws1.freeze_panes = None

ws1.append(["BÁO CÁO THẨM ĐỊNH NĂNG LỰC CHUYỂN ĐỔI WEBSITE — VISAGBLUESEA.COM"])
ws1.append(["Đánh giá độ sẵn sàng tiếp nhận quảng cáo Google Ads & Tối ưu tỷ lệ chuyển đổi (CRO)"])
ws1.append([])

ws1.merge_cells("A1:G1")
ws1.merge_cells("A2:G2")
ws1["A1"].font = font_title
ws1["A2"].font = font_subtitle

# Executive Stat Cards in rows 4-6
stat_cards = [
    ("TỶ LỆ CHUYỂN ĐỔI HIỆN TẠI", "< 0.4%", "Nhiều điểm nghẽn cản trở liên hệ"),
    ("MỤC TIÊU SAU TỐI ƯU", "2.8% – 3.5%", "Tăng gấp 6-8 lần lượng khách gọi/zalo"),
    ("LỖI NGHIÊM TRỌNG (P0)", "6 Hạng Mục", "Cần khắc phục ngay trong 48h"),
    ("LỖI MỨC ĐỘ CAO (P1)", "5 Hạng Mục", "Xử lý trong tuần đầu tiên"),
    ("TIẾT KIỆM NGÂN SÁCH ADS", "30% – 45%", "Nhờ nâng điểm chất lượng Landing Page")
]

ws1.append(["CHỈ SỐ ĐO LƯỜNG", "GIÁ TRỊ", "ĐÁNH GIÁ CHUYÊN MÔN", "HÀNH ĐỘNG TRỌNG TÂM"])
style_header_row(ws1, 4, EMERALD_HEADER)

ws1.append(["Tỷ lệ chuyển đổi (CVR) hiện tại", "< 0.4%", "Thất thoát 96% khách bấm vào quảng cáo", "Khắc phục nút liên hệ và biểu mẫu"])
ws1.append(["Tỷ lệ chuyển đổi tiềm năng", "2.8% – 3.5%", "Chuẩn ngành di trú & visa cao cấp", "Thiết lập Mobile Sticky Bar + Form 3 trường"])
ws1.append(["Lỗi chặn chuyển đổi P0 (Critical)", "6 lỗi", "Gây mất khách ngay khi vào web", "Sửa lỗi H1 Acerca de, CAPS TITLE, 3 số hotline"])
ws1.append(["Lỗi kỹ thuật & SEO P1 (High)", "5 lỗi", "Sụt giảm điểm chất lượng Google Ads", "Xóa URL clone, tối ưu sitemap, bổ sung H1"])
ws1.append(["Hạ tầng mã nguồn", "Wix Platform", "HTML 1.22MB ban đầu, nhiều JS nặng", "Tối ưu hóa tài nguyên và cấu hình tracking"])
ws1.append(["Hệ thống theo dõi chuyển đổi", "Chưa hoàn thiện", "Mất dấu nguồn lead từ từ khóa Google Ads", "Cài đặt GTM Conversion Tags cho Hotline/Zalo/Form"])

for r in range(5, 11):
    for c in range(1, 5):
        cell = ws1.cell(row=r, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws1.cell(row=r, column=2).alignment = Alignment(horizontal="center", vertical="center")
    ws1.cell(row=r, column=2).font = font_bold
    ws1.row_dimensions[r].height = 24

ws1.column_dimensions['A'].width = 30
ws1.column_dimensions['B'].width = 18
ws1.column_dimensions['C'].width = 45
ws1.column_dimensions['D'].width = 45

# ==========================================
# SHEET 2: ACTION DATABASE P0-P3
# ==========================================
ws2 = wb.create_sheet(title="Action_Database_P0_P3")
ws2.freeze_panes = None

headers_ws2 = [
    "Mã Finding", "Hạng Mục", "URL Xảy Ra Lỗi", "Nguyên Nhân Gốc Rễ (Root Cause)",
    "Tác Động Kinh Doanh", "Hành Động Kỹ Thuật Khắc Phục", "Người Phụ Trách",
    "Mức Ưu Tiên", "Độ Khó (Effort)", "Tiêu Chí Nghiệm Thu (Validation)"
]
ws2.append(headers_ws2)
style_header_row(ws2, 1, NAVY_HEADER)

actions_data = [
    (
        "F-UI-01", "3 Số Hotline Rối Mắt Ở Header", "https://www.visagbluesea.com/",
        "Header hiển thị cùng lúc 3 số không rõ nhãn, chữ 'Call now:' là link tel:+84-0932797164 nhưng không hiển thị số",
        "Khách hàng phân vân không biết bấm số nào, giảm tỷ lệ gọi trực tiếp",
        "Rút gọn còn 1 Hotline VN chính (0901.830.827) + 1 Zalo, đưa số quốc tế vào menu hệ thống chi nhánh",
        "Designer/Dev", "P0", "Thấp (1h)", "Header hiển thị rõ 1 Hotline + 1 nút Zalo, bấm là gọi ngay"
    ),
    (
        "F-UI-02", "Lộ Chữ Tiếng Tây Ban Nha 'Acerca de'", "https://www.visagbluesea.com/us-green-card-eb-5",
        "Theme mẫu của Wix để sót văn bản gốc tiếng Tây Ban Nha ('Acerca de' = About Us)",
        "Gây mất niềm tin nghiêm trọng đối với nhà đầu tư EB-5 (khoản đầu tư 800,000 USD)",
        "Đổi thẻ H1 thành 'Đầu Tư Định Cư Mỹ EB-5 — Nhận Thẻ Xanh Cho Cả Gia Đình'",
        "Content/Dev", "P0", "Rất thấp (15m)", "Kiểm tra thẻ H1 trang EB-5 hiển thị 100% tiếng Việt chuẩn"
    ),
    (
        "F-UI-03", "Thiếu Mobile Sticky Action Bar", "Toàn bộ website (Mobile view)",
        "Giao diện di động không có thanh nút bấm cố định chân trang hỗ trợ Thumb Zone",
        "Hơn 75% khách tìm trên di động phải cuộn ngược lên đầu trang để tìm số gọi, thất thoát 50% lead",
        "Lập trình thanh cố định đáy màn hình: [Gọi Hotline: 0901.830.827] và [Chat Zalo Tư Vấn]",
        "Frontend Dev", "P0", "Trung bình (3h)", "Mở trên điện thoại thấy ngay 2 nút nổi cố định chân trang"
    ),
    (
        "F-UI-04", "Form Tư Vấn Tách Ô Tên & Họ", "Trang chủ & Các trang dịch vụ",
        "Form theo chuẩn phương Tây tách riêng First Name / Last Name, bắt buộc nhập Email",
        "Tạo lực cản tâm lý khi gõ trên di động, tỷ lệ bỏ ngang form lên tới 65%",
        "Gộp thành 1 ô 'Họ và tên', chuyển Email thành tùy chọn, thêm ô chọn nhu cầu visa",
        "Dev/CRO", "P0", "Thấp (1h)", "Form chỉ còn 3 ô: Họ tên, SĐT/Zalo, Nhu cầu; gửi thử nghiệm mượt mà"
    ),
    (
        "F-SEO-01", "Trang Con Golden Visa Khuyết H1", "https://www.visagbluesea.com/eu-golden-visa",
        "Trang đích hoàn toàn không có thẻ tiêu đề H1 trong mã nguồn",
        "Google Ads phạt điểm chất lượng trang đích vì thiếu từ khóa cốt lõi, giá click CPC tăng cao",
        "Bổ sung thẻ H1: 'Chương Trình Golden Visa Châu Âu: Định Cư Hy Lạp & Síp 2026'",
        "SEO/Dev", "P0", "Rất thấp (15m)", "Dùng extension Detailed SEO kiểm tra thấy H1=1 chuẩn xác"
    ),
    (
        "F-TRK-01", "Chưa Cấu Hình Conversion Tag Google Ads", "Toàn bộ website",
        "GTM đã cài đặt nhưng chưa tạo thẻ chuyển đổi Google Ads cho Form và Nút Gọi/Zalo",
        "Thuật toán máy học Smart Bidding của Google Ads không có dữ liệu để tối ưu tìm khách thật",
        "Tạo Trigger GTM: Form Submission, Click tel:, Click zalo.me; liên kết Google Ads Conversion Action",
        "Ads Specialist", "P0", "Trung bình (2h)", "Test chế độ Preview GTM thấy bắn đủ Tag Conversion khi bấm nút"
    ),
    (
        "F-UI-05", "Tiêu Đề Văn Bản Mẫu 'CAPS TITLE'", "https://www.visagbluesea.com/",
        "Để sót chữ giữ chỗ (placeholder) 'CAPS TITLE' của template Wix trên trang chủ",
        "Website trông như công trình đang thi công dở dang, giảm uy tín thương hiệu",
        "Xóa bỏ hoàn toàn khối text 'CAPS TITLE' hoặc thay bằng tiêu đề tin tức chuyên môn",
        "Content/Dev", "P1", "Rất thấp (10m)", "Rà soát toàn bộ trang chủ không còn bất kỳ chữ mẫu tiếng Anh nào"
    ),
    (
        "F-UI-06", "Số Liệu Thành Tựu Dồn Cục '17 5347 235'", "https://www.visagbluesea.com/",
        "Các con số thành tựu bị dồn cục vào 1 thẻ H2 không có định dạng",
        "Khách hàng đọc lướt không hiểu ý nghĩa của các con số",
        "Thiết kế lại 3 thẻ Executive Stat Cards: 17+ Quốc gia, 5,300+ Khách hàng, 15+ Năm kinh nghiệm",
        "Designer/Dev", "P1", "Thấp (1.5h)", "Hiển thị 3 card số liệu lớn, có biểu tượng và nhãn giải thích rõ ràng"
    ),
    (
        "F-SEO-02", "Trang Nhân Bản Rác Lọt Vào Sitemap", "https://www.visagbluesea.com/copy-of-malta-investment-visa-1",
        "Thao tác clone trang trong Wix tạo URL /copy-of-... và bị Googlebot lập chỉ mục",
        "Tự cạnh tranh từ khóa (Cannibalization), làm loãng độ uy tín của website",
        "Chuyển hướng 301 Redirect trang rác về trang chính thức /malta-investment-visa hoặc xóa bỏ",
        "SEO Specialist", "P1", "Rất thấp (15m)", "Kiểm tra mã trạng thái HTTP trả về 301 chuyển hướng đúng trang"
    ),
    (
        "F-CRO-01", "Thiếu Trung Tâm Báo Phí RFQ Hub", "Toàn bộ website",
        "Các trang chi tiết chỉ chứa văn bản dài dòng, thiếu bảng so sánh quyền lợi và mức đầu tư",
        "Khách hàng không nắm được bài toán tài chính, thoát trang để so sánh bên khác",
        "Xây dựng Section/Trang RFQ Hub so sánh 3 gói di trú (Mỹ, Síp, Hy Lạp) kèm nút nhận bảng dự toán PDF",
        "CRO/Designer", "P1", "Cao (8h)", "Có bảng so sánh đa cột, khách điền 3 thông tin để tải file PDF"
    ),
    (
        "F-TEC-01", "Mã Nguồn HTML Nặng 1.22 MB Trên Wix", "Toàn bộ website",
        "Nền tảng Wix sinh ra mã HTML ban đầu hơn 1.2MB do nhúng inline style và script thừa",
        "Tiệm cận ngưỡng 2MB giới hạn cào của Googlebot, tốc độ tải trên mạng di động 4G bị chậm",
        "Tối ưu lại cấu trúc trang, tắt các widget Wix không sử dụng, nén toàn bộ ảnh sang định dạng WebP",
        "Dev/Technical", "P1", "Trung bình (4h)", "Kiểm tra dung lượng HTML giảm xuống dưới 800KB, TTFB < 0.8s"
    ),
    (
        "F-SEO-03", "Trang Chủ Bị Gán 2 Thẻ H1", "https://www.visagbluesea.com/",
        "Một đoạn văn bản dài 4 dòng bị gán nhầm thẻ H1 thứ hai bên cạnh H1 'Các dịch vụ nổi bật'",
        "Google bị rối loạn trọng tâm từ khóa chính của trang chủ",
        "Đổi đoạn văn bản thành thẻ `<p>`, gộp H1 thành duy nhất 1 câu định vị thương hiệu mạnh mẽ",
        "SEO Specialist", "P2", "Rất thấp (15m)", "Kiểm tra extension Detailed SEO báo H1=1 duy nhất"
    ),
    (
        "F-SEO-04", "Thiếu Schema Doanh Nghiệp & Dịch Vụ", "Toàn bộ website",
        "Website chỉ có 2 thẻ WebSite schema cơ bản, thiếu LocalBusiness, Organization, Service",
        "Mất cơ hội hiển thị thông tin thực thể doanh nghiệp nổi bật trên kết quả tìm kiếm Google",
        "Bổ sung cấu trúc JSON-LD: LegalService / EducationalOrganization, thông tin NAP 5 văn phòng",
        "SEO Specialist", "P2", "Thấp (2h)", "Test bằng công cụ Rich Results Test của Google đạt 100% hợp lệ"
    ),
    (
        "F-UI-07", "Tin Tức Chéo Không Khớp Trang Đích", "https://www.visagbluesea.com/study-in-australia",
        "Trang Du học Úc nhưng khối tin tức phía dưới lại hiện bài về Phần Lan, Canada, SAT Mỹ",
        "Phụ huynh tìm hiểu du học Úc bị phân tâm bởi các thông tin không liên quan",
        "Cấu hình bộ lọc bài viết tự động theo chuyên mục: Trang Úc chỉ hiển thị tin tức về Úc",
        "Content/Dev", "P2", "Thấp (1h)", "Khối tin tức hiển thị chính xác các bài viết về chính sách visa Úc"
    )
]

for idx, act in enumerate(actions_data, 2):
    ws2.append(act)
    for c in range(1, 11):
        cell = ws2.cell(row=idx, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    # Color badge for Priority
    p_cell = ws2.cell(row=idx, column=8)
    p_cell.alignment = Alignment(horizontal="center", vertical="center")
    if "P0" in act[7]:
        p_cell.font = font_red_bold
        p_cell.fill = PatternFill(start_color=LIGHT_RED, end_color=LIGHT_RED, fill_type="solid")
    elif "P1" in act[7]:
        p_cell.font = font_amber_bold
        p_cell.fill = PatternFill(start_color=LIGHT_YELLOW, end_color=LIGHT_YELLOW, fill_type="solid")
    else:
        p_cell.font = font_green_bold
        p_cell.fill = PatternFill(start_color=LIGHT_GREEN, end_color=LIGHT_GREEN, fill_type="solid")
    ws2.row_dimensions[idx].height = 42

ws2.column_dimensions['A'].width = 14
ws2.column_dimensions['B'].width = 28
ws2.column_dimensions['C'].width = 38
ws2.column_dimensions['D'].width = 45
ws2.column_dimensions['E'].width = 40
ws2.column_dimensions['F'].width = 50
ws2.column_dimensions['G'].width = 16
ws2.column_dimensions['H'].width = 14
ws2.column_dimensions['I'].width = 16
ws2.column_dimensions['J'].width = 45

# ==========================================
# SHEET 3: MA TRẬN URL & SITEMAP
# ==========================================
ws3 = wb.create_sheet(title="Ma_Tran_URL_Va_Sitemap")
ws3.freeze_panes = None

headers_ws3 = [
    "STT", "URL Hiện Tại", "Loại Trang", "Hành Động Đề Xuất",
    "URL Mục Tiêu Đề Xuất", "Ý Định Tìm Kiếm (Search Intent)", "Mục Tiêu Chuyển Đổi (CRO Goal)"
]
ws3.append(headers_ws3)
style_header_row(ws3, 1, AMBER_HEADER)

url_matrix = [
    (1, "https://www.visagbluesea.com/", "Trang Chủ", "Tối ưu giao diện & H1", "https://www.visagbluesea.com/", "Thương hiệu & Khám phá dịch vụ", "Chuyển đổi Hotline / Thẩm định hồ sơ"),
    (2, "/us-green-card-eb-5", "Landing Page", "Sửa lỗi H1 Acerca de, nâng cấp CRO", "/dinh-cu-my-eb5", "Tìm hiểu đầu tư định cư Mỹ nhận thẻ xanh", "Điền form thẩm định tài chính đầu tư"),
    (3, "/eu-golden-visa", "Landing Page", "Thêm H1, dựng bảng so sánh Síp vs Hy Lạp", "/golden-visa-chau-au", "Định cư Châu Âu diện mua bất động sản", "Nhận cẩm nang so sánh thuế & thẻ xanh"),
    (4, "/golden-visa-greece", "Trang phụ", "Gộp 301 về trang chi tiết Hy Lạp chuẩn", "/golden-visa-hy-lap", "Định cư Hy Lạp 250k-400k EUR", "Tải danh mục dự án BĐS Hy Lạp"),
    (5, "/greece-investment-visa", "Trang trùng lặp", "301 Redirect về /golden-visa-hy-lap", "/golden-visa-hy-lap", "Tránh trùng lặp từ khóa (Cannibalization)", "Dồn tín hiệu SEO về 1 URL duy nhất"),
    (6, "/study-in-australia", "Landing Page", "Lọc tin tức chuẩn Úc, thêm form học bổng", "/du-hoc-uc", "Tìm kiếm trường & học bổng du học Úc", "Đăng ký tư vấn chọn trường & học bổng"),
    (7, "/copy-of-malta-investment-visa-1", "Trang clone rác", "Xóa bỏ hoặc 301 Redirect về /malta", "/dinh-cu-malta", "Triệt tiêu rác sitemap", "Bảo vệ độ uy tín tên miền"),
    (8, "/contact-us", "Trang Liên Hệ", "Gom 4 form thành 1 form chuẩn", "/lien-he", "Khách hàng muốn kết nối ngay", "Gọi điện thoại / Chat Zalo / Đặt lịch hẹn"),
    (9, "MỚI: /trung-tam-bao-gia-rfq", "RFQ Hub", "Tạo mới trang trung tâm báo giá B2B", "/bang-gia-dinh-cu-visa", "Tra cứu chi phí trọn gói & lộ trình", "Điền 3 bước nhận bản dự toán PDF")
]

for idx, u in enumerate(url_matrix, 2):
    ws3.append(list(u))
    for c in range(1, 8):
        cell = ws3.cell(row=idx, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws3.cell(row=idx, column=1).alignment = Alignment(horizontal="center", vertical="center")
    ws3.row_dimensions[idx].height = 26

ws3.column_dimensions['A'].width = 10
ws3.column_dimensions['B'].width = 35
ws3.column_dimensions['C'].width = 18
ws3.column_dimensions['D'].width = 35
ws3.column_dimensions['E'].width = 30
ws3.column_dimensions['F'].width = 38
ws3.column_dimensions['G'].width = 40

# ==========================================
# SHEET 4: KIỂM ĐỊNH KỸ THUẬT & SEO
# ==========================================
ws4 = wb.create_sheet(title="Kiem_Dinh_SEO_Technical")
ws4.freeze_panes = None

headers_ws4 = ["Tiêu Chí Kỹ Thuật", "Hiện Trạng visagbluesea.com", "Tiêu Chuẩn 2026", "Đánh Giá", "Khuyến Nghị Kỹ Thuật"]
ws4.append(headers_ws4)
style_header_row(ws4, 1, GRAY_HEADER)

tech_checks = [
    ("Googlebot Fetch Limit", "HTML 1.22 MB tĩnh từ Wix", "< 2.0 MB HTML uncompressed", "Cảnh Báo Vàng", "Đã chiếm 61% hạn mức Googlebot. Cần lược bỏ CSS inline thừa của Wix."),
    ("Cấu Trúc Thẻ H1", "Trang chủ: 2 H1; EB-5: 'Acerca de'; Golden Visa: 0 H1", "Mỗi URL có duy nhất 1 H1 chứa từ khóa", "Lỗi Đỏ (Critical)", "Quy chuẩn lại 100% thẻ H1 đồng bộ với chiến dịch quảng cáo."),
    ("Title & Meta Description", "Title 25 ký tự (ngắn); Meta 248 ký tự (bị cắt)", "Title 50-60 ký tự; Meta 150-160 ký tự", "Cảnh Báo Vàng", "Viết lại Title & Description chuẩn định vị dịch vụ và thương hiệu."),
    ("Cấu Trúc Schema.org", "Chỉ có 2 thẻ WebSite cơ bản", "Bắt buộc có Organization, LegalService, FAQ", "Lỗi Đỏ (Thiếu)", "Bổ sung mã JSON-LD chuẩn cho tổ chức tư vấn di trú quốc tế."),
    ("Điều Phối AI Bot (robots.txt)", "Mở chung, chặn AdsBot trên thư mục partials", "Mở OAI-SearchBot, PerplexityBot; Chặn training bot nếu cần", "Đạt Chuẩn Cơ Bản", "Cần giữ mở các bot tìm kiếm AI để xuất hiện trên ChatGPT/Perplexity."),
    ("Responsive & Mobile View", "Chưa có Sticky Bar, form khó gõ ngón cái", "Tối ưu chuẩn Thumb Zone, nút bấm >= 44x44px", "Lỗi Đỏ (Trải nghiệm tệ)", "Bổ sung thanh điều hướng đáy màn hình gồm 2 nút Gọi và Zalo."),
    ("Dung Lượng Ảnh & Định Dạng", "Một số ảnh banner tải chậm trên 4G", "100% ảnh chuyển sang WebP, nén tối ưu", "Cần Tối Ưu", "Dùng công cụ nén ảnh WebP toàn diện giảm tải 70% băng thông.")
]

for idx, t in enumerate(tech_checks, 2):
    ws4.append(list(t))
    for c in range(1, 6):
        cell = ws4.cell(row=idx, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws4.row_dimensions[idx].height = 28

ws4.column_dimensions['A'].width = 25
ws4.column_dimensions['B'].width = 40
ws4.column_dimensions['C'].width = 30
ws4.column_dimensions['D'].width = 20
ws4.column_dimensions['E'].width = 50

# ==========================================
# SHEET 5: THIẾT LẬP TRACKING GOOGLE ADS
# ==========================================
ws5 = wb.create_sheet(title="Thiet_Lap_Tracking_Google_Ads")
ws5.freeze_panes = None

headers_ws5 = ["Sự Kiện Chuyển Đổi (Conversion Action)", "Loại Chuyển Đổi", "Điều Kiện Kích Hoạt (Trigger GTM)", "Giá Trị Chuyển Đổi Quy Ước", "Mục Đích Tối Ưu Ads"]
ws5.append(headers_ws5)
style_header_row(ws5, 1, EMERALD_HEADER)

tracking_plan = [
    ("Submit_Form_Tu_Van", "Chuyển Đổi Chính (Primary)", "Gửi thành công form 3 trường (Form Submission Event)", "500,000 VNĐ", "Tối ưu hóa giá thầu Smart Bidding (Target CPA / Max Conversions)"),
    ("Click_To_Call_Hotline", "Chuyển Đổi Chính (Primary)", "Nhấp liên kết tel:0901830827", "400,000 VNĐ", "Bắt trọn khách hàng có nhu cầu khẩn cấp gọi trực tiếp trên điện thoại"),
    ("Click_To_Chat_Zalo", "Chuyển Đổi Chính (Primary)", "Nhấp liên kết zalo.me/0901830827", "350,000 VNĐ", "Đo lường lượng khách hàng nhắn tin tư vấn trực tiếp qua Zalo"),
    ("Download_Tai_Lieu_EB5_PDF", "Chuyển Đổi Phụ (Secondary)", "Tải cẩm nang định cư / dự toán chi phí PDF", "100,000 VNĐ", "Đo lường tệp khách hàng tiềm năng giai đoạn nhận thức (TOFU)"),
    ("Scroll_75_Percent_Landing", "Chuyển Đổi Phụ (Micro)", "Cuộn trang đạt 75% độ dài Landing Page", "0 VNĐ (Theo dõi)", "Đánh giá chất lượng nội dung trang đích và độ gắn kết của người dùng")
]

for idx, tr in enumerate(tracking_plan, 2):
    ws5.append(list(tr))
    for c in range(1, 6):
        cell = ws5.cell(row=idx, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws5.row_dimensions[idx].height = 28

ws5.column_dimensions['A'].width = 30
ws5.column_dimensions['B'].width = 25
ws5.column_dimensions['C'].width = 45
ws5.column_dimensions['D'].width = 25
ws5.column_dimensions['E'].width = 50

# ==========================================
# SHEET 6: LỘ TRÌNH TRIỂN KHAI 4 TUẦN
# ==========================================
ws6 = wb.create_sheet(title="Lo_Trinh_Trien_Khai_4_Tuan")
ws6.freeze_panes = None

headers_ws6 = ["Giai Đoạn", "Thời Gian", "Nội Dung Công Việc Trọng Tâm", "Sản Phẩm Đầu Ra", "Trạng Thái"]
ws6.append(headers_ws6)
style_header_row(ws6, 1, NAVY_HEADER)

roadmap = [
    ("Tuần 1: Dọn Rác & Gắn Tracking", "Ngày 1 – Ngày 7", "Xóa bỏ lỗi H1 'Acerca de', 'CAPS TITLE', chuẩn hóa 1 Hotline + Zalo Header. Cài đặt toàn bộ GTM Tag Google Ads.", "Website sạch lỗi hiển thị, sẵn sàng đo lường chuyển đổi", "Sẵn Sàng Triển Khai"),
    ("Tuần 2: Nâng Cấp Mobile & Form", "Ngày 8 – Ngày 14", "Lập trình thanh Mobile Sticky Bar 2 nút Gọi/Zalo. Thiết kế lại Form tư vấn 3 trường tinh gọn có cam kết bảo mật.", "Trải nghiệm trên smartphone mượt mà, tỷ lệ bỏ form giảm 50%", "Sẵn Sàng Triển Khai"),
    ("Tuần 3: Dựng RFQ Hub & Landing Đích", "Ngày 15 – Ngày 21", "Hoàn thiện trang so sánh đầu tư định cư RFQ Hub. Tối ưu trang đích EB-5 Mỹ và Golden Visa Hy Lạp/Síp.", "02 Trang đích chuẩn CRO sẵn sàng đón nhận chiến dịch trả phí", "Sẵn Sàng Triển Khai"),
    ("Tuần 4: Chạy Thử & Tinh Chỉnh Ads", "Ngày 22 – Ngày 28", "Khởi chạy chiến dịch Google Search Ads ngân sách thử nghiệm. Đối soát số liệu thực tế, tinh chỉnh từ khóa và trang đích.", "Báo cáo hiệu quả CPA, tỷ lệ chuyển đổi và danh sách khách hàng lead", "Chờ Hoàn Thiện Web")
]

for idx, rm in enumerate(roadmap, 2):
    ws6.append(list(rm))
    for c in range(1, 6):
        cell = ws6.cell(row=idx, column=c)
        cell.font = font_regular
        cell.border = thin_border
        cell.alignment = Alignment(vertical="center", wrap_text=True)
    ws6.cell(row=idx, column=2).alignment = Alignment(horizontal="center", vertical="center")
    ws6.cell(row=idx, column=5).alignment = Alignment(horizontal="center", vertical="center")
    ws6.row_dimensions[idx].height = 32

ws6.column_dimensions['A'].width = 30
ws6.column_dimensions['B'].width = 18
ws6.column_dimensions['C'].width = 55
ws6.column_dimensions['D'].width = 45
ws6.column_dimensions['E'].width = 22

excel_path = "Du_Lieu_Trien_Khai_Chi_Tiet_visagbluesea.com.xlsx"
wb.save(excel_path)
print(f"Đã xuất thành công file Excel 6 sheets: {excel_path}")
