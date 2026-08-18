---
title: "arXiv 2602.09413 - DEP-E"
generated_at: "2026-08-19"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of LARV: Data-Free Layer-wise Adaptive Rescaling Veneer for Model Merging."
source_status: "local files only; source files withheld from public output"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-19"
temporal_cutoff: "2026-08-19"
primary_url: "https://arxiv.org/abs/2602.09413"
stable_identifier: "arXiv:2602.09413"
confidence_summary: "Medium: full-paper PDF and HTML passed the local integrity gate; independent reproduction was not performed."
safety_scope: "Research review and bounded implementation planning"
distribution_notes: "Original source files remain local and are not redistributed in this DEP."
---

# arXiv 2602.09413 - DEP-E

## Source Metadata

| Field | Value |
|---|---|
| Paper title | LARV: Data-Free Layer-wise Adaptive Rescaling Veneer for Model Merging |
| Authors | Not available from inspected sources |
| Platform | arXiv |
| arXiv ID | 2602.09413 |
| Revision/publication date | Not available from inspected sources |
| Primary URLs | https://arxiv.org/abs/2602.09413; https://arxiv.org/html/2602.09413; https://arxiv.org/pdf/2602.09413 |
| Local source status | Verified full PDF and full-paper HTML inspected locally; source files withheld from public output. |
| Access date | 2026-08-19 |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | https://arxiv.org/html/2602.09413 | Primary paper HTML | Full-paper title, abstract, headings, method/evidence text, and limitations cues | Research object, method, evidence, and reviewer notes | High | Text extraction may omit visual layout and fine-grained table context. |
| E2 | https://arxiv.org/pdf/2602.09413 | Primary paper PDF | PDF integrity gate and source-presence cross-check | Complete-source status | High | No independent reproduction or figure-by-figure audit in this batch pass. |
| E3 | https://arxiv.org/abs/2602.09413 | Canonical metadata record | arXiv identifier and public locator | Stable identity and provenance | High | Abstract page is metadata only and was not treated as the full paper. |

## Executive Summary

The reviewed paper, *LARV: Data-Free Layer-wise Adaptive Rescaling Veneer for Model Merging*, addresses a research problem described in its full-paper HTML as follows: Abstract Model merging aims to combine multiple fine-tuned models into a single multi-task model without access to training data. Existing task-vector merging methods such as TIES, TSV-M, and Iso-C/CTS differ in their aggregation rules but treat all layers nearly uniformly. This assumption overlooks the strong layer-wise heterogeneity in large vision transformers, where shallow layers are sensitive to interference while deeper layers encode stable task-specific features. We introduce LARV, a training-free, data-free, merger-agnostic L ayer-wise A daptive R escaling V eneer that plugs into any task-vector merger and assigns a per-layer scale to each task vector before aggregation, and show it consistently boosts diverse merging rules. LARV adaptively suppresses shallow-layer interference and amplifies deeper-layer alignment using a simple deterministic schedule, requiring no retraining or modification to existing mergers. To our knowledge, this is the first work to perform layer-aware scaling for task-vector merging. LARV computes simple data-free layer proxies and turns them into scales through a lightweight rule; we study several instantiations within one framework (e.g., tiered two/three-level scaling with fixed values, or continuous mappings) and show that tiered choices offer the best robustness, while continuous mappings remain an ablation. LARV is orthogonal to the base merger and adds negligible cost. On FusionBench with Vision Transformers, LARV consistently improves all task-vector baselines across 8/14/20-task settings; for example, Iso-C + LARV reaches 85.9% on ViT-B/32, 89.2% on ViT-B/16, and 92.6% on ViT-L/14. Layer-wise analysis and corruption tests further indicate that LARV suppresses shallow-layer interference while modestly amplifying deeper, task-stable features, turning model merging into a robust, layer-aware procedure rather than a uniform one. The source presents the paper's contribution through the following visible section structure: LARV: Data-Free Layer-wise Adaptive Rescaling Veneer for Model Merging, Abstract, 1 Introduction, 2 Related Work, Global and training-free merging., Structured and conflict-aware training-free merging., Adaptive or data-involving merging., Layer-wise representation studies and our position., 3 Method, 3.1 Preliminaries and Problem Setup, Why a single global scale is insufficient., 3.2 LARV: Layer-wise Rescaling Veneer over Any Merger. Reviewer interpretation: the work is most useful as a source-grounded design or evaluation reference, while the exact strength of its claims depends on the experiments, datasets, baselines, and boundary conditions reported in the paper. Full-paper source integrity passed; independent reproduction was not performed.

## Detailed Summary

### Problem and contribution

The paper frames its problem and motivation in the primary source. The extracted abstract is: Abstract Model merging aims to combine multiple fine-tuned models into a single multi-task model without access to training data. Existing task-vector merging methods such as TIES, TSV-M, and Iso-C/CTS differ in their aggregation rules but treat all layers nearly uniformly. This assumption overlooks the strong layer-wise heterogeneity in large vision transformers, where shallow layers are sensitive to interference while deeper layers encode stable task-specific features. We introduce LARV, a training-free, data-free, merger-agnostic L ayer-wise A daptive R escaling V eneer that plugs into any task-vector merger and assigns a per-layer scale to each task vector before aggregation, and show it consistently boosts diverse merging rules. LARV adaptively suppresses shallow-layer interference and amplifies deeper-layer alignment using a simple deterministic schedule, requiring no retraining or modification to existing mergers. To our knowledge, this is the first work to perform layer-aware scaling for task-vector merging. LARV computes simple data-free layer proxies and turns them into scales through a lightweight rule; we study several instantiations within one framework (e.g., tiered two/three-level scaling with fixed values, or continuous mappings) and show that tiered choices offer the best robustness, while continuous mappings remain an ablation. LARV is orthogonal to the base merger and adds negligible cost. On FusionBench with Vision Transformers, LARV consistently improves all task-vector baselines across 8/14/20-task settings; for example, Iso-C + LARV reaches 85.9% on ViT-B/32, 89.2% on ViT-B/16, and 92.6% on ViT-L/14. Layer-wise analysis and corruption tests further indicate that LARV suppresses shallow-layer interference while modestly amplifying deeper, task-stable features, turning model merging into a robust, layer-aware procedure rather than a uniform one.

### Method and mechanism

The full-paper text contains the following method-related evidence: LARV: Data-Free Layer-wise Adaptive Rescaling Veneer for Model Merging 1 Introduction 2 Related Work Global and training-free merging. Structured and conflict-aware training-free merging. The available heading structure is retained as a navigation aid rather than treated as proof of every technical claim.

### Evidence and results

Evidence-related text includes: 4 Results and Analysis 4.1 Experimental Setup 4.2 Main Results Across Backbones (8 tasks) Key Observations. C Experimental Setup and Protocol C.1 FusionBench Configuration and Evaluation Protocol C.2 Hyperparameters and Implementation Details D Ablation on Scaling Strategy: Beyond Simple Depth Priors D.1 Comprehensive Comparison to Depth-Only Heuristics Depth-only heuristics. Exact metrics and comparisons should be checked against the paper's tables and figures before making deployment decisions.

### Limitations and conclusion

Limitation-related text includes: This paradigm is both meaningful for revealing surprising linear structure in parameter space and useful for enabling capability sharing with no data, rapid deployment under data-access constraints, and mix-and-match assembly across tasks and architectures [ 35 , 24 , 16 , 1 , 7 ] . Where the source did not expose a clear limitation in the extracted text, this review records the gap rather than inferring that no limitation exists.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The paper investigates the problem stated in its title and abstract. | Author/source claim | E1 | Directly supported by the primary paper HTML. | High |
| C2 | The method is organized around the mechanisms and sections exposed by the full paper. | Reviewer interpretation | E1 | Useful for orientation; not a substitute for reproducing the method. | Medium |
| C3 | The work may inform an implementation or evaluation workflow. | Derived inference | E1, E2 | Plausible transfer value, but production readiness is not established. | Medium |

## Methodology

- `Research objective`: Preserve a concise, source-grounded review of one eligible arXiv archive paper and translate it into bounded implementation context.
- `Sources inspected`: The local verified full-paper PDF and full-paper HTML for arXiv:2602.09413; canonical arXiv metadata URL; three existing Black Lake DEP entries for related context.
- `Discovery strategy`: Enumerated PDF candidates with `rg --files -g "*.pdf"`; treated PDF parent directories as paper units; validated PDF and full-paper HTML; selected a uniform sample with PowerShell `Get-Random -Count 200` from the unseen valid-ID pool.
- `Inclusion criteria`: Full PDF at least 10 KB with `%PDF-` header and trailing `%%EOF`; full HTML at least 5 KB with at least 2,000 body characters, an article/main/LaTeXML marker, two heading markers, and two paper-structure terms.
- `Exclusion criteria`: Previously used IDs/titles/slugs, duplicate archive units, abstract-only or invalid source units, missing identifiers, and source units failing the integrity gate.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, and DEP-ready provenance review.
- `Evidence handling`: Primary-paper observations are separated from reviewer interpretation and derived implementation ideas; related DEP entries are context only.
- `Uncertainty handling`: Missing metrics, unavailable code/data, omitted visual detail, and lack of independent reproduction are stated explicitly.
- `Batch selection`: 75967 PDF candidates; 894 integrity-valid source units; 865 valid identified IDs; 2084 IDs found in repository/memory dedup scans; 396 duplicate exclusions; 0 reselections; 469 unseen eligible IDs; this item is sample position 137 of 200.

## Scope, Constraints, and Assumptions

- `Scope`: Primary-paper problem, method, evidence cues, limitations, implementation relevance, and three related repository entries.
- `Temporal boundary`: Public deposition date 2026-08-19; source version is the locally archived arXiv version identified as 2602.09413.
- `Evidence limits`: No independent reproduction, code execution, benchmark rerun, or complete visual/table audit was performed in this batch pass.
- `Assumptions`: The verified local full-paper HTML and PDF represent the same arXiv identifier; extracted text is sufficient for a concise review but not for exact metric transcription.
- `Constraints`: Source files are private local evidence and are withheld from the public repository; public artifacts contain URLs and derived notes only.
- `Out of scope`: Redistribution of source files, claims of peer review or deployment readiness, and unsupported numerical results.
- `Intended use`: Research triage, follow-on review, implementation ideation, and durable DEP provenance.

## Observations

- `Observed pattern`: The source's full-paper structure provides more evidence than an abstract-only record and supports a bounded review.
- `Technical implication`: A future implementation should preserve the paper's stated evaluation conditions rather than treating the headline contribution as context-free.
- `Open question`: Which reported results remain stable under alternative datasets, baselines, or operational constraints is not established by this batch artifact alone.

## Considerations

Adoption would require checking data provenance, evaluation leakage, maintenance burden, and failure handling specific to the paper's domain. Related repository entries are useful for comparison but do not independently validate the primary paper. Any implementation should begin with public or synthetic data and an explicit stop condition.

## Strengths

- The primary source was inspected as both a validated PDF and full-paper HTML.
- The artifact separates source claims, reviewer interpretation, and implementation inference.
- Public provenance is preserved without uploading original source files.

## Weaknesses

- The batch process does not reproduce experiments or independently verify every table and figure.
- Text extraction can underrepresent equations, diagrams, tables, and formatting-dependent qualifications.
- Related-entry selection is a conceptual bridge for follow-on review, not a systematic literature review.

## Potential Improvements

1. Perform a paper-specific replication or benchmark rerun using the source's stated datasets and baselines.
2. Add a figure/table audit with exact evidence anchors and versioned extraction notes.
3. Compare the method against at least one strong contemporary baseline under matched conditions.

## Potential Implementations

1. `Evidence-aware review assistant`: use the paper's concepts to organize public documents, retain evidence IDs, and surface unsupported claims; use local-only processing and human review.
2. `Bounded evaluation harness`: encode the paper's stated inputs, outputs, and metrics with synthetic or authorized public data; require baseline comparison and failure reports.
3. `Research-to-prototype notebook`: expose the method as a small, inspectable experiment with versioned configuration, provenance links, and a stop condition for missing evidence.

## Three Ways to Exercise This Research

1. `Source-map exercise`: map the paper's headings, claims, and evidence to a public toy corpus; success means every claim has an evidence ID; stop when the source boundary is unclear.
2. `Synthetic evaluation exercise`: implement a minimal safe analogue with synthetic inputs and compare it with a simple baseline; success means the metric and failure cases are reproducible; stop before using restricted data.
3. `Related-entry comparison`: compare the three repository neighbors against the primary paper's mechanism and evaluation assumptions; success means differences are recorded without conflating context with proof.

## Example MVP Product

- `Product name`: Paper Evidence Map
- `Target user`: Research engineer or technical reviewer.
- `Problem`: Turning a full paper into traceable implementation and evaluation decisions.
- `Core workflow`: Ingest public paper URLs, map claims to evidence, connect related DEP context, and emit a review checklist.
- `Data requirements`: Public paper metadata, full-text HTML/PDF available to the user, evidence IDs, and optional synthetic test data.
- `Architecture`: Local parser, evidence ledger, Markdown renderer, and human approval gate.
- `Success metrics`: Evidence coverage, reviewer correction rate, reproducible checklist completion, and zero source-file leakage.
- `Risk controls`: Local-only source handling, no secrets, no restricted-data upload, explicit uncertainty labels, and human sign-off.
- `Limitations`: It cannot prove experimental validity or replace expert paper reading.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| DEP-A-20260715-Mapping Text to Multiplex | .lake-data/DEP-A/DEP-A-20260715-Mapping Text to Multiplex | Shared terms: multiple, multi | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-Mapping%20Text%20to%20Multiplex/README.md |
| DEP-A-20260715-ObjectCache Layerwise Obj | .lake-data/DEP-A/DEP-A-20260715-ObjectCache Layerwise Obj | Shared terms: layer, wise | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-ObjectCache%20Layerwise%20Obj/README.md |
| DEP-A-20260721-ALVTS Layerwise | .lake-data/DEP-A/DEP-A-20260721-ALVTS Layerwise | Shared terms: layer, wise | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260721-ALVTS%20Layerwise/README.md |

These three entries are repository context selected by conceptual overlap cues; they are not treated as independent evidence for the primary paper.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| S1 | https://arxiv.org/html/2602.09413 | Full-paper text and section-level review | 2026-08-19 | Primary public locator; source file withheld locally. |
| S2 | https://arxiv.org/pdf/2602.09413 | PDF/source integrity status | 2026-08-19 | Primary public locator; source file withheld locally. |
| S3 | https://arxiv.org/abs/2602.09413 | Canonical metadata and stable identifier | 2026-08-19 | Metadata page only; not treated as the paper document. |
| S4 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-Mapping%20Text%20to%20Multiplex/README.md | Related DEP context: multiple, multi | 2026-08-19 | Repository file used for conceptual context. |
| S5 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-ObjectCache%20Layerwise%20Obj/README.md | Related DEP context: layer, wise | 2026-08-19 | Repository file used for conceptual context. |
| S6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260721-ALVTS%20Layerwise/README.md | Related DEP context: layer, wise | 2026-08-19 | Repository file used for conceptual context. |

## Appendix

- Source integrity result: PDF and full-paper HTML passed the mandatory local gate; original source files were not copied, staged, committed, or sent to Slack.
- Related context basis:
- https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-Mapping%20Text%20to%20Multiplex/README.md — repository context entry `.lake-data/DEP-A/DEP-A-20260715-Mapping Text to Multiplex`; selected for conceptual overlap indicated by multiple, multi; not used as primary evidence.
- https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-ObjectCache%20Layerwise%20Obj/README.md — repository context entry `.lake-data/DEP-A/DEP-A-20260715-ObjectCache Layerwise Obj`; selected for conceptual overlap indicated by layer, wise; not used as primary evidence.
- https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260721-ALVTS%20Layerwise/README.md — repository context entry `.lake-data/DEP-A/DEP-A-20260721-ALVTS Layerwise`; selected for conceptual overlap indicated by layer, wise; not used as primary evidence.
- Review status: concise source-grounded batch review; no independent reproduction.
