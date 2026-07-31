# STAAR Design Document Pack

## Final PDF (submit / compose this)

**[`Forensic-Sketch-Generator-STAAR-Design-Document.pdf`](./Forensic-Sketch-Generator-STAAR-Design-Document.pdf)** — **13 pages**

| Pages | Content |
|-------|---------|
| 1–3 | From `Research_paper1-3.pdf` (Title, Acknowledgement, Abstract) |
| 4+ | Problem Specification → Introduction → Literature Survey → Research Gap → Proposed Solution (Figure 1) → Results & Discussion → References |

**Style:** Times New Roman · maroon `#8A2400` · navy `#1F3863` (matched to cover PDF)

**Excluded (per request):** interim summary · experimental outcome tables

## Cover source

`Research_paper1-3.pdf` — locked first three pages merged as-is.

## Rebuild

```bash
python docs/interim-review/scripts/build_full_pdf.py
```

## Section markdown drafts

| File | Section |
|------|---------|
| `01-problem-specification.md` | Problem Specification |
| `02-introduction.md` | Introduction |
| `03-literature-survey.md` | Literature Survey |
| `04-research-gap.md` | Research Gap |
| `05-proposed-solution.md` | Proposed Solution |
| `06-results-and-discussion.md` | Results notes (PDF uses projected discussion only) |

## Figures

- `figures/figure1-system-architecture-bw.png` — block diagram embedded in PDF
