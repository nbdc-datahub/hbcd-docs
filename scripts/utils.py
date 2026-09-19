import pandas as pd
from datetime import datetime

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

    # # Generate merge.csv for local record
    # current_datetime = datetime.now().strftime("%Y-%m-%d")
    # df.to_csv(f"data/merge_{current_datetime}.csv", index=False)

    return df

