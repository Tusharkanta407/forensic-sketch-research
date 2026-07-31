import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon
from pathlib import Path

out = Path(r"d:\Forensic-Sketch-Generator\docs\interim-review\figures")
out.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots(figsize=(8.5, 11), dpi=220)
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis("off")
fig.patch.set_facecolor("white")
ax.set_facecolor("white")


def box(x, y, w, h, text, lw=1.4):
    p = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        linewidth=lw,
        edgecolor="black",
        facecolor="white",
    )
    ax.add_patch(p)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=9,
        color="black",
        family="DejaVu Sans",
    )


def diamond(cx, cy, w, h, text):
    pts = [(cx, cy + h / 2), (cx + w / 2, cy), (cx, cy - h / 2), (cx - w / 2, cy)]
    poly = Polygon(pts, closed=True, linewidth=1.4, edgecolor="black", facecolor="white")
    ax.add_patch(poly)
    ax.text(cx, cy, text, ha="center", va="center", fontsize=8, color="black")


def arrow(x1, y1, x2, y2):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->", color="black", lw=1.2),
    )


ax.text(
    5,
    13.5,
    "Figure 1. Proposed System Architecture",
    ha="center",
    va="center",
    fontsize=12,
    fontweight="bold",
    color="black",
)
ax.text(
    5,
    13.05,
    "AI-Assisted Forensic Sketch Generation Framework",
    ha="center",
    va="center",
    fontsize=9,
    color="black",
)

box(2.2, 11.5, 5.6, 0.95, "Module A\nInteractive Forensic Interview Agent")
box(2.2, 10.0, 5.6, 0.95, "Module B\nFace Feature Profile Builder")
box(2.2, 8.5, 5.6, 0.95, "Module C\nControllable Face Composer")
box(2.2, 7.0, 5.6, 0.95, "Module D\nForensic Sketch Renderer")
diamond(5, 5.7, 3.2, 1.0, "Witness\nApproved?")
box(0.4, 3.9, 3.4, 0.95, "Module E\nGuided Refinement Interview")
box(6.2, 3.9, 3.4, 0.95, "Final Forensic Sketch")
box(2.2, 1.8, 5.6, 0.95, "Optional Validation Layer\n(Identity / Quality Metrics)")

arrow(5, 11.5, 5, 10.95)
arrow(5, 10.0, 5, 9.45)
arrow(5, 8.5, 5, 7.95)
arrow(5, 7.0, 5, 6.2)

ax.annotate(
    "",
    xy=(2.1, 4.85),
    xytext=(3.6, 5.4),
    arrowprops=dict(arrowstyle="->", color="black", lw=1.2),
)
ax.text(2.55, 5.35, "No", fontsize=8, color="black")
ax.annotate(
    "",
    xy=(7.9, 4.85),
    xytext=(6.4, 5.4),
    arrowprops=dict(arrowstyle="->", color="black", lw=1.2),
)
ax.text(7.1, 5.35, "Yes", fontsize=8, color="black")

ax.plot([2.1, 1.5], [4.37, 4.37], color="black", lw=1.2)
ax.plot([1.5, 1.5], [4.37, 10.45], color="black", lw=1.2)
ax.annotate(
    "",
    xy=(2.2, 10.45),
    xytext=(1.5, 10.45),
    arrowprops=dict(arrowstyle="->", color="black", lw=1.2),
)
ax.text(0.2, 7.4, "Attribute\nupdates", fontsize=7, color="black", rotation=90, va="center")

ax.annotate(
    "",
    xy=(5, 2.75),
    xytext=(7.9, 3.9),
    arrowprops=dict(arrowstyle="->", color="black", lw=1.0, linestyle="dashed"),
)
ax.text(7.15, 3.15, "research only", fontsize=7, style="italic", color="black")

ax.text(
    5,
    0.7,
    "Black-and-white architectural diagram for Interim Review documentation",
    ha="center",
    fontsize=7,
    color="black",
)

bw = out / "figure1-system-architecture-bw.png"
fig.savefig(bw, bbox_inches="tight", facecolor="white", edgecolor="none")
plt.close()
print("saved", bw)
