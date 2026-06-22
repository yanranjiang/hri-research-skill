"""HRI Study Design Assistant — interactive demo powered by Claude."""

import os
from datetime import datetime
import streamlit as st
import anthropic

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="HRI Study Design Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Hero */
.hero { padding: 0.5rem 0 1.5rem 0; }
.hero-title { font-size: 2rem; font-weight: 800; color: #1a237e; margin: 0; line-height: 1.2; }
.hero-sub   { font-size: 1rem; color: #546e7a; margin-top: 0.4rem; }

/* Stage cards */
.stage-wrap  { border: 1px solid #e3e8f0; border-radius: 10px; padding: 1rem 1.2rem; margin: 0.8rem 0;
               background: #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.05); }
.stage-label { font-size: 0.78rem; font-weight: 700; letter-spacing: 0.08em;
               text-transform: uppercase; color: #7986cb; margin-bottom: 0.25rem; }
.stage-title { font-size: 1rem; font-weight: 700; color: #1a237e; margin-bottom: 0.1rem; }
.stage-desc  { font-size: 0.85rem; color: #78909c; margin-bottom: 0.8rem; }

/* Sidebar callout */
.sidebar-note { font-size: 0.8rem; color: #78909c; line-height: 1.5; }

/* Footer */
.footer { font-size: 0.78rem; color: #b0bec5; text-align: center;
          margin-top: 2.5rem; padding-top: 1rem; border-top: 1px solid #eceff1; }

/* Example pill buttons */
div[data-testid="stHorizontalBlock"] button {
    border-radius: 20px !important;
    font-size: 0.85rem !important;
}
</style>
""", unsafe_allow_html=True)

# ── Condensed HRI methodology system prompt ───────────────────────────────────
SYSTEM = """You are an expert HRI (Human-Robot Interaction) research methodologist, grounded in
Tian et al. (2024) "Experimental Methodology for Human-Robot Interaction", CRC Press.

Rules:
- Be specific and actionable. Never give generic advice.
- Always cite validated HRI instruments (SUS, NASA-TLX, Jian trust scale, etc.) with item counts.
- For power analysis, include complete runnable Python code using statsmodels.
- For statistical tests, include Python snippets using pingouin or statsmodels.
- Output clean markdown. Use tables where helpful.
- Be concise — avoid padding. Researchers are busy."""

# ── Stage definitions ─────────────────────────────────────────────────────────
STAGES = [
    ("🎯", "PICO & Hypotheses",
     "Clarify Population, Intervention, Comparison, Outcome — then form testable hypotheses",
     """Apply the PICO framework to the research scenario below, then formulate testable hypotheses.

Output exactly this structure:

## PICO Framework
| Element | Detail |
|---|---|
| **Population** | |
| **Intervention** | |
| **Comparison** | |
| **Outcome (primary)** | |
| **Outcome (secondary)** | |

## Refined Research Question
> One sentence, specific and testable.

## Hypotheses
**H1:** ...
**H2:** (if applicable) ..."""),

    ("📐", "Study Design",
     "Recommend within/between/mixed design with counterbalancing and control variables",
     """Based on the PICO above, recommend a study design.

## Design Type
State the design (within-subjects / between-subjects / mixed) and justify in 2–3 sentences.

## Conditions
List each condition with a one-line description.

## Counterbalancing
Specify the strategy (Latin square, full counterbalancing, randomisation) and show the schedule.

## Independent Variables
| IV | Levels | Type (within/between) |
|---|---|---|

## Dependent Variables
| DV | Category | Measurement method |
|---|---|---|

## Control Variables
List 4–6 variables that must be held constant and how.

## Session Length & Structure
Estimate session duration and outline the flow (welcome → consent → practice → conditions → debrief)."""),

    ("📊", "Power Analysis",
     "Calculate required sample size with complete runnable Python",
     """Generate a power analysis for this study.

## Assumed Effect Size
State the assumed Cohen's d or f and justify from published HRI literature (cite a paper or give a range).

## Required Sample Size

```python
# Power analysis — copy and run this directly
from statsmodels.stats.power import TTestIndPower, FTestAnovaPower
import math

# --- Parameters ---
alpha      = 0.05
power      = 0.80
effect     = 0.5   # Cohen's d (medium; adjust to your assumed effect)
attrition  = 0.20  # 20 % buffer

# --- Compute ---
# (Replace with FTestAnovaPower for ≥3 groups)
analysis = TTestIndPower()
n_per_group = analysis.solve_power(effect_size=effect, alpha=alpha, power=power)
total_with_buffer = math.ceil(n_per_group * (1 + attrition))

print(f"Required N per group: {math.ceil(n_per_group)}")
print(f"Total N (with {int(attrition*100)}% attrition buffer): {total_with_buffer}")
```

## Recruitment Recommendation
State the final recommended N and a realistic recruitment timeline."""),

    ("📋", "Measures & Instruments",
     "Map DVs to validated instruments with citations and admin schedule",
     """List all measures for this study.

## Subjective Measures
| Construct | Instrument | Scale | Items | When administered | Citation |
|---|---|---|---|---|---|

## Objective / Behavioural Measures
| Construct | Measure | How collected |
|---|---|---|

## Physiological Measures
State whether physiological measures are recommended for this study. If yes:
| Measure | Construct | Equipment | Sampling rate |
|---|---|---|---|

## Administration Schedule
Describe exactly when each instrument is administered within a session (before practice, after each condition, post-session)."""),

    ("📈", "Statistical Analysis Plan",
     "Primary and secondary tests with Python code matched to the design",
     """Generate a complete statistical analysis plan.

## Primary Analysis
| DV | Test | Assumptions to check | Python function |
|---|---|---|---|

## Secondary Analyses
List each secondary analysis with the same columns.

## Effect Size Metrics
State which effect size to report for each test (Cohen's d, η²p, r, BF10).

## Multiple Comparison Correction
State the correction strategy (Bonferroni, Holm, FDR) and threshold.

## Primary Analysis Code

```python
import pingouin as pg
import pandas as pd

# df columns: participant_id, condition, {primary_dv}
# Replace column names to match your dataset

result = pg.rm_anova(data=df, dv='{primary_dv}', within='condition',
                     subject='participant_id', detailed=True)
print(result[['Source', 'F', 'p-unc', 'np2']])

# Post-hoc (if significant)
posthoc = pg.pairwise_tests(data=df, dv='{primary_dv}', within='condition',
                             subject='participant_id', padjust='bonf')
print(posthoc[['A', 'B', 'T', 'p-corr', 'cohen-d']])
```

## If Assumptions Are Violated
State the non-parametric alternative for each primary test."""),

    ("✅", "Ethics Checklist",
     "HREC/IRB requirements and HRI-specific risk mitigations",
     """Generate a pre-submission ethics checklist for this study.

## Core HREC / IRB Requirements
- [ ] ...

## Informed Consent Elements
- [ ] ...

## HRI-Specific Risk Mitigations
| Risk | Likelihood | Mitigation |
|---|---|---|

## Data Management Plan
Address: storage location, anonymisation method, retention period, who has access.

## Debrief Protocol
Describe what participants are told at the end of the session (especially if any deception was used)."""),
]

# ── Helpers ───────────────────────────────────────────────────────────────────
def _client() -> anthropic.Anthropic | None:
    key = st.session_state.get("api_key") or os.environ.get("ANTHROPIC_API_KEY", "")
    return anthropic.Anthropic(api_key=key) if key else None


def _stream_stage(client: anthropic.Anthropic, full_context: str, stage_idx: int):
    """Generator: yields text chunks from Claude for one stage."""
    _, _, _, prompt_template = STAGES[stage_idx]
    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=1400,
        system=SYSTEM,
        messages=[{"role": "user", "content": f"Research scenario:\n{full_context}\n\n---\n\n{prompt_template}"}],
    ) as stream:
        yield from stream.text_stream


def _build_protocol(scenario: str, outputs: list[str]) -> str:
    date = datetime.now().strftime("%Y-%m-%d")
    sections = "\n\n---\n\n".join(
        f"## {icon} Stage {i + 1}: {title}\n\n{out}"
        for i, (icon, title, _, _) in enumerate(STAGES)
        for out in [outputs[i]]
    )
    return f"""# HRI Study Protocol
*Generated: {date}*

## Research Scenario
{scenario}

---

{sections}

---
*Generated by the HRI Study Design Assistant*
*Methodology: Tian et al. (2024) Experimental Methodology for Human-Robot Interaction, CRC Press*
"""


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🤖 HRI Study Design")
    st.markdown("<div class='sidebar-note'>Autonomous protocol generation powered by Claude.</div>",
                unsafe_allow_html=True)
    st.divider()

    api_input = st.text_input(
        "Anthropic API Key",
        type="password",
        placeholder="sk-ant-…",
        help="Or set ANTHROPIC_API_KEY in your environment",
        value=st.session_state.get("api_key", ""),
    )
    if api_input:
        st.session_state["api_key"] = api_input

    env_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if env_key and not api_input:
        st.success("API key loaded from environment ✓")

    st.divider()

    # Progress tracker
    st.markdown("**Protocol stages**")
    outputs = st.session_state.get("outputs", [])
    for i, (icon, title, _, _) in enumerate(STAGES):
        marker = "✅" if i < len(outputs) else "○"
        st.markdown(f"{marker} {icon} {title}")

    st.divider()
    st.markdown("""
**About**

[Irene Jiang](mailto:irenejiang09@gmail.com)
Research Scientist, CSIRO
HRI · Adaptive Autonomy · LLM × Robotics

[GitHub ↗](https://github.com/yanranjiang/hri-research-skill)
""")

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-title">🤖 HRI Study Design Assistant</div>
  <div class="hero-sub">
    Describe your research scenario → get a complete study protocol in seconds.<br>
    Grounded in Tian et al. (2024) <em>Experimental Methodology for Human-Robot Interaction</em>, CRC Press.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Quick examples ────────────────────────────────────────────────────────────
EXAMPLES = [
    ("⛏️ Mining SAR",
     "I want to compare LLM-based intent inference versus manual control for search-and-rescue "
     "with mining operators on a Boston Dynamics Spot robot. I'm interested in trust, workload, "
     "and intervention behaviour."),
    ("🚜 Agricultural Autonomy",
     "I want to study how shared autonomy affects operator workload and trust when controlling "
     "an agricultural robot for crop-row inspection. Participants will be experienced farm operators."),
    ("🦾 Collaborative Manipulation",
     "I'm studying how variable autonomy levels affect trust calibration and task performance "
     "during collaborative assembly tasks with a Franka Panda arm. Novice users, within-subjects."),
]

col1, col2, col3 = st.columns(3)
for (label, text), col in zip(EXAMPLES, [col1, col2, col3]):
    if col.button(label, use_container_width=True):
        st.session_state["scenario"] = text
        st.session_state.pop("outputs", None)

st.markdown("---")

# ── Input ─────────────────────────────────────────────────────────────────────
scenario = st.text_area(
    "Describe your research scenario",
    value=st.session_state.get("scenario", ""),
    height=130,
    placeholder=(
        "e.g. I want to study how shared autonomy affects operator trust and workload "
        "for mining operators controlling a Spot robot in a search-and-rescue scenario…"
    ),
    key="scenario",
)

constraints = st.text_input(
    "Additional constraints (optional)",
    placeholder="e.g. within-subjects preferred, ≤ 20 participants, 60-min sessions, no physiological sensors",
)

run = st.button("🚀  Generate Study Protocol", type="primary", use_container_width=True,
                disabled=not scenario.strip())

# ── Generation ────────────────────────────────────────────────────────────────
if run:
    client = _client()
    if not client:
        st.error("Please enter your Anthropic API key in the sidebar (or set ANTHROPIC_API_KEY).")
        st.stop()

    full_ctx = scenario.strip()
    if constraints.strip():
        full_ctx += f"\n\nAdditional constraints: {constraints.strip()}"

    outputs: list[str] = []
    st.session_state.pop("outputs", None)

    for i, (icon, title, desc, _) in enumerate(STAGES):
        st.markdown(f"""
<div class="stage-wrap">
  <div class="stage-label">Stage {i + 1} of {len(STAGES)}</div>
  <div class="stage-title">{icon} {title}</div>
  <div class="stage-desc">{desc}</div>
</div>
""", unsafe_allow_html=True)

        # Build context: scenario + all previous stage outputs
        ctx = full_ctx
        if outputs:
            prev = "\n\n".join(
                f"### {STAGES[j][1]}\n{o}" for j, o in enumerate(outputs)
            )
            ctx = f"{full_ctx}\n\n---\nPrevious stages:\n{prev}"

        placeholder = st.empty()
        accumulated = st.write_stream(_stream_stage(client, ctx, i))
        outputs.append(accumulated)

    st.session_state["outputs"] = outputs
    st.session_state["last_scenario"] = scenario

# ── Display stored outputs (after re-render / button click) ───────────────────
elif "outputs" in st.session_state:
    stored = st.session_state["outputs"]
    for i, (icon, title, desc, _) in enumerate(STAGES):
        with st.expander(f"{icon} Stage {i + 1}: {title}", expanded=False):
            st.markdown(stored[i])

# ── Download ──────────────────────────────────────────────────────────────────
if "outputs" in st.session_state and len(st.session_state["outputs"]) == len(STAGES):
    st.markdown("---")
    st.success("✅ Study protocol complete — all 6 stages generated.")

    protocol = _build_protocol(
        st.session_state.get("last_scenario", ""),
        st.session_state["outputs"],
    )
    filename = f"hri-study-protocol-{datetime.now().strftime('%Y%m%d')}.md"
    col_a, col_b, col_c = st.columns([2, 1, 2])
    col_b.download_button(
        "📥 Download Protocol",
        data=protocol,
        file_name=filename,
        mime="text/markdown",
        use_container_width=True,
    )

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
HRI Study Design Assistant ·
Methodology: Tian et al. (2024) <em>Experimental Methodology for Human-Robot Interaction</em>, CRC Press ·
Built by Irene Jiang · CSIRO · 2025
</div>
""", unsafe_allow_html=True)
