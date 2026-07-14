# Arxiv DEP Phase Log: OViP Preference Learning

## Public-Safe Run Summary

- `Deposit date`: 2026-07-14.
- `Paper`: arXiv:2505.15963v2, *OViP: Online Vision-Language Preference Learning for VLM Hallucination*.
- `Selection`: One uniform zero-based random index, 50,425 of 75,774 PDF-backed paper units.
- `Dedup result`: No prior or same-paper 24-hour marker; 0 exclusions; 0 reselections.
- `Source gate`: Initial partial state repaired to verified complete before extraction or synthesis.
- `Output class`: Containerized DEP-E research deposit plus operational log, phase log, Report-Mark, publication index row, and public dedup pointer.

## Phase Metrics

| Phase | Expected duration | Observed duration | Status | Evidence / outcome |
|---|---:|---:|---|---|
| Governance, memory, and skill-contract review | 10 minutes | 6.0 minutes | Complete | Automation memory plus source-processing, cache, public-safety, manuscript, DEP, archive-repair, download-safety, and Slack contracts were loaded. |
| Repository synchronization and live README review | 8 minutes | 1.0 minute | Complete | Current default-branch README and `.lake-data` filing/index rules were inspected. |
| Candidate enumeration and random draw | 5 minutes | 0.1 minutes | Complete | 75,774 PDF-parent units; uniform index 50,425; enumeration itself took 2.8 seconds. |
| Identifier derivation and dedup | 12 minutes | 1.0 minute | Complete | ID, DOI, title, and slug scans across the index, repository artifacts, memory, related-repository results, and active worktrees found no match. |
| Local source-integrity gate | 8 minutes | 0.2 minutes | Initial shortfall found | PDF passed; full-paper HTML was absent, so review paused. |
| Bounded archive repair and verification | 20 minutes | 0.4 minutes | Complete | Existing PDF preserved; HTML, metadata HTML, and source archive fetched; all integrity checks passed with no partials. |
| Extractor preflight and cache | 10 minutes | 0.1 minutes | Complete with fallback | Initial miss; local `missing-only` extraction completed in 0.661 seconds with `pypdf`, `html-regex`, and `tarfile`. |
| Primary paper review | 35 minutes | 16.0 minutes | Complete | Full method, metrics, tables, training dynamics, cost, limitations, ethics, and appendices were reviewed across three local text representations and public HTML. |
| Official code and publication verification | 12 minutes | 4.0 minutes | Complete | arXiv v2, DOI/license, and official repository structure/instructions were checked without execution. |
| Related DEP synthesis | 15 minutes | 6.0 minutes | Complete | Exactly three repository manuscripts were inspected and selected for concrete overlap. |
| Artifact drafting | 40 minutes | 24.0 minutes | Complete | Job log, phase log, Report-Mark, DEP README, schema-complete manuscript, and publication-index row were drafted. |
| Validation and dedup update | 15 minutes | 8.0 minutes | Complete | Required headings/counts, JSON, links, attribution order, four Python snippets, dedup uniqueness, trailing whitespace, final newlines, and public-safe content passed. |
| Commit, push, and Slack notification | 10 minutes | 3.0 minutes | Complete | Direct default-branch push succeeded; the public-safe channel notification linked the primary artifact commit and required paths. |

`Whole-job guidance`: The expected trajectory is approximately 200 minutes. Observed values are rounded public-safe elapsed estimates, not exact local timestamps. No estimate was used to truncate the paper-body review, limitations, related-entry exploration, or manuscript contract.

## Extraction Cache

- `Initial cache status`: Miss.
- `Refresh mode`: `missing-only`.
- `Integrity prerequisite`: Verified complete PDF and full-paper HTML before synthesis.
- `Preflight fallback order`: `pdftotext`, `fitz`, `pypdf`, `PyPDF2`, `pdfminer.six`, HTML, source package.
- `Available PDF backend`: `pypdf`.
- `Final cache status`: Cached.
- `Text outputs`: PDF text present (74,898 bytes); HTML text present (81,175 bytes); source text present (159,651 bytes).
- `Extractors`: `pypdf` for PDF, `html-regex` for HTML, and `tarfile` for TeX source.
- `Fallback reason`: `pdftotext` unavailable.
- `Backfill status`: Initial cache miss became a complete three-representation cache after the local archive repair; no cache network fallback was required.
- `Source locality`: All original and extracted source material remains local and is excluded from the repository and Slack.

## Dedup Index Update

- `Pre-selection index status`: 14 records; no arXiv:2505.15963 entry.
- `Artifact scans`: No matching arXiv ID, DOI, normalized title, or slug in Black Lake `.logs`, `.reports`, `.lake-data`, or `.staging`.
- `Automation memory`: No matching paper marker among prior runs.
- `Related repository`: No matching ID or normalized-title result in relevant Black-Lake-Data searches.
- `Same-paper window`: No marker in active worktree Markdown or JSON records within 24 hours.
- `Exclusions / reselections`: 0 / 0.
- `Post-submission pointer status`: Deposited record finalized with repository-relative artifact paths, source URLs, date-only deposit marker, primary artifact commit reference, status, and notes.

## Expected vs Observed Trajectory

Enumeration and the first-pass dedup were faster than estimated because the adjacent README and filename exposed the identifier cleanly and the first draw was unused. The integrity gate then correctly added a repair phase: a PDF alone was not treated as a complete paper, and review did not begin until full-paper HTML passed structural validation.

The extraction cache exceeded the normal minimum because the repaired unit supplied PDF, HTML, and TeX source representations. The `pypdf` fallback was adequate for PDF text, while HTML and source text were used to resolve table signs, formulas, appendix details, and extraction ambiguities.

The review separates author-reported empirical results, official repository evidence, and reviewer interpretation. It preserves the HRI construction caveat, evaluation-judge dependence, untuned filtering, seven-GPU cost, and non-reproduction boundary rather than inferring deployment readiness from benchmark gains or repository presence.

Related-entry exploration was intentionally open-ended. VLM Probing, VideoWeave Geometry, and BA-LoRA Bias were selected only after their manuscripts were inspected; they provide diagnostics, synthetic-visual consistency, and behavior-preserving adaptation context, not independent validation of OViP.

## Shortfalls and Follow-Up

- The official training, evaluation, judge, diffusion, and data pipelines were not executed; reported metrics and 1.97x efficiency remain author-reported.
- HRI uses observed potential gains and OViP reference values, so independent fixed-reference and uncertainty analyses are needed before cross-study use.
- The paper manually corrected only a subset of benchmark errors and states that its sampling filter was not carefully tuned.
- Synthetic negative images were not audited for semantic isolation, artifacts, representational bias, or label leakage.
- No source files are included in the public deposit; all original and extracted source material was withheld locally.

## Submission Outcome

- `Repository`: Delphoa/Black-Lake default branch.
- `Primary artifact commit`: https://github.com/Delphoa/Black-Lake/commit/601536e83c62347c47f33f93ce1882929672431e.
- `Slack notification`: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784009965170939.
- `Blockers`: None; reproduction and synthetic-negative audit remain follow-up work.
