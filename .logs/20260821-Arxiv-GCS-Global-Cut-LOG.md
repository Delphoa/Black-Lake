# Black Lake Arxiv DEP Job Log

- **Run date:** 2026-08-21 (UTC)
- **Status:** Selected, reviewed, packaged, and prepared for repository submission
- **Selected paper:** *Beyond Local Selection: Global Cut Selection for Enhanced Mixed-Integer Programming* — arXiv:2503.15847
- **Public provenance:** Official arXiv record, abstract, full-paper HTML, and PDF; source package was unavailable under the archive's terminal redirect policy.
- **Random selection:** Fast `rg --files -g "*.pdf"` enumeration followed by a uniform random reservation from an immutable candidate index; 75,967 PDF files, 75,964 parent units, 59,188 eligible rows.
- **Eligibility and deduplication:** Permanent repository/memory identity scan plus 24-hour marker scan across Black Lake `.logs`, `.reports`, `.lake-data`, and related DEP metadata; 6,801 duplicate archive identities, 1,999 permanent dedup exclusions, and 782 recent-marker exclusions were removed. One paper was reserved; excluded/reselected count: 0.
- **Source-integrity gate:** The local unit was repaired from official arXiv endpoints, then verified complete: PDF header/EOF checks passed and full-paper HTML passed size, body-text, document-marker, heading, and paper-structure checks. Source files remain local and none were uploaded.
- **Related DEP entries:** `DEP-E/Series 001/DEP-E-20260819-HGATSolver A`; `DEP-E/Series 002/DEP-E-20260819-Joint Optimization of`; `DEP-E/Series 002/DEP-E-20260819-Monte Carlo Tree Search`.
- **Outputs:** `.reports/BL-Arxiv-GCS-Global-Cut-20260821/Report-Mark.md`; `.lake-data/DEP-E/Series 002/DEP-E-20260821-Global Cut Selection/`.
- **Validation:** Public-output sanitizer and source-file allowlist are required before commit; the DEP contains only its README and schema-complete manuscript. Repository submission and remote audit are the final operational steps for this log.

## Questions for the Next Reviewer

1. Which global tree features most improve cut selection without making inference prohibitively expensive?
2. How should a solver detect when GCS is likely to increase node count despite reducing wall-clock time?
3. What reproducible benchmark protocol would separate model gains from solver, hardware, and instance effects?

## Challenges for the Next Review Pass

1. Reproduce the reported gains on unseen MIPLIB instances with a fixed solver and hardware budget.
2. Stress-test the method on oversized search trees and quantify the point at which graph encoding becomes the bottleneck.
3. Compare learned cut ordering and selection against strong adaptive baselines under identical time limits.
