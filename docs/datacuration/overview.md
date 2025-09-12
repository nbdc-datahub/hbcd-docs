
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
<p>Tabulated file names closely mirror their source derivative file names for easy cross-reference. See <a href="../../access/metadata/#exceptions-mri" target="_blank">here</a> for details.</p>
</div>
</p>

HBCD is organized following [Brain Imaging Data Structure](https://bids-specification.readthedocs.io/en/stable/) (BIDS) standards. At a high level, HBCD BIDS data has the folder structure displayed below, with all data nested under `hbcd/`. The main folders of interest are as follows: see linked sections for further details on the contents and folder structure of each.

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<thead>
<tr>
  <td style="width: 20%; text-align: left;"><b>Data Type</b></td>
  <td style="width: 15%; text-align: center;"><b>Folder Location</b></td>
  <td style="width: 65%; text-align: center;"><b>Description</b></td>
</tr>
</thead>
<tbody>
<tr style="background-color: #f9f9f9;">
  <td><i class="fa-solid fa-table" style="margin-right:6px; color:#666;"></i><strong><a href="../phenotypes" target="_blank">Tabulated Data</a></strong></td>
  <td><code style="background:#f5f5f5;">rawdata/phenotype/</code></td>
  <td style="word-wrap: break-word; white-space: normal;">
    Tabulated instrument data, one row per participant. Includes demographics, visit information, toxicology, behavior, and tables derived from file-based data (e.g., MRI, spectroscopy, EEG, and <a href="../../instruments/sensors/wearsensors">wearable sensors</a>).
  </td>
</tr>
<tr>
  <td><i class="fa-solid fa-folder-open" style="margin-right:6px; color:#666;"></i><strong><a href="../rawbids" target="_blank">Raw Data (File-based)</a></strong></td>
  <td><code style="background:#f5f5f5;">rawdata/sub-&lt;ID&gt;/</code></td>
  <td style="word-wrap: break-word; white-space: normal;">
    Raw participant-level files in <a href="https://bids.neuroimaging.io/">BIDS</a> format, organized by subject/session. Includes MRI, MRS, EEG, and motion/accelerometry.
  </td>
</tr>
<tr style="background-color: #f9f9f9;">
  <td><i class="fa-solid fa-folder-open" style="margin-right:6px; color:#666;"></i><strong><a href="../derivatives" target="_blank">Processed Data (File-based)</a></strong></td>
  <td><code style="background:#f5f5f5;">derivatives/</code></td>
  <td style="word-wrap: break-word; white-space: normal;">
    Processed derivatives of MRI, MRS, EEG, and motion/accelerometry data. Organized by subject/session following BIDS <code>derivatives/</code> conventions.
  </td>
</tr>
<tr>
  <td><i class="fa-solid fa-folder-open" style="margin-right:6px; color:#666;"></i><strong><a href="../concat" target="_blank">Concatenated Data</a></strong></td>
  <td><code style="background:#f5f5f5;">concatenated/</code></td>
  <td style="word-wrap: break-word; white-space: normal;">
    Concatenated files combining participant data for certain modalities (currently genetics only). Each file contains data for all participants.
  </td>
</tr>
</tbody>
</table>

<pre class="folder-tree">
hbcd/
|__ concatenated/      <span class="hashtag"># Concatenated Data (Genetics)</span>
|   |__ genetics/
|
|__ derivatives/       <span class="hashtag"># Processed File-Based Data (MRI, EEG, etc.)</span>
|   |__ bibsnet/
|   |__ hbcd_motion/
|   |__ made/
|   |__ mriqc/
|   |__ nibabies/
|   |__ osprey/
|   |__ qmri_postproc/
|   |__ qsiprep/
|   |__ qsirecon/
|   |__ symri/
|   |__ xcp_d/
|
|__ rawdata/ 
    |__ phenotype/     <span class="hashtag"># Tabulated Data (demographics, visit info, behavior, etc.)</span>
    |   |__ par_visit_data.*
    |   |__ sed_basic_demographics.*
    |   |__ <span class="placeholder">&lt;instrument_name&gt;</span>.*
    |
    |__ sub-<span class="label">&lt;label&gt;</span>/   <span class="hashtag"># Raw File-Based Data (MRI, EEG, etc.)</span>
    |   |__ sub-<span class="label">&lt;label&gt;</span>_sessions.tsv
    |   |__ sub-<span class="label">&lt;label&gt;</span>_sessions.json
    |   |__ ses-<span class="label">&lt;label&gt;</span>/
    |       |__ anat/
    |       |__ dwi/
    |       |__ eeg/
    |       |__ fmap/
    |       |__ func/
    |       |__ motion/
    |       |__ mrs/
    |       |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_scans.tsv
    |       |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_scans.json
    |
    |__ dataset_description.json
    |__ participants.tsv
    |__ participants.json 
</pre>
<br>
