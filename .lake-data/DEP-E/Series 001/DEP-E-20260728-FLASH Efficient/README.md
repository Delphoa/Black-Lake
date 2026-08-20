# DEP-E-20260728-FLASH Efficient

#flash #visuomotor #policy #research-review

Public-safe context: job `BLAD-2200-20260728-EB036F17`, item `BLAD-2200-20260728-EB036F17-P09`, uniformly selected `arXiv:2605.15492`. The archive unit reached a verified complete PDF-plus-full-paper-HTML state before review after one bounded local archive repair. Local paths, exact execution times, source documents, datasets, and executable research artifacts are withheld.

## Contents

- `README.md` - context, inventory, source boundary, synthesis, and attribution.
- `flash_efficient_manuscript.md` - schema-complete review of the paper, its evidence, limitations, and bounded implementation paths.

No `.source/` exists. No PDF, HTML, source archive, cache, extracted source text, dataset, model, credential, or executable artifact is deposited.

## Summary of Items

The paper studies flash, visuomotor, policy, sparse. Its abstract frames the contribution as follows: Generative models such as diffusion and flow matching have become dominant paradigms for visuomotor policy learning, yet their reliance on iterative denoising incurs high inference latency incompatible with real-time robotic control. We present Fast Legendre-polynomial Action policy via Sparse History-anchored flow (FLASH Policy), which replaces discrete action-chunk generation with continuous Legendre polynomial trajectory representation. Specifically, by fitting expert demonstrations under sparse temporal sampling, FLASH enables a single inference to cover a significantly extended action horizon. To further accelerate generation, FLASH initiates the flow matching process from history polynomial coefficients rather than uninformative Gaussian noise, shortening the transport distance and enabling accurate single-step inference. Moreover, analytic polynomial differentiation directly provides desired velocity feed-forward signals to the torque controller without numerical approximation. Extensive experiments on five simulated and two real-world manipulation tasks demonstrate that FLASH achieves state-of-the-art success rates ($\ge 92\%$ across all tasks), a per-episode inference time of $31.40\,ms$ (up to $175\times$ faster than diffusion policies and $18\times$ faster than prior flow matching policies), up to $4\times$ faster training convergence than ACT, and $5\times$ to $7\t… The full paper was inspected beyond the abstract, including introduction, method, evaluation, limitations/discussion, conclusion, and references. Reported results remain author claims unless independently reproduced.

## Insights and Relevance

The three related DEPs connect the selected work to Semantic Skill MoE Policies, FAVLA Fast-Slow - DEP-E, and ManipulationNet An - DEP-E. Their concrete shared concepts include visuomotor policies, sparse action sampling, fast-slow control, manipulation benchmarks. The combined implementation lesson is to preserve provenance, establish baseline parity, probe failure boundaries, and make downstream use review-gated when evidence is incomplete.

## Attribution Block

- https://arxiv.org/abs/2605.15492 - official metadata and public source locators.
- https://arxiv.org/html/2605.15492 - verified full paper; local copy withheld.
- https://arxiv.org/pdf/2605.15492 - verified PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2605.15492 - durable paper identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260719-Semantic%20Skill%20MoE - related DEP: Semantic Skill MoE Policies; source basis `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/semantic_skill_moe_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260722-FAVLA%20Fast-Slow - related DEP: FAVLA Fast-Slow - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260726-ManipulationNet%20An - related DEP: ManipulationNet An - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260726-ManipulationNet An/manipulationnet_an_manuscript.md`.
- Source files: PDF, full-paper HTML, metadata HTML, integrity records, and local companions; all withheld locally with zero source-document uploads.
