import html
import os
import markdown
import re
from datetime import datetime
from utils import load_and_filter

# NEW VERSION OF parse-by-domains.py that parses text documenting issues from a separate google sheet and matches issue based on ID#
os.chdir(os.path.dirname(os.path.abspath(__file__)))   

XLSX= "latest.xlsx"
# Parse text describing issue from google sheet
sheet_id = "1P6QFJaZjb-F5roWkzQXkoGFW1E95t9rge6RfNmmKozc"
sheet_gid = "0"
# Populate known issues page
HBCD_DOCS_MD = "../docs/changelog/issues-updates.md"

# FUNCTIONS
def map_type(value):
    if "issue" in value:
        return "Issue"
    elif "pending" in value:
        return "Pending Update"
    return None

def format_pr(pr):
    """Normalize numeric Target (PR) values to always show one decimal (e.g. '3' -> '3.0')."""
    if not pr:
        return "TBD"
    if pr != "TBD" and "." not in pr:
        try:
            float(pr)
            pr = f"{pr}.0"
        except ValueError:
            pass
    return pr

def target_sort_key(pr):
    """Sort Target (PR) values numerically ascending, with TBD sorted last."""
    pr = str(pr)
    if pr.upper() == "TBD":
        return (1, 0.0)
    try:
        return (0, float(pr))
    except ValueError:
        return (0, pr)

def insert_into_markdown(md_path, combined_html):
    START_MARKER = "<!-- BEGIN KNOWN_ISSUES_TABLE -->"
    END_MARKER = "<!-- END KNOWN_ISSUES_TABLE -->"

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_index = content.find(START_MARKER)
    end_index = content.find(END_MARKER)
    end_index += len(END_MARKER)

    new_content = (
        content[:start_index]
        + START_MARKER
        + combined_html
        + END_MARKER
        + content[end_index:]
    )
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Known issues table successfully updated.")

# Generate HTML tables 
def build_table(domain, rows):
    table_parts = []

    domain_esc = html.escape(domain)
    table_parts.append(f"""
<table class="compact-table-no-vertical-lines archive-table" data-domain="{domain_esc}">
<caption class="archive-table-title">{domain_esc}</caption>
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>
""")

    for issue_type, table, summary_html, pr in rows:
        type_attr = "issue" if issue_type == "Issue" else "update"
        table_parts.append(f'<tr data-domain="{domain_esc}" data-type="{type_attr}">')
        if issue_type == "Issue":
            type_label = '<i class="fas fa-bug icon-bug"></i>'
        else:
            type_label = '<i class="fa-solid fa-rotate icon-rotate"></i>'
        table_parts.append(f"<td>{type_label}</td>")
        table_parts.append(f"<td>{html.escape(str(table))}</td>")
        table_parts.append(f"<td>{summary_html}</td>")
        table_parts.append(
            f"<td style='text-align: center;'><span class='pill'>{html.escape(str(pr))}</span></td>"
        )
        table_parts.append("</tr>")
    table_parts.append("</tbody></table>")

    return "\n".join(table_parts)

# WORK
df = load_and_filter(XLSX, sheet_id, sheet_gid)
df = df[df["PR"] != "3"]

# Type mapping and sort by (1) domain, (2) table/topic
df["MappedType"] = df["Type"].apply(map_type)
df = df[df["MappedType"].notna()]
df = df.sort_values(by=['Domain', 'Table/Topic'])

# Build grouped structure (by domain only)
grouped_by_domain = {}

for _, row in df.iterrows():
    domain = row["Domain"]
    issue_type = row["MappedType"]
    table = row["Table/Topic"]
    summary_md = row["Text"]
    pr = format_pr(row["PR"])

    # Convert Markdown → HTML & strip outer <p>
    summary_html = markdown.markdown(
        summary_md,
        extensions=["extra", "sane_lists"]
    )
    summary_html = re.sub(r'^<p>(.*)</p>$', r'\1', summary_html, flags=re.DOTALL)

    grouped_by_domain.setdefault(domain, []).append(
        (issue_type, table, summary_html, pr)
    )

# Generate known issues and pending tables for internal page
table_configs = [
    ("Issue",
     '<i class="fas fa-bug icon-bug"></i> Known Issues'),
    ("Pending Update",
     '<i class="fa-solid fa-rotate icon-rotate"></i> Pending Updates'),
]

def build_combined_tables():
    tables = []

    for domain in sorted(grouped_by_domain.keys()):
        rows = grouped_by_domain[domain]
        # Sort within domain by Target (PR), then type, then Table/Topic
        rows = sorted(rows, key=lambda x: (target_sort_key(x[3]), x[0], x[1]))
        tables.append(build_table(domain, rows))

    return "\n\n".join(tables)

# Make table and insert into markdown
combined_tables_html_int = build_combined_tables()
insert_into_markdown(HBCD_DOCS_MD, combined_tables_html_int)


# df.to_csv("debug.tsv", sep='\t', index=False)
