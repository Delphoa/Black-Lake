---
title: "One-Touch Instruction Routing"
generated_at: "2026-07-19 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "A source-grounded review of multimodal task-instruction recommendation with template retrieval and constrained decoding."
source_status: "verified complete local PDF, official full-paper HTML, and metadata HTML inspected; all sources withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-19"
temporal_cutoff: "Sources and repository context inspected through the batch invocation."
primary_url: "https://arxiv.org/abs/2509.13773"
stable_identifier: "arXiv:2509.13773v1; DOI:10.48550/arXiv.2509.13773"
deployment_job_id: "BLAD-2200-20260719-7D93E819"
deployment_item_id: "BLAD-2200-20260719-7D93E819-P05"
confidence_summary: "High for paper identity and reported method/table transcription; medium for comparative generalization; low for on-device readiness."
safety_scope: "offline evaluation, privacy-preserving model design, allowlisted actions, confirmation gates, and human review"
distribution_notes: "No PDF, HTML, extracted text, cache, dataset, code, local path, or source document is redistributed."
---

# One-Touch Instruction Routing

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Canonical arXiv record | Metadata | HTML | arXiv:2509.13773v1 | https://arxiv.org/abs/2509.13773 | Metadata is not full-paper evidence. | 2026-07-19 | Inspected. |
| S2 | Official full-paper rendering | Primary paper | HTML | arXiv:2509.13773v1 | https://arxiv.org/html/2509.13773 | Verified local copy withheld. | 2026-07-19 | Inspected in full. |
| S3 | Paper PDF | Primary paper | PDF | arXiv:2509.13773v1 | https://arxiv.org/pdf/2509.13773 | Verified local copy withheld. | 2026-07-19 | Inspected through extraction. |
| S4 | arXiv-issued DOI | Identity | DOI | 10.48550/arXiv.2509.13773 | https://doi.org/10.48550/arXiv.2509.13773 | Persistent locator. | 2026-07-19 | Resolved. |
| S5 | VLM Probing DEP | Related | Markdown | DEP-E-20260712 | `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` | Related synthesis only. | 2026-07-19 | Inspected. |
| S6 | DMNN Conditional Paths DEP | Related | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` | Related synthesis only. | 2026-07-19 | Inspected. |
| S7 | Efficient FM Survey DEP | Related | Markdown | DEP-E-20260718 | `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` | Related synthesis only. | 2026-07-19 | Inspected. |
| S8 | Selection, repair, and cache records | Process evidence | Private records | `BLAD-2200-20260719-7D93E819-P05` | Local paths withheld | Integrity, dedup, and locality only. | 2026-07-19 | Verified. |

Authors: Zhipeng Bian, Jieming Zhu, Xuyang Xie, Quanyu Dai, Zhou Zhao, and Zhenhua Dong. Submitted 2025-09-17. Deployment job `BLAD-2200-20260719-7D93E819`; item `BLAD-2200-20260719-7D93E819-P05`.

## Evidence Ledger

| Evidence ID | Source | Claim or observation | Evidence type | Confidence | Limits |
|---|---|---|---|---|---|
| E1 | S2, sections 3.1-3.3 | MIRA combines structured reasoning, template retrieval, and a tokenizer-aligned prefix tree. | Direct method description. | High | No independent replication. |
| E2 | S2, section 4.1 | Dataset reports 4,952 train pairs, 956 test pairs, 1,000 users, three-plus annotations, and kappa 0.85. | Source-reported dataset facts. | High | Collection and demographic details are not independently audited. |
| E3 | S2, Table 1 | Qwen2.5VL-7B MIRA reports F1 0.9121 and HR@3 0.9629. | Comparative result. | High transcription; medium generalization. | Fixed task, split, and baseline set. |
| E4 | S2, Table 2 | Template augmentation reports 15.8%-24.1% F1 improvements. | Ablation. | High transcription; medium causal breadth. | Template construction and retrieval are coupled. |
| E5 | S2, section 4.3.4 | User study reports 93% and 95% validity ratios. | Human evaluation. | Medium | Preference does not prove long-term safety or utility. |
| E6 | S2, limitations | Modality coverage, template gaps, robustness, scalability, and privacy remain open. | Author-stated limitations. | High | Mitigations are future work. |
| E7 | S5-S7 | Representation quality, route stability, and end-to-end resource evidence complement the paper. | Reviewer synthesis. | Medium | Cross-paper bridge, not a source claim. |

## Executive Summary

MIRA reframes smartphone AI-service discovery as a bounded recommendation problem. A user long-presses a text or image object; a multimodal model extracts entities and intent, a retrieved template refines the reasoning, and a prefix tree constrains the final instruction to an approved candidate library. The paper reports strong gains over zero-shot and vanilla SFT baselines, including F1 0.9121 and HR@3 0.9629 for Qwen2.5VL-7B, plus high user-study validity ratios. Those results support further evaluation, not a deployment claim. The principal unresolved boundary is that candidate membership does not establish intent correctness, permission, privacy, or device-level efficiency.

## Detailed Summary

The task begins with a trigger object, such as a reservation image or a text fragment. During dataset construction, a teacher model receives the trigger and gold instruction and produces a three-part trace: entity extraction, contextual relevance analysis, and instruction synthesis. A smaller multimodal model is then supervised to generate the trace and instruction without the gold answer.

Template augmentation addresses incomplete or inconsistent traces. MIRA embeds an initial trace, retrieves a high-level reasoning template above a similarity threshold, and asks the model to instantiate the template against the trigger. About 80 templates were distilled with a closed model; low-similarity traces can become candidates for later clustering and human-governed library updates.

The final decoder switches to a prefix tree after the reasoning delimiter. Invalid tokens are masked at every step, so the decoded string belongs to the finite instruction set. This is a useful safety and quality primitive, but it only guarantees grammatical membership. A valid instruction may still be irrelevant, unauthorized, privacy-sensitive, or harmful if upstream recognition or routing is wrong.

The evaluation covers InternVL2.5 and Qwen2.5VL model sizes, four recommendation metrics, template ablation, threshold sensitivity, error analysis, and a user study. The strongest evidence is internal consistency across model sizes and the direct template ablation. External validity is limited by one dataset, selected baselines, source-reported measurements, and the absence of prospective device deployment.

## Key Claims and Evidence

1. **Bounded generation:** Section 3.3 supports the claim that prefix constraints restrict output to valid library strings. This does not prove semantic correctness.
2. **Template contribution:** Table 2 supports a measurable association between template augmentation and higher F1 across four models. It does not isolate every construction choice.
3. **Comparative accuracy:** Table 1 reports consistent gains over zero-shot and vanilla SFT baselines. Comparability is limited to the authors' dataset and task definition.
4. **Efficiency signal:** Table 3 reports 116 average tokens and 11.2 seconds for the 7B MIRA point. This is not a full smartphone benchmark.
5. **Known failures:** Analysis of 100 errors identifies entity omission, template misalignment, and trigger ambiguity. These categories motivate abstention and multi-signal evaluation.

## Methodology

### Paper Method

MIRA uses teacher-forced reasoning traces for SFT, similarity-based retrieval from a structured template library, and constrained autoregressive decoding through a tokenizer-derived trie. Retrieval thresholds are evaluated from 0.4 to 0.8, with 0.6 reported as best across four models. Evaluation uses recall, precision, F1, HR@1, and HR@3, followed by ablation, error analysis, and participant selection of expected recommendations.

### Review Method

The review inspected the canonical metadata, verified PDF, official full-paper HTML, tables, limitations, and exactly three repository entries. Claims were labeled as direct, source-reported, or reviewer synthesis. No code or dataset execution was treated as evidence.

### Random Selection and Deduplication

The archive contained 75,778 PDFs across 75,776 unique parent units. Uniform index 11,296 was selected on the first draw. Repository, memory, companion-repository, title, DOI, arXiv ID, slug, 24-hour, and current-job checks found no collision; exclusions and reselections were zero.

### Integrity and Locality

The unit began partial because full-paper HTML was absent. One bounded repair preserved the valid 3,231,506-byte PDF and added verified official HTML with 41,960 body characters, 22 headings, a document marker, and five structure terms. The cache completed for PDF and HTML. All source and cache files remain local.

## Scope, Constraints, and Assumptions

- Scope is instruction recommendation from text and image triggers, not general autonomous smartphone control.
- Reported results are transcribed from the paper and not independently replicated.
- Candidate-constrained output is assumed to use a correctly versioned tokenizer and trie.
- Permission, confirmation, privacy, retention, and action execution are outside the reported model evaluation.
- The paper's 7B model and two-GPU setup do not establish on-device feasibility.
- Related DEP connections are reviewer synthesis.

## Observations

- The trie creates a clean boundary between open reasoning and finite action selection.
- Template retrieval adds reusable structure but introduces a second learned routing surface that can drift.
- The strongest model reports very high hit rate, yet ambiguity remains a first-class error category.
- Reported inference time is comparable to closed-model APIs, while token count is much lower; hardware and serving context are insufficient for device conclusions.
- A permission-aware action catalog would make the constrained decoder more operationally meaningful.

## Considerations

- Add abstention when entity confidence, template similarity, or action margin is low.
- Treat sensitive triggers as a separate policy class with local processing and explicit confirmation.
- Version templates, embeddings, tokenizer, trie, and action metadata together.
- Evaluate subgroup, language, modality, and long-tail performance before expansion.
- Measure end-to-end interaction latency, memory, energy, thermals, and network dependence on target devices.

## Strengths

- Modular method with interpretable control points.
- Finite-candidate decoding is directly enforceable and testable.
- Evaluation spans four model sizes and includes ablation, sensitivity, error analysis, and a user study.
- Paper states important modality, generalization, robustness, and privacy limitations.

## Weaknesses

- Dataset and annotation provenance are summarized more than deeply audited.
- Baseline coverage is narrow for finite-candidate ranking/classification alternatives.
- Closed-model template distillation complicates reproducibility.
- Device readiness is inferred from size and selected latency statistics rather than measured end to end.
- User preference does not quantify false-action cost, permission errors, or longitudinal utility.

## Potential Improvements

- Add calibrated confidence and explicit abstention.
- Compare against retrieval-only, classifier, reranker, and finite-state baselines.
- Publish stratified performance for rare entities, languages, sensitive content, and ambiguous intents.
- Require human approval for template-library updates and measure route drift.
- Evaluate privacy-preserving on-device and hybrid serving configurations.
- Attach permission and confirmation policy to every terminal action.

## Potential Implementations

An initial implementation should remain offline: reproduce the action-candidate evaluator, build a versioned policy trie, and add a shadow-mode template router that never executes device actions. Promotion should require stable slice metrics, calibrated abstention, privacy review, and target-device measurements.

## Three Ways to Exercise This Research

1. **Recompute metrics:** Recreate recall, precision, F1, HR@1, and HR@3 from frozen prediction records and stratify by ambiguity and sensitivity.
2. **Stress the router:** Perturb entities, template similarity, and tokenizer versions; measure route changes, abstention, and invalid terminal states.
3. **Run a device shadow study:** Log only de-identified candidate rankings and user confirmations without executing actions; measure latency, utility, and false-action cost.

## Example MVP Product

**ActionLens** is an offline evaluation console for multimodal instruction routers. It ingests de-identified trigger fixtures, candidate actions, template scores, policy labels, and expected outputs. It renders the reasoning/template/action decision chain, blocks unauthorized terminals, computes slice metrics, and exports a signed evaluation manifest. It does not control a phone or transmit source content.

## Related Research and Reading

1. **VLM Probing:** representation probes can test whether the entities needed by the action router are encoded before debugging the final instruction.
2. **DMNN Conditional Paths:** dynamic routing requires route-stability and real-runtime evaluation; the same applies to template selection.
3. **Efficient FM Survey:** edge deployment must be evaluated across architecture, algorithms, serving, memory, energy, and device constraints.

## Source References

1. Zhipeng Bian et al., *MIRA: Empowering One-Touch AI Services on Smartphones with MLLM-based Instruction Recommendation*, https://arxiv.org/abs/2509.13773
2. Official full-paper HTML, https://arxiv.org/html/2509.13773
3. Official PDF, https://arxiv.org/pdf/2509.13773
4. Persistent DOI, https://doi.org/10.48550/arXiv.2509.13773
5. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`
6. `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md`
7. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md`

## Appendix

### Validation Checklist

- Title and H1 are identical and no more than 40 characters.
- All required schema sections are present.
- Evidence distinguishes paper claims from reviewer synthesis.
- Random selection and dedup/reselection outcomes are recorded.
- Source-integrity thresholds passed before review.
- Public allowlist contains generated Markdown and required index/status records only.
- No source document, extracted text, cache, private path, exact timestamp, or timezone label is published.
