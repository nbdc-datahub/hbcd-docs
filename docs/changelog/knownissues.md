
# Known Issues

The following issues have been identified in the current HBCD data release. **We are actively working to address them and expect most fixes to be implemented in Release 2.0 unless otherwise noted.** This page will be updated as new issues are discovered.    
If you have questions or would like to report an issue, please submit a ticket through the [Lasso Help Center](https://nbdc.lassoinformatics.com/issue-tracker).

## General

#### Instruction Metadata — Read Carefully

<table class="compact-table-no-vertical-lines" style="font-size: 15px;">
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<span style="color: #695541ff;"><i><b>Expected Fix: TBD</b></i></span><br><br>
  Instruction text in each form’s metadata is automatically extracted from the most recent <code>instruction</code> field in the REDCap Data Dictionary (based on field order). Because this process is automated, it may produce the following issues:
  <ul>
    <li>If an instruction spans multiple fields, only the <b>last portion</b> will be captured.</li>
    <li>Some fields may display text intended for a <b>previous section</b>.</li>
  </ul>
  Manual review and correction of instruction metadata are planned for a future release (<b>expected fix date TBD</b>). For the most accurate and complete information, please refer to the original form.</td>
</tr>
</tbody>
</table>

#### Differences in TSV vs Parquet Data
<table class="compact-table-no-vertical-lines" style="font-size: 15px;">
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<span style="color: #695541ff;"><i><b>Expected Fix: 2.0</b></i></span><br><br>
Currently, TSV and Parquet files are created from source data using separate pipelines, which may cause minor discrepancies in how decimal values are reported. Software and library differences in converting PHP code to Parquet introduces variation in the precision of floating-point values (<code>type_data</code>=<i>doubles</i>) relative to the TSV tables. To address this and align values with the source data, future Parquet files will be generated directly from the TSV tables as a final step. This change will align Parquet values with the source data reported in the tsv tables to ensure consistency between the two formats.
</td>
</tr>
</tbody>
</table>

## HBCD Study Data

### <a href="../../instruments/#demo" target="_blank"><i class="fas fa-id-card"></i></a> Demographics
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th style="width: 20%;">TABLE/DATA</th>
    <th style="width: 1%; text-align: center;">FIX</th>
    <th>KNOWN ISSUE</th>
  </tr>
</thead>
<tbody>
<tr>
  <td rowspan="3">Basic Demographics<br><code>sed_basic_demographics</code></td>
  <td><b>2.0</b></td> 
  <td><b>[1]</b> Mother Race (<code>screen_mother_race</code>) contains invalid response option 2 = <i>Hawaiian</i>.</td>
</tr>
<tr>
    <td><b>2.0</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  <b>[2]</b> Child Multi-Race (<code>child_ethnoracial_acs_by_multi_race</code>) coding is a duplicate of Child Multi-Ethnicity (<code>child_ethnoracial_acs_by_multi_ethnicity</code>) and will be removed.
  </td>
</tr>
<tr>
<td><b>2.0</b></td> 
<td style="word-wrap: break-word; white-space: normal;">
<b>[3]</b> Child Multi-Race/Ethnicity V01 data will be removed. In the meantime, we do not recommend using V01 data for this variable in analyses.
</td>
</tr>
<tr>
<td rowspan="3">Visit Information<br><code>par_visit_data</code></td>
<td><b>2.0</b></td> 
<td style="word-wrap: break-word; white-space: normal;">
  <b>[1]</b> Participants who did <b>not</b> withdraw from the study (<code>participant_withdrawal</code> = “no”) are assigned a sentinel withdrawal date (<code>participant_withdrawal_date</code>) of <code>12/26/1999</code>. These values will be updated to null for clarity and consistency.
</td>
</tr>
<tr>
<td><b>2.0</b></td> 
<td style="word-wrap: break-word; white-space: normal;">
<b>[2]</b> Erroneous inclusion of Biospec substance use flags <a href="../../instruments/demo/visitinfo/#substance-use-flags">derived from USDTL urine toxicology</a> (<code>su_flag_bio_*</code>) for V02 (urine samples not collected at V02) - will be removed to FIX.
</td>
</tr>
<tr>
<td><b>2.0</b></td> 
<td style="word-wrap: break-word; white-space: normal;">
<b>[3]</b> The TLFB substance use flags (<code>su_flag_tlfb_*</code>) for participants who do not have a Visit 2 have incorrect values of 'no:' these will be corrected to 'null.'
</td>
</tr>
</tr>
</tbody>
</table>

### <a href="../../instruments/#biospec" target="_blank"><i class="fa fa-vial"></i></a> Biospecimen & Omics

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th style="width: 20%;">TABLE/DATA</th>
    <th style="width: 1%; text-align: center;">FIX</th>
    <th>KNOWN ISSUE</th>
  </tr>
</thead>
<tbody>
<tr>
<td>Urine toxicology<br><code>bio_bm_biosample_urine</code></td>
  <td><b>2.0</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  Missing values for urinary cotinine (<code>bio_c_cot_u</code>) were erroneously set to <code>0</code> (N = 18) and will be restored in a future release. In the meantime, users can identify affected records by checking <code>bio_c_nicotine_u</code> for values of <code>3</code> (<code>--invalid</code>).
</td>
</tr>
</tbody>
</table>

### <a href="../../instruments/#neurocog" target="_blank"><i class="fa-solid fa-puzzle-piece"></i></a> Neurocognition & Language
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th style="width: 20%;">TABLE/DATA</th>
    <th style="width: 1%; text-align: center;">FIX</th>
    <th>KNOWN ISSUE</th>
  </tr>
</thead>
<tbody>
<tr>
  <td rowspan="2">SPM-2<br><code>ncl_cg_spm2__inf</code></td>
  <td><b>2.0</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  <b>[1]</b> Age fields are not currently included for the SPM-2. Until added, users can refer to corresponding age variables in related datasets for the same time point.
</td>
</tr>
<tr>
  <td><b>2.0</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  <b>[2]</b> Status Scores are missing for all but one subscale. To be provided in the next release.
</td>
</tr>
</tbody>
</table>

### <a href="../../instruments/#pex" target="_blank"><i class="fa-solid fa-baby"></i></a> Pregnancy & Exposure, Including Substance Use
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
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
  ICD codes are inconsistently provided, sometimes missing corresponding names/labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a>
</td>
</tr>
<tr>
  <td>APA 1/2<br><code>pex_bm_apa_anger_*</code></td>
  <td><b>2.0</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  T-scores and total scores are missing in the APA 1/2 for only the Anger subscale.
</td>
</tr>
<tr>
  <td>TLFB<br><code>pex_ch_tlfb</code></td>
  <td><b>2.0</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  Missing age variable fields (<code>gestational_age</code>, <code>adjusted_age</code>, and <code>candidate_age</code>). Until added, users can refer to corresponding age variables in related datasets for the same time point.
</td>
</tr>
</tbody>
</table>

### <a href="../../instruments/#socenvdet" target="_blank"><i class="fas fa-city"></i></a> Social & Environmental Determinants
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th style="width: 20%;">TABLE/DATA</th>
    <th style="width: 1%; text-align: center;">FIX</th>
    <th>KNOWN ISSUE</th>
  </tr>
</thead>
<tbody>
<tr>
  <td>eHITS<br><code>sed_bm_ehits</code></td>
  <td><b>2.0</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  The variable <code>sed_bm_ehits_total_score</code> was erroneously included and can safely be ignored - use <code>sed_bm_ehits_score</code> instead for sum scores.
</td>
</tr>
</tbody>
</table>

### <a href="../../instruments/#mri" target="_blank"><i class="fa fa-brain"></i></a> Imaging Data
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th style="width: 20%;">TABLE/DATA</th>
    <th style="width: 1%; text-align: center;">FIX</th>
    <th>KNOWN ISSUE</th>
  </tr>
</thead>
<tbody>
<tr>
  <td>Imaging Data</td>
  <td><b>TBD</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  For HBCD imaging data with multiple runs, the <code>run-{X}</code> field may not reflect chronological acquisition order.  
This affects both <b>raw BIDS and derivatives</b> as well as <b>derivative files converted to HBCD tabulated data</b> (<a href="../../datacuration/overview" target="_blank">see file type details</a>). Despite this, data remain internally consistent — e.g., run IDs match between raw and processed datasets.
</td>
</tr>
</tbody>
</table>


<br>