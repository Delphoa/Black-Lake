# DEP-E-20260716-PIArena Evaluation

#prompt-injection #llm-security #benchmarking #adversarial-evaluation #agent-security #llm-as-a-judge

This public-safe DEP-E entry reviews PIArena as a unified prompt-injection evaluation platform and analyzes what its cross-task and adaptive-attack results mean for defensive engineering. Original paper documents, extraction caches, and derived source text remain local and were not deposited.

## Contents

- `README.md` - deposit inventory, context, summary, relevance, and source attribution.
- `piarena_evaluation_manuscript.md` - schema-complete source-grounded research manuscript.

## Summary of Items

- `README.md` establishes the scope and source-withholding policy for this research entry.
- `piarena_evaluation_manuscript.md` reconstructs the threat model, modular benchmark design, adaptive strategy attack, reported evidence, measurement limitations, implementation relevance, and three related Black Lake research connections.

## Insights and Relevance

PIArena's most useful contribution is a common test harness for comparing attacks, defenses, datasets, and evaluators without treating one benchmark as a robustness certificate. Its reported results show that static success can disappear under adaptive attacks or different tasks, while task-aligned disinformation falls outside ordinary instruction-detection assumptions. For Black Lake, the paper connects source-ingestion safety, agent trace observability, and evaluator uncertainty: secure pipelines need both diverse adversarial tests and evidence about how their metrics were produced.

## Attribution Block

- Source URL: https://arxiv.org/abs/2604.08499v1
  - Applies to: `piarena_evaluation_manuscript.md`
  - Notes: Canonical metadata, abstract, version, authors, subjects, comments, DOI, and license.
- Source URL: https://arxiv.org/pdf/2604.08499
  - Applies to: `piarena_evaluation_manuscript.md`
  - Notes: Complete paper inspected locally; file withheld.
- Source URL: https://arxiv.org/html/2604.08499
  - Applies to: `piarena_evaluation_manuscript.md`
  - Notes: Official full-paper HTML inspected locally; file withheld.
- Source URL: https://doi.org/10.48550/arXiv.2604.08499
  - Applies to: `piarena_evaluation_manuscript.md`
  - Notes: arXiv-issued DataCite DOI.
- Source URL: https://github.com/sleeepeer/PIArena
  - Applies to: `piarena_evaluation_manuscript.md`
  - Notes: Official MIT-licensed implementation and dataset/leaderboard links; inspected but not executed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260708-Tech%20Intel%20Review/tech-intel-agent-systems-review.md
  - Applies to: `piarena_evaluation_manuscript.md`
  - Notes: Related DEP evidence for distributed tool-description injection and agent evaluation.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Agent%20Memory%20Forensics/memory-forensics.md
  - Applies to: `piarena_evaluation_manuscript.md`
  - Notes: Related DEP evidence for compromise channels and trace observability.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Judge%20Conformal/llm_judge_conformal_manuscript.md
  - Applies to: `piarena_evaluation_manuscript.md`
  - Notes: Related DEP evidence for uncertainty-aware LLM judging.
