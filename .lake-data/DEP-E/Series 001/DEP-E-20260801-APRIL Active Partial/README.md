# DEP-E-20260801-APRIL Active Partial

#april #learning #long-tail #research-review

Public-safe context: job `BLAD-2200-20260801-A1ED7FC9`, item `BLAD-2200-20260801-A1ED7FC9-P10`, uniformly selected `arXiv:2509.18521`. The archive unit reached a verified complete PDF-plus-full-paper-HTML state before review after one bounded local archive repair. Local paths, exact execution times, source documents, datasets, and executable research artifacts are withheld.

## Contents

- `README.md` - context, inventory, source boundary, synthesis, and attribution.
- `april_active_partial_manuscript.md` - schema-complete paper review, evidence ledger, limitations, and bounded implementation paths.

No `.source/` exists. No PDF, HTML, source archive, cache, extracted source text, dataset, model, credential, or executable artifact is deposited.

## Summary of Items

The paper addresses long-tail rollout latency in LLM reinforcement learning. APRIL over-provisions rollout requests, stops once the target batch size is reached, and resumes incomplete responses in later steps instead of discarding them. Across GRPO and DAPO experiments, the abstract reports 22.5% average rollout-throughput improvement, faster convergence, and 2.1% higher final accuracy on average; these results remain author-reported until independently reproduced.

## Insights and Relevance

The three related DEPs connect this work to AR-Drag Motion Control - DEP-E, Semantic Skill MoE Policies, and RLMF Uncertainty - DEP-E. Shared concepts include active, generation, learning, long-tail, partial, reinforcement, rollout, rollouts. The practical synthesis is to preserve provenance, compare against strong baselines, test sensitivity and distribution shift, and use abstention plus human review when evidence is incomplete.

## Attribution Block

- https://arxiv.org/abs/2509.18521 - metadata and public source locators.
- https://arxiv.org/html/2509.18521 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2509.18521 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2509.18521 - durable DOI record.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-AR-Drag%20Motion - related DEP: AR-Drag Motion Control - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260719-Semantic%20Skill%20MoE - related DEP: Semantic Skill MoE Policies; source basis `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/semantic_skill_moe_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260714-RLMF%20Uncertainty - related DEP: RLMF Uncertainty - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, integrity companions, and extraction caches; all withheld locally with zero source-document uploads.
