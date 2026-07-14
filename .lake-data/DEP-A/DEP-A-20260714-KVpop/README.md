# DEP-A-20260714-KVpop

#arxiv #kv-cache #online-pruning #long-context #qwen3 #model-finetuning #language-model-inference #machine-learning

This DEP-A entry preserves a public-safe, whitepaper-grade full-paper review of **“KVpop — Key-Value Cache Compression with Predictive Online Pruning,” arXiv:2607.05061v2**. The review reconstructs predictive retention scoring, training and inference behavior, long-context evaluation, official checkpoint artifacts, numerical inconsistencies, and an independent deployment interpretation. A complete PDF and full-paper HTML were verified from a local archive; source documents remain local and are withheld from this repository.

Deposition date: 2026-07-14  
Stable paper version: arXiv:2607.05061v2

## Contents

- `README.md` — deposition context, complete inventory, relationships, and attribution.
- `2607.05061-whitepaper-review.md` — validated public-safe full-paper review and independent re-conceptualization.

## Summary of Items

### `README.md`

Defines the stable record, inventories both files, identifies the official model release and baseline checkpoint, summarizes the paper’s key consistency defect, and records complete attribution.

### `2607.05061-whitepaper-review.md`

Reconstructs predictive online KV pruning, audits the two-billion-token full-model fine-tuning recipe, cross-checks reported retention/accuracy numbers, inspects public checkpoint configuration, and proposes serving and reliability tests. The validator passed the canonical review at 3,886 words.

## Insights and Relevance

KVpop is unusually concrete because an official self-contained Qwen3-8B release is publicly available, including custom model/cache code and weights. That improves inspectability, but it also clarifies that KVpop is not a scorer-only retrofit: the reported recipe fine-tunes all parameters on two billion tokens. The paper needs a correction because the abstract/Table 1, introduction, and conclusion report incompatible percentage pairs, and the released checkpoint’s 40,960-position configuration needs reconciliation with the paper’s evaluation beyond 131,000 tokens.

## Associated DEP Records

No same-paper or directly corresponding DEP-A, DEP-E, or relevant Delphoa-Labs/Black-Lake-Data record was verified after checking class indexes, DEP READMEs, logs, reports, arXiv ID, DOI, normalized title, method, benchmark, and implementation.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.05061
- Canonical PDF: https://arxiv.org/pdf/2607.05061
- Canonical full-paper HTML: https://arxiv.org/html/2607.05061
- DOI: https://doi.org/10.48550/arXiv.2607.05061
- Official model/code release: https://huggingface.co/sirluk/Qwen3-8B-KVpop-4x
- DMS comparison checkpoint: https://huggingface.co/nvidia/Qwen3-8B-DMS-8x
- Authors from the canonical arXiv record:
  - Lukas Hauzenberger — https://arxiv.org/search/cs?query=Hauzenberger%2C+L&searchtype=author
  - Niklas Schmidinger — https://arxiv.org/search/cs?query=Schmidinger%2C+N&searchtype=author
  - Anamaria-Roberta Hartl — https://arxiv.org/search/cs?query=Hartl%2C+A-R&searchtype=author
  - David Stap — https://arxiv.org/search/cs?query=Stap%2C+D&searchtype=author
  - Thomas Schmied — https://arxiv.org/search/cs?query=Schmied%2C+T&searchtype=author
  - Sebastian Böck — https://arxiv.org/search/cs?query=Boeck%2C+S&searchtype=author
  - Günter Klambauer — https://arxiv.org/search/cs?query=Klambauer%2C+G&searchtype=author
  - Sepp Hochreiter — https://arxiv.org/search/cs?query=Hochreiter%2C+S&searchtype=author
- Applies to: `README.md` and `2607.05061-whitepaper-review.md`.
- Verification note: complete source documents were verified locally and withheld from this repository.
