#!/usr/bin/env python3
"""Build the minimal Portuguese image timeline from the capture manifest."""

import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "projects/portfolio-evolution"
data = json.loads((CASE / "timeline.json").read_text())
asset = "../../public/images/cases/portfolio-evolution/"
visual = {
    "338d3e6",
    "df69626",
    "db2f11a",
    "965b240",
    "8c59af2",
    "585f05b",
    "cfa01e6",
    "d5d556e",
    "8c79505",
    "763e258",
    "4771bec",
    "a95c60c",
    "e41a75e",
    "594104f",
    "b18b050",
    "7507658",
    "3cd2208",
}


def preview(entry, device, label):
    images = entry["images"]
    description = escape(f"Home em português — {entry['title']}, {label}")
    return f'''<figure class="evolution-{device}"><a class="figure-image-link" href="{asset}{images[device]}" target="_blank" rel="noopener" aria-label="Ampliar: {description}"><img src="{asset}{images[device + "Viewport"]}" width="{1440 if device == "desktop" else 390}" height="{1000 if device == "desktop" else 844}" loading="lazy" alt="{description}"></a></figure>'''


items = []
for entry in data["commits"]:
    if entry["sha"][:7] not in visual:
        continue
    captures = "".join(
        preview(view, "desktop", "desktop") for view in entry.get("themes", [entry])
    )
    items.append(
        f'<li class="evolution-step"><div class="evolution-captures">{captures}</div></li>'
    )

references = "".join(
    f'''<figure class="evolution-{device} evolution-reference"><a class="figure-image-link" href="{asset}2026-09-14-c623256-reference-{device}.webp" target="_blank" rel="noopener" aria-label="Ampliar referência inicial de design, {label}"><img src="{asset}2026-09-14-c623256-reference-{device}.webp" loading="lazy" alt="Referência inicial de design da home, {label}; não é uma captura do site"></a></figure>'''
    for device, label in [("desktop", "desktop")]
)
def render_timeline():
    return f'<li class="evolution-step"><div class="evolution-captures">{references}</div></li>\n' + "".join(items)


if __name__ == "__main__":
    from build_site import main
    main()
