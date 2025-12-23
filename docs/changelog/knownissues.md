# Known Issues

The following issues have been identified in the current HBCD data release. **We are actively working to address them and expect most fixes to be implemented in Release 2.1 unless otherwise noted.** This page will be updated as new issues are discovered.    
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

#### Implausible Values for Gestational Age Across Multiple Instruments

<table class="compact-table-no-vertical-lines" style="font-size: 15px;">
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<span style="color: #695541ff;"><i><b>Expected Fix: TBD</b></i></span><br><br>
Several instruments contain implausible values for gestational age (<code>gestational_age</code>). This is currently under internal review and we will add more details as they become available.
</td>
</tr>
</tbody>
</table>

## <a href="../../instruments/#biospec" target="_blank"><i class="fa fa-vial"></i></a> Biospecimen & Omics
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
  <td>Urinary Creatinine<br><code>bio_bm_biosample_urine_results</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  Creatinine results (<code>bio_creat_u</code>) and units (<code>bio_creat_u_units</code>) are currently excluded due to presence of values outside of the expected range and will be-incorporated in the next release.
  </td>
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
  <td>Bayley-4 Scales<br><code>ncl_ch_bayley</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">There are 13 Bayley administrations that do not have valid scores for all sub-tests. For these participants, the sub-test scores and/or domain scores display as <code>-9999</code>. We recommend cleaning the data to remove participants with scores of <code>-9999</code>.<br>
  <a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/
nc_ch_bayley-supplemental.csv"><i class="fa-solid fa-download"></i> &nbsp; Download participant list</a> <i>(available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>)</i>
  </td>
</tr>
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
<tr>
  <td>ecPROMIS - Physical Activity<br><code>ph_cg_pms__pags</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">Summary scores (Summed Score, T-score, and SE) are currently excluded as they require first re-coding items to a 1 to 5 point scale, which will be done for the next release. In the interim, users can calculate summary scores themselves by following the <a href="../../instruments/physhealth/ecpromis-pags/#scoring">Scoring Procedures</a> documented on the instrument page.</td>
</tr>
<tr>
  <td>BISQ-SF<br><code>ph_cg_bisq</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">The Infant Sleep (IS) sub-scale score is currently missing and will be included for 2.1.</td>
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
  <td>TLFB<br><code>pex_ch_tlfb</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  Participants enrolled postnatally (<i>HBCD Main Child- Postnatal Recruitment</i> or <i>HBCD Multiple Birth- Postnatal Recruitment</i> cohorts) reported TLFB on the wrong weeks. Weeks were either reported in TLFB versions 1 or 2, but should be reported in TLFB version 3 (<a href="../../instruments/pregexp/su/tlfb/#v3">see details</a>).</td>
</tr>
</tbody>
</table>

#### LUCI NOTE: potential additional items to add
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
  <td>Health V1-Illness<br><code>pex_bm_health_preg__illness</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">All "highest temperature reported" items (e.g. <code>003__12</code>) are blank and will be populated in the next release.</td>
</tr>
<tr>
  <td>Health V2-Pregnancy<br><code>pex_bm_healthv2_preg</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  The following measure variables will be added for 2.1:<br>
   - All "highest temperature reported" items (e.g. <code>003__12</code>, <code>illness_015__12</code>, etc.)<br>
   - <code>exp__pnv_007__01</code><br>
   - <code>exp__pnv_011</code> and <code>exp__pnv_012</code> (reporting aspirin use)
   </td>
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
  <td>Imaging Data</td>
  <td><b>TBD</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  For HBCD imaging data with multiple runs, the <code>run-{X}</code> field may not reflect chronological acquisition order.  
This affects both <b>raw BIDS and derivatives</b> as well as <b>derivative files converted to HBCD tabulated data</b> (<a href="../../datacuration/overview" target="_blank">see file type details</a>). Despite this, data remain internally consistent — e.g., run IDs match between raw and processed datasets.
</td>
</tr>
<tr>
  <td>EEG</td>
  <td><b>2.1</b></td>
  <td style="word-wrap: break-word; white-space: normal;">Three V04 sessions in the HBCD-MADE pipeline derivatives for FACE and MMN tasks  are missing corresponding tabulated data. File-based data should therefore be used for analyses. Impacted participant IDs are available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>:<br>
  <a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/eeg-missing-tabulated-MADE-outputs-supplemental.csv"><i class="fa-solid fa-download"></i> &nbsp; Download participant list</a></td>
</tr>
</tbody>
</table>