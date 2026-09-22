import os

OUT = os.path.expanduser("~/portfolio/img")
os.makedirs(OUT, exist_ok=True)

ICONS = {
    "bot": '<rect x="4" y="8" width="16" height="12" rx="2"/><path d="M12 8V4"/><path d="M8 4h8"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M9 13v2"/><path d="M15 13v2"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "landmark": '<line x1="3" x2="21" y1="22" y2="22"/><line x1="6" x2="6" y1="18" y2="11"/><line x1="10" x2="10" y1="18" y2="11"/><line x1="14" x2="14" y1="18" y2="11"/><line x1="18" x2="18" y1="18" y2="11"/><polygon points="12 2 20 7 4 7"/>',
    "terminal": '<polyline points="4 17 10 11 4 5"/><line x1="12" x2="20" y1="19" y2="19"/>',
    "smartphone": '<rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/>',
    "book": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
}

PROJECTS = [
    ("seeks",     "#16f08a", "Seeks", "TALENT DISCOVERY", "users"),
    ("ethiope",   "#0fb8a0", "Ethiope East", "GOVERNMENT PORTAL", "landmark"),
    ("devpulse",  "#f5c518", "DevPulse", "AI DEV AGENT", "terminal"),
    ("dzpatch",   "#ff4d8d", "dzpatch", "EXPO · REACT NATIVE", "smartphone"),
    ("readaloud", "#9a6bff", "readaloud", "FLUTTER · TEXT-TO-SPEECH", "book"),
]

def darker(hexc, f=0.72):
    h = hexc.lstrip('#')
    r, g, b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    return '#%02x%02x%02x' % (int(r*f), int(g*f), int(b*f))

def dots():
    out = []
    for y in range(48, 900, 64):
        for x in range(48, 1200, 64):
            out.append(f'<circle cx="{x}" cy="{y}" r="2" fill="#0a0a0a" opacity="0.10"/>')
    return "".join(out)

for slug, accent, name, role, icon in PROJECTS:
    d = darker(accent)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="900" viewBox="0 0 1200 900">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{accent}"/>
      <stop offset="1" stop-color="{d}"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="900" fill="url(#g)"/>
  {dots()}
  <g transform="translate(940,130)" fill="none" stroke="#0a0a0a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" opacity="0.5">
    <g transform="scale(9)">{ICONS[icon]}</g>
  </g>
  <text x="56" y="770" font-family="JetBrains Mono, ui-monospace, Menlo, monospace" font-size="110" font-weight="800" letter-spacing="-3" fill="#0a0a0a">{name}</text>
  <text x="60" y="832" font-family="ui-monospace, Menlo, monospace" font-size="25" letter-spacing="5" fill="#0a0a0a" opacity="0.7">{role}</text>
</svg>'''
    path = os.path.join(OUT, slug + ".svg")
    with open(path, "w") as f:
        f.write(svg)
    print("wrote", slug + ".svg", os.path.getsize(path), "bytes")
