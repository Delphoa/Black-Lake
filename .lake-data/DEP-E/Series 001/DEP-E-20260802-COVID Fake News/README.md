# DEP-E-20260802-COVID Fake News

#artificial-intelligence #natural-language-processing #misinformation #fake-news #COVID-19 #transformers #adversarial-training #domain-adaptation #evaluation

Public-safe DEP-E research deposit reviewing arXiv:2101.05509v3, *Transformer-based Language Model Fine-tuning Methods for COVID-19 Fake News Detection*. The source-first review used a verified complete local PDF, full-paper HTML, metadata HTML, and TeX/source package. All source documents, caches, renders, receipts, verification records, and machine context were withheld locally; no `.source/` directory was created.

## Contents

- `README.md` - DEP classification, inventory, item summaries, relevance notes, and complete public attribution.
- `covid_fake_news_manuscript.md` - schema-complete manuscript review with source metadata, evidence ledger, method and result reconstruction, critique, implementation paths, safe MVP, related research, and replication appendix.

## Summary of Items

### `README.md`

Defines the public distribution boundary and records every public source locator used by the generated manuscript. It confirms that original PDF, HTML, metadata, TeX/source, cache, render, receipt, and verification files remain outside the repository.

### `covid_fake_news_manuscript.md`

Reviews the paper's six-token vocabulary expansion, heated-up softmax schedule, embedding-level fast-gradient training, and RoBERTa/CT-BERT fusion. It preserves the reported 0.990185 F1 while documenting the evidence boundary: one historical shared-task dataset, best-result selection without uncertainty, reuse of validation errors for augmentation, formula and fusion-description inconsistencies, no established official code release, and no evidence-retrieval or real-world deployment evaluation.

## Insights and Relevance

The paper remains useful as a modular fine-tuning case study: domain tokenization, hard-example optimization, adversarial regularization, and general/domain encoder diversity can be tested separately. Its near-ceiling benchmark score is not a factuality certificate. The related Black Lake entries extend the review in three directions: adversarial-label semantics, task-aligned disinformation evaluation, and evidence-backed claim correction. Together they motivate a safer system boundary in which a classifier only prioritizes review, while retrieval, provenance, calibrated abstention, and human judgment govern consequential decisions.

Random selection and deduplication were source-first and auditable. `rg --files -g "*.pdf"` produced 75,960 PDFs in 75,957 parent paper units. A cross-repository 1,881-ID used-paper index excluded 522 units, 185 identifier-incomplete units were withheld, and a uniform `Get-Random` draw selected zero-based eligible index 74,494 from 75,250 eligible units. Exact arXiv ID, both DOI values, normalized-title, slug, and public-safe 24-hour checks found no duplicate; no reselection was needed.

The initially partial local unit was repaired before synthesis. The valid PDF was preserved; approved ar5iv full-paper HTML, arXiv metadata HTML, and the source package were collected with bounded attempts. Independent checks confirmed the PDF header and EOF, substantial full-paper HTML structure, readable TeX archive, and zero partial files. No source file was uploaded.

## Attribution Block

- Source URL: https://arxiv.org/abs/2101.05509
  - Applies to: paper identity, authors, version history, subjects, comments, license locator, this README, and `covid_fake_news_manuscript.md`.
  - Notes: Metadata only; not substituted for the complete paper.
- Source URL: https://arxiv.org/pdf/2101.05509
  - Applies to: method, equations, Figure 1, Tables 1-2, conclusions, references, and visual review in `covid_fake_news_manuscript.md`.
  - Notes: Complete PDF verified locally and withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/2101.05509
  - Applies to: searchable full-paper review and document-structure verification.
  - Notes: Approved full-paper fallback used because official arXiv HTML was unavailable; local copy withheld.
- Source URL: https://arxiv.org/e-print/2101.05509
  - Applies to: TeX/source inspection, formula audit, and table cross-checks.
  - Notes: Source package collected locally and withheld.
- Source URL: https://doi.org/10.48550/arXiv.2101.05509
  - Applies to: persistent arXiv identity in both DEP files.
  - Notes: arXiv-issued DOI.
- Source URL: https://link.springer.com/chapter/10.1007/978-3-030-73696-5_9
  - Applies to: venue, pages, publication date, author identity, publisher metadata, and published chapter context.
  - Notes: Springer chapter record.
- Source URL: https://doi.org/10.1007/978-3-030-73696-5_9
  - Applies to: published chapter identity in both DEP files.
  - Notes: Springer DOI.
- Source URL: https://competitions.codalab.org/competitions/26655
  - Applies to: CONSTRAINT shared-task identity and phase context.
  - Notes: Public competition record; dataset not redistributed.
- Source URL: https://arxiv.org/abs/2011.03327
  - Applies to: dataset identity, size, annotation claim, and baseline context.
  - Notes: Primary dataset paper record.
- Source URL: https://arxiv.org/abs/2005.07503
  - Applies to: CT-BERT identity, target-domain purpose, and source-model context.
  - Notes: Primary model paper record.
- Source URL: https://github.com/huggingface/transformers
  - Applies to: named implementation-library provenance.
  - Notes: Current official repository inspected as context; not an experiment-time version pin.
- Source URL: https://github.com/huggingface/tokenizers
  - Applies to: tokenizer-library provenance and vocabulary-extension context.
  - Notes: Current official repository inspected as context; not an experiment-time version pin.
- Repository-relative source: `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md`
  - Applies to: adversarial perturbation and semantic-label-validity synthesis.
  - Notes: Related processed research; no source claim transferred.
- Repository-relative source: `.lake-data/DEP-E/DEP-E-20260716-PIArena Evaluation/piarena_evaluation_manuscript.md`
  - Applies to: task-aligned disinformation, evaluator uncertainty, and utility-tradeoff synthesis.
  - Notes: Related processed research; no source claim transferred.
- Repository-relative source: `.lake-data/DEP-A/DEP-A-20260717-CheckRLM Coherence/2607.02262-whitepaper-review.md`
  - Applies to: evidence retrieval, localized correction, provenance, and abstention synthesis.
  - Notes: Related processed research; no source claim transferred.
- Repository authority: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: DEP-E filing, naming, source-withholding, attribution, commit, and publication-index rules.
  - Notes: Live repository authority inspected before writing.
- Dedup context repository: https://github.com/Delphoa-Labs/Black-Lake-Data
  - Applies to: cross-repository used-paper and recent-marker validation.
  - Notes: Live README and default-branch research paths inspected; no file from that repository is deposited here.
