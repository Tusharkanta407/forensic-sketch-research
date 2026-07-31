"""Generate a Literature Study table slide matching the teal academic template."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

OUT_DIR = Path(r"d:\Forensic-Sketch-Generator\docs\interim-review\figures")
OUT_DIR.mkdir(parents=True, exist_ok=True)

TEAL = (83, 178, 201)  # #53B2C9
LINE = (180, 215, 225)
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
DARK = (35, 35, 35)

W, H = 1600, 900
MARGIN = 36
TITLE_H = 72
COL_H = 48
FOOTER_H = 36
TABLE_TOP = MARGIN + TITLE_H
TABLE_BOTTOM = H - MARGIN - FOOTER_H
BODY_TOP = TABLE_TOP + COL_H
BODY_H = TABLE_BOTTOM - BODY_TOP
ROW_H = BODY_H // 3

# Column fractions (sum ~ 1.0)
COLS = [
    ("Sl. No.", 0.06),
    ("Journal, Publisher, & Year", 0.16),
    ("Title & author", 0.22),
    ("Methodology", 0.20),
    ("Findings", 0.18),
    ("Limitation", 0.18),
]

ROWS = [
    [
        "1",
        "World Journal of Advanced Research and Reviews (WJARR), 2026",
        "Forensic sketch generation using Gen-AI — Soppari et al.",
        "Text cleaning → Stable Diffusion XL sketch; InsightFace / BiSeNet features; FAISS mugshot retrieval",
        "End-to-end text-to-sketch with identity ranking; reduces forensic artist dependency",
        "Limited iterative witness refinement; weak multimodal fusion; few scars / marks",
    ],
    [
        "2",
        "IEEE / CVPR workshops & related venues (TediGAN; ST²FG)",
        "TediGAN — Xia et al.; ST²FG — Oza et al.",
        "Text mapped to StyleGAN latent space; BERT + Affine Combination Module with iterative user edits",
        "High-res (1024²) controllable faces; refinement loop closest to forensic interview flow",
        "GAN instability; imperfect identity control; photo output, not forensic pencil sketch",
    ],
    [
        "3",
        "Elsevier / IEEE Access / forensic imaging venues",
        "DCGAN sketch–photo (Devakumar & Sarath); Attribute CycleGAN; CLIP4Sketch — Jain et al.",
        "Sketch-to-photo GANs / CycleGAN; diffusion-augmented sketch–mugshot matching with CLIP embeddings",
        "Strong identity-preserving cross-domain matching once a sketch exists; improved SSIM / retrieval",
        "Assumes hand-drawn or operator-made sketch first; no text-to-composite starting point",
    ],
]


def load_font(size: int, bold: bool = False):
    candidates = []
    if bold:
        candidates += [
            r"C:\Windows\Fonts\timesbd.ttf",
            r"C:\Windows\Fonts\arialbd.ttf",
            r"C:\Windows\Fonts\calibrib.ttf",
        ]
    candidates += [
        r"C:\Windows\Fonts\times.ttf",
        r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\calibri.ttf",
        r"C:\Windows\Fonts\DejaVuSans.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def wrap_fit(draw, text, font, max_width, max_lines=8):
    """Word-wrap text to fit width; shrink font slightly if still too tall."""
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if len(lines) > max_lines:
        lines = lines[: max_lines - 1] + [lines[max_lines - 1][: max(1, len(lines[max_lines - 1]) - 1)] + "…"]
    return lines


def draw_wrapped(draw, text, x, y, w, h, font, fill=DARK, pad=10):
    max_w = w - 2 * pad
    lines = wrap_fit(draw, text, font, max_w)
    line_h = font.size + 4
    total = len(lines) * line_h
    # Top-align with small padding (table cells read better top-aligned)
    ty = y + pad
    if total + 2 * pad > h:
        # compress line spacing slightly
        line_h = max(font.size, (h - 2 * pad) // max(1, len(lines)))
    for i, line in enumerate(lines):
        draw.text((x + pad, ty + i * line_h), line, font=font, fill=fill)


def main():
    img = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(img)

    # Outer border
    draw.rectangle([MARGIN - 2, MARGIN - 2, W - MARGIN + 2, TABLE_BOTTOM + 2], outline=TEAL, width=2)

    # Title bar
    draw.rectangle([MARGIN, MARGIN, W - MARGIN, MARGIN + TITLE_H], fill=TEAL)
    title_font = load_font(36, bold=True)
    draw.text((MARGIN + 22, MARGIN + 16), "Literature Study", font=title_font, fill=WHITE)

    # Column header bar
    draw.rectangle([MARGIN, TABLE_TOP, W - MARGIN, TABLE_TOP + COL_H], fill=TEAL)

    table_w = W - 2 * MARGIN
    xs = [MARGIN]
    for _, frac in COLS:
        xs.append(xs[-1] + int(table_w * frac))
    xs[-1] = W - MARGIN  # snap last edge

    header_font = load_font(15, bold=True)
    body_font = load_font(13)
    sn_font = load_font(16, bold=True)

    for i, (label, _) in enumerate(COLS):
        x0, x1 = xs[i], xs[i + 1]
        # header text
        tw = draw.textlength(label, font=header_font)
        tx = x0 + 10
        if i == 0:
            tx = x0 + (x1 - x0 - tw) / 2
        draw.text((tx, TABLE_TOP + 14), label, font=header_font, fill=WHITE)

    # Body rows
    for r, row in enumerate(ROWS):
        y0 = BODY_TOP + r * ROW_H
        y1 = y0 + ROW_H
        for c, cell in enumerate(row):
            x0, x1 = xs[c], xs[c + 1]
            if c == 0:
                tw = draw.textlength(cell, font=sn_font)
                draw.text(
                    (x0 + (x1 - x0 - tw) / 2, y0 + ROW_H / 2 - 10),
                    cell,
                    font=sn_font,
                    fill=DARK,
                )
            else:
                draw_wrapped(draw, cell, x0, y0, x1 - x0, ROW_H, body_font)

        # horizontal line under row
        if r < 2:
            draw.line([(MARGIN, y1), (W - MARGIN, y1)], fill=LINE, width=2)

    # vertical grid lines through body
    for x in xs[1:-1]:
        draw.line([(x, TABLE_TOP), (x, TABLE_BOTTOM)], fill=LINE, width=2)

    # bottom border of table
    draw.line([(MARGIN, TABLE_BOTTOM), (W - MARGIN, TABLE_BOTTOM)], fill=TEAL, width=2)
    draw.line([(MARGIN, TABLE_TOP), (MARGIN, TABLE_BOTTOM)], fill=TEAL, width=2)
    draw.line([(W - MARGIN, TABLE_TOP), (W - MARGIN, TABLE_BOTTOM)], fill=TEAL, width=2)

    # page number
    page_font = load_font(18)
    draw.text((W - MARGIN - 24, H - MARGIN - 8), "8", font=page_font, fill=BLACK)

    out = OUT_DIR / "literature-study-slide.png"
    img.save(out, "PNG")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
