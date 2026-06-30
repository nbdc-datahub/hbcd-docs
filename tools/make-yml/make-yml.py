import pandas as pd
import yaml
import os

os.chdir(os.getcwd())

INPUT = "instruments.csv"
OUTPUT = "../../docs/data/instruments.yml"

# Download google sheet as csv locally
sheet_id = "1_2TJ83VIMJMzW5LAgW-AmbmjiOkuT1-3WAvF-RS5g18"
g_id = "64448846"

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={g_id}"

df = pd.read_csv(url)
df.to_csv("instruments.csv", index=False)

# read all values as strings so that info like total number of items isn't converted from '25' to '25.0'
df = pd.read_csv(INPUT, dtype=str)

# Check that instrument/measure name is present otherwise raise error
required = ["measure"]
missing = [c for c in required if c not in df.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")

# Use all columns except id
fields = [c for c in df.columns if c != "id"]

instruments = {}

for _, row in df.iterrows():
    instrument_id = str(row["id"]).strip()

    instruments[instrument_id] = {}

    for field in fields:
        value = row[field]

        if pd.isna(value) or str(value).strip() == "":
            instruments[instrument_id][field] = None
            continue

        value = str(value).strip()

        # Fields that may contain multi-line values
        if field in ["qc", "full_name"]:
            items = [line.strip() for line in value.splitlines() if line.strip()]

            if len(items) == 1:
                instruments[instrument_id][field] = items[0]
            elif len(items) > 1:
                instruments[instrument_id][field] = items
            else:
                instruments[instrument_id][field] = None
        else:
            instruments[instrument_id][field] = value

with open(OUTPUT, "w") as f:
    yaml.safe_dump(
        instruments,
        f,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    )