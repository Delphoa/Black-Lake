# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260731-3D09E72F`
- Deployment item ID: `BLAD-2200-20260731-3D09E72F-P02`
- Public-safe date: 2026-07-31
- Paper: *Generalizable CT-Free PET Attenuation and Scatter Correction for Pediatric Patients*
- Identifier: `arXiv:2604.22894`; DOI: `10.48550/arXiv.2604.22894`
- URL: https://arxiv.org/abs/2604.22894

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 52,315 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Generalizable-CT-Free-PET-Attenuation-and` slug; the 24-hour marker cutoff was 2026-07-30.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 20,550,352 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 315,386 bytes, 71,096 body characters, 49 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260731-Arxiv-Generalizable-CT-Free-PET-Attenuation-and-LOG.md`
- `.reports/BL-Arxiv-Generalizable-CT-Free-PET-Attenuation-and-20260731/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260731-Generalizable CT-Free PET/README.md`
- `.lake-data/DEP-E/DEP-E-20260731-Generalizable CT-Free PET/generalizable_ct_free_pet_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260722-GenTune Traceable Prompts/gentune_traceable_prompts_manuscript.md` - GenTune Traceable Prompts Review - DEP-E; overlap: refinement, improve, environment, design.
2. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` - Acoustic Phase Retrieval - DEP-E; overlap: recovery, fourier, phase, reconstruction.
3. `.lake-data/DEP-E/DEP-E-20260720-Context Backdoor/context_backdoor_defense_manuscript.md` - Context Backdoor Defense - DEP-E; overlap: contextual, defense, context.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
