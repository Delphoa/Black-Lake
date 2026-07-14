# DEP-E-20260714-ComfyUI R1

#comfyui #workflow-generation #reasoning-models #reinforcement-learning #grpo #structured-generation #agent-systems #aigc

Public-safe context: This DEP-E reviews arXiv:2506.09790v1 after a local integrity repair established a verified full PDF and full-paper HTML. The selected paper now also has a later ACL Findings 2026 record. Original source files remain in the private archive and are not redistributed here.

## Contents

- `README.md`
  - DEP inventory, public-safe context, item summaries, relevance notes, and final source attribution.
- `comfyui_r1_manuscript.md`
  - Schema-complete manuscript reviewing ComfyUI-R1's knowledge-base construction, SFT-to-GRPO training, hybrid validity reward, experiments, limitations, implementation implications, random selection, deduplication, and source-integrity validation.

## Summary of Items

`README.md` records the DEP class, subject tags, source-withholding policy, complete two-file inventory, and canonical public locators.

`comfyui_r1_manuscript.md` is the durable research artifact. It distinguishes arXiv v1 evidence from the later publisher record, preserves reported metrics without implying independent reproduction, and relates ComfyUI-R1 to exactly three existing Black Lake deposits.

No `.source/` directory is included. The PDF, full-paper HTML, metadata HTML, TeX/source package, extracted text, and verification cache remain local. Public URLs provide provenance for the generated Markdown.

## Insights and Relevance

ComfyUI-R1 turns workflow generation into constrained program synthesis: retrieve a bounded node vocabulary, reason over a graph plan, emit a reversible code representation, and use hard validity gates before rewarding reference-node overlap. The strongest reported results are a 97% format-validity rate, node-level F1 of 0.62, graph-level F1 of 0.51 on the paper's test set, and a 0.67 ComfyBench execution pass rate. The design is relevant to agent systems beyond creative tooling because it separates probabilistic planning from executable structure and machine-checkable constraints. Its boundaries are equally important: most evaluation uses pre-retrieved candidate nodes, the community-derived knowledge base is not packaged for audit in the inspected sources, experiments were not reproduced, and the current integration repository does not provide a clearly pinned end-to-end ComfyUI-R1 release.

## Attribution Block

- Source URL: https://arxiv.org/abs/2506.09790
  - Applies to: `comfyui_r1_manuscript.md`
  - Notes: Canonical arXiv v1 metadata, authors, submission date, subjects, DOI, license link, and source locators.
- Source URL: https://arxiv.org/html/2506.09790
  - Applies to: `comfyui_r1_manuscript.md`
  - Notes: Verified full-paper HTML used for method, experiments, tables, ablations, implementation details, and conclusions.
- Source URL: https://arxiv.org/pdf/2506.09790
  - Applies to: `comfyui_r1_manuscript.md`
  - Notes: Canonical PDF locator; the verified local PDF was inspected but withheld from the repository.
- Source URL: https://doi.org/10.48550/arXiv.2506.09790
  - Applies to: `comfyui_r1_manuscript.md`
  - Notes: arXiv-issued DOI for the selected version.
- Source URL: https://aclanthology.org/2026.findings-acl.146/
  - Applies to: `comfyui_r1_manuscript.md`
  - Notes: Later Findings of ACL 2026 publication metadata, pages, DOI, and revision context.
- Source URL: https://doi.org/10.18653/v1/2026.findings-acl.146
  - Applies to: `comfyui_r1_manuscript.md`
  - Notes: Publisher DOI for the later ACL Findings record.
- Source URL: https://github.com/ATH-MaaS/ComfyUI-Copilot
  - Applies to: `comfyui_r1_manuscript.md`
  - Notes: Current destination of the paper-linked ComfyUI-Copilot integration repository; README and service notice inspected.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`; `comfyui_r1_manuscript.md`
  - Notes: Live repository layout, DEP class, source-withholding, attribution, and commit-message standard.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`; `comfyui_r1_manuscript.md`
  - Notes: Live DEP-E container, publication-index, and no-source-upload filing rules.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `comfyui_r1_manuscript.md`
  - Notes: Related repository contract inspected for cross-repository dedup and provenance context.
- Related repository entry: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260708-ConMax%20Reasoning
  - Applies to: `comfyui_r1_manuscript.md`
  - Notes: Related GRPO and reasoning-reward research deposit.
- Related repository entry: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-Structure%20Aware%20Systems
  - Applies to: `comfyui_r1_manuscript.md`
  - Notes: Related structure-preservation and verifiable mixed-workflow deposit.
- Related repository entry: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-SAILFISH%20Vetting
  - Applies to: `comfyui_r1_manuscript.md`
  - Notes: Related graph-first candidate reduction and precise validation deposit.
- Source policy: private local archive artifacts
  - Applies to: `comfyui_r1_manuscript.md`
  - Notes: Verified PDF, full-paper HTML, metadata HTML, and TeX/source package were inspected locally and explicitly withheld from public upload.
