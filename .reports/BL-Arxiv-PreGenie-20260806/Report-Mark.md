# BL-Arxiv-PreGenie-20260806 Report-Mark

## Source Metadata

| Field | Value |
|---|---|
| Title | *PreGenie: An Agentic Framework for High-quality Visual Presentation Generation* |
| Authors | Xiaojie Xu; Xinli Xu; Sirui Chen; Haoyu Chen; Fan Zhang; Ying-Cong Chen |
| arXiv | [2505.21660v2](https://arxiv.org/abs/2505.21660v2) |
| arXiv DOI | [10.48550/arXiv.2505.21660](https://doi.org/10.48550/arXiv.2505.21660) |
| Publication | Findings of ACL: EMNLP 2025, pages 3045–3063 |
| Publisher DOI | [10.18653/v1/2025.findings-emnlp.165](https://doi.org/10.18653/v1/2025.findings-emnlp.165) |
| Dates | Submitted 2025-05-27; revised 2025-08-31; ACL volume November 2025 |
| Evidence inspected | Complete local PDF, full-paper HTML, and metadata HTML; public ACL record and author publication pages |
| Source status | Complete-source gate passed; source files withheld locally; no source package available through the repair policy |

## Research Notes

PreGenie addresses presentation generation from text-image documents. The paper argues that direct slide-image generation weakens editability and content control, while code-first systems can leave a gap between generated code and the rendered visual result. Its central design is a two-stage agentic loop built on Slidev Markdown: analysis and initial generation, followed by iterative code and page review with regeneration.

The pipeline assigns five roles over shared context: a Text Summarizer, Image Captioner, Code Generator, Code Reviewer, and Page Reviewer. LLMs handle text summarization, code generation, and code review; a VLM handles image captioning and visual page review. The page reviewer inspects rendered slides for overflow, crowding, alignment, and other visual failures that may not be visible in source code.

The reported implementation uses Qwen2.5-72B-Instruct and Qwen2.5-VL-72B-Instruct, evaluates 200 image- and table-rich samples from DOC2PPT, and compares against PPTAgent, KCTV, and AutoPresent. Table 1 reports the following author-reported rows, with all values expressed as percentages: Ours `21.95/27.70/30.19/32.37/91.26/88.35`; Ours without Page Review `22.16/28.08/29.02/30.82/89.68/88.61`; Ours without Code Review `18.47/27.21/28.74/29.49/58.72/81.59`; PPTAgent `20.81/29.14/29.53/30.18/88.36/76.12`; and KCTV `25.67/33.82/–/–/94.90/–`. The columns are Rough-L, Coverage, CLIP, LongCLIP, Success Rate, and Figure Proportion.

The ablations support a bounded interpretation: page review improves the two text-image relevance columns over its ablation, while code review is associated with the largest success-rate difference. KCTV has higher text-only scores in the displayed table but does not provide the same image-generation comparison. A separate evaluation uses 20 experienced users and GPT-4o to score 10 slide sets from 1–10 on Page Design, Text Coherence, Text-Image Relevance, and Page Consistency; the paper reports an overall preference for PreGenie over PPTAgent, but the exact figure values were not independently transcribed.

Table 2 reports average API calls and generation time of 3 calls/14.6 seconds for Stage 1, 4.4 calls/8.9 seconds for code review, and 3.8 calls/51.5 seconds for visual review. This makes the VLM-based page review the visible latency hotspot. The paper also demonstrates long-text and existing-slide applications, but those examples do not establish production readiness.

The source's stated limitations are important: current MLLMs struggle with charts and graphs, and hallucination can produce intermediate code unrelated to the input. The paper contains an Ethical Considerations heading but no substantive ethical analysis in the inspected rendering. No paper-specific public code repository was located in the paper, ACL record, or inspected author publication pages; the paper's baseline comparisons use other authors' repositories and APIs.

## Evidence and Attribution

| ID | Source | Evidence used | Assessment |
|---|---|---|---|
| E1 | [arXiv record](https://arxiv.org/abs/2505.21660) | Title, authors, revision dates, DOI, abstract, subject, and canonical paper URLs | High for identity and version |
| E2 | [arXiv full-paper HTML](https://arxiv.org/html/2505.21660) | Introduction, related work, method, applications, limitations, and conclusion | High for source-grounded mechanism notes; no independent reproduction |
| E3 | [arXiv PDF](https://arxiv.org/pdf/2505.21660) | Full-paper integrity and cross-check of method/results structure | High for source integrity; source file withheld |
| E4 | [ACL Anthology record](https://aclanthology.org/2025.findings-emnlp.165/) | Venue, pages, publisher DOI, final citation, and license notice | High for publication metadata |
| E5 | [ACL paper PDF](https://aclanthology.org/2025.findings-emnlp.165.pdf) | Near-primary final-publication locator and citation cross-check | Medium-high; not collected or redistributed |
| E6 | [Xinli Xu publication page](https://xxu068.github.io/) and [Xiaojie Xu publication page](https://xjxu21.github.io/) | Author publication context; no PreGenie-specific code link found on inspected pages | Medium for availability boundary |
| E7 | [VLM Probing DEP](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md) | Limits of visual-language diagnostics and non-causal evaluator signals | Medium; related context only |
| E8 | [Evidence-Gated Agents DEP](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260730-Evidence-Gated%20Agents/evidence-gated-agents.md) and [Kimi K2.5 Visual Agentic DEP](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260727-Kimi%20K2%205%20Visual%20Agentic/kimi_k2_5_visual_agentic_manuscript.md) | Evidence-bound agent loops and multimodal agent evaluation patterns | Medium; related context only |

## Related DEP Entries

Exactly three related Black Lake entries were selected after inspecting their public Markdown artifacts:

1. [Evidence-Gated Agents](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260730-Evidence-Gated%20Agents/evidence-gated-agents.md) — repository-relative path `.lake-data/DEP-E/DEP-E-20260730-Evidence-Gated Agents/evidence-gated-agents.md`. Relevance: its evidence-gate synthesis maps directly to PreGenie's separation of fast generation from slower code and rendered-page adjudication. Source basis: the entry's cross-source sections on evidence boundaries, slow/fast validation, multimodal evaluation, and reviewer escalation.
2. [Kimi K2.5 Visual Agentic](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260727-Kimi%20K2%205%20Visual%20Agentic/kimi_k2_5_visual_agentic_manuscript.md) — repository-relative path `.lake-data/DEP-E/DEP-E-20260727-Kimi K2 5 Visual Agentic/kimi_k2_5_visual_agentic_manuscript.md`. Relevance: it provides a nearby multimodal-agent design and evaluation frame for visual perception, tool use, and agentic workflows. Source basis: the entry's method, evaluation, limitation, and evidence-extraction sections.
3. [VLM Probing](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md) — repository-relative path `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`. Relevance: it cautions that visual-language signals are diagnostic and correlational, which is directly relevant to treating a Page Reviewer score as a review signal rather than proof of slide quality. Source basis: the entry's probe results, leakage warnings, and recommended causal/behavioral cross-checks.

## Synthesis Note

### Concept Bridge

PreGenie can be understood as a render-and-review evidence loop: language models create an editable intermediate artifact, a code reviewer checks structural and semantic constraints, a renderer exposes the observable page state, and a vision-language reviewer feeds bounded corrections back to the generator. The three related DEP entries extend that bridge from presentation generation to general evidence-gated agents, multimodal agent evaluation, and evaluator skepticism. The common research question is not whether a model can generate plausible content, but whether a system can expose, test, and correct the gap between intent, intermediate artifact, and observed output.

### Potential Implementations

1. **Evidence-bound brief-to-slide pipeline:** convert an approved public brief into Slidev Markdown, retain claim-to-source links, run code and page checks, and require human approval before export.
2. **Visual regression gate for generated decks:** render a fixed synthetic/public benchmark, compare page geometry and text-image correspondence across versions, and route outliers to a reviewer instead of silently accepting them.
3. **Existing-deck repair workbench:** parse a deck or PDF into content and image notes, regenerate only selected pages, and preserve a before/after evidence card for every change.

### Deeper Relationship Observations

1. The paper's code/page split is a concrete instance of the evidence-gated pattern: a cheap symbolic check catches syntax and content failures, while a slower visual check catches failures that only appear after rendering.
2. Page review resembles transition verification: the system must assess the state produced by an action, not merely the action text or source code that requested it.
3. The paper's human-preference claim makes evaluator governance central. The VLM Probing entry's leakage and non-causality warnings imply that visual scores need calibration, counterfactual tests, and abstention paths.

### Conceptual Similarities

1. All four artifacts treat intermediate representations as inspectable evidence rather than disposable prompts.
2. All four use specialized roles or probes to separate perception, generation, validation, and interpretation.
3. All four warn that an aggregate score can hide a failure mode, so downstream systems need decomposed metrics and explicit limits.

### MVP Implementations with Code Mock-ups

1. **Bounded Slidev code gate**

   ```python
   def code_gate(markdown: str) -> dict:
       """Toy structural gate; it does not call a model or render content."""
       errors = []
       if not markdown.strip():
           errors.append("empty deck")
       if markdown.count("---") < 2:
           errors.append("missing slide separators")
       if "<script" in markdown.lower():
           errors.append("unexpected script tag")
       return {"passed": not errors, "errors": errors}
   ```

2. **Rendered-page review record**

   ```python
   def page_review(page_id: str, checks: dict) -> dict:
       """Store bounded findings for human review; no automatic export."""
       failures = [name for name, passed in checks.items() if not passed]
       return {
           "page_id": page_id,
           "status": "needs_review" if failures else "pass",
           "failed_checks": failures,
       }
   ```

3. **Claim-to-slide evidence card**

   ```python
   def evidence_card(slide_id: str, claims: list[str], sources: list[str]) -> dict:
       """Create an auditable, public-safe mapping without copying source files."""
       return {
           "slide_id": slide_id,
           "claim_count": len(claims),
           "source_urls": list(dict.fromkeys(sources)),
           "human_approval_required": True,
       }
   ```

### Developer Challenges

1. Define stable, model-independent checks for overflow, unreadable density, image relevance, and cross-slide consistency without reducing design to one brittle threshold.
2. Control latency and API cost when the visual reviewer is the slowest stage, while preserving reproducible prompts, model versions, and retry limits.
3. Prevent content drift during regeneration by preserving source claims, slide-level diffs, and human approval boundaries.

### Author Challenges

1. Report exact human and GPT-4o score tables, rater agreement, confidence intervals, and per-category variance so the preference claim is auditable.
2. Expand evaluation beyond image-rich DOC2PPT samples to charts, multilingual content, accessibility constraints, long documents, and adversarial layout cases.
3. Release a versioned paper implementation or detailed reproducibility package that identifies prompts, rendering environment, model endpoints, and evaluation assets.

## Validation Notes

- Manuscript contract: required YAML fields and headings are present; YAML title and H1 match and remain below 40 characters.
- Exact-three checks: three related DEP entries, three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP/code mock-ups, three developer challenges, and three author challenges.
- Source gate: complete PDF and full-paper HTML were verified before review; metadata/provenance/verification records were updated locally; the optional source package was unavailable.
- Public safety: generated files contain public URLs and repository-relative paths only. No PDF, HTML, metadata page, source archive, cache, extracted text, local path, or source attachment is included.

## Attribution Block

- Source URL: https://arxiv.org/abs/2505.21660
  - Applies to: Report-Mark.md
  - Notes: Canonical arXiv identity, authors, version history, abstract, and public paper locators.
- Source URL: https://arxiv.org/html/2505.21660
  - Applies to: Report-Mark.md
  - Notes: Full-paper method, experiments, limitations, and conclusion evidence; source file withheld locally.
- Source URL: https://aclanthology.org/2025.findings-emnlp.165/
  - Applies to: Report-Mark.md
  - Notes: Final publication metadata, pages, DOI, and venue record.
- Source URL: https://xxu068.github.io/
  - Applies to: Report-Mark.md
  - Notes: Author publication context and code-link availability check.
- Source URL: https://xjxu21.github.io/
  - Applies to: Report-Mark.md
  - Notes: Author publication context and code-link availability check.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260730-Evidence-Gated%20Agents/evidence-gated-agents.md
  - Applies to: Synthesis Note
  - Notes: Related Black Lake evidence-gating synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260727-Kimi%20K2%205%20Visual%20Agentic/kimi_k2_5_visual_agentic_manuscript.md
  - Applies to: Synthesis Note
  - Notes: Related Black Lake multimodal-agent synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md
  - Applies to: Synthesis Note
  - Notes: Related Black Lake evaluator and VLM-probing synthesis.
