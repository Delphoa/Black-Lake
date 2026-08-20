# DEP-E-20260820-GenPT Psychometrics

#arxiv #llm #psychometrics #agent-evaluation #safety

Deposition date: 2026-08-20.

This public-safe DEP-E records a source-grounded review of GenPT, a projective-testing framework for evaluating persona-conditioned LLM agents. The verified PDF and full-paper HTML were inspected locally, but all original source files remain withheld under the local archive. No `.source/` directory is included.

## Contents

- `README.md` — public-safe DEP inventory, summary, relevance, and attribution.
- `genpt_psychometrics_manuscript.md` — schema-complete manuscript research artifact with source metadata, evidence ledger, limitations, implementation paths, and validation notes.

## Summary of Items

- **`genpt_psychometrics_manuscript.md`**: Reviews the GenPT Examinee → Interpreter → Diagnostician pipeline, its TAT/Rorschach/SCT stimuli, reported reliability and validity results, official implementation context, and non-clinical safety boundary.
- **Source boundary**: Local PDF, full-paper HTML, metadata HTML, provenance, receipts, and verification artifacts were used for source-first review and are not public DEP contents.

## Insights and Relevance

GenPT is most useful as a measurement-design pattern for simulated agents, not as a clinical instrument. Its reported results suggest that indirect behavioral probes can reduce some questionnaire-style framing drift, while personality validity and context responsiveness remain backbone-dependent. The related Black Lake work on state traces, reliability gates, and benchmark uncertainty points toward a safer downstream design: preserve intermediate behavior and scoring evidence, measure perturbation response, calibrate or abstain, and keep all outputs in offline research review rather than person-level decision systems.

## Attribution Block

- Source URL: https://arxiv.org/abs/2606.00860
  - Applies to: paper identity, authors, abstract, version, and public locator.
- Source URL: https://arxiv.org/html/2606.00860
  - Applies to: full-paper method, experiments, results, limitations, ethics, and appendices.
- Source URL: https://aclanthology.org/2026.acl-long.1901/
  - Applies to: ACL publication context, version 2, venue, pages, and DOI.
- Source URL: https://github.com/sci-m-wang/GenPT
  - Applies to: official code, stimuli, repository layout, and implementation availability.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: public DEP filing and source-locality rules.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: companion provenance and source-deposition rules.
- Source files: none deposited; original source files remain withheld locally.
