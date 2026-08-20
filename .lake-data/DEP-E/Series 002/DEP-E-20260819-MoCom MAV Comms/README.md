# DEP-E-20260819-MoCom MAV Comms

Tags: `DEP-E`, `arXiv`, `micro air vehicles`, `visual communication`, `event vision`, `spiking neural networks`, `motion segmentation`, `robot swarms`

This public-safe research deposit reviews *MoCom: Motion-based Inter-MAV Visual Communication Using Event Vision and Spiking Neural Networks* (`arXiv:2510.14770v1`) and re-conceptualizes it as a low-bandwidth, line-of-sight motion channel for micro-air-vehicle coordination. The private source unit passed the complete-paper integrity gate after official full-paper HTML was repaired. Original source files and machine context were withheld locally.

## Contents

- `README.md` - deposit map, public context, item summaries, synthesis, and complete attribution.
- `mocom_mav_comms_manuscript.md` - schema-complete source-first manuscript with an evidence ledger, critique, implementation paths, exercises, and an MVP concept.

No `.source/` directory is present. PDF, full-paper HTML, metadata HTML, caches, rendered pages, acquisition receipts, and verification records were not copied, staged, uploaded, or attached.

## Summary of Items

The manuscript analyzes MoCom's four-symbol motion codebook, event-count segmentation, EventMAVNet spiking classifier, and Integrated MAV Segmentation and Recognition decoder. It preserves author-reported recognition results at three observation distances, the RTX 4090 batch-latency result, segmentation behavior at three pause lengths, resolution/timestep/polarity ablations, and three small indoor flight demonstrations.

The review separates those reported results from deployment claims. It records absent dataset cardinalities and split identities, a table-level accuracy mismatch, an unexplained energy-accounting method, dependence on multi-second action and pause intervals, a controller side channel in the flight setup, and the lack of an established paper-specific code/data release. It also records the random selection, cross-repository deduplication, source-integrity repair, and no-source-upload gate.

## Insights and Relevance

MoCom's strongest idea is protocol co-design: the motion alphabet, event sensor, temporal segmenter, spiking classifier, decoder, and control semantics form one channel. Its main practical weakness follows from the same coupling. A recognition model can be fast while the message remains slow, because the physical symbol duration, separation gap, flight energy, visibility, and safe maneuver envelope dominate end-to-end throughput.

The three related DEP entries make that boundary concrete. Spiking Pose Tracking contributes sparse temporal perception and evidence-aware efficiency analysis; Group-Control Swarms contributes compact command coding and a planning-versus-execution lens; HESIM contributes sensor-specific noise calibration and sim-to-real provenance. Together they motivate a simulator-first protocol workbench that reports bit error, message completion, latency, energy, collision clearance, observability, and abstention under calibrated event noise before any live swarm deployment.

## Attribution Block

- Source URL: https://arxiv.org/abs/2510.14770
  - Applies to: canonical arXiv identity, authors, v1 submission date, abstract, subjects, and source locators.
- Source URL: https://arxiv.org/html/2510.14770
  - Applies to: complete-paper method, equations, experiments, tables, figures, limitations, conclusion, and references.
- Source URL: https://arxiv.org/pdf/2510.14770
  - Applies to: complete-paper layout and visual cross-checking of all 13 pages, figures, tables, and algorithm presentation.
- Source URL: https://doi.org/10.48550/arXiv.2510.14770
  - Applies to: persistent arXiv identity.
- Source URL: https://doi.org/10.1109/TRO.2026.3677077
  - Applies to: published IEEE Transactions on Robotics identity.
- Source URL: https://api.crossref.org/works/10.1109/TRO.2026.3677077
  - Applies to: published title, authors, publisher, journal, year, and DOI cross-check.
- Source URL: https://aerospace.eng.usm.my/index.php?id=563&option=com_content&view=article
  - Applies to: author-controlled institutional listing of the 2026 journal publication and page range.
- Source URL: https://github.com/fangwei123456/spikingjelly
  - Applies to: generic spiking-neural-network framework linked by the paper; no MoCom-specific implementation was established.
- Source file: `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md`
  - Applies to: event-only spiking perception, temporal evidence aggregation, and efficiency-measurement relationship.
- Source file: `.lake-data/DEP-E/DEP-E-20260729-Group Control Swarms/group_control_swarms_manuscript.md`
  - Applies to: constrained swarm coordination, compact group coding, motion-primitive, and planning/execution relationship.
- Source file: `.lake-data/DEP-E/DEP-E-20260818-Hybrid Sensor HESIM/hesim_hybrid_sensor_manuscript.md`
  - Applies to: calibrated event-sensor noise, simulator provenance, and sim-to-real relationship.
- Source-handling note: original PDF, HTML, metadata, caches, renderings, receipts, and verification records were withheld locally, and no source files were uploaded.
