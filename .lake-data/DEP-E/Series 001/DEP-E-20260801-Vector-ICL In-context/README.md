# DEP-E-20260801-Vector-ICL In-context

#vector-icl #continuous #in-context #research-review

Public-safe context: job `BLAD-2200-20260801-A1ED7FC9`, item `BLAD-2200-20260801-A1ED7FC9-P09`, uniformly selected `arXiv:2410.05629`. The archive unit reached a verified complete PDF-plus-full-paper-HTML state before review after one bounded local archive repair. Local paths, exact execution times, source documents, datasets, and executable research artifacts are withheld.

## Contents

- `README.md` - context, inventory, source boundary, synthesis, and attribution.
- `vector_icl_in_context_manuscript.md` - schema-complete paper review, evidence ledger, limitations, and bounded implementation paths.

No `.source/` exists. No PDF, HTML, source archive, cache, extracted source text, dataset, model, credential, or executable artifact is deposited.

## Summary of Items

The paper studies whether an LLM can perform in-context learning directly over continuous representations. Vector-ICL aligns encoder outputs to the LLM embedding space with lightweight projectors trained by next-token prediction, then supplies projected vectors as context. In the inspected Table 2, finetuned Vector-ICL reports 98.16 on SST-2, 97.28 on IMDb, 85.20 on Emotion, and summarization scores of 20.08 on XSum and 20.49 on XLSum; these remain author-reported until independently reproduced.

## Insights and Relevance

The three related DEPs connect this work to CogEvo-Edu - DEP-E, RAPL Relation-Aware - DEP-E, and SANE Embeddings - DEP-E. Shared concepts include classification, learning, representations, vector. The practical synthesis is to preserve provenance, compare against strong baselines, test sensitivity and distribution shift, and use abstention plus human review when evidence is incomplete.

## Attribution Block

- https://arxiv.org/abs/2410.05629 - metadata and public source locators.
- https://arxiv.org/html/2410.05629 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2410.05629 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2410.05629 - durable DOI record.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260714-CogEvo%20Edu%20Agents - related DEP: CogEvo-Edu - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260714-CogEvo Edu Agents/cogevo_edu_agents_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260728-RAPL%20Relation-Aware - related DEP: RAPL Relation-Aware - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260728-RAPL Relation-Aware/rapl_relation_aware_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-SANE%20Embeddings - related DEP: SANE Embeddings - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, integrity companions, and extraction caches; all withheld locally with zero source-document uploads.
