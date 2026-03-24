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



## <i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Known Issues

<table class="compact-table-no-vertical-lines">

    <thead>
    <tr style="text-decoration: bold; font-size: 1.2em;">
    <th>TABLE/TOPIC</th>
    <th>SUMMARY</th>
    <th style='text-align: center;'><span class="tooltip tooltip-left">PR<span class="tooltiptext">Target Release</span></span></th>
    </tr>
    </thead>
    <tbody>
    
<tr class="domain-row-issue"><td colspan="4"><strong>ADMINISTRATIVE</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Study Navigators</td>
<td style='word-wrap: break-word; white-space: normal;'>The SUBSTANCE_USE and OTHER checkbox fields are blank and will be populated in the next release.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr class="domain-row-issue"><td colspan="4"><strong>BEHAVIOR &amp; CAREGIVER-CHILD INTERACTION</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>MAPS-TL</td>
<td style='word-wrap: break-word; white-space: normal;'>Notes appear in the score field in both versions (Infant/Toddlerhood) and will be moved to a separate field.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>MAPS-TL (&lt;1yr)</td>
<td style='word-wrap: break-word; white-space: normal;'>N=4 participants did not respond to any questions and should have a blank/null summary score, but instead have a score of 0 in <code>mh_cg_mapdb__inf</code>. Users should convert these cases to blank/null prior to conducting their statistical analyses.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>MAPS-TL (Tod)</td>
<td style='word-wrap: break-word; white-space: normal;'>A subset of participants (N=16) in <code>mh_cg_mapdb__tod</code> are missing scores because pro-rated scoring for the Toddlerhood version has not yet been updated for cases with missing or 'Decline to answer' values.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr class="domain-row-issue"><td colspan="4"><strong>BIOSPECIMEN &amp; OMICS</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Nails</td>
<td style='word-wrap: break-word; white-space: normal;'>Add unit (mg) for <code>nails_results_nail_weight</code> variable.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Nails</td>
<td style='word-wrap: break-word; white-space: normal;'>The toxicology results variable <code>bio_bm_biosample_nails_results_Nail_type</code> has a value of 4 (Unknown) for all rows and can safely be ignored; nail type can instead be found in <code>bio_bm_biosample_nails_typ_collection_nail_type</code>.</td>
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Nails &amp; Urine</td>
<td style='word-wrap: break-word; white-space: normal;'>Data dictionary level values have quotes around them, causing the downloaded to have double quotes (e.g. 1=""positive"").</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr class="domain-row-issue"><td colspan="4"><strong>DEMOGRAPHICS</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>MAV01</td>
<td style='word-wrap: break-word; white-space: normal;'>N=14 participants have a Maternal Age at V01 of 0 - these values should be excluded from analyses until corrected.</td>
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr class="domain-row-issue"><td colspan="4"><strong>EEG</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>.set files</td>
<td style='word-wrap: break-word; white-space: normal;'>Update EEG .set files to include subject release IDs.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Age fields</td>
<td style='word-wrap: break-word; white-space: normal;'>Chronological and adjusted age are inaccurate, falling outside of the expected 3-9 month range, for N=74 participants at V03 due to site data entry errors. Until resolved, exclude age values outside of. the expected range.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>HBCD-MADE</td>
<td style='word-wrap: break-word; white-space: normal;'>N=3 V04 sessions in the HBCD-MADE derivatives for FACE and MMN tasks are missing corresponding tabulated data. File-based data should therefore be used for analyses. Impacted participant IDs are available via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr class="domain-row-issue"><td colspan="4"><strong>GENERAL</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>DD &#x27;instruction&#x27;</td>
<td style='word-wrap: break-word; white-space: normal;'>The 'instruction' Data Dictionary element is currently blank and will be populated in a future release to resolve.</td>
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Implausible GA</td>
<td style='word-wrap: break-word; white-space: normal;'>A small subset of participants have implausible <code>gestational_age</code> (V01 only) values  for one or more instrument. Until corrected, review GA distribution to exclude outliers from analysis (should be positive and generally &lt; 45 weeks).</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr class="domain-row-issue"><td colspan="4"><strong>MRI</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Raw BIDS</td>
<td style='word-wrap: break-word; white-space: normal;'>There are 2 corrupted raw BIDS files (V02 bold runs under session-level <code>func/</code> folders of <code>rawdata/</code>) to be resolved. Impacted participant IDs/filepaths are available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center; font-weight: bold;'>21</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Run ID</td>
<td style='word-wrap: break-word; white-space: normal;'>The <code>run-{X}</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>XCP-D</td>
<td style='word-wrap: break-word; white-space: normal;'>Tabulated XCP-D Myers-Labonte tables (<code>img_xcpd_hash-{X}_space-fsLR_seg-MyersLabonte_stat-mean_desc-_morph</code>) metadata will be corrected to have a <code>sub_domain</code> value of <code>Structural MRI</code> (currently <code>Resting State fMRI</code>).</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr class="domain-row-issue"><td colspan="4"><strong>NEUROCOGNITION &amp; LANGUAGE</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>MLDS</td>
<td style='word-wrap: break-word; white-space: normal;'>Correct Data Dictionary 'description' element to remove erroneous text that appears at end (e.g., "√Ç √Ç √Ç √Ç ")</td>
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
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr class="domain-row-issue"><td colspan="4"><strong>PHYSICAL HEALTH</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>The Data Dictionary element <code>type_data</code> for <code>average_bmi</code> will be corrected to <code>double</code> (currently=<code>character</code>).</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'><a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Ranges used to filter out-of-range growth measurements</a> in <code>ph_ch_anthro</code> are not age-specific, leading to values that are within the valid range, but biologically implausible for the visit age. Filtering methods will be re-evaluated for the next release.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr class="domain-row-issue"><td colspan="4"><strong>PREGNANCY &amp; EXPOSURE</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>APA 1/2</td>
<td style='word-wrap: break-word; white-space: normal;'>Note that <code>pex_bm_apa_mania_001</code> through <code>mania_005</code> have incorrect Data Dictionary descriptions.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>APA 1/2</td>
<td style='word-wrap: break-word; white-space: normal;'>There are cases where APA Level 2 was administered against gating logic (e.g. for Repetitive Behavior despite there being missing Level 1 responses). As Level 2 administration was not expected, these are not scored (score = "No additional inquiry required") despite having Level 2 item responses present. The Level 2 item-level data will be removed in the future to prevent confusion.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>EPDS</td>
<td style='word-wrap: break-word; white-space: normal;'>N=2 participants in <code>pex_bm_epds</code> have a biologically implausible adjusted age of -1 at V02. Until corrected, please exclude from analyses.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>EPDS</td>
<td style='word-wrap: break-word; white-space: normal;'>Across visits V01-V03, there are a portion of participants with inconsistent data between individual item responses and the calculated sum score, including the following patterns: (1) individual items present, but sum score null; (2) individual items null, but sum score is 0.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Healthv2 Preg</td>
<td style='word-wrap: break-word; white-space: normal;'>The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping. This will be corrected in a future release.</td>
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Healthv2 Preg</td>
<td style='word-wrap: break-word; white-space: normal;'>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank. This will be addressed in a future release.</td>
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>PEX Health</td>
<td style='word-wrap: break-word; white-space: normal;'>ICD codes for the <code>pex_bm_health*</code> instrument tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></td>
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>TLFB</td>
<td style='word-wrap: break-word; white-space: normal;'>Weeks for postnatal recruits were mistakenly reported in the TLFB <strong>versions 1</strong> or <strong>2</strong> instead of <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3"><strong>version 3</strong> adapted for PNR</a>. These will be adjusted to <strong>version 3</strong>.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr class="domain-row-issue"><td colspan="4"><strong>SOCIAL &amp; ENVIRONMENTAL DETERMINANTS</strong></td></tr>
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
</tbody></table>



## <i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i> Pending Updates

<table class="compact-table-no-vertical-lines">

    <thead>
    <tr style="text-decoration: bold; font-size: 1.2em;">
    <th>TABLE/TOPIC</th>
    <th>SUMMARY</th>
    <th style='text-align: center;'><span class="tooltip tooltip-left">PR<span class="tooltiptext">Target Release</span></span></th>
    </tr>
    </thead>
    <tbody>
    
<tr class="domain-row-pending"><td colspan="4"><strong>BEHAVIOR &amp; CAREGIVER-CHILD INTERACTION</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>ECBQ</td>
<td style='word-wrap: break-word; white-space: normal;'>Change coding for "Does not apply" to 8 to match the IBQ-R.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>ERICA</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of the ERICA instrument.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr class="domain-row-pending"><td colspan="4"><strong>BIOSPECIMEN &amp; OMICS</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Olink</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of Olink Explore 384 Inflammation 1 Panel, proteomics measure of maternal inflammation during pregnancy.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Urine</td>
<td style='word-wrap: break-word; white-space: normal;'>Creatinine results (<code>bio_creat_u</code>) are currently excluded from the release due to out-of-range values and will be added once corrected.</td>
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr class="domain-row-pending"><td colspan="4"><strong>DEMOGRAPHICS</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>SU Flags</td>
<td style='word-wrap: break-word; white-space: normal;'>A derived/rolled up substance use flag for Stimulants will be added based on positive instrument-specific Stimulant results.</td>
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>VIsit Info</td>
<td style='word-wrap: break-word; white-space: normal;'>SU flags will include Nail toxicology results in addition to Urine.</td>
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Visit Level Data</td>
<td style='word-wrap: break-word; white-space: normal;'>Date of missed visit (<code>visit_missed_date</code>) is currently excluded from the release due to inaccuracies and will be added once corrected.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr class="domain-row-pending"><td colspan="4"><strong>GENERAL</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Language</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of language of administration across all instruments where applicable.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Multibirth Cohorts</td>
<td style='word-wrap: break-word; white-space: normal;'>Missing instrument fields for Sibling cohorts will be populated and <em>familyID</em> will be incorporated to help identify siblings - <a href="https://docs.hbcdstudy.org/latest/instruments/demo/visitinfo/#warning">see details</a>.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Sequence Field</td>
<td style='word-wrap: break-word; white-space: normal;'>The currently included Sequence field is blank across all instruments and will be removed.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr class="domain-row-pending"><td colspan="4"><strong>MRI</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>BrainSwipes</td>
<td style='word-wrap: break-word; white-space: normal;'>BrainSwipes will be updated with the most recent QC results, currently available in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>DICOMs</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of source DICOMs for all imaging modalities.</td>
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Scanner Info</td>
<td style='word-wrap: break-word; white-space: normal;'>Scanner information (currently available in the scans TSV files within the raw BIDS data as well as all sidecar JSON files) will be provided as tabulated data.</td>
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Summary Forms</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of MRI 'Scan Session' and 'Data' Summary Forms to release data with information from the MRI technician obtained on day of scan.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Var name length</td>
<td style='word-wrap: break-word; white-space: normal;'>Variable names for tabulated MRI data (particularly XCP-D outputs) can be upwards of 167 characters, which may exceed variable name limits in some software and lead to truncation or import errors. Shorter variable names will be implemented in a future release.</td>
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr class="domain-row-pending"><td colspan="4"><strong>NEUROCOGNITION &amp; LANGUAGE</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Bayley-4</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of item-level scores.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>CDI</td>
<td style='word-wrap: break-word; white-space: normal;'>Set percentile scores in <code>ncl_ch_cdiwgen</code> (with the exception of <code>percentile_both</code>) to data type=integer.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Vineland</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of language field to <code>ncl_cg_vabs</code>.</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr class="domain-row-pending"><td colspan="4"><strong>PHYSICAL HEALTH</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>BISQ-SF</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of age-based z-scores to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Z-Scores Excluded</a>).</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Vision Screener</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>ecPROMIS- Sleep</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of summary scores to <code>ph_cg_pms__sleep</code>.</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>ecPROMIS-PAG</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of summary scores to <code>ph_cg_pms__pags</code>. Until added, scores can be calculated by following the <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/ecpromis-pags/#scoring">Scoring Procedures</a> documentation.</td>
<td style='text-align: center; font-weight: bold;'></td>
</tr>
<tr class="domain-row-pending"><td colspan="4"><strong>PREGNANCY &amp; EXPOSURE</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of sex-specific birth weight to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Sex-Specific Birthweight for GA</a>).</td>
<td style='text-align: center; font-weight: bold;'>3</td>
</tr>
<tr class="domain-row-pending"><td colspan="4"><strong>SOCIAL &amp; ENVIRONMENTAL DETERMINANTS</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Child Demo</td>
<td style='word-wrap: break-word; white-space: normal;'>Update household roster count metadata to specify exclusion of Main Child (see "Household Roster" under <a href="https://docs.hbcdstudy.org/latest/instruments/SED/demo-ch/#warning">Data Warning</a>).</td>
<td style='text-align: center; font-weight: bold;'>2.1</td>
</tr>
</tbody></table>

<!-- END KNOWN_ISSUES_TABLE -->