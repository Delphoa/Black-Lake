# Arxiv DEP Job Log: Clothed Avatar CAR

Run date: 2026-07-09

## Selected Paper

- Title: High-Fidelity Clothed Avatar Reconstruction from a Single Image
- arXiv ID: 2304.03903v1
- Public URL: https://arxiv.org/abs/2304.03903
- Venue reference: CVPR 2023, pp. 8662-8672
- Paper slug: Clothed-Avatar-CAR

## Selection Method

- Enumerated local archive PDFs with `rg --files -g "*.pdf"`.
- Treated each PDF parent directory as one paper unit.
- Selected uniformly with PowerShell `Get-Random`.
- Candidate paper-unit count: 69,675.
- Zero-based random index: 26,889.
- Accepted paper unit identifier: arXiv:2304.03903.

## Deduplication and Exclusions

- Duplicate scan targets: `.logs`, `.reports`, `.lake-data`, automation memory, and related Black-Lake-Data context.
- Duplicate keys scanned: `2304.03903`, normalized title, `High-Fidelity Clothed Avatar Reconstruction`, `clothed-avatar`, `avatar reconstruction`, and `CAR`.
- Prior same-paper artifact markers found: 0.
- Same-paper 24-hour markers found: 0.
- Reselections required: 0.
- Source files collected into the DEP: 0.

## Outputs

- Job log: `.logs/20260709-Arxiv-Clothed-Avatar-CAR-LOG.md`
- Report-Mark: `.reports/BL-Arxiv-Clothed-Avatar-CAR-20260709/Report-Mark.md`
- DEP README: `.lake-data/DEP-E/DEP-E-20260709-Clothed Avatar CAR/README.md`
- DEP manuscript: `.lake-data/DEP-E/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md`

## Sources Inspected

- Local archive readme and PDF presence for arXiv:2304.03903; local paths withheld.
- arXiv abstract/API/source bundle for arXiv:2304.03903.
- CVF Open Access page for the CVPR 2023 proceedings entry.
- Official GitHub README for `TingtingLiao/CAR`.
- Live `Delphoa/Black-Lake` README and `Delphoa-Labs/Black-Lake-Data` README.
- Three related DEP entries listed in the Report-Mark and manuscript.

## Next-Review Questions

1. Can the official CAR repository be made reproducible despite missing visible license and placeholder model links?
2. How much of CAR's reported gain comes from canonical normal features versus the hyper-network initialization?
3. What privacy and consent controls are needed before single-image avatar reconstruction is used on real people?

## Challenges

1. PDF text tooling was unavailable locally, so the review relied on arXiv source TeX, arXiv metadata, CVF metadata, and official repository text.
2. The arXiv source package contained extra unused files from adjacent work, so included LaTeX sections were checked against `main.tex`.
3. Source files were not redistributed because no clear source redistribution license was confirmed for the paper package or code repository.
