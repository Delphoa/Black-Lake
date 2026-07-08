# Black Lake Arxiv DEP Log: SANE Embeddings

Public run date: 2026-07-09
Automation: Black Lake Arxiv DEP
Outcome: selected, reviewed, and deposited one arXiv archive paper.

## Selection

- Selected paper: Scalable attribute-aware network embedding with locality
- Identifier: arXiv:1804.07152
- Public source: https://arxiv.org/abs/1804.07152
- Sanitized provenance: local archive readme and PDF presence observed; local paths withheld.
- Random method: uniform random index over `rg --files -g "*.pdf"` output.
- Candidate count: 64,626 PDFs.
- Selected index: 24,529, zero-based.
- Candidate unit: PDF parent directory plus adjacent readme metadata.

## Eligibility

- Dedup scan locations: `Black-Lake/.logs`, `Black-Lake/.reports`, `Black-Lake/.lake-data`, repository README, automation memory, and related Black-Lake-Data context.
- Duplicate/reselection count: 0.
- Excluded count: 0.
- 24-hour cutoff: public-safe cutoff date 2026-07-08; no same-paper marker found.
- Validation: no prior Arxiv DEP log, Report-Mark, or DEP-E manuscript for arXiv:1804.07152 was found in inspected targets.

## Related DEP Entries

1. `Black-Lake-Data/.lake-data/DEP-20260630-Tech Intel 0104/daily_research_findings_2026-06-30_0104.md` - related graph topology inference and network observability.
2. `Black-Lake-Data/.lake-data/DEP-20260708-Tech Intel 1104/daily_research_findings_2026-07-08_1104.md` - related structured-vector-graph memory and ability-graph concepts.
3. `Black-Lake-Data/.lake-data/DEP-20260629-Study Fork Topics/study_fork_related_topics_2026-06-29_2346.md` - related embedding, vector database, GraphRAG, and dependency-graph retrieval topics.

## Outputs

- Report-Mark: `.reports/BL-Arxiv-SANE-20260709/Report-Mark.md`
- DEP-E: `.lake-data/DEP-E-20260709-SANE Embeddings`
- Manuscript: `.lake-data/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md`
- Source files collected: none; public arXiv URLs and source-withheld notes are used instead.

## Validation Notes

- Live `Black-Lake/README.md` and live `Black-Lake-Data/README.md` were inspected before artifact generation.
- arXiv metadata, arXiv source package TeX files, and selected local archive metadata were inspected.
- Local absolute paths, user home names, machine names, local timezone labels, and exact local execution timestamps were intentionally withheld.

## Questions for Next Reviewer

1. Should the next pass re-run SANE on one public attributed graph to verify the reported F1 and scalability behavior?
2. Which graph-memory DEP should become the first source-thread graph benchmark for Black-Lake?
3. Should future Arxiv DEP runs preserve arXiv source package file inventories when redistribution is not allowed?

## Challenges for Next Review Pass

1. Validate whether the SANE implementation or datasets remain available through public or author-controlled channels.
2. Compare SANE's locality alignment against a modern graph neural network baseline on the same attributed-node task.
3. Define a DEP relation-graph schema that can represent topology edges, attributes, and evidence provenance without leaking local archive details.
