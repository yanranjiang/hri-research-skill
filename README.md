# HRI Research Skill for Claude Code

A Claude Code skill that **autonomously generates complete HRI study protocols** from a research scenario description, and guides you through the full study lifecycle from question formulation to statistical reporting.

Grounded in:
> Tian, L., Wu, T. L. Y., Robinson, N. L., Carreno-Medrano, P., Chan, W. P., Sakr, M., Abdi, E., Croft, E. A., & Kulić, D. (2024). *Experimental Methodology for Human-Robot Interaction: Guidelines and Case Studies for Human-Centred and Ethical Robotics Research*. CRC Press, Taylor & Francis Group.

---

## What's New in v2.0 — Auto-Design Mode

Type `/hri-research` and describe your study. The agent **autonomously generates a complete protocol workspace**:

```
my-study/
├── research-question.md    ← PICO framework + testable hypotheses
├── study-design.md         ← design type, conditions, counterbalancing
├── power-analysis.py       ← runnable Python: compute N + attrition buffer
├── instruments.md          ← validated questionnaires + admin schedule
├── analysis-plan.md        ← statistical tests + Python snippets
├── ethics-checklist.md     ← HREC/IRB + HRI-specific risk mitigations
├── data-collection/
│   ├── session-script.md   ← minute-by-minute experimenter guide
│   └── debrief.md
└── study-protocol.md       ← compiled full protocol
```

No step-by-step prompting needed — the agent works autonomously and produces a `progress-report.html` for you to review and redirect.

---

## Interactive Web Demo

Try the HRI Study Design Assistant in your browser — paste your research scenario and get a complete study protocol generated stage by stage via Claude API.

### Run locally

```bash
cd demo
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
streamlit run app.py
```

### Deploy to Streamlit Cloud (free)

1. Fork this repo
2. Go to [share.streamlit.io](https://share.streamlit.io) → New app
3. Set **Main file path**: `demo/app.py`
4. Add `ANTHROPIC_API_KEY` in the Secrets panel
5. Deploy

---

## Claude Code Skill Usage

### Installation

**Option A — Copy directly**

```bash
mkdir -p ~/.claude/skills/hri-research
cp SKILL.md ~/.claude/skills/hri-research/SKILL.md
```

**Option B — Clone**

```bash
git clone https://github.com/yanranjiang/hri-research-skill.git
mkdir -p ~/.claude/skills/hri-research
cp hri-research-skill/SKILL.md ~/.claude/skills/hri-research/SKILL.md
```

### Usage — Auto-Design Mode (v2.0)

```
/hri-research
I want to study how shared autonomy affects trust and workload for mining
operators controlling a Spot robot in search-and-rescue.
```

The agent will create a study workspace and generate all protocol files autonomously.

**For long sessions**, set up `/loop` for agent continuity:

```
/loop
Continue the HRI study design. Read study-state.yaml to find the current stage,
complete it, write the file, mark it complete, then move to the next stage.
Stop when all stages are complete and progress-report.html is generated.
```

### Usage — Advisory Mode

Ask specific methodology questions:

```
/hri-research
I have EDA, HRV, NASA-TLX, and robot logs from 18 participants across 3 conditions.
How do I synchronise and fuse these streams before running statistics?
```

```
/hri-research
Two raters coded takeover behaviour from video. How do I check inter-rater
reliability before running my main analysis?
```

```
/hri-research
I want to test whether trust mediates the relationship between autonomy level
and intervention frequency. Show me the Python for this.
```

---

## Skill Coverage

| Stage | Auto-Design output | Advisory content |
|---|---|---|
| 1. Research Question | `research-question.md` | PICO framework, hypothesis formulation |
| 2. Study Design | `study-design.md` | Within/between/mixed, counterbalancing, IVs & DVs |
| 3. Power Analysis | `power-analysis.py` | Python code, effect size guidance |
| 4. Instruments | `instruments.md` | SUS, NASA-TLX, trust scales, physiological sensors |
| 5. Statistical Analysis | `analysis-plan.md` | LMM, mediation, Bayesian, DTW, change-point |
| 6. Ethics | `ethics-checklist.md` | HREC/IRB, HRI risk mitigations |
| 7. Session Script | `data-collection/session-script.md` | Session structure, WoZ protocols |
| 8. Full Protocol | `study-protocol.md` + `progress-report.html` | CONSORT reporting, venue guide |

Plus HRI-specific design patterns for: **adaptive/variable autonomy**, **LLM-based HRI**, **expert operator populations** (mining, agriculture, SAR), and **simulated users**.

---

## Requirements

- [Claude Code](https://claude.ai/code) CLI, desktop app, or VS Code / JetBrains extension
- Web demo: Python 3.10+, Anthropic API key

---

## Reference

```bibtex
@book{tian2024CRC,
  title={Experimental Methodology for Human-Robot Interaction:
         Guidelines and Case Studies for Human-Centred and Ethical Robotics Research},
  author={Tian, Leimin and Wu, Tina LY and Robinson, Nicole L and
          Carreno-Medrano, Pamela and Chan, Wesley P and Sakr, Maram and
          Abdi, Elahe and Croft, Elizabeth A and Kuli{\'c}, Dana},
  year={2024},
  publisher={CRC Press, Taylor \& Francis Group}
}
```

HRI Life Cycle Tool DOI: [https://doi.org/10.26180/26507314](https://doi.org/10.26180/26507314)

---

## Contributing

Issues and PRs welcome — particularly for:
- Additional validated HRI instruments
- Domain-specific patterns (surgical robotics, autonomous vehicles, social robotics)
- R code equivalents alongside the Python examples

---

## License

MIT
