# Data Structure Overview

The HBCD dataset follows NBDC data structure standards established as part of the ABCD Study (<a href="https://docs.abcdstudy.org/latest/documentation/curation/structure.html">see details</a>), which incorporates the [Brain Imaging Data Structure (BIDS)](https://bids-specification.readthedocs.io/en/stable/) wherever possible for cross-study consistency. At a high level, data are organized into two categories: **tabulated** and **file-based** data.

<i class="fa-solid fa-table header-icon"></i>  **Tabulated Data**              
Tidy tables with one row per participant session and one column per variable.       
**Includes:** Demographics, behavioral/phenotypic questionnaires (e.g. <a href="../../instruments/#behavior-biology-environment" target="_blank">see details</a>), and select file-based data converted to the tabulated standard to match other instrument data ([see details](#which-file-based-data-are-also-available-as-hbcd-tabulated-data)).   
<i><a href="../phenotypes" target="_blank" class="inline-doc-link">See detailed documentation →</a></i>

<i class="fa-solid fa-folder-open header-icon"></i>  **File-Based Data**          
File-based data is an umbrella term for all other data that isn't tabulated, typically required due to the complex or multidimensional nature of certain data modalities.       
**Includes**: Raw (**raw BIDS**) and processed (**derivative**) imaging, EEG, and wearable sensor recording data (with datasets organized under separate subject folders) and **concatenated data** for measures such as genomics, which include participant-level files aggregated across all subjects    
<i><a href="../file-based-data" target="_blank" class="inline-doc-link">See detailed documentation →</a></i>


## Folder Structure

<div id="filetrees" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">How To Read File Trees <span class="hint">(Click to expand)</span></span>
  <a class="anchor-link" href="#filetrees" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><b>The following conventions are used to improve readability of file tree diagrams throughout this site:</b></p>
<ul>
<li>
<strong>Curly brackets <code>{ }</code></strong> indicate placeholders with many possible values that are not exhaustively listed.
Example: <code>sub-{ID}_ses-{V0X}</code>, <code>run-{X}</code>.</li>
<li><strong>Angle brackets <code>&lt; &gt;</code></strong> indicate a defined set of all included values.
These values are either:
<ul>
<li>Listed directly inside the brackets and separated by <code>|</code>, or</li>
<li>Defined in a <b>Label Values Legend</b> below the file tree.</li>
</ul>
</li>
<li><strong>Sidecar JSON files</strong> may be omitted for brevity. When applicable, files with corresponding JSONs are marked with <code>(+JSON)</code>.
</li>
<li>Some pipelines generate an <code>.html</code> visual summary report for quality assessment. These reports source images from a <code>figures/</code> directory within the derivatives folder. The contents of <code>figures/</code> are not listed for brevity.</li>
</ul>
</div>

<pre class="folder-tree">
hbcd/
├── <span class="folder">rawdata/</span>
│
│   <span class="section"># Tabulated data (demographics, behavior, etc.)</span>
│   ├── <span class="folder">phenotype/</span>
│   │   └── <span class="file">{INSTRUMENT_NAME}.tsv</span>
│
│   <span class="section"># Raw BIDS (MRI/MRS, EEG, biosensors)</span>
│   ├── <span class="folder">sub-{ID}/</span>
│   │   ├── <span class="folder">ses-{V0X}/</span>   <span class="comment"># Modality-specific subfolders</span>
│   │   │   ├── <span class="folder">anat/</span>
│   │   │   ├── <span class="folder">dwi/</span>
│   │   │   ├── <span class="folder">eeg/</span>
│   │   │   ├── <span class="muted">...</span>
│   │   │   └── <span class="file">sub-{ID}_ses-{V0X}_scans.tsv</span>
│   │   └── <span class="file">sub-{ID}_sessions.tsv</span>
│
│   <span class="section"># Dataset-level metadata</span>
│   ├── <span class="file">dataset_description.json</span>
│   └── <span class="file">participants.tsv</span>
│
├── <span class="folder">derivatives/</span>
│   <span class="section"># Processed outputs by pipeline</span>
│   └── <span class="folder">{PIPELINE_NAME}/</span>
│       └── <span class="folder">sub-{ID}/</span>
│           └── <span class="folder">ses-{V0X}/</span>   <span class="comment"># Mirrors rawdata structure</span>
│
└── <span class="folder">concatenated/</span>
    <span class="section"># Aggregated cross-subject datasets</span>
    ├── <span class="folder">genetics/</span>
    ├── <span class="folder">geocoding/</span>
    └── <span class="folder">study_navigator/</span>
</pre>

## Which file-based data are also available as HBCD tabulated data?
<p>Whenever possible, tabulated data tables are derived from file-based data (e.g., MRS, MRI, EEG, wearable sensor data) to provide a single file with rows across participants/sessions. Users may choose either the original file-based data or the combined tabulated version, depending on their needs.</p>
<p><strong>Not all processed data are available in tabulated form.</strong> Tabulated datasets have <em>one row per participant/session</em>, so only derivatives that can be summarized into a single row/column structure are tabulated. If no tabulated file exists for the derivatives you need, you will need to use the file-based data.</p>
<p>Note tabulated files closely mirror their source derivative file names for easy cross-reference. For example, the following subject/session-level <a href="../../instruments/mri/fmri/#xcp-d" target="_blank">XCP-D derivatives</a> are combined into a single tabulated file:</p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<tr>
<td><b>File-based derivatives</b></td>
<td><code>sub-{ID}_ses-{V0X}_task-rest_dir-PA_run-{X}<span style="color: teal;">_space-fsLR_seg_Gordon_stat-alff_bold</span>.tsv</code> </td>
</tr>
<tbody>
<tr>
<td><b>Tabulated file</b></td>
<td><code>img_xcpd<span style="color: teal;">_space-fsLR_seg_Gordon_stat-alff_bold</span>.tsv</code></td>
</tbody>
</table>

<!-- 

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 16px;">
  <tbody>
  <tr>
    <td><a href="../file-based-data/#raw-bids"><strong>Raw BIDS</strong></a></td>
    <td>Raw imaging, EEG, and biosensor data converted to the BIDS standard with unaltered signal content</td>
  </tr>
  <tr>
    <td><a href="../file-based-data/#derivatives"><strong>Derivatives</strong></a></td>
    <td>Processed imaging, EEG, and biosensor datasets generated by standardized pipelines</td>
  </tr>
  <tr>
    <td><a href="../file-based-data/#concatenated-data"><strong>Concatenated Data</strong></a></td>
    <td style="word-wrap: break-word; white-space: normal;">Participant-level files aggregated across all subjects for select measures, e.g. <a href="../../instruments/biospec/illumina-gda-gwas" target="_blank">Illumina GDA GWAS</a></td>
  </tr>
  </tbody>
</table> -->
