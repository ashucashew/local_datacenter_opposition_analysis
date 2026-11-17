"""Summarize data/projects.csv.

Usage:  python3 analysis/summarize.py            (prints tables)
        python3 analysis/summarize.py --md FILE  (also writes a markdown copy)

Reruns cleanly whenever rows in data/projects.csv change. Standard library only.
MW and $ totals use only rows where the value is reported; the 'n_mw' / 'n_usd'
columns show how many rows contributed, so blanks are never silently zero.
"""
import csv
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "projects.csv"
STATUS_FIELDS = ["tenant_named", "land_status", "power_status",
                 "permits_or_financing", "developer_other_regional_sites"]


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def primary(mech):
    return mech.split(";")[0].strip() if mech else ""


def group(rows, key):
    out = OrderedDict()
    for r in sorted(rows, key=lambda r: key(r)):
        out.setdefault(key(r), []).append(r)
    return out


def stats(rows):
    mws = [num(r["size_mw"]) for r in rows if num(r["size_mw"]) is not None]
    usd = [num(r["announced_value_usd"]) for r in rows if num(r["announced_value_usd"]) is not None]
    return len(rows), sum(mws), len(mws), sum(usd) / 1e9, len(usd)


def table(title, rows, key, out):
    out.append(f"\n### {title}\n")
    out.append("| value | projects | MW | n_mw | $B | n_usd |")
    out.append("|---|---:|---:|---:|---:|---:|")
    for k, g in group(rows, key).items():
        n, mw, nmw, b, nb = stats(g)
        out.append(f"| {k or '(blank)'} | {n} | {mw:,.0f} | {nmw} | {b:,.1f} | {nb} |")
    n, mw, nmw, b, nb = stats(rows)
    out.append(f"| **total** | {n} | {mw:,.0f} | {nmw} | {b:,.1f} | {nb} |")


def share(rows, pred):
    """Share of projects, and share of reported MW, satisfying pred."""
    hit = [r for r in rows if pred(r)]
    tot_mw = sum(num(r["size_mw"]) or 0 for r in rows)
    hit_mw = sum(num(r["size_mw"]) or 0 for r in hit)
    return len(hit), len(rows), (hit_mw / tot_mw if tot_mw else 0)


def main():
    rows = list(csv.DictReader(open(DATA, newline="")))
    out = [f"# Sample summary ({len(rows)} projects)\n",
           f"Human-verified rows: {sum(r['human_verified'] == 'yes' for r in rows)} of {len(rows)}. "
           "All figures are provisional until every row is verified."]

    dims = [("Primary mechanism", lambda r: primary(r["mechanism"])),
            ("Realness tier", lambda r: r["realness_tier"]),
            ("Outcome", lambda r: r["outcome"]),
            ("Passes SemiAnalysis filter", lambda r: r["passes_semianalysis_filter"])]

    out.append("\n## 1. All projects")
    for t, k in dims:
        table(t, rows, k, out)

    out.append("\n## 2. By period (n≈10 each: suggestive, not conclusive)")
    for period, g in group(rows, lambda r: r["period"]).items():
        out.append(f"\n#### Period {period}")
        for t, k in dims:
            table(f"{t} ({period})", g, k, out)

    out.append("\n## 3. Key shares (share of projects; share of reported MW)")
    checks = [("(a) speculative", lambda r: r["realness_tier"] == "speculative"),
              ("(b) non-moratorium primary mechanism",
               lambda r: primary(r["mechanism"]) not in ("moratorium", "state_action")),
              ("(c) explicitly relocated", lambda r: r["outcome"] == "relocated"),
              ("(extra) proceeding despite opposition", lambda r: r["outcome"] == "proceeding"),
              ("(extra) passes SemiAnalysis filter = yes",
               lambda r: r["passes_semianalysis_filter"] == "yes")]
    out.append("\n| measure | all: projects | all: MW share | 2025 | 2026 |")
    out.append("|---|---|---:|---|---|")
    by_p = group(rows, lambda r: r["period"])
    for label, pred in checks:
        h, n, s = share(rows, pred)
        per = []
        for p in ("2025", "2026"):
            ph, pn, ps = share(by_p.get(p, []), pred)
            per.append(f"{ph}/{pn} ({ps:.0%} MW)")
        out.append(f"| {label} | {h}/{n} | {s:.0%} | {per[0]} | {per[1]} |")

    unk = sum(r[f] == "unknown" for r in rows for f in STATUS_FIELDS)
    out.append(f"\nUnknowns: {unk} of {len(rows) * len(STATUS_FIELDS)} values "
               f"({unk / (len(rows) * len(STATUS_FIELDS)):.0%}) in {', '.join(STATUS_FIELDS)}.")
    out.append(f"Rows missing MW: {sum(num(r['size_mw']) is None for r in rows)}; "
               f"missing $: {sum(num(r['announced_value_usd']) is None for r in rows)}.")

    out.append("\n## 4. Essay table\n")
    out.append("| | 2025 | 2026 | All |")
    out.append("|---|---|---|---|")
    def cell(g, pred=lambda r: True):
        g2 = [r for r in g if pred(r)]
        n, mw, _, _, _ = stats(g2)
        return f"{n} ({mw:,.0f} MW)"
    lines = [("Projects in sample", lambda r: True),
             ("Speculative", checks[0][1]),
             ("Non-moratorium mechanism", checks[1][1]),
             ("Proceeding despite opposition", checks[3][1]),
             ("Counts as delayed under SemiAnalysis filter", checks[4][1]),
             ("Explicitly relocated", checks[2][1])]
    for label, pred in lines:
        out.append(f"| {label} | {cell(by_p.get('2025', []), pred)} | "
                   f"{cell(by_p.get('2026', []), pred)} | {cell(rows, pred)} |")

    text = "\n".join(out)
    print(text)
    if "--md" in sys.argv:
        Path(sys.argv[sys.argv.index("--md") + 1]).write_text(text + "\n")


if __name__ == "__main__":
    main()
