# DEP-E-20260801-Verifiable Agent Systems

## Classification

- **DEP Class:** DEP-E - Ongoing research and evolving analysis
- **Title:** Verifiable Agent Systems
- **Source DEP:** `Black-Lake-Data/.lake-data/DEP-20260713-Tech Intel 1104`
- **Run date:** 2026-08-01
- **Status:** Full manuscript research artifact

## Tags

`#agentic-ai` `#verification` `#evidence-grounding` `#persistent-memory` `#ai-evals` `#provenance` `#security-operations` `#model-security` `#medical-ai-evaluation` `#edge-ai` `#ml-systems` `#ai-for-science` `#ai-safety`

## Inventory

- [`README.md`](README.md) - DEP classification, inventory, validation boundary, and final Attribution Block.
- [`verifiable-agent-systems.md`](verifiable-agent-systems.md) - Schema-complete manuscript research artifact reviewing the ten primary papers in the selected source DEP.

## Item Summary

The manuscript connects typed context evolution, selective memory, dense long-horizon grading, process-reward efficiency, provenance-based investigation, evidence-grounded malware analysis, independent proof criticism, clinical acquisition burden, and edge inference energy. It preserves source-specific methods, metrics, assumptions, and failure modes, then translates the shared pattern into bounded implementation concepts, exactly three safe exercise paths, and a local-first evidence-loop MVP.

## Insights and Relevance

The reviewed sources suggest that verifiability is distributed across the workflow rather than located in the model alone. Durable state should be typed and scoped; claims should resolve to evidence or artifacts; completion should be checked independently; revision should follow verifier feedback; and compute, energy, privacy, financial, clinical, and human burdens should constrain the loop. The synthesis is relevant to agent-platform design, evaluation engineering, defensive security, research agents, and safe infrastructure planning, but it is not an independent reproduction or deployment endorsement.

## Validation Boundary

The selected source DEP README and findings file, all ten complete primary papers, canonical arXiv metadata, first-page visual renders, and the official GRACE, LHTB, SAGEAgent, and ProofCouncil repository READMEs at immutable commits were inspected. Temporary review copies and extracted material remain withheld and are not deposited. No code, model, dataset, benchmark, theorem, malware sample, production alert stream, patient record, clinical workflow, or hardware measurement was executed or independently reproduced.

## Attribution Block

### Source DEP

- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/tree/2bebe12af935e746e37ccc8354beebe03c0694b7/.lake-data/DEP-20260713-Tech%20Intel%201104
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Selected source DEP at the reviewed repository snapshot.

### Primary Papers

- Source URL: https://arxiv.org/abs/2607.09175
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Primary GRACE paper, version v1.
- Source URL: https://arxiv.org/abs/2607.09532
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Primary statistically undetectable backdoors paper, version v1.
- Source URL: https://arxiv.org/abs/2607.08964
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Primary Long-Horizon-Terminal-Bench paper, version v2.
- Source URL: https://arxiv.org/abs/2607.09153
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Primary KV-PRM paper, version v1.
- Source URL: https://arxiv.org/abs/2607.09493
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Primary shared selective persistent memory paper, version v1.
- Source URL: https://arxiv.org/abs/2607.09176
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Primary SherAgent paper, version v1; defensive security evidence.
- Source URL: https://arxiv.org/abs/2607.09521
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Primary SAGEAgent paper, version v1; non-diagnostic evidence.
- Source URL: https://arxiv.org/abs/2607.09520
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Primary edge-VLM energy paper, version v1.
- Source URL: https://arxiv.org/abs/2607.09474
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Primary ProofCouncil paper, version v1.
- Source URL: https://arxiv.org/abs/2607.09179
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Primary Malaika paper, version v1; defensive static-analysis evidence.

### Official Implementations and Context

- Source URL: https://github.com/RedMind-Research/GRACE/tree/b8b6b9adbb1cd868a7298c8526b2f2e3774ccab4
  - Applies to: `verifiable-agent-systems.md`
  - Notes: GRACE official repository inspected at an immutable commit.
- Source URL: https://github.com/zli12321/LHTB/tree/b695ed2eaa41b95fd60949e595955fc8e60eac32
  - Applies to: `verifiable-agent-systems.md`
  - Notes: LHTB official repository and modified-harness guidance inspected at an immutable commit.
- Source URL: https://huggingface.co/datasets/IntelligenceLab/Long-Horizon-Terminal-Bench
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Official benchmark dataset route discovered through the project page; not downloaded.
- Source URL: https://github.com/Chongyu1117/SAGEAgent/tree/5fcb6941879d3bc25a99aaec203bc23f56e0e1af
  - Applies to: `verifiable-agent-systems.md`
  - Notes: SAGEAgent official repository inspected at an immutable commit.
- Source URL: https://github.com/eth-sri/proof-council/tree/2555c798013603748c5556866c89a9eae5795d48
  - Applies to: `verifiable-agent-systems.md`
  - Notes: ProofCouncil official repository inspected at an immutable commit.
- Source URL: https://arxiv.org/abs/2506.07982
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Tau2-bench primary context for the GRACE evaluation environment.
- Source URL: https://arxiv.org/abs/2606.18119
  - Applies to: `verifiable-agent-systems.md`
  - Notes: FirstProof Second Batch primary context for ProofCouncil.
- Source URL: https://arxiv.org/abs/2509.14335
  - Applies to: `verifiable-agent-systems.md`
  - Notes: MalEval primary context for Malaika.
- Source URL: https://attack.mitre.org/matrices/mobile/
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Official ATT&CK Mobile knowledge-base context.
- Source URL: https://github.com/ocsf/ocsf-schema
  - Applies to: `verifiable-agent-systems.md`
  - Notes: Official OCSF repository used as security-event schema context.

### Attribution Notes

- Paper and repository authors retain authorship and their respective licenses.
- This is a public-safe derived manuscript; no temporary paper, extraction, render, dataset, code checkout, or sensitive data is redistributed.
- Reported results remain source claims unless explicitly labeled as reviewer interpretation or inference.
