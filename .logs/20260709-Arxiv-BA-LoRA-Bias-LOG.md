# Arxiv BA-LoRA Bias Log

## Run Summary

- Automation: Black Lake Arxiv DEP 1500
- Public run date: 2026-07-09
- Selected paper: BA-LoRA: Bias-Alleviating Low-Rank Adaptation to Mitigate Catastrophic Inheritance in Large Language Models
- Stable identifier: arXiv:2408.04556
- Authors: Yupeng Chang, Yi Chang, Yuan Wu
- Selection outcome: accepted after duplicate checks.

## Selection Method

- Candidate enumeration used `rg --files -g "*.pdf"` over the local arXiv archive.
- Candidate unit rule: each PDF parent directory was treated as one paper unit, with nearby README/metadata considered supporting metadata.
- Candidate count: 72,743 paper units.
- Random method: PowerShell `Get-Random` selected index 55,421 from the sorted paper-unit list.
- Selected unit metadata exposed arXiv ID `2408.04556` and a local README title matching the public arXiv page.

## Deduplication and Exclusions

- Same-paper duplicate markers found in `Black-Lake/.logs`: 0.
- Same-paper duplicate markers found in `Black-Lake/.reports`: 0.
- Same-paper duplicate markers found in `Black-Lake/.lake-data`: 0.
- Same-paper duplicate markers found in automation memory: 0; memory file was absent before this run.
- Same-paper duplicate markers found in related `Black-Lake-Data` code search: 0.
- Same-paper 24-hour exclusion markers: 0.
- Reselections required: 0.

## Evidence Reviewed

- Local arXiv archive metadata README for arXiv:2408.04556.
- Public arXiv abstract page for arXiv:2408.04556.
- Public arXiv HTML for method, results, limitations, ethics, and reproducibility sections.
- Official GitHub repository `llm172/BA-LoRA`, including README/file inventory and default-branch metadata.
- Live `Delphoa/Black-Lake` and `Delphoa-Labs/Black-Lake-Data` README contracts.
- Three related Black-Lake DEP entries selected for conceptual overlap.

## Output Paths

- `.logs/20260709-Arxiv-BA-LoRA-Bias-LOG.md`
- `.reports/BL-Arxiv-BA-LoRA-Bias-20260709/Report-Mark.md`
- `.lake-data/DEP-E-20260709-BA-LoRA Bias/README.md`
- `.lake-data/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md`

## Source Collection

No `.source/` folder was created. The local archive PDF and public arXiv/code sources were inspected, but source files were not redistributed because redistribution permissions were not independently verified for this deposit.

## Next-Review Questions

1. Does BA-LoRA's official code reproduce the main NLG and NLU tables when pinned to the recorded repository commit and current dependency versions?
2. How much of BA-LoRA's reported robustness comes from PiSSA initialization versus the three output-space regularizers under controlled ablations?
3. Can the noisy-pretraining hypothesis be retested with matched model architectures and objectives rather than RoBERTa/T5 comparisons?

## Challenges

1. The arXiv abstract reports v8 while the experimental HTML inspected exposed v7 text, so a later pass should verify version-specific differences.
2. The official code repository did not expose a license through the GitHub API, which limits redistribution and reuse assumptions.
3. Full reproduction would require model weights, datasets, compute, and dependency pinning that were out of scope for this public-safe DEP run.
