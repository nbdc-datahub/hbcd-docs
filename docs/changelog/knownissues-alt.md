<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>

# Known Issues - ALT

The following issues have been identified in the current HBCD data release. **We are actively working to address them and expect most fixes to be implemented in Release 2.1 unless otherwise noted.** This page will be updated as new issues are reported.    
If you have questions or would like to report an issue, please submit a ticket through the [Help Center in the NBDC Data Access Platform](https://nbdc.lassoinformatics.com/issue-tracker).

<p style="font-size: 24px; font-weight: bold;">
  <a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vSRBrslwzR7xeb-ixpIAlvmrmTRXtYC560HHOvKPTSjga-AzBXntPqDuaQcVg_wE34OhcO2jwYJ6LM1/pubhtml"
     target="_blank" rel="noopener">
    <i class="fa-solid fa-arrow-up-right-from-square"></i>
    <i>Click to view in separate tab</i>
  </a>
</p>

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSRBrslwzR7xeb-ixpIAlvmrmTRXtYC560HHOvKPTSjga-AzBXntPqDuaQcVg_wE34OhcO2jwYJ6LM1/pubhtml" width="100%" height="480" frameborder="0"></iframe>


<!-- 

## General
<table class="compact-table-no-vertical-lines" style="font-size: 15px;">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr style="border-bottom:2px solid #ccc;">
<th>KNOWN ISSUE</th>
<th style="width: 1%; text-align: center;">FIX</th>
</tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<b>'Sequence' Field</b><br>
This field is included, but blank across all instruments and will be removed.</td>
<td><b>2.1</b></td> 
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<b>Instruction Metadata</b><br>
Instruction text in each form’s metadata is automatically extracted from the most recent <code>instruction</code> field in the REDCap Data Dictionary (based on field order). Because this process is automated, it may produce the following issues: <b>(1)</b> If an instruction spans multiple fields, only the <b>last portion</b> will be captured and/or <b>(2)</b> Some fields may display text intended for a <b>previous section</b>. Until this is corrected, please refer to original forms for accurate instruction text.</td>
<td><b>3.0+</b></td> 
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<b> Implausible Values for Gestational Age Across Multiple Instruments</b><br>
Several instruments contain implausible values for gestational age (<code>gestational_age</code>). This is currently under internal review and we will add more details as they become available.</td>
<td><b>3.0+</b></td> 
</tr>
</tbody>
</table>

## Behavior, Biology, & Environment
## Brain Activity & Biosensors

### EEG

<table class="compact-table-no-vertical-lines" style="font-size: 15px;">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr style="border-bottom:2px solid #ccc;">
<th>KNOWN ISSUE</th>
<th style="width: 1%; text-align: center;">FIX</th>
</tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<b>Missing Tabulated Derivatives</b><br>
Three V04 sessions in the HBCD-MADE pipeline derivatives for FACE and MMN tasks are missing corresponding tabulated data. File-based data should therefore be used for analyses. Impacted participant IDs are available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>:<br>
  <a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/eeg-missing-tabulated-MADE-outputs-supplemental.csv"><i class="fa-solid fa-download"></i> &nbsp; Download participant list</a></td>
<td><b>3.0+</b></td> 
</tr>
</tbody>
</table>

### Imaging

<table class="compact-table-no-vertical-lines" style="font-size: 15px;">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr style="border-bottom:2px solid #ccc;">
<th>KNOWN ISSUE</th>
<th style="width: 1%; text-align: center;">FIX</th>
</tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<b>Myers-Labonte Metadata</b><br>
The sidecar JSONs for Myers-Labonte-parcellated structural measures in the tabulated XCP-D derivatives should have a <code>sub_domain</code> value of <code>Structural MRI</code>, not <code>Resting State fMRI</code>:<br>
<code>img_xcpd_hash-{X}_space-fsLR_seg-MyersLabonte_stat-mean_desc-&lt;curv|sulc|thickness&gt;_morph</code><br>
  The Data Dictionary available via the NBDC Dictionary Query Tool is correct.</td>
<td><b>2.1</b></td> 
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<b>Run ID Order</b><br>
For HBCD imaging data with multiple runs, the <code>run-{X}</code> field may not reflect chronological acquisition order.  
This affects both <b>raw BIDS and derivatives</b> as well as <b>derivative files converted to HBCD tabulated data</b> (<a href="../../datacuration/overview" target="_blank">see file type details</a>). Despite this, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
<td><b>3.0+</b></td> 
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<b>Corrupted Files</b><br>
There are 2 corrupted raw BIDS files (V02 bold runs under session-level <code>func/</code> folders of <code>rawdata/</code>) to be resolved. Impacted participant IDs/filepaths are available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>:<br>
  <a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/img_rawBIDS-supplemental.csv"><i class="fa-solid fa-download"></i> &nbsp; Download filepaths list</a></td>
<td><b>3.0+</b></td> 
</tr>
</tbody>
</table>
 -->
