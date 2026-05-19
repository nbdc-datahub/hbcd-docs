<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
.pr-pill {
  display: inline-block;
  padding: 2px 8px;
  font-size: 1em;
  font-weight: 600;
  border-radius: 999px;
  line-height: 1;
  white-space: nowrap;
}
/* Version-specific styling */
.pr-general {
  background-color: #e6f0ff;
  color: #1a4fb3;
}
/* TBD PILL*/
.pr-tbd {
  background-color: #f1f3f5;
  color: #666;
  font-style: italic;
}
/* ICONS */
.icon-rotate {
  color: #199bd6;
  margin-right: 0.4em;
  font-size: 1em;
}
.icon-bug {
  color: #f97316;
  margin-right: 0.4em;
  font-size: 1em;
}
/* DOMAINS LEGEND*/
.study-legend {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
  font-size: 1.0em;
}
.study-legend td {
  vertical-align: top !important;
  padding-top: 0;
  line-height: 1.5;
  border-left: 3px solid transparent;
}
.study-legend i {
  margin-right: 6px;
  color: #0077ff;
  width: 18px;
  text-align: center;
}
</style>

# Known Issues & Pending Updates 

The tables below summarize known issues affecting the current data release and pending updates across study instruments. Entries are organized by domain and include the expected release in which each fix or update will be implemented. This page is updated regularly as new issues are identified and updates are planned.

To ask a question or report an issue, please submit a ticket through the [Help Center in the NBDC Data Access Platform →](https://nbdc.lassoinformatics.com/issue-tracker)

<div id="domains" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-book"></i></span>
  <span class="text-with-link">
    <span class="text">Domains Quick Guide</span>
    <a class="anchor-link" href="#domains" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><i>Click icons to view full list of associated instruments.</i></b></p>
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
</div>

---

<p style="font-size: 1.2em; color: #555; text-align: center; line-height: 2;">
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i> = Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Pending Update &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.1em;"></i> = Target Release for Fix
</p>
    
---


<!-- BEGIN KNOWN_ISSUES_TABLE -->
### Administrative

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Study Navigators</td>
<td>Populate SUBSTANCE_USE and OTHER checkbox fields.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
</tbody></table>


### Behavior &amp; Child-Caregiver Interaction

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>FAD</td>
<td>N=4 V06 participants with &lt;3 item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>MAPS-TL</td>
<td>Notes appear in the score field in both versions (Infant/Toddlerhood) and will be moved to a separate field.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>MAPS-TL (&lt;1yr)</td>
<td>N=4 participants with no item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>ecPROMIS CC</td>
<td>N=12 V03 participants with &lt;3 item responses are incorrectly scored as <code>0</code> in <code>mh_cg_pms__cc__inf</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ECBQ</td>
<td>Change coding for "Does not apply" to 8 to match the IBQ-R.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ERICA</td>
<td>Addition of the ERICA instrument.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>MAPS-TL (Tod)</td>
<td>Pro-rated scoring for <code>mh_cg_mapdb__tod</code> not yet implemented; N=16 participants missing scores.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
</tbody></table>


### Biospecimens &amp; Omics

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Nails</td>
<td>Add unit (mg) for <code>nails_results_nail_weight</code> variable.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Nails</td>
<td>Nail type is <code>4</code> (Unknown) in the main results table (<code>*_nails_results</code>) and should be obtained from the specimen table (<code>*_nails_type</code>).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Nails &amp; Urine</td>
<td>Data dictionary level values have quotes around them, causing the downloaded to have double quotes (e.g. 1=""positive"").</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Olink</td>
<td>Add Olink Explore 384 Inflammation 1 Panel, proteomics measure of maternal inflammation during pregnancy</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Urine</td>
<td>Add creatinine results (<code>bio_creat_u</code>).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
</tbody></table>


### Demographics

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Basic Demo</td>
<td>N=14 participants in <code>sed_basic_demographics</code> have a Maternal Age at V01 of 0; exclude these values from analyses until corrected.</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Basic Demo</td>
<td>
Remove internal <code>recruitment_site</code> categories only present in data dictionary (<code>30-32</code>: Sampled, USDTL, and BAH)</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>RESTRUCTURE</td>
<td>The Demographics domain includes 2 tables with derived information grouped into visit-specific data (<a href="https://docs.hbcdstudy.org/latest/instruments/demo/visitinfo/">Visit Info</a>) and general demographics (<a href="https://docs.hbcdstudy.org/latest/instruments/demo/basicdemo/">Basic Demographics</a>). In a future release, these tables will be restructured to instead organize variables as either longitudinal (dynamic measures that change over time) or global (static measures, such as sex assigned at birth and race/ethnicity).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>SU Flags</td>
<td>A derived/rolled up substance use flag for Stimulants will be added based on positive instrument-specific Stimulant results.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Visit Info</td>
<td>SU flags will include Nail toxicology results in addition to Urine.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
</tbody></table>


### EEG

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>.set files</td>
<td>Update EEG .set files to include subject release IDs.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Age fields</td>
<td>Chronological and adjusted age fall outside of 3-9 months in N=74 V03 sessions (site entry errors); exclude age values prior to analysis.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>MADE</td>
<td>N=3 V04 session derivatives are missing corresponding tabulated data for FACE/MMN tasks. See <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a> for impacted participant IDs.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
</tbody></table>


### General

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Implausible GA</td>
<td>A small subset of participants have implausible <code>gestational_age</code> (V01 only) values  for one or more instrument. Until corrected, review GA distribution to exclude outliers from analysis (should be positive and generally &lt; 45 weeks).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Instruction</td>
<td>The 'instruction' data dictionary element is currently blank.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Language</td>
<td>Add language of administration across all instruments where applicable.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Multibirth Cohorts</td>
<td>Missing instrument fields for Sibling cohorts will be populated and <em>FamilyID</em> will be added to help identify siblings - <a href="https://docs.hbcdstudy.org/latest/instruments/demo/visitinfo/#warning">see details</a>.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Sequence Field</td>
<td>The currently included Sequence field is blank across all instruments and will be removed.</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
</tbody></table>


### MRI

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Raw BIDS</td>
<td>Raw BIDs include 2 corrupted bold runs in V02; view participant IDs/filepaths in the<a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Run ID</td>
<td>The <code>run-[X]</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>XCP-D</td>
<td>Tabulated XCP-D Myers-Labonte tables (<code>img_xcpd_hash-[X]_space-fsLR_seg-MyersLabonte_stat-mean_desc-_morph</code>) metadata will be corrected to have a <code>sub_domain</code> value of <code>Structural MRI</code> (currently <code>Resting State fMRI</code>).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>BrainSwipes</td>
<td>BrainSwipes QC results will be updated with latest results  currently available in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Scanner Info</td>
<td>Scanner information must currently be parsed from raw BIDS data (specifically the scans .tsv files), as described <a href="https://docs.hbcdstudy.org/latest/help/faq/#faq-scanner-info">here</a>. Future releases will include a dedicated 'MRI Info' table that summarizes scanner information across participants, similar to the ABCD study (<a href="https://docs.abcdstudy.org/latest/documentation/imaging/admin.html#mr_y_adm__info">see details</a>).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Source DICOMs</td>
<td>Add source DICOMs for all imaging modalities.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Summary Forms</td>
<td>Add MRI Scan Session + Data Summary Forms (information from the MRI technician obtained on day of scan).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Var name length</td>
<td>Variable names for tabulated MRI data (particularly XCP-D outputs) can be upwards of 167 characters, which may exceed variable name limits in some software and lead to truncation or import errors.</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
</tbody></table>


### Neurocognition &amp; Language

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>MLDS</td>
<td>Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) includes implausible values due to data entry errors. Exclude values &gt;168 hours from analysis.</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Vineland</td>
<td>Subset of variables have a typo in the spelling of "receptive."</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Bayley-4</td>
<td>Add item-level scores.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Vineland</td>
<td>Add language field to <code>ncl_cg_vabs</code>.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
</tbody></table>


### Physical Health

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Growth</td>
<td>Adjusted age contains N=303 "unknown missing" values that are also missing 'Date of Administration'.</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Growth</td>
<td>The data dictionary element <code>type_data</code> for <code>average_bmi</code> will be corrected to <code>double</code> (currently=<code>character</code>).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Growth</td>
<td>Growth (<code>ph_ch_anthro</code>) filter ranges will be updated to be visit-specific, as current ranges allow biologically implausible values (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Range Checks</a>).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>BISQ-SF</td>
<td>Add Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Growth</td>
<td>Add age-based z-scores to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Z-Scores Excluded</a>).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Growth</td>
<td>Add sex-specific birth weight to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Sex-Specific Birthweight for GA</a>).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Vision Screener</td>
<td>Add more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ecPROMIS- Sleep</td>
<td>Add <code>ph_cg_pms__sleep</code>  summary scores</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ecPROMIS-PAG</td>
<td>Add scores to <code>ph_cg_pms__pags</code>. Until added, scores can be calculated by following the <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/ecpromis-pags/#scoring">Scoring Procedures</a> documentation.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
</tbody></table>


### Pregnancy &amp; Environmental Exposure

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>APA 1/2</td>
<td>APA Level 2 was sometimes administered despite unmet gating criteria (e.g., missing Level 1 responses). These cases are not scored (“No additional inquiry required”) even when Level 2 responses are present. Level 2 item data will be removed to avoid confusion.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>EPDS</td>
<td>Inconsistent scoring: (1) item responses present, but score is null (N=1); (2) all items null, but score is <code>0</code> (N≥3).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Healthv2 Preg</td>
<td>The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Healthv2 Preg</td>
<td>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>TLFB</td>
<td>PNR data were incorrectly reported using TLFB versions 1/2 and will be updated to <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3">version 3 specific to PNR</a>.</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>PEX Health</td>
<td>ICD codes for the <code>pex_bm_health*</code> tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
</tbody></table>


### Social &amp; Environmental Determinants

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>C-PACEs</td>
<td>Summary scores are inaccurate; until corrected, users can compute scores following the provided scoring documentation.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Demo</td>
<td>The variables <code>sed_bm_demo_residence_{001|002}</code>, present in the prior release, are missing in the current release.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>eHITS</td>
<td>Participants missing all item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Child Demo</td>
<td>Household roster will be updated to clarify that counts exclude the main child - see <a href="https://docs.hbcdstudy.org/latest/instruments/SED/demo-ch/#warning">Data Warning</a> ("Household Roster")</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Demo</td>
<td>Add V01 household income (<code>income_002</code>) (adult table).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Demo</td>
<td>Add variables on Other Biological Parent (adult table).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Demo</td>
<td>Add <code>work_{002–004}_post</code> (worked for pay + for X hours while pregnant) and <code>work_004__01</code> (job held ≥1 month since V01) (adult table).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Demo</td>
<td>Add household roster fields capturing the sex of listed individuals (adult &amp; child tables).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
</tbody></table><!-- END KNOWN_ISSUES_TABLE -->