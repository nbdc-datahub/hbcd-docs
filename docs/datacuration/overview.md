
# Data Structure Overview

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
<td><a href="../phenotypes" target="_blank"><strong>Tabulated Data</strong></a></td>
<td><code>rawdata/phenotype/</code></td>
<td style="word-wrap: break-word; white-space: normal;">Instrument data in tabulated format, containing all participant data per table. Includes demographics and visit information, toxicology, behavior, and tabulated data derived from file-based data (MRI, spectroscopy, EEG, and <a href="../../instruments/sensors/wearsensors">wearable sensors</a>).</td>
</tr>
<tr>
<td><a href="../file-based-data/#raw-bids" target="_blank"><strong>Raw BIDS (File-Based)</strong></a></td>
<td><code>rawdata/sub-&lt;ID&gt;/</code></td>
<td style="word-wrap: break-word; white-space: normal;">BIDS-formatted raw data of varied formats for MRI, MRS, EEG, and Biosensors. Participant data is included in separate subject/session-level folders.</td>
</tr>
<tr>
<td><a href="../file-based-data/#processed-derivatives" target="_blank"><strong>Processed Derivatives (File-Based)</strong></a></td>
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

<br>