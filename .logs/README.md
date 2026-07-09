# .logs

Operational logs for Black Lake repository activity.

Use this directory for:

- deposition run logs
- source-processing logs
- review traces
- ingestion notes
- verification logs
- blocker reports
- public-safe Arxiv DEP phase logs

Logs are supporting material, not canonical DEP entries. When a log supports a DEP, reference the DEP path clearly in the log filename or body.

Suggested filename format:

```text
YYYYMMDD-HHMM-short-subject.md
```

For Arxiv DEP phase metrics, use:

```text
YYYYMMDD-Arxiv-{paper-slug}-PHASE-LOG.md
```

Phase logs may include elapsed durations, counts, cache status, extractor/fallback status, expected-duration comparisons, and shortfalls. Do not include local paths, home directories, usernames, drive-letter paths, machine names, local workspace roots, local timezone labels, or exact local execution timestamps.
