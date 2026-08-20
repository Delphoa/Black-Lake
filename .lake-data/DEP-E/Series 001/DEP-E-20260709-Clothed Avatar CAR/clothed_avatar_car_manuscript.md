---
title: "CAR Avatar - DEP-E"
generated_at: "2026-07-09 (public-safe date; exact local execution timestamp withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of arXiv:2304.03903, a single-image clothed avatar reconstruction method."
source_status: "URLs and temporary source inspection; no source files redistributed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-09"
temporal_cutoff: "Sources inspected through 2026-07-09."
primary_url: "https://arxiv.org/abs/2304.03903"
stable_identifier: "arXiv:2304.03903v1"
confidence_summary: "Medium-high for metadata, method, and reported metrics from arXiv/CVF/source TeX; lower for reproducibility because experiments were not rerun."
safety_scope: "research review, implementation planning, consent-aware synthetic examples"
distribution_notes: "No local archive paths or source files are redistributed."
---

# CAR Avatar - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv abstract page | Primary paper metadata | HTML | arXiv:2304.03903v1 | https://arxiv.org/abs/2304.03903 | Public arXiv metadata and abstract; redistribution license not treated as source-file permission. | 2026-07-09 | Inspected |
| S2 | arXiv API | Canonical metadata | Atom XML | arXiv:2304.03903v1 | https://export.arxiv.org/api/query?id_list=2304.03903 | Public metadata. | 2026-07-09 | Inspected |
| S3 | arXiv source package | Primary paper source | TeX/source package | arXiv:2304.03903v1 | https://arxiv.org/e-print/2304.03903 | Inspected temporarily; not redistributed. | 2026-07-09 | Inspected |
| S4 | CVF Open Access page | Venue metadata | HTML | CVPR 2023, pp. 8662-8672 | https://openaccess.thecvf.com/content/CVPR2023/html/Liao_High-Fidelity_Clothed_Avatar_Reconstruction_From_a_Single_Image_CVPR_2023_paper.html | CVF page states open access version; authors/copyright holders retain rights. | 2026-07-09 | Inspected |
| S5 | Official CAR repository | Official implementation | GitHub README | `TingtingLiao/CAR` | https://github.com/TingtingLiao/CAR | README inspected; license and usable checkpoint link not confirmed from inspected files. | 2026-07-09 | Inspected |
| S6 | Local arXiv archive metadata | Selection provenance | Readme/PDF presence | arXiv:2304.03903 | Local path withheld | Local source archive confirmed selected paper unit; no local file redistributed. | 2026-07-09 | Observed |
| S7 | Black-Lake README | Repository standard | Markdown | origin/main | Black-Lake/README.md | DEP, report, log, attribution, and commit-message standard. | 2026-07-09 | Inspected |
| S8 | Black-Lake-Data README | Related repository standard | Markdown | main branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related DEP layout and attribution standard. | 2026-07-09 | Inspected |
| S9 | SANE Embeddings DEP | Related DEP entry | Markdown | DEP-E-20260709-SANE Embeddings | Black-Lake/.lake-data/DEP-E/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md | Related conceptual source, not validation for CAR claims. | 2026-07-09 | Inspected |
| S10 | 2D-RC OTFS DEP | Related DEP entry | Markdown | DEP-E-20260709-2D-RC OTFS | Black-Lake/.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md | Related conceptual source, not validation for CAR claims. | 2026-07-09 | Inspected |
| S11 | Tech Intel 0105 DEP | Related DEP entry | Markdown | DEP-20260707-Tech Intel 0105 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260707-Tech%20Intel%200105/daily_research_findings_2026-07-07_0105.md | Related MRI reconstruction and reliability finding. | 2026-07-09 | Inspected |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S2 | arXiv metadata | Title, authors, arXiv ID/version, categories, posted date, abstract, PDF link. | Source identity and high-level contribution. | High | Abstract is not enough for empirical claims. |
| E2 | S3 | Primary source TeX | `main.tex`, abstract, related work, method, experiments, tables, conclusion, acknowledgements. | Method, datasets, reported metrics, hyper-network details, limitations. | High for source claims | TeX source was inspected temporarily; experiments were not reproduced. |
| E3 | S4 | Venue page | CVPR 2023 publication, page range, abstract, related material links. | Venue metadata and published status. | High | Does not independently validate metrics. |
| E4 | S5 | Official repo README | Installation dependencies, training command, inference command, citation. | Implementation and reproducibility boundary. | Medium | License and checkpoint links were not confirmed from inspected files. |
| E5 | S6 | Local archive metadata | Randomly selected paper unit had readme/PDF presence for arXiv:2304.03903. | Selection provenance. | Medium | Local path withheld; PDF not redistributed. |
| E6 | S7, S8 | Repository standards | DEP class, README, attribution, logs, reports, source handling. | Output format compliance. | High | Policy sources, not research evidence. |
| E7 | S9-S11 | Related DEP entries | Related reconstruction, alignment, and geometry-prior synthesis context. | Related-entry bridge. | Medium | Related entries do not validate CAR results. |

## Executive Summary

CAR is a CVPR 2023 method for reconstructing a high-fidelity clothed and animatable human avatar from a single RGB image. The central mechanism is a two-stage coarse-to-fine pipeline: a learning-based canonical implicit model recovers general shape in canonical space, and an optimization-based SDF refinement stage improves posed-space surface details using predicted normal images. The paper also uses a hyper-network to initialize the refinement network, reducing optimization iterations.

The inspected paper source reports quantitative comparisons on MVP-Human and RenderPeople against PIFu, PIFuHD, ICON, ARCH, and ARCH++. CAR reports the strongest Chamfer and P2S results across the main MVP-Human and RenderPeople canonical/posed settings and strong normal-error results, but those numbers are author-reported and not reproduced here. The official repository exists, but inspected README evidence did not confirm a license file or working checkpoint links.

The main Black-Lake value is the design pattern: reconstruction from sparse evidence improves when a model uses explicit structure. CAR uses SMPL, linear blend skinning, canonical normals, SDF losses, and hyper-network initialization as constraints around a fundamentally underdetermined single-image task.

## Detailed Summary

### Problem

Single-image clothed avatar reconstruction is underdetermined. A single RGB frame gives visible texture and silhouette, but it cannot directly observe the backside, occluded body parts, true cloth thickness, cloth folds, body shape under clothing, or a canonical geometry suitable for animation. The paper positions this as a practical alternative to expensive scanning systems, depth sensors, multi-camera studios, and video-based optimization pipelines.

### Background

The related-work section contrasts static clothed human reconstruction with avatar reconstruction. PIFu and PIFuHD use pixel-aligned implicit functions but can smooth high-frequency clothing details or struggle with out-of-distribution poses. Body-prior methods such as PaMIR, GeoPIFu, ICON, ARCH, and ARCH++ use parametric body information to improve robustness, but the paper argues that canonical normal cues are especially important for clothing detail and animation-ready reconstruction.

### Method

CAR first estimates front/back normal images and an SMPL body from the input image. Its canonical implicit model predicts a signed distance field in canonical space from pixel-aligned image features, canonical normal features, and canonical point position. The source argues that SDF training is more surface-aware than occupancy classification and more robust to mapping noise between posed and canonical spaces.

The second stage refines the surface in posed space. A coarse mesh is warped to posed space, and an SDF network is optimized so surface normals align with predicted front/back normal images. The hyper-network conditions on an SMPL body mesh and generates initial SDF network parameters, so optimization starts close to a human-body prior rather than from random parameters.

### Experiments

The inspected source reports training on 100 MVP-Human subjects and 50 RenderPeople subjects. The test set includes 50 MVP-Human scans, 11 RenderPeople scans, and real internet images. The paper compares with PIFu, PIFuHD, ICON, ARCH, and ARCH++ using Chamfer, P2S, and normal errors in canonical and posed space.

The main comparison table reports CAR with the best Chamfer and P2S values across MVP-Human canonical, MVP-Human posed, RenderPeople canonical, and RenderPeople posed settings. Reported CAR values include MVP-Canonical Chamfer 1.0572 and P2S 1.0811, MVP-Posed Chamfer 1.0771 and P2S 1.0654, RP-Canonical Chamfer 1.5401 and P2S 1.4963, and RP-Posed Chamfer 1.5142 and P2S 1.4147. The table reports normal error 0.0902 for MVP-Posed and 0.0821/0.0871 for RP-Canonical/RP-Posed.

### Limitations

The source reports qualitative robustness on real images, but reconstruction from a single image remains vulnerable to occlusion, backside hallucination, loose clothing ambiguity, pose estimation failures, and dataset bias. The official repository README lists old CUDA/Python/PyTorch dependencies and placeholder links for pretrained models and extra data. The experiments were not reproduced in this run.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | CAR reconstructs clothed avatars through a two-stage canonical implicit model plus posed-space normal refinement. | Author claim supported by method source | E2 | Directly supported by the source TeX method section. | High |
| C2 | The canonical model uses SDFs, pixel-aligned image features, canonical normals, and canonical point locations. | Author method claim | E2 | Directly supported by method equations and text. | High |
| C3 | The hyper-network initializes the SDF refinement network and reduces optimization iterations. | Author method/efficiency claim | E2 | Supported by method and inference-speed discussion; not independently timed. | Medium-high |
| C4 | CAR reports best main-table Chamfer and P2S scores across MVP-Human and RenderPeople canonical/posed settings. | Author empirical result | E2 | Supported by table source; not reproduced. | High for reporting, low for reproduced validity |
| C5 | Production use needs consent, uncertainty reporting, and identity-sensitive data controls. | Reviewer interpretation | E2, E7 | Inferred from single-image human reconstruction risks and related DEP reliability themes. | Medium |
| C6 | The selected paper was eligible because no prior same-paper Black Lake Arxiv DEP marker was found. | Process claim | E5, E6 | Supported by repository and memory scans for ID/title/slug markers. | High |

## Methodology

- `Research objective`: Randomly select one eligible local arXiv archive paper, review it source-first, and deposit a public-safe log, Report-Mark, and DEP-E manuscript in Black-Lake.
- `Sources inspected`: Local archive metadata, arXiv abstract page, arXiv API, arXiv source package, CVF Open Access page, official GitHub README, live Black-Lake README, live Black-Lake-Data README, and three related DEP entries.
- `Discovery strategy`: Enumerated local archive PDFs with `rg --files -g "*.pdf"`, grouped candidates by PDF parent directory, selected a uniform random index with `Get-Random`, derived arXiv ID from local metadata and filename, then cross-checked public arXiv/CVF/code sources.
- `Inclusion criteria`: Sources were included when they identified the paper, supported method/result/limitation notes, defined repository deposition rules, or provided concrete conceptual overlap for related synthesis.
- `Exclusion criteria`: Local absolute paths, exact local execution timestamps, source PDFs, TeX source files, and any unlicensed source copies were excluded from public artifacts. Experiments and code execution were excluded.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and DEP-ready provenance analysis.
- `Evidence handling`: Author metrics are reported as author claims tied to source evidence. Reviewer interpretations are labeled as interpretation and not presented as paper results.
- `Uncertainty handling`: Missing license/checkpoint evidence, unreproduced experiments, unused source-package files, and inability to inspect with local PDF tooling are stated directly.
- `Random selection`: The run used a uniform random index over 69,675 PDF-parent paper units. The zero-based selected index was 26,889. The accepted identifier was arXiv:2304.03903.
- `Deduplication and reselection validation`: The run scanned `.logs`, `.reports`, `.lake-data`, automation memory, and related Black-Lake-Data context for arXiv ID, normalized title, slug, DOI, and phrase markers. Duplicate markers found: 0. Same-paper 24-hour markers found: 0. Reselections: 0.

## Scope, Constraints, and Assumptions

- `Scope`: Review CAR as a selected Black-Lake Arxiv DEP paper and synthesize it with three related DEP entries about alignment, geometry-aware learning, and reconstruction reliability.
- `Temporal boundary`: Sources inspected on 2026-07-09; paper version is arXiv:2304.03903v1.
- `Evidence limits`: Experiments were not reproduced; no source files were redistributed; official repository license and checkpoint availability were not confirmed from inspected files; local PDF text extraction tooling was unavailable.
- `Assumptions`: The arXiv source package corresponds to the selected paper version and the local archive readme correctly identifies the selected PDF.
- `Constraints`: Public artifact text omits local absolute paths, home-directory names, usernames, machine identifiers, local timezone labels, and exact local execution timestamps.
- `Out of scope`: Re-running training, collecting datasets, copying model checkpoints, evaluating real human images, or building a production avatar pipeline.
- `Intended use`: DEP deposition, research review, implementation planning, and future reconstruction-system audit design.
- `Audience`: Black-Lake reviewers, computer vision researchers, 3D/graphics engineers, and product/security reviewers.
- `Reproducibility boundary`: A future reviewer can follow public URLs and repository-relative paths, but cannot reproduce CAR solely from this artifact.
- `Data sensitivity`: Human-image reconstruction is identity-sensitive; examples and implementations should use synthetic, consented, or user-owned inputs.

## Observations

- `Observed pattern`: CAR's main strength is structural decomposition: canonical shape, posed deformation, normals, SDF surfaces, and SMPL priors each carry a different part of the ambiguity.
- `Technical implication`: The method suggests that reconstruction pipelines should make priors and refinement loops explicit rather than hiding them inside one opaque predictor.
- `Evidence tension`: Strong visual and metric claims are useful, but reproducibility depends on code, checkpoints, data rights, and environment details that were not fully available from inspected sources.
- `Safety implication`: A single-image avatar system can create plausible geometry that the image did not actually evidence, which matters for consent, identity, and downstream misuse.
- `Reviewer hypothesis`: CAR-style pipelines would benefit from uncertainty maps that label where the surface is evidence-supported, prior-driven, or optimization-hallucinated.

## Considerations

CAR should be treated as research evidence, not a ready production system. The method can generate compelling avatars, but real-world use requires explicit consent, data retention policy, subject deletion controls, and quality warnings. The reviewed paper focuses on reconstruction quality and efficiency; it does not fully address governance for reconstructing people from arbitrary images.

The implementation stack also matters. The official README lists older dependencies and external assets such as SMPL models, pretrained models, and extra data. Without a confirmed license file, model links, and dataset access, a reproduction attempt may be blocked or legally constrained.

Evaluation should go beyond aggregate mesh metrics. For users, local failures around face, hands, hair, loose garments, occluded backs, assistive devices, and non-standard poses can matter more than average Chamfer distance.

## Strengths

- CAR combines learning speed with optimization detail instead of choosing only one paradigm.
- SDF representation gives a surface-aware formulation better aligned with high-fidelity geometry than raw occupancy classification.
- Canonical normals are a concrete geometric feature that targets clothing surface detail.
- The paper evaluates both canonical and posed reconstruction, which matches the avatar goal.
- The hyper-network initialization gives a practical efficiency argument for refinement-based reconstruction.

## Weaknesses

- Author-reported experiments were not reproduced in this run.
- Official repository evidence did not confirm license, checkpoint availability, or complete reproduction data.
- The paper's real-image evidence is mainly qualitative from inspected sources.
- Single-image reconstruction remains underdetermined and can hallucinate unobserved surfaces.
- The paper does not foreground consent, identity safety, fairness, or deployment governance.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add uncertainty maps | Reliability | Single-image reconstruction needs local confidence. | Better manual review and safer product use. | Requires uncertainty calibration. | Compare uncertainty against local reconstruction errors. |
| Publish complete reproduction bundle | Reproducibility | README alone leaves model/data/license gaps. | Higher independent confidence. | Asset licensing and maintenance burden. | Re-run main tables from clean environment. |
| Expand fairness evaluation | Evaluation | Clothing/body/camera diversity affects performance. | Better deployment boundary. | Requires representative consented datasets. | Stratified metrics and failure-case audits. |
| Add consent-aware pipeline design | Product safety | Human-avatar generation is identity-sensitive. | Reduces misuse and privacy risk. | Adds workflow friction. | User testing and policy review. |
| Separate visible versus inferred geometry | Interpretability | Reviewers need to know what the image supports. | More trustworthy outputs. | Requires evidence tracing from pixels to mesh regions. | Region-level provenance overlays. |

## Potential Implementations

1. `Synthetic Avatar Reconstruction Bench`
   - `User`: Vision researcher.
   - `Goal`: Evaluate CAR-style reconstruction concepts without real identity data.
   - `Core mechanism`: Render synthetic clothed humans from known meshes, reconstruct from one view, and compare region-level errors.
   - `Required inputs`: Synthetic meshes, rendered RGB/normal images, camera parameters, and ground-truth surfaces.
   - `Outputs`: Mesh metrics, uncertainty overlays, failure-case gallery, and evidence ledger.
   - `Risk controls`: Synthetic or fully consented data only; no public release of identity-sensitive images.
   - `Evaluation`: Region-level error, aggregate metrics, calibration, and manual review.

2. `Consent-Aware Avatar Capture`
   - `User`: Product team building user-owned avatars.
   - `Goal`: Let a user create an avatar while preserving consent, deletion, and quality controls.
   - `Core mechanism`: Gate processing behind consent records, avoid default retention, and show confidence warnings.
   - `Required inputs`: User-provided image, consent record, retention preference, and processing policy.
   - `Outputs`: Avatar file, audit manifest, quality report, and deletion handle.
   - `Risk controls`: No third-party images, no background faces, no hidden retention, and no source-image publication.
   - `Evaluation`: Consent completion, deletion verification, user correction rate, and failure audit.

3. `Geometry Prior Adapter`
   - `User`: Research engineer.
   - `Goal`: Reuse CAR's structural idea across reconstruction tasks.
   - `Core mechanism`: Provide adapters for priors, coordinate transforms, implicit fields, and refinement losses.
   - `Required inputs`: Prior model, coordinate map, observed features, SDF/normal losses, and optimizer settings.
   - `Outputs`: Reconstruction artifact, metrics, and provenance map.
   - `Risk controls`: Domain-specific safety review and source-license checks before data ingestion.
   - `Evaluation`: Ablation tests showing which prior improves which error mode.

## Three Ways to Exercise This Research

1. `Synthetic single-view test`: Objective: render one synthetic clothed figure from a known mesh, reconstruct with a toy implicit model or review existing outputs, and compare visible versus occluded errors. Inputs: synthetic mesh, one RGB render, one normal render, and ground truth. Method: compute region-level Chamfer or proxy metrics. Output: error map and notes. Success criterion: visible/occluded differences are explicit. Safety boundary: synthetic data only.
2. `Prior ablation review`: Objective: audit whether body priors, normals, and SDF losses address different failure modes. Inputs: paper tables, method sections, and synthetic examples. Method: map each design element to expected errors and missing ablations. Output: ablation checklist. Success criterion: every claimed improvement has a proposed validation. Safety boundary: no real subject images required.
3. `Consent workflow prototype`: Objective: design a public-safe intake manifest for avatar reconstruction. Inputs: user-owned image placeholder, consent fields, retention choice, and output references. Method: validate required fields before reconstruction. Output: JSON manifest and review note. Success criterion: no job runs without consent and deletion fields. Safety boundary: no non-consensual or third-party images.

## Example MVP Product

- `Product name`: Avatar Evidence Bench
- `Target user`: Computer vision reviewers and product safety engineers.
- `Problem`: Single-image avatar papers and prototypes can look plausible while hiding occlusion, consent, and reproduction gaps.
- `Core workflow`: Import paper metadata, record source evidence, run or attach synthetic reconstruction outputs, score visible/occluded regions, create consent-safe audit manifests, and export a DEP-ready review packet.
- `Data requirements`: Public paper metadata, synthetic meshes/renders, optional consented test images, source URLs, region labels, metrics, and reviewer notes.
- `Architecture`: Local CLI, source metadata parser, synthetic scene loader, reconstruction adapter interface, metric runner, uncertainty/region reporter, consent manifest validator, and Markdown exporter.
- `Success metrics`: Percentage of claims with evidence, region-level metric coverage, consent manifest pass rate, reproducibility blockers identified, and zero local-context leaks.
- `Risk controls`: Synthetic data by default, consent required for real images, no default retention, source-license checks, and sanitization scan before export.
- `Limitations`: MVP would not reproduce CAR without external assets and code; it would provide an evidence and safety scaffold around reconstruction review.
- `MVP boundary`: Local research/audit tool, not a public avatar-generation service.
- `Evaluation plan`: Schema validation, synthetic smoke tests, sanitization scans, and reviewer comparison against plain paper summaries.
- `Failure modes`: Incorrect metadata extraction, false confidence in synthetic-only tests, missing license constraints, and region labels that do not match user-perceived quality.

Minimal illustrative validator:

```python
def validate_avatar_audit(job):
    required = ["source_url", "input_kind", "consent", "retention", "outputs"]
    missing = [key for key in required if key not in job]
    if missing:
        return {"ok": False, "missing": missing}
    if job["input_kind"] == "real_person" and not job["consent"].get("explicit"):
        return {"ok": False, "missing": ["explicit consent"]}
    return {"ok": True, "warnings": job.get("quality_warnings", [])}
```

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| CAR paper | Primary paper | Reviewed work on single-image clothed avatar reconstruction. | https://arxiv.org/abs/2304.03903 |
| CVF CAR page | Venue metadata | CVPR 2023 publication and page range. | https://openaccess.thecvf.com/content/CVPR2023/html/Liao_High-Fidelity_Clothed_Avatar_Reconstruction_From_a_Single_Image_CVPR_2023_paper.html |
| Official CAR repository | Official implementation | Implementation and reproduction context. | https://github.com/TingtingLiao/CAR |
| SANE Embeddings DEP | Related DEP | Alignment and local reconstruction concepts. | Black-Lake/.lake-data/DEP-E/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md |
| 2D-RC OTFS DEP | Related DEP | Domain-geometry-aware learning. | Black-Lake/.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md |
| SA-RDM-DC MRI finding | Related DEP source basis | Reconstruction reliability and self-auditing context. | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260707-Tech%20Intel%200105/daily_research_findings_2026-07-07_0105.md |
| SA-RDM-DC source | Related arXiv paper | MRI reconstruction reliability source referenced by related DEP. | https://arxiv.org/abs/2607.02428 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2304.03903 | Selected paper metadata and abstract. | 2026-07-09 | Primary arXiv page. |
| R2 | https://export.arxiv.org/api/query?id_list=2304.03903 | Title, authors, version, categories, date metadata. | 2026-07-09 | arXiv API inspected. |
| R3 | https://doi.org/10.48550/arXiv.2304.03903 | Persistent identifier. | 2026-07-09 | DOI reference. |
| R4 | https://arxiv.org/e-print/2304.03903 | Method, experiments, tables, conclusion from source TeX. | 2026-07-09 | Source inspected temporarily; not redistributed. |
| R5 | https://openaccess.thecvf.com/content/CVPR2023/html/Liao_High-Fidelity_Clothed_Avatar_Reconstruction_From_a_Single_Image_CVPR_2023_paper.html | CVPR 2023 venue metadata and page range. | 2026-07-09 | CVF page inspected. |
| R6 | https://github.com/TingtingLiao/CAR | Official implementation README. | 2026-07-09 | README inspected; license/checkpoint not confirmed. |
| R7 | Local arXiv archive metadata, path withheld | Random selection provenance and PDF/readme presence. | 2026-07-09 | No local paths or files redistributed. |
| R8 | Black-Lake/README.md | Repository DEP/log/report rules. | 2026-07-09 | Live README inspected after fetch. |
| R9 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository DEP rules. | 2026-07-09 | README inspected. |
| R10 | Black-Lake/.lake-data/DEP-E/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md | Related DEP synthesis. | 2026-07-09 | Related artifact inspected. |
| R11 | Black-Lake/.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md | Related DEP synthesis. | 2026-07-09 | Related artifact inspected. |
| R12 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260707-Tech%20Intel%200105/daily_research_findings_2026-07-07_0105.md | Related MRI reconstruction finding. | 2026-07-09 | Related artifact inspected. |
| R13 | https://arxiv.org/abs/2607.02428 | Source basis for SA-RDM-DC MRI reconstruction finding. | 2026-07-09 | Referenced through related artifact. |

## Appendix

### Random Selection and Deduplication Record

- `Selection command class`: `rg --files -g "*.pdf"` over the local arXiv source archive.
- `Paper-unit rule`: each PDF parent directory counted as one paper unit.
- `Candidate count`: 69,675 paper units.
- `Random method`: uniform random index with PowerShell `Get-Random`.
- `Selected zero-based index`: 26,889.
- `Selected identifier`: arXiv:2304.03903.
- `Selected title`: High-Fidelity Clothed Avatar Reconstruction from a Single Image.
- `Duplicate scan targets`: `.logs`, `.reports`, `.lake-data`, automation memory, and related Black-Lake-Data context.
- `Duplicate markers found`: 0.
- `24-hour same-paper markers found`: 0.
- `Reselection count`: 0.
- `Source files collected into this DEP`: none.

### Source Inventory

- No `.source/` folder was created.
- No PDF, TeX package, repository checkout, model checkpoint, image, or dataset file is redistributed.
- Public URLs and repository-relative paths provide provenance.

### Validation Checklist

- Required manuscript headings are present.
- YAML `title` and H1 are identical and no more than 40 characters.
- `## Evidence Ledger` maps claims to inspected sources.
- `## Key Claims and Evidence` separates author claims from reviewer interpretation.
- `## Three Ways to Exercise This Research` contains exactly three entries.
- `## Example MVP Product` contains required product fields and safe illustrative code.
- Random selection methodology and dedup/reselection validation are included.
- Public artifacts avoid local absolute paths, usernames, machine names, local timezone labels, and exact local execution timestamps.
