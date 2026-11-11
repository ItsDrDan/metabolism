#!/usr/bin/env python3
"""Assemble a CHEM 3B study game from the Metabolic Marathon engine (metabolism/index.html) plus a content.js
and a small config. Usage: python3 build_game.py <gamedir>  (reads <gamedir>/config.json and <gamedir>/content.js)"""
import json, re, sys, os
gd = sys.argv[1]
cfg = json.load(open(os.path.join(gd, 'config.json')))
content = open(os.path.join(gd, 'content.js')).read()
s = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'index.html')).read()  # the engine next to this tools/ folder

def rep(old, new, count=1):
    global s
    assert old in s, old[:60]
    s = s.replace(old, new, count)

rep('<title>Metabolic Marathon • ItsDrDan • CHEM 3B</title>', f'<title>{cfg["title"]} • ItsDrDan • CHEM 3B</title>')
s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{cfg["desc"]}">', s)
s = re.sub(r'<link rel="icon" href="[^"]*">', f'<link rel="icon" href="{cfg["favicon"]}">', s)
# hero
s = re.sub(r'<svg viewBox="0 0 200 200" aria-hidden="true">.*?</svg></div>', cfg['logo_svg'] + '</div>', s, flags=re.S)
rep('<span class="badge">⚡ Metabolic Marathon • ItsDrDan • CHEM 3B</span>', f'<span class="badge">{cfg["icon"]} {cfg["title"]} • ItsDrDan • CHEM 3B</span>')
rep('<h1><span class="a">Metabolic</span> <span class="b">Marathon</span></h1>', cfg['h1'])
rep('<p class="subtitle">Glycolysis to the urea cycle: order the pathways, count the ATP, name the reactions, and follow the fuel.</p>', f'<p class="subtitle">{cfg["subtitle"]}</p>')
s = re.sub(r'<p style="margin:0 18px 12px"><strong>Tip:</strong>.*?</p>', f'<p style="margin:0 18px 12px"><strong>Tip:</strong> {cfg["tip"]}</p>', s, flags=re.S)
# reference + videos
s = re.sub(r'<details class="card collapsible"><summary>🧠 Reference: pathway scorecard</summary>.*?</details>', cfg['reference'], s, flags=re.S)
s = re.sub(r'<div class="vidlist">.*?</div>', cfg['videos'], s, flags=re.S)
rep('Chapters 13–15.</p></details>', cfg['chapters'] + '.</p></details>')
s = re.sub(r'<p class="footer-note">Practice topics follow CHEM 3B Chapters 13.*?</p>', f'<p class="footer-note">{cfg["source_note"]}</p>', s, flags=re.S)
# content JS
a = s.index('/* ===== 1. Pathway Order ===== */'); b = s.index('/* ===== modes, state, journey ===== */')
s = s[:a] + content + '\n' + s[b:]
# modes / gen / badges
s = re.sub(r'const MODES=\[.*?\n\];', cfg['modes_js'], s, flags=re.S)
s = re.sub(r'const GEN=\{[^}]*\};', cfg['gen_js'], s)
rep("const JKEY='itsdrdan-metabolism-journey-v1';", f"const JKEY='itsdrdan-{cfg['id']}-journey-v1';")
s = re.sub(r'const BADGES=\[.*?\n\];', cfg['badges_js'], s, flags=re.S)
rep("game:'metabolism'", f"game:'{cfg['id']}'", 2)
rep("const state={mode:'order',", f"const state={{mode:'{cfg['first_mode']}',")
rep("bank/metabolism.json", f"bank/{cfg['bank']}.json")
rep("topics:[['metabolism','Metabolism','⚡']]", f"topics:[{cfg['topics']}]")
rep("storageKey:'itsdrdan-metabolism-exam-v1'", f"storageKey:'itsdrdan-{cfg['id']}-exam-v1'")
rep("Loading the Final Boss metabolism questions", f"Loading the Final Boss {cfg['bank_label']} questions")
# mode colors (CSS)
s = re.sub(r'\.mode-btn\[data-mode=order\].*?\.mode-btn\[data-mode=exam\]\{--md:#4b57d1;--mb:#eef0fe\}', cfg['mode_css'], s, flags=re.S)
s = re.sub(r'#practice\[data-mode=order\].*?#practice\[data-mode=exam\]\{--md:#4b57d1\}', cfg['practice_css'], s, flags=re.S)
rep('<h2 class="mode-title" id="modeTitle">Pathway Order</h2>', f'<h2 class="mode-title" id="modeTitle">{cfg["first_mode_title"]}</h2>')
# mascot faces (optional override)
if cfg.get('faces_js'):
    s = re.sub(r'const LGFACE=\{.*?\n\};', cfg['faces_js'], s, flags=re.S)
open(os.path.join(gd, 'index.html'), 'w').write(s)
print(gd, len(s))
