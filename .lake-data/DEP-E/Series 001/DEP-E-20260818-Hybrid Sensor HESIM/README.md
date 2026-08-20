# DEP-E-20260818-Hybrid Sensor HESIM

#hybrid-sensors #event-vision #imaging-noise #calibration #simulation #sim-to-real #research-review

This DEP-E preserves a source-grounded review of *Hybrid Event Frame Sensors: Modeling, Calibration, and Simulation* (arXiv:2511.18037v2). The review covers the unified APS-EVS noise model, real-sensor calibration protocol, H-ESIM RAW/event simulator, downstream video interpolation and deblurring evidence, limitations, and implementation implications. The original source bundle was verified locally and withheld from this public repository; provenance is preserved through public URLs.

## Contents

- \`README.md\` - public-safe inventory, summary, relevance, and attribution for this DEP-E.
- \`hesim_hybrid_sensor_manuscript.md\` - schema-complete manuscript research artifact with source metadata, evidence ledger, claims, limitations, implementations, exercises, related DEP entries, and validation notes.

## Summary of Items

- \`hesim_hybrid_sensor_manuscript.md\` reconstructs the shared latent-signal model for APS and EVS pixels, the dark/illuminated calibration workflow, the H-ESIM synthesis pipeline, the two-sensor evaluation, reported VFI/deblurring metrics, and the paper's stated boundary conditions.
- \`README.md\` records the public-safe source policy: the verified PDF, metadata HTML, full-paper HTML, source-package attempt, extracted material, and acquisition records remain local and are not redistributed.

## Insights and Relevance

The paper's durable relevance is a calibration-first pattern for sim-to-real sensing. Instead of treating event streams and frames as generic input channels, it ties both to a shared latent signal, estimates sensor-specific noise from controlled captures, and carries those parameters into a simulator whose outputs can be evaluated on real hardware. This creates an auditable bridge between physical sensor behavior and downstream learning, while exposing where the bridge can fail: unseen regimes, rolling-shutter distortion, event sparsity, no-reference metrics, and incomplete implementation release. The related Black Lake entries connect this pattern to multi-sensor spatiotemporal calibration, physically modeled RGBD imaging, and downstream simulation-to-real transfer.

## Source Policy

The selected paper passed the complete-source gate after one bounded brokered repair. The optional TeX/source package was unavailable through the permitted redirect policy. No original source file, cache, extracted text, rendering, provenance record, verification report, or local archive path is included here, and no public \`.source/\` directory was created.

## Attribution Block

- Source URL: https://arxiv.org/abs/2511.18037
  - Applies to: \`README.md\` and \`hesim_hybrid_sensor_manuscript.md\`.
  - Notes: Public arXiv metadata, authors, version history, abstract, and identifiers.
- Source URL: https://arxiv.org/pdf/2511.18037
  - Applies to: \`hesim_hybrid_sensor_manuscript.md\`.
  - Notes: Primary paper reviewed from the verified local copy; the PDF itself is withheld.
- Source URL: https://arxiv.org/html/2511.18037
  - Applies to: \`hesim_hybrid_sensor_manuscript.md\`.
  - Notes: Public full-paper HTML used to cross-check structure, tables, and claims; the local HTML is withheld.
- Source URL: https://doi.org/10.48550/arXiv.2511.18037
  - Applies to: \`hesim_hybrid_sensor_manuscript.md\`.
  - Notes: Persistent arXiv DOI.
- Source URL: https://yunfanlu.github.io/HESIM/
  - Applies to: \`hesim_hybrid_sensor_manuscript.md\`.
  - Notes: Author-controlled project page used for implementation context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md
  - Applies to: \`hesim_hybrid_sensor_manuscript.md\`.
  - Notes: Related DEP on targetless multi-sensor spatial and temporal calibration.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260730-Off-Aperture%20RGBD/off_aperture_rgbd_manuscript.md
  - Applies to: \`hesim_hybrid_sensor_manuscript.md\`.
  - Notes: Related DEP on physically modeled computational imaging, calibration, and sim-to-real optical limits.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260805-RetinaGAN%20Sim-to-Real/retinagan_sim_to_real_manuscript.md
  - Applies to: \`hesim_hybrid_sensor_manuscript.md\`.
  - Notes: Related DEP on task-preserving simulation-to-real transfer and downstream physical evidence.
- Source files: withheld locally; no original PDF, HTML, metadata page, source package, cache, extracted text, rendering, provenance record, or verification report is redistributed.
  - Applies to: all files in this DEP-E.
