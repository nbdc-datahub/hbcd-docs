<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>

# NEW VERSION OF PAGE WITH AUTOMATED PARSING FROM MONDAY.COM (includes known issues and pending updates)
# Known Issues & Pending Updates 

The following table outlines **known issues** (<i class="fas fa-bug issue-icon" title="Known Issue"></i>) relevant to the current release data and **pending updates** (<i class="fa-solid fa-clock pending-icon" title="Pending Update"></i>) across study instruments, organized by domain and including estimated release number for which the fix/update will be employed. This page will be updated as new issues are reported and updates are requested.
If you have questions or would like to report an issue, please submit a ticket through the [Help Center in the NBDC Data Access Platform](https://nbdc.lassoinformatics.com/issue-tracker).

<p style="font-size: 1.1em; color: #555;">
<i class="fas fa-bug issue-icon" title="Known Issue"></i>&nbsp;= Known Issue &nbsp;&nbsp;
<i class="fa-solid fa-clock pending-icon" title="Pending Update"></i>&nbsp;= Pending Update
</p>

<!-- BEGIN KNOWN_ISSUES_TABLE -->

<table class="compact-table-no-vertical-lines">

<thead>
<tr style="text-decoration: bold; font-size: 1.1em;">
<th style="width: 18%;">TABLE/TOPIC</th>
<th>SUMMARY</th>
<th style='text-align: center;'>FIX</th>
</tr>
</thead>
<tbody>


<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="3"><strong>ADMINISTRATIVE</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Study Navigators</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>The SUBSTANCE_USE and OTHER checkbox fields are blank and will be populated in the next release.</p></td>
<td style='text-align: center;'>2.1</td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="3"><strong>BEHAVIOR &amp; CAREGIVER-CHILD INTERACTION</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fa-solid fa-clock pending-icon" title="Pending Update"></i>
</span>
<span class="table-name">ECBQ</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Change coding for "Does not apply" to 8 to match the IBQ-R.</p></td>
<td style='text-align: center;'>3</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">MAPS-TL (&lt;1yr)</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>N=4 participants did not respond to any questions and should have a blank/null summary score, but instead have a score of 0. Users should convert these cases to blank/null prior to conducting their statistical analyses.</p></td>
<td style='text-align: center;'>TBD</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">MAPS-TL (Inf &amp; Tod)</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Notes appear in the score field in both versions (Infant/Toddlerhood) and will be moved to a separate field.</p></td>
<td style='text-align: center;'>3</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">MAPS-TL (Tod)</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>A subset of participants (N=16) are missing scores because pro-rated scoring for the Toddlerhood version has not yet been updated for cases with missing or 'Decline to answer' values.</p></td>
<td style='text-align: center;'>3</td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="3"><strong>BIOSPECIMEN &amp; OMICS</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Nails</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Add unit (mg) for <code>nails_results_nail_weight</code> variable.</p></td>
<td style='text-align: center;'>2.1</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Nails</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>The toxicology results variable <code>bio_bm_biosample_nails_results_Nail_type</code> has a value of 4 (Unknown) for all rows and can safely be ignored; nail type is provided in the specimen type table: <code>bio_bm_biosample_nails_typ_collection_nail_type</code>.</p></td>
<td style='text-align: center;'>3</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Nails &amp; Urine</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Note that the data dictionary level values have quotes around them (for example; 1= "positive" instead of 1=positive), causing the downloaded data dictionary to have double quotes (e.g. 1=""positive"").</p></td>
<td style='text-align: center;'>2.1</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fa-solid fa-clock pending-icon" title="Pending Update"></i>
</span>
<span class="table-name">Urine</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Out-of-range values in creatinine results (bio_creat_u) (currently removed from release)</p></td>
<td style='text-align: center;'>3</td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="3"><strong>DEMOGRAPHICS</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fa-solid fa-clock pending-icon" title="Pending Update"></i>
</span>
<span class="table-name">Visit Level Data</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Inaccurate missed_date values (currently excluded from release).</p></td>
<td style='text-align: center;'>3</td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="3"><strong>EEG</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">EEG</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>N=3 V04 sessions in the HBCD-MADE pipeline derivatives for FACE and MMN tasks are missing corresponding tabulated data. File-based data should therefore be used for analyses. Impacted participant IDs are available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a></p></td>
<td style='text-align: center;'>TBD</td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="3"><strong>GENERAL</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Implausible GA</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Several instruments contain implausible values for gestational age (<code>gestational_age</code>). This is currently under internal review and we will add more details as they become available.</p></td>
<td style='text-align: center;'>3</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Instruction Metadata</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Instruction text in each form’s metadata is automatically extracted from the most recent <code>instruction</code> field in the REDCap Data Dictionary (based on field order). Because this process is automated, it may produce the following issues: (1) If an instruction spans multiple fields, only the last portion will be captured and/or (2) Some fields may display text intended for a previous section. Until this is corrected, please refer to original forms for accurate instruction text.</p></td>
<td style='text-align: center;'>TBD</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fa-solid fa-clock pending-icon" title="Pending Update"></i>
</span>
<span class="table-name">Language</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Fields indicating language of administration will be included for all applicable instruments (including, but not limited to: Vineland and BISQ-SF).</p></td>
<td style='text-align: center;'>2.1</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Run ID</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>The <code>run-{X}</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</p></td>
<td style='text-align: center;'>3</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Sequence Field</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>The currently included Sequence field is blank across all instruments and will be removed.</p></td>
<td style='text-align: center;'>2.1</td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="3"><strong>MRI</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">MRI</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>There are 2 corrupted raw BIDS files (V02 bold runs under session-level <code>func/</code> folders of <code>rawdata/</code>) to be resolved. Impacted participant IDs/filepaths are available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</p></td>
<td style='text-align: center;'>TBD</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">MRI</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>The sidecar JSONs for Myers-Labonte-parcellated structural measures in the tabulated XCP-D derivatives should have a <code>sub_domain</code> value of <code>Structural MRI</code>, not <code>Resting State fMR</code>: <code>img_xcpd_hash-{X}_space-fsLR_seg-MyersLabonte_stat-mean_desc-_morph</code>. The Data Dictionary available via the NBDC Dictionary Query Tool is correct.</p></td>
<td style='text-align: center;'>2.1</td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="3"><strong>NEUROCOGNITION &amp; LANGUAGE</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fa-solid fa-clock pending-icon" title="Pending Update"></i>
</span>
<span class="table-name">CDI</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Set percentile scores in <code>ncl_ch_cdiwgen</code> (with the exception of <code>percentile_both</code>) to data type=integer.</p></td>
<td style='text-align: center;'>3</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">MLDS</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Correct Data Dictionary 'description' element to remove erroneous text that appears at end (e.g., "Â Â Â Â ")</p></td>
<td style='text-align: center;'>2.1</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">MLDS</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Total non-parental hours/week (<code>arr_hr_wk</code>) contains implausible values due to data entry errors. The maximum values is 168 hours: please exclude values greater than 168 from analysis.</p></td>
<td style='text-align: center;'>3</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Vineland</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Subset of variables have a typo in the spelling of "receptive."</p></td>
<td style='text-align: center;'>TBD</td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="3"><strong>PHYSICAL HEALTH</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fa-solid fa-clock pending-icon" title="Pending Update"></i>
</span>
<span class="table-name">BISQ-SF</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Addition of Infant Sleep (IS) sub-scale score.</p></td>
<td style='text-align: center;'>3</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Growth</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>The Data Dictionary element <code>type_data</code> for <code>average_bmi</code> will be corrected to <code>double</code> (currently=<code>character</code>).</p></td>
<td style='text-align: center;'>3</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Growth</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p><a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Ranges used to filter out-of-range growth measurements</a> in <code>ph_ch_anthro</code> are not age-specific, leading to values that are within the valid range, but biologically implausible for the visit age. Filtering methods will be re-evaluated for the next release.</p></td>
<td style='text-align: center;'>TBD</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fa-solid fa-clock pending-icon" title="Pending Update"></i>
</span>
<span class="table-name">ecPROMIS- Sleep</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Addition of summary scores</p></td>
<td style='text-align: center;'>3</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fa-solid fa-clock pending-icon" title="Pending Update"></i>
</span>
<span class="table-name">ecPROMIS-PAG</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Addition of summary scores (Summed Score, T-score, and SE). Until added, users can calculate summary scores themselves by following the Scoring Procedures documented on the instrument page.</p></td>
<td style='text-align: center;'>3</td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="3"><strong>PREGNANCY &amp; EXPOSURE</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">APA 1/2</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Note that <code>mania_001</code> through <code>mania_005</code> have incorrect Data Dictionary descriptions.</p></td>
<td style='text-align: center;'>2.1</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">APA 1/2</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>There are cases where APA Level 2 was administered against gating logic (e.g. for Repetitive Behavior despite there being missing Level 1 responses). As Level 2 administration was not expected, these are not scored (score = "No additional inquiry required") despite having Level 2 item responses present. The Level 2 item-level data will be removed in the future to prevent confusion.</p></td>
<td style='text-align: center;'>2.1</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">EPDS</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Note that N=2 participants have an adjusted age of -1 at V02, which is biologically implausible and should be excluded from analyses.</p></td>
<td style='text-align: center;'>2.1</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">EPDS</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Across visits V01-V03, there are a portion of participants with inconsistent data between individual item responses and the calculated sum score, including the following patterns: (1) individual items present, but sum score null; (2) individual items null, but sum score is 0.</p></td>
<td style='text-align: center;'>TBD</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Healthv2 Preg</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Note that the field for the date when PNV was stopped (exp__pnv_007__01) is blank, despite participants having reported stopping.</p></td>
<td style='text-align: center;'>TBD</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Healthv2 Preg</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank. This will be addressed in a future release.</p></td>
<td style='text-align: center;'>TBD</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Preg &amp; Inf Health</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>ICD codes for the  <code>pex_bm_health*</code> instrument tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></p></td>
<td style='text-align: center;'>3</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">TLFB</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Weeks for postnatal recruits were mistakenly reported in the TLFB <strong>versions 1</strong> or <strong>2</strong> instead of <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3"><strong>version 3</strong> adapted for PNR</a>. These will be adjusted to <strong>version 3</strong> in the next release.</p></td>
<td style='text-align: center;'>2.1</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">TLFB</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Select participants (N=8) were recruited postnatally, but not administered the V1 portion of the TLFB. When this was recognized, the participants were administered the TLFB at the next in-person visit, resulting in a longer recall period than specified in the protocol.</p></td>
<td style='text-align: center;'>TBD</td>
</tr>

<tr class="domain-row" style="background-color: #ff8a42cc; color: #695541ff;">
<td colspan="3"><strong>SOCIAL &amp; ENVIRONMENTAL DETERMINANTS</strong></td>
</tr>

<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">Demographics</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>The variables <code>sed_bm_demo_residence_{001|002}</code>, present in the prior release, are missing in the current release and will be added back.</p></td>
<td style='text-align: center;'>2.1</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">PACEs</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Summary scores are currently calculated as the sum of individual item responses rather than the average. This will be corrected in a future release. In the meantime, users may compute their own average-based summary scores using the item-level data provided in the dataset.</p></td>
<td style='text-align: center;'>2.1</td>
</tr>
<tr>

<td class="table-cell">
<span class="icon-wrapper">
    <i class="fas fa-bug issue-icon" title="Issue"></i>
</span>
<span class="table-name">eHITS</span>
</td>

<td style='word-wrap: break-word; white-space: normal;'><p>Participants who did not respond to any questions and should have a blank/null summary score instead have a score of 0. Users should convert these cases to blank/null prior to conducting analyses.</p></td>
<td style='text-align: center;'>2.1</td>
</tr>
</tbody>
</table>

<!-- END KNOWN_ISSUES_TABLE -->