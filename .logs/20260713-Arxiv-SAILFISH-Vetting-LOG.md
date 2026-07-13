# Arxiv DEP Job Log: SAILFISH Vetting

## Public-Safe Run Context

- `Deposit date`: 2026-07-13.
- `Selected paper`: arXiv:2104.08638v2, *SAILFISH: Vetting Smart Contract State-Inconsistency Bugs in Seconds*.
- `Authors`: Priyanka Bose, Dipanjan Das, Yanju Chen, Yu Feng, Christopher Kruegel, and Giovanni Vigna.
- `Venue`: 2022 IEEE Symposium on Security and Privacy, pages 161-178.
- `DOI`: https://doi.org/10.1109/SP46214.2022.9833721.
- `Review scope`: Source-first defensive security review; no exploit payloads were reproduced or operationalized.

## Random Selection and Eligibility

- `Paper unit`: Each unique parent directory containing at least one PDF was treated as one candidate.
- `Enumeration`: `rg --files -g "*.pdf"` found 75,761 PDF-backed paper units.
- `Selection method`: PowerShell `Get-Random` selected one uniform zero-based index from the complete candidate list.
- `Selected index`: 8,874.
- `Candidate PDF count`: One PDF in the selected paper unit.
- `Exclusions`: 0.
- `Reselections`: 0.
- `Identifier derivation`: The adjacent metadata README and PDF filename yielded arXiv:2104.08638; the normalized title was derived from the README and verified against arXiv.

## Dedup Validation

- The public dedup index contained no matching arXiv ID, DOI, normalized title, or slug before this deposit.
- Black Lake `.logs`, `.reports`, and `.lake-data` contained no matching Arxiv DEP artifacts.
- Automation memory contained no matching paper marker.
- Black-Lake-Data contained no matching ID or normalized title marker.
- No same-paper marker was found in other active worktree records within the 24-hour exclusion window.
- `Result`: Eligible on the first draw.

## Extraction and Evidence Review

- `Initial cache`: Miss.
- `Refresh mode`: `missing-only`.
- `Extractor`: `pypdf` succeeded after `pdftotext` was unavailable.
- `Cache result`: Partial; 117,020 bytes of PDF text were extracted, while local HTML and source-package text were absent.
- `Paper evidence inspected`: Abstract, introduction, problem definition, EXPLORE/SDG analysis, hazardous-access queries, REFINE/value-summary analysis, implementation, evaluation tables, ablation, limitations, conclusion, and appendices.
- `Public primary records inspected`: arXiv metadata, author-hosted paper, IEEE/DOI metadata, UCSB SecLab publication record, and the official code/data repository.
- `Released artifacts`: The official repository states that it contains code and experimental data and documents a Docker-based execution path. The code and experiments were not executed in this review.
- `Source files collected for deposition`: None; no `.source/` directory was created.

## Exactly Three Related DEP Entries

1. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260702-Tech Intel 1102/daily_research_findings_2026-07-02_1102.md` - Antaeus overlaps through staged repository-scale security triage: lightweight prioritization reduces the expensive reasoning surface, followed by context-grounded validation and evidence-linked findings.
2. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260626-Tech Intel 1103/daily_research_findings_2026-06-26_1103.md` - Chai overlaps through graph-based vulnerability reasoning and validation: library discrepancies become candidate signals that are propagated through a dependency graph and then tested for concrete security meaning.
3. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260706-Tech Intel 0104/daily_research_findings_2026-07-06_0104.md` - VeriChat overlaps through hybrid assurance: conversational reasoning is bounded by syntax, synthesis, simulation, and formal-verification tools, echoing SAILFISH's separation of broad discovery from precise feasibility checking.

## Outputs

- `.logs/20260713-Arxiv-SAILFISH-Vetting-LOG.md`
- `.logs/20260713-Arxiv-SAILFISH-Vetting-PHASE-LOG.md`
- `.reports/BL-Arxiv-SAILFISH-Vetting-20260713/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260713-SAILFISH Vetting/README.md`
- `.lake-data/DEP-E/DEP-E-20260713-SAILFISH Vetting/sailfish_vetting_manuscript.md`
- `.staging/arxiv-dep-dedup-index.json`

## Submission

- `Repository result`: Direct push to the default branch succeeded.
- `Artifact commit`: https://github.com/Delphoa/Black-Lake/commit/7e651d7.
- `Slack notification`: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1783923556974429.
- `Blockers`: None. The released analyzer and experimental data were not executed, which remains a validation shortfall rather than a submission blocker.

## Next-Review Questions

1. Does the released repository reproduce the paper's 89,853-contract aggregate results under its pinned Docker environment, including the reported timeout and error categories?
2. How do current Solidity compiler behavior, proxy patterns, and post-2020 contract idioms change SAILFISH's taint, call-graph, and state-summary precision?
3. Can hazardous-access candidates be paired with proof-producing or differential validation so that false positives and unsoundness are measured on a newer independently labeled corpus?

## Challenges

1. PDF text extraction preserved the full review surface but introduced typography and mathematical-symbol encoding noise.
2. The evaluation is historically substantial yet tied to contracts collected through 2020, older Solidity versions, and dependencies whose present compatibility was not tested.
3. The released code and data were inspected at the repository-documentation level but not executed, so this deposit does not independently reproduce performance, precision, or zero-day findings.
