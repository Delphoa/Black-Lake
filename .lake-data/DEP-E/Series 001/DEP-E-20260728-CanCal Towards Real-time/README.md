# DEP-E-20260728-CanCal Towards Real-time

#cancal #towards #realtime #research-review

Public-safe context: job `BLAD-2200-20260728-EB036F17`, item `BLAD-2200-20260728-EB036F17-P05`, uniformly selected `arXiv:2408.16515`. The archive unit reached a verified complete PDF-plus-full-paper-HTML state before review after one bounded local archive repair. Local paths, exact execution times, source documents, datasets, and executable research artifacts are withheld.

## Contents

- `README.md` - context, inventory, source boundary, synthesis, and attribution.
- `cancal_towards_real_time_manuscript.md` - schema-complete review of the paper, its evidence, limitations, and bounded implementation paths.

No `.source/` exists. No PDF, HTML, source archive, cache, extracted source text, dataset, model, credential, or executable artifact is deposited.

## Summary of Items

The paper studies cancal, towards, real-time, lightweight. Its abstract frames the contribution as follows: Ransomware attacks have emerged as one of the most significant cybersecurity threats. Despite numerous proposed detection and defense methods, existing approaches face two fundamental limitations in large-scale industrial applications: intolerable system overheads and notorious alert fatigue. To address these challenges, we propose CanCal, a real-time and lightweight ransomware detection system. Specifically, CanCal selectively filters suspicious processes by the monitoring layers and then performs in-depth behavioral analysis to isolate ransomware activities from benign operations, minimizing alert fatigue while ensuring lightweight computational and storage overhead. The experimental results on a large-scale industrial environment~(1,761 ransomware, ~3 million events, continuous test over 5 months) indicate that CanCal is as effective as state-of-the-art techniques while enabling rapid inference within 30ms and real-time response within a maximum of 3 seconds. CanCal dramatically reduces average CPU utilization by 91.04% (from 6.7% to 0.6%) and peak CPU utilization by 76.69% (from 26.6% to 6.2%), while avoiding 76.50% (from 3,192 to 750) of the inspection efforts from security analysts. By the time of this writing, CanCal has been integrated into a commercial product and successfully deployed on 3.32 million endpoints for over a year. From March 2023 to April 2024, CanCal su… The full paper was inspected beyond the abstract, including introduction, method, evaluation, limitations/discussion, conclusion, and references. Reported results remain author claims unless independently reproduced.

## Insights and Relevance

The three related DEPs connect the selected work to Memory Defense Layers - DEP-E, Context Backdoor Defense - DEP-E, and Constraint-Aware Systems - DEP-E. Their concrete shared concepts include ransomware detection, layered response, IoT security, industrial resilience. The combined implementation lesson is to preserve provenance, establish baseline parity, probe failure boundaries, and make downstream use review-gated when evidence is incomplete.

## Attribution Block

- https://arxiv.org/abs/2408.16515 - official metadata and public source locators.
- https://arxiv.org/html/2408.16515 - verified full paper; local copy withheld.
- https://arxiv.org/pdf/2408.16515 - verified PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2408.16515 - durable paper identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Memory%20Defense%20Layers - related DEP: Memory Defense Layers - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260718-Memory Defense Layers/memory-defense-layers.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-Context%20Backdoor - related DEP: Context Backdoor Defense - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260720-Context Backdoor/context_backdoor_defense_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260726-Constraint-Aware%20Systems - related DEP: Constraint-Aware Systems - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260726-Constraint-Aware Systems/constraint-aware-systems.md`.
- Source files: PDF, full-paper HTML, metadata HTML, integrity records, and local companions; all withheld locally with zero source-document uploads.
