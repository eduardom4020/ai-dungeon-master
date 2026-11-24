"""Generates refused-claim.png: a parchment-and-ink illustration of one real
exchange from the `refusals` eval (20261124-095600_ask-after-refusal-v2, run 3):
the player invents rain, the DM says it isn't raining and asks whether Kael
still moves to the table, the player says yes, the DM narrates (trimmed).
Same style as make_test_phases_image.py."""
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

random.seed(11)
np.random.seed(11)

W, H = 1920, 1080
INK = (43, 30, 20)
INK_SOFT = (78, 58, 40)
SEAL_RED = (110, 28, 22)
PARCH = (214, 190, 143)

FONT_DIR = "C:/Windows/Fonts/"
f_title = ImageFont.truetype(FONT_DIR + "OLDENGL.TTF", 78)
f_subtitle = ImageFont.truetype(FONT_DIR + "BOOKOSI.TTF", 26)
f_label = ImageFont.truetype(FONT_DIR + "BOOKOSB.TTF", 20)
f_body = ImageFont.truetype(FONT_DIR + "BOOKOSI.TTF", 27)
f_body_b = ImageFont.truetype(FONT_DIR + "BOOKOSB.TTF", 27)
f_footer = ImageFont.truetype(FONT_DIR + "BOOKOSB.TTF", 24)


def make_parchment(w, h):
    img = np.ones((h, w, 3), dtype=np.float32) * np.array(PARCH, dtype=np.float32)
    yy, xx = np.mgrid[0:h, 0:w]
    for _ in range(14):
        cx, cy = random.uniform(0, w), random.uniform(0, h)
        rx, ry = random.uniform(w * 0.15, w * 0.4), random.uniform(h * 0.15, h * 0.4)
        d2 = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2
        img -= (np.clip(1 - d2, 0, 1) ** 2 * random.uniform(8, 22))[:, :, None]
    img += np.random.normal(0, 6, (h, w, 1))
    dist = np.sqrt((xx / w - 0.5) ** 2 + (yy / h - 0.5) ** 2)
    img -= np.clip((dist - 0.32) * 90, 0, 65)[:, :, None]
    out = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")
    return out.filter(ImageFilter.GaussianBlur(0.6))


img = make_parchment(W, H).convert("RGBA")
ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
od = ImageDraw.Draw(ov)
for _ in range(220):
    x, y, r = random.uniform(0, W), random.uniform(0, H), random.uniform(0.5, 2.2)
    od.ellipse([x - r, y - r, x + r, y + r], fill=(90, 65, 40, random.randint(10, 35)))
img = Image.alpha_composite(img, ov).convert("RGB")
d = ImageDraw.Draw(img)


def jitter_points(box, step=14, amp=2.4):
    x0, y0, x1, y1 = box
    n_top, n_side = max(2, int((x1 - x0) / step)), max(2, int((y1 - y0) / step))
    pts = []
    for i in range(n_top + 1):
        pts.append((x0 + (x1 - x0) * i / n_top + random.uniform(-amp, amp), y0 + random.uniform(-amp, amp)))
    for i in range(n_side + 1):
        pts.append((x1 + random.uniform(-amp, amp), y0 + (y1 - y0) * i / n_side + random.uniform(-amp, amp)))
    for i in range(n_top + 1):
        pts.append((x1 - (x1 - x0) * i / n_top + random.uniform(-amp, amp), y1 + random.uniform(-amp, amp)))
    for i in range(n_side + 1):
        pts.append((x0 + random.uniform(-amp, amp), y1 - (y1 - y0) * i / n_side + random.uniform(-amp, amp)))
    pts.append(pts[0])
    return pts


def ink_rect(box, width=3, wash=None, color=INK):
    if wash:
        d.rectangle(box, fill=wash)
    d.line(jitter_points(box, 16, 2.2), fill=color, width=width, joint="curve")
    d.line(jitter_points((box[0] + 5, box[1] + 5, box[2] - 5, box[3] - 5), 20, 1.6), fill=color, width=1)


def wobble_line(p0, p1, segs=10, amp=3, width=3, fill=INK):
    pts = []
    for i in range(segs + 1):
        t = i / segs
        x, y = p0[0] + (p1[0] - p0[0]) * t, p0[1] + (p1[1] - p0[1]) * t
        if 0 < i < segs:
            x, y = x + random.uniform(-amp, amp), y + random.uniform(-amp, amp)
        pts.append((x, y))
    d.line(pts, fill=fill, width=width, joint="curve")


def wrap(text, font, max_width):
    lines, cur = [], ""
    for w in text.split():
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=font) <= max_width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    return lines + ([cur] if cur else [])


def center_text(text, font, cx, y, fill):
    d.text((cx - d.textlength(text, font=font) / 2, y), text, font=font, fill=fill)


# ---------- icons ----------
def person(cx, base_y, h, fill=INK, hood=False):
    head_r = h * 0.115
    head_cy = base_y - h + head_r
    body_top, body_bot = head_cy + head_r * 0.75, base_y - h * 0.16
    wt, wb = h * 0.13, h * 0.24
    if hood:
        d.polygon([(cx - head_r * 1.3, head_cy + head_r * 0.5), (cx, head_cy - head_r * 1.5),
                   (cx + head_r * 1.3, head_cy + head_r * 0.5), (cx + head_r * 0.9, head_cy + head_r * 1.1),
                   (cx - head_r * 0.9, head_cy + head_r * 1.1)], fill=fill)
    else:
        d.ellipse([cx - head_r, head_cy - head_r, cx + head_r, head_cy + head_r], fill=fill)
    d.polygon([(cx - wt, body_top), (cx + wt, body_top), (cx + wb, body_bot), (cx - wb, body_bot)], fill=fill)
    d.polygon([(cx - wb * 0.55, body_bot), (cx - wb * 0.05, body_bot), (cx - h * 0.02, base_y),
               (cx - wb * 0.45, base_y)], fill=fill)
    d.polygon([(cx + wb * 0.05, body_bot), (cx + wb * 0.55, body_bot), (cx + wb * 0.45, base_y),
               (cx + h * 0.02, base_y)], fill=fill)


def icon_player(cx, cy):
    person(cx, cy + 50, 110, hood=True)
    d.line([(cx + 22, cy - 50), (cx + 30, cy + 52)], fill=INK, width=5)  # staff


def icon_dm(cx, cy):
    # open book with a quill: the DM's notes
    b = cy + 20
    d.polygon([(cx - 52, b - 6), (cx, b - 22), (cx, b + 28), (cx - 52, b + 40)], fill=INK)
    d.polygon([(cx + 52, b - 6), (cx, b - 22), (cx, b + 28), (cx + 52, b + 40)], fill=INK)
    for k in range(1, 4):
        t = k / 4
        d.line([(cx - 52 + 48 * t, b - 6 + 28 * t), (cx - 4, b - 18 + 40 * t)], fill=PARCH, width=2)
        d.line([(cx + 52 - 48 * t, b - 6 + 28 * t), (cx + 4, b - 18 + 40 * t)], fill=PARCH, width=2)
    d.line([(cx + 36, b - 62), (cx + 10, b - 16)], fill=INK, width=4)
    d.polygon([(cx + 36, b - 62), (cx + 46, b - 52), (cx + 39, b - 47)], fill=INK)


# ---------- title ----------
ink_rect((330, 30, W - 330, 150), width=3, wash=(203, 178, 128))
center_text("The Refused Claim", f_title, W / 2, 35, INK)
center_text("A real exchange from the test runs: the player invents rain, the DM asks instead of narrating",
            f_subtitle, W / 2, 168, INK_SOFT)

# ---------- the four exchanges ----------
ROW_X0, ROW_X1 = 150, W - 150
ICON_W = 150
rows = [
    # (who, label, label_color, kind, content)
    ("player", "THE PLAYER", INK_SOFT, "claim",
     ("It starts pouring outside,", "so I move to a table near the fire.")),
    ("dm", "THE DM  \u00b7  OUT OF CHARACTER", SEAL_RED, "text",
     "It is not raining outside. Only the DM decides what happens in the world. "
     "Do you still want Kael to do this?  I move to a table near the fire."),
    ("player", "THE PLAYER", INK_SOFT, "text", "yes"),
    ("dm", "THE DM  \u00b7  THE STORY GOES ON", INK_SOFT, "text",
     "The firelight catches the edge of your travel-worn cloak as you cross the packed earth, leaving "
     "a faint dusting of ash on the table near the hearth. Grimbold polishes a tankard without looking "
     "up from his ledger ..."),
]
heights = [118, 150, 92, 186]
gap = 34
y = 236
for (who, label, label_color, kind, content), h in zip(rows, heights):
    if who == "player":
        box = (ROW_X0 + ICON_W, y, ROW_X1 - 260, y + h)
        icon_cx = ROW_X0 + ICON_W / 2 - 10
    else:
        box = (ROW_X0 + 260, y, ROW_X1 - ICON_W, y + h)
        icon_cx = ROW_X1 - ICON_W / 2 + 10
    hot = label_color == SEAL_RED
    wash = (212, 176, 128) if hot else (208, 184, 136)
    ink_rect(box, width=3, wash=wash, color=SEAL_RED if hot else INK)
    (icon_player if who == "player" else icon_dm)(icon_cx, y + h / 2 - 8)
    d.text((box[0] + 26, box[1] + 14), label, font=f_label, fill=label_color)
    tx, ty, tw = box[0] + 26, box[1] + 44, box[2] - box[0] - 52
    if kind == "claim":
        claim, rest = content
        d.text((tx, ty), claim, font=f_body_b, fill=SEAL_RED)
        cw = d.textlength(claim, font=f_body_b)
        wobble_line((tx - 4, ty + 17), (tx + cw + 4, ty + 15), segs=8, amp=2, width=3, fill=SEAL_RED)
        d.text((tx + cw + 12, ty), rest, font=f_body, fill=INK)
    else:
        for line in wrap(content, f_body, tw):
            d.text((tx, ty), line, font=f_body, fill=INK)
            ty += 34
    y += h + gap

# ---------- footer ----------
fy = y + 10
ink_rect((200, fy, W - 200, fy + 80), width=3, wash=(203, 178, 128))
center_text("Your character's actions are yours.  The world is the DM's to decide.", f_footer, W / 2, fy + 26, INK)

out_path = __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "refused-claim.png")
img.save(out_path)
print("saved", out_path, "bottom at", fy + 80)
