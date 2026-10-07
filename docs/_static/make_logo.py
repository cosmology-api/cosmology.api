# /// script
# requires-python = ">=3.11"
# dependencies = ["resvg-py"]
# ///
# Copyright (c) 2022, Nathaniel Starkman and Nicolas Tessore
"""Draw the cosmology.api logo: the cosmology-api organisation's mark.

A hexagon holding three linked cubes, as on the organisation's avatar, in its
near-white on slate. The cubes are drawn larger than on the avatar so they stay
legible as a favicon. The shapes are vector, so the logo is written as an SVG,
sharp at any size; for a bitmap, name a .png and give its size::

    uv run docs/_static/make_logo.py                     # favicon.svg
    uv run docs/_static/make_logo.py --size 2048 big.png
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

SLATE, WHITE = "#303841", "#f3f3f3"  # the organisation avatar's colours

# In a 64-unit square, all hexagons pointy-topped and centred on CENTRE. The
# outer hexagon's radius and line width; the links' hexagon, which holds a cube
# on every other corner, its radius; each cube's radius; and the inner lines'
# width.
CENTRE = 32
OUTER, OUTER_WIDTH = 25, 2.8
LINKS, CUBE, INNER_WIDTH = 13.5, 6.2, 2.0
CUBES = (0, 2, 4)  # which of the links' corners hold a cube: top, lower right, left

SVG = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="512" height="512">
  <rect width="64" height="64" rx="14" fill="{slate}"/>
  <g fill="none" stroke="{white}" stroke-linejoin="round">
    <path d="{outer}" stroke-width="{outer_width:g}" stroke-linejoin="miter"/>
    <path d="{links}" stroke-width="{inner_width:g}"/>
  </g>
  <path d="{cube_backs}" fill="{slate}"/>
  <path d="{cubes}" fill="none" stroke="{white}" stroke-width="{inner_width:g}"
    stroke-linejoin="round"/>
</svg>
"""


def corners(x: float, y: float, r: float) -> list[tuple[float, float]]:
    """Return a pointy-topped hexagon's corners, clockwise from the top."""
    return [
        (x + r * math.cos(math.radians(-90 + 60 * k)),
         y + r * math.sin(math.radians(-90 + 60 * k)))
        for k in range(6)
    ]  # fmt: skip


def outline(points: list[tuple[float, float]]) -> str:
    """Return a closed SVG path through ``points``."""
    return "M" + "L".join(f"{x:.2f} {y:.2f}" for x, y in points) + "Z"


def cube(x: float, y: float) -> str:
    """Return a cube at ``x``, ``y``: its outline, and the Y of its three edges."""
    c = corners(x, y, CUBE)
    edges = "".join(f"M{x:.2f} {y:.2f}L{c[k][0]:.2f} {c[k][1]:.2f}" for k in (5, 1, 3))
    return outline(c) + edges


def svg() -> str:
    """Return the logo as SVG text."""
    links = corners(CENTRE, CENTRE, LINKS)
    return SVG.format(
        slate=SLATE,
        white=WHITE,
        outer=outline(corners(CENTRE, CENTRE, OUTER)),
        outer_width=OUTER_WIDTH,
        links=outline(links),
        # Each cube is backed with the slate, so the links stop at its edge.
        cube_backs="".join(outline(corners(*links[k], CUBE)) for k in CUBES),
        cubes="".join(cube(*links[k]) for k in CUBES),
        inner_width=INNER_WIDTH,
    )


def main() -> None:
    """Parse the command line and save the logo."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "out",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("favicon.svg"),
        help="output file, SVG or PNG by its extension (default: favicon.svg)",
    )
    parser.add_argument(
        "--size", type=int, default=512, help="pixels per side, for a PNG"
    )
    args = parser.parse_args()

    if args.out.suffix == ".svg":
        args.out.write_text(svg())
    else:
        import resvg_py  # noqa: PLC0415  # only a PNG needs a renderer

        png = resvg_py.svg_to_bytes(svg_string=svg(), width=args.size)
        args.out.write_bytes(bytes(png))


if __name__ == "__main__":
    main()
