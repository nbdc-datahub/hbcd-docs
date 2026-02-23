<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>

# Known Issues & Pending Updates 

The tables below summarize **[Known Issues](#known-issues)** affecting the current data release and **[Pending Updates](#pending-updates)** across study instruments. Entries are organized by domain and include the expected release in which each fix or update will be implemented. This page is updated regularly as new issues are identified and updates are planned.

To ask a question or report an issue, please submit a ticket through the [Help Center in the NBDC Data Access Platform →](https://nbdc.lassoinformatics.com/issue-tracker)

<p><b>Domains Quick Guide <i>(click icons to view full list of associated instruments)</i></b></p>
<table class="study-legend">
<tbody>
<tr>
<td>
<a style="margin-left: 2px;" href="../../instruments/#adm" target="_blank"><i class="fa fa-clipboard-list"></i></a> Administrative<br>
<a style="margin-left: 2px;" href="../../instruments/#demo" target="_blank"><i class="fas fa-id-card"></i></a> Demographics<br><br>
<b>Brain Activity & Biosensors</b><br>
<a style="margin-left: 2px;" href="../../instruments/#eeg" target="_blank"><i class="fa-solid fa-file-waveform"></i></a> EEG<br>
<a style="margin-left: 2px;" href="../../instruments/#mri" target="_blank"><i class="fa fa-brain"></i></a> Imaging<br>
<a style="margin-left: 2px;" href="../../instruments/#sensors" target="_blank"><i class="fa fa-microchip"></i></a> Novel Technologies & Wearable Sensors
</td>
<td>
<b>Behavior, Biology, & Environment</b><br>
<a style="margin-left: 2px;" href="../../instruments/#mh" target="_blank"><i class="fa fa-people-arrows"></i></a> Behavior & Caregiver–Child Interaction<br>
<a style="margin-left: 2px;" href="../../instruments/#biospec" target="_blank"><i class="fa fa-vial"></i></a> Biospecimen & Omics<br>
<a style="margin-left: 2px;" href="../../instruments/#ncl" target="_blank"><i class="fa-solid fa-puzzle-piece"></i></a> Neurocognition & Language<br>
<a style="margin-left: 2px;" href="../../instruments/#ph" target="_blank"><i class="fa fa-heart-pulse"></i></a> Physical Health<br>
<a style="margin-left: 2px;" href="../../instruments/#pex" target="_blank"><i class="fa-solid fa-baby"></i></a> Pregnancy & Exposure, Including Substance Use<br>
<a style="margin-left: 2px;" href="../../instruments/#sed" target="_blank"><i class="fas fa-city"></i></a> Social & Environmental Determinants
</td>
</tr>
</tbody>
</table>

<!-- BEGIN KNOWN_ISSUES_TABLE -->



### <i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Known Issues

<table class="compact-table-no-vertical-lines">

<thead>
<tr style="text-decoration: bold; font-size: 1.2em;">
<th style="width: 18%;">TABLE/TOPIC</th>
<th>SUMMARY</th>
<th style='text-align: center;'><i class="fa-solid fa-calendar-plus"></i></th>
</tr>
</thead>
<tbody>


<tr class="domain-row-issue">
<td colspan="3"><strong>ADMINISTRATIVE</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>Study Navigators</td>
<td style='word-wrap: break-word; white-space: normal;'>The SUBSTANCE_USE and OTHER checkbox fields are blank and will be populated in the next release.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>

<tr class="domain-row-issue">
<td colspan="3"><strong>BEHAVIOR &amp; CAREGIVER-CHILD INTERACTION</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>MAPS-TL (&lt;1yr)</td>
<td style='word-wrap: break-word; white-space: normal;'>N=4 participants did not respond to any questions and should have a blank/null summary score, but instead have a score of 0 in <code>mh_cg_mapdb__inf</code>. Users should convert these cases to blank/null prior to conducting their statistical analyses.</td>
<td style='text-align: center; font-weight: bold;'>TBD</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>MAPS-TL (Inf &amp; Tod)</td>
<td style='word-wrap: break-word; white-space: normal;'>Notes appear in the score field in both versions (Infant/Toddlerhood) and will be moved to a separate field.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>MAPS-TL (Tod)</td>
<td style='word-wrap: break-word; white-space: normal;'>A subset of participants (N=16) in <code>mh_cg_mapdb__tod</code> are missing scores because pro-rated scoring for the Toddlerhood version has not yet been updated for cases with missing or 'Decline to answer' values.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>

<tr class="domain-row-issue">
<td colspan="3"><strong>BIOSPECIMEN &amp; OMICS</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>Nails</td>
<td style='word-wrap: break-word; white-space: normal;'>Add unit (mg) for <code>nails_results_nail_weight</code> variable.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Nails</td>
<td style='word-wrap: break-word; white-space: normal;'>The toxicology results variable <code>bio_bm_biosample_nails_results_Nail_type</code> has a value of 4 (Unknown) for all rows and can safely be ignored; nail type can instead be found in <code>bio_bm_biosample_nails_typ_collection_nail_type</code>.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Nails &amp; Urine</td>
<td style='word-wrap: break-word; white-space: normal;'>Note that the data dictionary level values have quotes around them (for example; 1= "positive" instead of 1=positive), causing the downloaded data dictionary to have double quotes (e.g. 1=""positive"").</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>

<tr class="domain-row-issue">
<td colspan="3"><strong>EEG</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>EEG</td>
<td style='word-wrap: break-word; white-space: normal;'>N=3 V04 sessions in the HBCD-MADE pipeline derivatives for FACE and MMN tasks are missing corresponding tabulated data. File-based data should therefore be used for analyses. Impacted participant IDs are available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center; font-weight: bold;'>TBD</td>
</tr>

<tr class="domain-row-issue">
<td colspan="3"><strong>GENERAL</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>Implausible GA</td>
<td style='word-wrap: break-word; white-space: normal;'>Several instruments contain implausible values for gestational age (<code>gestational_age</code>). This is currently under internal review and we will add more details as they become available.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Instruction Metadata</td>
<td style='word-wrap: break-word; white-space: normal;'>Instruction text in each form’s metadata is automatically extracted from the most recent <code>instruction</code> field in the REDCap Data Dictionary (based on field order). Because this process is automated, it may produce the following issues: (1) If an instruction spans multiple fields, only the last portion will be captured and/or (2) Some fields may display text intended for a previous section. Until this is corrected, please refer to original forms for accurate instruction text.</td>
<td style='text-align: center; font-weight: bold;'>TBD</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Run ID</td>
<td style='word-wrap: break-word; white-space: normal;'>The <code>run-{X}</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Sequence Field</td>
<td style='word-wrap: break-word; white-space: normal;'>The currently included Sequence field is blank across all instruments and will be removed.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>

<tr class="domain-row-issue">
<td colspan="3"><strong>MRI</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>MRI</td>
<td style='word-wrap: break-word; white-space: normal;'>There are 2 corrupted raw BIDS files (V02 bold runs under session-level <code>func/</code> folders of <code>rawdata/</code>) to be resolved. Impacted participant IDs/filepaths are available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center; font-weight: bold;'>TBD</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>MRI</td>
<td style='word-wrap: break-word; white-space: normal;'>The sidecar JSONs for Myers-Labonte-parcellated structural measures in the tabulated XCP-D derivatives should have a <code>sub_domain</code> value of <code>Structural MRI</code>, not <code>Resting State fMR</code>: <code>img_xcpd_hash-{X}_space-fsLR_seg-MyersLabonte_stat-mean_desc-_morph</code>. The Data Dictionary available via the NBDC Dictionary Query Tool is correct.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>

<tr class="domain-row-issue">
<td colspan="3"><strong>NEUROCOGNITION &amp; LANGUAGE</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>MLDS</td>
<td style='word-wrap: break-word; white-space: normal;'>Correct Data Dictionary 'description' element to remove erroneous text that appears at end (e.g., "Â Â Â Â ")</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>MLDS</td>
<td style='word-wrap: break-word; white-space: normal;'>Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) contains implausible values due to data entry errors. The maximum values is 168 hours: please exclude values greater than 168 from analysis.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Vineland</td>
<td style='word-wrap: break-word; white-space: normal;'>Subset of variables have a typo in the spelling of "receptive."</td>
<td style='text-align: center; font-weight: bold;'>TBD</td>
</tr>

<tr class="domain-row-issue">
<td colspan="3"><strong>PHYSICAL HEALTH</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>The Data Dictionary element <code>type_data</code> for <code>average_bmi</code> will be corrected to <code>double</code> (currently=<code>character</code>).</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'><a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Ranges used to filter out-of-range growth measurements</a> in <code>ph_ch_anthro</code> are not age-specific, leading to values that are within the valid range, but biologically implausible for the visit age. Filtering methods will be re-evaluated for the next release.</td>
<td style='text-align: center; font-weight: bold;'>TBD</td>
</tr>

<tr class="domain-row-issue">
<td colspan="3"><strong>PREGNANCY &amp; EXPOSURE</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>APA 1/2</td>
<td style='word-wrap: break-word; white-space: normal;'>Note that <code>pex_bm_apa_mania_001</code> through <code>mania_005</code> have incorrect Data Dictionary descriptions.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>APA 1/2</td>
<td style='word-wrap: break-word; white-space: normal;'>There are cases where APA Level 2 was administered against gating logic (e.g. for Repetitive Behavior despite there being missing Level 1 responses). As Level 2 administration was not expected, these are not scored (score = "No additional inquiry required") despite having Level 2 item responses present. The Level 2 item-level data will be removed in the future to prevent confusion.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>EPDS</td>
<td style='word-wrap: break-word; white-space: normal;'>N=2 participants in <code>pex_bm_epds</code> have a biologically implausible adjusted age of -1 at V02. Until corrected, please exclude from analyses.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>EPDS</td>
<td style='word-wrap: break-word; white-space: normal;'>Across visits V01-V03, there are a portion of participants with inconsistent data between individual item responses and the calculated sum score, including the following patterns: (1) individual items present, but sum score null; (2) individual items null, but sum score is 0.</td>
<td style='text-align: center; font-weight: bold;'>TBD</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Healthv2 Preg</td>
<td style='word-wrap: break-word; white-space: normal;'>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank. This will be addressed in a future release.</td>
<td style='text-align: center; font-weight: bold;'>TBD</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Preg &amp; Inf Health</td>
<td style='word-wrap: break-word; white-space: normal;'>ICD codes for the <code>pex_bm_health*</code> instrument tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>TLFB</td>
<td style='word-wrap: break-word; white-space: normal;'>Weeks for postnatal recruits were mistakenly reported in the TLFB <strong>versions 1</strong> or <strong>2</strong> instead of <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3"><strong>version 3</strong> adapted for PNR</a>. These will be adjusted to <strong>version 3</strong>.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>TLFB</td>
<td style='word-wrap: break-word; white-space: normal;'>Select participants (N=8) were recruited postnatally, but not administered the V1 portion of the TLFB. When this was recognized, the participants were administered the TLFB at the next in-person visit, resulting in a longer recall period than specified in the protocol.</td>
<td style='text-align: center; font-weight: bold;'>TBD</td>
</tr>

<tr class="domain-row-issue">
<td colspan="3"><strong>SOCIAL &amp; ENVIRONMENTAL DETERMINANTS</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>C-PACEs</td>
<td style='word-wrap: break-word; white-space: normal;'>Summary scores for <code>sed_bm_paces</code> are currently calculated as the sum of individual item responses rather than the average. This will be corrected in a future release. In the meantime, users may compute their own average-based summary scores using the item-level data provided in the dataset.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Demographics</td>
<td style='word-wrap: break-word; white-space: normal;'>The variables <code>sed_bm_demo_residence_{001|002}</code>, present in the prior release, are missing in the current release and will be added back.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>eHITS</td>
<td style='word-wrap: break-word; white-space: normal;'>In <code>sed_bm_ehits</code>, participants who did not respond to any questions have a summary score of 0 instead of missing. Until corrected, users should convert these cases to blank/null prior to conducting analyses.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
</tbody>
</table>



### <i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i> Pending Updates

<table class="compact-table-no-vertical-lines">

<thead>
<tr style="text-decoration: bold; font-size: 1.2em;">
<th style="width: 18%;">TABLE/TOPIC</th>
<th>SUMMARY</th>
<th style='text-align: center;'><i class="fa-solid fa-calendar-plus"></i></th>
</tr>
</thead>
<tbody>


<tr class="domain-row-pending">
<td colspan="3"><strong>BEHAVIOR &amp; CAREGIVER-CHILD INTERACTION</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>ECBQ</td>
<td style='word-wrap: break-word; white-space: normal;'>Change coding for "Does not apply" to 8 to match the IBQ-R.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>

<tr class="domain-row-pending">
<td colspan="3"><strong>BIOSPECIMEN &amp; OMICS</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>Urine</td>
<td style='word-wrap: break-word; white-space: normal;'>The creatinine results (<code>bio_bm_biosample_urine_results_bio_creat_u</code>) variable is currently excluded from the release due to out-of-range values and will be added once corrected.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>

<tr class="domain-row-pending">
<td colspan="3"><strong>DEMOGRAPHICS</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>Visit Level Data</td>
<td style='word-wrap: break-word; white-space: normal;'>The <code>visit_missed_date</code> variable (date of missed visits) is currently excluded from the release due to inaccuracies and will be added once corrected.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>

<tr class="domain-row-pending">
<td colspan="3"><strong>GENERAL</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>Language</td>
<td style='word-wrap: break-word; white-space: normal;'>Fields indicating language of administration will be included for all applicable instruments (including, but not limited to: Vineland and BISQ-SF).</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Multibirth Cohorts</td>
<td style='word-wrap: break-word; white-space: normal;'>For Multibirth Sibling cohorts: (1) instrument fields will be populated where mising and (2) the Data Dictionary element <em>familyID</em> will be incorporated to help identify siblings - <a href="https://docs.hbcdstudy.org/latest/instruments/demo/visitinfo/#warning">see details</a>.</td>
<td style='text-align: center; font-weight: bold;'>TBD</td>
</tr>

<tr class="domain-row-pending">
<td colspan="3"><strong>MRI</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>MRI</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of source DICOMs for all imaging modalities.</td>
<td style='text-align: center; font-weight: bold;'>TBD</td>
</tr>

<tr class="domain-row-pending">
<td colspan="3"><strong>NEUROCOGNITION &amp; LANGUAGE</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>CDI</td>
<td style='word-wrap: break-word; white-space: normal;'>Set percentile scores in <code>ncl_ch_cdiwgen</code> (with the exception of <code>percentile_both</code>) to data type=integer.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>

<tr class="domain-row-pending">
<td colspan="3"><strong>PHYSICAL HEALTH</strong></td>
</tr>

<tr>
<td class='table-cell' style='font-weight: bold;'>BISQ-SF</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>ecPROMIS- Sleep</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of summary scores to <code>ph_cg_pms__sleep</code>.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>ecPROMIS-PAG</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of summary scores (Summed Score, T-score, and SE) to <code>ph_cg_pms__pags</code>. Until added, users can calculate summary scores themselves by following the Scoring Procedures documented on the instrument page.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
</tbody>
</table>

<!-- END KNOWN_ISSUES_TABLE -->