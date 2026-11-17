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


BROAD = ROOT / "data" / "broad_list.csv"


def broad_section():
    """Light-coded list of every project named in Data Center Watch's free briefings."""
    if not BROAD.exists():
        return []
    b = list(csv.DictReader(open(BROAD, newline="")))
    out = [f"\n## 5. Broad list: projects named in DCW free briefings ({len(b)} projects)\n",
           "Coded from briefing text only (status as DCW reported it); not human-verified.\n"]
    out.append("| status at report | 2025 | 2026 | all |")
    out.append("|---|---:|---:|---:|")
    for s in ["blocked", "delayed", "contested", "proceeding"]:
        c = [sum(1 for r in b if r["status_at_report"] == s and (p is None or r["period"] == p))
             for p in ("2025", "2026", None)]
        out.append(f"| {s} | {c[0]} | {c[1]} | {c[2]} |")
    bd = [r for r in b if r["status_at_report"] in ("blocked", "delayed")]
    n = len(bd)
    out.append(f"\nAmong the {n} blocked or delayed projects:")
    mech = {}
    for r in bd:
        k = primary(r["mechanism"])
        mech[k] = mech.get(k, 0) + 1
    out.append("- primary mechanism: " + ", ".join(f"{k} {v}" for k, v in sorted(mech.items(), key=lambda x: -x[1])))
    nm = sum(r["end_user_named"] == "yes" for r in bd)
    rum = sum(r["end_user_named"] == "rumored" for r in bd)
    out.append(f"- end user named: {nm}/{n} ({nm / n:.0%}); rumored only: {rum}")
    out.append(f"- MW reported: {sum(bool(r['size_mw']) for r in bd)}/{n}; "
               f"$ reported: {sum(bool(r['announced_value_usd']) for r in bd)}/{n}")
    usd = sum(float(r["announced_value_usd"]) for r in bd if r["announced_value_usd"])
    out.append(f"- sum of reported $: ${usd / 1e9:,.1f}B")
    out.append(f"- also in core sample: {sum(bool(r['core_project_id']) for r in bd)}/{n}")
    nl = sum(r["mechanism"] == "state_action" for r in bd)
    out.append(f"- paused for non-local reasons (state tax policy etc.): {nl}")
    return out


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

    out += broad_section()
    text = "\n".join(out)
    print(text)
    if "--md" in sys.argv:
        Path(sys.argv[sys.argv.index("--md") + 1]).write_text(text + "\n")


if __name__ == "__main__":
    main()
