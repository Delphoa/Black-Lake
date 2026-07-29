# DEP-R-20260729-J-Space Profile

#artificial-intelligence #language-models #mechanistic-interpretability #jacobian-lens #global-workspace #record-catalog #provenance

- DEP Class: `DEP-R`
- Subject: *Verbalizable Representations Form a Global Workspace in Language Models*
- Profile ID: `j-space-workspace-20260729`
- Record role: stable identity, status, routing, taxonomy coverage, and correction boundary

This DEP-R is the static record layer of the J-space full DEP profile. It does not duplicate the evolving research objects in DEP-E or the frozen critical artifacts in DEP-A.

## Contents

- [`README.md`](README.md) - DEP-R identity, package inventory, profile relationships, relevance, and final attribution.
- [`j-space-static-archival-record.md`](j-space-static-archival-record.md) - stable source identity, implementation fingerprints, bounded claim status, lineage, distribution boundary, and correction policy.
- [`j-space-profile-object-register.json`](j-space-profile-object-register.json) - machine-readable registry of every canonical and supporting record-object type, its DEP class or workflow role, path, status, and scope decision.
- [`j-space-profile-crosswalk.md`](j-space-profile-crosswalk.md) - human-readable catalog linking all deposited profile and workflow objects across repository directories.

No `.source/` directory or source copy is included. The primary paper did not present a visible redistribution license in the inspected page, and the user did not authorize source-file deposition. No correction or supersession artifact is created because no correction is presently known.

## Summary of Items

### `README.md`

Defines this entry as `DEP-R` and keeps the static record distinct from research (`DEP-E`) and cold storage (`DEP-A`).

### `j-space-static-archival-record.md`

Preserves the durable citation, authorship, official source locators, inspected implementation version and blob fingerprints, narrow claim-status ledger, profile lineage, and future correction rule.

### `j-space-profile-object-register.json`

Provides the authoritative machine-readable mapping between record-object type and owning DEP class. It also accounts for objects that must not be manufactured: authorized source files, corrections, and completed-run staging artifacts.

### `j-space-profile-crosswalk.md`

Acts as the human navigation layer for the full profile and distinguishes canonical deposits from supporting workflow objects.

## Insights and Relevance

The profile separates three stability needs that would otherwise be conflated:

- `DEP-E` can continue research, replication planning, evaluation, and implementation analysis.
- `DEP-A` freezes the source-grounded review, extraction, transformed method card, and normalized evidence data.
- `DEP-R` preserves stable identity, routing, status, and correction semantics without restating the scientific analysis.

This separation makes downstream discovery and correction safer. A reviewer can locate the current research surface, retrieve the frozen interpretation, and verify which source or workflow objects were intentionally not deposited.

## J-Space Full DEP Profile

| Profile role | DEP class / workflow | External object |
|---|---|---|
| Evolving research | `DEP-E` | [`j-space-research-manuscript.md`](../DEP-E/DEP-E-20260729-Inspectable%20Agents/j-space-research-manuscript.md) |
| Research report | `DEP-E` | [`j-space-research-report.md`](../DEP-E/DEP-E-20260729-Inspectable%20Agents/j-space-research-report.md) |
| Literature review | `DEP-E` | [`j-space-literature-review.md`](../DEP-E/DEP-E-20260729-Inspectable%20Agents/j-space-literature-review.md) |
| Method evaluation | `DEP-E` | [`j-space-method-evaluation.md`](../DEP-E/DEP-E-20260729-Inspectable%20Agents/j-space-method-evaluation.md) |
| Evidence synthesis | `DEP-E` | [`j-space-evidence-synthesis.md`](../DEP-E/DEP-E-20260729-Inspectable%20Agents/j-space-evidence-synthesis.md) |
| Implementation note | `DEP-E` | [`j-space-implementation-note.md`](../DEP-E/DEP-E-20260729-Inspectable%20Agents/j-space-implementation-note.md) |
| Frozen manuscript review | `DEP-A` | [`j-space-workspace-review.md`](../DEP-A/DEP-A-20260729-J-Space%20Workspace/j-space-workspace-review.md) |
| Source extraction | `DEP-A` | [`j-space-source-extraction.md`](../DEP-A/DEP-A-20260729-J-Space%20Workspace/j-space-source-extraction.md) |
| Transformed method card | `DEP-A` | [`j-space-method-card.md`](../DEP-A/DEP-A-20260729-J-Space%20Workspace/j-space-method-card.md) |
| Claim-evidence dataset | `DEP-A` | [`j-space-claim-evidence-dataset.json`](../DEP-A/DEP-A-20260729-J-Space%20Workspace/j-space-claim-evidence-dataset.json) |
| Workflow trace | Workflow | [`20260729-J-Space-Full-Profile-LOG.md`](../../.logs/20260729-J-Space-Full-Profile-LOG.md) |
| Review and audit mark | Workflow | [`Report-Mark.md`](../../.reports/BL-J-Space-Full-Profile-20260729/Report-Mark.md) |

The complete object-type mapping is in [`j-space-profile-crosswalk.md`](j-space-profile-crosswalk.md).

## Attribution Block

- Source URL: https://transformer-circuits.pub/2026/workspace/index.html
  - Applies to: `j-space-static-archival-record.md`, `j-space-profile-object-register.json`, `j-space-profile-crosswalk.md`, and this README.
  - Notes: Canonical primary paper, published 2026-07-06 and inspected 2026-07-29. Linked and paraphrased; no source copy deposited.
- Source URL: https://www.anthropic.com/research/global-workspace
  - Applies to: `j-space-static-archival-record.md` and this README.
  - Notes: Official organization summary used as near-primary context.
- Source URL: https://github.com/anthropics/jacobian-lens
  - Applies to: `j-space-static-archival-record.md`, `j-space-profile-object-register.json`, and this README.
  - Notes: Official reference implementation; repository inspected but not cloned into this DEP or executed.
- Source URL: https://github.com/anthropics/jacobian-lens/blob/main/README.md
  - Applies to: `j-space-static-archival-record.md`.
  - Notes: Inspected repository documentation; blob `296ba6e47e3fc01da6bea94a0c38248ff9e6641a`.
- Source URL: https://github.com/anthropics/jacobian-lens/blob/main/pyproject.toml
  - Applies to: `j-space-static-archival-record.md`.
  - Notes: Inspected package metadata; blob `facb1859429522ce7a695a3a65970101cbdae4cb`.
- Source URL: https://github.com/anthropics/jacobian-lens/blob/main/LICENSE
  - Applies to: `j-space-static-archival-record.md`.
  - Notes: Apache License 2.0 for the companion code; blob `d645695673349e3947e8e5ae42332d0ac3164cd7`.
- Source URL: https://www.neuronpedia.org/jlens
  - Applies to: `j-space-static-archival-record.md`.
  - Notes: Public implementation locator linked by the paper; not used as independent validation.
- Source record: https://github.com/Delphoa/Black-Lake/tree/f91342a701df29adbb2df87886028a11f8095076/.lake-data/DEP-E/DEP-E-20260729-Inspectable%20Agents
  - Applies to: all files in this DEP-R.
  - Notes: Pinned selection-provenance record. Only the J-space research object is represented in this profile.
- Repository file: `.lake-data/DEP-A/DEP-A-20260729-J-Space Workspace/j-space-workspace-review.md`
  - Applies to: all files in this DEP-R.
  - Notes: Frozen source-grounded review at initial commit `5e9f722441b5fadbd910030b7641b301c217be75`.
