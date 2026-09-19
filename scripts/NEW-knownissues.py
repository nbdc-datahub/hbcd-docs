import pandas as pd
import html
import os
import markdown
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

XLSX = "latest.xlsx"
knownissues_md = "../docs/changelog/issues.md"

# Google Sheet
sheet_id = "1P6QFJaZjb-F5roWkzQXkoGFW1E95t9rge6RfNmmKozc"
sheet_gid = "0"

# ----------------------------------------------------------------------
# HTML
# ----------------------------------------------------------------------

type_icons = {
    "known_issue": '<i class="fas fa-bug icon-bug"></i>',
    "pending": '<i class="fa-solid fa-rotate icon-rotate"></i>',
}

def load_and_filter(xlsx_path, sheet_id, sheet_gid):
    """
    Load XLSX file, merge in google sheet issue text, filter to autoparsed
    rows, fill missing values, and strip whitespace.
    """
    df_monday = pd.read_excel(xlsx_path, dtype=str)
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_gid}"
    df_gsheet = pd.read_csv(url, usecols=['ID', 'Text'])
    df = pd.merge(df_monday, df_gsheet, on='ID', how='left')

    # Filter - only include items marked for autoparsing
    df = df[df['Autoparsed?'].str.contains('Yes')]

    # Fill missing values and strip whitespace
    df = df.fillna('')
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    return df


def normalize_text(text):
    """
    Strip HTML tags/entities and collapse whitespace so rendered summaries
    can be compared as plain text regardless of markup differences.
    """
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip().lower()

def build_rows(df):
    """Build HTML table rows grouped by Domain."""

    rows_html = []

    for domain, group in df.groupby("Domain", sort=True):

        # Domain header
        rows_html.append(
            f'<tr class="domain-row" data-domain="{html.escape(str(domain))}">'
            f'<th colspan="3">{html.escape(str(domain))}</th>'
            f'</tr>'
        )

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

            # Searchable text
            search_text = " ".join([
                str(row["Table/Topic"]),
                str(row["Summary"]),
                str(row["Type"]),
                str(row["PR"]),
                str(domain)
            ])

            rows_html.append(
                f'<tr class="issue-row" '
                f'data-domain="{html.escape(str(domain))}" '
                f'data-type="{html.escape(str(row["Type"]))}" '
                f'data-release="{html.escape(str(row["PR"]))}" '
                f'data-search="{html.escape(search_text.lower())}">'
            )

            rows_html.append(
                f'<td>{html.escape(str(row["Table/Topic"]))}</td>'
            )

            rows_html.append(
                f'<td>{icon} {summary_html}</td>'
            )

            rows_html.append(
                f'<td>{html.escape(str(row["PR"]))}</td>'
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
# df["Domain"] = df["Domain"].replace(domain_mapping)

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