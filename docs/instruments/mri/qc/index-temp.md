<p style="color: red; font-size: 1.5em;">UNDER CONSTRUCTION</p>

<p style="color: red;">Add overall overview of all QC procedures and where all QC results can be found in the release</p>

# Overview: Quality Control Procedures & Exclusion Criteria


## REVIEW & REVISE THIS FAQ

<div id="faq-qcrec" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text-with-link">
    <span class="text">Which imaging data are recommended for analysis?</span>
    <a class="anchor-link" href="#faq-qcrec" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
    </span>
  <span class="arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<p>The majority of processed derivative data should be safe to use for analysis. File selection procedures for processing generally exclude data that fails raw data QC, though specific procedures vary by pipeline (see <a href="../../instruments/processing/#file-selection-for-processing" target="_blank">see details</a>).</p>
<p>To help researchers make informed decisions, many pipelines generate visual reports to summarize the success and quality of processed outputs. This includes, for example, <a href="../../instruments/mri/mri-proc/#xcp-d" target="_blank">XCP-D</a> (structural and functional MRI) and <a href="../../instruments/mri/dmri/#qsiprep" target="_blank">QSIPrep</a> (diffusion MRI). </p>
<p>For structural and functional processing specifically, manual visual QC is performed on the visual reports using <a href="../../instruments/mri/brainswipes/">BrainSwipes</a>, the results of which are provided as tabulated release data.</li>
</div>



## ORIG FAQ


<div id="faq-qcrec" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text-with-link">
    <span class="text">Which imaging data are recommended for analysis?</span>
    <a class="anchor-link" href="#faq-qcrec" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
    </span>
  <span class="arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<p>All imaging data that pass compliance checks are provided in the release data, including data that failed raw data quality control (QC). To help researchers make informed decisions, QC metrics are provided in various formats:</p>
<b>Raw Imaging Data:</b> 
<ul>
<li>QC metrics for raw data are available in the <code>sub-{ID}_ses-{V0X}_scans.tsv</code> file within each subject session folder under <code>rawdata/</code>.</li>
<li>Additional exclusion criteria include <a href="../../instruments/mri/qc/#data-release-eligibility-criteria">acquisition parameter checks</a> and <a href="../../instruments/processing/#file-selection-for-processing">processing pipeline requirements</a>.</li>
<li>Structural and functional MRI data undergo MRIQC processing to generate image quality metrics. See the <a href="../../instruments/mri/smri/#mriqc">sMRI</a> and <a href="../../instruments/mri/fmri/#mriqc">sMRI</a> MRIQC derivatives</a> for more information. Researchers may use these outputs for further curation if desired.</li>
</ul>
<b>Processed Imaging Data (Derivatives):</b> 
<ul>
<li>.</li>
<li>Processing pipelines, such as <a href="../../instruments/mri/fmri/#xcpd" target="_blank">XCP-D</a> (for structural and functional MRI) and <a href="../../instruments/mri/dmri/#qsiprep" target="_blank">QSIPrep</a> (for diffusion MRI), produce visual reports that can help guide data selection.</li>
<li>Visual QC is performed on these reports using <a href="../../instruments/mri/brainswipes/">BrainSwipes</a>, and the results are available as <a href="../../datacuration/phenotypes">tabulated data</a>.</li>
</ul>
</div>

## Quality Control Procedures

MR data undergoes both **raw** and **processed** data quality control assessments, as summarized below. 

All imaging data that pass compliance checks are provided in the release data, including data that failed raw data quality control (QC). To help researchers make informed decisions, QC metrics are provided in various formats:</p>

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<thead>
<tr>
    <th>QC Type</th>
    <th>Specific Data Performed On</th>
    <th>Location of Output QC Metrics in Data Release</th>
</tr>
</thead>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Raw MR Data QC, including automated and manual</td>
    <td style="word-wrap: break-word; white-space: normal;">Raw DICOMs, after protocol compliance & completeness checks (<a href="../../qc/#compliance">see details</a>) and prior to BIDS conversion</td>
    <td style="word-wrap: break-word; white-space: normal;">Session-level Scans TSV files - <a href="../../qc/#scanstsv">see details</a> - includes both automated and manual QC metrics</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Raw BIDS QC via MRIQC Pipeline</td>
    <td style="word-wrap: break-word; white-space: normal;">MRIQC generates image quality metrics (IQM) for raw anatomical and functional data (only outputs for the scans selected for full structural and functional processing are included in the release)</td>
    <td style="word-wrap: break-word; white-space: normal;">MRIQC Pipeline Derivatives - <a href="../../qc/#scanstsv">see details</a>. NOTE that the MRIQC outputs are not used to inform HBCD processing workflows, but are instead simple made available in the release for users convenience.</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Processed Data: Pipeline-Specific Reports</td>
    <td style="word-wrap: break-word; white-space: normal;">Several pipelines generate visual reports and automated metrics for users to assess the quality of processed outputs (ADD MORE INFO)</td>
    <td style="word-wrap: break-word; white-space: normal;">Available in pipeline derivatives (ADD MORE INFO)</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Processed Data: BrainSwipes</td>
    <td style="word-wrap: break-word; white-space: normal;">Structural and functional visual reports derived from XCP-D derivative outputs - <a href="../../brainswipes/">see details</a></td>
    <td style="word-wrap: break-word; white-space: normal;">Available as tabulated derivatives, with most up-to-date results provided between releases in the HBCD Private Release Notes - <a href="../../brainswipes/#location-of-brainswipes-qc-results">see details</a></td>
</tr>
</tbody>
</table>




## Exclusion Criteria

**FOR RAW DATA, includes:**

- acquisition parameter checks

**FOR PROCESSED DATA, includes:**

- processing pipeline requirements/file selection
- removal based on manual visual review guided by BrainSwipes results



### copied text/draft from exclusion criteria page

 Acquisition parameters vary by scanner vendor, so inclusion criteria are typically defined as acceptable <b>ranges</b> rather than fixed values. Following BIDS conversion, modality-specific criteria are extracted from BIDS sidecar JSON files and evaluated accordingly. All images are additionally checked to confirm they were acquired using a head coil. 
 
 **Note that raw BIDS data are NOT excluded from inclusion in release data based on raw MR QC scores, so the raw BIDS data will included data that failed  
 
 data that all available BIDS data 
 
 **Note that ALL raw BIDS imaging data that fall within acceptable acquisition parameter ranges are included in the release and data are NOT excluded based on raw data QC results (described [here](qc.md)).**
 
 
 **Aside from acquisition parameter criteria, all raw data regardless of raw data QC scores are included in the release data.**