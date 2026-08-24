from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


SPREADSHEET_ID = "1l2nbu_iLbhqgF_TMDnNpaQPTSuJ1Ria0-Y5Em8QlEpA"

TABLES = [
    {
        "gid": "0",
        "range": None,
        "output": "docs/resources/tables/example.csv",
    },

    # Additional examples:
    # {
    #     "gid": "123456789",
    #     "range": "A1:F20",
    #     "output": "docs/resources/tables/another_table.csv",
    # },
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