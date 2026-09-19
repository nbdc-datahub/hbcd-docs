import pandas as pd
import html
import os
import markdown
import re
from utils import load_and_filter

os.chdir(os.path.dirname(os.path.abspath(__file__)))

XLSX = "latest.xlsx"
knownissues_md = "../docs/changelog/issues.md"

# Google Sheet
sheet_id = "1P6QFJaZjb-F5roWkzQXkoGFW1E95t9rge6RfNmmKozc"
sheet_gid = "0"

domain_mapping = {
    "Demographics": "Demo",
    "Administrative": "ADM",
    "All Data / General": "All/NA",
    "Behavior & Child-Caregiver Interaction": "MH",
    "Biospecimens & Omics": "BIO",
    "Neurocognition & Language": "NCL",
    "Novel Tech & Wearable Sensors": "NT",
    "Participant Derived": "PAR",
    "Physical Health": "PH",
    "Pregnancy & Environmental Exposure": "PEX",
    "Social & Environmental Determinants": "SED"
}

# ----------------------------------------------------------------------
# HTML
# ----------------------------------------------------------------------

type_icons = {
    "known_issue": '<i class="fas fa-bug icon-bug"></i>',
    "pending": '<i class="fa-solid fa-rotate icon-rotate"></i>',
}


def normalize_text(text):
    """
    Strip HTML tags/entities and collapse whitespace so rendered summaries
    can be compared as plain text regardless of markup differences.
    """
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip().lower()


def build_rows(df):
    """Build HTML <tr> markup, sorted alphabetically by Domain."""

    rows_html = []

    for domain, group in df.groupby("Domain", sort=True):

        for _, row in group.iterrows():

            icon = type_icons.get(row["Type"], "")

            summary_html = markdown.markdown(
                str(row["Summary"]),
                extensions=["extra", "sane_lists"]
            )

            summary_html = re.sub(
                r"^<p>(.*)</p>$",
                r"\1",
                summary_html,
                flags=re.DOTALL
            )

            rows_html.append("<tr>")
            rows_html.append(
                f"<td>{html.escape(str(row['Domain']))}</td>"
            )
            rows_html.append(
                f"<td>{html.escape(str(row['Table/Topic']))}</td>"
            )
            rows_html.append(
                f"<td>{icon} {summary_html}</td>"
            )
            rows_html.append(
                f"<td>{html.escape(str(row['PR']))}</td>"
            )
            rows_html.append("</tr>")

    return "\n".join(rows_html)


def replace_table_contents(md_path, rows_html):
    """
    Replace all existing rows inside the <tbody> of the HTML table
    embedded in the Markdown page.
    """

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the table body
    tbody_match = re.search(
        r"(<tbody\s*>)(.*?)(</tbody\s*>)",
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    if not tbody_match:
        raise ValueError(
            f"Could not find <tbody>...</tbody> in Markdown file: {md_path}"
        )

    # Preserve the existing <tbody> and </tbody> tags,
    # but replace everything between them.
    new_content = (
        content[:tbody_match.start(2)]
        + "\n"
        + rows_html
        + "\n"
        + content[tbody_match.end(2):]
    )

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Replaced table contents in {md_path}")

# ----------------------------------------------------------------------
# WORK
# ----------------------------------------------------------------------

df = load_and_filter(XLSX, sheet_id, sheet_gid)
# df = df[df["PR"] != "3"]

# Rename source column
df = df.rename(columns={"Text": "Summary"})

# Map full domain names to short codes
df["Domain"] = df["Domain"].replace(domain_mapping)

# Build HTML table rows
rows_html = build_rows(df)

# Insert rows into the HTML table embedded in the Markdown page
if rows_html:
    replace_table_contents(
        knownissues_md,
        rows_html
    )
else:
    print("No items to add to the archive.")