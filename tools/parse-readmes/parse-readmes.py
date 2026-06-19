#!/usr/bin/env python3

import re
from pathlib import Path

import pandas as pd
from bs4 import BeautifulSoup


DOCS_DIR = Path("../../docs/instruments")


def clean_text(text):
    if text is None:
        return ""

    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_markdown_file(path):

    content = path.read_text(encoding="utf-8")

    record = {
        "source_file": str(path)
    }

    # ---------------------------
    # Instrument title
    # ---------------------------
    m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if m:
        record["instrument"] = clean_text(m.group(1))

    # ---------------------------
    # Instrument full name
    # ---------------------------
    m = re.search(
        r"<p[^>]*>\s*<i>(.*?)</i>\s*</p>",
        content,
        re.DOTALL | re.IGNORECASE,
    )

    if m:
        record["full_name"] = clean_text(
            BeautifulSoup(m.group(1), "html.parser").get_text()
        )

    # ---------------------------
    # Parse metadata table
    # ---------------------------
    table_match = re.search(
        r"<table.*?</table>",
        content,
        re.DOTALL | re.IGNORECASE,
    )

    if not table_match:
        return record

    soup = BeautifulSoup(table_match.group(0), "html.parser")

    for row in soup.find_all("tr"):

        cells = row.find_all(["td", "th"])

        if len(cells) < 2:
            continue

        key = clean_text(cells[0].get_text(" ", strip=True))
        value_cell = cells[1]

        # ---------------------------
        # Special handling:
        # Administration section
        # ---------------------------
        if key.lower() == "administration":

            html = str(value_cell)

            child = re.search(
                r"Child-specific</b>:\s*([^<]+)",
                html,
                re.IGNORECASE,
            )

            respondent = re.search(
                r"Respondent</b>:\s*([^<]+)",
                html,
                re.IGNORECASE,
            )

            method = re.search(
                r"Method</b>:\s*(.*)",
                html,
                re.IGNORECASE | re.DOTALL,
            )

            if child:
                record["child_specific"] = clean_text(child.group(1))

            if respondent:
                record["respondent"] = clean_text(respondent.group(1))

            if method:
                method_text = BeautifulSoup(
                    method.group(1),
                    "html.parser",
                ).get_text(" ", strip=True)

                record["method"] = clean_text(method_text)

        # ---------------------------
        # Quality Control bullets
        # ---------------------------
        elif key.lower() == "quality control":

            bullets = [
                clean_text(li.get_text(" ", strip=True))
                for li in value_cell.find_all("li")
            ]

            record["quality_control"] = "; ".join(bullets)

        else:
            value = clean_text(
                value_cell.get_text(" ", strip=True)
            )

            col = (
                key.lower()
                .replace(" ", "_")
                .replace("-", "_")
            )

            record[col] = value

    return record


def main():

    records = []

    for md_file in DOCS_DIR.rglob("*.md"):
        records.append(parse_markdown_file(md_file))

    df = pd.DataFrame(records)

    preferred_order = [
        "instrument",
        "full_name",
        "table_name",
        "construct",
        "study_visits",
        "child_specific",
        "respondent",
        "method",
        "quality_control",
        "source_file",
    ]

    cols = (
        [c for c in preferred_order if c in df.columns]
        + [c for c in df.columns if c not in preferred_order]
    )

    df = df[cols]

    df.to_excel("instrument_metadata.xlsx", index=False)
    df.to_csv("instrument_metadata.csv", index=False)

    print(f"Extracted {len(df)} instruments")


if __name__ == "__main__":
    main()