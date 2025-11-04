<b style="color: red;">LUCI ADMIN NOTES: potential issues to be added -</b>

1. Basic Demo: University of Florida not properly coded - see [Monday.com](https://ucsd-actri.monday.com/boards/6045591843/pulses/18348405924)
1. Basic Demo: many participants have mismatching site values and labels - see [Monday.com](https://ucsd-actri.monday.com/boards/6045591843/pulses/18348433453)



# Known Issues

The following issues have been identified in the current HBCD data release. **We are actively working to address them and expect most fixes to be implemented in Release 2.1 unless otherwise noted.** This page will be updated as new issues are discovered.    
If you have questions or would like to report an issue, please submit a ticket through the [Lasso Help Center](https://nbdc.lassoinformatics.com/issue-tracker).

## Instruction Metadata — Read Carefully

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th>KNOWN ISSUE - <span style="color: #f97316;">EXPECTED FIX TBD</span></th>
  </tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
  Instruction text in each form’s metadata is automatically extracted from the most recent <code>instruction</code> field in the REDCap Data Dictionary (based on field order). Because this process is automated, it may produce the following issues:
  <ul>
    <li>If an instruction spans multiple fields, only the <b>last portion</b> will be captured.</li>
    <li>Some fields may display text intended for a <b>previous section</b>.</li>
  </ul>
  Manual review and correction of instruction metadata are planned for a future release (<b>expected fix date TBD</b>). For the most accurate and complete information, please refer to the original form.</td>
</tr>
</tbody>
</table>

## <a href="../../instruments/#pex" target="_blank"><i class="fa-solid fa-baby"></i></a> Pregnancy & Exposure, Including Substance Use
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
  <td>TLFB<br><code>pex_ch_tlfb</code></td>
  <td><b>2.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  Participants enrolled postnatally (<i>HBCD Main Child- Postnatal Recruitment</i> or <i>HBCD Multiple Birth- Postnatal Recruitment</i> cohorts) reported TLFB on the wrong weeks. Weeks were either reported in v1 or v2, but should be reported in v3.<br><br>
    <table class="table-no-vertical-lines">
    <tbody>
    <tr><td><b>v1</b></td>
    <td><b>Period 1:</b> Two Weeks Pre-LMP<br><b>Period 2:</b> Four Weeks Post-LMP<br><b>Period 3:</b> Last Week</td></tr>
    <tr><td><b>v2</b></td>
    <td><b>Period 4:</b> Last Two Weeks Before Delivery</td></tr>
    <tr><td><b>v3</b></td>
    <td><b>Period 1:</b> Two Weeks Pre-LMP<br><b>Period 2:</b> Four Weeks Post-LMP<br><b>Period 3:</b> LMP + 19 Weeks to LMP + 20 Weeks<br><b>Period 4:</b> Last Two Weeks Before Delivery</td></tr>
    </tbody>
    </table>
</td>
</tr>
</tbody>
</table>

## <a href="../../instruments/#mri" target="_blank"><i class="fa fa-brain"></i></a> Imaging Data
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
