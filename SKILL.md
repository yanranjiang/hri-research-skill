---
name: hri-research
description: >
  Comprehensive guide for designing and conducting Human-Robot Interaction (HRI) studies.
  In AUTO-DESIGN MODE (default for new studies): autonomously generates a complete study
  protocol workspace — research-question.md, study-design.md, power-analysis.py,
  instruments.md, analysis-plan.md, ethics-checklist.md, session-script.md —
  from a research scenario description, then compiles study-protocol.md and
  progress-report.html for human review. In ADVISORY MODE: covers the full study lifecycle
  from question formulation to dissemination, including multimodal data fusion,
  advanced statistical testing (LMM, mediation, Bayesian), and inter-rater reliability.
  Based on Tian et al. (2024) CRC Press.
version: 2.0.0
author: Orchestra Research
license: MIT
tags: [HRI, Human-Robot Interaction, Autonomous Protocol Generation, Auto-Design,
       Study Design, Experimental Methodology, Ethics, Robotics Research,
       Adaptive Autonomy, Multimodal Fusion, Statistical Testing, Mixed Effects,
       Mediation, Bayesian, File Generation, Agent Continuity]
dependencies: []
---

# HRI Research: Experimental Methodology Guide

A structured guide for designing rigorous, human-centred, and ethical HRI studies. Covers the full study lifecycle from question formulation through dissemination. Grounded in Tian et al. (2024), *Experimental Methodology for Human-Robot Interaction: Guidelines and Case Studies for Human-Centred and Ethical Robotics Research*, CRC Press.

**Key reference**: `@book{tian2024CRC}` — Leimin Tian, Tina LY Wu, Nicole L Robinson, Pamela Carreno-Medrano, Wesley P Chan, Maram Sakr, Elahe Abdi, Elizabeth A Croft, Dana Kulić.

---

## When to Use This Skill

- Designing a new HRI user study from scratch
- Choosing between within-subjects vs. between-subjects designs
- Selecting measures (subjective, objective, physiological) for HRI
- Preparing ethics applications and informed consent protocols
- Determining sample sizes for HRI studies
- Designing robot behaviours, scenarios, or Wizard-of-Oz setups
- Analysing HRI data (interaction logs, questionnaires, video)
- Fusing multimodal data streams (physiological, behavioural, subjective, robot logs)
- Choosing and applying advanced statistical tests (LMM, mediation, moderation, Bayesian)
- Computing inter-rater reliability for video annotation or qualitative coding
- Writing up HRI studies for HRI, RO-MAN, ICSR, CHI, or IJSR

**Do NOT use this skill when**:
- You need ML/training guidance for robot systems (use `trl-fine-tuning`, `peft`, etc.)
- You need paper writing structure (use `ml-paper-writing` or `systems-paper-writing`)
- You need research ideation (use `brainstorming-research-ideas` or `creative-thinking-for-research`)

---

## Auto-Design Mode: Autonomous Protocol Generation

**This is the default mode when a user describes a new HRI study.** Don't just advise — autonomously generate a complete set of study files they can use immediately.

**Run autonomously. Do not pause for confirmation at each stage — work through all stages, then surface a `progress-report.html` the user can review and redirect.**

### Getting Started

Determine user state and act immediately:

| User State | Action |
|---|---|
| Vague idea ("I want to study X") | Apply PICO to clarify (ask ≤ 2 questions max), then start |
| Clear research question | Start immediately — no clarifying questions |
| Existing design to review | Read their materials, identify gaps, generate missing files |
| Resuming (`study-state.yaml` exists) | Read state, continue from last incomplete stage |

### Workspace Structure

Create at the project root before writing any content:

```
{study-slug}/                      # e.g. shared-autonomy-mining/
├── study-state.yaml               # Stage tracking — update after each stage
├── research-question.md           # PICO framework, refined RQ, hypotheses
├── study-design.md                # Design type, conditions, counterbalancing
├── power-analysis.py              # Runnable Python — computes N + attrition buffer
├── instruments.md                 # Validated questionnaires + admin schedule
├── analysis-plan.md               # Statistical tests, effect sizes, corrections
├── ethics-checklist.md            # HREC/IRB requirements + HRI risk mitigations
├── data-collection/
│   ├── session-script.md          # Minute-by-minute experimenter guide
│   └── debrief.md                 # Participant debrief text
└── study-protocol.md              # Full compiled protocol (generated last)
```

Name the folder from the topic: `trust-calibration-spot/`, `llm-intent-hri/`, `ag-robot-shared-autonomy/`.

### Generation Pipeline

Work through each stage in order. Write the file, update `study-state.yaml` to `complete`, then move to the next — **no stopping between stages**.

```
Stage 1: Research Question
  Apply PICO → refine RQ → form 2–3 testable hypotheses
  → write research-question.md

Stage 2: Study Design
  Choose within/between/mixed design (justify) → counterbalancing strategy
  → write study-design.md

Stage 3: Power Analysis
  Justify assumed effect size from prior HRI literature → compute N → add 20% attrition buffer
  → write power-analysis.py (runnable, with printed output)

Stage 4: Instruments & Measures
  Map each DV to a validated, cited instrument → admin schedule per session
  → write instruments.md

Stage 5: Statistical Analysis Plan
  Select primary + secondary tests → effect size metrics → multiple comparison correction
  → write analysis-plan.md with Python code snippets

Stage 6: Ethics Checklist
  HREC/IRB requirements → HRI-specific risks (robot proximity, video recording, WoZ)
  → write ethics-checklist.md

Stage 7: Session Script
  Minute-by-minute experimenter guide → debrief text
  → write data-collection/session-script.md and data-collection/debrief.md

Stage 8: Compile + Confound Review
  Merge all stages → write study-protocol.md
  Check top confound risks (see pitfalls table) → add flags to study-state.yaml
  → generate progress-report.html
```

### `study-state.yaml` Template

```yaml
study:
  title: ""
  scenario: ""
  created: ""          # ISO date
  last_updated: ""

stages:
  research_question: pending   # pending | complete
  study_design: pending
  power_analysis: pending
  instruments: pending
  analysis_plan: pending
  ethics_checklist: pending
  session_script: pending
  protocol_compiled: pending

design:
  type: ""             # within | between | mixed | longitudinal
  n_conditions: 0
  target_n: 0
  primary_dv: ""
  primary_test: ""

flags: []              # open questions or confound risks for human review
```

### Progress Report

After Stage 8, generate `progress-report.html`. This is what the user sees to review and redirect your work.

```html
<!DOCTYPE html>
<html>
<head>
<title>HRI Study Design — Progress Report</title>
<style>
  body { font-family: system-ui, sans-serif; max-width: 900px; margin: 2rem auto; color: #333; line-height: 1.6; }
  h1   { color: #1a237e; border-bottom: 2px solid #e8eaf6; padding-bottom: 0.5rem; }
  h2   { color: #283593; margin-top: 2rem; }
  .done    { color: #2e7d32; font-weight: 600; }
  .pending { color: #bf360c; }
  table { border-collapse: collapse; width: 100%; margin: 1rem 0; }
  th, td { border: 1px solid #ddd; padding: 8px 12px; text-align: left; }
  th { background: #e8eaf6; font-weight: 600; }
  .risk { background: #fff8e1; border-left: 4px solid #f9a825; padding: 0.8rem 1rem; margin: 0.5rem 0; border-radius: 0 4px 4px 0; }
  .flag { background: #fce4ec; border-left: 4px solid #c62828; padding: 0.8rem 1rem; margin: 0.5rem 0; border-radius: 0 4px 4px 0; }
  footer { font-size: 0.85rem; color: #90a4ae; margin-top: 3rem; border-top: 1px solid #eceff1; padding-top: 1rem; }
</style>
</head>
<body>
  <h1>🤖 HRI Study Design — Progress Report</h1>
  <p><strong>Study:</strong> {title} &nbsp;|&nbsp; <strong>Generated:</strong> {date}</p>

  <h2>Stage Completion</h2>
  <table>
    <tr><th>Stage</th><th>File</th><th>Status</th></tr>
    <!-- one row per stage with class="done" or class="pending" -->
  </table>

  <h2>Key Design Decisions</h2>
  <table>
    <tr><th>Decision</th><th>Choice</th><th>Rationale</th></tr>
    <!-- design type, N, primary DV, primary test, counterbalancing strategy -->
  </table>

  <h2>Top Confound Risks</h2>
  <!-- 3 most relevant risks from the pitfalls table, with specific mitigations -->

  <h2>Open Questions for Human Review</h2>
  <!-- items from study-state.yaml flags — decisions that need the researcher's input -->

  <h2>Files Generated</h2>
  <ul><!-- list all files with one-line description --></ul>

  <footer>Generated by /hri-research v2.0 · Methodology: Tian et al. (2024) <em>Experimental Methodology for Human-Robot Interaction</em>, CRC Press</footer>
</body>
</html>
```

### Agent Continuity

For study designs that span multiple conversation turns, set up `/loop` so the agent continues autonomously across context windows:

```
/loop
Continue the HRI study design. Read study-state.yaml to find the current stage.
Complete it, write the output file, mark the stage "complete" in study-state.yaml,
then move to the next pending stage. Stop when all stages are complete and
progress-report.html is generated.
```

---

## HRI Study Lifecycle Overview

The HRI research lifecycle has eight stages. Each stage must be completed before proceeding to the next — ethics approval is a hard gate before any data collection.

```
1. Research Question & Hypotheses
         ↓
2. Study Design
         ↓
3. Robot Platform & Scenario Design
         ↓
4. Ethics & Institutional Approval  ← HARD GATE
         ↓
5. Participant Recruitment
         ↓
6. Data Collection & Procedure
         ↓
6.5 Multimodal Data Fusion          ← NEW: synchronise & fuse streams
         ↓
7. Statistical Analysis              ← EXPANDED: LMM, mediation, Bayesian
         ↓
8. Reporting & Dissemination
```

---

## Stage 1: Research Question & Hypotheses

### Formulating the Research Question

HRI research questions fall into three categories:

| Type | Example | Typical Method |
|------|---------|----------------|
| **Descriptive** | "How do operators monitor multiple robots in SAR?" | Observational, survey |
| **Comparative** | "Does shared autonomy reduce operator workload vs. teleoperation?" | Controlled experiment |
| **Causal / Mechanistic** | "Does trust in robot prediction accuracy cause reduced intervention frequency?" | Controlled experiment + mediation analysis |

**PICO framework** for HRI:
- **P**opulation: Who are the participants? (domain experts, novices, older adults)
- **I**ntervention: What robot behaviour / interaction modality is being tested?
- **C**omparison: What is the baseline or alternative condition?
- **O**utcome: What do you measure? (task performance, workload, trust, acceptance)

### Hypothesis Formulation

Write testable hypotheses in the form:
> **H1**: Participants using [condition A] will report significantly lower [measure] than participants using [condition B] as measured by [instrument].

**Common HRI hypothesis errors**:
- Underconstrained: "Users will prefer the robot" (prefer for what? measured how?)
- Confounded: Testing interaction modality while also changing robot appearance
- Untestable with proposed sample size: power < 0.80

---

## Stage 2: Study Design

### Experimental Design Choice

| Design | When to Use | Key Consideration |
|--------|-------------|------------------|
| **Within-subjects** | Conditions differ in interaction style; learning effects can be counterbalanced | Counterbalance order; allow washout period between conditions |
| **Between-subjects** | Learning/carry-over effects cannot be eliminated; large population differences expected | Requires larger N; check group equivalence at baseline |
| **Mixed** | Some factors within, some between (e.g., within: autonomy level; between: expertise group) | Most common in HRI; increases statistical power on within factors |
| **Longitudinal** | Studying trust or skill change over time | Attrition risk; plan for missing data |

### Counterbalancing

For within-subjects designs with ≤4 conditions, use a **Latin square**:

```
Participant 1: A → B → C
Participant 2: B → C → A
Participant 3: C → A → B
```

For ≥5 conditions or when order effects are asymmetric, use **balanced Latin square** or **randomisation with stratification**.

### Control Variables

Always report and control:
- Robot appearance / embodiment (if not the IV)
- Task difficulty and structure
- Participant prior experience with robots
- Ambient environment noise/lighting (for in-person studies)
- Time of day / fatigue (for multi-session studies)

### Independent Variables (IVs) in HRI

Common IVs:
- **Autonomy level**: teleoperation, shared autonomy, full autonomy
- **Interaction modality**: voice, gesture, GUI, haptic
- **Robot appearance**: mechanical, anthropomorphic, zoomorphic
- **Feedback type**: visual, auditory, tactile, multimodal
- **Task type**: manipulation, navigation, surveillance, collaboration

### Dependent Variables (DVs) — see Stage 6 for instruments

Core DV categories:
- Task performance (objective)
- Perceived usability / UX (subjective)
- Trust (subjective + behavioural)
- Cognitive workload (subjective + physiological)
- Situational awareness (subjective + behavioural)
- Social / affective response

---

## Stage 3: Robot Platform & Scenario Design

### Platform Selection Considerations

| Factor | Questions to Answer |
|--------|---------------------|
| **Embodiment** | Does physical presence matter for your RQ? If not, consider simulation/video |
| **Capability match** | Can the robot reliably execute the experimental tasks without confounds? |
| **Safety** | Can you ensure participant safety with co-located robot? What is e-stop protocol? |
| **Reproducibility** | Can other labs replicate with the same or equivalent platform? |
| **Ecological validity** | Does the platform match the real deployment context? |

**Common platforms by domain**:

| Domain | Platform Examples |
|--------|------------------|
| Manipulation | Franka Panda, UR5/10, Kinova Gen3 |
| Mobile / SAR | Boston Dynamics Spot, Clearpath Jackal, TurtleBot |
| Social / Home | Pepper, NAO, Furhat, Misty |
| Aerial | DJI Mavic (UAV studies), custom |
| Agriculture | Custom ground vehicles, collaborative arms |

### Scenario Design Principles

1. **Ecological validity**: Scenario should reflect real deployment conditions
2. **Controlled variation**: Only the IV(s) should differ between conditions — everything else identical
3. **Pilot testing**: Run 3–5 pilots before main study to catch confounds and calibrate task difficulty
4. **Failure modes**: Decide in advance how to handle robot failures (retry, exclude trial, exclude participant)

### Wizard-of-Oz (WoZ) Studies

WoZ is appropriate when:
- Target robot capability does not yet exist
- You need to isolate human perception from system performance
- Rapid prototyping of interaction concepts

**WoZ checklist**:
- [ ] Wizard is blind to condition order where possible
- [ ] Wizard training protocol is documented and standardised
- [ ] Wizard actions are logged (timing, inputs)
- [ ] Participants are debriefed about WoZ after study
- [ ] Wizard fatigue is managed (breaks, session limits)

### Simulation vs. Physical Robot

| Aspect | Simulation | Physical |
|--------|-----------|---------|
| Safety | High — no physical risk | Requires safety protocols |
| Ecological validity | Lower for embodiment effects | Higher |
| Cost / logistics | Lower | Higher |
| Reproducibility | Easier (save/load world state) | Harder (reset procedures) |
| When to use | Early validation, large N studies, remote studies | When embodiment/physical presence is the IV or a key factor |

---

## Stage 4: Ethics & Institutional Approval

### Ethics Checklist

Every HRI study with human participants requires ethics approval. Start this process early — approval can take 4–12 weeks.

**Core requirements**:
- [ ] Institutional ethics approval (IRB/HREC) obtained **before** any participant contact
- [ ] Informed consent form: purpose, procedures, risks, right to withdraw, data use
- [ ] Participant information sheet: plain-language, no coercion
- [ ] Data management plan: storage, anonymisation, retention, access
- [ ] Risk assessment: physical (robot proximity), psychological (stress, distressing content), privacy
- [ ] Deception protocol (if applicable): debrief procedure documented and approved

### Special Considerations for HRI

| Risk | Mitigation |
|------|-----------|
| Physical co-location with robot | E-stop accessible to participant; safety cage or barriers if needed; robot velocity limits |
| Data recording (video/audio) | Explicit consent for recording; face blurring if required; separate consent for clips used in papers/demos |
| Vulnerable populations | Additional safeguards; may require capacity assessment |
| Physiological sensors | Explain sensors fully; allow participant to decline individual sensors |
| Domain experts as participants | Avoid dual relationships; ensure voluntary participation |

### Anonymisation

- Replace names with participant IDs (P01, P02…)
- Remove or blur faces in video data before analysis
- Aggregate location data for remote participants
- Store consent forms separately from study data (different folder, different key)

---

## Stage 5: Participant Recruitment

### Sample Size & Power Analysis

**Power analysis** should be conducted before recruitment. Target power ≥ 0.80 at α = 0.05.

```python
# Example using statsmodels (Python)
from statsmodels.stats.power import TTestIndPower, FTestAnovaPower

# For independent t-test (between-subjects, 2 groups)
analysis = TTestIndPower()
n = analysis.solve_power(effect_size=0.5, alpha=0.05, power=0.8)
# effect_size: Cohen's d — 0.2 small, 0.5 medium, 0.8 large

# For one-way ANOVA (between-subjects, k groups)
analysis = FTestAnovaPower()
n = analysis.solve_power(effect_size=0.25, alpha=0.05, power=0.8, k_groups=3)
# effect_size: Cohen's f — 0.1 small, 0.25 medium, 0.4 large
```

**HRI-specific guidance**:
- Effect sizes in HRI are often medium (d ≈ 0.5, f ≈ 0.25) — assume medium unless prior literature suggests otherwise
- Within-subjects designs need fewer participants (typically 40–60% of between-subjects N)
- Add 15–20% to account for attrition and exclusions
- For pilot studies: n = 8–12 is typical; do not use pilot data in main analysis

### Participant Screening

Define inclusion/exclusion criteria and document them:

| Criterion | Common HRI examples |
|-----------|-------------------|
| Age | ≥18 (adults); specify if targeting older adults or specific age bands |
| Experience | Novice users (no prior robot experience); domain experts (≥2 years in domain) |
| Physical | Right-hand dominant if task requires specific hand; colour vision if colour cues used |
| Cognitive | Capacity to provide informed consent |
| Exclusion | Current or prior study on same topic; conflict of interest |

### Recruitment Sources

- University participant pools (for general population)
- Professional networks / industry partners (for domain experts)
- Online platforms: Prolific (preferred over MTurk for research), CloudResearch
- Community organisations (for older adults, specific populations)

**Incentives**: Ensure incentives are non-coercive. Common: gift vouchers, course credit, hourly rate aligned with local standards.

---

## Stage 6: Data Collection & Procedure

### Session Structure

A standard HRI session follows this order:

```
1. Welcome & check-in (5 min)
2. Participant information & consent (10 min)
3. Demographics questionnaire (5 min)
4. Introduction to robot / system (5–10 min)
5. Practice trials (5–15 min) — not analysed
6. Experimental trials (20–45 min)
   ├── Condition A → post-condition measures
   ├── [break if within-subjects]
   └── Condition B → post-condition measures
7. Post-session questionnaires (10–15 min)
8. Debrief & questions (5 min)
```

Total session: 60–90 min is optimal. >120 min risks fatigue confounds.

### Measures & Instruments

#### Subjective Measures (Questionnaires)

| Construct | Instrument | Scale | Items |
|-----------|-----------|-------|-------|
| **Usability** | SUS (System Usability Scale) | 5-point Likert | 10 |
| **Workload** | NASA-TLX | 6 subscales, 21-point each | 6 |
| **Trust in Robot** | Trust in Automation (Jian et al.) | 7-point Likert | 12 |
| **Trust in Robot** | HRI Trust Scale (Hancock et al.) | 7-point Likert | 14 |
| **Acceptance** | Unified Theory of Acceptance (UTAUT) | 7-point Likert | varies |
| **Acceptance** | Almere Model (for social robots) | 5-point Likert | 27 |
| **Situational Awareness** | SAGAT (probe-based) | task-specific | varies |
| **Situational Awareness** | SART | 7-point Likert | 10 |
| **User Experience** | AttrakDiff | 7-point semantic differential | 28 |
| **Presence / Embodiment** | IPQ (iGroup Presence Questionnaire) | 7-point Likert | 14 |
| **Anxiety** | STAI-State | 4-point Likert | 20 |
| **Robot Anxiety** | NARS (Negative Attitudes toward Robots) | 5-point Likert | 14 |

**Likert scale guidance**:
- Use 5 or 7 points (odd scale with neutral midpoint) unless instrument specifies otherwise
- Do not mix scale directions without reversing items
- Validate internal consistency: Cronbach's α ≥ 0.70 acceptable, ≥ 0.80 preferred

#### Objective / Behavioural Measures

| Construct | Measure |
|-----------|---------|
| **Task performance** | Completion time, success rate, error rate, path efficiency |
| **Intervention behaviour** | Intervention frequency, intervention duration, time-to-intervene |
| **Autonomy preference** | Proportion of time using each autonomy level (in variable autonomy systems) |
| **Gaze / attention** | Fixation duration, saccade patterns (eye-tracker), screen dwell time |
| **Physical workload** | Input device forces, movement frequency |
| **Communication** | Utterance count, turn-taking latency, interruption rate |

#### Physiological Measures

| Measure | Construct | Equipment |
|---------|-----------|-----------|
| Heart rate / HRV | Arousal, stress | Polar H10, Empatica E4 |
| EDA / skin conductance | Emotional arousal | Shimmer, Empatica E4 |
| EEG | Cognitive workload, attention | OpenBCI, Emotiv |
| EMG | Physical effort, fatigue | Delsys, Cometa |
| fNIRS | Prefrontal workload | NIRx, Artinis |

Physiological data requires signal processing expertise and artefact rejection — only include if it directly addresses your RQ.

### Data Logging

Checklist for data capture:
- [ ] Interaction logs: timestamped, labelled by condition and participant ID
- [ ] Questionnaires: paper or digital (Qualtrics, REDCap, LimeSurvey)
- [ ] Video: camera angles capture both participant and robot; consent obtained
- [ ] System logs: robot state, commands, errors, timestamps synchronised with interaction log
- [ ] Pilot data stored separately and not mixed with main study data

---

## Stage 6.5: Multimodal Data Fusion

HRI studies routinely collect data from 4–6 concurrent streams. Fusing them correctly is a prerequisite for valid analysis. Do this stage before running any inferential statistics.

### Modality Inventory

Map every data stream collected to its type, sampling rate, and format before writing any analysis code.

| Modality | Common Streams | Typical Rate | Format |
|----------|---------------|-------------|--------|
| **Subjective** | Questionnaire scales (SUS, NASA-TLX, trust) | Per-trial / per-condition | Tabular (CSV) |
| **Behavioural** | Interaction log (autonomy switches, commands, errors) | Event-driven | Timestamped CSV / ROS bag |
| **Performance** | Task completion time, success rate, path efficiency | Per-trial | Derived from logs |
| **Gaze** | Fixation position, saccade, AOI dwell | 60–300 Hz | Eye-tracker CSV |
| **Physiological — cardiac** | HR, IBI, HRV | 1–4 Hz (processed) / 500–2000 Hz (raw ECG) | Polar, Empatica, Shimmer |
| **Physiological — EDA** | Skin conductance level (SCL), SCR peaks | 4–64 Hz | Empatica, Shimmer |
| **Physiological — EEG** | Power bands (θ, α, β), ERPs | 128–1000 Hz | OpenBCI, BrainProducts |
| **Physiological — EMG** | Muscle activation amplitude | 1000–2000 Hz | Delsys, Cometa |
| **Robot state** | Joint positions, velocities, end-effector pose, autonomy level | 10–1000 Hz | ROS topic / CSV |
| **Video / audio** | RGB frames, audio waveform | 30 fps / 44 kHz | MP4, WAV |

---

### Step 1: Temporal Synchronisation

All streams must share a common time reference before any fusion. Misalignment > 500 ms is a systematic confound in physiological analyses.

#### Synchronisation Strategies

| Method | When to Use | Precision |
|--------|-------------|----------|
| **Hardware trigger** (TTL pulse, photodiode) | Gold standard; co-located equipment | < 1 ms |
| **NTP / PTP network sync** | Multi-machine ROS setups | 1–10 ms |
| **Shared clock event** (onset marker broadcast) | Software-only setups | 10–100 ms |
| **Post-hoc cross-correlation** | When hardware sync was missed | 100–500 ms (verify manually) |
| **Dynamic Time Warping (DTW)** | Elastic alignment of two signals with known correspondence points | signal-dependent |

**Minimum viable approach**: log a shared event marker (e.g., "trial_start", "trial_end") to every stream's timestamp column at the moment the event occurs. All subsequent alignment is relative to these anchors.

```python
import pandas as pd
import numpy as np

def align_to_anchor(stream_df, anchor_col, reference_time):
    """Shift a stream's timestamps so its anchor event aligns with reference_time."""
    anchor_time = stream_df[anchor_col].iloc[0]
    stream_df["time_aligned"] = stream_df["timestamp"] - anchor_time + reference_time
    return stream_df

# Example: align EDA stream to robot log's trial_start timestamp
robot_log = pd.read_csv("robot_log.csv")  # has 'trial_start_ts' column
eda = pd.read_csv("eda.csv")              # has 'timestamp' column

trial_start = robot_log["trial_start_ts"].iloc[0]
eda_aligned = align_to_anchor(eda, "timestamp", trial_start)
```

---

### Step 2: Per-Modality Preprocessing & Feature Extraction

Process each stream independently before fusion. Document all preprocessing choices — they are methodology decisions.

#### Physiological Preprocessing

```python
import neurokit2 as nk

# --- HRV (from ECG or Polar HR) ---
ecg_signals, info = nk.ecg_process(ecg_raw, sampling_rate=500)
hrv_features = nk.hrv(info["ECG_R_Peaks"], sampling_rate=500)
# Key features: HRV_RMSSD (parasympathetic), HRV_LF, HRV_HF, HRV_SDNN

# --- EDA ---
eda_signals, info = nk.eda_process(eda_raw, sampling_rate=4)
# Decompose into tonic (SCL) and phasic (SCR) components
scl = eda_signals["EDA_Tonic"]
scr_peaks = info["SCR_Peaks"]
scr_amplitude = eda_signals["SCR_Amplitude"].dropna().mean()

# --- Epoch by trial ---
events = nk.events_create(event_onsets=[trial_start_sample], event_durations=[trial_duration_samples])
epochs = nk.epochs_create(eda_signals, events, sampling_rate=4, epochs_start=0, epochs_end=trial_duration)
```

**Key HRV features for HRI workload**:

| Feature | Domain | Construct |
|---------|--------|-----------|
| RMSSD | Time | Parasympathetic activity; decreases under cognitive load |
| SDNN | Time | Overall HRV variability |
| LF/HF ratio | Frequency | Sympatho-vagal balance; increases under stress |
| LF power (0.04–0.15 Hz) | Frequency | Sympathetic + parasympathetic |
| HF power (0.15–0.40 Hz) | Frequency | Parasympathetic (respiratory) |
| Sample entropy (SampEn) | Nonlinear | Irregularity; decreases under cognitive load |

**EDA features**:

| Feature | Construct |
|---------|-----------|
| Mean SCL | Tonic arousal level |
| SCR count / min | Phasic arousal events |
| Mean SCR amplitude | Arousal magnitude |
| SCR latency | Reactivity speed |

#### EEG Feature Extraction

```python
import mne

raw = mne.io.read_raw_brainvision("study.vhdr", preload=True)
raw.filter(1., 40.)          # bandpass
raw.set_eeg_reference("average")
ica = mne.preprocessing.ICA(n_components=20)
ica.fit(raw)
ica.exclude = [0, 3]         # manually identified artifact components
raw_clean = ica.apply(raw.copy())

epochs = mne.Epochs(raw_clean, events, event_id, tmin=-0.2, tmax=1.0, baseline=(-0.2, 0))
psd = epochs.compute_psd(method="welch", fmin=1, fmax=40)

# Band power features per epoch
theta = psd.copy().crop(4, 8).get_data().mean(axis=-1)   # workload proxy
alpha = psd.copy().crop(8, 13).get_data().mean(axis=-1)   # relaxation / disengagement
beta  = psd.copy().crop(13, 30).get_data().mean(axis=-1)  # active cognition
```

#### Gaze Feature Extraction

```python
import pandas as pd

gaze = pd.read_csv("gaze.csv")  # columns: time, x, y, fixation_id, aoi_label

# Fixation-level features
fix_features = gaze.groupby(["participant", "condition", "trial"]).agg(
    fix_count=("fixation_id", "nunique"),
    mean_fix_duration=("duration_ms", "mean"),
    aoi_robot_dwell=("aoi_label", lambda x: (x == "robot").mean()),  # proportion on robot
    aoi_screen_dwell=("aoi_label", lambda x: (x == "screen").mean()),
).reset_index()
```

#### Behavioural Log Feature Extraction

```python
log = pd.read_csv("interaction_log.csv")

# Intervention features (shared autonomy studies)
intervention_features = log.groupby(["participant", "condition", "trial"]).agg(
    n_interventions=("event_type", lambda x: (x == "takeover").sum()),
    mean_intervention_duration=("duration_s", "mean"),
    time_to_first_intervention=("time_since_trial_start", "first"),
    autonomy_level_mean=("autonomy_level", "mean"),
).reset_index()
```

---

### Step 3: Fusion Strategy Selection

Choose fusion strategy based on your analytical goal and data completeness.

```
                    ┌─────────────────────────────────────────┐
                    │         Fusion Strategy Decision         │
                    └──────────────────┬──────────────────────┘
                                       │
              ┌────────────────────────┼─────────────────────────┐
              ▼                        ▼                          ▼
       Early Fusion            Late Fusion                Hybrid Fusion
    (Feature-level)         (Decision-level)          (Intermediate)
              │                        │                          │
   Concatenate features       Analyse each modality      Fuse some modalities
   → single model/test        separately → combine        early, rest late
              │                  predictions               │
   Best for: capturing      Best for: missing data,    Best for: modalities
   cross-modal interactions  modular analysis            at very different
   when all data complete    interpretability            timescales
```

#### Early Fusion (Feature Concatenation)

```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

# Merge all feature tables on [participant, condition, trial]
features = (
    hrv_features_per_trial
    .merge(eda_features_per_trial, on=["participant", "condition", "trial"])
    .merge(gaze_features_per_trial, on=["participant", "condition", "trial"])
    .merge(intervention_features, on=["participant", "condition", "trial"])
    .merge(questionnaire_scores, on=["participant", "condition"])  # condition-level
)

# Normalise within-participant (removes between-subject baseline differences)
feature_cols = [c for c in features.columns if c not in ["participant", "condition", "trial"]]
scaler = StandardScaler()
features[feature_cols] = scaler.fit_transform(features[feature_cols])

# Optional: reduce dimensionality before statistical testing
pca = PCA(n_components=0.90)  # retain 90% variance
X_reduced = pca.fit_transform(features[feature_cols])
print(f"Reduced from {len(feature_cols)} to {X_reduced.shape[1]} components")
```

#### Late Fusion (Decision Combination)

Analyse each modality separately (see Stage 7 for tests), then combine evidence:

```python
# Example: combine p-values from independent analyses using Fisher's method
from scipy.stats import combine_pvalues

p_hrv    = 0.03   # from LMM on HRV_RMSSD
p_eda    = 0.07   # from LMM on mean SCL
p_nasa   = 0.02   # from RM-ANOVA on NASA-TLX
p_perf   = 0.01   # from paired t-test on task completion time

stat, combined_p = combine_pvalues([p_hrv, p_eda, p_nasa, p_perf], method="fisher")
print(f"Fisher's combined p = {combined_p:.4f}")
```

#### Hybrid Fusion for Mixed-Timescale Data

Physiological streams (continuous) and questionnaires (per-condition) operate at different timescales. Fuse them hierarchically:

```
Level 1: Within-trial features
  ├── Mean HRV_RMSSD per trial epoch
  ├── Mean SCL per trial epoch
  └── Fixation count per trial epoch
           ↓ aggregate to condition level
Level 2: Per-condition features
  ├── Mean of trial-level physiological features
  ├── NASA-TLX score (condition-level questionnaire)
  └── Total intervention count across trials
           ↓ statistical analysis at condition level
```

---

### Step 4: Missing Data Across Modalities

Modalities fail independently (sensor dropout, questionnaire skips, technical errors). Handle each differently.

| Missing Pattern | Likely Cause | Strategy |
|----------------|-------------|---------|
| Entire participant missing a modality | Sensor failure, participant declined | Exclude participant from that modality's analysis only (not full exclusion); report N per modality |
| Random missing trials | Noise, artefact rejection | Within-participant mean imputation OR multiple imputation (mice) |
| Systematic missingness (e.g., always missing in condition B) | Equipment issue | Exclude trials; check for differential attrition |
| Physiological artefact epochs | Movement, electrode pop | Artefact rejection → interpolate short gaps (< 5 s) or exclude epoch |

```python
# Multiple imputation for missing trial-level features
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

imputer = IterativeImputer(max_iter=10, random_state=42)
features_imputed = imputer.fit_transform(features[feature_cols])

# Always check: is missingness random (MCAR) or systematic (MAR/MNAR)?
import missingno as msno
msno.matrix(features)   # visual pattern of missingness
```

---

### Step 5: Cross-Modal Convergent Validity

Before running your main analysis, verify that modalities agree on the direction of effects they are supposed to share.

**Expected convergence in workload studies**:
- ↑ NASA-TLX mental demand → ↓ HRV_RMSSD (physiological workload)
- ↑ NASA-TLX mental demand → ↑ EEG theta power (frontal)
- ↑ Task difficulty condition → ↑ fixation count on critical AOI

```python
import pingouin as pg

# Convergent validity: NASA-TLX vs HRV_RMSSD
corr = pg.corr(features["nasa_mental"], features["hrv_rmssd"], method="pearson")
print(corr[["r", "CI95%", "p-val"]])

# If correlation is near zero or wrong direction:
# - Suspect measurement validity of one modality
# - Check synchronisation (alignment error?)
# - Check preprocessing (wrong epoch window?)
# Do NOT proceed to main analysis until convergence is satisfactory
```

**Convergent validity benchmarks for HRI**:

| Pair | Expected r | If r < 0.2 |
|------|-----------|-----------|
| NASA-TLX total ↔ HRV_RMSSD | −0.3 to −0.6 | Check signal quality and epoch alignment |
| NASA-TLX mental ↔ EEG theta | +0.3 to +0.5 | Check electrode placement and band definition |
| Subjective trust ↔ intervention frequency | −0.3 to −0.5 | Check trust scale validity for task type |
| EDA mean SCL ↔ NASA-TLX frustration | +0.2 to +0.4 | EDA is weak correlate; acceptable if other modalities converge |

---

### Multimodal Fusion Checklist

- [ ] All streams have a shared timestamp or anchor event
- [ ] Synchronisation lag measured and < 100 ms (document actual value)
- [ ] Each modality preprocessed and validated independently (artefact check, signal quality)
- [ ] Feature extraction epoch windows match task structure
- [ ] Missing data pattern assessed (MCAR test or visual inspection)
- [ ] Missing data handled before fusion (not after)
- [ ] Features normalised within-participant before concatenation
- [ ] Convergent validity checked across modality pairs
- [ ] Fusion strategy documented with rationale (early / late / hybrid)
- [ ] Dimensionality reduction reported (if used): method, components retained, variance explained

---

## Stage 7: Statistical Analysis

### Full Analysis Pipeline

```
1. Data quality & exclusion
   ├── Apply pre-registered exclusion criteria
   ├── Verify N per modality and condition
   └── Document all exclusions with reasons

2. Descriptive statistics
   ├── Table 1: demographics + baseline measures
   ├── Per-condition means, SD, 95% CI
   └── Violin or raincloud plots (preferred over bar charts)

3. Assumption checks
   ├── Normality: Shapiro-Wilk (n ≤ 50), Kolmogorov-Smirnov (n > 50), QQ-plot
   ├── Homogeneity of variance: Levene's test (between) or Mauchly's (within)
   └── Independence: confirm no cross-contamination between conditions

4. Primary inferential tests (select from guide below)

5. Effect sizes (mandatory alongside every p-value)

6. Post-hoc comparisons (if omnibus significant)

7. Advanced analyses (as warranted by RQ)
   ├── Linear mixed-effects model (LMM)
   ├── Mediation / moderation
   ├── Bayesian analysis
   └── Time-series analysis

8. Reliability checks
   ├── Internal consistency (Cronbach's α, McDonald's ω)
   └── Inter-rater reliability (κ, ICC)

9. Qualitative analysis (if collected)
```

---

### 7.1 Statistical Test Selection

| Design | DV type | Test | Python |
|--------|---------|------|--------|
| 2 groups, between-subjects | Continuous | Independent t-test | `scipy.stats.ttest_ind` |
| 2 conditions, within-subjects | Continuous | Paired t-test | `scipy.stats.ttest_rel` |
| ≥3 groups, between-subjects | Continuous | One-way ANOVA + Tukey HSD | `pingouin.anova` + `pairwise_tukey` |
| ≥3 conditions, within-subjects | Continuous | RM-ANOVA + Bonferroni | `pingouin.rm_anova` + `pairwise_tests` |
| 2+ factors, mixed | Continuous | Mixed ANOVA | `pingouin.mixed_anova` |
| Repeated measures + missing data | Continuous | **Linear mixed-effects model (LMM)** | `statsmodels.MixedLM` / `pymer4` |
| 2 groups | Ordinal / non-normal | Mann-Whitney U | `scipy.stats.mannwhitneyu` |
| 2 conditions | Ordinal / non-normal | Wilcoxon signed-rank | `scipy.stats.wilcoxon` |
| ≥3 groups, non-parametric | Ordinal | Kruskal-Wallis + Dunn | `scipy.stats.kruskal` + `scikit_posthocs.posthoc_dunn` |
| ≥3 conditions, non-parametric | Ordinal | Friedman + Wilcoxon pairwise | `scipy.stats.friedmanchisquare` |
| Binary outcome | — | Fisher's exact / χ² | `scipy.stats.fisher_exact` |
| Causal pathway | Continuous | Mediation analysis | `pingouin.mediation_analysis` |
| Interaction effect (moderation) | Continuous | Moderation (regression with interaction term) | `statsmodels.OLS` |
| Small N, uncertainty quantification | Any | Bayesian analysis (Bayes factor / ROPE) | `pingouin` BF, `pymc` |
| Continuous time-series | Continuous | LMM with time predictor / DTW distance | `statsmodels.MixedLM` |

**Likert scale decision rule**: treat as interval (parametric) if scale has ≥5 points, distribution is approximately normal (Shapiro-Wilk p > 0.05 or n > 30 invoking CLT), and the subscale has ≥3 items averaged together. For single Likert items, always use non-parametric.

---

### 7.2 Effect Size Reference

| Test | Effect size metric | Small | Medium | Large |
|------|--------------------|-------|--------|-------|
| t-test | Cohen's d | 0.2 | 0.5 | 0.8 |
| ANOVA / RM-ANOVA | Cohen's f | 0.1 | 0.25 | 0.4 |
| ANOVA / RM-ANOVA | η²p (partial eta²) | 0.01 | 0.06 | 0.14 |
| LMM | Marginal R² (fixed effects) | 0.02 | 0.13 | 0.26 |
| Correlation | Pearson / Spearman r | 0.1 | 0.3 | 0.5 |
| χ² / Fisher | Cramér's V | 0.1 | 0.3 | 0.5 |
| Mann-Whitney | rank-biserial r | 0.1 | 0.3 | 0.5 |

Report effect sizes for every test — not just significant ones. Non-significant results with large effect sizes signal underpowered studies worth noting.

---

### 7.3 Multiple Comparisons

| Strategy | When | Formula |
|----------|------|---------|
| **Bonferroni** | Small number of pre-planned comparisons | α_adj = 0.05 / k |
| **Holm-Bonferroni** | Pre-planned; less conservative than Bonferroni | Sequential: sort p-values, apply 0.05/(k−i) |
| **FDR (Benjamini-Hochberg)** | Many exploratory comparisons (≥10) | q-value threshold |
| **No correction** | Single primary outcome with secondary exploratory | Label exploratory tests explicitly |

```python
from statsmodels.stats.multitest import multipletests

p_values = [0.02, 0.04, 0.08, 0.001, 0.15]
reject, p_corrected, _, _ = multipletests(p_values, alpha=0.05, method="holm")
# method options: "bonferroni", "holm", "fdr_bh", "fdr_by"
```

---

### 7.4 Linear Mixed-Effects Models (LMM)

**Use LMM instead of RM-ANOVA when**:
- You have missing data (LMM handles missing data under MAR assumption; RM-ANOVA requires listwise deletion)
- Observations are not equally spaced in time
- You have multiple random effects (e.g., participant AND task item)
- You want to include continuous covariates (expertise, age)
- You are modelling trial-level data nested within participants

```python
import statsmodels.formula.api as smf
import pandas as pd

# Data structure: one row per trial
# Columns: participant_id, condition, trial, workload (DV), prior_experience (covariate)

model = smf.mixedlm(
    "workload ~ condition + prior_experience",  # fixed effects
    data=df,
    groups=df["participant_id"],               # random intercept per participant
    # Optional: random slope for condition per participant:
    # re_formula="~condition"
)
result = model.fit(reml=True)
print(result.summary())

# Report: fixed effect estimate (β), SE, z, p-value
# Compute marginal R² (variance explained by fixed effects)
```

**Using pymer4 (R lme4 via Python) for more complex models**:

```python
from pymer4.models import Lmer

# Random intercept + random slope (most common in HRI)
model = Lmer(
    "workload ~ condition + (1 + condition | participant_id)",
    data=df
)
model.fit()
print(model.coefs)         # fixed effects table
print(model.ranef_var)     # random effects variance
model.plot_summary()
```

**Choosing random effects structure**:

| Structure | Formula | When |
|-----------|---------|------|
| Random intercept only | `(1 \| participant)` | Participants differ in baseline DV level |
| Random intercept + slope | `(1 + condition \| participant)` | Participants also differ in how much they respond to condition |
| Crossed random effects | `(1 \| participant) + (1 \| task_item)` | Both participants and task items vary |

Start with the maximal justified model (random intercept + slope) and simplify if it fails to converge.

**Model comparison** (to test significance of fixed effects):

```python
from pymer4.models import Lmer

m0 = Lmer("workload ~ 1 + (1 | participant_id)", data=df)
m1 = Lmer("workload ~ condition + (1 | participant_id)", data=df)
m0.fit(REML=False)
m1.fit(REML=False)

# Likelihood ratio test
from scipy.stats import chi2
LRT_stat = -2 * (m0.logLike - m1.logLike)
p_LRT = chi2.sf(LRT_stat, df=1)
print(f"χ²({1}) = {LRT_stat:.2f}, p = {p_LRT:.4f}")
```

---

### 7.5 Mediation Analysis

Use when you hypothesise a causal chain: **IV → Mediator → DV**.

**Example HRI hypothesis**: Autonomy level → Trust → Intervention frequency
- IV (X): Autonomy condition (0 = teleoperation, 1 = shared autonomy)
- Mediator (M): Trust score (post-condition)
- DV (Y): Intervention frequency (count)

```
X ──────────────────────────────────► Y   (total effect c)
 \                                   ▲
  a (X→M)    M (trust)    b (M→Y)  /
   └──────────────────────────────┘
                (indirect effect a×b)
```

```python
import pingouin as pg

results = pg.mediation_analysis(
    data=df,
    x="condition",        # IV
    m="trust_score",      # Mediator
    y="n_interventions",  # DV
    n_boot=5000,          # bootstrap for CIs
    seed=42,
)
print(results)
# Key outputs:
#   Direct effect (c'): X → Y controlling for M
#   Indirect effect (a×b): 95% bootstrap CI; if CI excludes 0 → significant mediation
#   Total effect (c = c' + a×b)
```

**Interpreting mediation**:

| Pattern | Interpretation |
|---------|----------------|
| c significant, c' non-significant, a×b CI excludes 0 | Full mediation |
| c significant, c' still significant, a×b CI excludes 0 | Partial mediation |
| a×b CI includes 0 | No mediation |
| c non-significant | No total effect to mediate — revisit theory |

**For multiple mediators** (e.g., trust AND situational awareness both mediate):
Use `pingouin.mediation_analysis` with multiple `m` variables, or use the `lavaan` package via R/rpy2 for structural equation modelling.

---

### 7.6 Moderation Analysis

Use when you hypothesise that the effect of IV on DV **depends on** a third variable (the moderator).

**Example**: The effect of autonomy level on workload is moderated by operator expertise.

```
IV (autonomy) ────────────────► DV (workload)
                    ↑
              Moderator (expertise)
```

```python
import statsmodels.formula.api as smf

# Centre variables before creating interaction (reduces multicollinearity)
df["condition_c"] = df["condition"] - df["condition"].mean()
df["expertise_c"] = df["expertise_years"] - df["expertise_years"].mean()
df["interaction"] = df["condition_c"] * df["expertise_c"]

model = smf.ols("workload ~ condition_c + expertise_c + interaction", data=df).fit()
print(model.summary())

# If interaction term (β₃) is significant → moderation confirmed
# Simple slopes analysis: re-run at expertise ± 1 SD
```

**Simple slopes** (to interpret a significant interaction):

```python
high_exp = df["expertise_years"].mean() + df["expertise_years"].std()
low_exp  = df["expertise_years"].mean() - df["expertise_years"].std()

for level, val in [("High expertise", high_exp), ("Low expertise", low_exp)]:
    df_sub = df.copy()
    df_sub["expertise_c"] = val - df["expertise_years"].mean()
    df_sub["interaction"] = df_sub["condition_c"] * df_sub["expertise_c"]
    res = smf.ols("workload ~ condition_c + expertise_c + interaction", data=df_sub).fit()
    print(f"{level}: β(condition) = {res.params['condition_c']:.3f}, p = {res.pvalues['condition_c']:.4f}")
```

---

### 7.7 Bayesian Analysis

Use Bayesian analysis when:
- Sample size is small (n < 20 per group) and you want to quantify evidence, not just reject H0
- You want to distinguish "no effect" from "not enough data to tell"
- Reviewers or the field expect Bayes factors alongside NHST

#### Bayes Factors (BF) with pingouin

```python
import pingouin as pg

# Bayesian paired t-test
result = pg.ttest(df[df.condition=="A"]["workload"],
                  df[df.condition=="B"]["workload"],
                  paired=True,
                  alternative="two-sided")
print(result[["T", "dof", "p-val", "cohen-d", "BF10"]])

# BF10 interpretation:
#   BF10 > 100  → decisive evidence for H1
#   BF10 30–100 → very strong evidence for H1
#   BF10 10–30  → strong evidence for H1
#   BF10 3–10   → moderate evidence for H1
#   BF10 1–3    → anecdotal evidence for H1
#   BF10 ~ 1    → no evidence either way
#   BF10 < 1/3  → moderate evidence for H0 (no effect)
```

#### ROPE (Region of Practical Equivalence)

Declare in advance a smallest effect size of interest (SESOI) for your construct. If the posterior 95% credible interval falls entirely within the ROPE → accept H0 with confidence.

```python
import arviz as az
import pymc as pm
import numpy as np

with pm.Model() as model:
    mu_diff = pm.Normal("mu_diff", mu=0, sigma=10)   # prior on mean difference
    sigma   = pm.HalfNormal("sigma", sigma=5)
    obs     = pm.Normal("obs", mu=mu_diff, sigma=sigma,
                        observed=df["workload_A"] - df["workload_B"])
    trace = pm.sample(2000, tune=1000, return_inferencedata=True)

# Check if 95% HDI falls within ROPE (e.g., [-0.2, 0.2] for Cohen's d)
az.plot_posterior(trace, var_names=["mu_diff"], rope=(-0.2, 0.2))
```

---

### 7.8 Time-Series & Continuous Stream Analysis

For continuous physiological or robot state data captured across a session.

#### Epoch-Based Analysis

The most common approach: segment continuous streams into task-relevant epochs, extract scalar features per epoch, then apply standard tests.

```python
import numpy as np

def extract_epoch_features(signal, sr, epoch_onsets_s, epoch_duration_s):
    """Extract per-epoch features from a 1-D signal."""
    epochs = []
    for onset in epoch_onsets_s:
        start = int(onset * sr)
        end   = int((onset + epoch_duration_s) * sr)
        epoch = signal[start:end]
        epochs.append({
            "mean": np.mean(epoch),
            "std":  np.std(epoch),
            "max":  np.max(epoch),
            "auc":  np.trapz(epoch) / sr,  # area under curve
        })
    return pd.DataFrame(epochs)
```

#### Dynamic Time Warping (DTW) for Trajectory Comparison

Use when comparing temporal patterns (e.g., workload trajectories across conditions) rather than scalar summaries.

```python
from dtaidistance import dtw, dtw_visualisation as dtwvis
import numpy as np

# Compare EDA time-series between two conditions for one participant
eda_a = np.array([...])  # EDA signal during condition A
eda_b = np.array([...])  # EDA signal during condition B

distance = dtw.distance(eda_a, eda_b)
path = dtw.warping_path(eda_a, eda_b)
dtwvis.plot_warping(eda_a, eda_b, path)

# Group-level: DTW distance matrix across participants
distances = dtw.distance_matrix_fast(np.stack([eda_a_all, eda_b_all]))
```

#### Change-Point Detection (detecting state transitions)

Useful for adaptive autonomy studies — detecting when operator mental state shifts.

```python
import ruptures as rpt

# Detect change points in EDA signal (e.g., workload transitions)
model = rpt.Pelt(model="rbf").fit(eda_signal.reshape(-1, 1))
breakpoints = model.predict(pen=10)  # pen: higher = fewer breakpoints
rpt.display(eda_signal, breakpoints)
```

---

### 7.9 Reliability & Inter-Rater Agreement

Required whenever two or more raters code qualitative data (video, transcripts, behaviour logs).

#### Internal Consistency (Scale Reliability)

```python
import pingouin as pg

# Cronbach's alpha for a scale (e.g., 12-item trust scale)
trust_items = df[["trust_q1", "trust_q2", ..., "trust_q12"]]
alpha = pg.cronbach_alpha(data=trust_items)
print(f"Cronbach's α = {alpha[0]:.3f}, 95% CI = {alpha[1]}")

# Interpret: α ≥ 0.70 acceptable; ≥ 0.80 good; ≥ 0.90 excellent
# Also compute McDonald's ω (more robust for non-tau-equivalent items):
# Use factor_analyzer or semopy packages
```

#### Inter-Rater Reliability

| Data Type | Metric | Rule of Thumb |
|-----------|--------|---------------|
| Nominal categories | Cohen's κ | κ ≥ 0.61 substantial; ≥ 0.81 almost perfect |
| Ordinal ratings | Weighted Cohen's κ | Same thresholds |
| Continuous ratings | Intraclass Correlation (ICC) | ICC ≥ 0.75 good; ≥ 0.90 excellent |
| Multiple raters, nominal | Fleiss' κ | Same as Cohen's κ |

```python
import pingouin as pg
from sklearn.metrics import cohen_kappa_score

# Cohen's κ for two raters on nominal categories (e.g., behaviour codes)
rater1 = ["help-seeking", "monitor", "monitor", "takeover", "monitor"]
rater2 = ["help-seeking", "takeover", "monitor", "takeover", "monitor"]
kappa = cohen_kappa_score(rater1, rater2)
print(f"Cohen's κ = {kappa:.3f}")

# ICC for two raters on continuous scores (e.g., engagement rating 1–7)
ratings = pd.DataFrame({"rater1": [4, 5, 3, 6, 4], "rater2": [4, 4, 3, 5, 5]})
icc = pg.intraclass_corr(data=ratings.melt(var_name="rater", value_name="score")
                                      .assign(target=list(range(5)) * 2),
                          targets="target", raters="rater", ratings="score")
print(icc)
# Use ICC(2,1) for absolute agreement, ICC(3,1) for consistency
```

**Resolve disagreements before analysis**: raters should discuss all disagreements and reach consensus. Run a second reliability check after the discussion round.

---

### 7.10 Qualitative Analysis

| Method | When | Output |
|--------|------|--------|
| **Thematic analysis** (Braun & Clarke 2006) | Inductive coding of interviews/open-responses | Theme map + quotes |
| **Content analysis** | Counting predefined category occurrences | Frequency table |
| **Grounded theory** | Building theory from data (no prior framework) | Theoretical model |
| **Interaction analysis** | Fine-grained video coding (gaze, gesture, turn-taking) | Coded timeline |
| **Discourse analysis** | Human-robot dialogue structure and pragmatics | Dialogue patterns |

**Mixed-methods integration**: run quantitative and qualitative analyses independently, then triangulate at the interpretation stage. Identify where they converge (strengthen claims) and diverge (discuss as limitation or nuance).

---

### 7.11 Pre-registration

Pre-register hypotheses, design, primary outcome, and analysis plan **before** data collection.

- **OSF** (osf.io): free, DOI-minted, standard for HRI/CHI
- **AsPredicted** (aspredicted.org): shorter form, useful for confirmatory tests

Pre-registration distinguishes confirmatory from exploratory analyses — call out unplanned tests explicitly in the paper. Reviewers at HRI, CHI, and RA-L increasingly flag unpre-registered analyses as exploratory.

---

### Statistical Analysis Reporting Checklist

- [ ] Test chosen matches design and DV type (see selection guide)
- [ ] Assumptions checked and reported (normality, homogeneity, sphericity)
- [ ] Effect size reported for every test (d, η²p, r, BF10, etc.)
- [ ] 95% CI reported alongside point estimates
- [ ] Multiple comparison correction applied and method stated
- [ ] LMM used for repeated measures with missing data (not RM-ANOVA with listwise deletion)
- [ ] Mediation: bootstrap CI reported (not Sobel test); n_boot ≥ 5000
- [ ] Moderation: interaction term in model; simple slopes plotted
- [ ] Bayes factor reported for small-N or null results
- [ ] Inter-rater reliability reported (κ or ICC) for all coded data; κ ≥ 0.61 before proceeding
- [ ] Pre-registered vs. exploratory tests labelled in the paper

---

## Stage 8: Reporting & Dissemination

### HRI Paper Structure

| Section | Content |
|---------|---------|
| **Introduction** | Motivation, RQ, contributions |
| **Related Work** | Prior HRI studies on the topic; gaps addressed |
| **System / Robot Description** | Platform, capabilities, implementation |
| **Study Design** | Design type, conditions, participants, procedure |
| **Measures** | Each DV, instrument citation, when administered |
| **Results** | Descriptive stats → assumption checks → inferential stats → effect sizes |
| **Discussion** | Interpret results relative to hypotheses; limitations; implications |
| **Conclusion** | Summary of contributions |

### Reporting Checklist (CONSORT-adapted for HRI)

- [ ] Sample size and power analysis reported
- [ ] Participant flow diagram (recruited → excluded → analysed)
- [ ] Demographics table (age, gender, prior robot experience)
- [ ] All DVs and instruments cited (with psychometric properties)
- [ ] Analysis plan stated (ideally pre-registered)
- [ ] Assumption checks reported
- [ ] Effect sizes reported for all inferential tests
- [ ] Confidence intervals reported where appropriate
- [ ] Deviations from protocol reported
- [ ] Ethics approval statement
- [ ] Data availability statement (open data encouraged)

### Key HRI Venues

| Venue | Type | Acceptance Rate |
|-------|------|-----------------|
| ACM/IEEE HRI | Conference (flagship) | ~20–25% |
| RO-MAN | Conference | ~30% |
| ICSR | Conference (social robots) | ~35% |
| IJSR | Journal | varies |
| THRI (ACM) | Journal | varies |
| HRI Late-Breaking | Short papers / posters | higher |
| CHI | Conference (broader UX) | ~25% |
| RA-L + ICRA/IROS | Journal + conference | varies |

---

## HRI-Specific Design Patterns

### Adaptive / Variable Autonomy Studies

For studies involving autonomy adjustment (shared autonomy, adjustable autonomy):

1. **Define autonomy levels explicitly**: what the robot does at each level (e.g., Level 0 = teleoperation, Level 3 = full autonomy)
2. **Control initiative**: who can initiate autonomy changes — human, robot, or both?
3. **Measure transition behaviour**: when and why participants switch levels
4. **Confound risk**: avoid conflating robot capability changes with interface changes when switching autonomy levels
5. **Outcome measures**: intervention frequency, task performance per level, workload per level, trust calibration

### LLM-Based HRI Studies

When the robot uses an LLM for dialogue, planning, or intent inference:

1. **Latency**: LLM inference latency may itself affect UX — measure and report
2. **Consistency**: LLM output varies across runs — log all prompts and responses; use temperature = 0 for reproducibility in pilots
3. **Confound**: participants may anthropomorphise more with natural language — account for this in trust/acceptance analysis
4. **Ground truth**: define ground truth for intent classification if testing accuracy
5. **Failure modes**: what happens when LLM produces wrong output? Include failure trials in design

### Expert Participant Studies (Mining, Agriculture, SAR)

When recruiting domain experts rather than naive users:

1. **Recruitment is harder** — plan 4–8 weeks; leverage partner organisations
2. **Smaller N is acceptable** if justified (hard-to-reach population) — typically n = 8–15 per group for exploratory studies
3. **Expertise as a variable**: stratify or measure prior experience as a covariate
4. **Ecological validity matters more**: use real or realistic operational scenarios
5. **Session flexibility**: experts have limited availability — design flexible 45–60 min sessions
6. **Debrief value**: expert participants often provide rich qualitative insights — plan semi-structured debrief

### Simulated Users in HRI (Wizard of Oz / Agent-Based)

When using simulated users (agent or human proxy) to test robot systems:

1. **Validity claim**: be explicit about what the simulated user models and what it does not
2. **Behavioural fidelity**: validate simulated user behaviour against real participant data where possible
3. **Parameter space exploration**: simulated users allow testing conditions impractical with human participants (e.g., edge cases, high trial counts)
4. **Report as simulation**: always disclose in methods; do not conflate with human participant results

---

## Common HRI Methodology Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| **Underpowered study** | Large variance, non-significant trends | Power analysis before recruitment; add participants |
| **Demand characteristics** | Participants guess the hypothesis and behave accordingly | Use cover story or within-subjects counterbalancing |
| **Novelty effect** | Participants respond positively to any robot, regardless of condition | Include familiarisation period; longitudinal follow-up |
| **Automation complacency** | Baseline autonomy level affects results | Counterbalance order; allow task familiarisation |
| **Experimenter bias** | Researcher's presence or behaviour influences participants | Standardise experimenter script; use video instructions |
| **Missing data strategy not defined** | Post-hoc exclusion choices inflate false positives | Pre-register exclusion and imputation criteria |
| **Confounded conditions** | IV and platform capability change together | Decouple IV from platform using simulation or WoZ |
| **No manipulation check** | Conditions may not differ as intended | Include manipulation check items (e.g., "how autonomous did the robot seem?") |
| **Questionnaire fatigue** | Participants rush through long questionnaires | Limit to 2–3 questionnaires per condition; use short validated scales |
| **No debrief for WoZ** | Participants feel deceived post-study | Always debrief WoZ after data collection |

---

## Usage Instructions for Agents

### Choosing a Mode

| Situation | Mode | What to do |
|---|---|---|
| User describes a new study or research scenario | **Auto-Design** | Create workspace, run generation pipeline, output `progress-report.html` |
| User asks a specific methodology question | **Advisory** | Answer using the relevant lifecycle stage below |
| User shares data for analysis | **Advisory** | Apply Stage 6.5 (fusion) and Stage 7 (statistics) guidance |
| User is writing up a paper | **Advisory** | Apply Stage 8 reporting checklists |

**Default to Auto-Design mode.** If in doubt, create the workspace and start generating — it is always easier for the user to redirect than to pull methodology knowledge from a conversation.

### Advisory Mode Checklist

When answering specific methodology questions:

1. **Identify the lifecycle stage**: which stage are they at? Tailor advice accordingly.
2. **Clarify the RQ**: if vague, apply the PICO framework to sharpen it (≤ 2 clarifying questions).
3. **Recommend design**: match design type to research question; justify choice; flag carry-over risk.
4. **Select measures**: map DVs to validated instruments with citations; warn against over-instrumenting (max 3 questionnaires per condition).
5. **Flag ethics gate**: ethics approval is a hard gate — no participant contact without it.
6. **Power analysis**: always run before recruitment; use the code templates in Stage 5.
7. **Anticipate confounds**: identify the top 2–3 risks from the pitfalls table; suggest mitigations.
8. **Fusion pipeline**: for multimodal studies, walk through Stage 6.5 Steps 1–5 in order — synchronisation first, convergent validity last.
9. **Statistical test selection**: use the table in §7.1; default to LMM over RM-ANOVA for repeated-measures with any missing data.
10. **Mediation vs. moderation**: mediation = "how/why does X affect Y?"; moderation = "when/for whom?" — clarify which the RQ implies before running analysis.
11. **Reporting**: reference both the §7 statistical checklist and the §8 CONSORT-adapted checklist.

**Key principles**:
- Validity: internal > external for causal claims; external > internal for deployment-oriented studies
- Participant welfare first — robot safety protocols are non-negotiable
- Multimodal data: check convergent validity before drawing conclusions from any single modality
- Transparency: distinguish confirmatory (pre-registered) from exploratory analyses in the paper
- Open science: pre-register, share data and instruments, report effect sizes even for null results
