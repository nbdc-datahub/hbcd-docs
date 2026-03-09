import pandas as pd
import html
import os
import markdown
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))   

TSV= "latest.tsv"
# External and internal paths
HBCD_DOCS_MD = "../docs/changelog/issues-updates.md"
INTERNAL_MD = "../../../hbcd-docs-internal/docs/changelog/knownissues.md"

# FUNCTIONS

def load_and_filter_tsv(tsv_path):
    """
    Load a TSV file, rename columns, filter rows, fill missing values, and strip whitespace.
    """
    # Load TSV as strings and rename columns 
    df = pd.read_csv(tsv_path, sep="\t", dtype=str)
    df = df.rename(columns={
    "RTDs": "Type",
    "RTDs Text (markdown format)": "Text"})

    # Filter
    df = df[df['Autoparsed?'].str.contains('Yes')]
    # df = df[df['RTDs_Status'].str.contains('Done')]

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
        + "\n\n"
        + combined_html
        + "\n\n"
        + END_MARKER
        + content[end_index:]
    )
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Known issues table successfully updated.")

# WORK
# Load TSV & filter
df = load_and_filter_tsv(TSV)

# Separate out Done items 
# df = df[~df['Status'].str.contains('Done')]
# df_done = df[df['Status'].str.contains('Done')]

# Type mapping and sort by (1) domain, (2) table/topic
df["MappedType"] = df["Type"].apply(map_type)
df = df[df["MappedType"].notna()]
df = df.sort_values(by=['Domain', 'Table/Topic'])

# Build grouped structure (separate by type - known issues vs pending updates)
grouped = {
    "Issue": {},
    "Pending Update": {}
}

for _, row in df.iterrows():
    domain = row["Domain"]
    issue_type = row["MappedType"]
    table = row["Table/Topic"]
    summary_md = row["Text"]
    pr = row["PR"]
    br = row["BR"]

    # Convert Markdown → HTML & strip outer <p>
    summary_html = markdown.markdown(
        summary_md,
        extensions=["extra", "sane_lists"]
    )
    summary_html = re.sub(r'^<p>(.*)</p>$', r'\1', summary_html, flags=re.DOTALL)

    grouped[issue_type].setdefault(domain, []).append(
        (table, summary_html, pr, br)
    )

# Generate HTML tables 
def build_table(data_dict, table_title, dest="external"):
    if "Known Issues" in table_title:
        domain_class = "domain-row-issue"
    else:
        domain_class = "domain-row-pending"

    table_parts = []

    table_parts.append(f"\n\n## {table_title}\n")
    table_parts.append('<table class="compact-table-no-vertical-lines">')

    if dest == "external":
        table_parts.append("""
    <thead>
    <tr style="text-decoration: bold; font-size: 1.2em;">
    <th>TABLE/TOPIC</th>
    <th>SUMMARY</th>
    <th style='text-align: center;'><span class="tooltip tooltip-left">PR<span class="tooltiptext">Target Release</span></span></th>
    </tr>
    </thead>
    <tbody>
    """)
    
    else:
        table_parts.append("""
    <thead>
    <tr style="text-decoration: bold; font-size: 1.2em;">
    <th style="width: 18%;">TABLE/TOPIC</th>
    <th>SUMMARY</th>
    <th style='text-align: center;'><span class="tooltip tooltip-left">PR<span class="tooltiptext">Target Public Release</span></span></th>
    <th style='text-align: center;'><span class="tooltip tooltip-left">BR<span class="tooltiptext">Target Beta Release</span></span></th>
    </tr>
    </thead>
    <tbody>
    """)

    for domain in sorted(data_dict.keys()):
        table_parts.append(f"""<tr class="{domain_class}"><td colspan="4"><strong>{html.escape(domain)}</strong></td></tr>""")

        for table, summary_html, pr, br in data_dict[domain]:
            table_parts.append("<tr>")
            table_parts.append(f"<td class='table-cell' style='font-weight: bold;'>{html.escape(str(table))}</td>")
            table_parts.append(f"<td style='word-wrap: break-word; white-space: normal;'>{summary_html}</td>")
            table_parts.append(f"<td style='text-align: center; font-weight: bold;'>{pr}</td>")

            # If internal, include BR column as well
            if dest == "internal":
                table_parts.append(f"<td style='text-align: center; font-weight: bold;'>{br}</td>")
            table_parts.append("</tr>")
    table_parts.append("</tbody></table>")
    return "\n".join(table_parts)

# Generate known issues and pending tables for external and internal pages
table_configs = [
    ("Issue",
     '<i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Known Issues'),
    ("Pending Update",
     '<i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i> Pending Updates'),
]

def build_combined_tables(dest):
    tables = [
        build_table(grouped[key], label, dest=dest)
        for key, label in table_configs
    ]
    return "\n\n".join(tables)

# Public and internal
combined_tables_html = build_combined_tables(dest="external")
combined_tables_html_int = build_combined_tables(dest="internal")

# Insert Into Markdown
insert_into_markdown(HBCD_DOCS_MD, combined_tables_html)
insert_into_markdown(INTERNAL_MD, combined_tables_html_int)

# df.to_csv('temp.tsv', index=None, na_rep='NA', sep='\t')

