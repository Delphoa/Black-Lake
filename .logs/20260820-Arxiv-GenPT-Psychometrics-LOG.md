# Arxiv DEP Log - GenPT Psychometrics

## Public-Safe Run Summary

- Run date: 2026-08-20.
- Selected paper: *GenPT: Beyond Self-Report for Reliable LLM Psychometrics via Generative Projective Testing*.
- Authors: Ming Wang, Shuang Wu, Bixuan Wang, Lu Lin, Yuxin Chen, Xiaocui Yang, Daling Wang, Shi Feng, Yifei Zhang, and Yufan Sun.
- Identifier: arXiv:2606.00860v1; arXiv DOI [10.48550/arXiv.2606.00860](https://doi.org/10.48550/arXiv.2606.00860).
- Publication context: ACL 2026 version 2, DOI [10.18653/v1/2026.acl-long.1901](https://doi.org/10.18653/v1/2026.acl-long.1901).

## Selection and Deduplication

- Enumeration method: `rg --files -g "*.pdf"` against the local arXiv archive.
- Inventory: 75,967 PDFs collapsed to 75,964 unique PDF-parent paper units; 75,777 units had modern arXiv IDs; 187 identifier-incomplete units were withheld.
- Reconciliation scan: 11,811 Black Lake and automation-memory Markdown records; 3,681 normalized arXiv IDs observed; 1,937 matching units excluded before the draw; 73,840 units remained eligible.
- Random method: sort eligible parent units by stable path order, then use PowerShell `Get-Random` for one zero-based uniform index. Selected index: 660.
- Dedup result: arXiv ID, DOI, normalized title, GenPT slug, Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, and Black-Lake-Data searches found no owning deposit.
- Duplicate exclusions after draw: 0. Same-paper markers within the preceding 24-hour window: 0. Reselections: 0.

## Local Source Integrity Gate

- Initial state: partial. The valid PDF existed, but the full-paper HTML companion was missing.
- Repair: one bounded single-paper collector run fetched the official full-paper HTML through the approved archive broker while preserving the valid PDF.
- Verification: PDF 38,927,706 bytes, `%PDF-` header, trailing `%%EOF`; full-paper HTML 399,005 bytes, 95,298 visible body characters, document marker, 142 heading markers, and seven paper-structure terms; metadata HTML present; no partial files.
- Final source state: complete. The source package was unavailable after the bounded attempt and was not required for the complete PDF/full-paper HTML gate.
- Source policy: PDF, full-paper HTML, metadata HTML, provenance, verification, receipts, and any derived extraction remain local. No source file, source archive, cache, extracted source text, or `.source/` directory was uploaded, committed, or attached to Slack.

## Review Notes

- GenPT uses an Examinee → Interpreter → Diagnostician pipeline over newly generated TAT-like scenes, Rorschach-style cards, and sentence stems.
- The evaluation holds Stage 1 behavior and prompts fixed while comparing Qwen3-8B, Phi-4-mini-reasoning, and Intern-S1-mini for interpretation and diagnosis across personality and mental-health-risk tasks.
- Reported evidence favors complementarity: questionnaires remain stronger on clean-persona traits, while GenPT reduces the tested questionnaire-style directional drift on risk tasks and shows a large Qwen3-specific longitudinal depression shift.
- The main boundary is psychometric rather than clinical: small persona samples, backbone dependence, simulated agents, limited cultural coverage, and no evidence for diagnosing or profiling people.
- Official code and stimuli are publicly linked at [sci-m-wang/GenPT](https://github.com/sci-m-wang/GenPT), but no code, models, datasets, or experiments were executed in this run.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` - state traces, context replay, and runtime monitoring as review objects.
2. `.lake-data/DEP-E/DEP-E-20260728-Agent Reliability Gates/agent-reliability-gates.md` - calibrated validators, rejection, evidence gates, and intervention boundaries.
3. `.lake-data/DEP-E/DEP-E-20260717-OMGEval Benchmark/omgeval_benchmark_manuscript.md` - benchmark validity, judge uncertainty, human comparison, and reproducibility limits.

## Generated Outputs

- `.logs/20260820-Arxiv-GenPT-Psychometrics-LOG.md`
- `.reports/BL-Arxiv-GenPT-Psychometrics-20260820/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260820-GenPT Psychometrics/README.md`
- `.lake-data/DEP-E/DEP-E-20260820-GenPT Psychometrics/genpt_psychometrics_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Validation Status

- Manuscript schema: required headings, front matter, evidence ledger, identical title/H1, and exactly three exercise paths validated.
- Report-Mark contract: source metadata, evidence attribution, exactly three related DEP entries, Synthesis Note cardinalities, validation notes, and final Attribution Block included.
- DEP README: title, tags, public-safe context, contents, item summaries, insights, and final Attribution Block included.
- Public-output allowlist: only generated Markdown under `.logs`, `.reports`, and `.lake-data` is intended for staging; no PDF, HTML, source archive, cache, extracted text, or `.source/` path is permitted.

## Submission

- Repository: direct push to the default branch; remote commit verified at https://github.com/Delphoa/Black-Lake/commit/5d98b49245c319e626c0634f4a7535426520cb06.
- Slack: posted to `#black-lake-artifacts` at https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1787192501624359.
- Submission scope: five public Markdown artifacts only; no source files or `.source/` directory were uploaded.

## Exactly 3 Next-Review Questions

1. Can a larger and culturally diverse persona panel reproduce the risk-task advantage without turning projective outputs into clinical proxies?
2. Which interpreter/diagnostician calibration and abstention rules separate content responsiveness from prompt-induced noise?
3. Can a preregistered multi-judge and human-audit protocol quantify whether the generated stimuli are actually contamination-resistant?

## Exactly 3 Challenges

1. Preventing research instrumentation from being repurposed for non-consensual psychological profiling or high-stakes decisions about people.
2. Separating genuine context sensitivity from backbone-specific prompt variance when each risk task uses a small persona sample.
3. Reproducing the full pipeline without redistributing sensitive dialogue data, licensed instruments, or private model credentials.

## Attribution Block

- Source URL: https://arxiv.org/abs/2606.00860
  - Applies to: paper identity, authors, abstract, version, and source locator.
- Source URL: https://arxiv.org/html/2606.00860
  - Applies to: full-paper method, experiments, results, limitations, and ethics review.
- Source URL: https://aclanthology.org/2026.acl-long.1901/
  - Applies to: ACL publication context, version 2, venue, and DOI.
- Source URL: https://github.com/sci-m-wang/GenPT
  - Applies to: official implementation and public artifact availability.
- Source files: withheld locally; none were uploaded or deposited.
