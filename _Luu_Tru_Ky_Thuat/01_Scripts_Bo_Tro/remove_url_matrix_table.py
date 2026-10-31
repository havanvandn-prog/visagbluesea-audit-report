import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = '_Luu_Tru_Ky_Thuat/01_Scripts_Bo_Tro/bien_tap_cau_chu.py'
with open(script_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Locate the table block
marker_comment = '<!-- Bảng ánh xạ URL Cũ sang Mới -->'
if marker_comment in text:
    idx_start = text.find(marker_comment)
    # Find the end of this block
    # It ends after </table> and its closing </div>
    idx_table = text.find('</table>', idx_start)
    idx_end = text.find('</div>\n          </div>', idx_table)
    if idx_end == -1:
        idx_end = text.find('</div>\n        </div>', idx_table)
    
    # Let's inspect exactly where it closes
    idx_close_div1 = text.find('</div>', idx_table) # closing overflow-x-auto
    idx_close_div2 = text.find('</div>', idx_close_div1 + 6) # closing outer div
    
    table_block = text[idx_start:idx_close_div2 + 6]
    print("Found table block length:", len(table_block))
    print("Snippet to remove:")
    print(table_block[:150] + "..." + table_block[-100:])
    
    text = text.replace(table_block, '')
    print("Successfully removed URL Mapping Matrix table block!")
    
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(text)
else:
    print("marker_comment not found!")
