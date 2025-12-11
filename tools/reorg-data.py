import pandas as pd
import os

df = pd.read_csv('twins.csv', header=None, names=["raw"])
lines = df["raw"].tolist()

# Convert every pair into a row
paired = list(zip(lines[0::2], lines[1::2]))

df_flagged = pd.DataFrame(paired, columns=["main", "sibling"])
df_flagged["main"] = "sub-" + df_flagged["main"].astype(str)
df_flagged["sibling"] = "sub-" + df_flagged["sibling"].astype(str)

df_flagged.to_csv(f'twins-new.csv', index=None)

