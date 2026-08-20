# DEP-E-20260711-Agent Memory Forensics

#agent-security #memory-security #agentic-ai #forensics #tool-use #observability #incident-response

Public deposition context: A source DEP was selected through the Black-Lake Data Processing & Review 0900 eligibility and random-selection process. This DEP-E expands the selected source's primary paper on defensive trajectory signatures for explicit-memory poisoning. Local execution context and private source material are not included.

## Contents

- README.md
  - DEP-E manifest, item summary, relevance statement, and final attribution block.
- memory-forensics.md
  - Schema-complete DEP research artifact reviewing the selected primary paper, its evidence boundaries, and defensive implementation paths.

No .source folder is included. The source DEP already preserves the original research finding as a repository artifact, while this deposit cites public primary URLs and does not redistribute the paper PDF, TeX source, code, data, or private traces.

## Summary of Items

- README.md identifies the DEP class, subject tags, included files, source-handling decision, and durable attribution.
- memory-forensics.md records the direct source review of arXiv:2606.30566, including reported results, limitations, explicit-memory assumptions, defensive design implications, and the related source-DEP context.

## Insights and Relevance

The deposited research distinguishes a useful operational pattern from an overbroad security claim. In an agent architecture where persistent memory retrieval is an explicit logged operation, a harmful later action can leave a trace signature suitable for defensive review. That finding does not generalize automatically to hidden state, implicit retrieval, or prompt-inline attacks. The resulting DEP-E therefore emphasizes evidence-ledger design, benign-workload calibration, telemetry minimization, and human review alongside detection.

## Attribution Block

- Source URL: https://arxiv.org/abs/2606.30566
  - Applies to: memory-forensics.md
  - Notes: Primary arXiv metadata and abstract for the selected paper.
- Source URL: https://arxiv.org/html/2606.30566
  - Applies to: memory-forensics.md
  - Notes: Primary full text inspected for method, reported results, and limitations.
- Source URL: https://doi.org/10.48550/arXiv.2606.30566
  - Applies to: memory-forensics.md
  - Notes: Persistent identifier for the selected paper.
- Source URL: https://arxiv.org/abs/2605.08442
  - Applies to: memory-forensics.md
  - Notes: Companion-work metadata referenced by the selected paper.
- Repository file: Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/README.md
  - Applies to: memory-forensics.md
  - Notes: Selected source DEP manifest and attribution context.
- Repository file: Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/daily_research_findings_2026-07-01_0103.md
  - Applies to: memory-forensics.md
  - Notes: Selected raw finding and primary-source locator.
- Repository file: Black-Lake/.logs/20260709-Arxiv-2D-RC-OTFS-LOG.md
  - Applies to: memory-forensics.md
  - Notes: Prior related material reviewed for this expansion pass.
- Repository file: Black-Lake/README.md
  - Applies to: README.md, memory-forensics.md
  - Notes: DEP-E placement, content, attribution, and commit-message authority.
- Repository file: Black-Lake-Data/README.md
  - Applies to: memory-forensics.md
  - Notes: Source DEP placement and attribution authority.
