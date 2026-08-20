---
title: "PreGenie Slides - DEP-E"
generated_at: "2026-08-06 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of PreGenie, an agentic multimodal framework for editable visual presentation generation."
source_status: "complete local PDF, full-paper HTML, and metadata inspected; public URLs only; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-06"
temporal_cutoff: "Public sources and related Black Lake artifacts inspected through 2026-08-06"
primary_url: "https://arxiv.org/abs/2505.21660"
stable_identifier: "arXiv:2505.21660v2; DOI:10.48550/arXiv.2505.21660; ACL DOI:10.18653/v1/2025.findings-emnlp.165"
confidence_summary: "High for identity, source integrity, and mechanism transcription; medium for author-reported results; low for independent reproducibility and deployment transfer."
safety_scope: "Offline research evaluation, bounded authoring assistance, and human-reviewed implementation planning only."
distribution_notes: "Original PDF, full-paper HTML, metadata HTML, source package, caches, and extracted text remain local and are not redistributed."
---

# PreGenie Slides - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2505.21660v2 | https://arxiv.org/abs/2505.21660 | Public metadata and paper locator; source file withheld. | 2026-08-06 | Inspected |
| S2 | Full paper | Primary artifact | HTML | arXiv:2505.21660v2 rendering | https://arxiv.org/html/2505.21660 | Full-paper evidence; local copy withheld. | 2026-08-06 | Integrity checked and inspected |
| S3 | Primary paper | Primary artifact | PDF | arXiv:2505.21660v2 | https://arxiv.org/pdf/2505.21660 | Full-paper evidence; local copy withheld. | 2026-08-06 | Integrity checked and inspected |
| S4 | ACL Anthology record | Publication record | HTML | 2025.findings-emnlp.165 | https://aclanthology.org/2025.findings-emnlp.165/ | Venue, pages, DOI, citation, and license notice. | 2026-08-06 | Inspected |
| S5 | ACL final paper locator | Near-primary publication | PDF | Findings of ACL: EMNLP 2025 | https://aclanthology.org/2025.findings-emnlp.165.pdf | Public locator; not collected or redistributed. | 2026-08-06 | Referenced for publication cross-check |
| S6 | Author publication pages | Author context | HTML | PreGenie publication listings | https://xxu068.github.io/; https://xjxu21.github.io/ | Public publication context; no paper-specific code link found on inspected pages. | 2026-08-06 | Inspected |
| S7 | Slidev | Framework context | Website | Current public site | https://sli.dev/ | Framework named by the paper; not treated as an implementation of PreGenie. | 2026-08-06 | Referenced |
| S8 | Related Black Lake entries | Related research | Markdown | Three DEP-E artifacts | Public GitHub links below | Derived reviews only; not evidence for the paper's metrics. | 2026-08-06 | Inspected |

The paper lists Xiaojie Xu, Xinli Xu, Sirui Chen, Haoyu Chen, Fan Zhang, and Ying-Cong Chen. The arXiv record reports submission on 2025-05-27 and revision on 2025-08-31. The ACL record identifies Findings of the Association for Computational Linguistics: EMNLP 2025, pages 3045–3063, and DOI `10.18653/v1/2025.findings-emnlp.165`.

The local source unit was initially partial because the PDF existed without metadata/full-paper HTML. One bounded archive repair preserved the valid PDF and produced qualifying metadata and full-paper HTML. The final PDF passed the `%PDF-` header and trailing `%%EOF` checks. The full HTML passed the size, body-text, document-marker, heading, and paper-structure checks. The source package was unavailable through the approved redirect policy. These source files and verification records remain local.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Primary/near-primary metadata | Title, authors, dates, version, venue, pages, DOI, abstract, and public locators | Identity and publication context | High | Metadata does not validate empirical results |
| E2 | S2, S3 | Primary paper | Introduction, related work, Slidev design, two-stage workflow, five roles, applications, limitations, and conclusion | Problem framing and mechanism | High for transcription | No experiment was rerun |
| E3 | S2, S3 | Primary paper | Qwen2.5 model choices, DOC2PPT selection of 200 image/table-rich samples, baselines, and evaluation protocol | Experimental setting | High for transcription | Dataset and model access were not independently verified |
| E4 | S2, S3 | Primary paper tables/figures | Table 1 ablations, Table 2 API-call/time records, and Figure 7 human/GPT-4o comparison direction | Reported evidence and cost tradeoff | Medium | Author-reported; exact figure scores were not independently transcribed |
| E5 | S2 | Primary paper | Limitations, Ethical Considerations heading, long-text/existing-slide applications | Boundary conditions and operational caution | High for stated limitations | Ethical section is substantively empty in the inspected rendering |
| E6 | S4-S6 | Near-primary publication and author context | Final publication metadata and author publication listings | Venue confirmation and code-availability boundary | Medium-high | Absence of a linked code repository is an inspection result, not proof that no private code exists |
| E7 | S8 | Related DEP artifacts | Evidence-bound agent loops, multimodal-agent evaluation, and VLM-probe limitations | Cross-DEP implementation synthesis | Medium | Related entries do not validate PreGenie's metrics |

## Executive Summary

PreGenie proposes an agentic framework for turning text-image documents into editable visual presentations. The contribution is a two-stage, multi-role workflow built on Slidev Markdown: first summarize and tag the multimodal input and generate initial code; then review the code and rendered pages iteratively, regenerating only where structural or visual checks fail. The paper's central practical idea is that source code review and rendered-page review catch different classes of failure.

The inspected full paper supports the mechanism and the bounded evaluation setting. The authors use Qwen2.5-72B-Instruct and Qwen2.5-VL-72B-Instruct, select 200 content-rich samples from DOC2PPT, and compare with PPTAgent, KCTV, and AutoPresent. In the displayed ablation table, PreGenie reports a 91.26% success rate versus 58.72% without code review and 89.68% without page review. Its CLIP and LongCLIP text-image relevance values are 30.19% and 32.37%, respectively, versus 29.02% and 30.82% without page review. These are author-reported results, not independent reproduction.

The evidence does not establish general presentation quality or deployment readiness. The visual-review stage is the reported latency hotspot, the exact human/GPT-4o figure values were not independently recovered, chart/graph understanding remains a stated weakness, hallucinated intermediate code remains possible, and no paper-specific public implementation was located in the inspected sources. Reviewer confidence is high for identity and mechanism, medium for reported comparative evidence, and low for reproducibility.

## Detailed Summary

### Problem context

Presentation generation must preserve content meaning while producing layouts that are readable, aesthetically coherent, image-aware, and editable. The paper positions direct slide-image generation as visually attractive but weak in editability and content control. It positions code-first systems as more editable but vulnerable to a gap between intermediate code and rendered output, especially when visual errors are not represented in the code.

### Method and architecture

PreGenie uses Slidev, a Markdown-based presentation framework. The five roles share context: the Text Summarizer extracts title, authors, affiliations, summaries, and other essential details; the Image Captioner assigns image titles, descriptions, and source locations; the Code Generator creates Slidev Markdown; the Code Reviewer checks syntax, content consistency, and user intent; and the Page Reviewer inspects rendered pages for overflow, crowding, alignment, and aesthetic issues. The paper assigns LLMs to text summarization/code roles and a VLM to image captioning/page review.

The workflow has two stages. Analysis and Initial Generation produces text and image Markdown notes and an initial deck. Iterative Review and Re-generation sends the generated code through code review, renders it, sends each page through visual review, and regenerates problematic pages until the page-level checks pass. The paper does not reintroduce code review after the page loop because it assumes that only a small portion of the deck changes at that stage; this is a design assumption that should be tested in replication.

### Data and evaluation

The implementation uses Qwen2.5-72B-Instruct for LLM roles and Qwen2.5-VL-72B-Instruct for VLM roles. The study samples 200 DOC2PPT examples rich in images, tables, and other content. Multi-page comparisons include PPTAgent and KCTV; AutoPresent is used for a single-page design comparison. Traditional metrics include text similarity, CLIP/LongCLIP text-image relevance, success rate, and figure proportion. The paper also uses GPT-4o and 20 experienced users to score 10 slide sets across Page Design, Text Coherence, Text-Image Relevance, and Page Consistency on a 1–10 scale.

### Reported results

Table 1 has six percentage columns: Rough-L, Coverage, CLIP, LongCLIP, Success Rate, and Figure Proportion. The `Ours` row is `21.95, 27.70, 30.19, 32.37, 91.26, 88.35`. Removing Page Review produces `22.16, 28.08, 29.02, 30.82, 89.68, 88.61`; removing Code Review produces `18.47, 27.21, 28.74, 29.49, 58.72, 81.59`; PPTAgent produces `20.81, 29.14, 29.53, 30.18, 88.36, 76.12`; and KCTV reports `25.67, 33.82, –, –, 94.90, –`. The display supports a stronger claim for code review's relationship to execution success than for a universal improvement across every text metric.

Table 2 reports 3 Stage-1 API calls and 14.6 seconds, 4.4 average code-review calls and 8.9 seconds, and 3.8 average visual-review calls and 51.5 seconds. The paper's text says the visual reviewer accounts for a significant share of the longer generation time. Figure 7 reports that both humans and GPT-4o prefer PreGenie overall to PPTAgent, with the largest qualitative advantage in page design and page consistency; exact plotted values were not treated as independently verified measurements.

### Applications, limitations, and conclusion

The paper demonstrates generation from long text by using an external LLM and image-generation model to create illustrations, then feeding those images into the captioner and code generator. It also demonstrates extracting content from poorly designed existing slides and reformatting them. These applications show extensibility, not validated robustness.

The authors state that MLLMs struggle with complex charts and graphs and may hallucinate intermediate code unrelated to the input. These limits directly affect scientific and business use because a polished slide can still misstate evidence. The Ethical Considerations heading is present but contains no substantive discussion in the inspected HTML. The conclusion repeats the claims about aesthetics, content consistency, and human preference within the tested setting.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | PreGenie uses a two-stage agentic workflow with five specialized LLM/VLM roles and Slidev Markdown as the editable intermediate representation. | Author method claim | E2 | Directly supported by the method sections and Figure 2 description. | High |
| C2 | Code review and rendered-page review target complementary failure modes. | Author method claim and reviewer interpretation | E2, E4 | The method directly supports the distinction; the causal size of the benefit remains author-reported. | Medium-high |
| C3 | In the displayed ablation, code review is associated with a large success-rate difference: 91.26% versus 58.72% without code review. | Author empirical claim | E4 | The table supports the number in the stated setting; no rerun or uncertainty interval was provided in this review. | Medium |
| C4 | Page review improves the reported CLIP and LongCLIP values over its ablation. | Author empirical claim | E4 | The displayed values support the direction, but the figure/table does not establish generalization beyond 200 selected samples. | Medium |
| C5 | PreGenie aligns more closely with human design preferences than PPTAgent in the reported 10-set evaluation. | Author empirical claim | E4 | The paper reports the direction, but exact figure values and rater agreement were not independently transcribed. | Medium |
| C6 | PreGenie is not yet a general-purpose or autonomous publication system. | Reviewer interpretation constrained by source limits | E5, E6 | Chart/graph weakness, hallucination risk, latency, missing implementation, and limited evaluation support this boundary. | High for the caution; not an author claim |

## Methodology

- `Research objective`: Preserve a source-grounded, public-safe review of PreGenie's mechanism, evidence, limitations, and implementation relevance.
- `Sources inspected`: The selected local PDF, repaired full-paper HTML and metadata HTML; the public arXiv record; the ACL Anthology record and final-paper locator; two author publication pages; Slidev's public locator; and exactly three related Black Lake DEP manuscripts.
- `Discovery strategy`: Enumerated the local archive with `rg --files -g "*.pdf"`; treated each PDF parent directory as a unit; sorted units and drew a uniform random index; then inspected arXiv/ACL/public author sources and related repository artifacts.
- `Selection evidence`: 75,960 PDFs and 75,957 units were enumerated; index 66,272 selected arXiv:2505.21660. The dedup scan checked ID, DOI, normalized title, slug, prior `.logs`, `.reports`, `.lake-data`, automation memory, metadata-only inventory rows, and same-paper-within-24-hours markers. The first draw was accepted with zero exclusions and zero reselections.
- `Source-integrity handling`: The initial unit was classified partial because full-paper HTML and metadata HTML were missing. One bounded archive repair preserved the valid PDF and produced qualifying HTML/metadata/provenance/verification artifacts before review. The final PDF and full HTML passed all required gates.
- `Inclusion criteria`: Included primary-paper identity, method, data, experiments, results, limitations, publication metadata, and related entries with concrete overlap in multimodal agents, visual evaluation, or evidence-bound review.
- `Exclusion criteria`: Abstract-only evidence, invalid/truncated source documents, unverified code or data claims, and related works without concrete conceptual overlap were excluded from central claims. The optional source package was not used because it was unavailable through the approved collector route.
- `Analytical approach`: Mixed empirical, conceptual, comparative, implementation, product, safety/ethics, and replication review.
- `Evidence handling`: Major claims are labeled as author claims, source metadata, reviewer interpretations, or derived implementation inferences and mapped to E-identifiers.
- `Uncertainty handling`: Exact figure scores, code availability, causal attribution of ablations, rater agreement, and deployment transfer are explicitly marked unavailable or unverified.
- `Claim selection`: Priority was given to the two-stage mechanism, role decomposition, ablation table, evaluation protocol, latency table, limitations, and source availability.
- `Cross-checking`: arXiv HTML, local PDF, ACL metadata, and author publication context were cross-checked. No code or experiment was executed.
- `Safety handling`: Examples are offline, synthetic/public-data oriented, human-reviewed, and designed to prevent unsupported publication or automatic consequential action.
- `Reviewer stance`: DEP-ready research review with bounded implementation and product translation.

## Scope, Constraints, and Assumptions

- `Scope`: PreGenie's problem, method, evaluation setting, reported evidence, limitations, related DEP bridges, and safe implementation implications.
- `Temporal boundary`: Public sources and related Black Lake artifacts inspected through 2026-08-06; paper revision v2 and ACL Findings record are preserved.
- `Evidence limits`: Results were not reproduced; source datasets, model weights, prompts, API endpoints, and paper-specific code were not independently obtained; exact human/GPT-4o figure values were not transcribed.
- `Assumptions`: The repaired arXiv HTML, local PDF, and ACL publication record describe the same research work; Table 1 column order follows the paper's displayed header order.
- `Constraints`: Public output excludes local paths, source files, caches, extracted text, private metadata, credentials, and exact local execution details. Copyrighted document images and potentially sensitive input content are not redistributed.
- `Out of scope`: Autonomous presentation publication, unrestricted external-model operation, claims of factual correctness for generated slides, and clinical/legal/financial use.
- `Intended use`: Research review, DEP deposition, evaluation planning, safe authoring-tool ideation, and replication backlog creation.
- `Audience`: Multimodal researchers, presentation-tool engineers, evaluation teams, product designers, and Black Lake reviewers.
- `Reproducibility boundary`: A future reproduction needs a fixed Slidev version, prompts, Qwen model versions, DOC2PPT sample manifest, baseline versions, rendering environment, evaluator protocol, and cost accounting.
- `Operational boundary`: Discusses review-loop architecture conceptually and with toy checks only; it does not provide unattended publishing or external-content ingestion automation.
- `Data sensitivity`: Public scholarly sources; any source-document contents used by a future implementation should remain licensed, minimized, and local by default.

## Observations

- `Observed pattern`: The strongest mechanism is not a new model layer but the insertion of a rendered-observation loop between code generation and final acceptance.
- `Technical implication`: A presentation pipeline should expose both source-level and render-level evidence because either view can miss failures visible in the other.
- `Contradiction or tension`: Code review is associated with a large success-rate difference, while page review costs more time and slightly lowers Figure Proportion relative to its ablation; the system therefore optimizes multiple objectives rather than one scalar.
- `Evidence-quality implication`: The human-preference result is directionally useful, but its exact magnitude, rater agreement, and cross-cultural stability are not visible in the inspected text.
- `Open question`: Whether a calibrated smaller VLM plus deterministic geometry checks can match the reported quality at substantially lower cost remains unanswered.

## Considerations

Generated presentations can launder unsupported claims into polished visual form. A safe system should require source links for claims, preserve the input-to-slide mapping, show diffs after regeneration, and route uncertain or chart-heavy pages to human review. Input documents may contain copyrighted images, confidential business material, personal data, or unpublished research; local processing and retention controls are therefore preferable.

The paper's use of external MLLM APIs and image-generation services introduces cost, privacy, model-version, and availability dependencies. A production-like evaluation must record model revisions, prompts, render versions, latency, API errors, and reviewer abstentions. Visual quality should not be used as a proxy for factual correctness, accessibility, or legal compliance.

## Strengths

- The intermediate Slidev representation preserves editability and makes code-level review possible.
- The five-role decomposition exposes where multimodal perception, language generation, structural review, and visual review occur.
- The ablations directly test the two review components instead of presenting only a final system score.
- The study combines traditional metrics with human and GPT-4o evaluations, making the quality question multidimensional.
- The paper acknowledges chart/graph understanding and hallucinated code as consequential failure modes.

## Weaknesses

- The evaluation uses 200 selected DOC2PPT samples and does not establish coverage of multilingual, accessibility, or chart-heavy inputs.
- The displayed human/GPT-4o comparison does not provide enough textual detail here to audit exact values, variance, or inter-rater agreement.
- The code/page ablation differences are observational comparisons from one reported setup, not a causal estimate with uncertainty intervals.
- Visual review is expensive and slow in the reported configuration, but the paper does not map a quality-cost frontier.
- No paper-specific public implementation, fixed prompts, or complete reproduction package was identified in the inspected sources.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish a fixed benchmark manifest with chart, multilingual, and accessibility strata | Evaluation | Reduces sample-selection ambiguity | Better coverage and transfer evidence | Additional annotation and licensing work | Stratified held-out evaluation |
| Add geometry and accessibility validators before VLM review | Efficiency and safety | Cheap checks can prefilter deterministic failures | Lower review cost and clearer failure attribution | Validator blind spots | Compare validator recall with human review |
| Release prompts, model versions, render config, and score variance | Reproducibility | Makes the reported ablations auditable | Independent replication and cost comparison | Release and maintenance burden | Seeded reruns and exact-output checks |
| Add claim-level provenance and regeneration diffs | Factuality | Prevents polished slides from obscuring content drift | Easier reviewer approval and rollback | More metadata and UI complexity | Inject controlled claim mutations |
| Evaluate smaller open models and reviewer abstention | Cost and robustness | The current visual stage dominates latency | Lower cost with visible uncertainty | Quality may degrade on complex pages | Pareto frontier over quality, latency, and abstentions |

## Potential Implementations

1. `Evidence-bound academic deck builder`: User is a researcher; input is a licensed paper or brief; mechanism is Slidev generation plus source-linked claims and code/page checks; output is an editable draft and review ledger; risk control is human approval and no source-file upload; evaluation uses a public/synthetic benchmark with chart and accessibility cases.
2. `Visual regression gate for generated reports`: User is a documentation team; input is versioned Markdown and images; mechanism is deterministic rendering followed by geometry, text-density, and multimodal review; output is a diff report and pass/needs-review status; risk control is local processing, thresholds per template, and rollback; evaluation measures failure recall and reviewer time.
3. `Existing-deck repair assistant`: User is an analyst; input is an authorized deck or PDF; mechanism is content extraction, image tagging, page-level regeneration, and before/after evidence cards; output is a selected-page repair proposal; risk control is minimal retention, page-scoped changes, and explicit export approval; evaluation measures factual preservation, layout correction, and accessibility checks.

## Three Ways to Exercise This Research

1. `Synthetic overflow loop`: Objective—test whether page review catches deterministic overflow. Inputs—three synthetic Slidev pages with controlled text and image bounds. Method—run the toy code gate, render locally, inject one overflow, and record page-review findings. Output—an auditable before/after Markdown record. Success—every injected overflow is flagged; stop if private content enters the fixture.
2. `Ablation replication slice`: Objective—compare code review and page review on a small licensed/public slide set. Inputs—ten public or synthetic document examples, fixed prompts, and one open model stack. Method—run full, no-code-review, and no-page-review variants with fixed seeds and human scoring. Output—metric table, latency log, and uncertainty notes. Success—directional effects are stable across seeds; stop if model or rendering versions cannot be pinned.
3. `Claim-preservation challenge`: Objective—measure whether visual improvement causes content drift. Inputs—short public briefs with explicit claims and images. Method—generate slides, apply bounded regeneration, and compare source-linked claim cards before and after. Output—factuality and layout-diff report. Success—layout corrections do not change approved claims without an explicit flag; stop before any automatic publication.

## Example MVP Product

- `Product name`: Slide Evidence Coach
- `Target user`: Research and documentation teams producing editable, source-grounded decks.
- `Problem`: Generated slides can look polished while hiding overflow, weak text-image pairing, or unsupported content changes.
- `Core workflow`: Register a licensed/public brief; extract claims and images; generate Slidev Markdown; run deterministic code checks; render pages; run bounded visual review; display claim links, diffs, latency, and approval state.
- `Data requirements`: Public or licensed briefs, approved images, source URLs, a versioned Slidev template, synthetic regression fixtures, and aggregate reviewer records.
- `Architecture`: Local document parser; claim/source ledger; Slidev generator; deterministic validators; renderer; VLM reviewer adapter; diff viewer; append-only approval record.
- `Success metrics`: Claim-preservation rate, overflow detection recall, human acceptance agreement, reviewer time per deck, latency per page, and abstention rate on charts or ambiguous layouts.
- `Risk controls`: Local-only default, source-link requirements, no raw secret logging, page-scoped regeneration, human approval before export, model/version pinning, and a hard stop on unsupported claims.
- `Limitations`: It cannot prove factual correctness, replace subject-matter review, guarantee aesthetic agreement, or safely process unlicensed/private documents without an approved deployment boundary.
- `MVP boundary`: One Slidev template, public/synthetic data only, one open model family, three deterministic validators, no automatic publication, and no model training.
- `Deployment model`: Local CLI or notebook with a Markdown/JSON decision record.
- `Evaluation plan`: Golden synthetic fixtures, fixed public examples, three-seed smoke tests, reviewer walkthroughs, and chart/accessibility stress cases.
- `Failure modes`: Unsupported claim drift, VLM evaluator bias, false visual alarms, layout regressions after regeneration, hidden API cost, and inaccessible source content.
- `Maintenance plan`: Version templates, renderers, model adapters, prompts, thresholds, source policies, and regression fixtures; require review for policy changes.

## Related Research and Reading

| Item | Type | Relevance | URL / Repository Path |
|---|---|---|---|
| PreGenie | Primary paper and final publication | Core method, evaluation, limitations, and publication record | https://arxiv.org/abs/2505.21660; https://doi.org/10.18653/v1/2025.findings-emnlp.165 |
| Slidev | Official framework context | Editable Markdown-to-slide substrate named by the paper | https://sli.dev/ |
| Evidence-Gated Agents DEP-E | Related Black Lake artifact | Evidence boundaries, slow/fast validation, and reviewer escalation | `.lake-data/DEP-E/DEP-E-20260730-Evidence-Gated Agents/evidence-gated-agents.md` |
| Kimi K2.5 Visual Agentic DEP-E | Related Black Lake artifact | Multimodal agent evaluation and visual-agent workflow context | `.lake-data/DEP-E/DEP-E-20260727-Kimi K2 5 Visual Agentic/kimi_k2_5_visual_agentic_manuscript.md` |
| VLM Probing DEP-E | Related Black Lake artifact | Diagnostic limits, leakage, and non-causal visual-language signals | `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` |

Exactly three related Black Lake entries are used in the synthesis: Evidence-Gated Agents, Kimi K2.5 Visual Agentic, and VLM Probing. They provide context only and do not validate PreGenie's reported metrics.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2505.21660 | Identity, version, authors, abstract, DOI, and submission history | 2026-08-06 | Primary metadata source |
| R2 | https://arxiv.org/html/2505.21660 | Full-paper method, experiments, applications, limitations, and conclusion | 2026-08-06 | Full-paper source inspected locally; source file withheld |
| R3 | https://arxiv.org/pdf/2505.21660 | PDF integrity and source cross-check | 2026-08-06 | PDF inspected locally; not redistributed |
| R4 | https://aclanthology.org/2025.findings-emnlp.165/ | Final venue, pages, DOI, citation, and license notice | 2026-08-06 | Near-primary publication record |
| R5 | https://aclanthology.org/2025.findings-emnlp.165.pdf | Final-paper locator and publication cross-check | 2026-08-06 | Not collected or redistributed |
| R6 | https://xxu068.github.io/; https://xjxu21.github.io/ | Author publication context and code-link availability check | 2026-08-06 | Context only |
| R7 | https://sli.dev/ | Slidev framework context | 2026-08-06 | Framework locator named by the paper |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260730-Evidence-Gated%20Agents/evidence-gated-agents.md | Related evidence-gated agent synthesis | 2026-08-06 | Related DEP context only |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260727-Kimi%20K2%205%20Visual%20Agentic/kimi_k2_5_visual_agentic_manuscript.md | Related multimodal visual-agent synthesis | 2026-08-06 | Related DEP context only |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md | Related VLM diagnostic and evaluator-limit synthesis | 2026-08-06 | Related DEP context only |

## Appendix

### Selection and deduplication validation

The local archive contained 75,960 PDF paths and 75,957 unique parent-directory paper units. A sorted-unit uniform random index draw selected zero-based index 66,272. The selected unit normalized to arXiv:2505.21660 from its filename and README. Scans for the arXiv ID, arXiv DOI, publisher DOI, normalized title, slug, prior Arxiv DEP outputs, automation memory, and same-paper-within-24-hours markers found no processed-paper collision. Two metadata-only author-inventory rows were treated as discovery metadata, not prior research deposits. No reselection was needed.

### Source-integrity validation

The PDF measured 4,770,862 bytes, began with `%PDF-1.5`, and contained a trailing `%%EOF`. The full-paper HTML measured 115,005 bytes, yielded 52,185 body characters after script/style removal, contained 60 heading markers and a document marker, and contained 8 paper-structure term classes. Metadata HTML was non-empty and no partial files remained. The optional source package was unavailable. Source files were withheld from this public repository.

### Metric mapping

Table 1's six columns are ordered as Rough-L, Coverage, CLIP, LongCLIP, Success Rate, and Figure Proportion. The displayed `Ours` row is `21.95, 27.70, 30.19, 32.37, 91.26, 88.35`. This explicit mapping is included because the HTML table separates headers from row cells and because the human/GPT-4o results are figure-based rather than fully represented as text.

### Attribution Block

- Source URL: https://arxiv.org/abs/2505.21660
  - Applies to: this manuscript
  - Notes: Canonical arXiv record; source files withheld locally.
- Source URL: https://arxiv.org/html/2505.21660
  - Applies to: this manuscript
  - Notes: Full-paper evidence; no HTML file is deposited here.
- Source URL: https://aclanthology.org/2025.findings-emnlp.165/
  - Applies to: this manuscript
  - Notes: Final publication metadata and DOI.
- Source URL: https://sli.dev/
  - Applies to: methodology and implementation context
  - Notes: Slidev framework locator named in the paper.
