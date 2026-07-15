# Report-Mark: Document Fraud LLM

## Report Scope

This public-safe Report-Mark records the 2026-07-15 source-first review of *Can Multi-modal (reasoning) LLMs detect document manipulation?* (arXiv:2508.11021v1). It preserves source identity, selection and dedup evidence, source-integrity repair, research findings, exactly three related DEP entries, implementation synthesis, validation, and attribution. Original paper files, extraction caches, local paths, and exact execution times are withheld.

## Source Metadata

| Field | Value |
|---|---|
| Title | *Can Multi-modal (reasoning) LLMs detect document manipulation?* |
| Authors | Zisheng Liang; Kidus Zewde; Rudra Pratap Singh; Disha Patil; Zexi Chen; Jiayu Xue; Yao Yao; Yifei Chen; Qinzhe Liu; Simiao Ren |
| Identifier | arXiv:2508.11021v1 |
| DOI | 10.48550/arXiv.2508.11021 |
| Submitted | 2025-08-14 |
| Subjects | Computer Vision and Pattern Recognition; Computation and Language |
| Primary record | https://arxiv.org/abs/2508.11021 |
| Full paper | https://arxiv.org/html/2508.11021; https://arxiv.org/pdf/2508.11021 |
| Source package | https://arxiv.org/e-print/2508.11021 |
| License shown by full text | CC BY-NC-ND 4.0 |
| Venue/code status | arXiv preprint; no separate publisher venue or official code repository found in the inspected record |
| Lineage notice | The arXiv record carries an administrator note for text overlap with arXiv:2503.20084. This report makes no inference about misconduct or intent. |

## Selection, Deduplication, and Integrity

- `Enumeration`: `rg --files -g "*.pdf"`; each unique PDF parent directory was one paper unit.
- `Candidate count`: 75,776.
- `Random method`: uniform PowerShell `Get-Random` over zero-based indices.
- `Selected index`: 2,983.
- `Dedup scopes`: `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and relevant Black-Lake-Data search results.
- `Dedup keys`: arXiv ID, DOI, normalized title, slug, and preceding-24-hour marker.
- `Outcome`: first draw accepted; duplicate exclusions 0; reselections 0.
- `Initial source state`: partial. A valid complete PDF existed; full-paper HTML and companion integrity records were missing.
- `Repair`: preserved the PDF; collected official full-paper HTML, abstract/metadata HTML, and source package; refreshed README, attribution, CSV summary, and verification JSON.
- `Final source state`: complete. PDF size/header/EOF passed; HTML size/body/document/heading/structure passed; source package present; zero partial files.
- `Extraction`: PDF, HTML, and TeX/source text succeeded. `pypdf` was the available PDF extractor.
- `No-source-upload gate`: passed. No PDF, HTML, metadata page, source archive, extracted source text, cache, integrity file, or local path appears in the public artifacts.

## Concise Research Notes

### Problem

The study asks whether state-of-the-art multimodal models can distinguish forged from authentic receipt images without task-specific training. The motivating hypothesis is complementary capability: traditional forensic models detect compression or pixel artifacts, while multimodal LLMs can read text, recompute totals, compare merchant fields, reason about dates, and notice layout inconsistencies.

### Method

The traditional baselines are a flattened-pixel SVM and CNN methods based on OH-JPEG/OH-JPEG+PQL features. The LLM pipeline supplies each image with a structured receipt-fraud prompt and requests JSON containing a continuous fraud score, evidence, and uncertainty. String processing recovers the number. ROC AUC is the main comparison metric because the data are imbalanced.

The benchmark naming is inconsistent: the paper uses “FindIt Again,” “find-it-2,” and RDDFD, while Table 1 describes 1,000 retail receipts and the cited reference is *Receipt dataset for document forgery detection*. A replication requires an exact manifest, not a name match.

### Results

Table 3 reports GPT-O1 at AUC 0.71, Gemini-2.5-Pro-Think at 0.63, Llama-4 at 0.60, Gemini-2.5-Flash-Think at 0.59, and Claude-3.7 at 0.57. Qwen2.5-VL, Pixtral, Deepseek, GPT-4o, Claude-3-Haiku, SVM, and the image-level CNN are around chance. The reasoning comparison reports Gemini Flash 0.55 without thinking versus 0.59 with thinking, and Gemini Pro 0.51 versus 0.63.

GPT-O1 is analyzed on a named set of 218 images, but the paper reports 192 scored outcomes: 161 correct and 31 wrong, comprising two false positives and 29 false negatives. Its nominal accuracy is 83.85%, yet the error composition shows poor fraud recall. Scores for both correct pristine cases and missed forged cases cluster at low values. A few predictions exceed 0.8, including the two false positives.

### Evidence Boundary

The paper explicitly omits model outputs when numerical recovery fails, the model refuses, or no usable reply arrives. It does not report the missing count per model. Missingness may therefore be informative rather than random. The work also lacks repeated seeds, confidence intervals, significance tests, fixed prompt-selection protocol, complete calibration metrics, code/configuration release, multi-dataset validation, and explanation-faithfulness tests.

The source supports the statement that GPT-O1 provided the best reported ranking signal and that thinking helped two Gemini comparisons. It does not support automatic fraud adjudication or a general claim that reasoning models reliably detect document manipulation.

## Evidence and Attribution Notes

| Evidence | Inspected basis | Supported conclusion | Limitation |
|---|---|---|---|
| Paper identity and version | arXiv metadata and DOI | Correct title, authors, date, ID, subjects, and lineage note | Metadata alone is not empirical evidence |
| Method and prompt | Full-paper HTML, PDF, and TeX/source | SVM/CNN/LLM design and common prompt | Code and model-call configuration are incomplete |
| Comparative table | Paper Table 3 | AUC ranking under reported retained outputs | Unknown per-model denominator and no uncertainty |
| Reasoning comparison | Paper Table 4 | Within-family Gemini uplift | One family and no repeated calls/statistical test |
| Error/calibration analysis | GPT-O1 section and histogram discussion | 161/192, 2 FP, 29 FN, low-score overlap | 218-versus-192 discrepancy not reconciled |
| Omission policy | Evaluation section | Parser/refusal/failure outputs are dropped | Missingness bias cannot be quantified |
| Lineage context | Selected arXiv note and arXiv:2503.20084 metadata | Explicit change-map review is needed | No misconduct or exact overlap extent inferred |
| Integrity/process | Private local verification summarized here | Complete source and reproducible selection record | Local records withheld by policy |

## Exactly Three Related DEP Entries

1. [`VLM Probing`](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md) — repository path `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`; primary basis arXiv:2005.07310v2. It contributes architecture-aware probes, random-weight controls, mismatch tests, attention caveats, and the principle that aggregate downstream performance is not sufficient evidence about internal multimodal behavior.
2. [`PAC Confidence`](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md) — repository path `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`; primary basis arXiv:2011.00716v5. It contributes support-aware intervals, simultaneous coverage, decision budgets, and an explicit on-distribution envelope for deciding when a score can safely trigger anything beyond review.
3. [`RLMF Uncertainty`](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-RLMF%20Uncertainty/rlmf_uncertainty_manuscript.md) — repository path `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md`; primary basis arXiv:2606.32032v1. It contributes a careful separation between expressed confidence, sampled-consistency proxies, factual correctness, support, linguistic uncertainty, and user reliance.

## Synthesis Note

### Concept Bridge

The selected paper provides an application benchmark: a multimodal model reads a receipt, assigns a fraud probability, and explains its decision. The three related entries turn this benchmark into a system design. VLM Probing asks whether the model's internal representations actually encode cross-modal alignment, relations, and modality-specific information. PAC Confidence asks whether the observed calibration data support a decision threshold with enough finite-sample evidence and within a declared distribution envelope. RLMF Uncertainty asks what the score or hedge means and whether it aligns with correctness, a sampled-consistency proxy, or merely a learned communication style.

The bridge is therefore `representation evidence -> task evidence -> confidence evidence -> supervised action`. None of these layers can replace another. A strong probe does not prove fraud detection; a strong AUC does not define a safe threshold; a calibrated phrase does not prove factual correctness; and a human-reviewed action still needs privacy and appeal controls.

### Potential Implementations

1. `Receipt Evidence Gate`: combine low-level manipulation features, multimodal semantic checks, a fixed-denominator failure registry, support-aware confidence intervals, shift detection, and human adjudication. The output is a review packet, not an automated fraud verdict.
2. `VLM Forensics Probe Suite`: use synthetic receipt edits to test text-region alignment, arithmetic sensitivity, merchant-field consistency, and counterfactual rationale faithfulness across model families and layers where accessible.
3. `Confidence-and-Coverage Release Card`: publish per-model denominators, refusals, parser failures, AUC intervals, calibration curves, support counts, risk-coverage, shift status, and approved action boundaries for every release.

### Deeper Relationship Observations

1. The 218-versus-192 denominator gap is not a clerical detail; it links the selected paper to PAC Confidence because interval validity and decision budgets depend on knowing which outcomes entered the sample and why others did not.
2. GPT-O1's fluent arithmetic and merchant explanations link to VLM Probing because explanation quality is not evidence of causal visual grounding; controlled region and mismatch probes are needed to distinguish genuine multimodal dependence from language priors.
3. The histogram's low scores for both true and missed forged cases link to RLMF Uncertainty because “confidence” conflates fraud probability, correctness confidence, sampled consistency, and communication style; the channels must be separately logged and evaluated.

### Conceptual Similarities

1. All four artifacts treat a scalar model output as incomplete evidence and add structure around it: internal probes, interval support, uncertainty semantics, or failure telemetry.
2. All four distinguish source-reported performance from the conditions under which a downstream decision is justified.
3. All four imply a fail-visible design: mismatches, unsupported bins, proxy disagreement, refusals, and parser failures should remain observable rather than being averaged away.

### MVP Implementations with Code Mock-ups

1. `Terminal-Status Registry` — dependency-free Python mock-up that makes every request count exactly once:

```python
from dataclasses import dataclass

TERMINAL = {"scored", "refused", "timeout", "invalid_json", "parse_failed"}

@dataclass(frozen=True)
class Outcome:
    request_id: str
    status: str
    fraud_score: float | None = None

def validate(outcome: Outcome) -> Outcome:
    if outcome.status not in TERMINAL:
        raise ValueError("non-terminal or unknown status")
    if outcome.status == "scored" and outcome.fraud_score is None:
        raise ValueError("scored outcome requires a score")
    if outcome.status != "scored" and outcome.fraud_score is not None:
        raise ValueError("failure outcome must not masquerade as scored")
    return outcome
```

2. `Support-Aware Review Gate` — illustrative logic that never accepts a point score without an interval and distribution check:

```python
def route(lower: float, upper: float, support: int, shifted: bool) -> str:
    if shifted or support < 30:
        return "review"
    if lower >= 0.90:
        return "high-risk-review"
    if upper <= 0.10:
        return "low-risk-review"
    return "review"

assert route(0.92, 0.97, 80, False) == "high-risk-review"
assert route(0.01, 0.08, 80, True) == "review"
```

3. `Counterfactual Rationale Probe` — synthetic-region mock-up that checks whether a cited feature changes the score:

```python
def rationale_delta(score_fn, image, cited_region, replace_region):
    baseline = score_fn(image)
    edited = replace_region(image, cited_region)
    return baseline - score_fn(edited)

def supported(delta: float, minimum_effect: float = 0.05) -> bool:
    return abs(delta) >= minimum_effect

# A production test would compare cited regions with random control regions
# and would never treat this one probe as proof of causal explanation.
```

### Developer Challenges

1. Build an immutable request/result schema that reconciles every input across asynchronous model APIs, timeouts, retries, malformed outputs, and parser versions without storing sensitive receipt contents in public telemetry.
2. Calibrate heterogeneous evidence channels whose scores have different meanings, missingness patterns, model-update cadences, and shift sensitivities while retaining channel-level auditability.
3. Create a synthetic-to-real evaluation harness that exercises pixel edits, OCR errors, arithmetic contradictions, privacy redaction, counterfactual probes, and reviewer workflows without leaking customer documents.

### Author Challenges

1. Publish a pinned dataset/split manifest and reconcile “FindIt Again,” “find-it-2,” RDDFD, 218 named images, and 192 scored GPT-O1 outcomes.
2. Release per-model terminal-status counts, model/API/decoding versions, prompt-selection protocol, parsing code, raw predictions, repeated-call uncertainty, and calibration metrics.
3. Provide a respectful paper-lineage change map against arXiv:2503.20084 covering reused and new data, prompts, models, analyses, figures, text, authorship, and claims.

## Validation Notes

- Live `Delphoa/Black-Lake` and `Delphoa-Labs/Black-Lake-Data` READMEs were fetched and read before drafting.
- The manuscript skill and its full artifact schema were read before generation.
- The source-integrity gate passed before synthesis; abstract-only evidence was not used as the paper.
- The selected paper's full PDF, full-paper HTML, metadata HTML, source package, method, results, conclusion, prompt appendix, tables, and reference context were inspected.
- Exactly three related DEP entries were inspected and recorded with repository paths, public GitHub URLs, relevance, and primary source bases.
- This Synthesis Note contains exactly three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP implementations with code mock-ups, three developer challenges, and three author challenges.
- The DEP short description `Document Fraud LLM` is 18 characters, within the 25-character limit.
- The manuscript YAML title and H1 are identical and under 40 characters.
- Public-safe scanning excludes local paths, drive letters, usernames, machine names, local timezone labels, exact local execution timestamps, and source-document content.
- Submission staging is restricted to generated Markdown under `.logs`, `.reports`, and `.lake-data`; no `.source/` directory or source document is permitted.

## Attribution Block

- Source URL: https://arxiv.org/abs/2508.11021
  - Applies to: source metadata, identity, submission history, DOI, subjects, license locator, and administrator note.
  - Notes: Abstract/metadata page; not treated as the full paper.
- Source URL: https://arxiv.org/html/2508.11021
  - Applies to: method, result tables, error analysis, conclusion, and appendix prompt.
  - Notes: Official full-paper HTML; verified local copy withheld.
- Source URL: https://arxiv.org/pdf/2508.11021
  - Applies to: full-paper pagination, figures, tables, and public PDF identity.
  - Notes: Verified source file retained locally and not redistributed.
- Source URL: https://arxiv.org/e-print/2508.11021
  - Applies to: source-level method, table, prompt, and reference cross-checks.
  - Notes: Source package retained locally and not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2508.11021
  - Applies to: persistent identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://creativecommons.org/licenses/by-nc-nd/4.0/
  - Applies to: license record and source-withholding decision.
  - Notes: Original source files were not uploaded.
- Source URL: https://arxiv.org/abs/2503.20084
  - Applies to: lineage context named by the selected arXiv record.
  - Notes: No inference about misconduct, intent, or exact overlap.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md
  - Applies to: representation-probing bridge.
  - Notes: Related processed DEP; primary basis arXiv:2005.07310v2.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md
  - Applies to: support-aware confidence and decision-gate bridge.
  - Notes: Related processed DEP; primary basis arXiv:2011.00716v5.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-RLMF%20Uncertainty/rlmf_uncertainty_manuscript.md
  - Applies to: uncertainty-semantics and proxy-governance bridge.
  - Notes: Related processed DEP; primary basis arXiv:2606.32032v1.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: repository standards and source-locality policy.
  - Notes: Live authority read before drafting.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: DEP class, path, and publication-index rules.
  - Notes: Live authority read before drafting.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: companion-repository provenance and dedup context.
  - Notes: Live authority read before drafting.
