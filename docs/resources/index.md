# Resources

## How to read file trees

The following conventions are used to improve readability of file tree diagrams throughout this site:
<ul>
<li>File prefixes <code>sub-[ID]_ses-[V0X]</code> are often replaced with <code>*</code> for brevity</li>
<li><strong>Square brackets <code>[ ]</code></strong> indicate placeholders with many possible values that are not exhaustively listed, e.g., <code>sub-[ID]</code></li>
<li><strong>Curly brackets <code>{ }</code></strong> indicate a defined set of all included values. These values are either listed directly inside the brackets (separated by <code>|</code>) or defined in a <b>Label Values Legend</b> below the file tree.</li>
<li><strong>Sidecar JSON files</strong> are either omitted or indicated by marking corresponding data files with <code>(+JSON)</code> for brevity.
</li>
<li>Some pipelines generate an <code>.html</code> visual summary report for quality assessment. These reports source images from a <code>figures/</code> directory within the derivatives folder. The contents of <code>figures/</code> are not listed for brevity.</li>
</ul>

## Load Parquet files (Python/R)

<pre>Loading parquet files in Python (<a href="https://docs.pola.rs/">polars</a> or <a href="https://pandas.pydata.org/docs/getting_started/index.html">pandas</a> module):<code>
  # Using `polars` module [RECOMMENDED]:
  import polars as pl
  parquet_df = pl.read_parquet("path/to/file.parquet")

  # Using `pandas` module:
  import pandas as pd
  parquet_df = pd.read_parquet("path/to/file.parquet")
</code></pre>
<pre>Loading Parquet file in R (<a href="https://arrow.apache.org/docs/r/">arrow</a> package):<code>
  # Using `arrow` package:
  library(arrow)
  parquet_df <- read_parquet("path/to/file.parquet")
</code></pre>

## Shadow matrices

*Load CSV/TSV and corresponding shadow matrix and add `_missing_reason` columns for missing values:*

#### Example 1: Python
<pre><code>import pandas as pd
import os

def load_data_with_shadow(data_path, shadow_path):  
    # Detect delimiter from file extension and load data
    def get_delimiter(path):
        ext = os.path.splitext(path)[1].lower()
        return "\t" if ext == ".tsv" else ","
    data = pd.read_csv(data_path, delimiter=get_delimiter(data_path))  
    shadow = pd.read_csv(shadow_path, delimiter=get_delimiter(shadow_path))

    # Annotate data with non-empty missingness reason columns (excluding participant_id, session_id) 
    for col in data.columns[2:]:  
        if col in shadow.columns:
            if not shadow[col].isna().all() and not (shadow[col] == '').all():
                data[f"{col}_missing_reason"] = shadow[col]
    return data

# Example usage:
df = load_data_with_shadow("data.tsv", "shadow_matrix.tsv")
# Example: View reasons for missing data for a given column/variable in the data file 
df[df["&lt;COLUMN NAME&gt;"].isna()][["&lt;COLUMN NAME&gt;_missing_reason"]]
</code></pre>

#### Example 2: NBDCtools Python package
<pre><code>
# install R backend with `NBDCtools` is required to run this code
from NBDCtools import create_dataset
create_dataset(
    dir_data="path/to/data",
    study="hbcd",
    vars=["var1", "var2", "var3"],
    tables=["table1", "table2"],
    bind_shadow=True
)</code>
</pre>

#### Example 3: NBDCtools in R
<pre><code>library(NBDCtools)
create_dataset(
  dir_data = "path/to/data",
  study = "hbcd",
  vars = c("var1", "var2", "var3"),
  tables = c("table1", "table2"),
  bind_shadow = TRUE
)
</code></pre>
