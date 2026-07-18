# 2026-07-18 - Arxiv DEP: Pixel-Point Transfer

- Actor/tool: Codex scheduled research workflow.
- Related DEP path: `.lake-data/DEP-E/DEP-E-20260718-Pixel Point Transfer/`.
- Action: Randomly selected, source-repaired, verified, reviewed, and synthesized *Learning from 2D: Contrastive Pixel-to-Point Knowledge Transfer for 3D Pretraining*.
- Inputs: Public arXiv, ar5iv, author-maintained publication, repository-authority, local source-integrity, and related-DEP evidence. Original source documents were withheld from publication.
- Outputs: `.reports/BL-Arxiv-Pixel-Point-Transfer-20260718/Report-Mark.md`, `.lake-data/DEP-E/DEP-E-20260718-Pixel Point Transfer/README.md`, `.lake-data/DEP-E/DEP-E-20260718-Pixel Point Transfer/pixel_point_transfer_manuscript.md`, and the DEP-E publication-index update.
- Outcome: Ready for repository validation and submission.
- Blockers: None. The official arXiv full-paper HTML response did not pass the document gate; the approved ar5iv fallback did.

## Random Selection and Deduplication

- Candidate enumeration: `rg --files -g "*.pdf"` over the local archive.
- Paper unit: Each unique PDF parent directory, with adjacent README, metadata, and source records used only to resolve identity.
- PDF candidates: 75,777.
- Candidate paper units: 75,776.
- Used primary arXiv IDs derived from Black Lake artifacts and automation memory: 384.
- Candidate units excluded because their derived arXiv ID was already used: 156.
- Candidate units excluded because no arXiv ID could be derived safely: 185.
- Locally eligible units after those filters: 75,435.
- Random method: PowerShell `Get-Random` rejection sampling over all unique paper units. This is uniform over the eligible set because every raw unit has equal draw probability and ineligible draws would be rejected.
- Selected zero-based raw index: 42,044.
- Draws: 1; duplicate rejections: 0; reselections: 0.
- Selected paper: *Learning from 2D: Contrastive Pixel-to-Point Knowledge Transfer for 3D Pretraining*.
- Selected identifier: `arXiv:2104.04687v3`; arXiv-issued DOI `10.48550/arXiv.2104.04687`.
- Exact-key validation: The arXiv ID, DOI, normalized title, and `Pixel-Point-Transfer` slug were absent from Black Lake `.logs`, `.reports`, and `.lake-data`, automation memory, and synthesized Black-Lake-Data entries.
- Metadata-only context: A Black Lake copy of the Black-Lake-Data author inventory contains the paper as an inventory row; it is not a prior review or DEP synthesis.
- Same-paper cutoff: No matching artifact or marker was found within the preceding 24 hours.

## Source Integrity Gate

- Initial state: Partial. The existing PDF was complete, but full-paper HTML was missing.
- Repair: Preserved the valid PDF, fetched metadata HTML and the source package, attempted official full-paper HTML once, and used one approved ar5iv full-paper fallback after the official response failed validation.
- PDF verification: 1,563,716 bytes; `%PDF-` header present; trailing `%%EOF` present; SHA-256 `e2c94c8525a96aef366fc431deca5a3f71f0a1a864914c2abdcaf8b8873e6b69`.
- Full-paper HTML verification: 273,704 bytes; 60,602 body characters; document marker present; 76 heading/section markers; six paper-structure terms; SHA-256 `219d8a2e7b90aa8a46f1b564400fd1ebcbb6363a1f7d2cda1c12d1a430f41147`.
- Metadata HTML: 43,765 bytes and treated as metadata only.
- Source package: 1,795,790 bytes, 21 readable entries, SHA-256 `94a0f3e7fea825358e58de392e38f30afbdf3729962460d415d99993f651c700`.
- Archive records updated: README, provenance JSON, machine-readable summary CSV, and verification report.
- Final state: Verified complete; zero `.part` files remained.
- Locality: PDF, full-paper HTML, abstract HTML, TeX/source, extracted content, caches, and verification records remained local. No source file or `.source/` directory was copied, staged, committed, attached, or posted.

## Evidence and Related DEP Validation

- Inspected evidence: arXiv v3 metadata, verified full paper, PDF, TeX/source package, pseudocode, supplementary material, tables, figures/captions, author-maintained publication page, and public related records.
- Venue status: The author page and arXiv record identify this as an arXiv preprint; no separate published DOI or official implementation repository was established.
- Exactly three related DEP entries were inspected:
  1. `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` - camera/BEV/point-cloud representation and 3D task transfer.
  2. `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md` - same-sample contrastive teacher/student alignment and relational distillation.
  3. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` - feature adaptation, joint latent modeling, and training-time geometry distillation.

## Next-Review Questions

1. Do PPKT gains persist on outdoor LiDAR or unseen indoor datasets when pretraining and fine-tuning scenes do not overlap?
2. How much of the benefit comes from pixel-point locality, the upsampling projection, the contrastive loss, or extra pretraining compute under matched budgets?
3. Can false negatives and calibration errors be measured when semantically equivalent pixels and points are treated as different contrastive instances?

## Challenges

1. The paper reports single-seed validation results and no released training repository, limiting independent reproduction.
2. Several narrative improvement values disagree with the displayed table arithmetic, so the tables were treated as authoritative and the discrepancies were preserved.
3. The aligned RGB-D and camera-intrinsic requirement narrows transferability and makes sensor calibration, occlusion, and depth quality part of the learning method.

## Submission Gate

- Allowed public scope: Generated Markdown under `.logs`, `.reports`, and `.lake-data` only.
- Forbidden source material: PDF, HTML, source archives, extraction caches, extracted source text, and local verification records.
- Required checks: manuscript schema, title/H1 equality and length, exact-three contracts, code syntax, DEP description length, publication-index uniqueness, final Attribution Blocks, URL coverage, public-leak scan, staged allowlist, and forbidden-extension scan.
