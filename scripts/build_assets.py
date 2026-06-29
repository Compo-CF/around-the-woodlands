"""Generate web assets for around-the-woodlands site from the 1024px master icon.

Outputs (all into the site root):
  favicon.png         — 256x256, simplified
  apple-touch-icon.png — 180x180
  icon.png            — 512x512 (in-page hero)
  og-image.png        — 1200x630 social-share card with icon + tagline
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "icon-master.png"
OUT = ROOT

# Same palette as the icon generator
SKY_TOP   = (244, 234, 210)
SKY_BOT   = (228, 213, 184)
HORIZON   = (201, 175, 134)
PINE_DEEP = (38, 58, 48)
TEXT_DARK = (42, 58, 46)
TEXT_MUTED= (107, 117, 101)


def resize(src: Image.Image, size: int) -> Image.Image:
    return src.resize((size, size), Image.LANCZOS)


def find_font(candidates, size):
    """Try to find a usable system font; fall back to PIL's default."""
    for name in candidates:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def make_og_image(icon: Image.Image) -> Image.Image:
    """1200x630 social-share card: icon left, tagline + app names right."""
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), SKY_TOP)
    # Vertical gradient
    px = img.load()
    for y in range(H):
        t = y / H
        r = int(SKY_TOP[0] + (SKY_BOT[0] - SKY_TOP[0]) * t)
        g = int(SKY_TOP[1] + (SKY_BOT[1] - SKY_TOP[1]) * t)
        b = int(SKY_TOP[2] + (SKY_BOT[2] - SKY_TOP[2]) * t)
        for x in range(W):
            px[x, y] = (r, g, b)

    # Drop the icon, square-cropped, on the left
    icon_size = 460
    icon_resized = icon.resize((icon_size, icon_size), Image.LANCZOS)
    icon_x = 60
    icon_y = (H - icon_size) // 2
    img.paste(icon_resized, (icon_x, icon_y))

    # Right side text
    draw = ImageDraw.Draw(img)
    text_x = icon_x + icon_size + 50
    bold = ["seguisb.ttf", "segoeuib.ttf", "Georgia Bold", "arialbd.ttf", "DejaVuSans-Bold.ttf"]
    reg  = ["segoeui.ttf", "Georgia", "arial.ttf", "DejaVuSans.ttf"]

    title_font = find_font(bold, 64)
    sub_font   = find_font(reg, 32)
    list_font  = find_font(reg, 28)

    draw.text((text_x, 180), "Around The Woodlands",
              font=title_font, fill=TEXT_DARK)
    draw.text((text_x, 270),
              "Field guides for life around\nThe Woodlands.",
              font=sub_font, fill=TEXT_DARK)
    draw.text((text_x, 410),
              "S-Tier Eats   ·   Fishing Guide\nTrail Guide (soon)",
              font=list_font, fill=TEXT_MUTED, spacing=8)

    return img


def main():
    if not MASTER.exists():
        raise SystemExit(f"Master icon missing at {MASTER}")
    master = Image.open(MASTER).convert("RGB")

    resize(master, 256).save(OUT / "favicon.png", "PNG", optimize=True)
    resize(master, 180).save(OUT / "apple-touch-icon.png", "PNG", optimize=True)
    resize(master, 512).save(OUT / "icon.png", "PNG", optimize=True)
    make_og_image(master).save(OUT / "og-image.png", "PNG", optimize=True)

    for f in ["favicon.png", "apple-touch-icon.png", "icon.png", "og-image.png"]:
        p = OUT / f
        print(f"  {f}: {p.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
