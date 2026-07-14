# Active arXiv inventory

`.lists` is the active, concise inventory for the local arXiv author archive. It is a metadata index only: it contains paper titles, public arXiv URLs, one-line descriptions, archive-created dates, author names, and update markers. PDFs, HTML pages, source packages, extraction caches, and other physical source records remain outside this repository.

## Update process

The daily local automation advances through one author at a time in sorted rotation. It stores only the rotation cursor in the local archive, not in this repository. The automation follows this order:

1. Select the next author directory with a local `_download-summary.csv`.
2. Read that author’s stored search URL, or derive the arXiv author-search URL from the directory name.
3. Run the `arxiv-bulk-author-archive` collector for that one author. The daily run uses the normal bulk output and does not collect companion artifacts for every paper.
4. Require a successful collector exit and `status=ok` for the selected author batch.
5. Read every author `_download-summary.csv`, keep only paper folders currently present in the local archive, and resolve full author names from cached local PDF/arXiv metadata when needed. The generator fails closed if it can only identify an abbreviated author name.
6. Write `index.md` at this level and one `index.md` inside each full-name author folder, then advance the local rotation cursor.

The inventory step is downstream of the archive step. If the archive run fails or any batch row is not `ok`, `.lists` is not updated.

## Inventory layout

```text
.lists/
  README.md
  index.md
  Full Author Name/
    index.md
```

`index.md` is the root summary. Each author index contains a compact table with these fields:

| Field | Meaning |
| --- | --- |
| `change` | `new`, `updated`, or `existing` compared with the preceding author index. |
| `title` | Full paper title. |
| `arxiv_url` | Public arXiv abstract URL. |
| `description` | One-line local abstract excerpt, or an explicit availability note. |
| `archived_date` | Date the paper folder was created in the local archive. |

Each index has a metadata header containing `repo_last_updated`, `local_archive_last_updated`, `documents_previously_counted`, the current document count, added/updated/removed counts, `update_status`, and an inventory fingerprint. `update_status` is `initial`, `changed`, or `unchanged`, so a reader can identify an inventory update without opening source records.

The active root index lists only authors currently represented by the local archive batch summary. Existing source folders are never copied into `.lists`, and the scheduled job does not delete older inventory folders automatically.
