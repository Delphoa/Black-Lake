# Arxiv DEP Phase Log: DASD Reasoning

## Public-Safe Run Summary

- Public date: 2026-07-25.
- Paper: *Distribution-Aligned Sequence Distillation for Superior Long-CoT Reasoning* (arXiv:2601.09088).
- Source-integrity result: repaired from partial to complete before review.
- Selection: uniform PowerShell `Get-Random` draw at zero-based index 56,517 of 75,777 parent-paper units; first draw accepted; 0 duplicate exclusions and 0 reselections.
- Dedup index status before update: no matching arXiv ID, DOI, normalized title, or slug record.

## Phase Metrics

| Phase | Expected duration | Observed duration | Outcome |
|---|---:|---:|---|
| PDF inventory and random draw | 5-10 min | 1 min | 75,780 PDFs reduced to 75,777 parent-paper units; first draw accepted. |
| Dedup and 24-hour screening | 5-10 min | 3 min | No prior owning artifact or recent same-paper marker. |
| Source integrity and local repair | 15-25 min | 12 min | Valid PDF preserved; full-paper HTML, metadata HTML, and TeX source package verified. |
| Missing-only cache extraction | 3-8 min | 1 min | Cache created from local sources. |
| Source review and visual PDF checks | 30-45 min | 33 min | Method, tables, figures, full HTML, TeX, official code page, and model/data release inspected. |
| Related DEP synthesis | 10-15 min | 8 min | Exactly three concrete overlap entries inspected. |
| Public drafting and validation | 20-35 min | 25 min | Schema, exact-count, public-safety, and allowlist checks completed. |

## Extraction Cache

- Initial cache state: miss.
- Final cache state: cached.
- Mode: `missing-only` against the selected local paper unit and central archive cache.
- Extractors: PDF `pypdf`; full-paper HTML `html-regex`; TeX source `tarfile`.
- Text outputs: PDF, HTML, and source text were all produced locally.
- Fallback: `pdftotext` was unavailable; the successful `pypdf` fallback was used.
- Network use during extraction: none. The repair completed before extraction and cache generation read the repaired local bundle.

## Dedup Index Update

- Target record: arXiv:2601.09088; DOI:10.48550/arXiv.2601.09088; slug `DASD-Reasoning`.
- Public artifact paths: the two logs, Report-Mark, DEP-E directory, and DEP-E publication index.
- Status: deposited after remote submission; the commit reference is recorded in the final dedup update.

## Expected vs Observed Trajectory

- Whole-job guidance: 90-120 minutes.
- Rounded observed duration: 83 minutes.
- Assessment: source repair, full-text evidence review, related-DEP inspection, and public-safety controls all completed within the guidance. No review phase was shortened merely to satisfy an estimate.

## Shortfalls and Follow-Up

- No code, checkpoint, dataset, training configuration, or benchmark run was executed; reported results remain author-reported and visually/textually cross-checked only.
- `pdftotext` was unavailable, although `pypdf`, full-paper HTML, and TeX extraction all succeeded.
- An independent replication should pin the released model/data revisions, training recipe, benchmark snapshots, compute budget, and seed set before making comparative performance claims.
