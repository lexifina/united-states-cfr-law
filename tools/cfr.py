"""Prints the Code of Federal Regulations as it stood on a given day, read from this repository's history.

    python tools/cfr.py 2024-06-01 "12 CFR 1026.43"     # one section (file title-12-part-1026/sec-0043.md)
    python tools/cfr.py 2024-06-01 "12 CFR 1026"        # a whole part
    python tools/cfr.py --law 2024-06-01 "17 CFR 240.10b-5"   # also name who is credited for the version shown

A thin wrapper around tools/on.py: the version is chosen by each commit's `In-force:` trailer, never by its commit
date. Standard library only.
"""
import re
import runpy
import sys
from pathlib import Path


def pad(s: str) -> str:
    return re.sub(r'\d+', lambda m: m.group(0).zfill(4), re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-'))


def target(ref: str) -> list[str]:
    m = re.fullmatch(r'\s*(\d+)\s*C\.?F\.?R\.?\s*(?:§+\s*|part\s+)?([0-9A-Za-z]+)(?:\.(\S+))?\s*', ref, re.I)
    if not m:
        return ref.split()
    act = f'title-{int(m.group(1)):02d}-part-{pad(m.group(2))}'
    return [act, f'sec-{pad(m.group(3))}'] if m.group(3) else [act]


if __name__ == '__main__':
    args = sys.argv[1:]
    flags = [a for a in args if a.startswith('--')]
    rest = [a for a in args if not a.startswith('--')]
    if not rest:
        sys.exit(__doc__)
    day, refs = rest[0], rest[1:]
    sys.argv = [str(Path(__file__).with_name('on.py')), *flags, day] + (target(' '.join(refs)) if refs else [])
    runpy.run_path(sys.argv[0], run_name='__main__')
