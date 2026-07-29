---
title: "J-Space Profile Crosswalk"
artifact_id: "DEP-R-JSPACE-CROSSWALK-20260729"
dep_class: "DEP-R"
profile_id: "j-space-workspace-20260729"
record_object_type: "index / catalog"
source_scope: "J-space research only"
generated_at: "2026-07-29"
---

# J-Space Profile Crosswalk

## Canonical DEP Objects

| Canonical object type | DEP class | Status | Profile object |
|---|---|---|---|
| DEP manifest / README | `DEP-E` | Deposited | [`DEP-E README`](../../DEP-E/DEP-E-20260729-Inspectable%20Agents/README.md) |
| DEP manifest / README | `DEP-A` | Deposited | [`DEP-A README`](../../DEP-A/DEP-A-20260729-J-Space%20Workspace/README.md) |
| DEP manifest / README | `DEP-R` | Deposited | [`DEP-R README`](README.md) |
| Research manuscript | `DEP-E` | Deposited | [`j-space-research-manuscript.md`](../../DEP-E/DEP-E-20260729-Inspectable%20Agents/j-space-research-manuscript.md) |
| Manuscript review | `DEP-A` | Deposited | [`j-space-workspace-review.md`](../../DEP-A/DEP-A-20260729-J-Space%20Workspace/j-space-workspace-review.md) |
| Research report | `DEP-E` | Deposited | [`j-space-research-report.md`](../../DEP-E/DEP-E-20260729-Inspectable%20Agents/j-space-research-report.md) |
| Literature review | `DEP-E` | Deposited | [`j-space-literature-review.md`](../../DEP-E/DEP-E-20260729-Inspectable%20Agents/j-space-literature-review.md) |
| Evaluation | `DEP-E` | Deposited | [`j-space-method-evaluation.md`](../../DEP-E/DEP-E-20260729-Inspectable%20Agents/j-space-method-evaluation.md) |
| Synthesis | `DEP-E` | Deposited | [`j-space-evidence-synthesis.md`](../../DEP-E/DEP-E-20260729-Inspectable%20Agents/j-space-evidence-synthesis.md) |
| Implementation note | `DEP-E` | Deposited | [`j-space-implementation-note.md`](../../DEP-E/DEP-E-20260729-Inspectable%20Agents/j-space-implementation-note.md) |
| Extraction | `DEP-A` | Deposited | [`j-space-source-extraction.md`](../../DEP-A/DEP-A-20260729-J-Space%20Workspace/j-space-source-extraction.md) |
| Transformed document | `DEP-A` | Deposited | [`j-space-method-card.md`](../../DEP-A/DEP-A-20260729-J-Space%20Workspace/j-space-method-card.md) |
| Dataset | `DEP-A` | Deposited | [`j-space-claim-evidence-dataset.json`](../../DEP-A/DEP-A-20260729-J-Space%20Workspace/j-space-claim-evidence-dataset.json) |
| Structured record | `DEP-R` | Deposited | [`j-space-profile-object-register.json`](j-space-profile-object-register.json) |
| Index / catalog | `DEP-R` | Deposited | [`j-space-profile-crosswalk.md`](j-space-profile-crosswalk.md) |
| Cold-storage asset | `DEP-A` | Deposited | [`j-space-workspace-review.md`](../../DEP-A/DEP-A-20260729-J-Space%20Workspace/j-space-workspace-review.md) |
| Static archival record | `DEP-R` | Deposited | [`j-space-static-archival-record.md`](j-space-static-archival-record.md) |
| Authorized source file | None | Not deposited | No authorization and no reviewed paper redistribution license; no `.source/` exists |
| Correction / supersession record | None | Not applicable | No correction is presently known; future correction policy is in the static record |

## Supporting Workflow Objects

| Supporting object type | Status | Workflow object |
|---|---|---|
| Operational log | Deposited | [`20260729-J-Space-Full-Profile-LOG.md`](../../../.logs/20260729-J-Space-Full-Profile-LOG.md) |
| Deposition log | Deposited | [`20260729-J-Space-Full-Profile-LOG.md`](../../../.logs/20260729-J-Space-Full-Profile-LOG.md) |
| Review log | Deposited | [`20260729-J-Space-Full-Profile-LOG.md`](../../../.logs/20260729-J-Space-Full-Profile-LOG.md) |
| Ingestion note | Deposited | [`20260729-J-Space-Full-Profile-LOG.md`](../../../.logs/20260729-J-Space-Full-Profile-LOG.md) |
| Process trace | Deposited | [`20260729-J-Space-Full-Profile-LOG.md`](../../../.logs/20260729-J-Space-Full-Profile-LOG.md) |
| Review report | Deposited | [`Report-Mark.md`](../../../.reports/BL-J-Space-Full-Profile-20260729/Report-Mark.md) |
| Audit summary | Deposited | [`Report-Mark.md`](../../../.reports/BL-J-Space-Full-Profile-20260729/Report-Mark.md) |
| Synthesis report | Deposited | [`Report-Mark.md`](../../../.reports/BL-J-Space-Full-Profile-20260729/Report-Mark.md) |
| Consolidation note | Deposited | [`Report-Mark.md`](../../../.reports/BL-J-Space-Full-Profile-20260729/Report-Mark.md) |
| Staging artifact | Not applicable at completion | Transient drafting material is not a canonical deposit and is not committed |
| Deduplication / pointer index | Accounted for | This crosswalk is the canonical pointer catalog; no duplicate source package was created |
| Publication index | Existing | [`DEP-E publication index`](../../DEP-E/.index/pubs-index.md) and [`DEP-A publication index`](../../DEP-A/.index/pubs-index.md) |
| Template | Existing | [`DEP README template`](../../../.templates/dep-readme-template.md) |

## Scope and Classification Notes

- DEP class and record-object type are separate axes. Every deposited canonical object inherits exactly one owning class.
- The existing `inspectable-agents.md` remains broader upstream context. It is not counted as a J-space-only profile object.
- Supporting workflow objects have no DEP class unless separately deposited inside a DEP.
- The existing DEP-A is an object-level selection from a multi-topic DEP-E, so the complete-record paired-review ledgers are not used.
- Publication indexes already own the relevant paper under the existing DEP-E and focused DEP-A; no duplicate row or DEP-R index is created.
