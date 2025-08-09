
# Data Structure Overview
HBCD is organized following [Brain Imaging Data Structure](https://bids-specification.readthedocs.io/en/stable/) (BIDS) standards. At a high level, HBCD BIDS data has the folder structure displayed below, with all data nested under `hbcd/`. The three main folders of interest are as follows: see linked sections for further details on the contents and folder structure of each.

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<thead>
<tr>
<td style="width: 10%;">&nbsp;</td>
<td style="width: 10%; text-align: center;"><b>Folder Location</b></td>
<td style="width: 70%; text-align: center;"><b>Description</b></td>
</tr>
</thead>
<tbody>
<tr>
<td><strong><a href="../phenotypes"><b>Tabulated Data</b></a></strong></td>
<td><code>rawdata/phenotype/</code></td>
<td style="word-wrap: break-word; white-space: normal;">Instrument data in tabulated format, containing all participant data per table, including demographics and visit information, toxicology, behavior, and tabulated data derived from file-based data (MRI, spectroscopy, EEG, and <a href="../../instruments/sensors/wearsensors">wearable sensors</a>).</td>
</tr>
<tr>
<td><strong><a href="../rawbids"><b>Raw File-based Data</b></a></strong></td>
<td><code>rawdata/sub-&lt;ID&gt;/</code></td>
<td style="word-wrap: break-word; white-space: normal;">BIDS-formatted raw data of varied formats for MRI, MRS, EEG, and motion/accelerometry. Participant data is included in separate subject/session-level folders.</td>
</tr>
<tr>
<td><strong><a href="../derivatives"><b>Processed File-based Data</b></a></strong></td>
<td><code>derivatives/</code></td>
<td style="word-wrap: break-word; white-space: normal;">Processed MRI, MRS, EEG, and motion/accelerometry derivatives of varied formats derived from processing pipelines. Participant data is included in separate subject/session-level folders</td>
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
|   |__ sub-<span class="label">&lt;label&gt;</span>/   <span class="hashtag"># Raw File-Based Data (MRI, EEG, etc.)</span>
|   |   |__ sub-<span class="label">&lt;label&gt;</span>_sessions.tsv
|   |   |__ sub-<span class="label">&lt;label&gt;</span>_sessions.json
|   |   |__ ses-<span class="label">&lt;label&gt;</span>/
|   |       |__ anat/
|   |       |__ dwi/
|   |       |__ eeg/
|   |       |__ fmap/
|   |       |__ func/
|   |       |__ motion/
|   |       |__ mrs/
|   |       |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_scans.tsv
|   |       |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_scans.json
|   |
|   |__ dataset_description.json
|   |__ participants.tsv
|   |__ participants.json 
|
|__ derivatives/        <span class="hashtag"># Processed File-Based Data (MRI, EEG, etc.)</span>
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


## When To Use Tabulated vs. File-Based Data

Tabulated data derived from file-based data exists in order to make the pipeline outputs more accessible. However, not all processed data is converted to tabulated data. Tabulated data includes all participant data, with one row per participant/session. As such, only the processed derivative files that can be collapsed into a single row/column of data are able to be converted. Therefore, if tabulated data doesn't exist for the derivatives/data you need for your analysis, you will need to use the file-based data instead.

Note that the tabulated data derived from processed file-based pipeline outputs will have a name basically matching the name of the derivative file from which it was sourced. For example, filenames for data from the following subject/session-level <a href="../derivatives/#xcp-d-xcp_d" target="_blank">XCP-D derivatives</a> combined into a single tabulated data file are:
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<tr>
<td><b>File-based derivative</b></td>
<td><code>sub-&lt;label&gt;_ses-&lt;label&gt;_task-rest_dir-PA_run-#<span style="color: teal;">_space-fsLR_seg_Gordon_stat-alff_bold</span>.tsv</code> </td>
</tr>
<tbody>
<tr>
<td><b>Tabulated file</b></td>
<td><code>img_xcpd<span style="color: teal;">_space-fsLR_seg_Gordon_stat-alff_bold</span>.tsv</code></td>
</tbody>
</table>

<br>

