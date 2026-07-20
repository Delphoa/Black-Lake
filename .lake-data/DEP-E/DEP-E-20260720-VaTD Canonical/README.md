# DEP-E-20260720-VaTD Canonical

#statistical-mechanics #scientific-ml #generative-models #thermodynamics #variational-inference #phase-transitions

This DEP-E deposit reviews a temperature-conditioned variational model for the canonical ensemble. It is a derived, public-safe research artifact based on a verified complete local source unit and public references. Original source documents remain local and were not uploaded.

## Contents

- `vatd_canonical_manuscript.md` - schema-complete research manuscript with evidence ledger, methods, limitations, implementation paths, exercises, and source references.
- `README.md` - deposit context, item summary, relevance, and attribution.

## Summary of Items

The manuscript examines Variational Temperature Differentiation (VaTD), which trains one tractable generative density over a continuous inverse-temperature interval by minimizing a variational free-energy objective. The paper demonstrates the approach on 16 by 16 Ising and XY models, differentiates the learned partition function for energy and heat capacity, and reports source-measured speed advantages over HMC for selected XY observables. The review distinguishes formal identities and source measurements from author estimates, plot-only scaling evidence, and proposed implementations.

Selection was uniform over 75,776 unique PDF-parent paper units: a random draw from the sorted unit list selected zero-based index 20,958. Deduplication by arXiv ID, DOI, normalized title, and slug found no matching Arxiv DEP, so the first draw was accepted with zero exclusions and zero reselections.

The local integrity gate initially found a valid PDF but missing full-paper HTML. Official full-paper HTML was acquired with bounded retries, and both artifacts then passed the required structural checks. The review did not begin until verification succeeded.

## Insights and Relevance

- A temperature-conditioned normalized density turns a family of equilibrium problems into one learned response surface and makes thermodynamic derivatives accessible.
- Tractable density evaluation is central: the partition-function estimate depends on `log q`, so an implicit generator is not a drop-in replacement.
- Amortized speed claims depend on query count, matched accuracy, training overhead, and baseline tuning; the reported crossover estimate should be measured independently.
- The Ising and XY studies provide useful evidence, but exact-reference model selection, single-run reporting, limited timing points, and absent frozen releases constrain reproducibility.
- The closest Black Lake bridges are differentiable physical structure, validation of sampled many-body states, and geometry-aware distribution transforms.

## Attribution Block

- **Primary paper:** Shuo-Hui Li, Yao-Wen Zhang, and Ding Pan, "Deep generative modelling of canonical ensemble with differentiable thermal properties," arXiv:2404.18404v2. [arXiv](https://arxiv.org/abs/2404.18404) - [DOI](https://doi.org/10.1103/8wx7-kyx8).
- **Official code:** Li, Zhang, and Pan, VaTD implementation, inspected at commit `d8fd69c243951769e1e083f8451339522873af8f). [GitHub](https://github.com/li012589/vatd).
- **Related DEP 1:** [Physical Data AI](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Physical%20Data%20AI/physical_data_ai_manuscript.md).
- **Related DEP 2:** [Surface SQD Study](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Surface%20SQD%20Study/surface-sqd-study.md).
- **Related DEP 3:** [Transport Convexity](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Transport%20Convexity/transport_convexity_manuscript.md).
- **Review status:** derived public-safe review; local source integrity verified after HTML repair.
- **Source-file policy:** PDFs, HTML, source archives, extracted text, and caches were withheld locally. No source files were uploaded and no `.source/` directory was created.
- **Prepared for:** Delphoa/Black-Lake Arxiv DEP.
- **Review date:** 2026-07-20.
