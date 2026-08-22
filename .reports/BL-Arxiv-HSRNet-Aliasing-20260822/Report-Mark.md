# Report-Mark: HSRNet Aliasing

## Source Metadata

- `Title`: *Hierarchical Similarity Learning for Aliasing Suppression Image Super-Resolution*
- `Authors`: Yuqing Liu; Qi Jia; Jian Zhang; Xin Fan; Shanshe Wang; Siwei Ma; Wen Gao
- `Identifier`: arXiv:2206.03361v1
- `arXiv DOI`: https://doi.org/10.48550/arXiv.2206.03361
- `Publication DOI`: https://doi.org/10.1109/TNNLS.2022.3191674
- `Public source`: https://arxiv.org/abs/2206.03361
- `Review status`: complete local PDF and full-paper HTML verified; source files withheld from the public deposit.

## Concise Research Notes

HSRNet frames single-image super-resolution as an inverse problem and uses an HQS-inspired iterative solver/denoiser architecture. The solver-like branch performs a learned least-squares update; the denoiser uses a Hierarchical Exploration Block for progressively larger receptive fields and a Multi-Scale Attention module for scale-aware feature weighting. The reported configuration uses ten HEB blocks and three iterations, trains on DIV2K with L1 loss, and evaluates standard super-resolution datasets with PSNR and SSIM.

The paper reports competitive quality with a compact parameter and MAC budget, including a BIx4 HSRNet configuration reported at 1.285M parameters and 203.2G MACs. These figures are source-reported and were not reproduced. Synthetic bicubic degradation, unavailable source code in the inspected public pages, missing hardware traces, and a visible table inconsistency limit transfer confidence.

## Evidence and Attribution

| Evidence | Basis | Use in this report |
|---|---|---|
| E1 | Official arXiv metadata and abstract | Identity, authors, date, abstract, and public locators. |
| E2 | Verified full-paper HTML and PDF | Observation model, HQS formulation, HEB, MSA, training, and evaluation setup. |
| E3 | Source tables and figures | Reported PSNR/SSIM, parameter, and MAC values. |
| E4 | Source conclusion and review checks | Limitations, non-reproduction boundary, and source-table caveat. |
| E5 | Three canonical related DEP manuscripts | Concrete cross-DEP conceptual bridges only. |

Claims about method are source-supported transcriptions. Claims about implementation value are reviewer hypotheses. Performance claims remain author-reported until independently reproduced.

## Related DEP Entries

1. `.lake-data/DEP-E/Series 002/DEP-E-20260819-LFMamba Light Field Image/lfmamba_light_field_image_manuscript.md` - direct overlap in image super-resolution, multi-scale structure, and efficiency-aware design.
2. `.lake-data/DEP-E/Series 001/DEP-E-20260720-WKGM MRI Reconstruction/wkgm_mri_reconstruction_manuscript.md` - overlap in iterative inverse reconstruction and explicit learned-prior/data-consistency structure.
3. `.lake-data/DEP-E/Series 001/DEP-E-20260819-EnsIR An Ensemble/ensir_an_ensemble_manuscript.md` - overlap in image restoration, model diversity, and uncertainty-aware evaluation.

## Synthesis Note

### Concept Bridge

HSRNet's central bridge is between classical inverse-problem structure and learned image priors. The solver-like step makes the degradation model visible, while HEB and MSA encode the repeated structures that the inverse problem alone cannot recover. This bridge can connect directly to the three related DEP themes: super-resolution architectures, iterative reconstruction, and ensemble-based uncertainty.

### Three Potential Implementations

1. **Alias-aware benchmark harness:** a deterministic runner for synthetic repeated structures, controlled blur/noise/downsampling, baseline interpolation, compact CNN, and HSRNet-style solver/denoiser variants.
2. **Restoration evidence service:** an offline service that returns an enhanced image plus degradation assumptions, model/configuration identifiers, resource traces, and an abstention reason.
3. **Budget-constrained architecture search:** a controlled sweep over HEB depth, MSA scales, and iteration count, retaining only runs that satisfy fixed quality, latency, and memory budgets.

### Three Deeper Relationship Observations

1. HSRNet and WKGM both make the inverse problem explicit, suggesting that data consistency and learned priors can be evaluated as separate evidence-bearing stages rather than one opaque network.
2. HSRNet and LFMamba both treat spatial or multi-scale structure as a computational resource, so comparisons should report how receptive-field expansion changes quality per parameter and per MAC.
3. HSRNet and EnsIR point to complementary uncertainty strategies: structure-aware restoration can generate a strong candidate, while model diversity or disagreement can flag ambiguous texture and degradation shift.

### Three Conceptual Similarities

1. All three bridges preserve a distinction between an input observation and a reconstructed or enhanced representation.
2. All three make architecture choices meaningful only when tied to a frozen evaluation protocol and explicit failure boundaries.
3. All three support provenance-rich experimentation in which model version, data condition, and resource cost travel with the output.

### Three MVP Implementations with Code Mock-ups

1. **Deterministic degradation and baseline runner**

   ```python
   from dataclasses import dataclass
   import hashlib

   @dataclass(frozen=True)
   class Case:
       image_id: str
       scale: int
       noise: float

   def case_key(case: Case) -> str:
       raw = f"{case.image_id}|{case.scale}|{case.noise:.4f}".encode()
       return hashlib.sha256(raw).hexdigest()[:12]

   def evaluate(case: Case, restore):
       degraded = make_synthetic_degradation(case.image_id, case.scale, case.noise)
       restored = restore(degraded, scale=case.scale)
       return {"case": case_key(case), "restored": restored, "provenance": case}
   ```

2. **Abstention gate for shifted degradation**

   ```python
   def guarded_restore(model, image, shift_score, threshold=0.35):
       if shift_score > threshold:
           return {"status": "abstain", "reason": "degradation_shift", "output": None}
       output, confidence = model(image)
       if confidence < 0.60:
           return {"status": "abstain", "reason": "low_confidence", "output": None}
       return {"status": "ok", "reason": None, "output": output}
   ```

3. **Resource-aware configuration selector**

   ```python
   def choose_config(records, min_psnr, max_macs, max_latency_ms):
       eligible = [r for r in records
                   if r["psnr"] >= min_psnr
                   and r["macs"] <= max_macs
                   and r["latency_ms"] <= max_latency_ms]
       if not eligible:
           return {"status": "no_safe_config", "config": None}
       best = max(eligible, key=lambda r: (r["ssim"], -r["macs"]))
       return {"status": "selected", "config": best["name"]}
   ```

### Three Developer Challenges

1. Reconstruct the exact degradation, architecture, and training configuration without an identified official implementation.
2. Design ablations that isolate HEB, MSA, iteration count, and solver formulation under matched compute and seeds.
3. Instrument latency, memory, failure cases, and confidence so a quality gain cannot hide an unsafe or impractical operating boundary.

### Three Author Challenges

1. Resolve the visible source-table inconsistency and publish a machine-readable result manifest.
2. Provide reproducible code, environment pins, seeds, hardware traces, and a clear license or artifact-availability statement.
3. Extend evaluation beyond bicubic degradation to real sensor, motion, blur, compression, and perceptual-quality conditions.

## Validation Notes

- The source unit was initially partial and was repaired before review; PDF and full-paper HTML passed the required integrity checks.
- The cache layer completed in `missing-only` mode with `pypdf` and HTML-regex; no network was used during extraction.
- Selection used a private immutable candidate index and a family reservation; dedup/reselection checks passed with no reselect.
- The repository Series map validated against the shared head and planned ordinal 1667 in Series 002.
- The public allowlist is Markdown logs/reports/DEP artifacts plus the derived dedup pointer and owning Series map/index files; no source file is staged.

## Final Attribution Block

- Primary source: https://arxiv.org/abs/2206.03361
- Full-paper source: https://arxiv.org/html/2206.03361
- PDF source: https://arxiv.org/pdf/2206.03361
- ArXiv DOI: https://doi.org/10.48550/arXiv.2206.03361
- Publication DOI: https://doi.org/10.1109/TNNLS.2022.3191674
- Related DEP sources: the three canonical repository-relative paths listed above.
- Public-safe note: source files, extracted text, caches, verification records, and local paths were withheld from Black Lake and Slack.
