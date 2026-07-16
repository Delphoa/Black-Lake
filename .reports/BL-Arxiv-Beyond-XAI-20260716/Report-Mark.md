# Report-Mark: Beyond XAI

Public run date: 2026-07-16

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Beyond Explainable AI (XAI): An Overdue Paradigm Shift and Post-XAI Research Directions* |
| Authors | Saleh Afroogh; Syed Ishtiaque Ahmed; Petra Ahrweiler; and 46 additional authors listed by the canonical arXiv record |
| Stable identifiers | arXiv:2602.24176v5; DOI:10.48550/arXiv.2602.24176 |
| Publication context | First submitted 2026-02-27; current revision 2026-05-25; Computers and Society (cs.CY) |
| Artifact type | Cross-disciplinary position paper and narrative literature synthesis |
| Source state | Verified complete local PDF and official full-paper HTML; metadata HTML and source package also retained locally |
| Distribution | Generated Markdown only; all original and extracted source files withheld locally |

## Concise Research Notes

- **Problem:** Post-hoc XAI is expected to make opaque models understandable and calibrate user trust, yet simplified explanations can be unfaithful while faithful accounts can be too complex for intended users. The paper argues that the field often conflates model behavior, world causation, user sense-making, and scientific explanation.
- **Scope:** The paper deliberately targets post-hoc explanations for complex black-box DNNs and LLMs under the DARPA-style objective of end-user trust. It excludes intrinsically interpretable models and does not deny the usefulness of diagnostic tools for developers.
- **Evidence synthesis:** Four symptom groups organize cited empirical work: the trust-explanation gap, stakeholder misalignment, explanation backfire/cognitive overload, and exclusion or disparity for vulnerable users. Examples include a cited 457-clinician study in which biased AI plus explanations reduced diagnostic accuracy by 9.1 percentage points.
- **Root diagnosis:** The paper develops a deep-superficial tension, explanatory-level confusion, correlation-versus-causation confusion, five challenged assumptions about trust and knowledge formation, and a formal proxy-model argument.
- **Formal claim:** If a proxy explanation is incomplete or unfaithful, another model may be needed to explain the relationship, creating regress; if it is complete and faithful, the original is effectively interpretable and the proxy becomes unnecessary. This is an author argument, not an established theorem about every explanation practice.
- **Alternative:** Four directions replace a single explanatory promise: Interactive AI for behavioral verification and expert certification; AI Epistemology for knowledge-validation standards; User-Sensible AI for community- and context-specific mediation; and Model-Centered Interpretability for honest analysis of model internals.
- **Agent relevance:** The paper explicitly argues that post-hoc explanation becomes weaker for non-deterministic agent systems. Runtime observability, tamper-resistant traces, tool-call evidence, policy enforcement, and controlled behavioral tests are presented as more useful than a narrative after the fact.
- **Limitations:** No original experiment, benchmark, code, dataset, preregistered search protocol, inclusion flow, study-quality assessment, or meta-analysis is reported. The 287-entry bibliography provides breadth but not systematic-review guarantees.
- **Internal consistency caution:** The paper describes “four symptoms and eight root causes,” yet its enumerated two paradoxes, two conceptual confusions, and five false assumptions total nine root-cause items. The claimed 13 total issues is consistent with four plus nine, not four plus eight.
- **Implementation relevance:** The most transferable pattern is a claim-evidence contract: separate model diagnostics from real-world claims, require behavioral tests and provenance, measure calibrated reliance rather than explanation preference alone, and preserve expert disagreement rather than hiding it behind certification.

## Evidence and Attribution

| ID | Evidence inspected | Supports | Assessment |
|---|---|---|---|
| E1 | Complete PDF, official full-paper HTML, and TeX/source package | Scope, definitions, symptom taxonomy, formal argument, proposed directions, limitations, conclusion | High confidence for faithful reporting; arguments and cited findings were not independently reproduced |
| E2 | Canonical arXiv metadata and DOI | Title, 49-author record, versions, dates, subject, persistent identifier | High |
| E3 | Source bibliography and figure inventory | 287 bibliography entries, seven figure assets, breadth of cited domains | High for inventory; no claim-quality audit was performed |
| E4 | Local integrity and processing records | Random selection, dedup, initial partial state, bounded repair, final structural completeness | High; local locations and files intentionally withheld |
| E5 | Three related DEP manuscripts and their cited source bases | Model-probe limits, runtime verification, high-stakes saliency boundary | Medium; synthesis context does not validate this paper |

Author claims are labeled as such in the manuscript. Numerical examples are reported from the selected paper's discussion of prior studies, not reproduced measurements. The post-XAI product and governance implications below are reviewer interpretations.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` — selected because VALUE uses probes and attention to inspect multimodal representations while explicitly preserving the distinction between decodable or correlated signals and causal model use. Source basis: arXiv:2005.07310 and DOI:10.1007/978-3-030-58539-6_34.
2. `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` — selected because persistent-state agents, online safety monitoring, recursive evidence replay, and latent-state review turn runtime evidence into the verification substrate that the post-XAI paper requests. Source basis includes arXiv:2607.02510, arXiv:2607.02514, and arXiv:2607.02509.
3. `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md` — selected because its clinical setting makes the distinction operational: attention and graph visualizations can help inspection, but they are not causal explanations, calibration evidence, or prospective safety certification. Source basis: arXiv:2307.11986 and DOI:10.1145/3580305.3599819.

## Synthesis Note

### Concept Bridge

The four artifacts form a ladder from model signal to warranted reliance. VLM Probing asks what information is recoverable inside a model, but warns that attention and probe accuracy do not establish causal use. Medical Diff VQA shows the same gap in a consequential application: a plausible attention map cannot substitute for calibration, subgroup analysis, external validation, or clinician review. Agent State Review moves from static outputs to dynamic systems, where decisions depend on persistent state, evidence replay, tools, and control flow. The selected paper supplies the umbrella distinction: model-centered analysis may remain useful, but claims about reliability require behavioral verification, provenance, challenge, and institutional accountability.

### Potential Implementations

1. **Claim-evidence release gate:** Require each consequential model claim to declare whether it concerns internal computation, observed behavior, real-world causation, or user experience; attach versioned evidence, limitations, and a reviewer decision before release.
2. **Interactive verification console:** Present domain experts with bounded counterexamples, reference swaps, ablations, uncertainty, and audit history; record approvals and dissent without converting review into a universal “explanation.”
3. **Agent execution certification harness:** Capture tool calls, state changes, evidence citations, policy decisions, and output checks in tamper-evident traces; evaluate deterministic invariants and stochastic risk thresholds across replayed scenarios.

### Deeper Relationship Observations

1. Decodability, saliency, and narrative fluency are all evidence about an interface to a model, not automatically evidence that the highlighted mechanism caused the decision or that the decision is correct in the world.
2. Moving from explanation to expert verification changes rather than removes the trust problem: reliability now depends on reviewer competence, panel diversity, incentive design, contestability, and trace quality.
3. Agentic systems amplify the paper's argument because the relevant object is an execution trajectory across state and tools; a static explanation of the final answer omits the very events that must be audited.

### Conceptual Similarities

1. Each entry separates observable output quality from hidden or intermediate representation claims.
2. Each entry needs interventions—mismatched captions, reference swaps, relation removal, evidence replay, or state perturbation—to test whether the proposed evidence actually controls behavior.
3. Each entry treats uncertainty and missing evidence as first-class review outputs rather than smoothing them into a confident explanation.

### MVP Implementations with Code Mock-Ups

1. **Claim-type validator:** reject a release card when a high-impact claim lacks typed evidence or confuses model and world claims.

```python
ALLOWED = {"model_internal", "behavioral", "world_causal", "user_study"}

def validate_claim(claim: dict) -> dict:
    errors = []
    if claim.get("type") not in ALLOWED:
        errors.append("untyped_claim")
    if not claim.get("evidence_ids"):
        errors.append("missing_evidence")
    if claim.get("type") == "world_causal" and not claim.get("intervention_basis"):
        errors.append("causal_claim_without_intervention_basis")
    return {"accepted": not errors, "errors": errors}
```

Use this as a documentation gate, not as an automated truth oracle; human reviewers still assess evidence quality.

2. **Bounded challenge schedule:** predeclare a compact intervention suite for model or agent review.

```python
def challenge_plan():
    return [
        {"case": "baseline", "change": None},
        {"case": "evidence_removed", "change": "remove_primary_evidence"},
        {"case": "counterexample", "change": "inject_verified_counterexample"},
        {"case": "state_replay", "change": "replay_from_checkpoint"},
        {"case": "tool_denied", "change": "deny_optional_tool"},
    ]
```

Run only on synthetic, public, or authorized test cases with fixed policies and explicit stop conditions.

3. **Reliance card:** preserve performance, uncertainty, disagreement, and trace coverage separately so a polished explanation cannot hide weak evidence.

```python
def reliance_card(total, correct, abstained, traced, reviewer_votes):
    return {
        "accuracy": correct / max(1, total - abstained),
        "abstention_rate": abstained / max(1, total),
        "trace_coverage": traced / max(1, total),
        "reviewer_agreement": max(reviewer_votes.values()) / max(1, sum(reviewer_votes.values())),
    }
```

The card is descriptive. Production use needs confidence intervals, subgroup metrics, severity weighting, and governance review.

### Developer Challenges

1. Capturing complete, privacy-preserving evidence across model calls, tools, state stores, human actions, and retries without producing unauditable trace volume.
2. Designing interventions that test causal dependence while remaining deterministic enough for regression, representative enough for risk review, and safe for governed environments.
3. Preventing review interfaces and certification labels from becoming new persuasive explanations that encourage overreliance despite weak or stale evidence.

### Author Challenges

1. Convert the narrative evidence review into a reproducible protocol with search sources, dates, queries, inclusion/exclusion rules, quality assessment, and claim-level citation checks.
2. Narrow or defend the proxy-model paradox against explanation practices that are explicitly partial, task-bounded, plural, or contrastive and do not promise complete model duplication.
3. Empirically compare the four proposed directions against representative XAI baselines using calibrated reliance, error detection, coverage, accessibility, expert workload, disagreement, and institutional cost.

## Validation Notes

- Random selection used uniform rejection sampling over 75,776 parent-directory units after `rg --files -g "*.pdf"` enumeration; the first raw draw at zero-based index 28,956 passed identifier and dedup gates, so reselections were zero.
- The primary-record dedup set contained 232 used arXiv IDs; 93 archive units matched those IDs and 185 units lacked a derivable identifier. No selected ID, DOI, normalized-title, slug, or preceding-24-hour marker was found.
- Source state was initially `partial` because full-paper HTML was absent. The valid PDF was preserved; official HTML, metadata HTML, and source archive were repaired locally with bounded direct-HTTPS attempts.
- Final source verification passed: PDF 1,976,924 bytes with `%PDF-` and trailing `%%EOF`; official full-paper HTML 356,861 bytes with 140,055 body characters, a document marker, 71 heading markers, and seven structure terms; zero partial files.
- The manuscript title and H1 are identical and under 40 characters. All required manuscript sections are present; `## Three Ways to Exercise This Research` has exactly three entries.
- This Report-Mark contains one concept bridge and exactly three entries in each required synthesis group. The three code blocks use only synthetic structures and standard Python syntax.
- No source file was copied into the repository. The public package contains generated Markdown only and no `.source/` directory.
- No code, dataset, experiment, or citation-level systematic-review protocol was executed. Empirical examples remain source-reported and the formal paradox remains an author argument.

## Attribution Block

- Source URL: https://arxiv.org/abs/2602.24176
  - Applies to: `Report-Mark.md`
  - Notes: Canonical metadata, abstract, version history, subject, author record, DOI, and public source locators.
- Source URL: https://arxiv.org/pdf/2602.24176
  - Applies to: `Report-Mark.md`
  - Notes: Public equivalent of the complete PDF inspected locally; file not redistributed.
- Source URL: https://arxiv.org/html/2602.24176
  - Applies to: `Report-Mark.md`
  - Notes: Official full-paper rendering used to inspect definitions, cited evidence, formal argument, proposed directions, and limitations; file not redistributed.
- Source URL: https://arxiv.org/e-print/2602.24176
  - Applies to: `Report-Mark.md`
  - Notes: Local source evidence used to verify section structure, equations, bibliography count, figures, and conclusion; file not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2602.24176
  - Applies to: `Report-Mark.md`
  - Notes: arXiv-issued persistent identifier.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `Report-Mark.md`
  - Notes: Live repository authority for logs, reports, DEP contents, source withholding, attribution, and commit rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `Report-Mark.md`
  - Notes: Live DEP-E filing and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `Report-Mark.md`
  - Notes: Live companion-repository authority used for dedup context.
- Repository file: `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md
  - Applies to: `Report-Mark.md`
  - Notes: Related model-probing and evidence-boundary synthesis; source basis arXiv:2005.07310 and DOI:10.1007/978-3-030-58539-6_34.
- Repository file: `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260708-Agent%20State%20Review/agent_state_review.md
  - Applies to: `Report-Mark.md`
  - Notes: Related runtime-state, evidence-replay, and safety-monitoring synthesis; source basis includes arXiv:2607.02510, arXiv:2607.02514, and arXiv:2607.02509.
- Repository file: `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Medical%20Diff%20VQA/medical_diff_vqa_manuscript.md
  - Applies to: `Report-Mark.md`
  - Notes: Related high-stakes multimodal evaluation and saliency-boundary synthesis; source basis arXiv:2307.11986 and DOI:10.1145/3580305.3599819.
