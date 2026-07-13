# Arxiv DEP Phase Log: SAILFISH Vetting

## Public-Safe Run Summary

- `Deposit date`: 2026-07-13.
- `Paper`: arXiv:2104.08638v2, *SAILFISH: Vetting Smart Contract State-Inconsistency Bugs in Seconds*.
- `Selection`: One uniform zero-based random index, 8,874 of 75,761 PDF-backed paper units.
- `Dedup result`: No prior or same-paper 24-hour marker; 0 exclusions; 0 reselections.
- `Output class`: DEP-E research deposit plus operational log, phase log, Report-Mark, and public dedup pointer.

## Phase Metrics

| Phase | Expected duration | Observed duration | Status | Evidence / outcome |
|---|---:|---:|---|---|
| Governance, memory, and skill-contract review | 8 minutes | 4.0 minutes | Complete | Automation memory plus cache, public-safety, manuscript-schema, DEP, and Slack contracts were loaded. |
| Repository synchronization and live README review | 8 minutes | 1.0 minute | Complete | Current `main` tips and README contracts were inspected for both repositories. |
| Candidate enumeration and random draw | 5 minutes | 0.1 minutes | Complete | 75,761 PDF-parent paper units; uniform index 8,874; enumeration itself took 2.774 seconds. |
| Identifier derivation and dedup | 10 minutes | 0.2 minutes | Complete | ID, DOI, title, and slug scans across the index, both repositories, memory, and worktree markers found no match. |
| Extractor preflight and cache | 10 minutes | 0.1 minutes | Complete with fallback | Initial miss; local `pypdf` extraction completed in 1.114 seconds because `pdftotext` was unavailable. |
| Primary paper review | 30 minutes | 13.0 minutes | Complete | Full PDF-derived text was inspected across design, evaluation, limitations, conclusion, and appendices. |
| Publication and released-artifact verification | 10 minutes | 4.0 minutes | Complete | arXiv v2, IEEE DOI, UCSB publication record, author PDF, and official code/data repository were checked. |
| Related DEP synthesis | 15 minutes | 5.0 minutes | Complete | Exactly three repository entries and their cited primary arXiv records were inspected. |
| Artifact drafting | 35 minutes | 22.0 minutes | Complete | Job log, phase log, Report-Mark, DEP README, and schema-complete manuscript were produced. |
| Validation and dedup update | 12 minutes | 7.0 minutes | Complete | Required headings/counts, JSON, paths, attribution order, and public-safe content were checked. |
| Commit, push, and Slack notification | 10 minutes | 3.0 minutes | Complete | Direct default-branch push succeeded and the required channel notification was posted. |

`Whole-job guidance`: The expected trajectory was approximately 153 minutes. The observed trajectory remained below that guidance without truncating the source-first paper review, limitations, released-artifact check, related-entry synthesis, or manuscript schema. Observed values are rounded public-safe elapsed estimates, not exact local timestamps.

## Extraction Cache

- `Initial cache status`: Miss.
- `Refresh mode`: `missing-only`.
- `Local source inventory`: One PDF and adjacent metadata README records.
- `Preflight fallback order`: `pdftotext`, `fitz`, `pypdf`, `PyPDF2`, `pdfminer.six`, HTML, source package.
- `Available backend`: `pypdf`.
- `Local extractor result`: PDF text succeeded through `pypdf`; `pdftotext` was unavailable.
- `Final cache status`: Partial, because PDF text is present while local HTML and source-package text are absent.
- `Text outputs`: PDF text present (117,020 bytes); HTML text absent; source text absent.
- `Fallback reason`: `pdftotext` unavailable.
- `Backfill status`: Local PDF-text backfill completed; no paper-body network backfill was needed.
- `Network use`: Public primary metadata, venue, author-paper, code, and related-paper pages were inspected separately after selection.

## Dedup Index Update

- `Pre-selection index status`: No arXiv:2104.08638 entry.
- `Artifact scans`: No matching arXiv ID, DOI, normalized title, or slug in Black Lake `.logs`, `.reports`, or `.lake-data`.
- `Automation memory`: No matching paper marker among prior runs.
- `Related repository`: No matching ID or normalized title marker in Black-Lake-Data.
- `Same-paper window`: No marker in active worktree records within 24 hours.
- `Exclusions / reselections`: 0 / 0.
- `Post-submission status`: Pointer finalized as deposited with repository-relative artifact paths, source URLs, date-only deposit marker, primary artifact commit reference, and notes.

## Expected vs Observed Trajectory

Enumeration, dedup, and extraction were faster than estimated because the archive metadata exposed the identifier cleanly, the first draw was eligible, and `pypdf` extracted the local PDF successfully. The saved time was applied to the EXPLORE/REFINE mechanism, evaluation tables, ablation, stated unsoundness, appendices, and official release verification.

The review distinguishes three evidence layers: the paper's historical experiment claims, the official repository's present claim that code/data are available, and reviewer interpretations about modern implementation paths. It does not infer current analyzer compatibility or reproduced results from repository presence alone.

Related-entry exploration was intentionally open-ended. Antaeus, Chai, and VeriChat were selected only after their repository artifacts and cited primary abstracts were inspected; they are conceptual bridges, not independent validation of SAILFISH.

No phase estimate was used as a reason to omit required headings, exact-count synthesis elements, cache methodology, random-selection methodology, or dedup validation.

## Shortfalls and Follow-Up

- The PDF extractor introduced encoding noise around typography, symbols, and some table cells; key numbers were checked against surrounding text and the author-hosted PDF view.
- The released Docker image, analyzer code, contract corpus, and benchmark scripts were not executed; reproducibility remains unverified in this run.
- The paper's corpus ends in 2020 and the prototype depends on historical Solidity/Slither behavior, limiting direct inference about current contracts.
- SAILFISH explicitly does not claim soundness; unresolved external calls, inline assembly, exception/reversion behavior, loops, and coarse collection summaries remain important boundaries.
- No source files were collected for redistribution, so the DEP contains generated analysis and public URLs only.

## Submission Outcome

- `Repository`: Delphoa/Black-Lake default branch.
- `Artifact commit`: https://github.com/Delphoa/Black-Lake/commit/7e651d7.
- `Slack notification`: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1783923556974429.
- `Blockers`: None. Reproduction of the released analyzer and experimental data remains future work.
