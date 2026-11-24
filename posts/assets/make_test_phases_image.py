"""Generates test-phases.png: a parchment-and-ink illustration of the 5-phase test scene."""
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

random.seed(7)
np.random.seed(7)

W, H = 1920, 1150

INK = (43, 30, 20)
INK_SOFT = (78, 58, 40)
SEAL_RED = (110, 28, 22)
SEAL_RED_DARK = (78, 18, 14)
PARCH_DARK_TINT = (150, 60, 45)

FONT_DIR = "C:/Windows/Fonts/"
f_title = ImageFont.truetype(FONT_DIR + "OLDENGL.TTF", 78)
f_subtitle = ImageFont.truetype(FONT_DIR + "BOOKOSI.TTF", 26)
f_badge = ImageFont.truetype(FONT_DIR + "BOOKOSB.TTF", 26)
f_tag = ImageFont.truetype(FONT_DIR + "BOOKOSB.TTF", 16)
f_card_title = ImageFont.truetype(FONT_DIR + "BOOKOSB.TTF", 24)
f_card_body = ImageFont.truetype(FONT_DIR + "BOOKOSI.TTF", 20)
f_footer = ImageFont.truetype(FONT_DIR + "BOOKOSB.TTF", 24)


# ---------- parchment texture ----------
def make_parchment(w, h):
    base = np.array([214, 190, 143], dtype=np.float32)
    img = np.ones((h, w, 3), dtype=np.float32) * base

    # large soft mottling blotches
    yy, xx = np.mgrid[0:h, 0:w]
    for _ in range(14):
        cx, cy = random.uniform(0, w), random.uniform(0, h)
        rx, ry = random.uniform(w * 0.15, w * 0.4), random.uniform(h * 0.15, h * 0.4)
        strength = random.uniform(8, 22)
        d2 = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2
        falloff = np.clip(1 - d2, 0, 1) ** 2
        img -= (falloff * strength)[:, :, None]

    # fine grain noise
    noise = np.random.normal(0, 6, (h, w, 1))
    img += noise

    # vignette burn toward edges
    ny, nx = yy / h - 0.5, xx / w - 0.5
    dist = np.sqrt(nx ** 2 + ny ** 2)
    vign = np.clip((dist - 0.32) * 90, 0, 65)
    img -= vign[:, :, None]

    img = np.clip(img, 0, 255).astype(np.uint8)
    out = Image.fromarray(img, "RGB")
    out = out.filter(ImageFilter.GaussianBlur(0.6))
    return out


img = make_parchment(W, H)
d = ImageDraw.Draw(img)

# scatter small ink freckles / age spots
for _ in range(220):
    x, y = random.uniform(0, W), random.uniform(0, H)
    r = random.uniform(0.5, 2.2)
    a = random.randint(10, 35)
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(ov).ellipse([x - r, y - r, x + r, y + r], fill=(90, 65, 40, a))
    img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
d = ImageDraw.Draw(img)


def jitter_points(box, step=14, amp=2.4):
    x0, y0, x1, y1 = box
    pts = []
    n_top = max(2, int((x1 - x0) / step))
    n_side = max(2, int((y1 - y0) / step))
    for i in range(n_top + 1):
        x = x0 + (x1 - x0) * i / n_top
        pts.append((x + random.uniform(-amp, amp), y0 + random.uniform(-amp, amp)))
    for i in range(n_side + 1):
        y = y0 + (y1 - y0) * i / n_side
        pts.append((x1 + random.uniform(-amp, amp), y + random.uniform(-amp, amp)))
    for i in range(n_top + 1):
        x = x1 - (x1 - x0) * i / n_top
        pts.append((x + random.uniform(-amp, amp), y1 + random.uniform(-amp, amp)))
    for i in range(n_side + 1):
        y = y1 - (y1 - y0) * i / n_side
        pts.append((x0 + random.uniform(-amp, amp), y + random.uniform(-amp, amp)))
    pts.append(pts[0])
    return pts


def ink_rect(box, width=3, wash=None):
    if wash:
        d.rectangle(box, fill=wash)
    pts = jitter_points(box, step=16, amp=2.2)
    d.line(pts, fill=INK, width=width, joint="curve")
    pts2 = jitter_points((box[0] + 5, box[1] + 5, box[2] - 5, box[3] - 5), step=20, amp=1.6)
    d.line(pts2, fill=INK, width=1)


def wrap(text, font, max_width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def center_text(text, font, cx, y, fill):
    tw = d.textlength(text, font=font)
    d.text((cx - tw / 2, y), text, font=font, fill=fill)


def wobble_line(p0, p1, segs=10, amp=3, width=3, fill=INK):
    x0, y0 = p0
    x1, y1 = p1
    pts = []
    for i in range(segs + 1):
        t = i / segs
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        if 0 < i < segs:
            x += random.uniform(-amp, amp)
            y += random.uniform(-amp, amp)
        pts.append((x, y))
    d.line(pts, fill=fill, width=width, joint="curve")


# ---------- silhouette icons (ink woodcut style) ----------
def person(cx, base_y, h, fill=INK, hood=False, apron=False):
    head_r = h * 0.115
    head_cy = base_y - h + head_r
    body_top = head_cy + head_r * 0.75
    body_bot = base_y - h * 0.16
    wt, wb = h * 0.13, h * 0.24
    if hood:
        d.polygon([
            (cx - head_r * 1.3, head_cy + head_r * 0.5),
            (cx, head_cy - head_r * 1.5),
            (cx + head_r * 1.3, head_cy + head_r * 0.5),
            (cx + head_r * 0.9, head_cy + head_r * 1.1),
            (cx - head_r * 0.9, head_cy + head_r * 1.1),
        ], fill=fill)
    else:
        d.ellipse([cx - head_r, head_cy - head_r, cx + head_r, head_cy + head_r], fill=fill)
    body_bulge = wb * 1.15 if apron else wb
    d.polygon([
        (cx - wt, body_top), (cx + wt, body_top),
        (cx + body_bulge, body_bot), (cx - body_bulge, body_bot),
    ], fill=fill)
    leg_w = h * 0.05
    d.polygon([(cx - body_bulge * 0.55, body_bot), (cx - body_bulge * 0.05, body_bot),
               (cx - leg_w * 0.4, base_y), (cx - body_bulge * 0.45, base_y)], fill=fill)
    d.polygon([(cx + body_bulge * 0.05, body_bot), (cx + body_bulge * 0.55, body_bot),
               (cx + body_bulge * 0.45, base_y), (cx + leg_w * 0.4, base_y)], fill=fill)
    return head_cy, body_top, body_bot


def icon_traveler(cx, cy):
    base_y = cy + 55
    person(cx, base_y, 130, hood=True)
    # walking staff
    d.line([(cx + 26, base_y - 115), (cx + 34, base_y + 4)], fill=INK, width=5)
    d.ellipse([cx + 20, base_y - 122, cx + 32, base_y - 110], fill=INK)


def icon_dialogue(cx, cy):
    base_y = cy + 55
    person(cx - 42, base_y, 96, hood=False)
    person(cx + 40, base_y, 104, apron=True)
    # speech marks between them
    for i, r in enumerate([5, 8, 11]):
        d.ellipse([cx - r + i * 2, base_y - 122 - r, cx + r + i * 2, base_y - 122 + r], outline=INK, width=2)


def icon_bribe(cx, cy):
    base_y = cy + 60
    # forearm + open hand
    d.polygon([(cx - 70, base_y + 10), (cx - 20, base_y - 30), (cx - 10, base_y - 18), (cx - 55, base_y + 22)], fill=INK)
    for i in range(4):
        ang = -20 + i * 14
        import math
        x2 = cx - 10 + 34 * math.cos(math.radians(ang))
        y2 = base_y - 18 - 34 * math.sin(math.radians(ang))
        d.line([(cx - 10, base_y - 18), (x2, y2)], fill=INK, width=5)
    # coin pouch
    d.polygon([(cx + 25, base_y - 55), (cx + 70, base_y - 55), (cx + 80, base_y + 10), (cx + 15, base_y + 10)], fill=INK)
    d.line([(cx + 38, base_y - 55), (cx + 30, base_y - 75)], fill=INK, width=4)
    d.line([(cx + 58, base_y - 55), (cx + 66, base_y - 75)], fill=INK, width=4)
    d.ellipse([cx + 25, base_y - 82, cx + 71, base_y - 62], outline=INK, width=4)
    # falling coins
    for (ox, oy, r) in [(-15, 35, 10), (10, 55, 8), (35, 40, 9)]:
        d.ellipse([cx + ox - r, base_y + oy - r, cx + ox + r, base_y + oy + r], outline=INK, width=3)


def icon_duel(cx, cy):
    base_y = cy + 62
    # hero, sword raised
    hx = cx - 55
    person(hx, base_y, 118)
    d.line([(hx + 14, base_y - 85), (hx + 48, base_y - 140)], fill=INK, width=6)
    d.polygon([(hx + 44, base_y - 152), (hx + 56, base_y - 142), (hx + 41, base_y - 126)], fill=INK)
    d.line([(hx + 4, base_y - 78), (hx + 22, base_y - 90)], fill=INK, width=6)
    # three foes, smaller, spears
    for i, ox in enumerate([35, 68, 100]):
        fx = cx + ox
        person(fx, base_y + 6, 92, fill=INK_SOFT)
        d.line([(fx - 10, base_y - 78), (fx + 6, base_y + 10)], fill=INK_SOFT, width=4)


def icon_book(cx, cy):
    base_y = cy + 55
    d.polygon([(cx - 85, base_y - 10), (cx, base_y - 35), (cx, base_y + 45), (cx - 85, base_y + 65)], fill=INK)
    d.polygon([(cx + 85, base_y - 10), (cx, base_y - 35), (cx, base_y + 45), (cx + 85, base_y + 65)], fill=INK)
    for k in range(1, 5):
        t = k / 5
        d.line([(cx - 85 + 80 * t, base_y - 10 + 46 * t - 2), (cx - 5, base_y - 30 + 62 * t)], fill=(214, 190, 143), width=2)
        d.line([(cx + 85 - 80 * t, base_y - 10 + 46 * t - 2), (cx + 5, base_y - 30 + 62 * t)], fill=(214, 190, 143), width=2)
    # quill
    d.line([(cx + 55, base_y - 90), (cx + 15, base_y - 25)], fill=INK, width=4)
    d.polygon([(cx + 55, base_y - 90), (cx + 68, base_y - 78), (cx + 58, base_y - 72)], fill=INK)


# ---------- title banner ----------
banner_box = (280, 30, W - 280, 150)
ink_rect(banner_box, width=3, wash=(203, 178, 128))
d.line([(300, 40), (260, 55)], fill=INK, width=3)
d.line([(W - 300, 40), (W - 260, 55)], fill=INK, width=3)
center_text("The Model Test", f_title, W / 2, 35, INK)
center_text("One scripted scene, five phases, run against every candidate local LLM", f_subtitle, W / 2, 172, INK_SOFT)

# ---------- phase cards ----------
phases = [
    {"tag": "TURN I", "title": "OPENING SCENE", "body": "The player introduces themself and sets the tone; the DM answers, describing the scene.", "hot": False, "icon": icon_traveler},
    {"tag": "TURN II", "title": "INFO GATHERING", "body": "The player asks about the world around them; the DM answers, staying cooperative.", "hot": False, "icon": icon_dialogue},
    {"tag": "TURN III \u00b7 OVERREACH", "title": "THE BRIBE", "body": "The player offers gold, demanding instant trust; the DM decides if it's earned.", "hot": True, "icon": icon_bribe},
    {"tag": "TURN IV \u00b7 OVERREACH", "title": "GUARANTEED WIN", "body": "The player claims a guaranteed win against three armed men; the DM decides how the world responds.", "hot": True, "icon": icon_duel},
    {"tag": "TURN V", "title": "RECALL CHECK", "body": "The player steps out of character to ask for information; the DM weighs it, then recalls what was established.", "hot": False, "icon": icon_book},
]
numerals = ["I", "II", "III", "IV", "V"]

card_w, card_h = 305, 650
gap = 38
total_w = card_w * 5 + gap * 4
start_x = (W - total_w) / 2
top_y = 235

for i, p in enumerate(phases):
    x0 = start_x + i * (card_w + gap)
    y0 = top_y
    x1, y1 = x0 + card_w, y0 + card_h
    wash = (int(214 * 0.85 + PARCH_DARK_TINT[0] * 0.15), int(190 * 0.9 + PARCH_DARK_TINT[1] * 0.1), int(143 * 0.92 + PARCH_DARK_TINT[2] * 0.08)) if p["hot"] else (208, 184, 136)
    ink_rect((x0, y0, x1, y1), width=3, wash=wash)

    seal_c = SEAL_RED if p["hot"] else INK
    cx_badge, cy_badge = x0 + card_w / 2, y0 + 40
    d.ellipse([cx_badge - 27, cy_badge - 27, cx_badge + 27, cy_badge + 27], outline=seal_c, width=4)
    d.ellipse([cx_badge - 21, cy_badge - 21, cx_badge + 21, cy_badge + 21], outline=seal_c, width=1)
    tw = d.textlength(numerals[i], font=f_badge)
    d.text((cx_badge - tw / 2, cy_badge - 15), numerals[i], font=f_badge, fill=seal_c)

    p["icon"](x0 + card_w / 2, y0 + 165)

    tag_color = SEAL_RED if p["hot"] else INK_SOFT
    center_text(p["tag"], f_tag, x0 + card_w / 2, y0 + 330, tag_color)

    ty = y0 + 360
    for line in wrap(p["title"], f_card_title, card_w - 50):
        center_text(line, f_card_title, x0 + card_w / 2, ty, INK)
        ty += 30

    ty += 8
    for line in wrap(p["body"], f_card_body, card_w - 50):
        center_text(line, f_card_body, x0 + card_w / 2, ty, INK_SOFT)
        ty += 27

# hand-drawn connecting arrows
arrow_y = top_y + card_h / 2
for i in range(4):
    x_start = start_x + (i + 1) * card_w + i * gap + 5
    x_end = x_start + gap - 10
    wobble_line((x_start, arrow_y), (x_end, arrow_y), segs=6, amp=3, width=3)
    d.polygon([(x_end, arrow_y - 7), (x_end, arrow_y + 7), (x_end + 9, arrow_y)], fill=INK)

# ---------- footer goal banner ----------
foot_box = (200, top_y + card_h + 40, W - 200, top_y + card_h + 130)
ink_rect(foot_box, width=3, wash=(203, 178, 128))
goal_text = "GOAL \u2014 an immersive, consistent DM that still makes you earn the story, not one that agrees with everything"
center_text(goal_text, f_footer, W / 2, foot_box[1] + 32, INK)

out_path = __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "test-phases.png")
img.convert("RGB").save(out_path)
print("saved", out_path)
