# Data Structure Overview

The HBCD dataset follows NBDC data structure standards established as part of the ABCD Study (<a href="https://docs.abcdstudy.org/latest/documentation/curation/structure.html">see details</a>), which incorporates the [Brain Imaging Data Structure (BIDS)](https://bids-specification.readthedocs.io/en/stable/) wherever possible for cross-study consistency. At a high level, data are organized into two categories: **tabulated** and **file-based** data.

<i class="fa-solid fa-table header-icon"></i>  **Tabulated Data**          
Data across all participants organized tidy tables following a standard format with one row per participant session and one column per variable.      
**Includes:** Demographics, behavioral/phenotypic questionnaires, and select [tabulated pipeline derivatives](#tabulated-pipeline-derivatives).  
<i><a href="../phenotypes" class="inline-doc-link">See detailed documentation →</a></i>

<i class="fa-solid fa-folder-open header-icon"></i>  **File-Based Data**          
File-based data is an umbrella term for all other data that isn't tabulated, typically required due to the complex or multidimensional nature of certain data modalities. File-based data are in varied, modality-specific formats.    
**Includes**: Raw (**[raw BIDS](file-based-data.md#raw-bids)**) and processed **[derivatives](file-based-data.md#derivatives)** for  imaging, EEG, and wearable sensor recording data (organized under separate subject session-level folders) and **[concatenated data](file-based-data.md#concatenated-data)** aggregated across participants for certain modalities (e.g., genomnics).       
<i><a href="../file-based-data" class="inline-doc-link">See detailed documentation →</a></i>

## Folder Structure

<div id="filetrees" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">How To Read File Trees</span>
  <a class="anchor-link" href="#filetrees" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><b>The following conventions are used to improve readability of file tree diagrams throughout this site:</b></p>
<ul>
<li>File prefixes <code>sub-[ID]_ses-[V0X]</code> are often replaced with <code>*</code> for brevity</li>
<li><strong>Square brackets <code>[ ]</code></strong> indicate placeholders with many possible values that are not exhaustively listed, e.g., <code>sub-[ID]</code></li>
<li><strong>Curly brackets <code>{ }</code></strong> indicate a defined set of all included values. These values are either listed directly inside the brackets (separated by <code>|</code>) or defined in a <b>Label Values Legend</b> below the file tree.</li>
<li><strong>Sidecar JSON files</strong> are either omitted or indicated by marking corresponding data files with <code>(+JSON)</code> for brevity.
</li>
<li>Some pipelines generate an <code>.html</code> visual summary report for quality assessment. These reports source images from a <code>figures/</code> directory within the derivatives folder. The contents of <code>figures/</code> are not listed for brevity.</li>
</ul>
</div>

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

## Tabulated Pipeline Derivatives

Processing pipelines for imaging, EEG, and wearable sensor recordings output derivative files to separate subject- and session-specific directories. Whenever possible, derivative data is combined across participants to additionally provide a single file in the tabulated data. Users may choose to use either the file-based or tabulated data for their analyses depending on their needs. *See filenaming conventions for tabulated derivatives under naming convention exceptions [here](../standards/naming-conventions.md#exceptions).*

**Not all processed data are available in tabulated form.** Tabulated datasets have one row per participant/session, so only derivatives that can be summarized into a single row/column structure are tabulated. If no tabulated file exists for the derivatives you need, you will need to use the file-based data.
