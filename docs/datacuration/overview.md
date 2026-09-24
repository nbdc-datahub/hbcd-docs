# Data Structure

## Folder Structure

The HBCD dataset follows NBDC data structure standards established as part of the ABCD Study (<a href="https://docs.abcdstudy.org/latest/documentation/curation/structure.html">see details</a>), which incorporates the [Brain Imaging Data Structure (BIDS)](https://bids-specification.readthedocs.io/en/stable/) wherever possible for cross-study consistency. Release data are organized as displayed in the file tree below (see [How to read file trees](../help/resources.md#how-to-read-file-trees)). At a high level, data are organized into two categories: **[tabulated](#tabulated-data)** and **[file-based](#file-based-data)** data.

<pre class="folder-tree">
hbcd/
├── rawdata/
│   ├── phenotype/        <span class="section"># Tabulated data (demographics, behavior, etc.)</span>
│   │   └── [INSTRUMENT_NAME].tsv
│   │
│   ├── sub-[ID]/         <span class="section"># Raw BIDS with modality-specific subfolders (MRI/MRS, EEG, biosensors)</span>
│   │   ├── ses-[V0X]/
│   │   │   ├── anat/
│   │   │   ├── dwi/
│   │   │   ├── eeg/
│   │   │   ├── <span class="muted">...</span>
│   │   │   └── sub-[ID]_ses-[V0X]_scans.tsv
│   │   └── sub-[ID]_sessions.tsv  
│   │        
│   ├── dataset_description.json  <span class="section"># Dataset-level metadata</span>
│   └── participants.tsv
│
├── derivatives/        <span class="section"># Processed outputs by pipeline</span>
│   └── {PIPELINE_NAME}/
│       └── sub-[ID]/
│           └── ses-[V0X]/   <span class="comment"># Mirrors rawdata structure</span>
│
└── concatenated/       <span class="section"># Aggregated cross-subject datasets</span>
    ├── genetics/
    ├── geocoding/
    └── study_navigator/
</pre>


## Tabulated Data

Tabulated data are data across all participants organized tidy tables following a standard format with one row per participant session and one column per variable. This includes demographics, behavioral/phenotypic questionnaires, and select [tabulated pipeline derivatives](#tabulated-derivatives). Tables follow the BIDS organizational structure so data from different sources can be linked by participant ID and visit number. Each table is available as:

* **TSV/CSV**: plain text files for easy inspection and broad compatibility
* **Parquet**: compressed files optimized for efficient analysis in Python and R ([see details](https://parquet.apache.org/))
* **Shadow matrix**: a companion file that records why individual values are missing

<p>
<div id="tabulated-derivatives" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
<i class="fa-solid fa-diagram-project"></i>
</span>
<span class="text-with-link">
    <span class="text">Tabulated pipeline derivatives</span>
    <a class="anchor-link" href="#tabulated-derivatives" title="Copy link">
        <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow rotate">▸</span>
</div>
<div class="collapsible-content open">
<p>Processing pipelines for imaging, EEG, and wearable sensor recordings output derivative files to separate subject- and session-specific directories. Whenever possible, derivative data is combined across participants to additionally provide a single file in the tabulated data. Users may choose to use either the file-based or tabulated data for their analyses depending on their needs.</p>
<p><strong>Not all processed data are available in tabulated form.</strong> Tabulated datasets have one row per participant/session, so only derivatives that can be summarized into a single row/column structure are tabulated. If no tabulated file exists for the derivatives you need, you will need to use the file-based data.</p>
</div>
</p>

### TSV vs Parquet files

<p>
<div class="banner">
  <span class="emoji"><i class="fa-brands fa-python"></i></span>
  <span class="text">
  See helper functions for loading Parquet files under <a href="../../help/resources/#load-parquet-files">Resources</a>.
  </span>
</div>
</p>

One of the key difference between these file types is that TSV/CSV file types store metadata in accompanying `.json` files, whereas Parquet stores metadata directly in the file, reducing import errors and improving performance for large datasets. Review the table below to choose the optimal format for your needs:

<table class="table-no-vertical-lines">
  <thead>
    <tr>
      <th>Format</th>
      <th>Best for</th>
      <th>Advantages</th>
      <th>Limitations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>TSV/CSV</strong></td>
      <td>Quick inspection and spreadsheets</td>
      <td>
        <ul>
          <li>Easy to open</li>
          <li>Widely compatible</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Slower for large files</li>
          <li>Metadata stored separately</li>
          <li>No selective column loading</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><strong>Parquet</strong></td>
      <td>Analysis in Python or R</td>
      <td>
        <ul>
          <li>Fast and compact</li>
          <li>Embedded metadata</li>
          <li>Preserves data types</li>
          <li>Supports selective column loading</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Not easily viewed in Excel</li>
          <li>Not currently supported by BIDS</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

<div id="warning" class="banner data-warning" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fas fa-exclamation-triangle"></i>
</span>
<span class="text-with-link">
    <span class="text">WARNING: Incorrect Data Types Inferred for CSV/TSV</span>
    <a class="anchor-link" href="#warning" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content" style="background-color: #fcfaed;">
<p>
  CSV and TSV files do not contain an embedded data schema. Because column
  metadata are provided separately, import tools in Python and R may infer
  some column types incorrectly. For example:
</p>
<ul>
  <li>
    Categorical codes stored as strings, such as <code>"0"</code> and
    <code>"1"</code> for “No” and “Yes,” may be imported as numbers.
  </li>
  <li>
    Numeric columns may be imported as text when missing values are represented
    as <code>n/a</code>, as required for TSV files by the BIDS specification.
  </li>
</ul>
<p>
  <b>It is therefore critical that you specify column types during import</b>, particularly data type (<code>type_data</code>), using the accompanying metadata. See <a href="../../help/resources/#nbdctools">NBDCtools</a> for available functions to automate this process (e.g. <a href="https://software.nbdc-datahub.org/NBDCtools/reference/read_dsv_formatted.html"><code>read_dsv_formatted()</code></a> for R users).
</p>
</div>
<p></p>


### Shadow matrices

<p>
<div class="banner">
  <span class="emoji"><i class="fa-brands fa-python"></i></span>
  <span class="text">
  See helper functions for re-integrating shadow matrix information with the main table under <a href="../../resources/#shadow-matrices">Resources</a>.
  </span>
</div>
</p>

Every TSV and Parquet file in `rawdata/phenotype/` has a corresponding **shadow matrix** in the same format. The shadow matrix has the same structure and column names as its data file but records **why values are missing**. For example, non-response codes such as “Don't Know” and “Decline to Answer” are converted to blank cells in the main data file. Their meaning is preserved in the corresponding shadow matrix. For each cell:

* **Data value present →** shadow matrix cell is blank.
* **Data value missing →** shadow matrix cell contains the reason for missingness.

![](images/shadowmatrix.png)

Separating missingness reasons from the primary data serves several purposes, such as preserving information about non-response without cluttering the main dataset. However, in some analyses, the reason a value is missing may itself be meaningful. For example, researchers may want to examine how often participants report that they do not understand a question. In these cases, missingness information can be joined back to the primary data (see [Resources](../resources/index.md#shadow-matrices)).


## File-Based Data

File-based data is an umbrella term for all other data. Unlike tabulated data, organized in a uniform way across study instruments, file-based data comes in varied, often modality-specific formats required to meet the complex or multidimensional nature of certain data modalities. 

### Raw BIDS & Derivatives 

Raw BIDS & derivatives are provided for imaging, EEG, and biosensor recordings, organized under separate subject, session, and modality-specific subfolders according to the [BIDS](https://bids-specification.readthedocs.io/en/stable/) standard. **Raw BIDS** are raw data (in BIDS standard format) while **derivatives** are processed datasets generated by [standardized pipelines](../standards/pipelines.md).

#### Raw BIDS (`rawdata/`)

*Raw MRI/MRS, EEG, biosensor recordings, and dataset metadata. Click on the links to see detailed folder contents for each modality:*

<pre class="folder-tree">
hbcd/
└── <b>rawdata/</b>
    ├── sub-[ID]/
    │   └── ses-[V0X]/
    │       ├── anat/     <span class="section"><a href="../../instruments/mri/#raw-mr-bids"># Imaging & Spectroscopy</a></span>
    │       ├── dwi/
    │       ├── fmap/
    │       ├── func/
    │       ├── mrs/
    │       ├── eeg/      <span class="section"><a href="../../instruments/eeg/#rawbids"># EEG</a></span>
    │       ├── motion/   <span class="section"><a href="../../instruments/sensors/wearsensors/#rawbids"># Wearable sensors</a></span>
    │       └── sub-[ID]_ses-[V0X]_scans.tsv <span class="section"># Session-level metadata</span>
    │
    ├── dataset_description.json             <span class="section"># Dataset-level metadata</span>
    ├── participants.tsv                     <span class="section"># Participant-level metadata</span>
    └── sub-[ID]_ses-[V0X]_scans.tsv         <span class="section"># Scan-level metadata</span>
</pre>

#### Participant-, session-, and scan-level metadata
<table class="table-no-vertical-lines">
<thead><tr><th>Level</th><th>File</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Participant</td><td><code>participants.tsv</code></td><td>General participant information (e.g., sex).</td></tr>
<tr><td>Session</td><td><code>sub-[ID]_sessions.tsv</code></td><td>Session information, including collection site, age at session, and head size.</td></tr>
<tr><td>Scan</td><td><code>sub-[ID]_ses-[V0X]_scans.tsv</code></td><td>Per-scan information, including <a href="../../instruments/mri/qc/#location-in-release-data">raw data QC metrics</a> and scanner metadata.</td></tr>
</tbody>
</table>

#### Derivatives (`derivatives/`)

*Processed datasets generated by modality-specific [standardized pipelines](../standards/pipelines.md):*

<pre class="folder-tree">
└── <b>derivatives/</b>
    <span class="section"># Structural & Functional MRI</span>
    ├── mriqc/
    ├── bme_x/
    ├── bibsnet/
    ├── nibabies/
    ├── freesurfer/
    ├── mcribs/
    ├── xcp_d/

    <span class="section"># Quantitative MRI</span>
    ├── symri/
    ├── qmri_postproc/

    <span class="section"># Diffusion MRI</span>
    ├── qsiprep/
    ├── qsirecon/
    ├── qsirecon-DIPYDKI/
    ├── qsirecon-DSIStudio/
    ├── qsirecon-TORTOISE_model-MAPMRI/
    └── qsirecon-TORTOISE_model-tensor/

    <span class="section"># Other Modalities</span>
    ├── osprey/       <span class="hashtag"># MRS</span>
    ├── made/         <span class="hashtag"># EEG</span>
    └── hbcd_motion/  <span class="hashtag"># Biosensor Recordings</span>
</pre>
<p></p>


### Concatenated Data

Similar to tabulated data, concatenated data are participant-level datasets aggregated across all participants into a single file or file set. The key difference is that the data are not converted to the HBCD standard tabulated format. This is needed in cases where datasets include cohort-wide data and/or the original community-standard formats are required to support common analysis workflows and maximize compatibility with existing tools. Click the links below to view measure documentation.

<pre class="folder-tree">
hbcd/
└── <b>concatenated/</b>
  <span class="section"><a href="../../instruments/biospec/illumina-gda-gwas"># Illumina Global Diversity GWAS Array</a></span>
    ├── genetics/
    │   └── genotype_microarray/
    │       └── GDA/
    │           ├── batch.info
    │           ├── hbcd.bed
    │           ├── hbcd.bim
    │           └── hbcd.fam
    │
  <span class="section"><a href="../../instruments/SED/geocoded-linkage"># Geocoded Linked External Data</a></span>
    ├── geocoding/
    │   └── HBCD_address_history_geocoded.csv
    │
  <span class="section"><a href="../../instruments/biospec/olink"># Olink Explore 384 Inflammation 1 Panel</a></span>
    ├── proteins/
    │   └── olink/
    │       └── inflammation/
    │           ├── Olink_allplates_long.csv
    │           └── Olink_allplates_wide.csv
    │
  <span class="section"><a href="../../instruments/admin/study-navigators"># Study Navigator Contact Form</a></span>
    └── study_navigator/
        └── study_navigator_export.csv
</pre>







<!-- <div id="sm-values" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Missingness Reasons</span>
  <a class="anchor-link" href="#sm-values" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Common shadow matrix values include:</p>
<ul>
<li><strong>Decline to Answer</strong>- participant declined to answer a question</li>
<li><strong>Don't Know</strong>- participant did not know the answer</li>
<li><strong>Missed Visit</strong>- participant did not attend a visit</li>
<li><strong>Missed Instrument</strong>- participant did not complete assessment</li>
<li><strong>Logic Skipped</strong>- question skipped due to branching logic</li>
<li><strong>Unknown Missing</strong>- reason for missing value unknown and/or instrument was not administered (check against the <i>Administration</i> field included for instruments)</li>
</ul>
<p>
The following domains/instruments have additional unique shadow matrix values used where applicable:</p>
<table class="table-no-vertical-lines">
<thead>
<tr>
<th>Table(s)</th>
<th>Unique Shadow Matrix Values [<i>+Variable Name If Specific</i>]</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>BioSpecimens (<i>All</i>)</strong></td>
<td>
  <ul>
    <li><i>"Please refer to corresponding categorical field for more details"</i></li>
  </ul>
</td>
</tr>
</tbody>
</table>
</div>
<p></p> -->
