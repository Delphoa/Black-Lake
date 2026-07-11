---
title: "BEAGLE Learner - DEP-E"
generated_at: "2026-07-10"
artifact_type: "DEP research artifact"
primary_subject: "Source-first review of BEAGLE, a neuro-symbolic learner-simulation framework for realistic novice programming trajectories."
source_status: "mixed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-10"
temporal_cutoff: "arXiv version 2 updated 2026-05-05; repository context inspected 2026-07-10"
primary_url: "https://arxiv.org/abs/2602.13280"
stable_identifier: "arXiv:2602.13280v2"
confidence_summary: "Medium-high: arXiv metadata and source package were inspected directly, but code, datasets, and human-study raw data were not available from inspected sources."
safety_scope: "educational, privacy-preserving, evaluation-oriented"
distribution_notes: "Public URLs and repository-relative paths only; local execution context withheld."
---

# BEAGLE Learner - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | BEAGLE arXiv record | Primary paper metadata | arXiv abstract/API record | arXiv:2602.13280v2 | https://arxiv.org/abs/2602.13280 | Public arXiv metadata; DOI not exposed by inspected metadata. | 2026-07-10 | Inspected |
| S2 | BEAGLE arXiv source package | Primary paper source | LaTeX source package | arXiv:2602.13280v2 | https://arxiv.org/e-print/2602.13280v2 | Public source package inspected for review; not redistributed. | 2026-07-10 | Inspected |
| S3 | Local archive metadata README | Local metadata pointer | Markdown metadata | arXiv:2602.13280 | Repository-external local archive metadata, public path withheld | Used only to identify the public arXiv record and PDF presence. | 2026-07-10 | Inspected |
| S4 | Black-Lake README | Repository standard | Markdown | main branch | https://raw.githubusercontent.com/Delphoa/Black-Lake/main/README.md | Output repository DEP-E, report, log, and attribution rules. | 2026-07-10 | Inspected |
| S5 | Black-Lake-Data README | Related repository standard | Markdown | main branch | https://github.com/Delphoa-Labs/Black-Lake-Data | Related source DEP and attribution rules. | 2026-07-10 | Inspected |
| S6 | Local AI Stack DEP-E | Related DEP entry | Markdown manuscript | DEP-E-20260709-Local AI Stack | Delphoa/Black-Lake/.lake-data/DEP-E-20260709-Local AI Stack/local-ai-research.md | Public repository-relative artifact. | 2026-07-10 | Inspected |
| S7 | Tech Intel 0101 DEP-E | Related DEP entry | Markdown manuscript | DEP-E-20260710-Tech Intel 0101 | Delphoa/Black-Lake/.lake-data/DEP-E-20260710-Tech Intel 0101/tech-intel-0101-research.md | Public repository-relative artifact. | 2026-07-10 | Inspected |
| S8 | Tech Intel 1102 source DEP | Related DEP entry | Markdown findings artifact | DEP-20260702-Tech Intel 1102 | Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260702-Tech Intel 1102/daily_research_findings_2026-07-02_1102.md | Public repository-relative artifact. | 2026-07-10 | Inspected |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary arXiv record | Title, authors, publication date, update date, version, subject category, abstract, and absence of DOI in inspected metadata. | Bibliographic identity and core abstract claims. | High | Abstract cannot validate all experimental details. |
| E2 | S2 | Primary source package | Main paper source, appendix, prompt appendix, bibliography, source README, and figure inventory. | Method, evaluation design, metrics, ablations, and limitations. | High | LaTeX extraction is imperfect; figures were listed but not visually reinterpreted. |
| E3 | S2 | Main evaluation table | Particle Simulator metrics: BEAGLE `D_KL=0.31`, `D_debug=0.02`, `P_Recur=86.2%`, realism `2.44/3`, solve rate `10%`. | Behavioral, epistemic, and perceptual fidelity claims. | Medium | Metrics were not reproduced; table context comes from source package. |
| E4 | S2 | Human Turing test appendix | `N=71` participants, `852` observations, 52.8% accuracy, `d'=0.15`, TOST result reported by authors, participant feedback notes. | Human perceptual-fidelity claim. | Medium | Stimuli and raw responses were not available; protocol involves breakdown from sparse LLM outputs. |
| E5 | S2 | Method sections and appendix | Semi-Markov controller, BKT parameters, Explicit Flaw Injection, Strategist/Executor split, observation gating, and prompt blocks. | Mechanism of action and implementation interpretation. | High | No runnable code repository was identified. |
| E6 | S4, S5 | Repository standards | DEP placement, short-description limit, README contents, attribution-block rules, and source handling. | Deposit structure and public-safe provenance handling. | High | Process evidence, not technical paper evidence. |
| E7 | S6-S8 | Related DEP entries | Agent memory, secure state, early-abort/evidence-state control, reversible context management, and real-device agent evaluation summaries. | Related-entry synthesis and conceptual bridge. | Medium | Related entries are prior generated artifacts; they were treated as contextual evidence, not authority for BEAGLE claims. |
| E8 | Marker scans across Black-Lake, Black-Lake-Data, and automation memory | Repository status evidence | No matches for arXiv ID, normalized title, or BEAGLE learner slug; zero 24-hour same-paper markers. | Dedup/reselection validation. | High | Limited to repository and memory state available during this run. |

## Executive Summary

BEAGLE is a source-first learner-simulation paper about making LLM agents behave like novice students rather than optimized solvers. The authors argue that ordinary LLM student simulators exhibit competency bias: even when prompted to be novices, they tend to solve quickly, skip the messy trial-and-error loops of learning, and silently use knowledge the simulated student should not have. BEAGLE addresses this by adding explicit controls around behavior timing, knowledge state, observation access, and generation roles.

The paper's contribution is best understood as trajectory governance for synthetic learners. A semi-Markov controller governs metacognitive and cognitive states, Bayesian Knowledge Tracing tracks concept mastery, Explicit Flaw Injection blocks unavailable concepts, and a Strategist/Executor split prevents the generator from quietly repairing errors. The evaluation reports stronger fidelity to real learner traces than several baselines, including a main Particle Simulator result with `D_KL=0.31`, debug divergence `0.02`, recurrence `86.2%`, and realism `2.44/3`.

Reviewer confidence is medium-high for the paper's identity, architecture, and reported metrics because arXiv metadata and source files were inspected directly. Confidence is lower for reproducibility and real-world deployment because no official code repository, public raw student data, or runnable benchmark package was identified. The safest downstream use is as a research design and evaluation pattern for synthetic learner trajectories, not as proof that simulated students can replace human learning studies.

Random selection methodology and dedup validation were completed before review. The run enumerated 75,438 paper units using `rg --files -g "*.pdf"`, selected uniform random index 61,883, accepted `arXiv:2602.13280` on the first draw, and found zero duplicate or same-paper markers in Black-Lake artifacts, Black-Lake-Data context, or automation memory.

## Detailed Summary

### Problem Context

Educational AI needs authentic student data for tutoring systems, intervention design, and stress testing, but the paper notes that real data collection is constrained by privacy regulation, IRB and consent requirements, longitudinal cost, and ethical risk when experimenting with learners. Synthetic learners are attractive because they could let researchers test pedagogical strategies before deploying them with students.

The paper's central problem is that LLMs are not naturally novice-like. Preference-tuned models tend to optimize for correct and efficient answers. For programming tasks, that means they often build complete solutions quickly instead of showing the loops real learners display: partial plans, flawed attempts, execution feedback, confusion, debugging, reflection, and repeated error recurrence.

### Mechanism

BEAGLE uses Self-Regulated Learning theory as the conceptual scaffold. It represents student behavior with metacognitive states and cognitive states. The semi-Markov controller lets states persist for non-geometric durations, which matters because learners can get stuck or remain in debugging loops. Symbolic control samples the current behavior state and knowledge constraints at each step.

The knowledge model is Bayesian Knowledge Tracing. Mastery is tracked per knowledge component using standard BKT parameters from prior work: initial mastery `0.10`, learning rate `0.25`, slip `0.05`, and guess `0.20`. Mastery is discretized into low, medium, and high bands for prompt injection.

Explicit Flaw Injection is the paper's answer to hidden LLM knowledge. When a concept should be unavailable, the prompt injects a hard constraint that the simulated learner cannot use that concept. The appendix gives examples such as blocking the math library, degree-to-radian conversion, numerical integration, or conditionals. If a concept is blocked, BKT updates for that concept are frozen until tutor-mediated support releases the block.

The Strategist/Executor split is an architectural guard against silent self-correction. The Strategist emits a goal, mindset, and directive; the Executor turns that into code and monologue under the current state constraints. Observation gating further limits what the agent can see. For example, during enacting states, diagnostic feedback can be hidden so the simulated learner remains in realistic trial-and-error loops.

### Evaluation

The evaluation spans physics, applied math, and computing tasks, including Particle Simulator, Bouncing Ball, Inclined Plane, and Gradient Descent. The paper uses four datasets with distinct roles: the Snyder corpus for semi-Markov calibration, Cohn block-based study traces as behavioral ground truth, a Python pilot study for additional behavioral ground truth and Turing-test stimuli, and the Bielefeld dataset for capture protocol grounding.

Baselines include Vanilla prompting, Chain-of-Thought, Few-Shot, SimStudent, LLM-SS, CoderAgent, and prompt variants that receive BEAGLE's metacognitive prompt without the architectural control. The default table reports Gemini 2.0 Flash with `N=50` simulations and `T=30` steps.

On the main Particle Simulator table, BEAGLE reports a low solve rate of 10% rather than the too-efficient 90-100% behavior of several prompting baselines. That is a feature for the paper's target: the goal is not task performance, but realistic struggle. BEAGLE reports best `D_KL=0.31`, best debug divergence `0.02`, best nonlinearity `0.34`, second-best recurrence `86.2%`, and best overall realism `2.44/3`.

The ablation table supports the importance of semi-Markov control. Removing semi-Markov dynamics increases `D_KL` to `6.81`, while removing the Strategist or Executor changes recurrence and realism. The paper interprets this as evidence that behavior dynamics and role separation matter beyond prompt wording alone.

The human Turing test compares BEAGLE trajectories with real student data. The appendix reports `N=71` participants and 852 observations. Overall accuracy was 52.8%, with `d'=0.15`; the authors apply a TOST equivalence procedure and report a maximum p-value of `0.038`, interpreting this as perceptual equivalence within their margin. The appendix also notes cues that sometimes distinguished AI from real traces, such as docstrings, premature imports, or mechanical switching between methods.

### Limitations

Several limits matter for downstream use. The paper's datasets include IRB-governed and student-derived traces, so public reproducibility is constrained. The source package includes detailed prompts and LaTeX but not a runnable implementation package. The human Turing-test stimuli involve a diff-based breakdown from sparse LLM outputs into denser code progressions, which is reasonable but should be tested carefully because it changes trace presentation. The tutoring case study discussed in the appendix uses small per-condition sample sizes, and the authors explicitly caution against strong human-tutor-design conclusions without validation with real learners.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | BEAGLE addresses LLM competency bias by constraining process, not only final outputs. | Author claim and reviewer interpretation | E1, E5 | Supported by the abstract and method architecture. | High |
| C2 | Semi-Markov behavior control is central to matching real learner trajectory dynamics. | Author claim | E3, E5 | Supported by main metrics and the no-semi-Markov ablation reporting `D_KL=6.81`. | Medium |
| C3 | BKT plus Explicit Flaw Injection enforces knowledge gaps more strongly than prompt-only novice personas. | Author claim and reviewer interpretation | E5 | Mechanism is clear in the appendix; empirical isolation is partial because code/data were not reproduced. | Medium |
| C4 | BEAGLE improves behavioral, epistemic, and perceptual fidelity on the reported Particle Simulator setup. | Author claim | E3 | Supported by inspected table values; not independently reproduced. | Medium |
| C5 | Human raters could not reliably distinguish BEAGLE traces from real student traces under the reported protocol. | Author claim | E4 | Supported by source-package Turing-test statistics; protocol and raw data were not independently inspected. | Medium |
| C6 | The paper is relevant to Black-Lake agent-memory and trajectory-control deposits. | Reviewer synthesis | E7 | Supported by concrete overlap with state, memory, context, and evaluation entries. | Medium |
| C7 | This run did not duplicate an existing BEAGLE arXiv DEP. | Repository status claim | E8 | Marker scans found zero duplicates and zero same-paper 24-hour markers. | High |

## Methodology

- `Research objective`: Randomly select one eligible paper from the local arXiv archive, verify it is not already deposited, review it source-first, and create a Black-Lake log, Report-Mark, and DEP-E manuscript deposit.
- `Sources inspected`: Local metadata README, arXiv API metadata for `2602.13280`, arXiv source package for `2602.13280v2`, live Black-Lake README, live Black-Lake-Data README, and three related DEP entries.
- `Discovery strategy`: Used `rg --files -g "*.pdf"` to enumerate local PDF candidates, grouped candidates by PDF parent directory, selected a uniform random index with PowerShell `Get-Random`, then used arXiv metadata and source-package inspection for paper review.
- `Inclusion criteria`: The selected paper was accepted because it had a public arXiv record, a local PDF unit, nearby metadata, no duplicate markers, and sufficient primary source material in the arXiv source package.
- `Exclusion criteria`: Prior Black-Lake artifacts, same-paper markers within 24 hours, title/ID matches, inaccessible code, and redistributable source collection were excluded from the public deposit.
- `Analytical approach`: Mixed empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication-planning review.
- `Evidence handling`: Author claims are preserved as claims unless supported by inspected source-package methods, tables, or appendices. Reviewer interpretations are labeled separately.
- `Uncertainty handling`: Missing code, private datasets, unavailable raw human-study responses, uninspected rendered figures, and unreproduced metrics are explicitly recorded.
- `Extraction process`: arXiv metadata was read through the public API; source package files were inspected from the public e-print; repository and related DEP files were read as Markdown.
- `Version control`: Output repository default branch was fetched before writing; related source repository was freshly cloned for context inspection.
- `Safety handling`: The artifact treats education and learner data as privacy-sensitive. Examples use synthetic data and avoid claims that synthetic students replace real learner validation.
- `Reviewer stance`: DEP-ready preservation, research critique, implementation translation, and future-review planning.

## Scope, Constraints, and Assumptions

- `Scope`: Review BEAGLE as a learner-simulation and agent-trajectory-control paper, then deposit a public-safe Black-Lake DEP-E artifact.
- `Temporal boundary`: Source review covers arXiv version 2 updated 2026-05-05 and repository context available on 2026-07-10.
- `Evidence limits`: No official code repository, public raw student trace dataset, runnable benchmark package, or DOI was found from inspected metadata and search results. Figures were identified from the source package but not separately interpreted beyond text references.
- `Assumptions`: The arXiv source package corresponds to the latest public paper version exposed by the arXiv API at review time. Absence of duplicate markers means no same-paper Black-Lake DEP existed in inspected locations.
- `Constraints`: Public artifacts must not include local archive paths, local execution timestamps, local timezone labels, usernames, machine names, private data, or restricted student data.
- `Out of scope`: Reproducing experiments, collecting student data, validating tutoring interventions with humans, rendering figures, or deploying BEAGLE in an educational product.
- `Intended use`: DEP deposition, paper review, implementation ideation, research backlog seeding, and semantic linking to related agent-trajectory artifacts.
- `Audience`: Research reviewers, education-AI engineers, tutoring-system designers, agent-evaluation researchers, and Black-Lake automation maintainers.
- `Reproducibility boundary`: Metadata and source-package inspection are reproducible from public arXiv URLs; reported metrics require author code/data or an independent reimplementation.
- `Data sensitivity`: Public paper/source files and public repository artifacts only; student trace data is treated as sensitive and not collected.

## Observations

- `Observed pattern`: BEAGLE shifts student simulation from persona prompting to process control.
- `Observed pattern`: The paper's strongest methodological idea is making knowledge absence operational, not just descriptive.
- `Technical implication`: Agent evaluation should score intermediate behavior traces, not only task success.
- `Technical implication`: Synthetic learner systems need explicit privacy and validity boundaries because they are often motivated by restricted real-student data.
- `Contradiction or tension`: The best simulator for novice behavior may intentionally solve fewer tasks, which can look worse under ordinary model-performance metrics.
- `Open question`: How much of the human Turing-test result depends on the diff-based breakdown mechanism versus the underlying BEAGLE trajectory content?
- `Reviewer hypothesis`: BEAGLE-style state labels could become useful audit metadata for many agent domains where process realism matters.

## Considerations

BEAGLE should be handled as an educational research artifact with privacy-sensitive implications. Synthetic learner traces may reduce the need to expose real student data during early system design, but they can also create false confidence if treated as human substitutes. Any product use should preserve a sharp boundary between simulation-supported stress testing and validated learning outcomes with real students.

The paper also has general agent-engineering relevance. Many agent systems are judged by final task success, but BEAGLE shows that the path can be the object of study. This is directly relevant to tutoring, safety, clinical orchestration, autonomous labs, RAG, and software agents where intermediate states carry risk, evidence, or governance meaning.

Implementation reuse should be cautious. The source package exposes prompts and methods, but no official code repository was identified. Reimplementations should start with synthetic tasks, transparent state logs, and clear safeguards against using simulated behavior for high-stakes educational decisions.

## Strengths

- The paper targets an important failure mode in LLM simulation: models can act competent even when asked to role-play incompetence.
- The architecture combines symbolic state, knowledge tracing, perceptual gating, and neural generation in a way that is inspectable.
- The evaluation uses multiple fidelity dimensions instead of optimizing only answer correctness.
- The appendix provides substantial implementation detail, including BKT behavior, Explicit Flaw Injection, prompt blocks, and human Turing-test protocol.
- The work has clear transfer value for process-level agent evaluation beyond education.

## Weaknesses

- No official code repository was identified from inspected sources, limiting immediate reproducibility.
- The relevant human and student datasets are privacy-sensitive and not public from the inspected sources.
- Several results depend on LLM-as-judge metrics, which require careful calibration and can be sensitive to rubric design.
- The human Turing-test presentation uses a breakdown mechanism to transform sparse generated code states into denser progressions.
- The paper's education-specific claims need validation across broader age groups, domains, institutions, and tutoring settings.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release a minimal runnable simulator | Reproducibility | The paper source has detailed method descriptions but no identified official code. | Enables independent smoke tests and metric checks. | Must avoid releasing restricted student data. | Provide synthetic tasks, public fixtures, and deterministic seeds. |
| Add a public synthetic benchmark suite | Evaluation | Private traces limit comparability. | Gives downstream researchers a common starting point. | Synthetic benchmarks may overfit to BEAGLE design. | Compare against held-out public programming traces where permitted. |
| Isolate breakdown effects | Human evaluation | Turing-test stimuli are transformed for temporal density. | Clarifies whether perceptual fidelity comes from behavior or presentation. | Requires new human or calibrated judge study. | Compare sparse, dense, and human-captured trace formats. |
| Expand beyond Python programming | Generalization | Learner behavior may differ across domains. | Tests whether SRL control transfers to other open-ended tasks. | Requires new task and knowledge-component design. | Run small synthetic pilots in writing, math, and science inquiry. |
| Add governance labels to generated traces | Product safety | Synthetic learner data can be misused as validation evidence. | Makes artifact limits visible to downstream tools. | Requires consistent metadata conventions. | Require state, source, and simulation-limit fields in trace output. |

## Potential Implementations

1. `Synthetic Tutor Stress Lab`
   - `User`: Education-AI researcher or tutoring-system engineer.
   - `Goal`: Stress-test hint strategies before running human-subject studies.
   - `Core mechanism`: Generate novice-like programming traces with explicit behavior states, mastery estimates, flaw-injection flags, and tutor-intervention points.
   - `Required inputs`: Synthetic programming tasks, knowledge-component map, BKT parameters, prompt templates, and intervention policies.
   - `Outputs`: Trace logs, error recurrence summaries, hint-effect comparisons, and review notes.
   - `Risk controls`: Synthetic data by default, no claims about human efficacy without validation, privacy labels, and human review.
   - `Evaluation`: Compare generated trace distributions against permitted public or institution-approved traces.

2. `Process Fidelity Auditor`
   - `User`: Agent evaluation researcher.
   - `Goal`: Score whether an agent follows an intended process, not only whether it reaches a correct answer.
   - `Core mechanism`: Map event logs into state transitions, compute divergence from reference behavior distributions, and flag suspiciously efficient or linear traces.
   - `Required inputs`: Agent event logs, target behavior schema, reference transition distribution, and scoring rubric.
   - `Outputs`: Process-fidelity scorecard, trace anomalies, and reviewer questions.
   - `Risk controls`: Use authorized logs only, avoid sensitive content retention, and separate process score from final task grade.
   - `Evaluation`: Run on synthetic traces with known perturbations and measure whether the auditor catches shortcut behavior.

3. `Knowledge-Gap Scenario Builder`
   - `User`: Curriculum designer or educational data scientist.
   - `Goal`: Create controlled scenarios where missing concepts lead to realistic errors.
   - `Core mechanism`: Define knowledge components, mastery levels, blocked concepts, and tutor-release conditions, then generate safe synthetic traces.
   - `Required inputs`: Task descriptions, concept map, mastery priors, allowed concepts, and teacher feedback templates.
   - `Outputs`: Scenario cards, expected misconceptions, synthetic code attempts, and intervention checkpoints.
   - `Risk controls`: Clearly mark simulations as synthetic, avoid profiling real students, and require educator review.
   - `Evaluation`: Expert review of whether simulated errors match plausible misconceptions.

## Three Ways to Exercise This Research

1. `Synthetic trace smoke test`: Objective: implement a toy state machine with construct/debug/reflect states and compare generated transition counts against a target distribution. Inputs: synthetic tasks and state labels. Method: simulate 30-step traces and compute transition counts. Output: trace-fidelity note. Success criterion: non-linear debugging loops appear without using real student data. Safety boundary: synthetic traces only.
2. `Knowledge-gap prompt test`: Objective: test whether blocking a concept changes generated solutions. Inputs: one toy programming task and a concept-block list. Method: run a safe local prompt or stub generator with and without the block. Output: comparison table of errors. Success criterion: blocked concept causes plausible workaround attempts. Safety boundary: no real student profiling.
3. `Tutor policy comparison`: Objective: compare reflective hints versus direct corrective hints in a synthetic simulator. Inputs: toy error states and two hint templates. Method: apply each policy across simulated traces and record recurrence changes. Output: policy note with caveats. Success criterion: difference is visible and labeled as simulation-only. Safety boundary: no human-learning claims without study approval.

## Example MVP Product

- `Product name`: LearnerTrace Sandbox
- `Target user`: Education-AI researchers and tutoring-system developers.
- `Problem`: Tutoring systems need realistic learner-process tests, but authentic longitudinal student data is expensive, sensitive, and hard to share.
- `Core workflow`: Define a task, map knowledge components, choose learner profile, generate synthetic traces, run tutor interventions, compute process-fidelity metrics, and export a public-safe review report.
- `Data requirements`: Synthetic or authorized programming tasks, concept maps, public prompt templates, BKT settings, behavior-state schema, tutor policies, and generated trace logs.
- `Architecture`: Local simulator core, state-transition sampler, knowledge-state tracker, flaw-injection module, prompt or stub generator, trace scorer, privacy/sanitization gate, and Markdown report generator.
- `Success metrics`: Trace divergence from target distribution, error recurrence rate, number of unsupported claims caught, educator plausibility rating, and absence of private data in exports.
- `Risk controls`: Synthetic defaults, no real-student identifiers, no high-stakes placement use, explicit simulation labels, educator review, and public-safe artifact checks.
- `Limitations`: Does not prove tutor effectiveness, does not replace classroom validation, and requires careful task-specific concept mapping.
- `MVP boundary`: Toy Python tasks and synthetic learner traces only.
- `Deployment model`: Local CLI or notebook for research review.
- `Evaluation plan`: Compare toy traces against expected state distributions and run educator review on plausibility.
- `Failure modes`: Over-realistic claims from synthetic data, poor concept maps, judge bias, prompt leakage of blocked concepts, and hidden formatting effects.
- `Maintenance plan`: Version prompt templates, concept maps, scoring rubrics, sanitization rules, and validation datasets.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| BEAGLE arXiv record | Primary paper | Source paper metadata and abstract. | https://arxiv.org/abs/2602.13280 |
| BEAGLE arXiv source package | Primary source package | Paper body, appendix, prompts, and source README used for review. | https://arxiv.org/e-print/2602.13280v2 |
| Agent Memory in Local AI Stack DEP-E | Related Black-Lake artifact | Persistent state and secure-agent governance related to BEAGLE's explicit state controls. | Delphoa/Black-Lake/.lake-data/DEP-E-20260709-Local AI Stack/local-ai-research.md |
| Tech Intel 0101 DEP-E | Related Black-Lake artifact | Early abort, evidence-state control, and trajectory governance adjacent to BEAGLE. | Delphoa/Black-Lake/.lake-data/DEP-E-20260710-Tech Intel 0101/tech-intel-0101-research.md |
| Tech Intel 1102 source DEP | Related Black-Lake-Data artifact | Reversible context management, real-device evaluation, and auditable agent workflows. | Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260702-Tech Intel 1102/daily_research_findings_2026-07-02_1102.md |
| Self-Regulated Learning literature | Background theory | BEAGLE grounds learner dynamics in SRL theory and related cognitive/metacognitive behavior work. | Cited in BEAGLE source package bibliography |
| Bayesian Knowledge Tracing | Methodological background | BEAGLE uses BKT for mastery tracking and concept availability. | Cited in BEAGLE source package bibliography |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2602.13280 | Title, authors, arXiv ID, publication/update dates, category, abstract, version, and primary public record. | 2026-07-10 | Primary arXiv metadata inspected. |
| R2 | https://arxiv.org/e-print/2602.13280v2 | Main paper source, appendix, prompt appendix, bibliography, source README, and figure inventory. | 2026-07-10 | Source package inspected; not collected or redistributed. |
| R3 | https://raw.githubusercontent.com/Delphoa/Black-Lake/main/README.md | Output repository DEP-E, README, attribution, log, and report rules. | 2026-07-10 | Live README fetched before writing. |
| R4 | https://github.com/Delphoa-Labs/Black-Lake-Data | Related source repository README and DEP context. | 2026-07-10 | Repository cloned for context; local clone path withheld. |
| R5 | Delphoa/Black-Lake/.lake-data/DEP-E-20260709-Local AI Stack/local-ai-research.md | Related entry on local AI, agent memory, and secure state governance. | 2026-07-10 | Repository-relative artifact inspected. |
| R6 | Delphoa/Black-Lake/.lake-data/DEP-E-20260710-Tech Intel 0101/tech-intel-0101-research.md | Related entry on controlled agent episodes and evidence-state RAG. | 2026-07-10 | Repository-relative artifact inspected. |
| R7 | Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260702-Tech Intel 1102/daily_research_findings_2026-07-02_1102.md | Related entry on trajectory/context management and agent evaluation realism. | 2026-07-10 | Repository-relative artifact inspected. |
| R8 | Repository and automation marker scans | Dedup/reselection validation for arXiv ID, normalized title, and slug. | 2026-07-10 | Public artifact records and automation memory scanned; local paths withheld. |

## Appendix

### Random Selection And Dedup Validation

- Candidate enumeration command pattern: `rg --files -g "*.pdf"` against the local arXiv source archive.
- Paper-unit rule: each PDF parent directory counted as one paper.
- Candidate count: 75,438.
- Random method: uniform `Get-Random` index over candidate paper units.
- Random index: 61,883.
- Accepted paper: `arXiv:2602.13280`.
- Reselections: 0.
- Duplicate matches in Black-Lake `.logs`, `.reports`, `.lake-data`: 0.
- Duplicate matches in automation memory: 0.
- Duplicate matches in Black-Lake-Data context: 0.
- Same-paper 24-hour markers: 0.

### Source Inventory

- Source files collected into this DEP: none.
- `.source/` folder included: no.
- Reason: the public arXiv source package and PDF were inspected but not redistributed; source URLs are preserved instead.

### Validation Checklist

- YAML front matter present: yes.
- YAML `title` and H1 identical and no more than 40 characters: yes.
- Required manuscript sections present: yes.
- Evidence ledger present: yes.
- Methodology includes random selection and dedup validation: yes.
- Three exercise paths: exactly 3.
- Example MVP fields complete: yes.
- Local absolute paths, usernames, machine names, local timezone labels, and exact local execution timestamps: withheld.
