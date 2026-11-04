#!/usr/bin/env python3
"""Generate PWA icons for 多多速记"""
from PIL import Image, ImageDraw, ImageFont

def make_icon(text, size, font_size_factor=0.55):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    radius = size // 5
    bg = (15, 23, 42, 255)  # #0f172a
    draw.rounded_rectangle([0, 0, size, size], radius=radius, fill=bg)
    font_size = int(size * font_size_factor)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc", font_size)
    except Exception:
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except Exception:
            font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (size - text_w) / 2
    y = (size - text_h) / 2 - text_h * 0.1
    # cyan gradient-ish accent color
    draw.text((x, y), text, font=font, fill=(34, 211, 238, 255))  # #22d3ee
    return img

for size in [192, 512]:
    icon = make_icon("记", size)
    icon.save(f"icon-{size}.png")
    print(f"icon-{size}.png generated")
