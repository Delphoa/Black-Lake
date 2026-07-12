# Arxiv DEP Log: VLM Probing

## Public-Safe Run Summary

- Date: 2026-07-12
- Actor/tool: Codex recurring `Black Lake Arxiv DEP 0900` workflow
- Action: Randomly select one eligible local arXiv paper, review it source-first, synthesize it with three related DEP entries, and deposit a log, Report-Mark, and DEP-E manuscript.
- Outcome: Selected arXiv:2005.07310v2, *Behind the Scene: Revealing the Secrets of Pre-trained Vision-and-Language Models*; duplicate checks passed and no reselection was required.
- Affected DEP: `.lake-data/DEP-E-20260712-VLM Probing`
- Blockers: No blocking issue. The paper-linked code repository was unavailable during inspection, and no source package was present in the local archive unit.

## Random Selection Method

- Enumeration command: `rg --files -g "*.pdf"` against the local arXiv archive.
- Candidate unit: Each unique PDF parent directory, with adjacent readme or metadata files treated as metadata for the same paper unit.
- Candidate units: 75,761.
- Draw method: PowerShell `Get-Random` uniform zero-based index with duplicate rejection.
- Selected zero-based index: 9,460.
- Selected arXiv ID: 2005.07310v2.
- Selected title: *Behind the Scene: Revealing the Secrets of Pre-trained Vision-and-Language Models*.
- Duplicate rejections and reselections: 0.

## Deduplication and Eligibility

- Dedup locations: `Black-Lake/.logs`, `Black-Lake/.reports`, `Black-Lake/.lake-data`, automation memory, `Black-Lake-Data/.lake-data`, and `Black-Lake-Data/.reports`.
- Matching keys: arXiv ID and versionless ID, DOI, normalized title, and slug variants.
- Used arXiv IDs observed: 344.
- Candidate archive units excluded by used arXiv ID: 65.
- Exact selected-paper matches: 0.
- Public-safe 24-hour cutoff date: 2026-07-11; no selected-paper marker was found on or after the cutoff.
- Eligibility result: Accepted on the first random draw.

## Source Review

- Local evidence: Paper PDF and adjacent provenance readme were inspected; local paths are withheld.
- Extraction: `pypdf` produced a 58,111-byte text cache. HTML and source-package text were unavailable locally.
- Public evidence: arXiv abstract/HTML, the ECCV 2020 paper page/PDF, Microsoft Research publication metadata, DOI metadata, and the paper-linked code locator were inspected where accessible.
- Code status: The paper points to `https://github.com/JizeCao/VALUE`; the repository returned unavailable/not-found responses during this run, so no code claims were used as reproducibility evidence.
- Source files collected into the DEP: None. The original PDF remains in the private source archive and is not redistributed.

## Related DEP Entries

1. `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` — joint multimodal latent fusion and geometry-aware representation evaluation provide a modern target for VALUE-style probing.
2. `.lake-data/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` — representation collapse, output-space regularization, and robustness metrics complement attention and embedding probes.
3. `.lake-data/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` — specialized attention, heterogeneous feature pathways, and distillation expose architecture-level questions similar to VALUE's head specialization analysis.

## Output Inventory

- `.logs/20260712-Arxiv-VLM-Probing-LOG.md`
- `.reports/BL-Arxiv-VLM-Probing-20260712/Report-Mark.md`
- `.lake-data/DEP-E-20260712-VLM Probing/README.md`
- `.lake-data/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`

## Validation Notes

- Live `Delphoa/Black-Lake` README inspected at default-branch commit `cd1763795d659e9ef5effc6b0bd0ef00150ea5d3` before writing.
- Live `Delphoa-Labs/Black-Lake-Data` default branch verified at `a5617922963be56fc5a7d3172535cb3167146209`; its README was inspected before its DEP layout was used for dedup context.
- Public artifacts use repository-relative paths, public URLs, date-only markers, and withheld-local-context notes.
- No `.source/` directory was created because no source files were collected for redistribution.

## Attribution Block

- Source URL: https://arxiv.org/abs/2005.07310
  - Applies to: paper identity, version, authors, abstract, and primary source claims.
- Source URL: https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/6959_ECCV_2020_paper.php
  - Applies to: ECCV publication context and public paper access.
- Source URL: https://doi.org/10.1007/978-3-030-58539-6_34
  - Applies to: persistent publication identifier.
- Source URL: https://github.com/JizeCao/VALUE
  - Applies to: paper-declared code locator; unavailable during inspection.
