
# Data Structure Overview

<p>
<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Which file-based data are also available as tabulated data? <span class="hint">(Click to expand)</span></span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p><strong>When possible</strong>, tabulated data tables are derived from file-based data (e.g., MRS, MRI, EEG, wearable sensor data) to provide a single file with rows across participants/sessions. Users may choose either the original file-based data or the combined tabulated version, depending on their needs.</p>
<p><strong>Not all processed data are available in tabulated form.</strong> Tabulated datasets have <em>one row per participant/session</em>, so only derivatives that can be summarized into a single row/column structure are included. If no tabulated file exists for the derivatives you need, you will need to use the file-based data.</p>
<ul>
<li><strong>Tabulated data</strong>: one row per participant/session with summary fields.</li>
<li><strong>File-based data</strong>: required for complex, multidimensional, or non-row-summarizable outputs.</li>
</ul>
<p>Note tabulated files closely mirror their source derivative file names for easy cross-reference. See <a href="../../access/metadata/#exceptions-mri" target="_blank">here</a> for details.</p>
</div>
</p>

HBCD is organized following [Brain Imaging Data Structure](https://bids-specification.readthedocs.io/en/stable/) (BIDS) standards. At a high level, HBCD BIDS data has the folder structure displayed below, with all data nested under `hbcd/`. The three main folders of interest are as follows: see linked sections for further details on the contents and folder structure of each.

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<thead>
<tr>
  <th style="width: 10%;">&nbsp;</th>
  <th style="width: 10%;">Folder Location</th>
  <th style="width: 70%;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="../phenotypes"><strong>Tabulated Data</strong></a></td>
<td><code>rawdata/phenotype/</code></td>
<td style="word-wrap: break-word; white-space: normal;">Instrument data in tabulated format, containing all participant data per table. Includes demographics and visit information, toxicology, behavior, and tabulated data derived from file-based data (MRI, spectroscopy, EEG, and <a href="../../instruments/sensors/wearsensors">wearable sensors</a>).</td>
</tr>
<tr>
<td><a href="../rawbids"><strong>Raw BIDS (File-Based)</strong></a></td>
<td><code>rawdata/sub-&lt;ID&gt;/</code></td>
<td style="word-wrap: break-word; white-space: normal;">BIDS-formatted raw data of varied formats for MRI, MRS, EEG, and Biosensors. Participant data is included in separate subject/session-level folders.</td>
</tr>
<tr>
<td><a href="../derivatives"><strong>Processed Derivatives (File-Based)</strong></a></td>
<td><code>derivatives/</code></td>
<td style="word-wrap: break-word; white-space: normal;">Processed MRI, MRS, EEG, and Biosensor data of varied formats derived from processing pipelines. Participant data is included in separate subject/session-level folders.</td>
</tr>
</tbody>
</table>

<pre class="folder-tree">
hbcd/
|__ rawdata/ 
|   |__ phenotype/     <span class="hashtag"># Tabulated Data (demographics, visit info, behavior, etc.)</span>
|   |   |__ par_visit_data.*
|   |   |__ sed_basic_demographics.*
|   |   |__ <span class="placeholder">&lt;instrument_name&gt;</span>.*
|   |
|   |__ sub-<span class="label">{ID}</span>/      <span class="hashtag"># Raw BIDS Formatted Data (MRI, MRS, EEG, & Biosensors)</span>
|   |   |__ sub-<span class="label">{ID}</span>_sessions.tsv
|   |   |__ sub-<span class="label">{ID}</span>_sessions.json
|   |   |__ ses-<span class="label">&lt;V0X&gt;</span>/
|   |       |__ anat/
|   |       |__ dwi/
|   |       |__ eeg/
|   |       |__ fmap/
|   |       |__ func/
|   |       |__ motion/
|   |       |__ mrs/
|   |       |__ sub-<span class="label">{ID}</span>_ses-<span class="label">&lt;V0X&gt;</span>_scans.tsv
|   |       |__ sub-<span class="label">{ID}</span>_ses-<span class="label">&lt;V0X&gt;</span>_scans.json
|   |
|   |__ dataset_description.json
|   |__ participants.tsv
|   |__ participants.json 
|
|__ derivatives/        <span class="hashtag"># Processed Pipeline Derivatives (MRI, MRS, EEG, & Biosensors)</span>
    |__ bibsnet/
    |__ hbcd_motion/
    |__ made/
    |__ mriqc/
    |__ nibabies/
    |__ osprey/
    |__ qmri_postproc/
    |__ qsiprep/
    |__ qsirecon/
    |__ symri/
    |__ xcp_d/
</pre>

## Tabulated Data

Tabulated data, located under `rawdata/phenotype/`, refers to **instrument or derived data in tabulated format**. This includes behavior, demographics, toxicology results, and data derived from brain imaging and other <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> data. See full list of tables included in the release under <a href="../../instruments/#instruments-by-domain" target="_blank">Instruments by Domain</a>.

Key features of tabulated data include:

- Data are curated to follow the [BIDS](https://bids-specification.readthedocs.io/en/stable/modality-agnostic-files.html#phenotypic-and-assessment-data) standard linked by participant ID and visit number. See [Table Organization](#table-organization) below for details.
- Tabulated data is available in both plain text (`.tsv`) and Parquet (`.parquet`) formats, with accompanying metadata explaining the contents of each table. See [File Types](#file-types) below for details.

<pre class="folder-tree">
hbcd/
|__ rawdata/ 
    |__ phenotype/ 
        |__ sed_basic_demographics.*        <span class="hashtag"># Basic Demographics</span>
        |__ par_visit_data.*                <span class="hashtag"># Visit Information</span>
        |__ bio_biosample_<span class="placeholder">&lt;nails|urine&gt;</span>.*   <span class="hashtag"># Toxicology</span>
        |__ <span class="placeholder">&lt;instrument_name&gt;</span>.*             <span class="hashtag"># Instrument Data</span>
</pre>

## File-Based Data

### Raw BIDS

The `rawdata/` folder includes raw <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> MR Imaging, MR Spectroscopy, EEG, and [wearable sensor](../instruments/sensors/wearsensors.md) recordings, converted to BIDS and organized under subject and session-specific directories for processing through BIDS App pipelines ([see details](../instruments/processing/index.md)). 

<pre class="folder-tree" style="font-size: 11px;">
hbcd/
|__ rawdata/ 
    |__ sub-<span class="label">{ID}</span>/
    |   |__ sub-<span class="label">{ID}</span>_sessions.tsv
    |   |__ sub-<span class="label">{ID}</span>_sessions.json
    |   |__ ses-<span class="label">{V0X}</span>/
    |       |__ anat/
    |       |__ dwi/
    |       |__ eeg/
    |       |__ fmap/
    |       |__ func/
    |       |__ motion/
    |       |__ mrs/
    |       |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_scans.tsv
    |       |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_scans.json
    |
    |__ dataset_description.json
    |__ participants.tsv
    |__ participants.json 
</pre>

#### Participant-, Session-, & Scan-Level Data
Participant-, session-, and scan-level data are stored in standardized `.tsv` files, accompanied by a `.json` sidecar file that defines the columns and describes the data fields, located in the `rawdata/` directory and its subdirectories:

- **Participant-level**: Stored in `rawdata/participants.tsv`, this file includes basic demographic and participant information (e.g., sex).
- **Session-level**: Stored in `sub-<label>_sessions.tsv` within each subject folder, this file includes session information such as collection site, the participant’s age at each session, and head size.
- **Scan-level**:  Each session folder includes a `sub-<label>_ses-<label>_scans.tsv` file with per-scan information including participant age at scan as well as all raw data QC scores (see [HBCD MR Quality Control Procedures](../instruments/mri/qc.md#location-of-raw-data-qc-results-in-data-release)).

#### Modality-Specific Data
<i>Expand the section below for links to detailed descriptions of each raw BIDS folder and its contents.</i>

<div id="rawbids-links" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-link"></i></span>
  <span class="text-with-link">
<span class="text">Links to Detailed Folder Descriptions</span>
  <a class="anchor-link" href="#rawbids-links" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Raw BIDS Folder</th>
  <th>Relevant Modalities With Link to Documentation</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="2"><code>anat/</code></td>
  <td><a href="../../instruments/mri/smri/#rawbids" target="_blank">Structural MRI</a></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/qmri/#rawbids" target="_blank">Quantitative MRI</a></td>
</tr>
<tr>
  <td><code>func/</code> & <code>fmap/</code></td>
  <td><a href="../../instruments/mri/fmri/#rawbids" target="_blank">Functional MRI</a></td>
</tr>
<tr>
  <td><code>dwi/</code></td>
  <td><a href="../../instruments/mri/dmri/#rawbids" target="_blank">Diffusion MRI</a></td>
</tr>
<tr>
  <td><code>mrs/</code></td>
  <td><a href="../../instruments/mri/mrs/#rawbids" target="_blank">MR Spectroscopy</a></td>
</tr>
<tr>
  <td><code>eeg/</code></td>
  <td><a href="../../instruments/eeg/#rawbids" target="_blank">EEG</a></td>
</tr>
<tr>
  <td><code>motion/</code></td>
  <td><a href="../../instruments/sensors/wearsensors/#rawbids" target="_blank">Wearable Sensors</a></td>
</tr>
</tbody>
</table>
</div>

### Processed Derivatives

The `derivatives/` folder contains derivatives, which are file outputs from <a href="../../instruments/processing/" target="_blank">processing pipelines</a>. 

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    <span class="hashtag"># Structural & Functional MRI</span>             
    |__ mriqc/      
    |__ bibsnet/    
    |__ nibabies/   
    |__ freesurfer/ 
    |__ mcribs/     
    |__ xcp_d/      
    |               
    <span class="hashtag"># Quantitative MRI</span>    
    |__ symri/           
    |__ qmri_postproc/  
    | 
    <span class="hashtag"># Diffusion MRI</span>                                  
    |__ qsiprep/                         
    |__ qsirecon/                        
    |__ qsirecon-DIPYDKI/                
    |__ qsirecon-DSIStudio/               
    |__ qsirecon-NODDI/                  
    |__ qsirecon-TORTOISE_model-MAPMRI/  
    |__ qsirecon-TORTOISE_model-tensor/  
    |
    |__ osprey/       <span class="hashtag"># MRS</span>
    |__ made/         <span class="hashtag"># EEG</span>
    |__ hbcd_motion/  <span class="hashtag"># Biosensors Recordings</span>
</pre>

### Guide To File Tree Visuals

**The following formatting was employed to enhance readability of the file structure visuals:**

*   Some entities include a set of specific values, each of which is associated with a separate file: these values are either enclosed within `<>` as a list, separated by `|`, or listed in a **Label Values Legend**
*   For brevity, sidecar JSON files containing metadata for the corresponding data file may not be displayed, in which case files with corresponding JSONs are labeled with `(+JSON)` after the filename
*   Several pipelines produce an `.html` visual summary report intended to be used for quality assessment of processed outputs. These files, typically located at either the pipeline folder or session-level, source their images from a `figures/` folder found in the derivatives. For readability, the contents of the `figures/` folders are not listed

#### Modality-Specific Data
<i>Expand the section below for links to detailed descriptions of each pipeline derivatives folder and its contents.</i>

<div id="rawbids-links" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-link"></i></span>
  <span class="text-with-link">
<span class="text">Links to Detailed Folder Descriptions</span>
  <a class="anchor-link" href="#rawbids-links" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Derivatives Folder</th>
  <th>Name of Pipeline</th>
  <th>Relevant Modalities With Link to Documentation</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="2"><code>mriqc/</code></td>
  <td><a href="../../instruments/mri/smri/#mriqc" target="_blank">Structural MRI</a></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#mriqc" target="_blank">Functional MRI</a></td>
</tr>
</tbody>
</table>

- [EEG](../instruments/eeg/index.md#derivatives)
- [Motion](../instruments/sensors/wearsensors.md#derivatives)
- [MRS](../instruments/mri/mrs.md#derivatives)
- [dMRI](../instruments/mri/dmri.md#derivatives)
- [qMRI](../instruments/mri/qmri.md#derivatives)
</div>


<br>