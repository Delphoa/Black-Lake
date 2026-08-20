# DEP-E-20260729-Inspectable Agents

#artificial-intelligence #language-models #mechanistic-interpretability #jacobian-lens #global-workspace #agent-evaluation #provenance #safety

- DEP Class: `DEP-E`
- Artifact type: `DEP research package`
- Source DEP: [`DEP-20260717-Tech Intel 0104`](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260717-Tech%20Intel%200104)
- Run date: `2026-07-29`
- Full-profile subject: *Verbalizable Representations Form a Global Workspace in Language Models*
- Profile ID: `j-space-workspace-20260729`

This historical DEP-E originally reviewed ten research findings as a connected evidence set for inspectable agents. The full-profile additions in this package are deliberately narrower: every new file prefixed `j-space-` concerns only the Jacobian lens, J-space/global-workspace evidence, and the official implementation surfaces for that one selected paper. The other subjects remain preserved in the original manuscript but are not imported into the J-space profile.

## Contents

| File | Record-object type | Purpose |
|---|---|---|
| [`README.md`](README.md) | DEP manifest / README | DEP-E identity, complete package inventory, scope boundary, profile links, and attribution |
| [`inspectable-agents.md`](inspectable-agents.md) | Legacy DEP research artifact | Preserved original multi-topic manuscript; not counted as a J-space-only full-profile object |
| [`j-space-research-manuscript.md`](j-space-research-manuscript.md) | Research manuscript | Schema-complete, source-grounded reconstruction and critical analysis |
| [`j-space-research-report.md`](j-space-research-report.md) | Research report | Findings, quantitative anchors, open questions, and next research decisions |
| [`j-space-literature-review.md`](j-space-literature-review.md) | Literature review | Bounded comparison of the primary paper and official source surfaces |
| [`j-space-method-evaluation.md`](j-space-method-evaluation.md) | Evaluation | Construct validity, causal controls, coverage, reproducibility, and safety-readiness assessment |
| [`j-space-evidence-synthesis.md`](j-space-evidence-synthesis.md) | Synthesis | Integrated causal argument and claim-status map |
| [`j-space-implementation-note.md`](j-space-implementation-note.md) | Implementation note | Local-only open-model research harness, records, acceptance tests, and stop conditions |

No external source files, model weights, prompts, corpora, activations, benchmark payloads, or repository clones are committed.

## Summary of Items

### `README.md`

Defines the owning research class, distinguishes the legacy multi-topic artifact from the J-space-only profile objects, inventories every file, and provides reciprocal navigation outside this directory.

### `inspectable-agents.md`

Preserves the original ten-subject review and its cross-domain synthesis. It supplies historical context and selection lineage only; its unrelated subjects do not support the new J-space objects.

### `j-space-research-manuscript.md`

Provides the complete evidence ledger and manuscript schema for the Jacobian lens construction, sparse J-space, report and reasoning interventions, selective bypass behavior, workspace structure, alignment cases, counterfactual reflection, limitations, replication paths, and bounded MVP.

### `j-space-research-report.md`

Condenses the research state into supported findings, unresolved questions, quantitative anchors, research decisions, and prioritized next evidence.

### `j-space-literature-review.md`

Compares the evidentiary roles of the full paper, Anthropic summary, official repository, and Neuronpedia locator without expanding into unrelated literature or source-DEP topics.

### `j-space-method-evaluation.md`

Evaluates what the lens measures, the strength of its causal controls, external validity, reproducibility, failure modes, and appropriate research-only status.

### `j-space-evidence-synthesis.md`

Connects transport, sparse representation, reportability, mediation, intermediate use, flexible reuse, selectivity, broadcast, auditing, and training into one bounded causal chain.

### `j-space-implementation-note.md`

Translates the source into a local-only open-model replication design with explicit provenance records, negative controls, privacy boundaries, acceptance tests, and stop conditions.

## Insights and Relevance

The J-space evidence supports a narrower conclusion than “thought reading”: a small, vocabulary-aligned component is unusually involved in selected reportable and flexible computations, while some automatic cognition bypasses it. That makes the method useful for research hypothesis generation and causal audit follow-up, but insufficient as a standalone safety monitor, intent proof, or consciousness test.

The full profile keeps evolving analysis in DEP-E, freezes the focused review and derived evidence in DEP-A, and preserves stable identity and routing in DEP-R. This lets future work change without erasing the original review or silently redefining the source.

## J-Space Full DEP Profile

| External object | Object type | DEP class / workflow | Link |
|---|---|---|---|
| Focused DEP-A manifest | DEP manifest / README | `DEP-A` | [`README.md`](../../../DEP-A/Series%20001/DEP-A-20260729-J-Space%20Workspace/README.md) |
| Frozen manuscript review | Manuscript review; cold-storage asset | `DEP-A` | [`j-space-workspace-review.md`](../../../DEP-A/Series%20001/DEP-A-20260729-J-Space%20Workspace/j-space-workspace-review.md) |
| Source extraction | Extraction | `DEP-A` | [`j-space-source-extraction.md`](../../../DEP-A/Series%20001/DEP-A-20260729-J-Space%20Workspace/j-space-source-extraction.md) |
| Method card | Transformed document | `DEP-A` | [`j-space-method-card.md`](../../../DEP-A/Series%20001/DEP-A-20260729-J-Space%20Workspace/j-space-method-card.md) |
| Claim-evidence data | Dataset | `DEP-A` | [`j-space-claim-evidence-dataset.json`](../../../DEP-A/Series%20001/DEP-A-20260729-J-Space%20Workspace/j-space-claim-evidence-dataset.json) |
| Static profile manifest | DEP manifest / README | `DEP-R` | [`README.md`](../../../DEP-R/Series%20001/DEP-R-20260729-J-Space%20Profile/README.md) |
| Static archival record | Static archival record | `DEP-R` | [`j-space-static-archival-record.md`](../../../DEP-R/Series%20001/DEP-R-20260729-J-Space%20Profile/j-space-static-archival-record.md) |
| Machine object register | Structured record | `DEP-R` | [`j-space-profile-object-register.json`](../../../DEP-R/Series%20001/DEP-R-20260729-J-Space%20Profile/j-space-profile-object-register.json) |
| Human profile crosswalk | Index / catalog | `DEP-R` | [`j-space-profile-crosswalk.md`](../../../DEP-R/Series%20001/DEP-R-20260729-J-Space%20Profile/j-space-profile-crosswalk.md) |
| Workflow trace | Five log/trace types | Workflow | [`20260729-J-Space-Full-Profile-LOG.md`](../../../../.logs/20260729-J-Space-Full-Profile-LOG.md) |
| Review and audit mark | Four report/note types | Workflow | [`Report-Mark.md`](../../../../.reports/BL-J-Space-Full-Profile-20260729/Report-Mark.md) |
| DEP-E publication index | Publication index | Workflow | [`pubs-index.md`](../../.index/pubs-index.md) |
| DEP-A publication index | Publication index | Workflow | [`pubs-index.md`](../../../DEP-A/.index/pubs-index.md) |

## Attribution Block

### J-space primary and official sources

- Source URL: https://transformer-circuits.pub/2026/workspace/index.html
  - Applies to: every `j-space-*` file and this README.
  - Notes: Complete primary paper, published 2026-07-06 and inspected 2026-07-29. Linked and paraphrased; no source copy deposited.
- Source URL: https://www.anthropic.com/research/global-workspace
  - Applies to: every `j-space-*` Markdown file and this README.
  - Notes: Official author-organization summary used as near-primary context.
- Source URL: https://github.com/anthropics/jacobian-lens
  - Applies to: every `j-space-*` file and this README.
  - Notes: Official companion repository inspected for implementation and reproducibility boundaries; not executed or redistributed.
- Source URL: https://github.com/anthropics/jacobian-lens/blob/main/README.md
  - Applies to: `j-space-research-manuscript.md`, `j-space-literature-review.md`, `j-space-method-evaluation.md`, and `j-space-implementation-note.md`.
  - Notes: Inspected reference documentation; blob `296ba6e47e3fc01da6bea94a0c38248ff9e6641a`.
- Source URL: https://github.com/anthropics/jacobian-lens/blob/main/pyproject.toml
  - Applies to: `j-space-research-manuscript.md` and `j-space-implementation-note.md`.
  - Notes: Inspected `jlens` 0.1.0 package metadata; blob `facb1859429522ce7a695a3a65970101cbdae4cb`.
- Source URL: https://github.com/anthropics/jacobian-lens/blob/main/LICENSE
  - Applies to: `j-space-research-manuscript.md` and `j-space-implementation-note.md`.
  - Notes: Apache License 2.0 for the companion code; blob `d645695673349e3947e8e5ae42332d0ac3164cd7`.
- Source URL: https://www.neuronpedia.org/jlens
  - Applies to: `j-space-research-manuscript.md` and `j-space-literature-review.md`.
  - Notes: Public interactive surface linked by the paper; context only, not independent validation.
- Source record: https://github.com/Delphoa/Black-Lake/tree/f91342a701df29adbb2df87886028a11f8095076/.lake-data/DEP-E/DEP-E-20260729-Inspectable%20Agents
  - Applies to: every `j-space-*` file and this README.
  - Notes: Pinned selection provenance. The generated profile objects exclude all unrelated research subjects.

### Legacy multi-topic manuscript sources

- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260717-Tech%20Intel%200104
  - Applies to: `inspectable-agents.md` and this README.
  - Notes: Selected upstream source DEP for the original multi-topic artifact.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260717-Tech%20Intel%200104/daily_research_findings_2026-07-17_0104.md
  - Applies to: `inspectable-agents.md`.
  - Notes: Daily findings source for the original selection set.
- Source URL: https://openai.com/index/unlocking-self-improvement-gpt-red/
  - Applies to: `inspectable-agents.md` only.
  - Notes: Original GPT-Red source; excluded from J-space profile objects.
- Source URL: https://openai.com/index/separating-signal-from-noise-coding-evaluations/
  - Applies to: `inspectable-agents.md` only.
  - Notes: Original coding-evaluation audit source; excluded from J-space profile objects.
- Source URL: https://arxiv.org/abs/2607.13618
  - Applies to: `inspectable-agents.md` only.
  - Notes: STOCKTAKE canonical record; excluded from J-space profile objects.
- Source URL: https://arxiv.org/html/2607.13618
  - Applies to: `inspectable-agents.md` only.
  - Notes: STOCKTAKE full paper; excluded from J-space profile objects.
- Source URL: https://arxiv.org/abs/2607.08077
  - Applies to: `inspectable-agents.md` only.
  - Notes: Modular-pretraining paper; excluded from J-space profile objects.
- Source URL: https://alignment.anthropic.com/2026/modular-pretraining/
  - Applies to: `inspectable-agents.md` only.
  - Notes: Official modular-pretraining account; excluded from J-space profile objects.
- Source URL: https://doi.org/10.1038/s41586-026-10675-5
  - Applies to: `inspectable-agents.md` only.
  - Notes: Medical-agent source; excluded from J-space profile objects.
- Source URL: https://doi.org/10.1038/s42256-026-01261-5
  - Applies to: `inspectable-agents.md` only.
  - Notes: AI X-ray scientist source; excluded from J-space profile objects.
- Source URL: https://arxiv.org/abs/2607.13157v1
  - Applies to: `inspectable-agents.md` only.
  - Notes: Oracle Agent Memory source; excluded from J-space profile objects.
- Source URL: https://arxiv.org/abs/2607.13939
  - Applies to: `inspectable-agents.md` only.
  - Notes: HORCRUX canonical record; excluded from J-space profile objects.
- Source URL: https://arxiv.org/html/2607.13939
  - Applies to: `inspectable-agents.md` only.
  - Notes: HORCRUX full paper; excluded from J-space profile objects.
- Source URL: https://arxiv.org/abs/2607.13754
  - Applies to: `inspectable-agents.md` only.
  - Notes: PriEval-Protect source; excluded from J-space profile objects.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-A/Series%20001/DEP-A-20260719-Oracle%20Agent%20Memory
  - Applies to: `inspectable-agents.md` only.
  - Notes: Prior Oracle Agent Memory review used for original continuity.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-Smart%20Coverage%20Goals
  - Applies to: `inspectable-agents.md` only.
  - Notes: Prior Smart Coverage Goals review used for original continuity.
- Source URL: https://doi.org/10.6028/NIST.CSWP.39.ipd
  - Applies to: `inspectable-agents.md` only.
  - Notes: NIST crypto-agility context used by the original artifact; excluded from J-space profile objects.
