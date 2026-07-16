# DEP-E-20260716-DMNN Conditional Paths

**Title:** Dynamic Multi-path Neural Network review
**Tags:** conditional-compute, dynamic-routing, computer-vision, efficient-inference, source-first-review

Public-safe context: on 2026-07-16, one local arXiv paper unit was selected uniformly from 75,776 unique PDF-parent units and accepted on the first draw after ID, DOI, normalized-title, slug, repository, memory, companion-repository, and 24-hour checks. Its valid PDF lacked full-paper HTML, so an approved ar5iv fallback repaired the unit and passed the mandatory integrity gate. No local path, exact execution timestamp, private cache, or source file appears here.

## Contents

- `dmnn_conditional_paths_manuscript.md` - schema-complete, source-grounded research manuscript.
- `README.md` - deposit context, inventory, synthesis, and attribution.

## Summary of Items

The manuscript reconstructs DMNN's gated sub-block paths, recurrent/category-informed controller, execution-rate objective, ImageNet and CIFAR-100 evidence, and controller ablation. It records the reported ResNet-50/101 FLOP-accuracy trade-offs while separating arithmetic estimates from actual latency, memory, energy, or cost. Random selection, deduplication, repair, extraction-cache behavior, code-availability checks, and the no-source-upload gate are recorded as evidence.

## Insights and Relevance

DMNN shows that conditional execution can vary both effective depth and width per input. Its strongest reported point nearly matches the authors' ResNet-50 accuracy at 57.6% of its FLOPs, while a DMNN-101 point reports comparable accuracy at 54.9%. These are useful architecture results, but dynamic branching can erase arithmetic savings through poor batching, kernel launch overhead, memory traffic, and accelerator under-utilization.

The three related deposits sharpen that boundary. AFIDAF distinguishes parameters and FLOPs from device efficiency; HSD FTI-FDet adds latency, memory, model size, and field-failure measures; SMES connects conditional routing to load balance and runtime execution. Together they motivate compiler-aware Pareto evaluation and route-stability testing before deployment claims.

## Attribution Block

- Primary paper: *Dynamic Multi-path Neural Network*, Yingcheng Su, Shunfeng Zhou, Yichao Wu, Tian Su, Ding Liang, Jiaheng Liu, Dixin Zheng, Yingxu Wang, Junjie Yan, and Xiaolin Hu.
- arXiv: https://arxiv.org/abs/1902.10949v3
- Full paper: https://arxiv.org/pdf/1902.10949 and https://ar5iv.labs.arxiv.org/html/1902.10949
- DOI: https://doi.org/10.48550/arXiv.1902.10949
- This deposit is an independent review. Source files, metadata HTML, cache outputs, and extracted text were withheld locally and were not uploaded.
