# arXiv DEP Log: Off-Aperture RGBD

- `Run date`: 2026-07-30
- `Selected paper`: *Learned Off-aperture Encoding for Wide Field-of-view RGBD Imaging* — arXiv:2507.22523
- `Selection method`: `rg --files -g "*.pdf"` found 75,959 PDFs. Their 75,956 unique parent directories were sorted, then a uniform PowerShell `Get-Random` draw selected zero-based index 30,138.
- `Source state`: repaired from partial to complete. The existing PDF passed the size, header, and EOF checks; the bounded brokered repair added verified metadata and full-paper HTML. Source-package retrieval was unavailable; this did not affect the complete-paper gate.

## Dedup and Reselection Validation

The arXiv ID, arXiv DOI, normalized title, and slug were checked against live Black-Lake `.logs`, `.reports`, `.lake-data`, `.staging`, this automation's history, and relevant Black-Lake-Data entries. No processed DEP or 24-hour same-paper marker matched. Black-Lake-Data contained one metadata-only inventory row, which is not a processed deposit. The first draw was accepted: 0 duplicate exclusions, 0 other exclusions, and 0 reselections.

## Output Paths

- `.logs/20260730-Arxiv-Off-Aperture-RGBD-LOG.md`
- `.reports/BL-Arxiv-Off-Aperture-RGBD-20260730/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260730-Off-Aperture RGBD/README.md`
- `.lake-data/DEP-E/DEP-E-20260730-Off-Aperture RGBD/off_aperture_rgbd_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next Review Questions

1. How does optical performance vary across repeated fabrication batches, illumination spectra, temperature, and mechanical remounting?
2. Can DOE position, refractive surfaces, and decoders be jointly optimized within a measured compute and memory budget?
3. Does active-depth ground truth change the RGBD conclusions compared with semantic-model-assisted fine-tuning?

## Challenges

1. Wide-angle double propagation makes fully end-to-end refractive-plus-diffractive optimization expensive.
2. Fabrication and assembly imperfections introduce haze and halo artifacts that simulation does not fully represent.
3. The reported prototypes and selected datasets do not establish robustness for safety-critical perception.
