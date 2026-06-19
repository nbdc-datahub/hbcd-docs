import pandas as pd
import yaml
import os

os.chdir(os.getcwd())

INPUT = "instruments.csv"
OUTPUT = "../docs/data/instruments.yml"

# df = pd.read_csv(INPUT)
# read all values as strings so that info like total number of items isn't converted from '25' to '25.0'
df = pd.read_csv(INPUT, dtype=str)

# df = df[df['battery'] != 'Infant']      

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
        else:
            instruments[instrument_id][field] = str(value).strip()

with open(OUTPUT, "w") as f:
    yaml.safe_dump(
        instruments,
        f,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    )