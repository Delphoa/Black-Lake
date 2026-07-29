# Report-Mark: J-Space Full DEP Profile

- Run date: `2026-07-29`
- Profile ID: `j-space-workspace-20260729`
- Artifact scope: J-space and global-workspace source research only
- Supporting object types: `review report`, `audit summary`, `synthesis report`, `consolidation note`

## Source Metadata

| Field | Value |
|---|---|
| Primary work | *Verbalizable Representations Form a Global Workspace in Language Models* |
| Authors | Wes Gurnee et al. |
| Publication | Transformer Circuits Thread |
| Published | 2026-07-06 |
| Primary URL | https://transformer-circuits.pub/2026/workspace/index.html |
| Official summary | https://www.anthropic.com/research/global-workspace |
| Official implementation | https://github.com/anthropics/jacobian-lens |
| Source DEP snapshot | `DEP-E-20260729-Inspectable Agents` at `f91342a701df29adbb2df87886028a11f8095076` |
| Focused DEP-A baseline | `DEP-A-20260729-J-Space Workspace` at initial commit `5e9f722441b5fadbd910030b7641b301c217be75` |
| Source-file status | URLs only; no source file, clone, model, prompt set, corpus, or activation payload deposited |

## Review Report

### Scope reviewed

The profile was reviewed as a three-class, full-taxonomy representation of one research object:

- `DEP-E` for ongoing research objects;
- `DEP-A` for frozen interpretation and source-derived cold-storage objects;
- `DEP-R` for stable identity, routing, taxonomy coverage, and correction policy.

The original DEP-E remains a broader historical record. Only new files prefixed `j-space-` are counted as source-specific profile research objects.

### Object coverage

| Class | Canonical objects |
|---|---|
| `DEP-E` | Manifest, research manuscript, research report, literature review, evaluation, synthesis, implementation note |
| `DEP-A` | Manifest, manuscript review, extraction, transformed document, dataset, cold-storage asset |
| `DEP-R` | Manifest, structured record, index/catalog, static archival record |
| Accounted but not deposited | Authorized source file; correction/supersession record |

The structured DEP-R register also maps every supporting workflow object. A consolidated log carries the five log/trace roles, while this Report-Mark carries the four formal report/note roles.

### Research quality

The new objects maintain the evidence boundary established by the frozen review:

- reported findings are distinguished from reviewer conclusions;
- quantitative anchors remain attributed to the primary paper;
- the repository is treated as a reference implementation, not reproduction proof;
- bypass behavior, proprietary-model dependence, and monitoring-calibration gaps remain visible;
- consciousness and intent claims remain expressly unsupported.

## Audit Summary

| Audit area | Result | Notes |
|---|---|---|
| Single class per DEP entry | Pass | E, A, and R are separate records |
| Mandatory README components | Pass | Tags, Contents, item summaries, relevance, relationships, and final Attribution Blocks present |
| External README links | Pass | Both A and E manifests link to opposite-class, R, log, report, and discovery objects |
| Complete taxonomy accounting | Pass | DEP-R register covers every enumerated canonical and supporting type |
| Source-only scope | Pass | Other Inspectable Agents subjects are excluded from generated substantive objects |
| Source redistribution | Pass | No `.source/` or copied paper/repository payload |
| Correction integrity | Pass | No correction object fabricated; future policy preserves provenance |
| Publication indexes | Pass | Existing E/A ownership retained; no duplicate rows or invented R index |
| Paired-review ledgers | Not applicable | The A is an object-level selection, not a review of the complete multi-topic E |
| Staging hygiene | Pass | No incomplete staging object is part of the profile |

## Synthesis Report

The profile's scientific center is a bounded causal claim: the Jacobian lens identifies a sparse, vocabulary-aligned component that is unusually involved in selected verbal report, intermediate reasoning, and flexible computation. The global-workspace interpretation gains support from capacity and propagation evidence, but the same source shows that automatic processing can bypass the interface.

The full DEP split makes that boundary operational:

- DEP-E holds questions, evaluation, synthesis, and implementation work that may change.
- DEP-A holds the frozen critical interpretation and normalized source-derived evidence.
- DEP-R holds facts and routing that should stay stable even as analysis evolves.

This organization prevents a readable internal signal from being mistaken for an immutable truth. Future empirical changes belong in DEP-E; a stable prior review remains retrievable in DEP-A; and any correction must be explicit in the DEP-R lineage.

## Consolidation Note

### Consolidated source position

1. The paper supplies substantial causal evidence for a workspace-like interface in tested models.
2. The method is not a complete view of cognition and cannot support absence-of-risk conclusions.
3. Public code makes new research possible but does not reproduce the proprietary experiments.
4. The appropriate next step is a pre-registered open-model replication with matched controls and provenance receipts.
5. Production monitoring, automated intent labels, and consciousness claims remain outside the evidence boundary.

### Consolidated navigation

- Evolving research: [DEP-E README](../../.lake-data/DEP-E/DEP-E-20260729-Inspectable%20Agents/README.md)
- Frozen artifacts: [DEP-A README](../../.lake-data/DEP-A/DEP-A-20260729-J-Space%20Workspace/README.md)
- Static register: [DEP-R README](../../.lake-data/DEP-R/DEP-R-20260729-J-Space%20Profile/README.md)
- Complete crosswalk: [j-space-profile-crosswalk.md](../../.lake-data/DEP-R/DEP-R-20260729-J-Space%20Profile/j-space-profile-crosswalk.md)
- Workflow trace: [20260729-J-Space-Full-Profile-LOG.md](../../.logs/20260729-J-Space-Full-Profile-LOG.md)

## Validation Notes

- The manuscript follows the expanded manuscript schema and contains exactly three exercise paths.
- JSON dataset and object register syntax were checked.
- Cross-directory Markdown targets were resolved against the repository worktree.
- README Contents lists were checked against files inside each DEP.
- The final diff was reviewed for J-space-only scope and public-safe provenance.
- No independent paper experiment or reference implementation run was performed.

## Attribution Block

- Source URL: https://transformer-circuits.pub/2026/workspace/index.html
  - Applies to: all research findings and claim-status judgments in this report.
  - Notes: Complete primary paper inspected on 2026-07-29; linked and paraphrased.
- Source URL: https://www.anthropic.com/research/global-workspace
  - Applies to: official context and terminology.
  - Notes: Near-primary organization summary; not used in place of the paper.
- Source URL: https://github.com/anthropics/jacobian-lens
  - Applies to: implementation and reproducibility findings.
  - Notes: Official reference repository inspected but not executed or redistributed.
- Source URL: https://www.neuronpedia.org/jlens
  - Applies to: public implementation context.
  - Notes: Locator only; not treated as independent validation.
- Source record: https://github.com/Delphoa/Black-Lake/tree/f91342a701df29adbb2df87886028a11f8095076/.lake-data/DEP-E/DEP-E-20260729-Inspectable%20Agents
  - Applies to: selection provenance and scope exclusions.
  - Notes: Only its J-space source research is represented in this profile.
- Repository file: `.lake-data/DEP-A/DEP-A-20260729-J-Space Workspace/j-space-workspace-review.md`
  - Applies to: review baseline, evidence boundary, and consolidated interpretation.
  - Notes: Initial focused review created at commit `5e9f722441b5fadbd910030b7641b301c217be75`.
