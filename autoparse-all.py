from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

'''
This script does 2 things to pull data locally, which iss then automatically autoparsed via macros, requiring no further action:

1. Autoparses google sheets for Static/Dynamic tables
2. Autoparses all instrument info from Airtable

'''

SPREADSHEET_ID = "1l2nbu_iLbhqgF_TMDnNpaQPTSuJ1Ria0-Y5Em8QlEpA"

OUT_DIR="data/tables/demo"

TABLES = [
    {
        "gid": "0",
        "range": None,
        "output": f"{OUT_DIR}/static1-sex-age-other.csv"
    },
    {
        "gid": "361477160",
        "range": None,
        "output": f"{OUT_DIR}/static2-ACS-race-ethnicity.csv",
    },
    {
        "gid": "1954407438",
        "range": None,
        "output": f"{OUT_DIR}/static3-AOU-race-ethnicity.csv",
    },
    {
        "gid": "973349704",
        "range": None,
        "output": f"{OUT_DIR}/dynamic1.csv",
    }
]

def download_table(gid, output, cell_range=None):
    params = {
        "tqx": "out:csv",
        "gid": str(gid),
    }

    if cell_range:
        params["range"] = cell_range

    url = (
        f"https://docs.google.com/spreadsheets/d/"
        f"{SPREADSHEET_ID}/gviz/tq?{urlencode(params)}"
    )

    request = Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
    )

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(
        f"Downloading gid={gid}"
        f"{f', range={cell_range}' if cell_range else ''}"
        f" → {output_path}"
    )

    with urlopen(request, timeout=30) as response:
        csv_data = response.read()

    # Write only after a successful download.
    temporary_path = output_path.with_suffix(".csv.tmp")
    temporary_path.write_bytes(csv_data)
    temporary_path.replace(output_path)


def main():
    for table in TABLES:
        download_table(
            gid=table["gid"],
            cell_range=table.get("range"),
            output=table["output"],
        )


if __name__ == "__main__":
    main()


'''
2 - AUTOPARSE INSTRUMENT INFO FROM AIRTABLE

'''

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

OUTPUT_FILE = Path("data/instruments.yml")

# Set this to an Airtable view name or ID to limit exported records (e.g. AIRTABLE_VIEW = "Website Export")
AIRTABLE_VIEW: Optional[str] = None

# Airtable field used as the key in the generated YAML. TO DO: eventually change this to "slug"
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

# Removes backslashes used to escape Markdown punctuation (e.g. Fig1\_nails.png  -> Fig1_nails.png)
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

def main() -> None:
    records = fetch_airtable_records()
    instruments = build_instruments(records)
    write_yaml(instruments)

if __name__ == "__main__":
    main()