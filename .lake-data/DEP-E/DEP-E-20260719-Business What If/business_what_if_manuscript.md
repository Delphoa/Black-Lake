---
title: "Business What-If Decision Support"
generated_at: "2026-07-19 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A source-grounded review of what-if analysis practices and decision-support requirements for business professionals."
source_status: "verified complete local PDF, official full-paper HTML, and metadata HTML inspected; all sources withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-19"
temporal_cutoff: "Sources and repository context inspected through the batch invocation."
primary_url: "https://arxiv.org/abs/2212.13643"
stable_identifier: "arXiv:2212.13643v4; DOI:10.48550/arXiv.2212.13643"
deployment_job_id: "BLAD-2200-20260719-7D93E819"
deployment_item_id: "BLAD-2200-20260719-7D93E819-P06"
confidence_summary: "High for identity, study design, participant counts, and reported themes; medium for transfer across business contexts; low for causal productivity effects."
safety_scope: "offline decision support, uncertainty communication, scenario provenance, human approval, and non-executing prototypes"
distribution_notes: "No PDF, HTML, metadata, extracted text, cache, dataset, local path, or source document is redistributed."
---

# Business What-If Decision Support

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Canonical arXiv record | Metadata | HTML | arXiv:2212.13643v4 | https://arxiv.org/abs/2212.13643 | Metadata only. | 2026-07-19 | Inspected. |
| S2 | Official full-paper rendering | Primary paper | HTML | arXiv:2212.13643v4 | https://arxiv.org/html/2212.13643 | Verified local copy withheld. | 2026-07-19 | Inspected in full. |
| S3 | Paper PDF | Primary paper | PDF | arXiv:2212.13643v4 | https://arxiv.org/pdf/2212.13643 | Verified local copy withheld. | 2026-07-19 | Inspected through extraction. |
| S4 | arXiv-issued DOI | Identity | DOI | 10.48550/arXiv.2212.13643 | https://doi.org/10.48550/arXiv.2212.13643 | Persistent locator. | 2026-07-19 | Resolved. |
| S5 | Beyond XAI DEP | Related | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-Beyond XAI/beyond_xai_manuscript.md` | Related synthesis only. | 2026-07-19 | Inspected. |
| S6 | Judge Conformal DEP | Related | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md` | Related synthesis only. | 2026-07-19 | Inspected. |
| S7 | PAC Confidence DEP | Related | Markdown | DEP-E-20260713 | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Related synthesis only. | 2026-07-19 | Inspected. |
| S8 | Selection, repair, and cache | Process evidence | Private records | `BLAD-2200-20260719-7D93E819-P06` | Local paths withheld | Integrity, dedup, and locality only. | 2026-07-19 | Verified. |

Authors: Sneha Gathani, Zhicheng Liu, Peter J. Haas, and Çağatay Demiralp. Submitted 2022-12-27; v4 dated 2025-03-01. Deployment job `BLAD-2200-20260719-7D93E819`; item `BLAD-2200-20260719-7D93E819-P06`.

## Evidence Ledger

| Evidence ID | Source | Claim or observation | Type | Confidence | Limits |
|---|---|---|---|---|---|
| E1 | S2, section 3.1 | Twenty-two professionals across marketing, sales, product, and operations participated. | Study design. | High | Small purposive sample. |
| E2 | S2, section 5.2.1 | 20/22 reported sensitivity-analysis needs; 17/22 wanted driver-importance analysis. | Qualitative count. | High transcription; medium prevalence. | Not population-estimating. |
| E3 | S2, section 5.2.2 | Spreadsheets dominated; five used dashboards and eight had technical-team access. | Reported workflow evidence. | Medium-high | Self-report. |
| E4 | S2, section 7.1 | All participants completed ten prototype tasks; sensitivity ranked highest and goal seeking needed most guidance for six. | Task-study observation. | High transcription; medium transfer. | Guided single-use-case session. |
| E5 | S2, sections 8.1-8.3 | Future systems need risk interpretation, collaboration, and scenario management. | Author design synthesis. | Medium-high | Requires product validation. |
| E6 | S2, section 8.4 | Sample, self-report, prototype, single use case, and lack of tool comparison limit claims. | Author-stated limitation. | High | Bounds generalization. |
| E7 | S5-S7 | Explanation quality and confidence evidence should accompany scenarios. | Reviewer synthesis. | Medium | Cross-paper design bridge. |

## Executive Summary

Business professionals already perform sophisticated what-if reasoning, but often through manually edited spreadsheets, copied tables, and trial-and-error formulas. A two-part study with 22 participants documents these practices and uses a visual-analytics prototype to probe sensitivity, driver importance, summary, goal seeking, and constrained analysis. Participants completed the tasks and described speed and confidence benefits, while also exposing requirements for data preparation, risk assessment, domain constraints, interpretation, collaboration, and scenario reuse. The evidence supports a design agenda, not a universal productivity claim.

## Detailed Summary

Study I reconstructed how participants frame questions, formulate hypotheses, translate them into simple models, revise those models with data, and compare scenarios. Sensitivity analysis was the most common desired technique. Driver importance, segmentation, correlation, comparison, and goal seeking also appeared, but were often approximated through spreadsheet manipulation.

Study II gave the same participants a prototype built around a marketing-mix model. Ten tasks exercised driver ranking, perturbation, summaries, target seeking, and constraints. The probe exposed model performance and allowed business boundaries to rule out implausible optima. Participants valued interactive exploration, yet requested clearer interpretation, reusable states, cross-technique handoff, risk signals, and domain-aware constraints.

The discussion shifts from individual calculations to decision management. As scenario count grows, professionals need formal goals, versioned inputs, provenance, comparison, communication, and a way to combine quantitative output with qualitative domain context. Natural-language interfaces may improve accessibility, but the paper does not present or evaluate an LLM-based implementation.

## Key Claims and Evidence

1. **Advanced work with rudimentary tools:** Sections 5.2.1-5.2.3 document sophisticated goals performed through manual spreadsheet processes.
2. **Prototype accessibility:** Section 7.1 reports completion of all ten tasks by all participants; guided-session evidence does not establish independent adoption.
3. **Confidence is socio-technical:** Section 8.1 argues that model scores should be paired with risk and next-step guidance rather than displayed in isolation.
4. **Collaboration matters:** Section 8.2 frames interactive scenarios as shared decision objects during meetings.
5. **Provenance is central:** Section 8.3 argues that rapidly multiplying decision paths require tracking, comparison, and reuse.

## Methodology

The paper recruited professionals who use organizational data, decide at least weekly, and lack formal programming/data-science training. Both studies totaled 120-140 minutes across separate sessions. Interviews and task sessions were recorded and transcribed. The first author performed iterative coding and consulted co-authors to resolve ambiguity. The review inspected the full paper, tables, limitations, and exactly three related DEP entries; source claims and reviewer synthesis are explicitly separated.

Random selection used uniform index 41,046 from 75,776 unique PDF-parent units derived from 75,778 PDFs. ID, DOI, normalized-title, slug, prior cron, 24-hour, companion-repository, and current-job checks found no collision. One repair pass preserved the valid PDF and added verified official HTML; extraction cache status is `cached`.

## Scope, Constraints, and Assumptions

- Findings concern 22 participants and one prototype context, not all business professionals.
- Counts summarize the study sample and are not prevalence estimates.
- Self-reported Study I workflows may differ from observed practice.
- Prototype interaction design and WIA technique are partly confounded.
- The marketing-mix task may not transfer to other domains.
- Related DEP connections are reviewer synthesis.

## Observations

- Domain experts need to inspect and constrain models, not merely consume predictions.
- Spreadsheet familiarity reflects accessibility and institutional fit, not analytical sufficiency.
- Goal seeking creates plausible-looking points that may violate real-world constraints.
- Saving scenario state is essential for comparison, collaboration, and audit.
- Confidence should connect statistical support to business risk and next actions.

## Considerations

- Version data, model, formula, constraints, and annotations together.
- Display uncertainty and out-of-support warnings near every prediction.
- Make irreversible business actions require explicit human approval.
- Provide plain-language explanations without treating them as validity evidence.
- Evaluate longitudinally against current tools and real decisions.

## Strengths

- Targets an underserved practitioner group.
- Combines interviews with hands-on prototype use.
- Preserves participant counts and concrete workflow examples.
- Identifies data, model, risk, collaboration, and provenance requirements.
- States important threats to validity.

## Weaknesses

- Small per-department sample.
- Self-reported first study.
- One use case and one prototype.
- No state-of-the-art tool comparison.
- No longitudinal decision-quality or error-cost measurement.

## Potential Improvements

- Run multi-industry longitudinal field studies.
- Factorially separate interaction design from analytic technique.
- Compare against spreadsheets and commercial BI tools.
- Add calibrated intervals, shift warnings, and risk labels.
- Measure reproducibility, collaboration, decision errors, and time.
- Include qualitative evidence and domain rationale in scenario records.

## Potential Implementations

Start with an offline scenario ledger, risk-aware goal-seeking service, and comparison UI. It should never execute a business action. Each result should preserve model/data identity, constraints, uncertainty, shift status, domain rationale, and approval state. Promotion requires security review, statistical validation, and longitudinal usability evidence.

## Three Ways to Exercise This Research

1. **Workflow replay:** Reproduce a real spreadsheet scenario inside a versioned ledger and compare time, errors, and recoverability.
2. **Constraint stress test:** Generate infeasible and out-of-support goals; verify warnings, abstention, and audit logs.
3. **Collaboration study:** Compare static exports with live scenario comparison during a team decision and measure comprehension and disagreement resolution.

## Example MVP Product

**Scenario Ledger** is a non-executing decision workbench. It imports tabular fixtures and a frozen predictive model, lets a user define drivers and constraints, records every variant immutably, renders intervals and risk notes, and exports a review packet. The MVP excludes autonomous action, hidden model updates, and source-data redistribution.

## Related Research and Reading

1. **Beyond XAI:** interface explanations must not substitute for behavioral tests, provenance, and expert challenge.
2. **Judge Conformal:** interval width and empirical coverage can make score uncertainty operational.
3. **PAC Confidence:** guarantees must travel with assumptions and shift status.

## Source References

1. Sneha Gathani et al., *What-if Analysis for Business Professionals: Current Practices and Future Opportunities*, https://arxiv.org/abs/2212.13643
2. Official full-paper HTML, https://arxiv.org/html/2212.13643
3. Official PDF, https://arxiv.org/pdf/2212.13643
4. Persistent DOI, https://doi.org/10.48550/arXiv.2212.13643
5. `.lake-data/DEP-E/DEP-E-20260716-Beyond XAI/beyond_xai_manuscript.md`
6. `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md`
7. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`

## Appendix

- YAML title and H1 are identical and within 40 characters.
- Required manuscript sections are present.
- Random/dedup and integrity outcomes are recorded.
- Exactly three related DEP entries are used.
- Source files, extracted text, caches, local paths, exact timestamps, and timezone labels are withheld.
