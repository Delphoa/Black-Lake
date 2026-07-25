# DEP-E-20260725-ToolEmu Audit

#agent-safety #tool-use #sandboxing #evaluation #benchmark-lineage #reproducibility #research

Public-safe DEP-E research deposit generated from an iterative, source-first review of `DEP-20260714-Tech Intel 1305`. This pass expands the randomly selected ToolEmu thread through the complete v2 paper, ICLR record, official release at a fixed commit, benchmark assets, and release metadata.

## Contents

- `README.md` - DEP inventory, summary, relevance, source policy, and attribution.
- `toolemu-audit.md` - Schema-complete manuscript covering ToolEmu's emulator/evaluator design, benchmark, validation evidence, release drift, reproducibility limits, safe implementation paths, and follow-on reading.

No `.source/` directory is present. A temporary 70-page paper copy and a temporary shallow repository checkout supported read-only review. They are excluded from this package. No paper, benchmark file, repository code, prompt corpus, trajectory, model output, credential, or external source file is deposited.

## Summary of Items

### `toolemu-audit.md`

The manuscript separates four evidence layers: the selected DEP lineage, ToolEmu's paper-reported study, the current public release, and reviewer interpretation. The paper shows how a language model can emulate tool state and how adversarial state generation can increase failure discovery at a measurable cost in precision and emulator validity. It also demonstrates that safety and helpfulness must be evaluated together.

The new release review identifies two unresolved provenance defects. The pinned assets contain 38 toolkits and 330 tools, while the v2 paper and repository README declare 36 and 311. The repository's Apache-2.0 license file also conflicts with the MIT classifier in `setup.py`. No release note or manifest in the inspected tree reconciles either difference.

## Insights and Relevance

ToolEmu's durable idea is to separate the agent, virtual environment, safety evaluator, and helpfulness evaluator so that long-tail risks can be explored without real side effects. The evidence also shows why an LM-only sandbox cannot be its own authority: adversarial emulation found more failures but produced more critical simulation issues, and the public benchmark evolved without explicit lineage.

The downstream design implication is a hybrid evaluator. Language models can propose difficult virtual states and interpret trajectories, while typed invariants, deterministic simulators, immutable manifests, and independent human labels provide the evidence gates. This makes the artifact useful for agent-safety testing, benchmark governance, and provenance-preserving semantic-web expansion.

## Attribution Block

- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/tree/68af13582e1506c4a20cc8b051c703ba2e7120d0/.lake-data/DEP-20260714-Tech%20Intel%201305
  - Applies to: `toolemu-audit.md` and `README.md`.
  - Notes: Selected source DEP and its prior Report-Mark lineage.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/68af13582e1506c4a20cc8b051c703ba2e7120d0/.reports/BL-DEP-20260714-Tech%20Intel%201305-20260723/README.md
  - Applies to: `toolemu-audit.md`.
  - Notes: Latest prior source report inspected before expansion.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/68af13582e1506c4a20cc8b051c703ba2e7120d0/.lake-data/DEP-20260714-Tech%20Intel%201305/BL-DEP-Mark002%20Report-Mark.md
  - Applies to: `toolemu-audit.md`.
  - Notes: Latest prior Report-Mark and preserved research threads.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/9b475c0fb9d68d8a14131530d6bb4fca77004ae1/.lake-data/DEP-E/DEP-E-20260723-ANCHOR%20Audit
  - Applies to: `toolemu-audit.md`.
  - Notes: Latest prior same-family DEP-Class artifact reviewed before iterative expansion.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/9b475c0fb9d68d8a14131530d6bb4fca77004ae1/.lake-data/DEP-E/DEP-E-20260723-ANCHOR%20Audit/anchor-audit.md
  - Applies to: `toolemu-audit.md`.
  - Notes: Complete prior manuscript and five-thread expansion pool.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/9b475c0fb9d68d8a14131530d6bb4fca77004ae1/.logs/20260723-DEP-20260714-Tech%20Intel%201305-LOG.md
  - Applies to: `toolemu-audit.md`.
  - Notes: Latest prior operational log, questions, challenges, and validation notes.
- Source URL: https://arxiv.org/abs/2309.15817v2
  - Applies to: `toolemu-audit.md`.
  - Notes: Canonical ToolEmu metadata and current arXiv version.
- Source URL: https://arxiv.org/pdf/2309.15817v2
  - Applies to: `toolemu-audit.md`.
  - Notes: Complete 70-page paper, tables, figures, limitations, appendices, and prompts inspected.
- Source URL: https://openreview.net/forum?id=GEcwtMk1uA
  - Applies to: `toolemu-audit.md`.
  - Notes: ICLR 2024 Spotlight venue record.
- Source URL: https://github.com/ryoungj/ToolEmu/tree/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb
  - Applies to: `toolemu-audit.md`.
  - Notes: Official implementation pinned to the inspected public release tree.
- Source URL: https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/README.md
  - Applies to: `toolemu-audit.md`.
  - Notes: Release description, setup, benchmark-count claim, and historical run guidance.
- Source URL: https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/assets/all_cases.json
  - Applies to: `toolemu-audit.md`.
  - Notes: Pinned 144-case benchmark asset inspected statically.
- Source URL: https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/assets/all_toolkits.json
  - Applies to: `toolemu-audit.md`.
  - Notes: Pinned toolkit asset used to verify the 38-toolkit/330-tool release state.
- Source URL: https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/requirements.txt
  - Applies to: `toolemu-audit.md`.
  - Notes: Public dependency surface inspected for reproduction limits.
- Source URL: https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/setup.py
  - Applies to: `toolemu-audit.md`.
  - Notes: Package metadata and MIT classifier inspected.
- Source URL: https://github.com/ryoungj/ToolEmu/blob/ac4a7ab7ed8c7985d96231e214bd6b54304b7ddb/LICENSE
  - Applies to: `toolemu-audit.md`.
  - Notes: Apache License 2.0 text inspected.
- Source URL: https://arxiv.org/abs/2607.10455v1
  - Applies to: `toolemu-audit.md`.
  - Notes: Previously reviewed ANCHOR comparison source.
- Source URL: https://arxiv.org/abs/2410.09024
  - Applies to: `toolemu-audit.md`.
  - Notes: AgentHarm follow-up benchmark locator; not substantively re-reviewed.
- Source URL: https://arxiv.org/abs/2506.14866
  - Applies to: `toolemu-audit.md`.
  - Notes: OS-Harm follow-up benchmark locator; not substantively re-reviewed.
- Source URL: https://arxiv.org/abs/2402.10260
  - Applies to: `toolemu-audit.md`.
  - Notes: StrongREJECT follow-up evaluation locator; not substantively re-reviewed.
- Source URL: https://alignment.anthropic.com/2025/petri/
  - Applies to: `toolemu-audit.md`.
  - Notes: Petri official follow-up research locator; not substantively re-reviewed.

This package is an independent research review and does not imply author endorsement. All linked source materials remain under their original terms.
