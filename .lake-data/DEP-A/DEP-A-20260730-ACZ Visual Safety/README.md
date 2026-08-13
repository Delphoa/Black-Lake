# DEP-A-20260730-ACZ Visual Safety

#artificial-intelligence #multimodal-safety #jailbreaks #visual-degradation #alignment #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.07250v1, *Hard to Read, Easy to Jailbreak: How Visual Degradation Bypasses MLLM Safety Alignment*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.07250-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.07250-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Figure 1: Illustration of visual degradation leading to jailbreaks. In summary, our contributions are as follows: We identify a novel security vulnerability where visual context compression and resolution degradation significantly increase the success rate of jailbreak attacks in SOTA MLLMs. To strictly quantify the decoupling between visual understanding and safety alignment, we introduce two concurrent normalized metrics for a given input x x : the OCR Score 𝒪 ​ 𝒞 ​ ℛ ​ ( x ) \mathcal{OCR}(x) and the Attack Success Rate 𝒜 ​ 𝒮 ​ ℛ ​ ( x ) \mathcal{ASR}(x) .To evaluate the model’s OCR performance at a given DPI, we employ two metrics with distinct granularities: Character-level OCR Accuracy and Word-level OCR Accuracy .

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat visual legibility and safety recognition as separate monitored channels: transcribe degraded text, audit the recovered semantics, and abstain whenever the two channels disagree beyond a calibrated threshold.

## Associated DEP Records

- [DEP-A-20260715-AnchorKV Safety](../DEP-A-20260715-AnchorKV%20Safety/README.md) - direct multimodal-context safety and cache-integrity context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.07250v1
  - Applies to: `2605.07250-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.07250v1
  - Applies to: `2605.07250-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.07250v1
  - Applies to: `2605.07250-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.07250
  - Applies to: `2605.07250-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/Westlake-AGI-Lab/ACZ-Jailbreak
  - Applies to: reproducibility context in `2605.07250-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Zhixue Song
  - arXiv author search: https://arxiv.org/search/?query=Zhixue%20Song&searchtype=author
  - Applies to: the reviewed paper and `2605.07250-whitepaper-review.md`.
- Author: Boyan Han
  - arXiv author search: https://arxiv.org/search/?query=Boyan%20Han&searchtype=author
  - Applies to: the reviewed paper and `2605.07250-whitepaper-review.md`.
- Author: Yiwei Wang
  - arXiv author search: https://arxiv.org/search/?query=Yiwei%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2605.07250-whitepaper-review.md`.
- Author: Chi Zhang
  - arXiv author search: https://arxiv.org/search/?query=Chi%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2605.07250-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
