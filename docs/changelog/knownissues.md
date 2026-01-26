# Known Issues

The following issues have been identified in the current HBCD data release. **We are actively working to address them and expect most fixes to be implemented in Release 2.1 unless otherwise noted.** This page will be updated as new issues are discovered.    
If you have questions or would like to report an issue, please submit a ticket through the [Lasso Help Center](https://nbdc.lassoinformatics.com/issue-tracker).

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
<b>Instruction Metadata</b><br>
Instruction text in each form’s metadata is automatically extracted from the most recent <code>instruction</code> field in the REDCap Data Dictionary (based on field order). Because this process is automated, it may produce the following issues: <b>(1)</b> If an instruction spans multiple fields, only the <b>last portion</b> will be captured and/or <b>(2)</b> Some fields may display text intended for a <b>previous section</b>. Until this is corrected, please refer to original forms for accurate instruction text.</td>
<td>TBD</td> 
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<b> Implausible Values for Gestational Age Across Multiple Instruments</b><br>
Several instruments contain implausible values for gestational age (<code>gestational_age</code>). This is currently under internal review and we will add more details as they become available.</td>
<td>TBD</td> 
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<b>'Sequence' Field</b><br>
This field is included, but blank across all instruments and will be removed.</td>
<td>3.0</td> 
</tr>
</tbody>
</table>

## <a href="../../instruments/#mh" target="_blank"><i class="fa fa-people-arrows"></i></a> Behavior & Caregiver-Child Interaction</span>
<table class="compact-table-no-vertical-lines" style="font-size: 15px;">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr style="border-bottom:2px solid #ccc;">
    <th>DATA</th>
    <th style="width: 1%; text-align: center;">FIX</th>
    <th>KNOWN ISSUE</th>
  </tr>
</thead>
<tbody>
<tr>
  <td>MAPS-TL Infancy<br><code>mh_cg_mapdb__inf</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">N=4 participants did not respond to any questions and should have a blank/null summary score, but instead have a score of 0. Users should convert these cases to blank/null prior to conducting their statistical analyses.</td>
</tr>
<tr>
  <td>MAPS-TL<br><code>mh_cg_mapdb__*</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">Notes appear in the score field and will be moved to a separate field in the next release.</td>
</tr>
<tr>
  <td>MAPS-TL Toddlerhood<br><code>mh_cg_mapdb__tod</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">A subset of participants (N=16) are missing scores because pro-rated scoring for the Toddlerhood version has not yet been updated for cases with missing or 'Decline to answer' values.</td>
</tr>
</tbody>
</table>

## <a href="../../instruments/#biospec" target="_blank"><i class="fa fa-vial"></i></a> Biospecimen & Omics
<table class="compact-table-no-vertical-lines" style="font-size: 15px;">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr style="border-bottom:2px solid #ccc;">
    <th>DATA</th>
    <th style="width: 1%; text-align: center;">FIX</th>
    <th>KNOWN ISSUE</th>
  </tr>
</thead>
<tbody>
<tr>
  <td>Nails</td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">The toxicology results variable <code>bio_bm_biosample_nails_results_Nail_type</code> has a value of 4 (Unknown) for all rows and can safely be ignored; nail type is provided in the specimen type table: <code>bio_bm_biosample_nails_typ_collection_nail_type</code>.</td>
</tr>
<tr>
  <td>Urine</td>
  <td><b>TBD</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">The field <code>bio_bm_biosample_urine_results_bio_c_aha_u</code> includes N=2 participants with spurious values (all other rows are blank or '0') that should not be used and can safely be ignored.</td>
</tr>
</tbody>
</table>

## <a href="../../instruments/#ncl" target="_blank"><i class="fa-solid fa-puzzle-piece"></i></a> Neurocognition & Language
<table class="compact-table-no-vertical-lines" style="font-size: 15px;">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr style="border-bottom:2px solid #ccc;">
    <th>TABLE/DATA</th>
    <th style="width: 1%; text-align: center;">FIX</th>
    <th>KNOWN ISSUE</th>
  </tr>
</thead>
<tbody>
<tr>
  <td>MLDS<br><code>ncl_ch_mlds</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  The variable "total hours per week of non parental hours" (<code>ncl_ch_mlds_arr_hr_wk</code>) contains implausible values due to data entry errors. The max plausible value for this variable is 168 hours; any observations greater than 168 are erroneous- please do not include these observations in your analysis.
  </td>
</tr>
</tbody>
</table>

## <a href="../../instruments/#ph" target="_blank"><i class="fa fa-heart-pulse"></i></a> Physical Health
<table class="compact-table-no-vertical-lines" style="font-size: 15px;">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr style="border-bottom:2px solid #ccc;">
    <th>TABLE/DATA</th>
    <th style="width: 1%; text-align: center;">FIX</th>
    <th>KNOWN ISSUE</th>
  </tr>
</thead>
<tbody>
<tr>
  <td>Growth<br><code>ph_ch_anthro</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">Ranges used to filter out-of-range  growth measurements (<a href="../../instruments/physhealth/growth/#warning" target="_blank">see details</a>) are not age-specific, leading to values that are within the valid range, but biologically implausible for the visit age. Filtering methods will be re-evaluated for the next release.</td>
</tr>
</tbody>
</table>


## <a href="../../instruments/#pex" target="_blank"><i class="fa-solid fa-baby"></i></a> Pregnancy & Exposure, Including Substance Use
<table class="compact-table-no-vertical-lines" style="font-size: 15px;">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr style="border-bottom:2px solid #ccc;">
    <th style="width: 20%;">TABLE/DATA</th>
    <th style="width: 1%; text-align: center;">FIX</th>
    <th>KNOWN ISSUE</th>
  </tr>
</thead>
<tbody>
<tr>
  <td>Pregnancy/Infant Health<br><code>pex_bm_health*</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  ICD codes are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <i>Health V1- Medications</i>, while the <i>Health V2- Pregnancy</i> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a>
</td>
</tr>
<tr>
  <td>Healthhx</td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">The field <code>pex_bm_health_preg__healthhx_002__01</code> ("Approximately how many weeks into your pregnancy were you when you found out that you were pregnant?") is blank.
</td>
</tr>
<tr>
  <td>TLFB<br><code>pex_ch_tlfb</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  Participants enrolled postnatally (<i>HBCD Main Child- Postnatal Recruitment</i> or <i>HBCD Multiple Birth- Postnatal Recruitment</i> cohorts) reported TLFB on the wrong weeks. Weeks were either reported in TLFB versions 1 or 2, but should be reported in TLFB version 3 (<a href="../../instruments/pregexp/su/tlfb/#v3">see details</a>).</td>
</tr>
<tr>
  <td>EPDS<br><code>pex_bm_epds</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">Across visits V01-V03, there are a portion of participants with inconsistent data between individual item responses and the calculated sum score, including the following patterns: (1) individual items present, but sum score null; (2) individual items null, but sum score is 0.</td>
</tr>
</tbody>
</table>

## <a href="../../instruments/#mri" target="_blank"><i class="fa fa-brain"></i></a> Imaging & EEG Data
<table class="compact-table-no-vertical-lines" style="font-size: 15px;">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr style="border-bottom:2px solid #ccc;">
    <th>TABLE/DATA</th>
    <th style="width: 1%; text-align: center;">FIX</th>
    <th>KNOWN ISSUE</th>
  </tr>
</thead>
<tbody>
<tr>
  <td>EEG</td>
  <td><b>2.1</b></td>
  <td style="word-wrap: break-word; white-space: normal;">Three V04 sessions in the HBCD-MADE pipeline derivatives for FACE and MMN tasks  are missing corresponding tabulated data. File-based data should therefore be used for analyses. Impacted participant IDs are available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>:<br>
  <a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/eeg-missing-tabulated-MADE-outputs-supplemental.csv"><i class="fa-solid fa-download"></i> &nbsp; Download participant list</a></td>
</tr>
<tr>
<td rowspan="2">Imaging</td>
<td><b>2.1</b></td> 
<td style="word-wrap: break-word; white-space: normal;">The sidecar JSONs for Myers-Labonte-parcellated structural measures in the tabulated XCP-D derivatives should have a <code>sub_domain</code> value of <code>Structural MRI</code>, not <code>Resting State fMRI</code>:<br>
<code>img_xcpd_hash-{X}_space-fsLR_seg-MyersLabonte_stat-mean_desc-&lt;curv|sulc|thickness&gt;_morph</code><br>
  The Data Dictionary available via the NBDC Dictionary Query Tool is correct.</td>
</tr>
<tr>
<td><b>3.0</b></td> 
<td style="word-wrap: break-word; white-space: normal;">
For HBCD imaging data with multiple runs, the <code>run-{X}</code> field may not reflect chronological acquisition order.  
This affects both <b>raw BIDS and derivatives</b> as well as <b>derivative files converted to HBCD tabulated data</b> (<a href="../../datacuration/overview" target="_blank">see file type details</a>). Despite this, data remain internally consistent — e.g., run IDs match between raw and processed datasets.</td>
</tr>
</tbody>
</table>