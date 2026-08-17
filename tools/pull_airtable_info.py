import csv
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import quote

import requests
import yaml
from dotenv import load_dotenv
    
load_dotenv()

AIRTABLE_TOKEN = os.environ["AIRTABLE_TOKEN"]
AIRTABLE_BASE_ID = os.environ["AIRTABLE_BASE_ID"]
AIRTABLE_TABLE_ID = os.environ["AIRTABLE_TABLE_ID"]

OUTPUT_FILE = Path("../docs/data/instruments.yml")
CSV_OUTPUT_FILE = Path("../docs/data/instruments.csv")

# Set this to an Airtable view name or ID to limit exported records
# (e.g. AIRTABLE_VIEW = "Website Export")
AIRTABLE_VIEW: Optional[str] = None

# Airtable field used as the key in the generated YAML.
# TO DO: eventually change this to "slug"
KEY_FIELD = "id"

class LiteralString(str):
    """String that should be rendered as a YAML multiline block."""

class LiteralDumper(yaml.SafeDumper):
    """Custom YAML dumper that supports literal multiline strings."""

def represent_literal_string(
    dumper: yaml.SafeDumper,
    value: LiteralString,
) -> yaml.nodes.ScalarNode:
    """Render LiteralString values using YAML's | block style."""

    return dumper.represent_scalar(
        "tag:yaml.org,2002:str",
        value,
        style="|",
    )

LiteralDumper.add_representer(
    LiteralString,
    represent_literal_string,
)

# Removes backslashes used to escape Markdown punctuation (e.g. Fig1\_nails.png  -> Fig1_nails.png - note that this will not remove ALL backslashes)
MARKDOWN_ESCAPE_PATTERN = re.compile(
    r"\\([\\`*_{}\[\]()<>#+.!|>\-~])"
)

# Retrieve all records available from Airtable
def fetch_airtable_records() -> List[Dict[str, Any]]:
    encoded_table = quote(AIRTABLE_TABLE_ID, safe="")

    url = (
        f"https://api.airtable.com/v0/"
        f"{AIRTABLE_BASE_ID}/{encoded_table}"
    )

    headers = {
        "Authorization": f"Bearer {AIRTABLE_TOKEN}",
    }
    
    params: Dict[str, Any] = {"pageSize": 100}

    if AIRTABLE_VIEW:
        params["view"] = AIRTABLE_VIEW

    records: List[Dict[str, Any]] = []

    while True:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=30,
        )
        response.raise_for_status()

        payload = response.json()
        records.extend(payload.get("records", []))

        offset = payload.get("offset")
        if not offset:
            break

        params["offset"] = offset

    return records


def unescape_markdown(value: str) -> str:
    """
    Remove Markdown escape characters including URLs, markdown links/images, regular markdown text (e.g. Fig1\\_nails.png -> Fig1_nails.png)
    """

    # Run repeatedly in case a value contains multiple levels of escaping, such as "\\\\_" instead of "\\_".
    previous_value = None

    while value != previous_value:
        previous_value = value
        value = MARKDOWN_ESCAPE_PATTERN.sub(
            r"\1",
            value,
        )

    return value


def clean_html_attribute_escapes(value: str) -> str:
    """
    Remove unnecessary escape backslashes inside raw HTML tags. Normally the general Markdown cleaup will handle this, but this is an additional pass to catch backslashes before URL-safe punctuation that may appear in src, href, id, class, other HTML attributes
    """

    def clean_tag(match: re.Match) -> str:
        tag = match.group(0)
        # Remove a backslash preceding characters commonly found in URLs, filenames, fragments, and HTML attributes.
        tag = re.sub(
            r"\\([A-Za-z0-9_./:?&=#%+\-])",
            r"\1",
            tag,
        )
        return tag

    return re.sub(
        r"<[^>]+>",
        clean_tag,
        value,
        flags=re.DOTALL,
    )


def clean_string_value(
    value: str,
    field_name: Optional[str] = None,
) -> str:
    """
    Markdown escape sequences removed throughout the value. HTML tags get additional cleanup so escaped filenames and URLs work
    """

    value = unescape_markdown(value)
    value = clean_html_attribute_escapes(value)

    # Replace non-breaking spaces with regular spaces.
    value = value.replace("&nbsp;", " ")
    value = value.replace("\u00A0", " ")

    # table_name values should never contain literal backslashes.
    if field_name == "table_name":
        value = value.replace("\\", "")

    return value

def prepare_value(
    value: Any,
    field_name: Optional[str] = None,
) -> Any:
    """
    Prepare an Airtable value for YAML and CSV output:

    - Remove Markdown escape backslashes throughout string values
    - Clean escaped URLs and filenames inside HTML attributes
    - Remove all remaining backslashes from table_name values
    - Convert blank strings and "NA" to null
    - Render multiline strings with YAML's | block style
    - Process lists and dictionaries recursively
    """

    if isinstance(value, str):
        value = clean_string_value(
            value,
            field_name=field_name,
        )

        # Airtable rich-text fields commonly end with a newline.
        value = value.rstrip()

        if value in {"", "NA"}:
            return None

        if "\n" in value:
            return LiteralString(value)

        return value

    if isinstance(value, list):
        return [
            prepare_value(
                item,
                field_name=field_name,
            )
            for item in value
        ]

    if isinstance(value, dict):
        return {
            key: prepare_value(
                item,
                field_name=key,
            )
            for key, item in value.items()
        }

    return value


def build_instruments(
    records: List[Dict[str, Any]],
) -> Dict[str, Dict[str, Any]]:
    """Convert Airtable records into a dictionary keyed by KEY_FIELD."""

    instruments: Dict[str, Dict[str, Any]] = {}

    for record in records:
        fields = record.get("fields", {})
        key = fields.get(KEY_FIELD)

        if not key:
            print(
                f"Skipping Airtable record {record.get('id')}: "
                f"missing {KEY_FIELD!r}"
            )
            continue

        instrument = {
            field_name: prepare_value(
                value,
                field_name=field_name,
            )
            for field_name, value in fields.items()
            if field_name != KEY_FIELD
        }

        instruments[str(key)] = instrument

    return instruments


def write_yaml(
    instruments: Dict[str, Dict[str, Any]],
) -> None:
    """Write the processed instrument records to the YAML output file."""

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8",
    ) as file:
        yaml.dump(
            instruments,
            file,
            Dumper=LiteralDumper,
            sort_keys=False,
            allow_unicode=True,
            width=1000,
        )

    print(
        f"Wrote {len(instruments)} instruments "
        f"to {OUTPUT_FILE}"
    )


def prepare_csv_value(value: Any) -> Any:
    """
    Convert a processed value into a CSV-compatible value.

    Lists and dictionaries are serialized as JSON strings. Null values are
    written as blank cells.
    """

    if value is None:
        return ""

    if isinstance(value, (list, dict)):
        return json.dumps(
            value,
            ensure_ascii=False,
        )

    return str(value)


def write_csv(
    instruments: Dict[str, Dict[str, Any]],
) -> None:
    """Write the processed instrument records to the CSV output file."""

    CSV_OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Collect every field name while preserving its first-seen order.
    field_names: List[str] = []

    for instrument in instruments.values():
        for field_name in instrument:
            if field_name not in field_names:
                field_names.append(field_name)

    csv_columns = [KEY_FIELD] + field_names

    with CSV_OUTPUT_FILE.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=csv_columns,
        )

        writer.writeheader()

        for key, instrument in instruments.items():
            row = {
                KEY_FIELD: key,
                **{
                    field_name: prepare_csv_value(
                        instrument.get(field_name)
                    )
                    for field_name in field_names
                },
            }

            writer.writerow(row)

    print(
        f"Wrote {len(instruments)} instruments "
        f"to {CSV_OUTPUT_FILE}"
    )


def main() -> None:
    """Fetch Airtable records and write the YAML and CSV files."""

    records = fetch_airtable_records()
    instruments = build_instruments(records)

    write_yaml(instruments)
    write_csv(instruments)


if __name__ == "__main__":
    main()