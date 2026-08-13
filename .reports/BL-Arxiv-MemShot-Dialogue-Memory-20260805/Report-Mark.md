# Report-Mark: MemShot Dialogue Memory

## Source Metadata

| Field | Value |
|---|---|
| Title | Memory Shot for Long-Term Dialogue |
| Authors | Chunyi Peng; Haidong Xin; Xuanshuo Sheng; Xin Dai; Zhenghao Liu; Shuo Wang; Yukun Yan; Zulong Chen; Yu Gu; Ge Yu |
| Identifier | arXiv:2606.28338v1 |
| Paper date | 2026-05-30, submitted date on the canonical arXiv record |
| DOI | [10.48550/arXiv.2606.28338](https://doi.org/10.48550/arXiv.2606.28338) |
| Primary record | https://arxiv.org/abs/2606.28338 |
| Full paper | https://arxiv.org/html/2606.28338 |
| PDF | https://arxiv.org/pdf/2606.28338 |
| Official implementation | https://github.com/NEUIR/MemShot, README fetched at commit `af01f8b20fbc8bddcad34b73725b4989d9424ec4` |
| Venue context | The inspected PDF carries an ACM-style placeholder header; publication or acceptance status was not independently established |
| Source integrity | Initial partial local unit repaired to verified complete PDF and full-paper HTML before review |
| Source distribution | Source files, extracted text, caches, and private verification records withheld locally |

## Research Notes

MemShot addresses long-term dialogue memory as a representation problem. Existing memory systems commonly rewrite, compress, integrate, and retrieve text-centered units. The paper argues that these operations can be expensive and can weaken speaker transitions, turn boundaries, timestamps, and local adjacency. MemShot instead renders contiguous dialogue spans into structured visual memory shots and lets a multimodal language model retrieve and reason over those shots.

The method has three essential steps. First, a dialogue is split into temporally localized chunks. Second, each chunk is organized into a hierarchical template with a header containing session metadata and a chat region preserving speaker-aware turn order. Third, the template is rendered as an image. The paper's default implementation fixes image width at 948 pixels and target height at 768 pixels, packs complete turn-pairs, and overlaps adjacent shots by up to two turn-pairs when space allows. Retrieval uses Qwen3-VL-Embedding-8B and generation uses Qwen3-VL-Instruct at 2B, 8B, or 32B scales.

The source reports competitive results on LoCoMo and LongMemEval. On LoCoMo with Qwen3-VL-8B, MemShot reports 75.13 overall accuracy/F1 of 56.46, compared with Text RAG at 70.39/53.28; with Qwen3-VL-32B it reports 79.61/58.43 versus Text RAG at 77.34/55.69. On LongMemEval with Qwen3-VL-8B, MemShot reports 66.00/50.91 versus Text RAG at 60.60/46.33; with Qwen3-VL-32B it reports 74.80/55.53 versus Text RAG at 72.40/51.89. The additional Qwen3-VL-2B table reports 45.60/38.24 for MemShot. These numbers are author-reported and were not reproduced.

The most useful ablation evidence is structural. Removing rendering while retaining equivalent text content reduces LoCoMo performance; removing the header weakens the benefit of adding more retrieved units; and fixed-height 768-pixel rendering outperforms 512-pixel, 1024-pixel, and full-session alternatives in the reported Qwen3-VL-8B comparison. The paper also reports about a 5% retrieval gain at top-10 and more than 2% better generation conditioned on correctly retrieved units, plus a 70x memory-construction speedup relative to heavier text-memory baselines. The speed claim should be read as a paper-reported construction comparison, not as an end-to-end serving guarantee.

The official repository confirms a runnable-shaped, script-based pipeline with rendering, retrieval, inference, and LLM-judge stages. Its README warns that model, data, cache, and output paths are hard-coded in scripts; its dependency file pins CUDA-oriented packages including PyTorch, Transformers, vLLM, FAISS, Pillow, and NumPy. The code was inspected but not executed.

## Evidence and Attribution

| Evidence ID | Source | Evidence used | Assessment |
|---|---|---|---|
| E1 | https://arxiv.org/abs/2606.28338 | Title, authors, arXiv version, date, abstract, DOI, HTML/PDF/source links | High for identity and author framing; abstract is insufficient for detailed empirical claims |
| E2 | https://arxiv.org/html/2606.28338 | Introduction, methodology, equations, benchmark setup, Tables 1-5, retrieval analysis, saliency analysis, case studies, conclusion, and appendices | High for transcription of inspected paper content; no independent reproduction |
| E3 | https://arxiv.org/pdf/2606.28338 | Printed tables, figures, implementation details, metrics, and paper header | High for reported paper evidence; extracted text contains encoding noise |
| E4 | https://doi.org/10.48550/arXiv.2606.28338 | Persistent arXiv-issued DOI locator | High for stable identity; not a separate publisher validation |
| E5 | https://github.com/NEUIR/MemShot | Official README, requirements, rendering implementation, and retrieval launcher; README SHA `af01f8b20fbc8bddcad34b73725b4989d9424ec4` | Medium to high for implementation inventory; code, checkpoints, and datasets were not run |
| E6 | Private local extraction cache | `pypdf` PDF text and `html-regex` full-paper text produced after the complete-source gate | High for processing provenance; private cache is not redistributed |
| E7 | `.lake-data/DEP-A/DEP-A-20260714-C-DIC Dialogue Memory/2606.12411-whitepaper-review.md` | Revisable latent states, retrieval-aware write-back, closed-loop evaluation, storage-growth caveats | Medium for related synthesis; distinct paper and method |
| E8 | `.lake-data/DEP-A/DEP-A-20260714-MemRouter/2605.00356-whitepaper-review.md` | Separation of write admission from retrieval and answer generation, latency and budget analysis | Medium for related synthesis; distinct paper and method |
| E9 | `.lake-data/DEP-A/DEP-A-20260714-Agent Memory Forensics/agent-memory-forensics-intake-review.md` | Memory provenance, observable traces, defensive detection, and evidence boundaries | Medium for safety and governance synthesis; review artifact rather than direct validation |

## Related DEP Entries

1. [C-DIC Dialogue Memory](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-C-DIC%20Dialogue%20Memory/2606.12411-whitepaper-review.md) - overlaps long-term dialogue memory construction and retrieval, but represents memory as revisable latent thread states rather than rendered visual shots. Source basis: the reviewed DEP's architecture, closed-loop, storage-growth, and LongMemEval sections.
2. [MemRouter](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-MemRouter/2605.00356-whitepaper-review.md) - overlaps memory-system decomposition and efficiency, especially the separation of write admission, retrieval, and answer generation. Source basis: the reviewed DEP's matched-harness, storage-policy, and latency analysis.
3. [Agent Memory Forensics](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-Agent%20Memory%20Forensics/agent-memory-forensics-intake-review.md) - overlaps memory governance, provenance, telemetry, and defensive failure localization. Source basis: the reviewed DEP's evidence model, privacy-minimized trace design, and operational-boundary sections.

## Synthesis Note

### Concept Bridge

MemShot's central bridge is from dialogue history to a structured, retrievable scene representation. It preserves enough local order and metadata for a multimodal model to reason over evidence without repeatedly rewriting the history. In Black Lake terms, this connects the memory object's physical representation, the retrieval policy, and the answer-generation evidence boundary. The bridge is a reviewer synthesis: the related DEPs are conceptual neighbors, not interchangeable implementations or independent validation of MemShot.

### Potential Implementations

1. `Structure-preserving dialogue memory`: A local-only service renders synthetic or authorized dialogue into timestamped, speaker-aware memory shots, stores the source-to-shot map, and returns top-k shots with provenance. It should support deletion, re-rendering, and abstention when layout or metadata is incomplete.
2. `Privacy-aware memory gateway`: A governed gateway adds retention labels, user-visible memory controls, consent and deletion receipts, contradiction flags, and access logs around a visual-memory index. The multimodal model receives only authorized shots and their provenance labels.
3. `Memory representation benchmark`: A benchmark harness compares text chunks, rendered shots, latent summaries, and learned admission policies under the same retriever, answer model, prompt, judge, context budget, seeds, and concurrency. It reports retrieval, answer correctness, evidence grounding, latency, storage, and privacy failures separately.

### Deeper Relationship Observations

1. MemShot moves complexity from write-time language generation into a representation-and-serving layer. The claimed speedup is therefore a systems trade: cheaper construction can produce larger image stores, multimodal indexing costs, and new privacy or accessibility obligations.
2. The three related DEPs expose complementary control points. C-DIC revises latent state, MemRouter controls admission, and Agent Memory Forensics constrains observable traces. MemShot primarily changes the stored unit, so its downstream reliability still depends on independent read and governance policies.
3. Preserving structure is not the same as preserving truth. A rendered shot can retain an incorrect, stale, or sensitive utterance with high fidelity. Structure-aware memory therefore needs contradiction handling, source authority, deletion semantics, and uncertainty labels in addition to better retrieval.

### Conceptual Similarities

1. MemShot and C-DIC both treat long-term memory as an explicit external state that mediates between dialogue history and generation rather than assuming the raw context window is sufficient.
2. MemShot and MemRouter both separate memory representation or write policy from answer generation, making it possible to compare admission, retrieval, and response quality as distinct stages.
3. MemShot and Agent Memory Forensics both make operational evidence important: the former preserves speaker/time/turn structure for reasoning, while the latter preserves action/trace structure for defensive audit. Neither evidence form guarantees semantic correctness without governance.

### MVP Implementations

1. `Synthetic shot renderer` - bounded renderer and provenance map for safe local experiments.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Turn:
    speaker: str
    text: str
    turn_id: int

def make_shots(turns, session_id, timestamp, turns_per_shot=4):
    if turns_per_shot < 1:
        raise ValueError("turns_per_shot must be positive")
    shots = []
    for offset in range(0, len(turns), turns_per_shot):
        chunk = tuple(turns[offset:offset + turns_per_shot])
        shots.append({
            "header": {"session_id": session_id, "timestamp": timestamp},
            "turns": [turn.__dict__ for turn in chunk],
            "source_turn_ids": [turn.turn_id for turn in chunk],
        })
    return shots
```

2. `Provenance-aware retrieval ledger` - deterministic retrieval stub that refuses unlabelled or deleted memory units.

```python
def retrieve(query_terms, shots, top_k=3):
    allowed = [shot for shot in shots
               if shot.get("status", "active") == "active"
               and shot.get("authority", "unknown") != "blocked"]
    def score(shot):
        words = " ".join(turn["text"] for turn in shot["turns"]).lower()
        return sum(term.lower() in words for term in query_terms)
    ranked = sorted(allowed, key=score, reverse=True)
    return [{"shot": shot, "score": score(shot)} for shot in ranked[:top_k]]
```

3. `Memory-evidence evaluation gate` - a safe audit record for comparing representations without calling a model.

```python
def evaluate_memory_record(record):
    required = {"source_turn_ids", "retriever", "model_version", "deletion_state"}
    missing = sorted(required - record.keys())
    if missing or record.get("deletion_state") != "active":
        return {"status": "abstain", "missing": missing or ["active-memory-required"]}
    return {"status": "review", "evidence_ids": list(record["source_turn_ids"])}
```

### Developer Challenges

1. Reproducing the image rendering, Qwen3-VL embedding/generation, vLLM serving, benchmark conversion, and GLM-5 judging stack with the pinned dependencies, checkpoints, data, and paths.
2. Separating the causal contributions of visual layout, header metadata, overlap, chunk height, retriever, prompt, judge, and model scale under matched compute and repeated seeds.
3. Adding lifecycle controls for deletion, correction, contradiction, sensitive content, accessibility, multilingual rendering, image integrity, and storage/index cost without breaking evidence traceability.

### Author Challenges

1. Release a complete reproduction manifest with model and dataset versions, render outputs or hashes, environment lock, hardware, seeds, prompts, raw predictions, and metric-calculation scripts.
2. Report end-to-end cost and latency, including rendering, image storage, indexing, retrieval, multimodal prefill, concurrency, cache behavior, and failure recovery rather than construction latency alone.
3. Extend evaluation to memory lifecycle and safety properties: user deletion, edits, contradictions, authority labels, privacy leakage, OCR/layout failures, accessibility, multilingual dialogue, calibrated abstention, and independent judges.

## Validation Notes

- The source-integrity gate passed before synthesis: valid PDF and full-paper HTML; abstract HTML was treated as metadata only.
- The cache contract passed: `cached` public summary, local PDF and HTML text, `pypdf` fallback for unavailable `pdftotext`, and no source-text output.
- The live `Delphoa/Black-Lake` and `Delphoa-Labs/Black-Lake-Data` READMEs were fetched before writing.
- Exactly three related DEP entries were selected from repository content and each has a concrete overlap reason and source basis.
- The manuscript uses identical YAML `title` and H1 values no longer than 40 characters, all required schema headings, exactly three exercise paths, and explicit random-selection, cache, and dedup/reselection records.
- Public-output review must confirm only generated Markdown, the publication-index row, and the derived dedup JSON are staged. PDFs, HTML, source archives, extracted text, cache files, local paths, and source records must remain unstaged and local.
- No source files were uploaded or attached; no `.source/` directory was created.

## Attribution Block

- Source URL: https://arxiv.org/abs/2606.28338
  - Applies to: this Report-Mark and the related DEP manuscript.
  - Notes: Canonical public metadata, authorship, version, abstract, and public source locators.
- Source URL: https://arxiv.org/html/2606.28338
  - Applies to: this Report-Mark and the related DEP manuscript.
  - Notes: Full-paper method, benchmark, ablation, retrieval, analysis, and conclusion evidence.
- Source URL: https://arxiv.org/pdf/2606.28338
  - Applies to: this Report-Mark and the related DEP manuscript.
  - Notes: Printed tables, figures, implementation details, and paper-header evidence.
- Source URL: https://doi.org/10.48550/arXiv.2606.28338
  - Applies to: source identity fields.
  - Notes: ArXiv-issued DOI locator.
- Source URL: https://github.com/NEUIR/MemShot
  - Applies to: official implementation inventory and reproduction boundary.
  - Notes: README, requirements, rendering script, and retrieval launcher inspected; no code was executed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: repository layout, DEP class, attribution, and public-source policy.
  - Notes: Live repository authority fetched before writing.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related raw-data repository context and source-file policy.
  - Notes: Live related-repository authority fetched before writing.
