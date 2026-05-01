import pandas as pd
import html
import os
import markdown
import numpy as np
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))   

XLSX= "latest.xlsx"
HBCD_DOCS_MD = "../docs/changelog/issues-updates.md"

# HBCD_DOCS_MD = "../docs/changelog/test.md"


# FUNCTIONS

def load_and_filter_xlsx(xlsx_path):
    """
    Load XLSX file, rename columns, filter rows, fill missing values, and strip whitespace.
    """
    df = pd.read_excel(xlsx_path, dtype=str)
    df = df.rename(columns={
    "RTDs": "Type",
    "RTDs Text (markdown format)": "Text"})

    # Filter - only include items marked for autoparsing
    df = df[df['Autoparsed?'].str.contains('Yes')]

    # Fill missing values and strip whitespace 
    df = df.fillna('')
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    return df

def map_type(value):
    if value == "known_issue":
        return "Issue"
    elif value == "pending":
        return "Pending Update"
    return None


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

    table_parts.append(f"\n### {html.escape(domain)}")
    table_parts.append("""
<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>
""")

    for issue_type, table, summary_html, pr in rows:
        table_parts.append("<tr>")
        if issue_type == "Issue":
            type_label = '<i class="fas fa-bug icon-bug"></i>'
        else:
            type_label = '<i class="fa-solid fa-rotate icon-rotate"></i>'
        table_parts.append(f"<td>{type_label}</td>")
        table_parts.append(f"<td>{html.escape(str(table))}</td>")
        table_parts.append(f"<td style='word-wrap: break-word; white-space: normal;'>{summary_html}</td>")

         # Determine pill class based on PR value
        if str(pr).upper() == "TBD":
            pill_class = "pr-pill pr-tbd"
        else:
            pill_class = f"pr-pill pr-general"

        table_parts.append(
                f"<td style='text-align: center;'><span class='{pill_class}'>{html.escape(str(pr))}</span></td>"
            )
        table_parts.append("</tr>")
    table_parts.append("</tbody></table>")

    return "\n".join(table_parts)

# WORK
df = load_and_filter_xlsx(XLSX)

# Drop unecessary columns (for troubleshooting purposes)
df = df.drop(['Name'], axis=1)
df = df.drop(['Status'], axis=1)
df = df.drop(['BR'], axis=1)

# Replace empty PR cells with 'TBD'
df['PR'] = df['PR'].replace('', 'TBD') 

# Type mapping and sort by (1) domain, (2) table/topic
df["MappedType"] = df["Type"].apply(map_type)
df = df[df["MappedType"].notna()]
df = df.sort_values(by=['Domain', 'Table/Topic'])

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
    pr = row["PR"]

    # Convert Markdown → HTML & strip outer <p>
    summary_html = markdown.markdown(
        summary_md,
        extensions=["extra", "sane_lists"]
    )
    summary_html = re.sub(r'^<p>(.*)</p>$', r'\1', summary_html, flags=re.DOTALL)

    grouped_by_domain.setdefault(domain, []).append(
        (issue_type, table, summary_html, pr)
    )

# Generate known issues and pending tables 
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
        # Sort within domain
        rows = sorted(rows, key=lambda x: (x[0], x[1]))  # (type, table)
        tables.append(build_table(domain, rows))

    return "\n\n".join(tables)

# Make table and insert into markdown
combined_tables_html_int = build_combined_tables()
insert_into_markdown(HBCD_DOCS_MD, combined_tables_html_int)


# df.to_csv("debug.tsv", sep='\t', index=False)
