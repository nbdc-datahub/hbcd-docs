# Tools & Resources

## Recommended Tools

***All of the following are free, open-source applications.***

### NBDC Sandbox   
The [NBDC Sandbox](https://nbdc-safe.lassoinformatics.com/pun/sys/dashboard) provides a secure, cloud-based analysis environment designed to support data analysis workflows, particularly for neuroimaging and large-scale tabular datasets, without having to download and manage data locally. See the [NBDC Sandbox Tutorial Series](https://hdcc-sandbox-rtd.readthedocs.io/latest/) to get started.

### NBDCtools
NBDCtools, available in both [R](https://software.nbdc-datahub.org/NBDCtools/) and [Python](https://software.nbdc-datahub.org/nbdctools-py/), is a package for creating custom, analysis-ready datasets by simply specifying the variable or table names you need. NBDCtools automatically retrieves the specified columns from locally downloaded HBCD tabulated data and assembles them into a single in-memory data frame, minimizing storage and memory use. This provides a flexible alternative to building datasets through the NBDC Data Access Platform or DEAP, eliminating the need to manually parse files or resolve formatting issues. In addition to dataset assembly, NBDCtools includes functions for working with shadow matrices as well as applying transformations and filters.   

### Brain Imaging Utilities

- **[ITK-Snap](http://www.itksnap.org/pmwiki/pmwiki.php)**: Recommended for interactive visualization of MRI images. See [Andy's Brain Blog](https://andysbrainbook.readthedocs.io/en/latest/ITK-Snap/ITK-Snap_Overview.html#itk-snap-overview) for primer and tutorials.
- **[FSLeyes](https://fsl.fmrib.ox.ac.uk/fsl/docs/#/utilities/fsleyes)**: Also recommended for interactive visualization of MRI images. Part of the FSL software suite.
- **[Connectome Workbench](https://www.humanconnectome.org/software/connectome-workbench)**: Software package that includes critically useful tools such as **wb_view** for interactive visualization of surface-based and connectivity data (e.g. to create overlays of structural/functional data) and **[wb_command](https://www.humanconnectome.org/software/workbench-command)**, a set of command-line tools for processing and analysis of neuroimaging data.

### NMIND

[NMIND](https://www.nmind.org/about) is a collaborative initiative dedicated to improving transparency, reproducibility, and efficiency in neuroimaging research. NMIND principles, standards, and tools were used to develop the HBCD [Processing & Derivative Data Standards](../standards/processing/standards.md). Explore a growing collection of tools tested and improved through the NMIND process at [Evaluated Tools](https://www.nmind.org/proceedings/).

### ReproSchema

[ReproSchema](https://www.repronim.org/reproschema/) provides a standardized schema and supporting tools for documenting questionnaires and tracking changes across releases. See [Chen et al. (2025), Figure 1](https://www.jmir.org/2025/1/e63343#figure1) for an overview. In brief, ReproSchema functionality includes the following:

- **Questionnaire structure:** Defines standard for questions, response options, skip logic, and associated metadata using three levels:
  **Protocol** (set of instruments) → **Activity** (single instrument) → **Item** (single question).
- **Version tracking:** Supports version-controlled questionnaire definitions in GitHub, allowing researchers to review changes to wording, response options, item order, and skip logic. See <a href="https://github.com/ReproNim/HBCD-ReproSchema"><i class="fa-brands fa-github"></i> HBCD-ReproSchema</a>.
- **Supporting tools:** Provides questionnaire validation, conversion to and from REDCap formats, and browser-based questionnaire administration.


<div id="reproschema-example" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
    <span class="text">Example: Questionnaire Changes Across Releases</span>
    <a class="anchor-link" href="#reproschema-example" title="Copy link"><i class="fa-solid fa-link"></i></a>
  </span>
  <span class="arrow rotate">▸</span>
</div>
<div class="collapsible-content">
<p>Version histories help researchers identify changes that may affect longitudinal analyses. This hypothetical example illustrates changes to a sleep question and its response options.</p>

<table class="table-no-vertical-lines">
<thead><tr><th>Release</th><th>Question</th><th>Response Format</th><th>Analysis Considerations</th></tr></thead>
<tbody>
<tr>
  <td>1.0</td>
  <td>How many hours do you sleep on a typical night?</td>
  <td>Numeric entry (hours)</td>
  <td>Reference version.</td>
</tr>
<tr>
  <td>2.0</td>
  <td>On average, how many hours of sleep do you get per night?</td>
  <td>Predefined hour ranges</td>
  <td>Categories reduce precision. Comparing with release 1.0 may require grouping numeric responses into matching ranges.</td>
</tr>
<tr>
  <td>3.0</td>
  <td>On average, how many hours of sleep do you get in a 24-hour period, including naps?</td>
  <td>Same ranges as release 2.0</td>
  <td>Measures total daily sleep rather than nighttime sleep, limiting direct comparison with earlier releases.</td>
</tr>
</tbody>
</table>
</div>

## Resources & Helper Functions

### How to read file trees

The following conventions are used to improve readability of file tree diagrams throughout this site:
<ul>
<li>File prefixes <code>sub-[ID]_ses-[V0X]</code> are often replaced with <code>*</code> for brevity</li>
<li><strong>Square brackets <code>[ ]</code></strong> indicate placeholders with many possible values that are not exhaustively listed, e.g., <code>sub-[ID]</code></li>
<li><strong>Curly brackets <code>{ }</code></strong> indicate a defined set of all included values. These values are either listed directly inside the brackets (separated by <code>|</code>) or defined in a <b>Label Values Legend</b> below the file tree.</li>
<li><strong>Sidecar JSON files</strong> are either omitted or indicated by marking corresponding data files with <code>(+JSON)</code> for brevity.
</li>
<li>Some pipelines generate an <code>.html</code> visual summary report for quality assessment. These reports source images from a <code>figures/</code> directory within the derivatives folder. The contents of <code>figures/</code> are not listed for brevity.</li>
</ul>

### Loading Parquet files

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

### Shadow matrices

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
