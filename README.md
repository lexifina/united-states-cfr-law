# The Code of Federal Regulations, as a git repository

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the US Code of Federal Regulations, which global-law reads at `united-states/federal/cfr/`.

The Code of Federal Regulations (CFR), one file per section or appendix, as a git history from the 2017 annual editions to today's eCFR. Each change is a commit dated the day it took effect and, where the section's source note names it, authored by the Federal Register document that made it. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `united-states/cfr/acts`.

Titles are added one at a time; the titles held so far are those with a `title-NN-part-*` folder.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did 12 CFR 1026.43 say on 1 June 2022? | `python tools/cfr.py 2022-06-01 "12 CFR 1026.43"` |
| A whole part on a day | `python tools/cfr.py 2022-06-01 "12 CFR 1026"` |
| Every change to a section | `git log -p -- title-12-part-1026/sec-0043.md` |
| Which rule wrote each line | `git blame title-12-part-1026/sec-0043.md` |
| Everything one Federal Register document changed | `git log --author="89 FR 64577"` |

Files: each CFR part is a folder, `title-12-part-1026/`; a section is `sec-<number after the dot>.md` with every run of digits padded to four (12 CFR 1026.43 is `sec-0043.md`, 17 CFR 240.10b-5 is `title-17-part-0240/sec-0010b-0005.md`); an appendix or supplement is `appendix-a.md`, `supplement-i.md`. `tools/cfr.py` finds the file for you. Each file starts with the section's heading as printed, then one paragraph or table row per line (cells joined by ` | `).

## Dates and authors

The text comes from the official annual edition of each title (revised once a year, as of 1 January, 1 April, 1 July or 1 October depending on the title) and from today's eCFR. Between two editions, each section whose words changed is dated by the eCFR's record of the day that section's amendment took effect:

- **Changed once in the window.** The commit is dated that day and credited to the Federal Register document the section's source note gained.
- **Changed more than once.** The text in between is not available from a source this record may use, so the commit on the last day carries the later edition's text, is credited to every document the source note gained, and its note lists every day the section changed.
- **No recorded date, or no document named.** The change is labelled unexplained and authored by the Office of the Federal Register (at an address that cannot exist).

Each title starts with its first edition (2017), credited to the publisher as the oldest version available. Commits are dated at noon, America/New_York, and carry the day in an `In-force:` trailer, which the tools read.

## Date erratum

The historical commit `3a9ab1d40ba7b0f8c5985f5853e88fdfb9594c9a` records 22 March 2024 as the publication date of 89 FR 18543. The [official eCFR source notes for 32 CFR 161.5 and 161.23](https://www.govinfo.gov/bulkdata/ECFR/title-32/ECFR-title32.xml) cite that document as published on 14 March 2024. The commit's publication date is incorrect; its recorded `In-force: 2024-03-15` date has not been changed. The source notes do not establish a separate signing date.

## What it does not show

- Text before 2017, and the text between two changes to one section in the same edition year.
- Source notes, authority citations at the head of each part, editorial notes, effective-date notes and footnotes.
- Changes that alter only punctuation or spacing: two renderings with the same letters and digits count as the same.
- The Federal Register preambles that explain each rule; follow the `Source:` link in a commit for the document.

This is a research aid. For anything that matters, read the official edition at govinfo.gov or the eCFR.

## How it is checked and built

See [REPRODUCE.md](REPRODUCE.md): the sources, the build steps and the checks. No AI model wrote, dated or credited any text.

## Reuse

The text of the CFR is a work of the United States Government and carries no copyright (17 U.S.C. 105). The arrangement of the history, the commit messages, the tools and the documentation are © Lexifina, released under CC BY 4.0; see [LICENSE](LICENSE).

Built by [Lexifina](https://lexifina.com). For corrections, open an issue.
