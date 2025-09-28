
# Data Structure Overview

HBCD is organized following [Brain Imaging Data Structure](https://bids-specification.readthedocs.io/en/stable/) (BIDS) standards. At a high level, HBCD BIDS data has the folder structure displayed below, with all data nested under `hbcd/`. The three main folders of interest are as follows: see linked sections for further details on the contents and folder structure of each.

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
    <tr>
      <th>Type</th>
      <th>Description</th>
      <th>Study Measures</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><i class="fa-solid fa-table"></i> <a href="../phenotypes" target="_blank"><strong>Tabulated Data</strong></a><br><code>rawdata/phenotype/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">Standardized tabular format containing all participant responses per instrument.</td>
      <td>
        • <a href="../../instruments/#demographics-visit-information" target="_blank">Demographics & Visit Information</a><br>
        • <a href="../../instruments/#behavior-biology-environment" target="_blank">Behavior, Biology, & Environment</a><br>
        • Tabulated derivatives <i>(<a href="#warning">details</a></i>)
      </td>
    </tr>
    <tr>
      <td><i class="fa-solid fa-folder-open"></i> <a href="../file-based-data/#raw-bids" target="_blank"><strong>Raw BIDS</strong></a><br><code>rawdata/sub-&lt;ID&gt;/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">Unprocessed imaging, EEG, and biosensor data, minimally converted to BIDS without altering signal content.</td>
      <td><a href="../../instruments/#brain-activity-biosensors">Brain Activity & Biosensors</a></td>
    </tr>
    <tr>
      <td><i class="fa-solid fa-folder-open"></i> <a href="../file-based-data/#processed-derivatives" target="_blank"><strong>Derivatives</strong></a><br><code>derivatives/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">Processed outputs derived from raw BIDS using processing/analysis pipelines.</td>
      <td><a href="../../instruments/#brain-activity-biosensors">Brain Activity & Biosensors</a></td>
    </tr>
  </tbody>
</table>

<p>
<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Which file-based data are also available as HBCD tabulated data? <span class="hint">(Click to expand)</span></span>
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

<br>