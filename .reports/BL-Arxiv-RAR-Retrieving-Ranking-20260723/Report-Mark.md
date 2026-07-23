# Report-Mark: RAR Retrieving and Ranking

## Source Metadata

| Field | Value |
|---|---|
| Paper | *RAR: Retrieving And Ranking Augmented MLLMs for Visual Recognition* |
| Authors | Ziyu Liu; Zeyi Sun; Yuhang Zang; Wei Li; Pan Zhang; Xiaoyi Dong; Yuanjun Xiong; Dahua Lin; Jiaqi Wang |
| Canonical record | [arXiv:2403.13805v2](https://arxiv.org/abs/2403.13805v2) |
| arXiv DOI | [10.48550/arXiv.2403.13805](https://doi.org/10.48550/arXiv.2403.13805) |
| Publisher DOI | [10.1109/TIP.2025.3644175](https://doi.org/10.1109/TIP.2025.3644175) |
| Dates | Submitted 2024-03-20; revised 2026-05-15 |
| Official code | [Liuziyu77/RAR](https://github.com/Liuziyu77/RAR) |
| Review date | 2026-07-23; exact local execution time withheld |
| Source state | Complete and verified after bounded local repair; source files withheld locally and not uploaded |

## Concise Research Notes

**Problem.** Frozen vision-language encoders are efficient retrieval and classification tools, but similarity alone can confuse visually close categories. General MLLMs can reason over images and descriptions, yet they are expensive and unreliable when asked to search an unconstrained ontology.

**Method.** RAR separates recall from discrimination. Frozen CLIP encoders query an external image/text memory, HNSW can accelerate approximate nearest-neighbor lookup, and the resulting top-k category names are presented to an MLLM for comparative reranking. In detection, the method acts on object proposals/crops and can blur background context. The default candidate count is five.

**Reported evidence.** On the 11-dataset 4-shot benchmark, CLIP+KNN averages 57.0 and RAR with LLaVA-1.5 averages 63.2. With CLIP ViT-L/14@336, 4-shot performance rises from 65.0 to 69.9 and 8-shot from 70.8 to 75.5. On LVIS with ground-truth proposals, cropped-box CLIP reports 48.7 AP and RAR reports 56.2–57.1 AP. V3Det gains are smaller: 9.8 AP becomes 10.8–11.3.

**Boundary evidence.** In the 4-shot table, Flowers-102 falls from 84.5 to 80.4 after reranking. With Detic proposals on LVIS, absolute AP falls to 13.4 for CLIP and 19.2 for RAR, compared with 48.7 and 56.2 under ground-truth boxes. HNSW's accuracy effect also varies by dataset. These results constrain any blanket claim that reranking reliably corrects retrieval.

**Reviewer interpretation.** RAR is most valuable as a modular cascade whose stages can be measured independently. Retrieval top-k recall is a hard ceiling, and region proposal recall is an earlier ceiling in detection. A production derivative should expose abstention, validate that outputs belong to the candidate set, version every memory and model surface, and report proposal recall, top-k recall, conditional reranker accuracy, and end-to-end accuracy separately.

## Evidence and Attribution

| Evidence | Source location | Assessment |
|---|---|---|
| Frozen CLIP retrieval followed by MLLM candidate reranking | Abstract, method, and architecture figure in the [full paper](https://arxiv.org/html/2403.13805v2) | Direct source claim; high confidence. |
| Default `k=5`, with the reported four-dataset average peaking at 85.19 | Candidate-count ablation | Direct numeric claim; local optimum only. |
| 4-shot average 57.0 to 63.2 | Few-shot Table III | Direct numeric claim; aggregate across 11 datasets. |
| Flowers-102 84.5 to 80.4 | Few-shot Table III | Direct negative evidence; high confidence. |
| LVIS 48.7 to 56.2–57.1 AP with ground-truth proposals | Detection Table VII and visually checked PDF page | Direct numeric claim; oracle proposal context must remain attached. |
| V3Det 9.8 to 10.8–11.3 AP with ground-truth proposals | Detection Table VIII and visually checked PDF page | Direct numeric claim; smaller gain than LVIS. |
| LVIS with Detic proposals: 13.4 to 19.2 AP | Proposal ablation | Direct boundary evidence; proposal quality dominates absolute results. |
| HNSW lowers lookup time in the tested comparison | Efficiency ablation | Supported in the tested setup; not a universal scale/accuracy guarantee. |
| Candidate recall bounds reranking success | Method structure | Reviewer deduction with high confidence. |
| Need for output constraints, provenance, privacy review, and stage telemetry | Gaps identified against deployment needs | Reviewer recommendation, not an author-validated feature. |

The PDF, full-paper HTML, metadata HTML, source archive, extracted-text cache, provenance record, and verification report were used only in the private source-first workflow. They remain withheld locally. Public links in this report identify the evidence without redistributing local source artifacts.

## Related DEP Entries

1. **MemReranker Reasoning Aware** — `.lake-data/DEP-A/DEP-A-20260715-MemReranker Reasoning Awa/2605.06132-whitepaper-review.md`. Source basis: the inspected whitepaper review describes dense retrieval followed by fine-grained reasoning-aware reranking. Relevance: both systems inherit a candidate-recall ceiling and must balance second-stage quality against latency and calibration.
2. **MIRA One Touch** — `.lake-data/DEP-E/DEP-E-20260719-MIRA One Touch/mira_one_touch_manuscript.md`. Source basis: the inspected manuscript reviews multimodal similarity retrieval from a finite template library followed by constrained action generation. Relevance: both architectures use a bounded candidate layer to make a higher-level multimodal decision safer and more tractable.
3. **VLM Probing** — `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`. Source basis: the inspected manuscript reviews internal vision-language fusion and the limits of interpreting probes/attention. Relevance: it provides methods and cautions for studying whether RAR corrections arise from visual evidence, label semantics, or prompt structure.

## Synthesis Note

### Concept Bridge

RAR, MemReranker, MIRA, and VLM probing can be placed on one mechanistic map. RAR and MemReranker are explicit cascades: broad retrieval creates a candidate set and a richer second stage resolves close alternatives. MIRA uses the same shape in an action domain, retrieving a template before constrained generation. VLM probing adds an analysis layer that asks which visual and linguistic representations the second stage actually uses. Across all four, the intermediate candidate representation is the control point: it bounds search, enables attribution, and makes upstream recall separable from downstream reasoning.

The bridge also exposes a common failure law. A second-stage model can reorder or reject candidates, but cannot reliably recover information removed by proposal generation or retrieval. Better reasoning therefore does not eliminate the need for recall audits. Conversely, widening the candidate set can improve recall while increasing ambiguity, latency, and prompt load. The useful design question is not “retriever or reasoner?” but how to allocate error, compute, and governance across the interface between them.

### Potential Implementations

1. **Versioned visual-candidate API:** Serve CLIP/HNSW candidates with score margins, memory provenance, and embedding versions; send only ambiguous requests to a constrained MLLM that must select a candidate or abstain.
2. **Proposal-aware detector verifier:** Couple each region proposal with proposal confidence and top-k label recall estimates. Allow the MLLM to rerank labels but prevent it from masking low proposal coverage; route uncertain regions to human review.
3. **Cross-domain reranking observatory:** Compare RAR-style visual reranking, MemReranker-style document reranking, and MIRA-style template selection using shared metrics for candidate coverage, conditional correctness, correction rate, regression rate, latency, and calibration.

### Deeper Relationship Observations

1. **The candidate set is an information bottleneck and a safety boundary.** RAR uses it to bound visual labels; MIRA uses it to bound action templates; MemReranker uses it to bound evidence. The same interface that limits recovery also enables output validation and auditability.
2. **Reasoning gains are conditional, not absolute.** RAR's reranker only operates on retrieved labels, while VLM probing warns that apparent attention or probe associations do not automatically establish causal use. A correction should be attributed to second-stage reasoning only after controlling candidate coverage and prompt effects.
3. **Upstream quality can dominate downstream sophistication.** RAR's Detic ablation demonstrates proposal dependence directly. The analogous risks are missing documents in a memory reranker and missing templates in MIRA. In each case, second-stage improvements can coexist with poor end-to-end performance.

### Conceptual Similarities

1. **Two-speed computation:** Each related design spends cheap computation broadly and expensive computation narrowly.
2. **Externalized memory or catalog:** Labels, documents, or templates live outside the reasoning model and can be updated independently, creating both modularity and provenance obligations.
3. **Measurable stage boundary:** Candidate coverage and conditional selection accuracy can be evaluated separately, enabling better error attribution than one blended end-to-end score.

### MVP Implementations with Code Mock-Ups

1. **Constrained candidate gate.** This mock-up keeps the output inside the retrieved label set and abstains when retrieval evidence is too flat. The reranker scores are placeholders for an MLLM adapter.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Decision:
    label: str | None
    candidates: tuple[str, ...]
    reason: str


def decide(retrieval_scores: dict[str, float], reranker_scores: dict[str, float]) -> Decision:
    ranked = sorted(retrieval_scores.items(), key=lambda item: item[1], reverse=True)[:5]
    candidates = tuple(label for label, _ in ranked)
    if len(ranked) < 2 or ranked[0][1] - ranked[1][1] < 0.01:
        return Decision(None, candidates, "abstain: weak retrieval margin")
    allowed_scores = {label: reranker_scores[label] for label in candidates}
    label = max(allowed_scores, key=allowed_scores.get)
    return Decision(label, candidates, "candidate-constrained rerank")
```

2. **Top-k ceiling audit.** This evaluator separates candidate coverage from conditional reranker correctness, preventing an end-to-end average from hiding retrieval misses.

```python
def audit(samples: list[dict], k_values: tuple[int, ...] = (1, 3, 5, 7)) -> list[dict]:
    rows = []
    for k in k_values:
        covered = 0
        correct_when_covered = 0
        for sample in samples:
            candidates = sample["retrieved"][:k]
            has_truth = sample["truth"] in candidates
            covered += int(has_truth)
            correct_when_covered += int(has_truth and sample["reranked"][0] == sample["truth"])
        conditional = correct_when_covered / covered if covered else 0.0
        rows.append({"k": k, "coverage": covered / len(samples), "conditional": conditional})
    return rows
```

3. **Provenance-aware memory record.** This minimal record prevents embeddings from becoming anonymous vectors and supports later deletion, re-embedding, or license review.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class MemoryItem:
    item_id: str
    label: str
    source_uri: str
    license_id: str
    consent_basis: str
    embedding_model: str
    embedding_version: str
    active: bool = True


def compatible(item: MemoryItem, required_version: str) -> bool:
    return item.active and item.embedding_version == required_version
```

### Developer Challenges

1. **Reproducible interfaces:** Image crops, preprocessing, embedding versions, index parameters, prompt templates, and MLLM versions must be frozen together; otherwise a result cannot be attributed to one component.
2. **Constrained, calibrated outputs:** MLLMs may answer outside the candidate set or change behavior across prompts. Developers need schema enforcement, abstention, calibration data, retries with bounded budgets, and deterministic fallbacks.
3. **Stage-aware observability:** Proposal misses, retrieval misses, reranker regressions, index drift, and memory corruption appear similar in end-to-end metrics. Instrumentation must preserve the full candidate trace without leaking protected source data.

### Author Challenges

1. **Separating oracle and deployable evidence:** Ground-truth proposals clarify the label-ranking contribution but can be misread as full detector performance. Authors should foreground realistic proposal results and report proposal recall explicitly.
2. **Reporting distributional regressions:** Aggregate gains should be accompanied by class- and dataset-level correction/regression matrices, confidence intervals, and significance tests so negative transfer is visible.
3. **Completing the operational evidence:** Reproducible prompts, checkpoint hashes, seeds, index parameters, memory provenance, latency distributions, token/energy cost, and license/privacy analysis are needed for stronger deployment claims.

## Validation Notes

- **Random selection:** 75,780 PDFs mapped to 75,777 paper units. After 280 already-used exclusions and 185 identifier-incomplete withholds, `Get-Random` selected zero-based index 16,161 from 75,312 eligible units.
- **Deduplication:** The scan covered Black-Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and the corresponding Black-Lake-Data DEP surfaces. Final matching used arXiv ID, both DOI values, normalized title, and slug. Duplicate rejections/reselections: 0. Recent-marker cutoff: 2026-07-22.
- **Initial source state:** Partial because a valid PDF existed without verified full-paper HTML.
- **Repair:** A bounded acquisition preserved the PDF and obtained metadata HTML, official full-paper HTML, and source material. No partial bytes were accepted as progress.
- **PDF validation:** 5,314,877 bytes, `%PDF-` header, terminal `%%EOF`, 15 pages, unencrypted. Selected pages containing the architecture and result tables were rendered and visually inspected; text and tables were legible despite non-fatal local font warnings.
- **HTML validation:** 524,628 bytes, 89,851 stripped body characters, valid full-document marker, 40 heading markers, and multiple paper-structure terms.
- **Review boundary:** Public code and project context were inspected, but code and experiments were not executed. Reported results remain source claims rather than independent reproduction.
- **Related synthesis:** Exactly three related DEP entries were inspected and used; their relevance is stated in `## Related DEP Entries`.
- **Public-output gate:** The intended submission allowlist consists only of this generated report, the generated log, the DEP README, the manuscript, and the DEP-E publication index update.
- **Source-upload gate:** No PDF, HTML, source archive, extracted text, cache, local provenance record, or verification file belongs in the public commit. Source files were withheld locally.

## Attribution Block

| Source | Attribution | Use and boundary |
|---|---|---|
| [arXiv:2403.13805v2](https://arxiv.org/abs/2403.13805v2) | Ziyu Liu, Zeyi Sun, Yuhang Zang, Wei Li, Pan Zhang, Xiaoyi Dong, Yuanjun Xiong, Dahua Lin, and Jiaqi Wang | Canonical metadata, version history, abstract, subject classes, and public locator; accessed 2026-07-23. |
| [Full-paper arXiv HTML](https://arxiv.org/html/2403.13805v2) | Same authors | Method, experimental tables, ablations, conclusions, and reference evidence; verified local copy withheld. |
| [arXiv PDF](https://arxiv.org/pdf/2403.13805v2) | Same authors | Layout and visual table/figure verification; verified local copy withheld. |
| [arXiv DOI](https://doi.org/10.48550/arXiv.2403.13805) | DataCite/arXiv persistent record | Persistent identifier. |
| [IEEE DOI](https://doi.org/10.1109/TIP.2025.3644175) | IEEE Transactions on Image Processing | Journal-version locator and bibliographic context. |
| [Official RAR repository](https://github.com/Liuziyu77/RAR) | RAR authors | Usage and license context; inspected but not executed. |
| [Official project page](https://liuziyu77.github.io/RAR/) | RAR authors | Supporting author-maintained overview. |
| Local metadata HTML, full-paper HTML, PDF, source archive, extracted text, attribution record, and integrity reports | Original paper authors and locally generated verification metadata | Evidence only; all files withheld locally and none uploaded. |
| `.lake-data/DEP-A/DEP-A-20260715-MemReranker Reasoning Awa/2605.06132-whitepaper-review.md` | Delphoa/Black-Lake DEP-A artifact | Related retrieve-then-rerank synthesis; repository-relative citation. |
| `.lake-data/DEP-E/DEP-E-20260719-MIRA One Touch/mira_one_touch_manuscript.md` | Delphoa/Black-Lake DEP-E artifact | Related multimodal retrieval/constrained-generation synthesis; repository-relative citation. |
| `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` | Delphoa/Black-Lake DEP-E artifact | Related vision-language fusion/probing synthesis; repository-relative citation. |
