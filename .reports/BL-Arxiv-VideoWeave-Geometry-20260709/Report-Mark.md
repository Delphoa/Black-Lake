# Report-Mark: VideoWeave Geometry

Run date: 2026-07-09

## Source Metadata

| Field | Value |
|---|---|
| Paper title | VideoWeave: Unlocking Geometric Consistency in Video Generation via Joint Geometry-Video Modeling |
| Authors | Xunzhi Xiang, Zixuan Duan, Yabo Chen, Zhengxuan Wei, Guiyu Zhang, Zixiao Gu, Zhe Gao, Haibin Huang, Chi Zhang, Qi Fan, Xuelong Li |
| arXiv ID | 2606.14162 |
| DOI | https://doi.org/10.48550/arXiv.2606.14162 |
| Submitted | 2026-06-12 |
| Primary URLs | https://arxiv.org/abs/2606.14162 ; https://arxiv.org/html/2606.14162 |
| Project page | https://videoweave.github.io/ |
| Local archive metadata | PDF filename `2606.14162.pdf` and nearby README metadata were inspected; no local paths are published. |
| Source files collected | None |
| Access date | 2026-07-09 |

## Concise Research Notes

VideoWeave targets a failure mode in large-scale video diffusion models: temporally plausible frames can still drift geometrically under camera motion, viewpoint changes, and longer horizons. The paper argues that explicit geometry guidance through depth maps, point clouds, reconstructed 3D structures, supervision targets, or reward signals can propagate upstream reconstruction errors and add expensive geometry pipelines.

The proposed alternative is a latent-space post-training framework. VideoWeave adapts implicit geometry-model features into geometry latents, jointly denoises geometry and video latents in a shared diffusion space, then distills the resulting joint score field into a compact generator. At inference, the geometry latent is discarded; the generated video latent is expected to carry the distilled geometry-aware prior.

The authors introduce GeoVid-80K, an 80K-video dataset with paired appearance and geometry representations. The inspected HTML reports evaluations for text-to-video and image-to-video settings, with metrics covering VBench quality, 3D reconstruction consistency, and epipolar consistency. Reported results show VideoWeave-T2V improving PSNR to 21.4994 and inlier rate to 0.7068 in Table 1, and VideoWeave-I2V improving PSNR to 21.1826 and inlier rate to 0.7788 in Table 2. Ablations support the learnable adapter, joint modeling, and score-distillation stages as material contributors.

## Evidence and Attribution

| ID | Evidence | Supports | Notes |
|---|---|---|---|
| E1 | arXiv abstract page for 2606.14162 | Title, authors, submission date, arXiv ID, DOI, abstract, project page link | Primary public metadata |
| E2 | arXiv HTML full text | Method, dataset construction, evaluation protocol, quantitative tables, ablations, conclusion | Primary full-text evidence |
| E3 | VideoWeave project page | Public summary, overview, qualitative-results framing | Author/project context |
| E4 | Local archive README metadata | Confirms selected paper identity and archive unit | Metadata only; no local paths published |
| E5 | Black-Lake and Black-Lake-Data scans | Deduplication and related-entry selection | Repository context |

## Related DEP Entries

1. `Delphoa/Black-Lake/.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md`
   - Relevance: This processed Black-Lake artifact includes WorldDirector and frames persistent dynamic object memory as a first-class state object in world simulation. VideoWeave addresses a neighboring problem: transferring geometry-aware priors into video generation so spatial structure remains coherent over time.
   - Source basis: Inspected artifact sections on source metadata, evidence ledger, detailed summary, and related reading.

2. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md`
   - Relevance: The visual world-model hallucination finding treats world-model failure as a coverage and evaluation problem. VideoWeave similarly treats apparent visual quality as insufficient unless geometric and epipolar consistency are measured.
   - Source basis: Inspected finding titled "Predictable and Preventable Hallucination in Visual World Models."

3. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260625-Tech Intel 1446/daily_research_findings_2026-06-25_1446.md`
   - Relevance: The HoloAgent-0 finding connects robot control loops to 3D spatial memory. VideoWeave is not a robot-control paper, but its focus on stable geometry across viewpoint and time is directly adjacent to embodied agents that need persistent spatial representations.
   - Source basis: Inspected finding titled "HoloAgent-0 connects robot control loops to 3D spatial memory."

## Synthesis Note

### Concept Bridge

VideoWeave bridges generative video modeling and world-model reliability by moving geometry from an explicit reconstruction artifact into a training-time latent companion. The related DEP entries show the same pressure from adjacent angles: persistent state for world simulation, coverage-aware hallucination evaluation, and embodied 3D spatial memory. The common review object is not video quality alone; it is whether a system preserves spatial state across time, occlusion, viewpoint shift, and downstream action.

### Potential Implementations

1. Geometry-aware video generation review harness: compare generated clips with reconstruction and epipolar metrics before accepting them as world-model evidence.
2. Embodied-agent simulation filter: reject or flag generated simulation segments whose inferred scene geometry drifts under planned camera or robot motion.
3. Source-grounded media DEP workflow: attach geometry-consistency summaries to generated visual artifacts so Black-Lake reviews can distinguish visual fidelity from spatial reliability.

### Deeper Relationship Observations

1. VideoWeave and the visual world-model hallucination entry both challenge appearance-only evaluation; one uses geometry metrics, while the other uses coverage and hallucination diagnostics.
2. VideoWeave and WorldDirector differ in mechanism but share a persistent-scene goal: stable object and layout identity across camera movement and time.
3. VideoWeave and HoloAgent-0 point toward a broader embodied-AI requirement: spatial memory must be both generatable and actionable, not just visually pleasing.

### Conceptual Similarities

1. All three related entries treat state as something that must persist beyond one generated frame, response, or action.
2. All three separate domain structure from generic model capability, whether through geometry latents, object memory, coverage diagnostics, or 3D spatial memory.
3. All three imply that deployment needs task-specific validation signals rather than generic aggregate quality scores.

### MVP Implementations with Code Mock-ups

1. Geometry metric gate:

```python
def accept_clip(metrics):
    return (
        metrics["psnr"] >= 20.0
        and metrics["epipolar_error"] <= 8.0
        and metrics["inlier_rate"] >= 0.65
    )
```

2. Spatial drift audit row:

```python
def drift_row(clip_id, before, after):
    return {
        "clip_id": clip_id,
        "layout_delta": round(abs(after["layout"] - before["layout"]), 4),
        "object_delta": round(abs(after["objects"] - before["objects"]), 4),
        "needs_review": abs(after["layout"] - before["layout"]) > 0.15,
    }
```

3. Source-first media record:

```python
def media_record(arxiv_id, dep_path, evidence_ids):
    return {
        "source": f"https://arxiv.org/abs/{arxiv_id}",
        "dep_path": dep_path,
        "evidence": evidence_ids,
        "source_files_collected": False,
    }
```

### Developer Challenges

1. Reproducing the paper requires code, dataset release terms, and substantial video-generation compute that were not available in this run.
2. Geometry metrics can be expensive and brittle if the reconstruction pipeline fails on stylized or low-texture generated videos.
3. Integrating geometry-aware generation into products requires guardrails around synthetic media provenance and overconfident simulation use.

### Author Challenges

1. Release enough of GeoVid-80K, filtering code, and training configuration to let outside reviewers distinguish dataset contribution from modeling contribution.
2. Report more failure cases for dynamic scenes, occlusion, long-horizon camera motion, and geometry-estimator mismatch.
3. Clarify licensing and reuse boundaries for the curated dataset, project examples, and any future model artifacts.

## Validation Notes

- Required random selection method was used and recorded without publishing local paths.
- Deduplication searched arXiv ID, title, and slug markers in Black-Lake, Black-Lake-Data context, and automation memory.
- No prior same-paper artifact was found; no reselection was needed.
- The report cites exactly three related entries with concrete conceptual overlap.
- Source files were not collected into the DEP; no `.source/` directory is used.
- Public artifact text was checked to avoid local absolute paths, usernames, private filesystem roots, local timezone labels, and exact local execution timestamps.

## Attribution Block

- Source URL: https://arxiv.org/abs/2606.14162
  - Applies to: Report-Mark and DEP manuscript.
  - Notes: Primary arXiv metadata, abstract, DOI, and source links for VideoWeave.
- Source URL: https://arxiv.org/html/2606.14162
  - Applies to: Report-Mark and DEP manuscript.
  - Notes: Primary full-text source for method, dataset, experiments, results, ablations, and conclusion.
- Source URL: https://videoweave.github.io/
  - Applies to: Report-Mark and DEP manuscript.
  - Notes: Official project page used for author-provided overview and qualitative framing.
- Repository path: Delphoa/Black-Lake/.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md
  - Applies to: related DEP synthesis.
  - Notes: Existing processed Black-Lake artifact with WorldDirector and state-review context.
- Repository path: Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md
  - Applies to: related DEP synthesis.
  - Notes: Existing source package entry on visual world-model hallucination and coverage diagnostics.
- Repository path: Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260625-Tech Intel 1446/daily_research_findings_2026-06-25_1446.md
  - Applies to: related DEP synthesis.
  - Notes: Existing source package entry on HoloAgent-0 and 3D spatial memory.
