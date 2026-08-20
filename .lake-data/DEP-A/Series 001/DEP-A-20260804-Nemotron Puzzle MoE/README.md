# DEP-A-20260804-Nemotron Puzzle MoE

#artificial-intelligence #mixture-of-experts #model-compression #long-context #LLM-serving #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.04371v2, *Nemotron-Labs-3-Puzzle-75B-A9B: Compressing Hybrid MoE LLMs*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.04371-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.04371-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The final model preserves the parent hybrid block layout, with 88 total blocks: 40 Mamba blocks, 40 MoE blocks, and 8 attention blocks. The KV cache is quantized to FP8 in order to reduce memory overhead and to allow performing the first BMM of the scaled dot product attention operation in FP8 precision. , 2025 ) is a decomposed neural architecture search (NAS) framework for LLMs.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Nemotron-Labs-3-Puzzle-75B-A9B: Compressing Hybrid MoE LLMs as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260717-CrossPool Cold MoE](../DEP-A-20260717-CrossPool%20Cold%20MoE/README.md) - direct MoE deployment and efficiency context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.04371v2
  - Applies to: `2607.04371-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.04371v2
  - Applies to: `2607.04371-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.04371v2
  - Applies to: `2607.04371-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.04371
  - Applies to: `2607.04371-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://huggingface.co/nvidia/NVIDIA-Nemotron-Labs-3-Puzzle-75B-A9B-BF16
  - Applies to: reproducibility context in `2607.04371-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://huggingface.co/nvidia/NVIDIA-Nemotron-Labs-3-Puzzle-75B-A9B-NVFP4
  - Applies to: reproducibility context in `2607.04371-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://huggingface.co/nvidia/NVIDIA-Nemotron-Labs-3-Puzzle-75B-A9B-FP8
  - Applies to: reproducibility context in `2607.04371-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Akhiad Bercovich
  - arXiv author search: https://arxiv.org/search/?query=Akhiad%20Bercovich&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Talor Abramovich
  - arXiv author search: https://arxiv.org/search/?query=Talor%20Abramovich&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Daniel Afrimi
  - arXiv author search: https://arxiv.org/search/?query=Daniel%20Afrimi&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Shay Aharon
  - arXiv author search: https://arxiv.org/search/?query=Shay%20Aharon&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Nir Ailon
  - arXiv author search: https://arxiv.org/search/?query=Nir%20Ailon&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Vladimir Anisimov
  - arXiv author search: https://arxiv.org/search/?query=Vladimir%20Anisimov&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Omer Ullman Argov
  - arXiv author search: https://arxiv.org/search/?query=Omer%20Ullman%20Argov&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Maor Ashkenazi
  - arXiv author search: https://arxiv.org/search/?query=Maor%20Ashkenazi&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Tomer Asida
  - arXiv author search: https://arxiv.org/search/?query=Tomer%20Asida&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Nave Assaf
  - arXiv author search: https://arxiv.org/search/?query=Nave%20Assaf&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Tomer Bar Natan
  - arXiv author search: https://arxiv.org/search/?query=Tomer%20Bar%20Natan&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Alexander Bukharin
  - arXiv author search: https://arxiv.org/search/?query=Alexander%20Bukharin&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Grzegorz Chlebus
  - arXiv author search: https://arxiv.org/search/?query=Grzegorz%20Chlebus&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Marcin Chochowski
  - arXiv author search: https://arxiv.org/search/?query=Marcin%20Chochowski&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Eric Chung
  - arXiv author search: https://arxiv.org/search/?query=Eric%20Chung&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Mohammad Dabbah
  - arXiv author search: https://arxiv.org/search/?query=Mohammad%20Dabbah&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Carlo del Mundo
  - arXiv author search: https://arxiv.org/search/?query=Carlo%20del%20Mundo&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Ewa Dobrowolska
  - arXiv author search: https://arxiv.org/search/?query=Ewa%20Dobrowolska&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Ido Galil
  - arXiv author search: https://arxiv.org/search/?query=Ido%20Galil&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Yaniv Galron
  - arXiv author search: https://arxiv.org/search/?query=Yaniv%20Galron&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Amnon Geifman
  - arXiv author search: https://arxiv.org/search/?query=Amnon%20Geifman&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Yonatan Geifman
  - arXiv author search: https://arxiv.org/search/?query=Yonatan%20Geifman&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Izik Golan
  - arXiv author search: https://arxiv.org/search/?query=Izik%20Golan&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Alex Gronskiy
  - arXiv author search: https://arxiv.org/search/?query=Alex%20Gronskiy&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Tomasz Grzegorzek
  - arXiv author search: https://arxiv.org/search/?query=Tomasz%20Grzegorzek&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Netanel Haber
  - arXiv author search: https://arxiv.org/search/?query=Netanel%20Haber&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Lior Kadoch
  - arXiv author search: https://arxiv.org/search/?query=Lior%20Kadoch&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Grzegorz Karch
  - arXiv author search: https://arxiv.org/search/?query=Grzegorz%20Karch&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Tomer Keren
  - arXiv author search: https://arxiv.org/search/?query=Tomer%20Keren&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Abhinav Khattar
  - arXiv author search: https://arxiv.org/search/?query=Abhinav%20Khattar&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Amir Klein
  - arXiv author search: https://arxiv.org/search/?query=Amir%20Klein&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Tugrul Konuk
  - arXiv author search: https://arxiv.org/search/?query=Tugrul%20Konuk&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Roi Koren
  - arXiv author search: https://arxiv.org/search/?query=Roi%20Koren&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Daniel Korzekwa
  - arXiv author search: https://arxiv.org/search/?query=Daniel%20Korzekwa&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Shaun Kotek
  - arXiv author search: https://arxiv.org/search/?query=Shaun%20Kotek&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Konstantinos Krommydas
  - arXiv author search: https://arxiv.org/search/?query=Konstantinos%20Krommydas&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Itay Levy
  - arXiv author search: https://arxiv.org/search/?query=Itay%20Levy&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Ofri Masad
  - arXiv author search: https://arxiv.org/search/?query=Ofri%20Masad&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Yoav Miron
  - arXiv author search: https://arxiv.org/search/?query=Yoav%20Miron&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Pavlo Molchanov
  - arXiv author search: https://arxiv.org/search/?query=Pavlo%20Molchanov&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Shahar Mor
  - arXiv author search: https://arxiv.org/search/?query=Shahar%20Mor&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Zach Moshe
  - arXiv author search: https://arxiv.org/search/?query=Zach%20Moshe&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Saurav Muralidharan
  - arXiv author search: https://arxiv.org/search/?query=Saurav%20Muralidharan&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Najeeb Nabwani
  - arXiv author search: https://arxiv.org/search/?query=Najeeb%20Nabwani&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Besmira Nushi
  - arXiv author search: https://arxiv.org/search/?query=Besmira%20Nushi&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Mostofa Patwary
  - arXiv author search: https://arxiv.org/search/?query=Mostofa%20Patwary&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Omri Puny
  - arXiv author search: https://arxiv.org/search/?query=Omri%20Puny&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Johannes Rausch
  - arXiv author search: https://arxiv.org/search/?query=Johannes%20Rausch&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Tomer Ronen
  - arXiv author search: https://arxiv.org/search/?query=Tomer%20Ronen&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Sepehr Sameni
  - arXiv author search: https://arxiv.org/search/?query=Sepehr%20Sameni&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Itamar Schen
  - arXiv author search: https://arxiv.org/search/?query=Itamar%20Schen&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Elad Segal
  - arXiv author search: https://arxiv.org/search/?query=Elad%20Segal&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Daniel Serebrenik
  - arXiv author search: https://arxiv.org/search/?query=Daniel%20Serebrenik&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Ido Shahaf
  - arXiv author search: https://arxiv.org/search/?query=Ido%20Shahaf&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Soumye Singhal
  - arXiv author search: https://arxiv.org/search/?query=Soumye%20Singhal&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Daniil Sorokin
  - arXiv author search: https://arxiv.org/search/?query=Daniil%20Sorokin&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Sharath Turuvekere Sreenivas
  - arXiv author search: https://arxiv.org/search/?query=Sharath%20Turuvekere%20Sreenivas&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Marta Stepniewska-Dziubinska
  - arXiv author search: https://arxiv.org/search/?query=Marta%20Stepniewska-Dziubinska&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Ali Taghibakhshi
  - arXiv author search: https://arxiv.org/search/?query=Ali%20Taghibakhshi&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Nima Tajbakhsh
  - arXiv author search: https://arxiv.org/search/?query=Nima%20Tajbakhsh&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Oren Tropp
  - arXiv author search: https://arxiv.org/search/?query=Oren%20Tropp&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Dor Tzur
  - arXiv author search: https://arxiv.org/search/?query=Dor%20Tzur&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Anna Warno
  - arXiv author search: https://arxiv.org/search/?query=Anna%20Warno&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Yi-Fu Wu
  - arXiv author search: https://arxiv.org/search/?query=Yi-Fu%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Michal Zawalski
  - arXiv author search: https://arxiv.org/search/?query=Michal%20Zawalski&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Jiaqi Zeng
  - arXiv author search: https://arxiv.org/search/?query=Jiaqi%20Zeng&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Yian Zhang
  - arXiv author search: https://arxiv.org/search/?query=Yian%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Ran Zilberstein
  - arXiv author search: https://arxiv.org/search/?query=Ran%20Zilberstein&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Amit Zuker
  - arXiv author search: https://arxiv.org/search/?query=Amit%20Zuker&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Author: Ran El-Yaniv
  - arXiv author search: https://arxiv.org/search/?query=Ran%20El-Yaniv&searchtype=author
  - Applies to: the reviewed paper and `2607.04371-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
