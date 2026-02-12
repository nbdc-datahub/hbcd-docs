<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
</style>   

# Release Notes & History

## Participant Population (Inclusion/Exclusion Criteria)

HBCD enrolls at least 25% of participants who have more than minimal substance use during pregnancy, including opioids ([Si et al. 2024](https://doi.org/10.1016/j.dcn.2024.101432)). In addition, HBCD enrollment strategies aimed at yielding a study population that is representative of the individual and geographic characteristics of reproductive-aged women in the United States who had a birth in the past 12 months, and include an adequate comparison group for substance exposed individuals ([Nelson et al. 2024](https://doi.org/10.1016/j.dcn.2024.101441)). There are siblings enrolled in HBCD, some of whom are twins or triplets (multiples). IDs for multiples are presented in the *HBCD Private Release Notes* - see <a href="../../instruments/demo/visitinfo/#multiple-birth-participants" target="_blank">Multiple Birth Participants</a> under **Visit Information** for details.

## General Rules Applied to All Data

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
    <td><strong>Exclusions applied to all data</strong></td>
    <td>
    <ul>
      <li>Inactive participants/sessions excluded</li>
    </ul></td>
</tr>
<tr>
  <td><strong>Field Conversions</strong></td>
  <td>
    <ul>
      <li>Empty fields are replaced with 'n/a'</li>
      <li>Sex is set to 'Other' for participants with only one active Visit 1 (V01) visit</li>
      <li>'Candidate_Age' values are replaced with 'n/a' for Visit 1 (V01)</li>
    </ul>
  </td>
</tr>
</tbody>
</table>

## Version: R2.0

<div style="background:#f2f6fc; padding:12px 20px; border-radius:10px; text-align:center; margin-bottom:25px; box-shadow:0 2px 4px rgba(0,0,0,0.05);">
  <span style="font-size:1.1em; font-weight:600; color:#2a5d9f;">
    <i class="fa-solid fa-calendar" style="margin-right:8px; vertical-align: 1px;"></i>
    Release Date: 2026-02-11
  </span>
</div>

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; margin: 20px 0;">
  <!-- Participants -->
  <div style="background:#f9f9f9; flex:1; min-width:180px; padding:20px; border-radius:12px; box-shadow:0 2px 6px rgba(0,0,0,0.1); text-align:center;">
    <h3 style="margin:0; font-size:1.1em; color:#666;">Participants</h3>
    <p style="margin:10px 0 0; font-size:1.8em; font-weight:600; color:#2a5d9f;">3,605</p>
  </div>
  <!-- Visits -->
  <div style="background:#f9f9f9; flex:1; min-width:180px; padding:20px; border-radius:12px; box-shadow:0 2px 6px rgba(0,0,0,0.1); text-align:center;">
    <h3 style="margin:0; font-size:1.1em; color:#666;">Total Visits</h3>
    <p style="margin:10px 0 0; font-size:1.8em; font-weight:600; color:#2a5d9f;">8,415</p>
    <p style="margin:10px 0 0; font-size:0.9em; color:#444;">
    V01: 3,545 | V02: 2,310<br>
    V03: 1,398 | V04: 679 | V05: 483</p>
  </div>
  <!-- By Sex -->
  <div style="background:#f9f9f9; flex:1; min-width:180px; padding:20px; border-radius:12px; box-shadow:0 2px 6px rgba(0,0,0,0.1); text-align:center;">
    <h3 style="margin:0; font-size:1.1em; color:#666;">By Sex</h3>
    <p style="margin:10px 0 0; font-size:0.9em; color:#444;">
      <i>V02 onwards visit done:</i><br>
      <span style="font-weight:600; color:#2a5d9f;">1,159 (F) | 1,271 (M)</span></p>
      <p style="margin:10px 0 0; font-size:0.9em; color:#444;">
      <i>V01 Only:</i> <span style="font-weight:600; color:#2a5d9f;">1,175 (Unknown)</span></p>
  </div>
</div>

<h4>Below are the key changes made in Release 2.0 - click to expand each section for details.</h4>

<div id="2.0-cohorts" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-user-group"></i></span>
  <span class="text-with-link">
  <span class="text">New Participant Cohorts: Inclusion of Multiple Birth + PNR</span>
  <a class="anchor-link" href="#2.0-cohorts" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>
<ol>
<li><strong>Multiple Birth Participants</strong>: multiple participants from the same birth (e.g. twins)</li>
<li><strong>Postnatal Recruits (PNR)</strong>: joined the study after the child is born (complete a modified V01 and V02)</li>
</ol>
</p>
</div>

<div id="2.0-new-tables" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-table"></i></span>
  <span class="text-with-link">
  <span class="text">+ 40 New Instruments/Measures Across 8 Domains</span>
  <a class="anchor-link" href="#2.0-new-tables" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p style="font-size: 0.9em; color: #696969ff; font-weight: bold;">
<i style="color: teal;" class="fas fa-layer-group"></i>&nbsp;= Concatenated Data - <a href="../../datacuration/file-based-data/#concatenated-data" target="_blank"><i>see details</i></a>
</p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
<thead>
<tr>
<th>Domain</th>
<th>Instrument</th>
<th>Construct</th>
</tr>
</thead>
<tbody>
<tr><td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>BEHAVIOR, BIOLOGY, & ENVIRONMENT</b></td></tr>
<tr>
<td><i style="color: #199bd6; font-size: 1.0rem; margin-right: 2px;" class="fa fa-clipboard-list"></i> <a href="../../instruments/#adm" target="_blank"> Administrative</a></td>
  <td><i style="color: teal;" class="fas fa-layer-group"></i>&nbsp;  Study Navigator Contact Form</td>
  <td>Recruitment/Retention</td>
</tr>
<tr>
<td rowspan="7"><i style="color: #199bd6; font-size: 1.0rem; margin-right: 2px;" class="fa fa-people-arrows"></i> <a href="../../instruments/#mh" target="_blank"> Beh & CH-CG Int</a></td>
<td>CHAOS</td><td>Family Organization</td>
</tr>
<tr><td>ecPROMIS CH-CG Relationship <b>[1-5 year]</b></td><td>Child-Caregiver Interaction</td></tr>
<tr><td>ecPROMIS Peer Relationships</td><td>Peer Relationships</td></tr>
<tr><td>ecPROMIS Self-Regulation</td><td>Self-Regulation and Flexibility</td></tr>
<tr><td>FAD (GF6+)</td><td style="word-wrap: break-word; white-space: normal;">Global Functioning of Family Unit</td></tr>
<tr><td>ECBQ (VSF)+BI</td><td>Early Childhood Behavior + Inhibition</td></tr>
<tr><td>MAPS-TL <b>[Toddlerhood & Preschool]</td> <td>Irritability</td></tr>
<tr>
<td><i style="color: #199bd6; font-size: 1.0rem; margin-right: 2px;" class="fa fa-vial"></i> <a href="../../instruments/#biospec" target="_blank"> Biospecimen & Omics</a></td>
<td><i style="color: teal;" class="fas fa-layer-group"></i>&nbsp; Illumina GDA GWAS</td>
<td>GWAS, EWAS, Transcriptome</td>
</tr>
<tr><td rowspan="4"><i style="color: #199bd6; font-size: 1.0rem; margin-right: 2px;" class="fa-solid fa-puzzle-piece"></i> <a href="../../instruments/#ncl" target="_blank"> Neurocog & Language</a></td>
<td>Bayley-4 Scales</td><td>Child Development (Cognitive, Language, Motor)</td>
</tr>
<tr><td>MacArthur-Bates CDI-I</td><td>Language Development (Words & Gestures)</td></tr>
<tr><td>SPM-2 <b>[Toddler]</b></td>  <td>Sensory Processing/Integration</td></tr>
<tr><td>Vineland Adaptive Behavior</td><td>Adaptive Behavior</td></tr>
<tr><td rowspan="7"><i style="color: #199bd6; font-size: 1.0rem; margin-right: 2px;" class="fa fa-heart-pulse"></i> <a href="../../instruments/#ph" target="_blank"> Physical Health</a></td>
<td>Brief Infant Sleep Questionnaire</td><td>Sleep</td>
</tr>
<tr><td>ecPROMIS Physical Activity/Greenspace</td> <td>Physical Activity</td></tr>
<tr><td>ecPROMIS Sleep</td> <td>Sleep</td></tr>
<tr><td>Medical History</td><td>Medical History</td></tr>
<tr><td>Infant Nutrition Questionnaire</td><td>Nutrition</td></tr>
<tr><td>Screen-Based Media Use (<i>ScreenQ</i>)</td><td>Media Use</td></tr>
<tr><td>Vision Screener</td><td>Vision</td></tr>
<tr><td rowspan="2"><i style="color: #199bd6; font-size: 1.0rem; margin-right: 2px;" class="fa-solid fa-baby"></i> <a href="../../instruments/#pex" target="_blank"> Pregnancy & Exposure</a></td>
<td>ASSIST <b>[V4]</b></td>  <td>Substance Use Post-Pregnancy</td></tr>
<tr><td>Substance Use Patterns</td>  <td>Substance Use in Pregnancy</td></tr>
<tr><td rowspan="12"><i style="color: #199bd6; font-size: 1.0rem; margin-right: 2px;" class="fas fa-city"></i> <a href="../../instruments/#sed" target="_blank"> Social & Environment</a></td>
<td><i style="color: teal;" class="fas fa-layer-group"></i>&nbsp; Geocoded Linkage</td>  <td>Neighborhood Measures</td></tr>
<tr><td>ACEs</td>  <td>Adverse Childhood Experiences</td></tr>
<tr><td>Child Demographics - V4 & V6</td><td>Demographics</td></tr>
<tr><td>Composite Abuse Scale (CABr-SF)</td>  <td>Intimate Partner Violence</td></tr>
<tr><td>Current Employment</td><td>Current Employment</td></tr>  
<tr><td>HOME-21 IT</td><td>Child’s Home Environment</td></tr>  
<tr><td>Household Chemical Exposures</td> <td>Household Chemical Exposures</td></tr>  
<tr><td>Lead Exposures</td><td>Lead Exposures</td></tr> 
<tr><td>PACES <b>[&lt;18]</b></td><td>Protective Factors</td></tr>  
<tr><td>Second Hand Smoke Exposure</td> <td>Second Hand Smoke Exposure</td></tr>
<tr><td>Transition in Care Screener</td><td>Recruitment/Retention</td></tr>
<tr><td>Vancouver Index of Acculturation (VIA)</td><td>Acculturation</td></tr> 
<tr><td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>BRAIN ACTIVITY & BIOSENSORS</b></td></tr>
<tr>
<td rowspan="2"><i style="color: #199bd6; font-size: 1.0rem; margin-right: 2px;" class="fa-solid fa-file-waveform"></i> <a href="../../instruments/#eeg" target="_blank"> EEG</a></td>
<td>EEG Acquisition Checklist + Reattempt 1/2</td><td>Acquisition Checklists</td></tr>
<tr><td>ERP SummaryStats</td><td>Tabulated HBCD-MADE derivatives</td></tr>
<tr>
<td><i style="color: #199bd6; font-size: 1.0rem; margin-right: 2px;" class="fa fa-brain"></i> <a href="../../instruments/#mri" target="_blank"> MRI</a></td>
<td>Pre-Scan Questionnaire</td><td>Infant Sleep Environment</td>
</tr>
<tr>
<td><i style="color: #199bd6; font-size: 1.0rem; margin-right: 2px;" class="fa fa-microchip"></i> <a href="../../instruments/#sensors" target="_blank"> Novel Tech & Wearables</a></td>
<td>Biosensor Receipt & Setup</td><td>Administrative</td></tr>
</tr>
</tbody>
</table>
</div>

<div id="2.0-mri-eeg" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-brain"></i></span>
  <span class="text-with-link">
  <span class="text">MRI & EEG: New processed derivatives, full raw BIDS inclusion, & scanner metadata</span>
  <a class="anchor-link" href="#2.0-mri-eeg" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><b>Cross-Modality Updates (MRI &amp; EEG)</b></p>
<ul>
<li><strong>Full Raw BIDS Inclusion</strong>: All raw BIDS data are now included for both MRI and EEG (previously, only raw data that passed initial raw-data quality control were released).</li>
<li><strong>Additional participant- and visit-level data</strong> </li>
</ul>
<p><b>MRI-Specific Updates</b></p>
<ul>
<li><b>Enhanced <a href="../../datacuration/file-based-data/#participant-session-scan-level-data" target="_blank">Scans TSV</a> metadata</b>: The session-level <code>sub-{ID}_ses-{V0X}_scans.tsv</code> files now include detailed scanner metadata, including: <code>ScannerManufacturer</code>, <code>ScannerModel</code>, <code>ScannerSoftwareVersion</code>, and <code>ScannerSerialNumber</code> (enables differentiation of multiple scanners within the same site).   </li>
<li><strong>Processed data exclusion criteria updated</strong>: New procedures have been implemented to remove MRI derivatives with serious data quality issues.
See: <a href="../../instruments/mri/exclusion-criteria/#processed-data-exclusion-criteria">MR Exclusion Criteria</a> for full details.</li>
</ul>
</div>

<div id="r2.0res-KI" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa-solid fa-arrows-rotate"></i></span>
  <span class="text-with-link">
  <span class="text">10+ Resolved Known Issues</span>
  <a class="anchor-link" href="#r2.0res-KI" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8c4266; color: #6e6256ff;">
  <tr>
    <th style="width: 1%;">Domain</th>
    <th>Table/Data</th>
    <th>Resolved Known Issue</th>
  </tr>
</thead>
<tbody>
<tr>
  <td style="text-align: center;">N/A</td>
  <td>General</td>
  <td style="word-wrap: break-word; white-space: normal;"><b>[1]</b> Resolved lower floating-point value precision in Parquet files by creating all data available in the release in one step (<code>type_data</code>=<i>doubles</i>)</td>
</tr>
<tr>
  <td rowspan="6" style="text-align: center;"><a href="../../instruments/#demo" target="_blank"><i class="fas fa-id-card"></i></a></td>
  <td rowspan="3">Basic Demographics<br><code>sed_basic_demographics</code></td>
  <td><b>[1]</b> Removal of invalid response option 2 = <i>Hawaiian</i> from Mother Race (<code>screen_mother_race</code>).</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">
  <b>[2]</b> Removed Child Multi-Race (<code>child_ethnoracial_acs_by_multi_race</code>) variable due to duplicated coding to Child Multi-Ethnicity (<code>child_ethnoracial_acs_by_multi_ethnicity</code>).
  </td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<b>[3]</b> Removed Child Multi-Ethnicity V01 data.
</td>
</tr>
<tr>
<td rowspan="3">Visit Level Data<br><code>par_visit_data</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  <b>[1]</b> Participants who did <b>not</b> withdraw from the study (<code>participant_withdrawal</code> = “no”) were assigned a sentinel withdrawal date (<code>participant_withdrawal_date</code>) of <code>12/26/1999</code>. These values were updated to null for clarity and consistency.
</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<b>[2]</b> Removed V02 Biospec substance use flags <a href="../../instruments/demo/visitinfo/#substance-use-flags">derived from USDTL urine toxicology</a> (<code>su_flag_bio_*</code>) (urine samples not collected at V02).
</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
<b>[3]</b> Corrected values (replaced 'no' with 'null') of the TLFB substance use flags (<code>su_flag_tlfb_*</code>) for participants without a V02 visit.
</td>
</tr>
<tr>
<td style="text-align: center;"><a href="../../instruments/#biospec" target="_blank"><i class="fa fa-vial"></i></a></td>
<td>Urine toxicology</td>
  <td style="word-wrap: break-word; white-space: normal;">
  Restored 'missing' values for urinary cotinine (<code>bio_bm_biosample_urine__results_results_bio_c_cot_u</code>) erroneously set to <code>0</code> (N = 18).
</td>
</tr>
<tr>
  <td rowspan="2" style="text-align: center;"><a href="../../instruments/#ncl" target="_blank"><i class="fa-solid fa-puzzle-piece"></i></a></td>
  <td rowspan="2">SPM-2<br><code>ncl_cg_spm2__inf</code></td>
  <td style="word-wrap: break-word; white-space: normal;">
  <b>[1]</b> Added age fields - <code>gestational_age</code>, <code>adjusted_age</code>, and <code>candidate_age</code>.
</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">
  <b>[2]</b> Added Status Scores that were missing for all but one subscale.
</td>
</tr>
<tr>
  <td rowspan="2" style="text-align: center;"><a href="../../instruments/#pex" target="_blank"><i class="fa-solid fa-baby"></i></a></td>
  <td>APA 1/2<br><code>pex_bm_apa_anger_*</code></td>
  <td style="word-wrap: break-word; white-space: normal;">
  Added missing T-scores and total scores to Anger subscale (remaining subscales intact).
</td>
</tr>
<tr>
  <td>TLFB<br><code>pex_ch_tlfb</code></td>
  <td style="word-wrap: break-word; white-space: normal;">
  Added age variable fields - <code>gestational_age</code>, <code>adjusted_age</code>, and <code>candidate_age</code>.
</td>
</tr>
<tr>
  <td style="text-align: center;"><a href="../../instruments/#sed" target="_blank"><i class="fas fa-city"></i></a></td>
  <td>eHITS<br><code>sed_bm_ehits</code></td>
  <td style="word-wrap: break-word; white-space: normal;">
  Corrected calculation for the two eHits "score" variables (<code>score</code> & <code>total_score</code>).
</td>
</tr>
</tbody>
</table>
</div>

-----------------------

## Version: R1.1

<div style="background:#f2f6fc; padding:12px 20px; border-radius:10px; text-align:center; margin-bottom:25px; box-shadow:0 2px 4px rgba(0,0,0,0.05);">
  <span style="font-size:1.1em; font-weight:600; color:#2a5d9f;">
    <i class="fa-solid fa-calendar" style="margin-right:8px; vertical-align: 1px;"></i>
    Release Date: 2025-10-10
  </span>
</div>

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; margin: 20px 0;">
  <!-- Participants -->
  <div style="background:#f9f9f9; flex:1; min-width:180px; padding:20px; border-radius:12px; box-shadow:0 2px 6px rgba(0,0,0,0.1); text-align:center;">
    <h3 style="margin:0; font-size:1.1em; color:#666;">Participants</h3>
    <p style="margin:10px 0 0; font-size:1.8em; font-weight:600; color:#2a5d9f;">1,426</p>
  </div>
  <!-- Visits -->
  <div style="background:#f9f9f9; flex:1; min-width:180px; padding:20px; border-radius:12px; box-shadow:0 2px 6px rgba(0,0,0,0.1); text-align:center;">
    <h3 style="margin:0; font-size:1.1em; color:#666;">Total Visits</h3>
    <p style="margin:10px 0 0; font-size:1.8em; font-weight:600; color:#2a5d9f;">2,207</p>
    <p style="margin:10px 0 0; font-size:0.9em; color:#444;">V01: 1,426 | V02: 660 | V03: 121</p>
  </div>
  <!-- By Sex -->
  <div style="background:#f9f9f9; flex:1; min-width:180px; padding:20px; border-radius:12px; box-shadow:0 2px 6px rgba(0,0,0,0.1); text-align:center;">
    <h3 style="margin:0; font-size:1.1em; color:#666;">By Sex (V02/V03)</h3>
    <p style="margin:10px 0 0; font-size:1.4em; font-weight:600; color:#2a5d9f;">
      ♀ 328 &nbsp; | &nbsp; ♂ 338
    </p>
  </div>
</div>

### 1.1 Existing Study Data Updates

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 16px;">
<thead>
<th>Domain</th>
<th>Table/Data</th>
<th>Update/Improvement</th>
</thead>
<tbody>
<tr>
  <td style="text-align: center;"><span class="tooltip tooltip-right"><i class="fas fa-id-card" style="font-size:1.1em; margin-right: 2px;"></i><span class="tooltiptext">Demographics</span></span></td>
  <td>Basic Demographics<br><code>sed_basic_demographics</code></td>
  <td style="word-wrap: break-word; white-space: normal;">
  Reviewed scoring for AOU and ACS EthnoRacial fields. The multiracial options for <strong>ACS – Child – Multi Race</strong> (<code>child_ethnoracial_acs_by_multi_race</code>) were merged into one due to limited granularity in the <em>child_race</em> field.</td>
</tr>
<tr>
  <td style="text-align: center;"><span class="tooltip tooltip-right"><i class="fa fa-vial" style="font-size:1.1em; margin-right: 2px;"></i><span class="tooltiptext">Biospecimen & Omics</span></span></td>
  <td>Nails & Urine Toxicology<br><code>bio_bm_biosample_*</code></td>
  <td style="word-wrap: break-word; white-space: normal;">
  Removed 'Specimen ID’ fields from all Biospecimen tables and time from dates in 'Nails Results.'
</td>
</tr>
<tr>
  <td style="text-align: center;"><span class="tooltip tooltip-right"><i class="fa-solid fa-baby" style="font-size:1.1em; margin-right: 2px;"></i><span class="tooltiptext">Pregnancy Exposure, Including Substance Use</span></span></td>
  <td>Pregnancy & Infant Health<br><code>pex_bm_health*</code></td>
  <td style="word-wrap: break-word; white-space: normal;">
  Medications are now categorized into more detailed components based on <strong>RxNorm IDs</strong> to improve clarity and enable more granular analyses.
  Additional columns specify: <em>Brand Name</em>, <em>Ingredient</em>, <em>Precise Ingredient</em>, and <em>Multiple Active Ingredients</em>.
</td>
</tr>
<tr>
  <td style="text-align: center;"><span class="tooltip tooltip-right"><i class="fas fa-city" style="font-size:1.1em; margin-right: 2px;"></i><span class="tooltiptext">Social & Environmental Determinants</span></span></td>
  <td>V01 Demographics<br><code>sed_bm_demo</code></td>
  <td style="word-wrap: break-word; white-space: normal;">
  Added <strong>Birth Parent Sexual Orientation</strong> variable.
</td>
</tr>
<tr>
  <td style="text-align: center;"><span class="tooltip tooltip-right"><i class="fa fa-brain" style="font-size:1.1em; margin-right: 2px;"></i><span class="tooltiptext">Magnetic Resonance Imaging & Spectroscopy</span></span></td>
  <td>BrainSwipes QC<br><code>img_brainswipes*</code></td>
  <td style="word-wrap: break-word; white-space: normal;">
  Added QC results missing from R1.0 (N=8).
</td>
</tr>
</tbody>
</table>
<p></p><p></p>

<div id="updatedfiles" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-arrows-rotate"></i></span>
  <span class="text-with-link">
  <span class="text">Full Updated File List</span>
  <a class="anchor-link" href="#visitinfo" title="updatedfiles">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Basic Demographics</strong></p>
<ul>
<li><code>sed_basic_demographics.json</code></li>
<li><code>sed_basic_demographics.parquet</code></li>
<li><code>sed_basic_demographics.tsv</code></li>
</ul>
<p><strong>BioSpecimens</strong></p>
<ul>
<li><code>bio_bm_biosample_nails_results.json</code></li>
<li><code>bio_bm_biosample_nails_results.parquet</code></li>
<li><code>bio_bm_biosample_nails_results.tsv</code></li>
<li><code>bio_bm_biosample_nails_results_shadow.parquet</code></li>
<li><code>bio_bm_biosample_nails_results_shadow.tsv</code></li>
<li><code>bio_bm_biosample_urine.json</code></li>
<li><code>bio_bm_biosample_urine_results.parquet</code></li>
<li><code>bio_bm_biosample_urine_results.tsv</code></li>
<li><code>bio_bm_biosample_urine_results_shadow.parquet</code></li>
<li><code>bio_bm_biosample_urine_results_shadow.tsv</code></li>
</ul>
<p><strong>SPM-2</strong></p>
<ul>
<li><code>ncl_cg_spm2__inf.json</code></li>
<li><code>ncl_cg_spm2__inf.parquet</code></li>
<li><code>ncl_cg_spm2__inf.tsv</code></li>
<li><code>ncl_cg_spm2__inf_shadow.parquet</code></li>
<li><code>ncl_cg_spm2__inf_shadow.tsv</code></li>
</ul>
<p><strong>TLFB</strong></p>
<ul>
<li><code>pex_ch_tlfb.json</code></li>
<li><code>pex_ch_tlfb.parquet</code></li>
<li><code>pex_ch_tlfb.tsv</code></li>
<li><code>pex_ch_tlfb_shadow.parquet</code></li>
<li><code>pex_ch_tlfb_shadow.tsv</code></li>
</ul>
<p><strong>PEX Health V2 Preg</strong></p>
<ul>
<li><code>pex_bm_healthv2_preg.json</code></li>
</ul>
</div>

### 1.1 Resolved Known Issues

<div id="r1.1demo" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><a href="../../instruments/#demo" target="_blank"><i class="fas fa-id-card"></i></a></span>
  <span class="text-with-link">
  <span class="text">Demographics</span>
  <a class="anchor-link" href="#r1.1demo" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p style="font-size: 1.0em;"><strong>Basic Demographics (<code>sed_basic_demographics</code>)</strong></p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
  <tr>
    <td>
      <strong>Income Not Displayed For All Participants</strong> (<code>income</code>)<br>
    Missing income fields for subset of subjects now added.</td>
  </tr>  
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
    <strong>Duplicate Options for 'Mother Race' Variable</strong> (<code>screen_mother_race</code>)<br>
    Option #3, a duplicate of option #5 for 'Black African American,' now removed.</td>
  </tr>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
    <strong>Gestational Age at Delivery and Mother’s Age at Delivery</strong> (<code>&lt;gestational|mother&gt;_age_delivery</code>)<br>
    Data from deliveries that occurred after the R1.0 cutoff date of 2025-07-01 (and therefore did not undergo QC) now removed so that only eligible participants with V01 + V02 or V03 are retained.</td>
  </tr>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
    <strong>Mother Ethnicity</strong> (<code>screen_mother_ethnicity</code>)<br>
    Incorrectly documented as a 4-level variable in the data dictionary, with additional values of 0 and 1 that were not used. The data now only includes the valid levels: 2 (Hispanic) and 3 (Non-Hispanic).</td>
  </tr>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
    <strong>Mother Race & Ethnicity</strong> (<code>rc_mother_ethnoracial_aou_race_ethnicity</code>)<br>
    Addition of formerly missing response option, "None of these fully describe me/Other."</td>
  </tr>
</tbody>
</table>
<p style="font-size: 1.0em;"><strong>Visit Level Data (<code>par_visit_data</code>)</strong></p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
      Addition of missing <strong>Substance Use flags</strong> (<i><a href="../../instruments/demo/visitinfo/#substance-use-flags">see details</a></i>) for alcohol, opioid, cannabis, and nicotine.</td>
  </tr>  
</tbody>
</table>
</div>

<div id="r1.1biospec" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><a href="../../instruments/#biospec" target="_blank"><i class="fa fa-vial"></i></a></span>
  <span class="text-with-link">
  <span class="text">Biospecimens</span>
  <a class="anchor-link" href="#r1.1biospec" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p style="font-size: 1.0em;"><strong>Nails & Urine (<code>bio_bm_biosample_&lt;nails|urine&gt;</code>)</strong></p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
  <tr>
  <td>Addition of formerly missing <strong>collection and analysis dates</strong> (<i>Collection/Received/Report</i>).</td>
  </tr>  
</tbody>
</table>
<p style="font-size: 1.0em;"><strong>Urine (<code>bio_bm_biosample_urine_results</code>)</strong></p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
      <strong>Corrected Specific Gravity Variable</strong><br>
      Values for the 'Urine Specific Gravity' field (<code>bio_spg_u</code>) have been set to the correct floating point value for the appropriate thousandths format (were previously set to '1' and data type to 'integer'). The corrected variable can now be used for urinary concentration corrections.</td>
  </tr>  
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
      <strong>Toxicology (Cotinine)</strong><br>
      All negative values for urinary toxicology results field <code>bio_c_cot_u</code> are now set to ‘0’ (as negative values are not biologically plausible).</td>
  </tr> 
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
      <strong>Corrected Negative Gestational Ages</strong><br>
      The negative gestational ages for 2 participants in the Urine dataset have been corrected.</td>
  </tr>  
</tbody>
</table>
</div>

<div id="r1.1eeg" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><a href="../../instruments/#eeg" target="_blank"><i class="fa-solid fa-file-waveform"></i></a></span>
  <span class="text-with-link">
  <span class="text">EEG</span>
  <a class="anchor-link" href="#r1.1eeg" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
    The <strong>HBCD-MADE</strong> resting-state derivative files (<code>processed_data/*_task-RS_powerSummaryStats.csv</code>) have been removed due to errors caused by a previous pipeline bug. These files should not be used for analysis. Users can regenerate the corresponding summary statistics using the scripts provided in  <a href="https://hbcd-eeg-utilities.readthedocs.io/en/stable/">HBCD EEG Utilities</a>.
    </td>
  </tr>  
</tbody>
</table>
</div>

<div id="r1.1ngl" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><a href="../../instruments/#ncl" target="_blank"><i class="fa-solid fa-puzzle-piece"></i></a></span>
  <span class="text-with-link">
  <span class="text">Neurocognition & Language</span>
  <a class="anchor-link" href="#r1.1ngl" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
      The <strong>SPM-2 (<code>ncl_cg_spm2__inf</code>)</strong> now includes <strong>verified t-scores</strong>, originally excluded due to errors in conversion from raw scores.</td>
  </tr>  
</tbody>
</table>
</div>

<div id="r1.1pex" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><a href="../../instruments/#pex" target="_blank"><i class="fa-solid fa-baby"></i></a></span>
  <span class="text-with-link">
  <span class="text">Pregnancy & Exposure, Including Substance Use</span>
  <a class="anchor-link" href="#r1.1pex" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
      <strong>Health V2- Infancy</strong> (<code>pex_bm_healthv2_inf</code>)<br>
      Erroneously included descriptive fields <code>001__00</code> - <code>005__00</code> now removed.</td>
  </tr>  
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
      <strong>APA 1/2 (<code>pex_bm_apa</code>)</strong><br>
      Summary scores and corresponding T-scores are now provided, where appropriate, for Level 2 domains.
    </td>
  </tr>  
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
      <strong>EPDS (<code>pex_bm_epds</code>)</strong><br>
      Duplicate data for each item (e.g., <code>epds_001</code> and <code>epds_001_01</code>) now removed.</td>
  </tr>  
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
      <strong>TLFB (<code>pex_ch_tlfb</code>)</strong><br>
      <strong>#1 Corrected logic for TLFB substance use flags</strong><br>
      Previously, only the alcohol use flag applied the intended criteria (use during or after pregnancy across V01–V02). All substance use flags now follow this logic.
      </td>
  </tr>    
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
      <strong>#2 Age Variables Removed</strong><br>
      TLFB age variable fields (<i>gestational_age</i>, <i>adjusted_age</i>, and <i>candidate_age</i>) are now removed due to incorrect values.</td>
  </tr>  
</tbody>
</table>
</div>

## Version: R1.0

<div style="background:#f2f6fc; padding:12px 20px; border-radius:10px; text-align:center; margin-bottom:25px; box-shadow:0 2px 4px rgba(0,0,0,0.05);">
  <span style="font-size:1.1em; font-weight:600; color:#2a5d9f;">
    <i class="fa-solid fa-calendar" style="margin-right:8px; vertical-align: 1px;"></i>
    Release Date: 2025-06-26
  </span>
</div>

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; margin: 20px 0;">
  <!-- Participants -->
  <div style="background:#f9f9f9; flex:1; min-width:180px; padding:20px; border-radius:12px; box-shadow:0 2px 6px rgba(0,0,0,0.1); text-align:center;">
    <h3 style="margin:0; font-size:1.1em; color:#666;">Participants</h3>
    <p style="margin:10px 0 0; font-size:1.8em; font-weight:600; color:#2a5d9f;">1,426</p>
  </div>
  <!-- Visits -->
  <div style="background:#f9f9f9; flex:1; min-width:180px; padding:20px; border-radius:12px; box-shadow:0 2px 6px rgba(0,0,0,0.1); text-align:center;">
    <h3 style="margin:0; font-size:1.1em; color:#666;">Total Visits</h3>
    <p style="margin:10px 0 0; font-size:1.8em; font-weight:600; color:#2a5d9f;">2,207</p>
    <p style="margin:10px 0 0; font-size:0.9em; color:#444;">V01: 1,426 | V02: 660 | V03: 121</p>
  </div>
  <!-- By Sex -->
  <div style="background:#f9f9f9; flex:1; min-width:180px; padding:20px; border-radius:12px; box-shadow:0 2px 6px rgba(0,0,0,0.1); text-align:center;">
    <h3 style="margin:0; font-size:1.1em; color:#666;">By Sex (V02/V03)</h3>
    <p style="margin:10px 0 0; font-size:1.4em; font-weight:600; color:#2a5d9f;">
      ♀ 328 &nbsp; | &nbsp; ♂ 338
    </p>
  </div>
</div>

#### Participant & Visit Exclusions

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
  <td><strong>Excluded Participants</strong></td>
  <td>
    <ul>
      <li>Participants with no brain rating or brain rating noted as "atypical"</li>
      <li>Postnatal Recruitment participants</li>
      <li>Multiple Birth participants</li>
    </ul>
  </td>
</tr>
<tr>
    <td><strong>Excluded Visit Data</strong></td>
    <td>
    <ul>
      <li>Visits with 'LaunchPad Complete' Status set to 'Complete' after 2024-07-01.</li>
    </ul>
</tr>
</tbody>
</table>

#### Instrument & Field Exclusions

<div id="r1-exclusions" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-filter"></i></span>
  <span class="text-with-link">
  <span class="text"><i>Click to Expand</i></span>
  <a class="anchor-link" href="#r1-exclusions" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p style="font-size: 1.0em;"><strong>Instrument Exclusions</strong></p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <th>Instrument</th>
  <th>Table Name</th>
</thead>
<tbody>
<tr><td>Biosensor Receipt Form</td><td><code>sens_ch_rcpt</code></td></tr>
<tr><td>EEG Acquisition Checklists</td><td><code>eeg_ch_chkl</code> / <code>eeg_ch_chkl_&lt;1|2&gt;</code></td></tr>
<tr><td>ERICA forms</td><td><code>mh_cg_erica_&lt;3_7m|7_9m&gt;</code> / <code>mh_cg_erica_fcm_adm_&lt;3_7m|7_9m&gt;</code></td></tr>
<tr><td>GABI Setup/Receipt</td><td><code>nt_pa_gabi_setup</code> / <code>nt_pa_gabi_rcpt</code></td></tr>
<tr><td>MRI Checklists & Pre/Post Scan Prep</td><td><code>mri_ra_chkl_data</code> / <code>mri_ra_chkl_scan</code> / <code>mri_ra_prep</code></td></tr>
<tr><td>NIH Baby ToolBox</td><td><code>ncl_ch_nbtb</code></td></tr>
<tr><td>Participant / RA Feedback</td><td><code>adm_cg_fb</code> / <code>adm_ra_fb</code></td></tr>
<tr><td>Urgent Events & Participant Alerts</td><td><code>adm_fd_urgent</code> / <code>admin_alert</code></td></tr>
<tr><td>Visit Start / Visit Level Data</td><td><code>visit_start</code> / <code>adm_fd_visitdata</code></td></tr>
</tbody>
</table>
<p style="font-size: 1.0em;"><strong>Instrument Field Exclusions</strong></p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <th>Table Field(s)</th>
  <th>Field Name(s)/Details</th>
</thead>
<tbody>
  <tr><td>Date of Administration</td><td><code>date_taken</code></td></tr>
  <tr><td>Examiner</td><td><code>examiner</code></td></tr>
  <tr><td>REDCap Complete status</td><td><code>complete</code></td>
  <tr><td>Timestamps</td><td><code>timestamp</code> / <code>timestamp_start</code> / <code>timestamp_stop</code> / <code>timestamp_redcap_locked</code></td></tr>
  </tr><tr><td>Visit Data</td><td><code>visit_stage</code> removed from the <code>visit_data</code> category</td></tr>
  <tr><td>Breast Feeding History Fields</td><td><code>ph_cg_phx_i_bfh</code> – All fields except <code>001</code> excluded</td></tr>
  <tr><td>Height/Weight/Head Circumference BMI</td><td><code>ph_ch_anthro</code> – BMI-related fields removed</td></tr>
</tbody>
</table>
</div>


