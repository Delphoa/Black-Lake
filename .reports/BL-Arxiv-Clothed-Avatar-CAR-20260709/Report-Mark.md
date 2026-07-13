# Report-Mark: Clothed Avatar CAR

Run date: 2026-07-09

## Source Metadata

| Field | Value |
|---|---|
| Title | High-Fidelity Clothed Avatar Reconstruction from a Single Image |
| Authors | Tingting Liao, Xiaomei Zhang, Yuliang Xiu, Hongwei Yi, Xudong Liu, Guo-Jun Qi, Yong Zhang, Xuan Wang, Xiangyu Zhu, Zhen Lei |
| Identifier | arXiv:2304.03903v1 |
| DOI | https://doi.org/10.48550/arXiv.2304.03903 |
| Venue | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2023, pp. 8662-8672 |
| Primary URLs | https://arxiv.org/abs/2304.03903 ; https://openaccess.thecvf.com/content/CVPR2023/html/Liao_High-Fidelity_Clothed_Avatar_Reconstruction_From_a_Single_Image_CVPR_2023_paper.html |
| Official code | https://github.com/TingtingLiao/CAR |
| Source status | Local archive metadata observed; arXiv source inspected temporarily; no source files redistributed. |
| Access date | 2026-07-09 |

## Concise Research Notes

CAR addresses single-image clothed avatar reconstruction. The problem is difficult because a single RGB image underdetermines 3D shape, clothing surface detail, occluded body regions, and animation-ready canonical geometry. The paper combines learning-based canonical reconstruction with optimization-based surface refinement.

The first stage predicts a canonical implicit surface using pixel-aligned image features, canonical normal features, and canonical point coordinates. The authors use a signed distance function rather than an occupancy classifier, arguing that SDF training is more robust to pose-to-canonical mapping noise and surface-level reconstruction. The second stage refines the posed-space surface with another SDF network supervised by predicted front/back normal images. A hyper-network generates initialization parameters for that optimization network from an SMPL body mesh, reducing the iteration count reported for refinement.

The inspected source reports training on 100 MVP-Human subjects and 50 RenderPeople subjects, with tests on 50 MVP-Human scans, 11 RenderPeople scans, and internet images. CAR is compared with PIFu, PIFuHD, ICON, ARCH, and ARCH++. In the main comparison table, CAR reports the best Chamfer and P2S scores across MVP-Human and RenderPeople canonical/posed settings, and the best normal scores in posed MVP and both RenderPeople settings. The source reports about 5 minutes per subject on one TITAN X GPU, compared with several hours for optimization-heavy alternatives.

The review treats those metrics as reported author results, not reproduced findings. No local source files were deposited, and no `.source/` folder was created.

## Evidence and Attribution

| ID | Source | Evidence Used | Supports | Confidence | Limitation |
|---|---|---|---|---|---|
| E1 | arXiv API and abstract page | Title, authors, arXiv version, categories, abstract, posted date. | Identity and high-level contribution. | High | Abstract is incomplete evidence for results. |
| E2 | arXiv source package | `main.tex`, abstract, related work, method, experiment, tables, conclusion. | Method, datasets, metrics, limitations, and source structure. | High | Source was inspected temporarily and not redistributed. |
| E3 | CVF Open Access page | CVPR venue, page range, abstract, related material links. | Published venue metadata. | High | CVF page is metadata and abstract, not full independent validation. |
| E4 | Official GitHub README | Installation requirements, training/inference commands, citation. | Code availability and implementation boundary. | Medium | License and pretrained model links were not available from inspected files. |
| E5 | Black-Lake README | DEP classes, file placement, attribution, commit-message standard. | Output format and repository compliance. | High | Repository policy, not paper evidence. |
| E6 | Black-Lake-Data README | Related repository DEP expectations. | Related-entry context. | High | Repository policy, not paper evidence. |
| E7 | Related DEP entries | SANE, 2D-RC OTFS, and SA-RDM-DC MRI reconstruction context. | Synthesis bridge. | Medium | Related sources were not re-reviewed as primary claims for CAR. |

## Related DEP Entries

1. `Black-Lake/.lake-data/DEP-E/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md`
   - Relevance: SANE uses local reconstruction weights and alignment between attribute and topology neighborhoods. CAR similarly aligns image features, body priors, normals, and canonical geometry to recover missing structure.
   - Source basis: Repository manuscript for arXiv:1804.07152.

2. `Black-Lake/.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md`
   - Relevance: 2D-RC encodes known domain geometry into a learner through delay-Doppler structure. CAR encodes human-body geometry through SMPL, linear blend skinning, canonical normals, and SDF constraints.
   - Source basis: Repository manuscript for arXiv:2311.08543.

3. `Black-Lake-Data/.lake-data/DEP-20260707-Tech Intel 0105/daily_research_findings_2026-07-07_0105.md`
   - Relevance: The SA-RDM-DC MRI finding is another reconstruction-from-partial-observation system, with reliability/error outputs as a deployment concern. CAR has analogous need for uncertainty maps around occlusion, loose clothing, and identity-sensitive reconstruction.
   - Source basis: Daily finding referencing https://arxiv.org/abs/2607.02428.

## Synthesis Note

### Concept Bridge

CAR is best read as a geometry-guided reconstruction system. It does not ask a generic network to infer a full clothed body from pixels alone. Instead, it carries the image into a structured space: SMPL gives a coarse human prior, linear blend skinning links posed and canonical coordinates, canonical normals carry surface orientation, SDF losses make the representation surface-aware, and a hyper-network initializes optimization. The related DEP entries share that pattern: SANE aligns separate relation spaces, 2D-RC encodes channel geometry, and SA-RDM-DC adds reconstruction reliability signals.

### Potential Implementations

1. Avatar reconstruction audit bench: build a local synthetic evaluation harness that compares reconstructed mesh metrics, occlusion regions, and surface-normal consistency without using real identity images.
2. Consent-first avatar capture workflow: wrap reconstruction around user-provided images, explicit consent records, deletion controls, and visible uncertainty warnings.
3. Geometry-prior adapter library: expose reusable abstractions for combining priors, implicit fields, and refinement loops across vision reconstruction tasks.

### Deeper Relationship Observations

1. CAR and 2D-RC both show that architectural priors can reduce sample burden when observations are sparse or ambiguous.
2. CAR and SANE both use alignment across representational spaces; failure occurs when the spaces are forced together without reliable correspondence.
3. CAR and SA-RDM-DC both need reliability outputs because high-quality aggregate reconstruction can hide severe local failures.

### Conceptual Similarities

1. Partial observation recovery: single RGB images, corrupted time series, undersampled MRI, and sparse graph views all require inference beyond direct measurements.
2. Structured priors: SMPL, topology neighborhoods, delay-Doppler structure, and k-space consistency all constrain otherwise underdetermined learning.
3. Reviewable uncertainty: each system benefits from explicit evidence about what was seen, inferred, optimized, and potentially wrong.

### MVP Implementations With Code Mock-Ups

1. Mesh review manifest generator:

```python
def build_mesh_review_manifest(paper_id, sources, metrics):
    return {
        "paper_id": paper_id,
        "sources": [s for s in sources if s["public"]],
        "metric_claims": metrics,
        "local_paths": "withheld",
        "needs_reproduction": True,
    }
```

2. Consent-aware reconstruction job record:

```python
def avatar_job_record(image_id, consent_id, output_refs):
    if not consent_id:
        raise ValueError("consent record required")
    return {
        "image_id": image_id,
        "consent_id": consent_id,
        "outputs": output_refs,
        "retention": "user-controlled",
    }
```

3. Reconstruction uncertainty queue:

```python
def route_uncertain_regions(regions, threshold=0.35):
    return [
        {"region": r["name"], "action": "manual_review"}
        for r in regions
        if r["uncertainty"] >= threshold
    ]
```

### Developer Challenges

1. Reproducing CAR requires old CUDA/PyTorch-style dependencies, SMPL assets, model checkpoints, and data access that are not fully resolved by the inspected README.
2. Production use must prevent silent reconstruction of non-consenting subjects and avoid storing identity-sensitive inputs by default.
3. Quality metrics must report local failures around occlusion, loose garments, hands, hair, and backside hallucination rather than only aggregate mesh scores.

### Author Challenges

1. Publish a clearly licensed, checkpoint-complete, dataset-documented reproduction path.
2. Add uncertainty maps or failure classifiers for regions where the single image provides weak evidence.
3. Evaluate fairness and robustness across body types, clothing styles, mobility aids, camera viewpoints, and cultural clothing variation.

## Validation Notes

- The selected paper was accepted after scanning repository artifacts and automation memory for arXiv ID, normalized title, slug, and key phrases.
- No prior same-paper Black Lake Arxiv DEP was found.
- No same-paper marker appeared inside the 24-hour exclusion window.
- The arXiv source package contained unused adjacent files; included files were checked through `main.tex`.
- The public artifacts omit local absolute paths, home directories, usernames, machine names, local timezone labels, and exact local execution timestamps.
- No source files are redistributed.

## Attribution Block

- Source URL: https://arxiv.org/abs/2304.03903
  - Applies to: Report-Mark and DEP manuscript.
  - Notes: Primary arXiv metadata and abstract for the selected paper.
- Source URL: https://export.arxiv.org/api/query?id_list=2304.03903
  - Applies to: Report-Mark and DEP manuscript.
  - Notes: Canonical arXiv API metadata for title, authors, version, categories, and dates.
- Source URL: https://arxiv.org/e-print/2304.03903
  - Applies to: Report-Mark and DEP manuscript.
  - Notes: Public arXiv source package inspected temporarily; not redistributed.
- Source URL: https://openaccess.thecvf.com/content/CVPR2023/html/Liao_High-Fidelity_Clothed_Avatar_Reconstruction_From_a_Single_Image_CVPR_2023_paper.html
  - Applies to: Report-Mark and DEP manuscript.
  - Notes: CVPR 2023 venue metadata, page range, abstract, and related material links.
- Source URL: https://github.com/TingtingLiao/CAR
  - Applies to: implementation and reproducibility notes.
  - Notes: Official repository README inspected through GitHub.
- Source reference: Black-Lake/README.md
  - Applies to: repository format and deposition rules.
  - Notes: Live README inspected after fetch.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related DEP context rules.
  - Notes: Live related repository README inspected.
- Source reference: Black-Lake/.lake-data/DEP-E/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md
  - Applies to: related DEP synthesis.
  - Notes: Related artifact inspected as conceptual context.
- Source reference: Black-Lake/.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md
  - Applies to: related DEP synthesis.
  - Notes: Related artifact inspected as conceptual context.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260707-Tech%20Intel%200105/daily_research_findings_2026-07-07_0105.md
  - Applies to: related DEP synthesis.
  - Notes: Related daily research finding for SA-RDM-DC MRI reconstruction.
