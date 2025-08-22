
import csv, re, requests, sys, pathlib
from jinja2 import Environment, FileSystemLoader

# ===== CONFIG =====
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRGlLulWGbqHPglvKSZDDck8wkRtPKZjcinGGTc3RZg_4iyGOq5KLOoVekclucPwNOV_T44Ikkz_8gU/pub?gid=1164815538&single=true&output=csv"

# Column headers as they appear in your sheet
COLS = {
    "Email Address": "email",
    "Workgroup": "workgroup",
    "Full name of instrument": "name",
    "Acronym or short name (if applicable)": "acronym",  
    "Name of Instrument as you would like it to appear in the table of contents and the top of the page": "title",
    "Table name (as it appears on Lasso preferred if known)": "table_name",
    "Construct, e.g. Mental health (if applicable)": "construct",
    "Child Specific? (Administration & Quality Control)": "child_specific",
    "Respondent (Administration & Quality Control)": "respondent",
    "Administration method (Administration & Quality Control) - SELECT ALL THAT APPLY": "administration",
    "Visits administered (Administration & Quality Control) - SELECT ALL THAT APPLY": "visits",
    "Completion time (Administration & Quality Control)": "completion_time",
    "Quality Control Procedures": "quality_control",
    "If needed: upload file(s) for quality control description": "qc_file",
    "INSTRUMENT DETAILS": "instrument_details",
    "Scoring Procedures - OPTION 1 - enter text in form": "scoring_procedures",
    "Scoring Procedures - OPTION 2 - Upload a file": "scoring_file",
    "Responsible Use Warning": "responsible_use",
    "Data Warning": "data_warning",
    "References": "references",
    "Detailed instruction, assessment item, and scoring changes": "hbcd_modifications",
    "Additional comments/questions you have about this form": "additional_comments",
    "Additional files you would like to provide (please explain what each is under Additional comments/questions)": "additional_files"
}

TEMPLATE_DIR = pathlib.Path("templates")
TEMPLATE_NAME = "instrument.md.j2"

OUT_DIR = pathlib.Path("new_pages")   # same folder as script; change to "instruments" if desired
SKIP_EMPTY_NAMES = True
OVERWRITE_FILES = True

# ===== UTIL =====
def slugify(s: str) -> str:
    s = s.strip().lower().replace("&", "and")
    s = re.sub(r"[^\w\- ]+", "", s)
    s = re.sub(r"\s+", "-", s)
    return s[:80].strip("-") or "instrument"

def coerce_links(row: dict):
    links = []
    if row.get("link1_label") and row.get("link1_url"):
        links.append((row["link1_label"], row["link1_url"]))
    if row.get("link2_label") and row.get("link2_url"):
        links.append((row["link2_label"], row["link2_url"]))
    return links

def read_rows():
    resp = requests.get(CSV_URL, timeout=30)
    resp.raise_for_status()
    lines = resp.text.splitlines()
    return list(csv.DictReader(lines))

def main():
    rows = read_rows()
    if not rows:
        sys.exit("No rows found in CSV.")

    # Check required columns exist in CSV
    required = [k for k,v in COLS.items() if v in ("name","description")]
    missing = [col for col in required if col not in rows[0].keys()]
    if missing:
        sys.exit(f"ERROR: Missing expected column(s): {missing}")

    # Prepare template env
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
    tpl = env.get_template(TEMPLATE_NAME)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    created, skipped = 0, 0

    for raw in rows:
        # Map sheet headers -> internal keys
        row = {internal: (raw.get(sheet_col) or "").strip()
               for sheet_col, internal in COLS.items()}

        name = row.get("name", "")
        if SKIP_EMPTY_NAMES and not name:
            skipped += 1
            continue

        # Build derived fields
        row["links"] = coerce_links(row)

        # Render page
        slug = slugify(name or "instrument")
        out_path = OUT_DIR / f"{slug}.md"
        if out_path.exists() and not OVERWRITE_FILES:
            skipped += 1
            continue

        out_path.write_text(tpl.render(**row), encoding="utf-8")
        created += 1

    print(f"Done. Created/updated: {created} | Skipped: {skipped}")

if __name__ == "__main__":
    main()