import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

card4_marker = """          <!-- Card 4 -->
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
          </div>"""

five_more_cards = """
          <!-- Card 5 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P1">
            <div class="flex items-center justify-between">
              <span class="font-mono font-bold text-xs text-slate-900">F-UI-05</span>
              <span class="badge-p1 text-[10px] font-bold px-2 py-0.5 rounded">P1 Ưu Tiên Cao</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Tiêu đề mẫu "CAPS TITLE" trên trang chủ</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Xóa bỏ khối chữ mẫu template Wix, thay bằng tiêu đề năng lực tư vấn chuyên nghiệp.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Trang Chủ Desktop</span>
              <a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>

          <!-- Card 6 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P1">
            <div class="flex items-center justify-between">
              <span class="font-mono font-bold text-xs text-slate-900">F-UI-06</span>
              <span class="badge-p1 text-[10px] font-bold px-2 py-0.5 rounded">P1 Ưu Tiên Cao</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Số liệu thành tựu dồn cục "17 5347 235"</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Tách thành 3 Stat Cards riêng biệt: 17+ Quốc Gia, 5.300+ Khách Hàng, 235+ Đối Tác.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Khu Vực Bằng Chứng</span>
              <a href="https://www.visagbluesea.com/" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>

          <!-- Card 7 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P1">
            <div class="flex items-center justify-between">
              <span class="font-mono font-bold text-xs text-slate-900">F-CRO-01</span>
              <span class="badge-p1 text-[10px] font-bold px-2 py-0.5 rounded">P1 Ưu Tiên Cao</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Thiếu Trung Tâm Báo Phí RFQ Hub</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Dựng phễu báo giá tự động cho phép chọn quốc gia và tải bảng dự toán chi phí chi tiết.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Trang Dịch Vụ Định Cư</span>
              <span class="text-slate-400 text-xs font-medium">Toàn hệ thống</span>
            </div>
          </div>

          <!-- Card 8 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P1">
            <div class="flex items-center justify-between">
              <span class="font-mono font-bold text-xs text-slate-900">F-TEC-01</span>
              <span class="badge-p1 text-[10px] font-bold px-2 py-0.5 rounded">P1 Ưu Tiên Cao</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Mã nguồn Wix nặng 1.22 MB làm chậm web</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Gỡ bỏ script thừa, nén WebP toàn bộ hình ảnh, tối ưu tốc độ tải trang dưới 2.5s.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Hạ Tầng Nền Tảng</span>
              <span class="text-slate-400 text-xs font-medium">Tối ưu tốc độ</span>
            </div>
          </div>

          <!-- Card 9 -->
          <div class="mobile-card-item bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs space-y-2" data-prio="P2">
            <div class="flex items-center justify-between">
              <span class="font-mono font-bold text-xs text-slate-900">F-UI-07</span>
              <span class="badge-p2 text-[10px] font-bold px-2 py-0.5 rounded">P2 Trung Bình</span>
            </div>
            <h4 class="font-bold text-xs text-slate-900">Tin tức chéo không khớp trang đích</h4>
            <p class="text-[11px] text-slate-600 leading-relaxed"><strong>Khắc phục:</strong> Cấu hình bộ lọc tin tức đúng chuyên mục từng quốc gia, giữ mạch tìm hiểu của khách.</p>
            <div class="pt-1 flex items-center justify-between border-t border-slate-100">
              <span class="text-[10px] text-slate-400">Trang Du Học & Định Cư</span>
              <a href="https://www.visagbluesea.com/du-hoc-uc" target="_blank" class="text-emerald-600 text-xs font-semibold inline-flex items-center gap-1">Soi lỗi ↗</a>
            </div>
          </div>"""

if card4_marker in text:
    text = text.replace(card4_marker, card4_marker + five_more_cards)
    print("Added 5 more mobile cards successfully!")
else:
    print("Error: card4_marker not found!")

with open(script_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved bien_tap_cau_chu.py with 9 mobile cards!")
