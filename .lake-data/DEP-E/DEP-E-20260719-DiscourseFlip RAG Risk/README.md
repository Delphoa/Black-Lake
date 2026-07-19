# DEP-E-20260719-DiscourseFlip RAG Risk

#rag-security #retrieval-poisoning #opinion-manipulation #provenance #defense-in-depth #semantic-graphs #responsible-ai

Public-safe deposition context: `Black Lake Arxiv DEP 2200 x10` job `BLAD-2200-20260719-7D93E819`, item `BLAD-2200-20260719-7D93E819-P02`, uniformly selected and source-first reviewed arXiv:2606.01212v2 on 2026-07-19. The archive unit was repaired from partial to verified complete before synthesis. Local source locations, exact execution times, and all source files are withheld.

## Contents

- `README.md` - inventory, context, summary, defensive safety boundary, source policy, and attribution.
- `discourseflip_rag_risk_manuscript.md` - schema-complete research manuscript covering the paper's threat model, evidence, user study, defense findings, limitations, defensive implementation paths, selection/dedup process, integrity gate, and related DEP synthesis.

No `.source/` directory is present. The paper PDF, full-paper HTML, metadata HTML, source package, extracted text, and processing cache remain local and were not deposited.

## Summary of Items

`discourseflip_rag_risk_manuscript.md` reviews a black-box RAG threat in which opinion manipulation is distributed across a semantic query network rather than aimed only at one query or protected root topic. It records the 40-topic, 5,843-query experimental setting; reported cross-model and cross-retriever results; an 81-participant study; and mitigation tests spanning input, corpus, retrieval, top-k content, and generation.

Because the source is dual-use, the deposit preserves mechanism-level risk and aggregate evidence without reproducing attack prompts, optimized poisoned text, executable procedures, or payload-generation code. Every proposed implementation is defensive and intended for authorized offline evaluation. The artifact connects the paper to exactly three inspected entries: Self-Correcting RAG, Memory Defense Layers, and Agent Memory Forensics.

## Insights and Relevance

The reusable finding is structural: fluent documents can evade surface anomaly checks while their combined retrieval pattern produces network-level response drift. Root-topic neutralization and query paraphrasing are therefore incomplete when neighboring queries and source composition remain unobserved. A defensible stack joins provenance-aware corpus admission, source-independent evidence selection, semantic-neighborhood monitoring, contradiction checks, response-drift analysis, conservative generation, and incident traceability.

The paper does not establish universal RAG compromise. Its claims depend on write access, retrievability, graph construction, model-specific agents and classifiers, selected topics, and short-session human evaluation. Production conclusions require independent replication, domain-specific calibration, privacy review, and controls against suppressing legitimate minority evidence.

## Source and Distribution Policy

- Source state: verified complete after bounded local repair.
- Source documents: withheld locally.
- Public deposit: generated Markdown plus required repository indexes only.
- `.source/`: not created.
- Source uploads: zero.
- Safety boundary: no operational attack prompts, payloads, optimization logic, or deployment instructions.
- Deployment job ID: `BLAD-2200-20260719-7D93E819`.
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P02`.

## Attribution Block

- Source URL: https://arxiv.org/abs/2606.01212
  - Applies to: `discourseflip_rag_risk_manuscript.md` and this README.
  - Notes: Canonical metadata and abstract page; metadata only, not the full paper.
- Source URL: https://arxiv.org/html/2606.01212
  - Applies to: `discourseflip_rag_risk_manuscript.md`.
  - Notes: Official full-paper HTML inspected locally; source file withheld.
- Source URL: https://arxiv.org/pdf/2606.01212
  - Applies to: `discourseflip_rag_risk_manuscript.md`.
  - Notes: Verified PDF inspected locally; source file withheld.
- Source URL: https://arxiv.org/e-print/2606.01212
  - Applies to: `discourseflip_rag_risk_manuscript.md`.
  - Notes: Official source package used for tables, equations, and appendix cross-checks; source file withheld.
- Source URL: https://doi.org/10.48550/arXiv.2606.01212
  - Applies to: persistent paper identity in both files.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-A/DEP-A-20260715-Self-Correcting%20RAG
  - Applies to: related evidence-portfolio and contradiction-checking analysis.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260718-Memory%20Defense%20Layers
  - Applies to: related architectural defense and provenance analysis.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260711-Agent%20Memory%20Forensics
  - Applies to: related graph/trajectory detection analysis.
- Source files: verified paper PDF, full-paper HTML, metadata HTML, source package, extracted text, and processing cache.
  - Applies to: source-first review and integrity validation.
  - Notes: All source files were withheld locally; zero source documents were uploaded. Deployment context is job `BLAD-2200-20260719-7D93E819`, item `BLAD-2200-20260719-7D93E819-P02`.
