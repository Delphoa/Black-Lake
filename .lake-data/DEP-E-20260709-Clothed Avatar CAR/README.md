# DEP-E-20260709-Clothed Avatar CAR

#computer-vision #avatar-reconstruction #implicit-surfaces #single-image-reconstruction #research-review

Public-safe context: This DEP-E entry preserves a source-first research manuscript for arXiv:2304.03903, "High-Fidelity Clothed Avatar Reconstruction from a Single Image." Local archive paths, local execution timestamps, usernames, machine identifiers, and source files are withheld. No `.source/` folder is included.

## Contents

- `README.md` - DEP manifest, item summary, relevance note, and attribution block.
- `clothed_avatar_car_manuscript.md` - Schema-complete manuscript research artifact for the selected paper.

## Summary of Items

- `README.md`: Documents the DEP entry, public-safe context, file inventory, source policy, and attribution.
- `clothed_avatar_car_manuscript.md`: Reviews the CAR paper, records source metadata, evidence ledger, selection/dedup methodology, related DEP synthesis, implementation ideas, and validation notes.

## Insights and Relevance

CAR is relevant to Black-Lake because it is a compact example of geometry-guided reconstruction from sparse evidence. The paper combines SMPL priors, canonical normals, signed distance fields, and optimization refinement to recover a clothed avatar from one RGB image. That design pattern connects to other Black-Lake themes: structured priors can make learning more data-efficient, but the result must remain reviewable because reconstruction systems can hallucinate details and carry identity or consent risks.

## Attribution Block

- Source URL: https://arxiv.org/abs/2304.03903
  - Applies to: `clothed_avatar_car_manuscript.md`
  - Notes: Primary arXiv abstract and metadata for the selected paper.
- Source URL: https://export.arxiv.org/api/query?id_list=2304.03903
  - Applies to: `clothed_avatar_car_manuscript.md`
  - Notes: Canonical arXiv API metadata for title, authors, arXiv version, categories, and dates.
- Source URL: https://doi.org/10.48550/arXiv.2304.03903
  - Applies to: `clothed_avatar_car_manuscript.md`
  - Notes: Persistent arXiv DOI reference.
- Source URL: https://arxiv.org/e-print/2304.03903
  - Applies to: `clothed_avatar_car_manuscript.md`
  - Notes: Public arXiv source package inspected temporarily; not redistributed.
- Source URL: https://openaccess.thecvf.com/content/CVPR2023/html/Liao_High-Fidelity_Clothed_Avatar_Reconstruction_From_a_Single_Image_CVPR_2023_paper.html
  - Applies to: `clothed_avatar_car_manuscript.md`
  - Notes: CVPR 2023 Open Access metadata, page range, abstract, and related material links.
- Source URL: https://github.com/TingtingLiao/CAR
  - Applies to: `clothed_avatar_car_manuscript.md`
  - Notes: Official code repository README inspected; no license file or checkpoint link was confirmed from inspected files.
- Source reference: Black-Lake/README.md
  - Applies to: `README.md`, `clothed_avatar_car_manuscript.md`
  - Notes: Live repository deposition standard inspected after fetch.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `README.md`, `clothed_avatar_car_manuscript.md`
  - Notes: Related DEP repository standard inspected.
- Source reference: Black-Lake/.lake-data/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md
  - Applies to: `clothed_avatar_car_manuscript.md`
  - Notes: Related DEP entry used for conceptual synthesis.
- Source reference: Black-Lake/.lake-data/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md
  - Applies to: `clothed_avatar_car_manuscript.md`
  - Notes: Related DEP entry used for conceptual synthesis.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260707-Tech%20Intel%200105/daily_research_findings_2026-07-07_0105.md
  - Applies to: `clothed_avatar_car_manuscript.md`
  - Notes: Related DEP entry used for MRI reconstruction and reliability-context synthesis.
