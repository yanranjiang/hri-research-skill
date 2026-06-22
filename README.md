# HRI Research Skill for Claude Code

A Claude Code skill that guides you through the full lifecycle of a Human-Robot Interaction (HRI) research study — from question formulation to statistical reporting. Load it once in a conversation and get methodology advice, instrument recommendations, code templates, and analysis checklists tailored to your study.

Grounded in:
> Tian, L., Wu, T. L. Y., Robinson, N. L., Carreno-Medrano, P., Chan, W. P., Sakr, M., Abdi, E., Croft, E. A., & Kulić, D. (2024). *Experimental Methodology for Human-Robot Interaction: Guidelines and Case Studies for Human-Centred and Ethical Robotics Research*. CRC Press, Taylor & Francis Group.

---

## What it covers

| Stage | Content |
|-------|---------|
| 1. Research question | PICO framework, hypothesis formulation |
| 2. Study design | Within/between/mixed/longitudinal, counterbalancing, IVs & DVs |
| 3. Robot platform & scenario | Platform selection, Wizard-of-Oz, simulation vs. physical |
| 4. Ethics & approval | HREC/IRB checklist, consent, anonymisation, risk assessment |
| 5. Participant recruitment | Power analysis code, screening criteria, incentives |
| 6. Data collection | Session structure, validated instruments (SUS, NASA-TLX, trust scales, etc.), physiological measures |
| 6.5 Multimodal data fusion | Synchronisation, per-modality preprocessing (HRV, EDA, EEG, gaze, robot logs), early/late/hybrid fusion, convergent validity |
| 7. Statistical analysis | Test selection, LMM, mediation, moderation, Bayesian (Bayes factors, ROPE), time-series (DTW, change-point), inter-rater reliability (κ, ICC) |
| 8. Reporting | HRI venue guide, CONSORT-adapted checklist |

Plus HRI-specific design patterns for: adaptive/variable autonomy, LLM-based HRI, expert participant studies (mining, agriculture, SAR), and simulated users.

---

## Installation

### Option A — Copy the skill file directly

1. Download `SKILL.md` from this repository
2. Place it at:
   ```
   ~/.claude/skills/hri-research/SKILL.md
   ```
3. Restart Claude Code (or open a new session)

### Option B — Clone the repo

```bash
git clone https://github.com/yanranjiang/hri-research-skill.git
mkdir -p ~/.claude/skills/hri-research
cp hri-research-skill/SKILL.md ~/.claude/skills/hri-research/SKILL.md
```

That's it. No dependencies, no build step.

---

## Usage

In any Claude Code conversation, type:

```
/hri-research
```

Then describe your situation. Examples:

```
/hri-research
I'm designing a within-subjects study comparing teleoperation vs shared autonomy
on a Spot robot with 20 mining operators. What design should I use and how
many participants do I need?
```

```
/hri-research
I have EDA, HRV, NASA-TLX, and robot interaction logs from 18 participants
across 3 conditions. How do I synchronise and fuse these streams?
```

```
/hri-research
I want to test whether trust mediates the relationship between autonomy level
and intervention frequency. Show me how to run this in Python.
```

```
/hri-research
Two raters coded takeover behaviour from video. How do I check inter-rater
reliability before running my main analysis?
```

The skill stays active for the rest of that conversation — you don't need to invoke it again.

---

## What you get

- **Study design guidance** matched to your population, platform, and constraints
- **Validated instrument recommendations** with citation and item counts
- **Python code templates** (neurokit2, mne, pingouin, statsmodels, pymer4, dtaidistance, ruptures, pymc, arviz)
- **Decision tables** for statistical test selection, fusion strategy, and random effects structure
- **Checklists** for ethics, data logging, multimodal fusion, statistical reporting, and paper write-up
- **HRI-domain specifics** — autonomy studies, LLM-based robots, expert operator populations, simulated users

---

## Requirements

- [Claude Code](https://claude.ai/code) (CLI, desktop app, or VS Code / JetBrains extension)
- No other dependencies

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
- Domain-specific patterns (social robotics, surgical robotics, autonomous vehicles)
- R code equivalents alongside the Python examples

---

## License

MIT
