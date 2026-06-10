# ⚔️ SHINGEKI NO KYOJIN — The Complete Lore Encyclopedia

<div align="center">

![Status](https://img.shields.io/badge/STATUS-ACTIVE-red?style=for-the-badge&labelColor=0e0d0b&color=801414)
![Version](https://img.shields.io/badge/VERSION-V4.81-gold?style=for-the-badge&labelColor=0e0d0b&color=c8a96e)
![Clearance](https://img.shields.io/badge/CLEARANCE-ALPHA%20EYES%20ONLY-darkred?style=for-the-badge&labelColor=0e0d0b&color=4a1010)
![Tech](https://img.shields.io/badge/BUILT%20WITH-HTML%20CSS%20JS-white?style=for-the-badge&labelColor=0e0d0b)

</div>

<br/>

> *"They took everything. Our land. Our history. Our names.*
> *One boy remembered. One boy saw it all coming."*

<br/>

---

## 🏰 WHAT IS THIS

**Shingeki No Kyojin — The AoT Encyclopedia** is a cinematic, lore-first encyclopedia for *Attack on Titan* — built for people who've watched every episode, read every chapter, and still want to go deeper.

This is not a fan wiki. This is not a marketing page.

This is a **classified military intelligence archive** — designed to feel like you broke into a Marleyan database and found everything they tried to hide. Every section is a dossier. Every interaction has weight. Every pixel was a deliberate choice.

If you're a new watcher, turn back. **Full spoilers. No mercy.**

---

## ⚡ FEATURES

### 🗂️ The Archive Sections
| Section | What's Inside |
|---|---|
| **THE FALL OF HISTORY** | Full AoT timeline from Year 1 to the Rumbling — alternating dossier cards with classified stamps |
| **THE THREE WALLS** | Wall Maria, Rose & Sina — full lore breakdown with aerial map backdrop |
| **THE NINE POWERS** | All 9 titan shifters — flip cards with grayscale-to-color hover glow, inheritor chains, danger ratings |
| **POWERS AT WAR** | All major factions — Survey Corps, Warriors, Yeagerists, Tyburs and more |
| **THE SOLDIERS** | Character dossiers — arc summaries, affiliations, and fates. Brutally honest. |
| **CRITICAL CAMPAIGNS** | The battles that changed everything — Shiganshina, Liberio, the Rumbling |
| **THE CONSOLE** | A fully functional CRT terminal — type commands to decrypt classified intel |
| **CLASSIFIED INTEL** | Dark lore facts most watchers missed — click to declassify |
| **SCALE OF TERROR** | Animated titan size comparison chart — from 3m pure titans to Eren's 200m+ final form |
| **THE RUMBLING** | A fullscreen horror sequence — Eren's face, 1.6 billion casualties, the typewriter quote |
| **TEST YOUR INTEL** | 10-question lore quiz with military rank assignment at the end |

---

### 🎮 Interactions Worth Seeing
- **CRT Terminal Console** — real command parser with `help`, `status`, `decrypt basement`, `decrypt path` and more. Decrypting triggers image embeds and classified documents inside the terminal.
- **Nine Titans Flip Cards** — hover instantly de-greys the titan art with a color glow, then after exactly 500ms the card flips to show full specs. The timing is deliberate.
- **The Rumbling Onslaught** — click the widget, the screen shakes, a cubic ease-out counter races to **1,600,000,000**, then a fullscreen horror overlay takes over with Eren's face and a typewriter speech. One of a kind interaction.
- **Scroll-triggered Timeline** — the history line draws itself as you scroll down through the years.
- **Scale Chart** — titan height bars animate in with a staggered wave the moment the section hits your viewport.
- **Declassify Cards** — click any lore fact card to remove the redaction stamp and reveal the truth.

---

## 🎨 DESIGN SYSTEM

Built on a **restricted military tactical intelligence** aesthetic. Cold, dark, deliberate.

```
Background:   #050505   — absolute dark
Cards:        #0e0d0b   — barely visible surface
Gold:         #c8a96e   — Survey Corps authority
Red:          #801414   — danger, combat, blood
Bright Red:   #ff1a1a   — critical alarms, horror
Text:         #e2dcd0   — warm parchment readability
```

**Typography:**
- `Outfit` — geometric command-center headers
- `JetBrains Mono` — terminal logs, telemetry data, classified tags

---

## 🛠️ TECH STACK

Pure vanilla. No frameworks. No dependencies. Just the fundamentals pushed to their limit.

```
HTML5       — semantic structure
CSS3        — custom properties, keyframes, transforms, GPU compositing
JavaScript  — DOM manipulation, requestAnimationFrame, IntersectionObserver
Google Fonts — Outfit + JetBrains Mono
```

### Under The Hood
- `requestAnimationFrame` + cubic ease-out curve for the 1.6B count-up animation
- `IntersectionObserver` for scroll-triggered bar chart with 80ms stagger
- `will-change: opacity` on the horror overlay for GPU-layer isolation — zero frame drops
- CRT scanline effect via `repeating-linear-gradient` at 3px intervals
- Phosphor flicker via high-frequency `opacity` keyframe (0.15s infinite)
- Dual-phase hover timing on titan cards — instant color, 500ms flip delay
- Fixed height pre-allocation on all dynamic containers — no layout shifts

---

## 🚀 GETTING STARTED

No build step. No npm install. No config.

```bash
git clone https://github.com/H8rsh100/aot-encyclopedia
cd aot-encyclopedia
# open index.html in your browser
```

Or just visit the live site → **[GitHub Pages Link]**

---

## 📟 TERMINAL COMMANDS

Open the **THE CONSOLE** section and try these:

```
help           → lists all available commands
status         → current archive operational status  
campaigns      → lists critical military campaigns
wall_status    → structural integrity of all three walls
decrypt basement → unlocks Grisha's basement files
decrypt path   → reveals the path of the titans
rumbling       → initiates the onslaught sequence
clear          → wipes the terminal output
```

---

## 🎖️ QUIZ RANKS

Complete the 10-question intel evaluation to receive your rank:

| Score | Rank |
|---|---|
| 0–3 | Civilian — *You know nothing beyond the walls* |
| 4–6 | Garrison Soldier — *You've read the basics* |
| 7–8 | Survey Corps — *You've been beyond the walls* |
| 9–10 | Humanity's Strongest — *You know the truth of this world* |

---

## 📁 PROJECT STRUCTURE

```
aot-encyclopedia/
├── index.html          # entire site — single file
├── assets/
│   ├── hor.jpg         # Eren horror overlay
│   └── ...             # titan art, wall maps, backgrounds
└── README.md
```

---

## 🩸 BUILT BY

Made with obsession, lore knowledge, and zero sleep.

> *"If you win, you live. If you lose, you die. If you don't fight, you can't win."*
> — Eren Yeager

---

<div align="center">

**[ SNK ARCHIVE — CLASSIFIED ]**

*Dedicate Your Heart.*

![Footer](https://img.shields.io/badge/SURVEY%20CORPS-RESTRICTED%20ARCHIVE%20YEAR%20854-red?style=for-the-badge&labelColor=050505&color=801414)

</div>
