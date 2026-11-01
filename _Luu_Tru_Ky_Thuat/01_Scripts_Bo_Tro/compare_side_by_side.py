from PIL import Image

im_clone = Image.open(r"_Luu_Tru_Ky_Thuat\02_Screenshots_Debug_Va_Khao_Sat\clone_screenshot.png")
im_target = Image.open(r"C:\Users\ADMIN\.gemini\antigravity\brain\38c1b87a-0391-4409-94c9-3e9563c23cb2\.user_uploaded\media_1793516369190_2addd489.png")

# Resize target to width 1920 keeping aspect ratio
w_target, h_target = im_target.size
scale = 1920 / w_target
h_scaled = int(h_target * scale)
im_target_scaled = im_target.resize((1920, h_scaled), Image.Resampling.LANCZOS)

# Create side-by-side comparison image
canvas = Image.new("RGB", (1920, h_scaled + 1080), (255, 255, 255))
canvas.paste(im_target_scaled, (0, 0))
canvas.paste(im_clone, (0, h_scaled))

out_cmp = r"_Luu_Tru_Ky_Thuat\02_Screenshots_Debug_Va_Khao_Sat\side_by_side_comparison.png"
canvas.save(out_cmp)
print(f"Side-by-side comparison saved to: {out_cmp}")
