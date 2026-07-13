# DEP-A-20260714-ConMax Confidence

#arxiv #reasoning-models #chain-of-thought #reasoning-compression #reinforcement-learning #confidence-rewards #qwen #llm-efficiency #cold-storage

This cold-storage entry preserves a public-safe, whitepaper-grade archival intake review derived from the complete repository record `.lake-data/DEP-E/DEP-E-20260708-ConMax Reasoning` at source commit `e4dbe1a71bdef28ee7c38b7d6e8ecec707890b73` and a complete inspection of arXiv:2601.04973v1. The source DEP-E was reviewed in place. It was not reclassified or modified, and its files were neither moved nor copied into this DEP-A.

Public-safe review date: 2026-07-14  
Paired task indicator: `BL-DEPPAIR-20260714-24CD1ACC`  
Direction: `DEP-E -> DEP-A`  
DEP-A intake status: complete  
DEP-A deposition status: complete

## Contents

- `README.md` — entry classification, public-safe context, item inventory, provenance pair, associated records, and final attribution.
- `conmax-confidence-intake-review.md` — validated full-paper and complete-DEP review covering the ConMax pipeline, equations, experiments, results, ablations, claim calibration, external context, failure modes, hypotheses, and replication agenda.

## Summary of Items

### `README.md`

Defines the stable DEP-A scope, exact source path and commit, paired task indicator, publication identity, one-way review relationship, complete inventory, and public source attribution.

### `conmax-confidence-intake-review.md`

Reads both tracked source DEP-E files in full and reconstructs the complete 12-page ConMax paper, including five result tables, four figures, eight numbered equations, the appendix prompt, limitations, ethics statement, and references. It identifies ConMax as confidence-scored dataset distillation; audits the 20,000-question source pool, rejection sampling, roughly 9,000/6,500 data split, GRPO training, downstream SFT, benchmark metrics, and token-length semantics; compares primary records for ThinkPrune and L1; and preserves a Table 5 inconsistency rather than silently correcting it. No experiment was rerun.

## Insights and Relevance

The durable mechanism is to separate outcome sufficiency from representation plausibility and validate the compressed artifact on its consumer. ConMax’s reported Qwen2.5-7B result reduces average generated length from 8,603 to 4,906 tokens while average accuracy moves from 54.2 to 53.5. The review finds this trade-off credible within the tested setup but narrows broader claims: teacher likelihood is not proof of logical validity, the baseline set is limited, hardware and lifecycle cost are absent, and no official ConMax implementation was established. The review also records that Table 5 prints a 1.3-point loss for values whose arithmetic indicates 0.7.

## Provenance Pair

- Paired task indicator: `BL-DEPPAIR-20260714-24CD1ACC`
- Direction: `DEP-E -> DEP-A`
- Source DEP-E: `.lake-data/DEP-E/DEP-E-20260708-ConMax Reasoning`
- Source commit: `e4dbe1a71bdef28ee7c38b7d6e8ecec707890b73`
- Generated DEP-A: `.lake-data/DEP-A/DEP-A-20260714-ConMax Confidence`
- Source action: review-only.
- Source DEP modified: no.
- Files moved: no.
- Existing files copied into DEP-A: no.
- New derived data generated: yes.
- DEP-A intake status: complete after validation and repository submission.
- DEP-A deposition status: complete after validation and repository submission.

This paired record is one-way. It documents that the DEP-E was reviewed to generate new derived DEP-A data. It does not reclassify, transfer, supersede, or mutate the DEP-E.

## Associated DEP Records

- [Source DEP-E record](../../DEP-E/DEP-E-20260708-ConMax%20Reasoning/README.md) — complete repository record reviewed in place.
- [DEP-E publication index entry](../../DEP-E/.index/pubs-index.md) — existing class-level publication mapping for ConMax.

No other same-pair DEP-A was verified in the live review ledgers, existing DEP-A metadata, or repository history.

## Attribution Block

- Source repository URL: https://github.com/Delphoa/Black-Lake/tree/e4dbe1a71bdef28ee7c38b7d6e8ecec707890b73/.lake-data/DEP-E/DEP-E-20260708-ConMax%20Reasoning
  - Applies to: `conmax-confidence-intake-review.md`
  - Notes: Complete source DEP-E repository record reviewed in place at the exact source commit; source files were not modified, moved, copied, or uploaded.
- Source URL: https://arxiv.org/abs/2601.04973
  - Applies to: `conmax-confidence-intake-review.md`
  - Notes: Canonical metadata and abstract record for ConMax v1.
- Source URL: https://arxiv.org/pdf/2601.04973
  - Applies to: `conmax-confidence-intake-review.md`
  - Notes: Complete 12-page primary paper inspected for all text, equations, tables, figures, limitations, ethics, references, and appendix prompt; source document was not uploaded.
- Source URL: https://arxiv.org/html/2601.04973
  - Applies to: `conmax-confidence-intake-review.md`
  - Notes: Full-paper HTML used to cross-check section structure and machine-readable values.
- Source URL: https://doi.org/10.48550/arXiv.2601.04973
  - Applies to: `conmax-confidence-intake-review.md`
  - Notes: arXiv-issued DOI for the reviewed version.
- Source URL: https://arxiv.org/abs/2504.01296
  - Applies to: `conmax-confidence-intake-review.md`
  - Notes: Primary ThinkPrune record used for predecessor and alternative-mechanism context.
- Source URL: https://arxiv.org/abs/2503.04697
  - Applies to: `conmax-confidence-intake-review.md`
  - Notes: Primary L1 record used for controllable reasoning-length context.
- Source URL: https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k
  - Applies to: `conmax-confidence-intake-review.md`
  - Notes: Official dataset page for the source corpus named by the paper.
- Source URL: https://github.com/huggingface/Math-Verify
  - Applies to: `conmax-confidence-intake-review.md`
  - Notes: Official evaluator repository named by the paper; inspected at repository-documentation level and not executed.
- Generated review: `conmax-confidence-intake-review.md`
  - Applies to: this DEP-A entry.
  - Notes: New public-safe derived analysis written in original language. Repository data was reviewed in place; source documents were not uploaded.
