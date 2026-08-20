---
title: "How to Forget Clients in Federated Online Learning to Rank?"
artifact_type: "DEP-E research deposit"
primary_subject: "Federated online learning-to-rank unlearning"
source_id: "arXiv:2401.13410v1"
public_date: "2026-08-04"
source_status: "complete local PDF and full-paper HTML verified; source files withheld locally"
---

# How to Forget Clients in Federated Online Learning to Rank?

Tags: `#arxiv` `#federated-learning` `#unlearning` `#learning-to-rank` `#privacy` `#online-learning`

This public-safe DEP-E deposit reviews a source-verified paper on removing a client's contribution from a federated online ranker without full retraining. It preserves evidence links, implementation boundaries, and follow-on research questions. The source PDF, full-paper HTML, metadata, extracted text, and verification records remain local and are not part of this repository.

## Contents

- [Schema-complete manuscript](forget_foltr_manuscript.md)
- [Report-Mark](../../../../.reports/BL-Arxiv-How-to-Forget-FOLTR-20260804/Report-Mark.md)
- [Job log](../../../../.logs/20260804-Arxiv-How-to-Forget-FOLTR-LOG.md)

## Summary of Items

- `forget_foltr_manuscript.md`: source metadata, evidence ledger, detailed research summary, limitations, implementation ideas, and source references.
- `Report-Mark`: concise evidence/attribution record plus exactly three implementation, relationship, similarity, developer-challenge, and author-challenge items.
- The local source unit passed the PDF and full-paper HTML integrity gate after one bounded repair. The optional source archive was unavailable through the brokered request and was not needed for this review.

## Insights and Relevance

The paper makes historical update state the bridge between privacy requests and efficient learning-system maintenance. Retained update intervals can reduce retraining work, but they also create storage, leakage, staleness, and audit obligations. The most useful implementation direction is a synthetic, replayable benchmark that measures deletion-reference quality together with update storage, local computation, communication, and verification cost.

The work is directly relevant to federated ranking, model governance, privacy engineering, and Black-Lake's broader interest in auditable state transitions. Its verification setup is best treated as a research signal, not a universal deletion proof: the authors themselves qualify how well the target-client distinction generalizes.

## Attribution Block

Primary source: Shuyi Wang, Bing Liu, and Guido Zuccon, “How to Forget Clients in Federated Online Learning to Rank?”, [arXiv:2401.13410v1](https://arxiv.org/abs/2401.13410), [arXiv DOI](https://doi.org/10.48550/arXiv.2401.13410), published in ECIR 2024 with publisher DOI [10.1007/978-3-031-56063-7_7](https://doi.org/10.1007/978-3-031-56063-7_7). Full-paper HTML: [arxiv.org/html/2401.13410](https://arxiv.org/html/2401.13410). Official results repository: [ielab/2024-ECIR-foltr-unlearning](https://github.com/ielab/2024-ECIR-foltr-unlearning). Related DEP entries are linked in the manuscript and Report-Mark. Source files were withheld locally; no source files were uploaded to Black-Lake or Slack.
