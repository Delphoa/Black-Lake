# Report-Mark: Business What-If Analysis

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260719-7D93E819`
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P06`
- Review date: 2026-07-19
- Review type: source-first HCI and decision-support synthesis

## Source Metadata

| Field | Value |
|---|---|
| Paper | *What-if Analysis for Business Professionals: Current Practices and Future Opportunities* |
| Authors | Sneha Gathani; Zhicheng Liu; Peter J. Haas; Çağatay Demiralp |
| Stable identifier | arXiv:2212.13643v4 |
| Submission history | Submitted 2022-12-27; v4 dated 2025-03-01 |
| DOI | https://doi.org/10.48550/arXiv.2212.13643 |
| Primary record | https://arxiv.org/abs/2212.13643 |
| Full-paper HTML | https://arxiv.org/html/2212.13643 |
| PDF | https://arxiv.org/pdf/2212.13643 |
| Source state | Verified complete after one bounded repair; source files withheld locally. |
| Deployment job ID | `BLAD-2200-20260719-7D93E819` |
| Deployment item ID | `BLAD-2200-20260719-7D93E819-P06` |

## Concise Research Notes

### Problem

Business professionals use data to make frequent decisions but often lack programming or formal data-science training. Existing what-if analysis research and tools emphasize technical analysts, leaving domain experts to construct fragile spreadsheet workflows for sensitivity, driver importance, segmentation, comparison, and goal seeking.

### Method

The paper reports a two-part study with the same 22 professionals from marketing, sales, product, and operations. Study I used interviews to reconstruct goals, tools, practices, and constraints. Study II used a visual-analytics prototype as a probe for ten tasks spanning driver importance, sensitivity, summary, goal-seeking, and constrained analysis. Sessions were transcribed and iteratively coded, primarily by the first author with co-author consultation.

### Evidence

Twenty of 22 participants reported sensitivity-analysis needs; 17 of 22 wanted driver-importance analysis. Most work centered on spreadsheets; only five used dashboards, and eight had access to technical data teams. All 22 completed the ten prototype tasks within the allotted session. Participants ranked sensitivity analysis highest, while six needed the most guidance for goal seeking. Findings emphasize faster decisions and greater confidence alongside needs for data preparation, risk communication, domain constraints, scenario provenance, and collaboration.

### Limits

The sample has few participants per department, Study I relies on self-report, Study II uses one marketing-mix use case and one prototype, interaction design may confound technique reactions, and the study does not compare against state-of-the-art tools. Qualitative findings reveal requirements and mechanisms, not population prevalence or causal productivity gains.

## Evidence and Attribution

| Claim | Source basis | Reviewer qualification |
|---|---|---|
| Participants perform advanced analysis through manual spreadsheet methods. | Sections 5.2.1-5.2.3. | Qualitative and self-reported; valuable for requirement discovery. |
| The study included 22 professionals across four functions. | Section 3.1. | Purposive sample, not statistically representative. |
| All participants completed ten prototype tasks. | Section 7.1. | Shows task accessibility in a guided study, not long-term adoption. |
| Risk and model performance need actionable interpretation. | Sections 7.3 and 8.1. | Design recommendation grounded in participant feedback. |
| Scenario provenance should be a product requirement. | Section 8.3 plus reviewer synthesis. | Requires implementation and longitudinal validation. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Beyond XAI/beyond_xai_manuscript.md` - warns that fluent explanations do not establish reliability and advocates evidence chains.
2. `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md` - shows how uncertainty envelopes and review capacity can travel with a score.
3. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` - clarifies coverage assumptions and the danger of confidence claims under shift.

## Synthesis Note

### Concept Bridge

The paper's prototype is not merely a dashboard; it is a decision-state editor. A user defines goals, drivers, constraints, models, and alternative paths, then needs to understand why an output changed and what risk accompanies it. Beyond XAI supplies the warning that an intuitive explanation is not verification. Judge Conformal and PAC Confidence supply a complementary calibration layer: predictions should travel with uncertainty, support size, assumptions, and shift status. Together they motivate a business what-if workbench that records every scenario as an immutable, reviewable decision artifact rather than an ephemeral spreadsheet state.

### Potential Implementations

1. Build a scenario ledger that versions inputs, constraints, model identity, outputs, uncertainty, annotations, and approval status.
2. Add risk-aware goal seeking that returns feasible ranges and warnings instead of one apparently optimal point.
3. Create a collaboration view that compares scenarios, preserves domain rationale, and exports an executive-readable evidence packet.

### Deeper Relationship Observations

1. What-if interaction is a form of model steering, so confidence and failure evidence should update as inputs leave well-supported regions.
2. Domain constraints improve practical plausibility but can also hide model misspecification unless assumptions remain visible.
3. Scenario proliferation is an information-management problem; provenance and comparison become as important as numerical optimization.

### Conceptual Similarities

1. Business what-if tools and post-XAI systems both mediate trust through an interface and therefore risk confusing usability with validity.
2. Goal-seeking outputs and LLM judge scores both benefit from uncertainty envelopes rather than unsupported point estimates.
3. Scenario confidence and PAC-style guarantees both depend on explicit assumptions and distribution-shift monitoring.

### MVP Implementations with Code Mock-Ups

1. Immutable scenario record:

```python
def scenario(model_id, drivers, constraints, result):
    return {"model": model_id, "drivers": dict(drivers),
            "constraints": list(constraints), "result": result,
            "status": "draft"}
```

2. Feasibility gate:

```python
def feasible(candidate, constraints):
    failures = [c["name"] for c in constraints
                if not c["check"](candidate)]
    return {"ok": not failures, "failures": failures}
```

3. Risk-aware comparison:

```python
def compare(a, b):
    return {"delta": b["value"] - a["value"],
            "overlap": not (a["high"] < b["low"] or b["high"] < a["low"]),
            "needs_review": a["shifted"] or b["shifted"]}
```

### Developer Challenges

1. Models, data snapshots, and business constraints must be versioned so a scenario can be reproduced later.
2. Optimization must avoid infeasible or misleading recommendations when variables are correlated or causality is unknown.
3. Interfaces must expose uncertainty and provenance without recreating the complexity that drove users back to spreadsheets.

### Author Challenges

1. Validate requirements across more industries, roles, cultures, and decision frequencies.
2. Separate the benefit of each analysis technique from the specific prototype interaction design.
3. Measure longitudinal decision quality, error cost, collaboration, and adoption against existing tools.

## Validation Notes

- Random selection: uniform index 41,046 of 75,776 units from 75,778 PDFs; first draw.
- Dedup: repository, memory, companion-repository, title, DOI, slug, 24-hour, and current-job checks found no collision; exclusions 0; reselections 0.
- Integrity: one bounded partial-to-complete repair; PDF and official HTML passed; cache `cached`; no partials.
- Structure: required sections present; exactly three items per mandated synthesis category; three syntax-checked Python mock-ups.
- Public-safety: private paths, exact local timestamps, timezone labels, and user/machine context withheld.
- Source locality: zero source-document uploads; no `.source/` directory.

## Attribution Block

- https://arxiv.org/abs/2212.13643 - canonical metadata, authorship, abstract, identifier, and revision history.
- https://arxiv.org/html/2212.13643 - primary full-paper evidence for study design, findings, discussion, and limitations.
- https://arxiv.org/pdf/2212.13643 - validated complete paper rendering; withheld locally.
- https://doi.org/10.48550/arXiv.2212.13643 - persistent identifier.
- `.lake-data/DEP-E/DEP-E-20260716-Beyond XAI/beyond_xai_manuscript.md` - related trust and verification context.
- `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md` - related uncertainty-envelope context.
- `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` - related coverage and shift context.
- PDF, HTML, metadata, extracted text, and cache records were inspected locally and withheld from Git and Slack.
