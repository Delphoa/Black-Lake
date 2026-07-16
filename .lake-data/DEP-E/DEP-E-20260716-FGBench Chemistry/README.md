# DEP-E-20260716-FGBench Chemistry

#chemistry #molecular-reasoning #functional-groups #llm-benchmark #datasets #structure-aware #research-review

Public-safe review of FGBench, a functional-group-level molecular property reasoning dataset and benchmark. This deposit contains generated Markdown only. Paper files, molecular tables, code, images, caches, and extracted text were withheld; no `.source/` exists.

## Contents

- `README.md` - public-safe inventory, synthesis, and attribution.
- `fgbench_chemistry_manuscript.md` - schema-complete source-grounded manuscript.

## Summary of Items

The manuscript reconstructs FGBench's MoleculeNet-derived comparison pipeline, AccFG localization, three reasoning categories, 625,936 QA count, 7,146-item model benchmark, main results, limitations, official repository availability, and validation provenance. It separates reported model performance from chemical validity and downstream drug-design claims.

## Insights and Relevance

FGBench makes functional-group differences explicit rather than asking models to infer every structure-property relation from a whole-molecule string. The main benchmark shows current models remain weak: best single Boolean accuracy is 0.687 and best interaction Boolean accuracy 0.693, with large validity/RMSE variation.

The useful unit is 42,967 validated molecular comparison pairs, from which 625,936 template QA items are generated. Evaluation should therefore control pair/molecule/scaffold/source leakage and report effective independence. Position/chain/stereoisomerism and 3D context are explicitly incomplete. Official MIT code and a Hugging Face dataset are available, but were not downloaded or executed.

Related Black Lake work reinforces task-relevant structure, life-science in-silico boundaries, and benchmark artifact governance.

## Attribution Block

- Paper: Xuan Liu; Siru Ouyang; Xianrui Zhong; Jiawei Han; Huimin Zhao, *FGBench: A Dataset and Benchmark for Molecular Property Reasoning at Functional Group-Level in Large Language Models*, arXiv:2508.01055v4.
- arXiv: https://arxiv.org/abs/2508.01055v4
- HTML: https://arxiv.org/html/2508.01055v4
- PDF: https://arxiv.org/pdf/2508.01055
- DOI: https://doi.org/10.48550/arXiv.2508.01055
- Official repository: https://github.com/xuanliugit/FGBench
- Dataset: https://huggingface.co/datasets/xuan-liu/FGBench
- License evidence: paper CC BY-SA 4.0; inspected repository MIT. Dataset/source-component terms require separate review.
- Source handling: no paper, code, molecular-data, image, cache, or extracted-text file was uploaded.
