"""Generates architecture.png: a parchment-and-ink diagram of the current
multi-agent pipeline (orchestrator, fast path, Referee/Router, NPC agent,
Worldbuilder, DM/Narrator, shared World State)."""
import math
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

random.seed(11)
np.random.seed(11)

W, H = 1920, 1700

INK = (43, 30, 20)
INK_SOFT = (78, 58, 40)
SEAL_RED = (110, 28, 22)

FONT_DIR = "C:/Windows/Fonts/"
f_title = ImageFont.truetype(FONT_DIR + "OLDENGL.TTF", 72)
f_subtitle = ImageFont.truetype(FONT_DIR + "BOOKOSI.TTF", 25)
f_node_title = ImageFont.truetype(FONT_DIR + "BOOKOSB.TTF", 23)
f_node_sub = ImageFont.truetype(FONT_DIR + "BOOKOSI.TTF", 17)
f_small = ImageFont.truetype(FONT_DIR + "BOOKOSI.TTF", 16)
f_footer = ImageFont.truetype(FONT_DIR + "BOOKOSB.TTF", 22)


def make_parchment(w, h):
    base = np.array([214, 190, 143], dtype=np.float32)
    img = np.ones((h, w, 3), dtype=np.float32) * base
    yy, xx = np.mgrid[0:h, 0:w]
    for _ in range(16):
        cx, cy = random.uniform(0, w), random.uniform(0, h)
        rx, ry = random.uniform(w * 0.15, w * 0.4), random.uniform(h * 0.15, h * 0.4)
        strength = random.uniform(8, 22)
        d2 = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2
        falloff = np.clip(1 - d2, 0, 1) ** 2
        img -= (falloff * strength)[:, :, None]
    noise = np.random.normal(0, 6, (h, w, 1))
    img += noise
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

for _ in range(300):
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


def wobble_line(p0, p1, segs=10, amp=3, width=3, fill=INK, arrow=True):
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
    if arrow:
        ang = math.atan2(y1 - pts[-2][1], x1 - pts[-2][0])
        for side in (0.5, -0.5):
            a2 = ang + math.pi + side
            d.line([(x1, y1), (x1 + 11 * math.cos(a2), y1 + 11 * math.sin(a2))], fill=fill, width=width)


# ---------- compact icons ----------
def icon_player(cx, cy):
    r = 16
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=INK)
    d.polygon([(cx - 20, cy + 24), (cx + 20, cy + 24), (cx + 13, cy + 64), (cx - 13, cy + 64)], fill=INK)


def icon_fork(cx, cy):
    d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=INK)
    d.line([(cx, cy), (cx, cy + 20)], fill=INK, width=5)
    wobble_line((cx, cy + 20), (cx - 30, cy + 48), segs=4, amp=2, width=5)
    wobble_line((cx, cy + 20), (cx + 30, cy + 48), segs=4, amp=2, width=5)


def icon_lightning(cx, cy):
    pts = [(cx - 6, cy - 34), (cx + 10, cy - 34), (cx - 2, cy - 2), (cx + 12, cy - 2),
           (cx - 12, cy + 34), (cx - 2, cy + 2), (cx - 16, cy + 2)]
    d.polygon(pts, fill=SEAL_RED)


def icon_scale(cx, cy):
    d.line([(cx, cy - 32), (cx, cy + 22)], fill=INK, width=5)
    d.line([(cx - 34, cy - 22), (cx + 34, cy - 22)], fill=INK, width=4)
    d.ellipse([cx - 6, cy - 38, cx + 6, cy - 26], outline=INK, width=3)
    for sx in (-34, 34):
        d.line([(cx + sx, cy - 22), (cx + sx - 14, cy + 4)], fill=INK, width=2)
        d.line([(cx + sx, cy - 22), (cx + sx + 14, cy + 4)], fill=INK, width=2)
        d.arc([cx + sx - 16, cy - 2, cx + sx + 16, cy + 18], 10, 170, fill=INK, width=3)
    d.line([(cx - 24, cy + 22), (cx + 24, cy + 22)], fill=INK, width=5)


def icon_dialogue(cx, cy):
    for ox in (-20, 20):
        d.rounded_rectangle([cx + ox - 22, cy - 18, cx + ox + 22, cy + 10], radius=8, outline=INK, width=3)
    d.polygon([(cx - 26, cy + 8), (cx - 14, cy + 8), (cx - 22, cy + 20)], fill=INK)
    d.polygon([(cx + 14, cy + 8), (cx + 26, cy + 8), (cx + 20, cy + 20)], fill=INK)


def icon_book(cx, cy):
    d.polygon([(cx - 36, cy - 14), (cx, cy - 28), (cx, cy + 22), (cx - 36, cy + 34)], fill=INK)
    d.polygon([(cx + 36, cy - 14), (cx, cy - 28), (cx, cy + 22), (cx + 36, cy + 34)], fill=INK)
    for k in range(1, 4):
        t = k / 4
        d.line([(cx - 36 + 34 * t, cy - 14 + 24 * t), (cx - 3, cy - 24 + 28 * t)], fill=(214, 190, 143), width=1)
        d.line([(cx + 36 - 34 * t, cy - 14 + 24 * t), (cx + 3, cy - 24 + 28 * t)], fill=(214, 190, 143), width=1)


def icon_quill(cx, cy):
    d.line([(cx + 16, cy - 32), (cx - 14, cy + 30)], fill=INK, width=4)
    d.polygon([(cx + 16, cy - 32), (cx + 24, cy - 20), (cx + 2, cy - 10),
               (cx - 10, cy - 2), (cx + 2, cy - 18)], fill=INK)
    d.ellipse([cx - 18, cy + 26, cx - 8, cy + 36], fill=INK)


def icon_ledger(cx, cy):
    d.rectangle([cx - 46, cy - 40, cx + 46, cy + 40], outline=INK, width=3)
    d.line([(cx, cy - 40), (cx, cy + 40)], fill=INK, width=2)
    for yy in (-24, -8, 8, 24):
        d.line([(cx - 36, cy + yy), (cx - 8, cy + yy)], fill=INK_SOFT, width=1)
        d.line([(cx + 8, cy + yy), (cx + 36, cy + yy)], fill=INK_SOFT, width=1)


def draw_node(box, icon_fn, icon_y, title, subtitle_lines, title_y, line_h=23, wash=(208, 184, 136)):
    x0, y0, x1, y1 = box
    ink_rect(box, width=3, wash=wash)
    cx = (x0 + x1) / 2
    if icon_fn:
        icon_fn(cx, icon_y)
    ty = title_y
    for line in wrap(title, f_node_title, (x1 - x0) - 30):
        center_text(line, f_node_title, cx, ty, INK)
        ty += 28
    ty += 6
    for line in subtitle_lines:
        center_text(line, f_node_sub, cx, ty, INK_SOFT)
        ty += line_h


# ---------- title banner ----------
banner_box = (260, 30, W - 260, 150)
ink_rect(banner_box, width=3, wash=(203, 178, 128))
d.line([(280, 40), (240, 55)], fill=INK, width=3)
d.line([(W - 280, 40), (W - 240, 55)], fill=INK, width=3)
center_text("The Architecture", f_title, W / 2, 35, INK)
center_text("Five working pieces, one shared memory, and a fast path for the easy turns",
            f_subtitle, W / 2, 172, INK_SOFT)

MAIN_CX = 650

# PLAYER
player_box = (MAIN_CX - 160, 220, MAIN_CX + 160, 405)
draw_node(player_box, icon_player, 255, "PLAYER", ["types an action into the CLI"], 328)

wobble_line((MAIN_CX, 405), (MAIN_CX, 430))

# ORCHESTRATOR
orch_box = (MAIN_CX - 240, 430, MAIN_CX + 240, 610)
draw_node(orch_box, icon_fork, 470, "ORCHESTRATOR",
          ["deterministic Python,", "picks what this turn needs"], 513)

FAST_CX = 310
REF_CX = 960
wobble_line((MAIN_CX - 60, 610), (FAST_CX, 660))
wobble_line((MAIN_CX + 60, 610), (REF_CX, 660))

# FAST PATH
fast_box = (FAST_CX - 160, 660, FAST_CX + 160, 870)
draw_node(fast_box, icon_lightning, 714, "FAST PATH",
          ["sentence embeddings judge it", "low-risk, skips the Referee call"], 760)

# REFEREE + ROUTER
ref_box = (REF_CX - 200, 660, REF_CX + 200, 910)
draw_node(ref_box, icon_scale, 710, "RULES REFEREE + ROUTER",
          ["turn_type \u00b7 addresses_npc", "scene_shift \u00b7 known_to_dm",
           "same call judges outcome + twist"], 766)
center_text('a "/dm" turn always forces this path', f_small, REF_CX, 878, INK_SOFT)

NPC_CX = 800
WB_CX = 1180
wobble_line((REF_CX - 40, 910), (NPC_CX + 15, 975))
wobble_line((REF_CX + 40, 910), (WB_CX - 15, 975))
center_text("only if flagged \u2014 run concurrently", f_small, (NPC_CX + WB_CX) / 2, 950, INK_SOFT)

# NPC AGENT
npc_box = (NPC_CX - 150, 980, NPC_CX + 150, 1170)
draw_node(npc_box, icon_dialogue, 1026, "NPC AGENT",
          ["own persona, own memory", "only if this NPC is addressed"], 1070)

# WORLDBUILDER
wb_box = (WB_CX - 150, 980, WB_CX + 150, 1170)
draw_node(wb_box, icon_book, 1026, "WORLDBUILDER",
          ["invents lore that fits", "auto-triggered, or /worldbuild"], 1070)

# converge into DM
dm_box = (MAIN_CX - 240, 1230, MAIN_CX + 240, 1420)
wobble_line((FAST_CX, 870), (MAIN_CX - 160, 1230), amp=4)
wobble_line((NPC_CX, 1170), (MAIN_CX - 15, 1230), amp=3)
wobble_line((WB_CX, 1170), (MAIN_CX + 160, 1230), amp=3)

draw_node(dm_box, icon_quill, 1280, "DM / NARRATOR",
          ["streams the reply live",
           "TIGHT by default, FULL SCENE on a real shift"], 1326)

wobble_line((MAIN_CX, 1420), (MAIN_CX, 1470))
center_text("back to the player, streamed live, one token at a time", f_subtitle, MAIN_CX, 1478, INK_SOFT)

# ---------- World State side panel ----------
ws_box = (1430, 430, 1860, 1420)
ink_rect(ws_box, width=3, wash=(203, 178, 128))
ws_cx = (ws_box[0] + ws_box[2]) / 2
icon_ledger(ws_cx, 500)
center_text("WORLD STATE", f_node_title, ws_cx, 560, INK)
for i, line in enumerate(["location \u00b7 scene summary", "known NPCs \u00b7 established facts", "recent turn history"]):
    center_text(line, f_node_sub, ws_cx, 596 + i * 24, INK_SOFT)

d.line(jitter_points((ws_box[0] + 30, 684, ws_box[2] - 30, 686), step=18, amp=1.5), fill=INK_SOFT, width=1)

for i, line in enumerate([
    "shared memory, not chat history \u2014",
    "every agent reads this each turn,",
    "the DM's reply writes back into it",
]):
    center_text(line, f_node_sub, ws_cx, 712 + i * 24, INK_SOFT)

# connectors from each agent box into the World State panel (land in the
# empty lower portion of the panel, well clear of the text block above).
# ref/wb/dm connect straight across -- nothing else sits between them and
# the panel. npc sits to the LEFT of wb, so its direct line would cut
# through wb's box; instead it ticks down into the empty gap below the
# npc/wb row (clear of wb, whose bottom edge is above that gap) and
# travels under wb to reach the panel.
for box, cy in ((ref_box, 830), (wb_box, 1075), (dm_box, 1340)):
    bx1 = box[2]
    by = (box[1] + box[3]) / 2
    wobble_line((bx1, by), (ws_box[0], cy), segs=6, amp=2.5, width=2, fill=INK_SOFT, arrow=False)

npc_cx = (npc_box[0] + npc_box[2]) / 2
wobble_line((npc_cx, npc_box[3]), (npc_cx, 1200), segs=3, amp=1.5, width=2, fill=INK_SOFT, arrow=False)
wobble_line((npc_cx, 1200), (ws_box[0], 1200), segs=8, amp=2.5, width=2, fill=INK_SOFT, arrow=False)

# ---------- footer ----------
foot_box = (260, 1560, W - 260, 1650)
ink_rect(foot_box, width=3, wash=(203, 178, 128))
center_text("Built with Ollama \u00b7 ministral-3:8b \u00b7 sentence-transformers \u2014 all local, no paid APIs",
            f_footer, W / 2, 1592, INK)

out_path = "C:/Users/Eduardo Braga/Projects/ai-dungeon-master/posts/assets/architecture.png"
img.convert("RGB").save(out_path)
print("saved", out_path)
