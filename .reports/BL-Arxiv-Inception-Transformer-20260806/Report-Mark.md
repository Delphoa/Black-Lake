# Report-Mark: Inception Transformer

## Source Metadata

- `Full title`: *Inception Transformer*.
- `Authors`: Chenyang Si; Weihao Yu; Pan Zhou; Yichen Zhou; Xinchao Wang; Shuicheng Yan.
- `Source version`: arXiv:2205.12956v2; PDF footer dated 2022-05-26; metadata page records 2022-05-25 submission and 2022-05-26 online date.
- `Stable DOI`: [10.48550/arXiv.2205.12956](https://doi.org/10.48550/arXiv.2205.12956).
- `Primary record`: [arXiv abstract/metadata](https://arxiv.org/abs/2205.12956).
- `Full-paper source`: [ar5iv HTML](https://ar5iv.labs.arxiv.org/html/2205.12956), used as the approved full-paper fallback after [official arXiv HTML](https://arxiv.org/html/2205.12956) returned 404 during repair.
- `Official implementation`: [sail-sg/iFormer](https://github.com/sail-sg/iFormer), inspected at commit [725d8e7f](https://github.com/sail-sg/iFormer/commit/725d8e7f455b5e17be20788b9bcd6c6c505c4be0).
- `Local source state`: complete PDF and full-paper HTML were repaired and verified in the private archive; metadata HTML was retained; the TeX/source package was unavailable. No source file, cache, extracted text, or repair receipt was deposited.

## Research Notes

The paper proposes iFormer as a general vision backbone that explicitly splits visual channels into high- and low-frequency paths. The high-frequency path uses depthwise convolution and max-pooling; the low-frequency path uses pooled multi-head self-attention and then restores spatial resolution. A depthwise-convolution fusion layer recombines the paths. The frequency-ramp structure decreases the high-frequency channel share and increases the low-frequency share from shallow to deep stages.

The reported ImageNet-1K 224px results are 83.4% top-1 for iFormer-S at 20M parameters and 4.8G FLOPs, 84.6% for iFormer-B at 48M/9.4G, and 84.8% for iFormer-L at 87M/14.0G. The paper also reports iFormer-S at 46.2 box AP and 41.9 mask AP on COCO with Mask R-CNN, and 48.6 mIoU on ADE20K with Semantic FPN. Its ablation moves from 80.8% top-1 for attention-only to 81.2% with attention, max-pooling, and depthwise convolution under slightly lower reported compute.

The strongest interpretation is architectural: locality and global context can be allocated to different channel groups and recombined with a smaller attention burden. The results remain author-reported. The review did not reproduce training or inference, and the paper itself identifies manually selected frequency-ramp ratios and lack of ImageNet-21K training as limitations.

## Evidence and Attribution

| ID | Evidence | Supports | Assessment |
|---|---|---|---|
| E1 | [arXiv metadata](https://arxiv.org/abs/2205.12956) | Identity, authors, dates, abstract, arXiv ID | High for source identity; metadata alone is not enough for empirical claims |
| E2 | [Full-paper HTML fallback](https://ar5iv.labs.arxiv.org/html/2205.12956) and [arXiv PDF](https://arxiv.org/pdf/2205.12956) | Inception mixer, frequency ramp, methods, tables, figures, ablations, conclusion, limitations | High for transcription; no independent reproduction |
| E3 | [Official README](https://github.com/sail-sg/iFormer/blob/725d8e7f455b5e17be20788b9bcd6c6c505c4be0/README.md) | Dependencies, training/validation commands, checkpoints/config links, headline metrics | Medium because commands and artifacts were not run |
| E4 | [Official model implementation](https://github.com/sail-sg/iFormer/blob/725d8e7f455b5e17be20788b9bcd6c6c505c4be0/models/inception_transformer.py) | Channel split, high/low mixers, pooled attention, fusion, four-stage backbone | High for implementation surface; environment compatibility not tested |
| E5 | [Apache License](https://github.com/sail-sg/iFormer/blob/725d8e7f455b5e17be20788b9bcd6c6c505c4be0/LICENSE) | Public code license visibility | High for the inspected repository license; checkpoint/data terms still require separate review |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` — direct conceptual overlap: image-domain and Fourier-domain filters are evaluated as alternatives to attention in compact vision backbones. Source basis: [arXiv:2407.12217](https://arxiv.org/abs/2407.12217).
2. `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md` — downstream overlap: a structured visual representation is converted into oriented detection outputs, making spatial priors and failure boundaries relevant to iFormer transfer. Source basis: [arXiv:2506.10601](https://arxiv.org/abs/2506.10601).
3. `.lake-data/DEP-E/DEP-E-20260728-HeightFormer Learning/heightformer_learning_manuscript.md` — architecture/task overlap: transformer attention is localized into height sequences for efficient visual 3D detection. Source basis: [arXiv:2503.10777](https://arxiv.org/abs/2503.10777).

## Synthesis Note

### Concept Bridge

iFormer’s main bridge is a representation-allocation rule: use local operators where high-frequency detail is useful, use reduced-resolution attention where global context is useful, and make the allocation change with depth. That rule connects naturally to compact spectral mixers, structured spatial supervision, and localized geometric attention. The bridge is useful for system design, but it is a reviewer interpretation rather than a new result established by the paper.

#### Exactly Three Potential Implementations

1. **Dual-path vision backbone registry** — expose iFormer, attention-only, convolution-only, and AFIDAF-style mixers behind one interface with matched widths, FLOPs, training schedule, and seed manifest.
2. **Frequency-aware dense-task adapter** — reuse the high/low feature streams as inputs to detection or segmentation heads, logging which branch contributes to edges, small objects, and boundaries.
3. **Local deployment evidence card** — package model/config hashes, latency distributions, memory, energy, operator support, accuracy, and failure slices into a public-safe comparison record.

#### Exactly Three Deeper Relationship Observations

1. The frequency ramp, AFIDAF’s dual-domain alternation, and HeightFormer’s local height sequences all make a global operator cheaper by restricting where or how it acts.
2. SSP shows that a structured representation can improve downstream detection only within explicit spatial assumptions; iFormer should therefore be tested on boundary, overlap, and texture-shift slices rather than headline averages alone.
3. The recurring design pattern is not “attention versus convolution” but “allocate inductive bias by scale, location, or channel group, then measure the handoff.”

#### Exactly Three Conceptual Similarities

1. All four artifacts treat heterogeneous feature paths as a way to preserve complementary information that a single uniform mixer can lose.
2. All four make an efficiency claim that must be separated into parameter count, arithmetic FLOPs, actual device cost, and task quality.
3. All four benefit from an evidence ledger that ties architectural choices to ablations, task metrics, and failure conditions.

#### Exactly Three MVP Implementations with Code Mock-ups

1. **Mixer switchboard** — safe synthetic-input harness for comparing feature mixers under a fixed interface.

   ```python
   def compare_mixers(batch, mixers):
       """Return shape and summary statistics; training is intentionally out of scope."""
       results = {}
       for name, mixer in mixers.items():
           features = mixer(batch)
           results[name] = {"shape": tuple(features.shape), "mean": float(features.mean())}
       return results
   ```

2. **Branch attribution ledger** — record branch-level metrics without uploading input images.

   ```python
   def branch_record(model_name, metrics, source_url):
       required = {"accuracy", "flops", "latency_ms"}
       missing = required.difference(metrics)
       if missing:
           raise ValueError(f"missing metrics: {sorted(missing)}")
       return {"model": model_name, "metrics": dict(metrics), "source_url": source_url}
   ```

3. **Boundary-slice evaluator** — compare texture, blur, and small-object slices on authorized public data.

   ```python
   def slice_summary(rows):
       """Aggregate precomputed public benchmark rows; never accepts raw private data."""
       grouped = {}
       for row in rows:
           key = row["slice"]
           grouped.setdefault(key, []).append(float(row["score"]))
       return {key: sum(values) / len(values) for key, values in grouped.items()}
   ```

#### Exactly Three Developer Challenges

1. Reproducing the legacy training stack requires version pinning across PyTorch, timm, detection/segmentation toolkits, data layout, and multi-GPU launch behavior.
2. The code exposes several shape and pooling assumptions, so export, odd image sizes, mixed precision, and hardware operator support need explicit tests.
3. A fair comparator must hold data, augmentation, resolution, seeds, optimizer, and evaluation heads constant while measuring real latency and memory in addition to FLOPs.

#### Exactly Three Author Challenges

1. The paper leaves frequency-ramp ratios manually specified, which weakens transfer guidance across tasks and model scales.
2. The experimental evidence does not isolate all interactions among max-pooling, depthwise convolution, pooled attention, fusion, and stage-wise ratios.
3. The paper reports strong benchmark results but does not provide repeated-seed uncertainty, broad robustness slices, or device-level cost evidence needed for deployment claims.

## Validation Notes

- Source gate: pass after repair; PDF exceeded the minimum size and passed `%PDF-`/`%%EOF`; full-paper HTML was 648,256 bytes with 62,882 verified characters, 58 headings, a document marker, and 7 structure terms.
- Cache gate: pass; initial miss to `cached` in `missing-only` mode; `pypdf` and `html-regex` succeeded; source extractor was not applicable.
- Dedup gate: pass; no prior ID/DOI/title/slug marker and no same-paper marker within 24 hours; no reselection.
- Public-safety gate: all generated text is date-only or duration-only where run metadata is needed; no local paths, usernames, machine identifiers, caches, extracted text, PDFs, HTML, or source packages are included.
- Manuscript gate: required headings, YAML/H1 title identity, exactly three exercise paths, and source references are present.

## Attribution Block

- Source URL: https://arxiv.org/abs/2205.12956
  - Applies to: Report-Mark, DEP README, manuscript, logs, and dedup pointer.
  - Notes: Canonical public metadata and paper locator; local source files were withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/2205.12956
  - Applies to: methods, results, ablation, conclusion, and limitations.
  - Notes: Approved full-paper fallback; no HTML file was deposited.
- Source URL: https://arxiv.org/pdf/2205.12956
  - Applies to: paper tables, figures, and PDF integrity provenance.
  - Notes: PDF remained in the private local archive only.
- Source URL: https://doi.org/10.48550/arXiv.2205.12956
  - Applies to: stable paper identifier.
  - Notes: Public DOI locator.
- Source URL: https://github.com/sail-sg/iFormer
  - Applies to: official implementation and reproduction planning.
  - Notes: Repository inspected; code, checkpoints, and dependencies were not copied or executed.
- Source URL: https://github.com/sail-sg/iFormer/blob/725d8e7f455b5e17be20788b9bcd6c6c505c4be0/LICENSE
  - Applies to: license visibility note.
  - Notes: Apache License 2.0 text inspected.
