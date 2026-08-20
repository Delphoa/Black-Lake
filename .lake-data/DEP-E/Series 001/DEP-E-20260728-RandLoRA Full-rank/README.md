# DEP-E-20260728-RandLoRA Full-rank

#randlora #fullrank #parameterefficient #research-review

Public-safe context: job `BLAD-2200-20260728-EB036F17`, item `BLAD-2200-20260728-EB036F17-P01`, uniformly selected `arXiv:2502.00987`. The archive unit reached a verified complete PDF-plus-full-paper-HTML state before review after one bounded local archive repair. Local paths, exact execution times, source documents, datasets, and executable research artifacts are withheld.

## Contents

- `README.md` - context, inventory, source boundary, synthesis, and attribution.
- `randlora_full_rank_manuscript.md` - schema-complete review of the paper, its evidence, limitations, and bounded implementation paths.

No `.source/` exists. No PDF, HTML, source archive, cache, extracted source text, dataset, model, credential, or executable artifact is deposited.

## Summary of Items

The paper studies randlora, full-rank, parameter-efficient, fine-tuning. Its abstract frames the contribution as follows: Low-Rank Adaptation (LoRA) and its variants have shown impressive results in reducing the number of trainable parameters and memory requirements of large transformer networks while maintaining fine-tuning performance. The low-rank nature of the weight update inherently limits the representation power of fine-tuned models, however, thus potentially compromising performance on complex tasks. This raises a critical question: when a performance gap between LoRA and standard fine-tuning is observed, is it due to the reduced number of trainable parameters or the rank deficiency? This paper aims to answer this question by introducing RandLoRA, a parameter-efficient method that performs full-rank updates using a learned linear combinations of low-rank, non-trainable random matrices. Our method limits the number of trainable parameters by restricting optimization to diagonal scaling matrices applied to the fixed random matrices. This allows us to effectively overcome the low-rank limitations while maintaining parameter and memory efficiency during training. Through extensive experimentation across vision, language, and vision-language benchmarks, we systematically evaluate the limitations of LoRA and existing random basis methods. Our findings reveal that full-rank updates are beneficial across vision and language tasks individually, and even more so for vision-language tasks, where Raâ€¦ The full paper was inspected beyond the abstract, including introduction, method, evaluation, limitations/discussion, conclusion, and references. Reported results remain author claims unless independently reproduced.

## Insights and Relevance

The three related DEPs connect the selected work to BA-LoRA Bias - DEP-E, Efficient FM Survey - DEP-E, and Device Tuning MTL - DEP-E. Their concrete shared concepts include low-rank adaptation, parameter-efficient tuning, foundation-model efficiency, device adaptation. The combined implementation lesson is to preserve provenance, establish baseline parity, probe failure boundaries, and make downstream use review-gated when evidence is incomplete.

## Attribution Block

- https://arxiv.org/abs/2502.00987 - official metadata and public source locators.
- https://arxiv.org/html/2502.00987 - verified full paper; local copy withheld.
- https://arxiv.org/pdf/2502.00987 - verified PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2502.00987 - durable paper identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260709-BA-LoRA%20Bias - related DEP: BA-LoRA Bias - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Efficient%20FM%20Survey - related DEP: Efficient FM Survey - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260719-Device%20Tuning%20MTL - related DEP: Device Tuning MTL - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md`.
- Source files: PDF, full-paper HTML, metadata HTML, integrity records, and local companions; all withheld locally with zero source-document uploads.
