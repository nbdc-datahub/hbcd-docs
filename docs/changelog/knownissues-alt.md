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

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vSRBrslwzR7xeb-ixpIAlvmrmTRXtYC560HHOvKPTSjga-AzBXntPqDuaQcVg_wE34OhcO2jwYJ6LM1/pubhtml" width="100%" height="300" frameborder="0"></iframe>


## Monday parsing tests


### Release 2.1

<p style="font-size: 0.9em; color: #555;">
<i class="fas fa-bug issues-icon" title="Known Issue"></i>&nbsp;= Known Issue &nbsp;&nbsp;
<i class="fa-solid fa-clock pending-icon" title="Pending Update"></i>&nbsp;= Pending Update
</p>

<!-- BEGIN KNOWN_ISSUES_TABLE -->

<table class="compact-table-no-vertical-lines">

<thead>
<tr>
<th style="width: 18%;">Table/Topic</th>
<th>Summary</th>
</tr>
</thead>
<tbody>


<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="2"><strong>ALL</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Sequence Field</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>The currently included Sequence field is blank across all instruments and will be removed.</p></td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fa-solid fa-clock pending-icon" title="Pending Update"></i>
</span>
<span class="table-name">Language</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Fields indicating language of administration will be included for all applicable instruments (including, but not limited to: Vineland and BISQ-SF).</p></td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="2"><strong>BIOSAMPLES</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Nails</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Add unit (mg) for <code>nails_results_nail_weight</code> variable.</p></td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Nails &amp; Urine</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Note that the data dictionary level values have quotes around them (for example; 1= "positive" instead of 1=positive), causing the downloaded data dictionary to have double quotes (e.g. 1=""positive"").</p></td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="2"><strong>MRI</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">MRI</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>The sidecar JSONs for Myers-Labonte-parcellated structural measures in the tabulated XCP-D derivatives should have a <code>sub_domain</code> value of <code>Structural MRI</code>, not <code>Resting State fMR</code>: <code>img_xcpd_hash-{X}_space-fsLR_seg-MyersLabonte_stat-mean_desc-_morph</code>. The Data Dictionary available via the NBDC Dictionary Query Tool is correct.</p></td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="2"><strong>NEUROCOG AND LANG</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">MLDS</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Correct Data Dictionary 'description' element to remove erroneous text that appears at end (e.g., "Â Â Â Â ")</p></td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="2"><strong>PEX</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">TLFB</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Weeks for postnatal recruits were mistakenly reported in the TLFB <strong>versions 1</strong> or <strong>2</strong> instead of <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3"><strong>version 3</strong> adapted for PNR</a>. These will be adjusted to <strong>version 3</strong> in the next release.</p></td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">APA 1/2</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>There are cases where APA Level 2 was administered against gating logic (e.g. for Repetitive Behavior despite there being missing Level 1 responses). As Level 2 administration was not expected, these are not scored (score = "No additional inquiry required") despite having Level 2 item responses present. The Level 2 item-level data will be removed in the future to prevent confusion.</p></td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">EPDS</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Note that N=2 participants have an adjusted age of -1 at V02, which is biologically implausible and should be excluded from analyses.</p></td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="2"><strong>SED</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">eHITS</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Participants who did not respond to any questions and should have a blank/null summary score instead have a score of 0. Users should convert these cases to blank/null prior to conducting analyses.</p></td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Demographics</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>The variables <code>sed_bm_demo_residence_{001|002}</code>, present in the prior release, are missing in the current release and will be added back.</p></td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">PACEs</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Summary scores are currently calculated as the sum of individual item responses rather than the average. This will be corrected in a future release. In the meantime, users may compute their own average-based summary scores using the item-level data provided in the dataset.</p></td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="2"><strong>STUDY NAVIGATOR</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Study Navigators</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>The SUBSTANCE_USE and OTHER checkbox fields are blank and will be populated in the next release.</p></td>
</tr>
</tbody>
</table>

<!-- END KNOWN_ISSUES_TABLE -->