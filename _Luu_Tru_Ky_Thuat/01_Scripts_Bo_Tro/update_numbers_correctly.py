import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Section 2 Card titles with clear numbers: "Điểm Nghẽn 01" to "Điểm Nghẽn 05"
content = content.replace(
    '<h3 class="text-sm sm:text-base font-bold text-slate-900">Header Chứa 3 Số Điện Thoại Gây Rối Mắt & Chữ "Call now:" Mất Số</h3>',
    '<h3 class="text-sm sm:text-base font-bold text-slate-900">Điểm Nghẽn 01: Header Chứa 3 Số Điện Thoại Gây Rối Mắt & Chữ "Call now:" Mất Số</h3>'
)
content = content.replace(
    '<h3 class="text-sm sm:text-base font-bold text-slate-900">Lộ Tiêu Đề Tiếng Tây Ban Nha "Acerca de" Trên Trang Định Cư Mỹ EB-5</h3>',
    '<h3 class="text-sm sm:text-base font-bold text-slate-900">Điểm Nghẽn 02: Lộ Tiêu Đề Tiếng Tây Ban Nha "Acerca de" Trên Trang Định Cư Mỹ EB-5</h3>'
)
content = content.replace(
    '<h3 class="text-sm sm:text-base font-bold text-slate-900">Thiếu Thanh Nút Bấm Cố Định Dưới Đáy Màn Hình Điện Thoại (Thumb Zone)</h3>',
    '<h3 class="text-sm sm:text-base font-bold text-slate-900">Điểm Nghẽn 03: Thiếu Thanh Nút Bấm Cố Định Dưới Đáy Màn Hình Điện Thoại (Thumb Zone)</h3>'
)
content = content.replace(
    '<h3 class="text-sm sm:text-base font-bold text-slate-900">Biểu Mẫu Tư Vấn Tách Ô Tên & Họ Riêng Biệt, Bắt Nhập Email</h3>',
    '<h3 class="text-sm sm:text-base font-bold text-slate-900">Điểm Nghẽn 04: Biểu Mẫu Tư Vấn Tách Ô Tên & Họ Riêng Biệt, Bắt Nhập Email</h3>'
)
content = content.replace(
    '<h3 class="text-sm sm:text-base font-bold text-slate-900">Chưa Cài Đặt Thẻ Đo Lường Chuyển Đổi Google Ads (GTM Tag)</h3>',
    '<h3 class="text-sm sm:text-base font-bold text-slate-900">Điểm Nghẽn 05: Chưa Cài Đặt Thẻ Đo Lường Chuyển Đổi Google Ads (GTM Tag)</h3>'
)

# 2. Update Section 4 Subtitle: 10 hạng mục kỹ thuật
content = content.replace(
    'Danh mục 14 hạng mục kỹ thuật cần xử lý (Hiển thị dạng Card trên Mobile, Bảng trên Desktop).',
    'Danh mục 10 hạng mục kỹ thuật cần xử lý (Hiển thị dạng Card trên Mobile, Bảng trên Desktop).'
)

# 3. Update Section 4 Filter buttons: 10 items total
old_sec4_btns = '''            <button onclick="filterTablePriority('all', this)" class="table-filter-btn active px-3 py-1 text-xs font-semibold rounded-lg border border-slate-300 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              Tất Cả (14)
            </button>
            <button onclick="filterTablePriority('P0', this)" class="table-filter-btn px-3 py-1 text-xs font-semibold rounded-lg border border-slate-300 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              P0 Khẩn Cấp (6)
            </button>
            <button onclick="filterTablePriority('P1', this)" class="table-filter-btn px-3 py-1 text-xs font-semibold rounded-lg border border-slate-300 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              P1 Quan Trọng (5)
            </button>
            <button onclick="filterTablePriority('P2', this)" class="table-filter-btn px-3 py-1 text-xs font-semibold rounded-lg border border-slate-300 bg-white text-slate-700 whitespace-nowrap shrink-0 transition-colors">
              P2 Trung Bình (3)
            </button>'''

new_sec4_btns = '''            <button onclick="filterTablePriority('all', this)" class="table-filter-btn active px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-slate-900 text-white whitespace-nowrap shrink-0">
              Tất Cả (10)
            </button>
            <button onclick="filterTablePriority('P0', this)" class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0">
              P0 Khẩn Cấp (5)
            </button>
            <button onclick="filterTablePriority('P1', this)" class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0">
              P1 Ưu Tiên Cao (4)
            </button>
            <button onclick="filterTablePriority('P2', this)" class="table-filter-btn px-3 py-1 text-xs font-bold rounded-lg border border-slate-200 bg-white text-slate-700 whitespace-nowrap shrink-0">
              P2 Trung Bình (1)
            </button>'''

content = content.replace(old_sec4_btns, new_sec4_btns)

# 4. Standardize Section 4 Desktop Table headers & row numbers 01 to 10
old_table_block = '''          <table class="w-full text-left border-collapse text-xs sm:text-sm" id="desktop-action-table">
            <thead>
              <tr class="bg-slate-100 border-b border-slate-200 text-slate-700 font-bold">
                <th class="p-3 whitespace-nowrap">Mã</th>
                <th class="p-3">Hạng Mục Công Việc</th>
                <th class="p-3">Vấn Đề Ghi Nhận</th>
                <th class="p-3">Hành Động Khắc Phục</th>
                <th class="p-3 whitespace-nowrap">Ưu Tiên</th>
                <th class="p-3 whitespace-nowrap">Link Soi Lỗi</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 text-slate-700">
              <tr class="table-row-item hover:bg-slate-50" data-prio="P0">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-UI-01</td>
                <td class="p-3 font-semibold text-slate-900">Header 3 Hotline rối mắt</td>
                <td class="p-3 text-slate-600">3 số điện thoại không rõ vai trò, chữ Call now mất số</td>
                <td class="p-3 text-slate-800">Quy chuẩn còn 1 Hotline chính + 1 Zalo, có nhãn rõ</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Trang chủ <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P0">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-UI-02</td>
                <td class="p-3 font-semibold text-slate-900">Sót chữ Tây Ban Nha "Acerca de"</td>
                <td class="p-3 text-slate-600">Thẻ H1 trang EB-5 triệu đô hiển thị chữ nước ngoài</td>
                <td class="p-3 text-slate-800">Đổi thành "Đầu Tư Định Cư Mỹ EB-5 — Nhận Thẻ Xanh"</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/us-green-card-eb-5" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Trang EB-5 <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P0">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-UI-03</td>
                <td class="p-3 font-semibold text-slate-900">Thiếu Mobile Sticky Action Bar</td>
                <td class="p-3 text-slate-600">Không có nút gọi/zalo cố định đáy màn hình điện thoại</td>
                <td class="p-3 text-slate-800">Lập trình thanh cố định đáy: 2 nút [Gọi Ngay] + [Zalo]</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Bật mobile <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P0">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-UI-04</td>
                <td class="p-3 font-semibold text-slate-900">Form tách riêng ô Tên & Họ</td>
                <td class="p-3 text-slate-600">Form phức tạp, bắt buộc nhập email tạo ma sát tâm lý</td>
                <td class="p-3 text-slate-800">Gộp thành 3 ô: Họ tên, SĐT Zalo, Nhu cầu quan tâm</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/contact-us" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Trang Form <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P0">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-TRK-01</td>
                <td class="p-3 font-semibold text-slate-900">Chưa gắn thẻ đo lường Google Ads</td>
                <td class="p-3 text-slate-600">GTM chưa cấu hình ghi nhận chuyển đổi lượt gọi và gửi form</td>
                <td class="p-3 text-slate-800">Tạo Conversion Action trong Google Ads và kích hoạt GTM</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><span class="text-slate-400">GTM Snippet</span></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P1">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-UI-05</td>
                <td class="p-3 font-semibold text-slate-900">Tiêu đề mẫu "CAPS TITLE"</td>
                <td class="p-3 text-slate-600">Sót chữ mẫu tiếng Anh của template Wix trên trang chủ</td>
                <td class="p-3 text-slate-800">Xóa bỏ khối chữ mẫu, thay bằng tiêu đề chuyên môn</td>
                <td class="p-3"><span class="badge-p1 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P1 (Cao)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Trang chủ <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P1">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-UI-06</td>
                <td class="p-3 font-semibold text-slate-900">Số liệu thành tựu dồn cục "17 5347 235"</td>
                <td class="p-3 text-slate-600">Các con số dồn chung vào thẻ H2 không có nhãn</td>
                <td class="p-3 text-slate-800">Thiết kế 3 thẻ Stat Cards: 17+ Quốc gia, 5,300+ Khách hàng</td>
                <td class="p-3"><span class="badge-p1 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P1 (Cao)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Trang chủ <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P1">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-CRO-01</td>
                <td class="p-3 font-semibold text-slate-900">Thiếu Trung Tâm Báo Phí RFQ Hub</td>
                <td class="p-3 text-slate-600">Trang chi tiết chỉ có bài viết dài, thiếu bảng dự toán BOQ</td>
                <td class="p-3 text-slate-800">Dựng trang RFQ Hub so sánh 3 gói định cư và nút tải PDF</td>
                <td class="p-3"><span class="badge-p1 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P1 (Cao)</span></td>
                <td class="p-3 whitespace-nowrap"><span class="text-blue-600 font-semibold">Tạo mới</span></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P1">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-TEC-01</td>
                <td class="p-3 font-semibold text-slate-900">Mã nguồn Wix nặng 1.22 MB</td>
                <td class="p-3 text-slate-600">Mã nguồn nặng làm chậm tốc độ tải trang trên điện thoại, ảnh hưởng điểm trang đích Google Ads</td>
                <td class="p-3 text-slate-800">Tắt các widget thừa, nén ảnh WebP để tăng tốc độ trang đích dưới 2.5 giây</td>
                <td class="p-3"><span class="badge-p1 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P1 (Cao)</span></td>
                <td class="p-3 whitespace-nowrap"><span class="text-slate-400">Toàn site</span></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P2">
                <td class="p-3 font-mono font-bold text-slate-900 whitespace-nowrap">F-UI-07</td>
                <td class="p-3 font-semibold text-slate-900">Tin tức chéo không khớp trang đích</td>
                <td class="p-3 text-slate-600">Trang Du học Úc nhưng khối tin tức hiện bài Phần Lan, Canada</td>
                <td class="p-3 text-slate-800">Lọc bài viết theo chuyên mục tương ứng với từng quốc gia</td>
                <td class="p-3"><span class="badge-p2 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P2 (TB)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/study-in-australia" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Trang Úc <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
            </tbody>
          </table>'''

new_table_block = '''          <table class="w-full text-left border-collapse text-xs sm:text-sm" id="desktop-action-table">
            <thead>
              <tr class="bg-slate-100 border-b border-slate-200 text-slate-700 font-bold">
                <th class="p-3 whitespace-nowrap text-center w-12">STT</th>
                <th class="p-3">Hạng Mục Công Việc</th>
                <th class="p-3">Vấn Đề Ghi Nhận</th>
                <th class="p-3">Hành Động Khắc Phục</th>
                <th class="p-3 whitespace-nowrap">Ưu Tiên</th>
                <th class="p-3 whitespace-nowrap">Link Soi Lỗi</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 text-slate-700">
              <tr class="table-row-item hover:bg-slate-50" data-prio="P0">
                <td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">01</td>
                <td class="p-3 font-semibold text-slate-900">Header 3 Hotline rối mắt (F-UI-01)</td>
                <td class="p-3 text-slate-600">3 số điện thoại không rõ vai trò, chữ Call now mất số</td>
                <td class="p-3 text-slate-800">Quy chuẩn còn 1 Hotline chính + 1 Zalo, có nhãn rõ</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Trang chủ <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P0">
                <td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">02</td>
                <td class="p-3 font-semibold text-slate-900">Sót chữ Tây Ban Nha "Acerca de" (F-UI-02)</td>
                <td class="p-3 text-slate-600">Thẻ H1 trang EB-5 triệu đô hiển thị chữ nước ngoài</td>
                <td class="p-3 text-slate-800">Đổi thành "Đầu Tư Định Cư Mỹ EB-5 — Nhận Thẻ Xanh"</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/us-green-card-eb-5" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Trang EB-5 <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P0">
                <td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">03</td>
                <td class="p-3 font-semibold text-slate-900">Thiếu Mobile Sticky Action Bar (F-UI-03)</td>
                <td class="p-3 text-slate-600">Không có nút gọi/zalo cố định đáy màn hình điện thoại</td>
                <td class="p-3 text-slate-800">Lập trình thanh cố định đáy: 2 nút [Gọi Ngay] + [Zalo]</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Bật mobile <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P0">
                <td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">04</td>
                <td class="p-3 font-semibold text-slate-900">Form tách riêng ô Tên & Họ (F-UI-04)</td>
                <td class="p-3 text-slate-600">Form phức tạp, bắt buộc nhập email tạo ma sát tâm lý</td>
                <td class="p-3 text-slate-800">Gộp thành 3 ô: Họ tên, SĐT Zalo, Nhu cầu quan tâm</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/contact-us" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Trang Form <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P0">
                <td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">05</td>
                <td class="p-3 font-semibold text-slate-900">Chưa gắn thẻ đo lường Google Ads (F-TRK-01)</td>
                <td class="p-3 text-slate-600">GTM chưa cấu hình ghi nhận chuyển đổi lượt gọi và gửi form</td>
                <td class="p-3 text-slate-800">Tạo Conversion Action trong Google Ads và kích hoạt GTM</td>
                <td class="p-3"><span class="badge-p0 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P0 (Khẩn)</span></td>
                <td class="p-3 whitespace-nowrap"><span class="text-slate-400">GTM Snippet</span></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P1">
                <td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">06</td>
                <td class="p-3 font-semibold text-slate-900">Tiêu đề mẫu "CAPS TITLE" (F-UI-05)</td>
                <td class="p-3 text-slate-600">Sót chữ mẫu tiếng Anh của template Wix trên trang chủ</td>
                <td class="p-3 text-slate-800">Xóa bỏ khối chữ mẫu, thay bằng tiêu đề chuyên môn</td>
                <td class="p-3"><span class="badge-p1 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P1 (Cao)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Trang chủ <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P1">
                <td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">07</td>
                <td class="p-3 font-semibold text-slate-900">Số liệu thành tựu dồn cục "17 5347 235" (F-UI-06)</td>
                <td class="p-3 text-slate-600">Các con số dồn chung vào thẻ H2 không có nhãn</td>
                <td class="p-3 text-slate-800">Thiết kế 3 thẻ Stat Cards: 17+ Quốc gia, 5,300+ Khách hàng</td>
                <td class="p-3"><span class="badge-p1 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P1 (Cao)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Trang chủ <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P1">
                <td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">08</td>
                <td class="p-3 font-semibold text-slate-900">Thiếu Trung Tâm Báo Phí RFQ Hub (F-CRO-01)</td>
                <td class="p-3 text-slate-600">Trang chi tiết chỉ có bài viết dài, thiếu bảng dự toán BOQ</td>
                <td class="p-3 text-slate-800">Dựng trang RFQ Hub so sánh 3 gói định cư và nút tải PDF</td>
                <td class="p-3"><span class="badge-p1 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P1 (Cao)</span></td>
                <td class="p-3 whitespace-nowrap"><span class="text-blue-600 font-semibold">Tạo mới</span></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P1">
                <td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">09</td>
                <td class="p-3 font-semibold text-slate-900">Mã nguồn Wix nặng 1.22 MB (F-TEC-01)</td>
                <td class="p-3 text-slate-600">Mã nguồn nặng làm chậm tốc độ tải trang trên điện thoại, ảnh hưởng điểm trang đích Google Ads</td>
                <td class="p-3 text-slate-800">Tắt các widget thừa, nén ảnh WebP để tăng tốc độ trang đích dưới 2.5 giây</td>
                <td class="p-3"><span class="badge-p1 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P1 (Cao)</span></td>
                <td class="p-3 whitespace-nowrap"><span class="text-slate-400">Toàn site</span></td>
              </tr>
              <tr class="table-row-item hover:bg-slate-50" data-prio="P2">
                <td class="p-3 font-bold text-slate-900 whitespace-nowrap text-center">10</td>
                <td class="p-3 font-semibold text-slate-900">Tin tức chéo không khớp trang đích (F-UI-07)</td>
                <td class="p-3 text-slate-600">Trang Du học Úc nhưng khối tin tức hiện bài Phần Lan, Canada</td>
                <td class="p-3 text-slate-800">Lọc bài viết theo chuyên mục tương ứng với từng quốc gia</td>
                <td class="p-3"><span class="badge-p2 text-[11px] font-bold px-2 py-0.5 rounded whitespace-nowrap">P2 (TB)</span></td>
                <td class="p-3 whitespace-nowrap"><a href="https://www.visagbluesea.com/study-in-australia" target="_blank" class="text-emerald-600 hover:underline font-medium inline-flex items-center gap-1">Trang Úc <i data-lucide="external-link" class="w-3 h-3"></i></a></td>
              </tr>
            </tbody>
          </table>'''

content = content.replace(old_table_block, new_table_block)

# 5. Full 10 Mobile Cards (cards 01 to 10 for mobile with P0, P1, P2)
old_mobile_block = '''        <!-- 2. GIAO DIỆN DI ĐỘNG (MOBILE CARD STACK) -->
        <div class="md:hidden space-y-3" id="mobile-action-cards">
          <!-- Card 1 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P0">
            <div class="flex items-center justify-between">
              <span class="font-mono font-bold text-xs text-slate-900">F-UI-01</span>
              <span class="badge-p0 text-[10px] font-bold px-2 py-0.5 rounded">P0 Khẩn Cấp</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Header 3 Hotline rối mắt & Call now mất số</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Giữ lại 1 Hotline chính (0901.830.827) + 1 Zalo, có nhãn rõ ràng.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Header Desktop</span>
              <a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>

          <!-- Card 2 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P0">
            <div class="flex items-center justify-between">
              <span class="font-mono font-bold text-xs text-slate-900">F-UI-02</span>
              <span class="badge-p0 text-[10px] font-bold px-2 py-0.5 rounded">P0 Khẩn Cấp</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Sót chữ Tây Ban Nha "Acerca de" trên EB-5</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Đổi H1 thành "Đầu Tư Định Cư Mỹ EB-5 — Nhận Thẻ Xanh Cho Cả Gia Đình".</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Trang EB-5 20 tỷ</span>
              <a href="https://www.visagbluesea.com/us-green-card-eb-5" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>

          <!-- Card 3 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P0">
            <div class="flex items-center justify-between">
              <span class="font-mono font-bold text-xs text-slate-900">F-UI-03</span>
              <span class="badge-p0 text-[10px] font-bold px-2 py-0.5 rounded">P0 Khẩn Cấp</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Thiếu Mobile Sticky Action Bar</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Gắn thanh cố định đáy: 2 nút [Gọi Ngay 24/7] + [Chat Zalo] vừa ngón cái.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Mobile Toàn Site</span>
              <a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>

          <!-- Card 4 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P0">
            <div class="flex items-center justify-between">
              <span class="font-mono font-bold text-xs text-slate-900">F-UI-04</span>
              <span class="badge-p0 text-[10px] font-bold px-2 py-0.5 rounded">P0 Khẩn Cấp</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Form tách riêng ô Tên & Họ, bắt email</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Rút gọn còn 3 ô: Họ tên, SĐT Zalo, Nhu cầu; cam kết phản hồi sau 15 phút.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Trang Liên Hệ</span>
              <a href="https://www.visagbluesea.com/contact-us" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>

          <!-- Card 5 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P0">
            <div class="flex items-center justify-between">
              <span class="font-mono font-bold text-xs text-slate-900">F-TRK-01</span>
              <span class="badge-p0 text-[10px] font-bold px-2 py-0.5 rounded">P0 Khẩn Cấp</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Chưa gắn thẻ đo lường Google Ads</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Cài đặt theo dõi tự động cho nút Gọi, nút Zalo và Form gửi thông tin.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">GTM Conversion</span>
              <span class="text-slate-400 text-xs">Cài trong GTM</span>
            </div>
          </div>
        </div>'''

new_mobile_block = '''        <!-- 2. GIAO DIỆN DI ĐỘNG (MOBILE CARD STACK - ĐỦ 10 HẠNG MỤC) -->
        <div class="md:hidden space-y-3" id="mobile-action-cards">
          <!-- Card 01 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P0">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-slate-900">Hạng Mục 01</span>
              <span class="badge-p0 text-[10px] font-bold px-2 py-0.5 rounded">P0 Khẩn Cấp</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Header 3 Hotline rối mắt & Call now mất số (F-UI-01)</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Giữ lại 1 Hotline chính (0901.830.827) + 1 Zalo, có nhãn rõ ràng.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Header Desktop</span>
              <a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>

          <!-- Card 02 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P0">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-slate-900">Hạng Mục 02</span>
              <span class="badge-p0 text-[10px] font-bold px-2 py-0.5 rounded">P0 Khẩn Cấp</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Sót chữ Tây Ban Nha "Acerca de" trên EB-5 (F-UI-02)</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Đổi H1 thành "Đầu Tư Định Cư Mỹ EB-5 — Nhận Thẻ Xanh Cho Cả Gia Đình".</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Trang EB-5 20 tỷ</span>
              <a href="https://www.visagbluesea.com/us-green-card-eb-5" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>

          <!-- Card 03 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P0">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-slate-900">Hạng Mục 03</span>
              <span class="badge-p0 text-[10px] font-bold px-2 py-0.5 rounded">P0 Khẩn Cấp</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Thiếu Mobile Sticky Action Bar (F-UI-03)</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Gắn thanh cố định đáy: 2 nút [Gọi Ngay 24/7] + [Chat Zalo] vừa ngón cái.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Mobile Toàn Site</span>
              <a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>

          <!-- Card 04 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P0">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-slate-900">Hạng Mục 04</span>
              <span class="badge-p0 text-[10px] font-bold px-2 py-0.5 rounded">P0 Khẩn Cấp</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Form tách riêng ô Tên & Họ, bắt email (F-UI-04)</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Rút gọn còn 3 ô: Họ tên, SĐT Zalo, Nhu cầu; cam kết phản hồi sau 15 phút.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Trang Liên Hệ</span>
              <a href="https://www.visagbluesea.com/contact-us" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>

          <!-- Card 05 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P0">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-slate-900">Hạng Mục 05</span>
              <span class="badge-p0 text-[10px] font-bold px-2 py-0.5 rounded">P0 Khẩn Cấp</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Chưa gắn thẻ đo lường Google Ads (F-TRK-01)</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Cài đặt theo dõi tự động cho nút Gọi, nút Zalo và Form gửi thông tin.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">GTM Conversion</span>
              <span class="text-slate-400 text-xs">Cài trong GTM</span>
            </div>
          </div>

          <!-- Card 06 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P1">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-slate-900">Hạng Mục 06</span>
              <span class="badge-p1 text-[10px] font-bold px-2 py-0.5 rounded">P1 Ưu Tiên Cao</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Tiêu đề mẫu "CAPS TITLE" trên trang chủ (F-UI-05)</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Xóa bỏ khối chữ mẫu, thay bằng tiêu đề chuyên môn chuẩn định vị.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Trang Chủ Desktop</span>
              <a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>

          <!-- Card 07 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P1">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-slate-900">Hạng Mục 07</span>
              <span class="badge-p1 text-[10px] font-bold px-2 py-0.5 rounded">P1 Ưu Tiên Cao</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Số liệu dồn cục "17 5347 235" không nhãn (F-UI-06)</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Thiết kế 3 thẻ Stat Cards: 17+ Quốc gia, 5,300+ Khách hàng, 235+ Đối tác.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Trang Chủ Desktop</span>
              <a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>

          <!-- Card 08 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P1">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-slate-900">Hạng Mục 08</span>
              <span class="badge-p1 text-[10px] font-bold px-2 py-0.5 rounded">P1 Ưu Tiên Cao</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Thiếu Trung Tâm Báo Phí RFQ Hub (F-CRO-01)</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Dựng trang RFQ Hub so sánh 3 gói định cư và nút tải dự toán chi phí PDF.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Toàn Hệ Thống</span>
              <span class="text-blue-600 text-xs font-semibold">Tạo mới</span>
            </div>
          </div>

          <!-- Card 09 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P1">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-slate-900">Hạng Mục 09</span>
              <span class="badge-p1 text-[10px] font-bold px-2 py-0.5 rounded">P1 Ưu Tiên Cao</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Mã nguồn Wix nặng 1.22 MB làm chậm trang đích (F-TEC-01)</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Tắt các widget thừa, nén ảnh WebP để tăng tốc độ trang đích dưới 2.5 giây.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Trang Đích Ads</span>
              <span class="text-slate-400 text-xs">Tối ưu tốc độ</span>
            </div>
          </div>

          <!-- Card 10 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P2">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-slate-900">Hạng Mục 10</span>
              <span class="badge-p2 text-[10px] font-bold px-2 py-0.5 rounded">P2 Trung Bình</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Tin tức chéo không khớp trang đích (F-UI-07)</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Lọc bài viết theo đúng chuyên mục tương ứng với từng quốc gia dịch vụ.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Trang Úc & Mỹ</span>
              <a href="https://www.visagbluesea.com/study-in-australia" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>
        </div>'''

content = content.replace(old_mobile_block, new_mobile_block)

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated numbers across bien_tap_cau_chu.py successfully!')
