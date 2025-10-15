# Release Notes & History

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
  <span class="text">Full Updated Files List</span>
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
<li><code>bio_bm_biosample_urine.parquet</code></li>
<li><code>bio_bm_biosample_urine.tsv</code></li>
<li><code>bio_bm_biosample_urine_shadow.parquet</code></li>
<li><code>bio_bm_biosample_urine_shadow.tsv</code></li>
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
  <span class="text-with-link">
  <span class="text">Demographics</span>
  <a class="anchor-link" href="#r1.1demo" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead>
  <tr>
    <th>Table/Data</th>
    <th>Resolved Known Issue</th>
  </tr>
</thead>
<tbody>
<!-- Demo -->
<tr>
  <td rowspan="5">
    <div class="icon-text-block">
      <a href="../../instruments/#demo" target="_blank">
        <i class="fas fa-id-card"></i>
      </a>
      <div class="text-block">
        Basic Demographics<br>
        <code>sed_basic_demographics</code>
      </div>
    </div>
  </td>
  <td>Added income fields (<code>income</code>) originally missing for subset of subjects.</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Removed Mother Race (<code>screen_mother_race</code>) variable option #3, a duplicate of option #5 for 'Black African American.'</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Removed Gestational/Mother’s Age at Delivery (<code>&lt;gestational|mother&gt;_age_delivery</code>) that occurred after the R1.0 cutoff date of 2025-07-01 (and therefore did not undergo QC).</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Removed invalid levels 0 & 1 from Mother Ethnicity (<code>screen_mother_ethnicity</code>). Valid levels remaining: 2 (Hispanic) and 3 (Non-Hispanic).</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Added response option ("None of these fully describe me/Other") for Mother Race & Ethnicity (<code>rc_mother_ethnoracial_aou_race_ethnicity</code>).</td>
</tr>
<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#demo" target="_blank">
        <i class="fas fa-id-card"></i>
      </a>
      <div class="text-block">
        Visit Information<br>
        <code>par_visit_data</code>
      </div>
    </div>
  </td>
  <td style="word-wrap: break-word; white-space: normal;">Added Substance Use flags (<i><a href="../../instruments/demo/visitinfo/#substance-use-flags">see details</a></i>) for alcohol, opioid, cannabis, and nicotine.</td>
</tr>
</tbody>
</table>
</div>

<div id="r1.1behbioenv" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Behavior, Biology, & Environment</span>
  <a class="anchor-link" href="#r1.1begbioenv" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead>
  <tr>
    <th>Table/Data</th>
    <th>Resolved Known Issue</th>
  </tr>
</thead>
<tbody>
<!-- Biospec -->
<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#biospec" target="_blank">
        <i class="fas fa-vial"></i>
      </a>
      <div class="text-block">
        Nails & Urine<br>
        <code>bio_bm_biosample_*</code>
      </div>
    </div>
  </td>
  <td style="word-wrap: break-word; white-space: normal;">Added collection and analysis dates (<i>Collection/Received/Report</i>) to all tables.</td>
</tr>
<tr>
  <td rowspan="3">
    <div class="icon-text-block">
      <a href="../../instruments/#biospec" target="_blank">
        <i class="fas fa-vial"></i>
      </a>
      <div class="text-block">
        Urine<br>
        <code>bio_bm_biosample_urine</code>
      </div>
    </div>
  </td>
  <td style="word-wrap: break-word; white-space: normal;">Corrected 'Urine Specific Gravity' field (<code>bio_spg_u</code>) to floating point values for the appropriate thousandths format (previously set to '1' and data type to 'integer').</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Set all negative values for Urinary Toxicology (Cotinine) results (<code>bio_c_cot_u</code>) to ‘0’ (negative values are not biologically plausible).</td>
</tr>
<tr>
  <td>Corrected negative gestational ages for 2 participants in the Urine dataset.</td>
</tr>
<!-- Neurocog -->
<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#neurocog" target="_blank">
        <i class="fa-solid fa-puzzle-piece"></i>
      </a>
      <div class="text-block">
        SPM-2<br>
        <code>ncl_cg_spm2__inf</code>
      </div>
    </div>
  </td>
  <td>Added verified t-scores (originally excluded due to errors in conversion from raw scores).</td>
</tr>
<!-- PEX -->
<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#pex" target="_blank">
        <i class="fa-solid fa-baby"></i>
      </a>
      <div class="text-block">
        Health V2 - Infancy<br>
        <code>pex_bm_healthv2_inf</code>
      </div>
    </div>
  </td>
  <td>Removed erroneously included descriptive fields <code>001__00</code> - <code>005__00</code>.</td>
</tr>
<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#pex" target="_blank">
        <i class="fa-solid fa-baby"></i>
      </a>
      <div class="text-block">
        APA 1/2<br>
        <code>pex_bm_apa</code>
      </div>
    </div>
  </td>
  <td>Added summary scores and corresponding T-scores, where appropriate, for Level 2 domains.</td>
</tr>
<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#pex" target="_blank">
        <i class="fa-solid fa-baby"></i>
      </a>
      <div class="text-block">
        EPDS<br>
        <code>pex_bm_epds</code>
      </div>
    </div>
  </td>
  <td style="word-wrap: break-word; white-space: normal;">Removed duplicate data for each item (e.g., <code>epds_001</code> and <code>epds_001_01</code>).</td>
</tr>

<tr>
  <td rowspan="2">
    <div class="icon-text-block">
      <a href="../../instruments/#pex" target="_blank">
        <i class="fa-solid fa-baby"></i>
      </a>
      <div class="text-block">
        TLFB<br>
        <code>pex_ch_tlfb</code>
      </div>
    </div>
  </td>
  <td style="word-wrap: break-word; white-space: normal;">Corrected logic for TLFB substance use flags. Previously, only the alcohol use flag applied the intended criteria (use during or after pregnancy across V01–V02).</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Removed age variable fields (<i>gestational_age</i>, <i>adjusted_age</i>, and <i>candidate_age</i>) due to incorrect values.</td>
</tr>
</tbody>
</table>
</div>

<div id="r1.1eeg" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Brain Activity & Biosensors</span>
  <a class="anchor-link" href="#r1.1eeg" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead>
  <tr>
    <th>Table/Data</th>
    <th>Resolved Known Issue</th>
  </tr>
</thead>
<tbody>
<!-- EEG -->
<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#eeg" target="_blank">
        <i class="fa fa-bolt"></i>
      </a>
      <div class="text-block">
        HBCD-MADE Derivatives
      </div>
    </div>
  </td>
  <td style="word-wrap: break-word; white-space: normal;">Removed erroneous resting-state summary files (<code>*_task-RS_powerSummaryStats.csv</code>) due to a pipeline bug. Users can generate these summary statistics with <a href="https://hbcd-eeg-utilities.readthedocs.io/en/stable/">HBCD EEG Utilities</a>.</td>
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
  <th>Instrument(s)</th>
  <th>Table Name(s)</th>
</thead>
<tbody>
<tr><td>Biosensor Receipt Form</td><td><code>sens_ch_rcpt</code></td></tr>
<tr><td>EEG Acquisition Checklists</td><td><code>eeg_ch_chkl</code> / <code>eeg_ch_chkl_&lt;1|2&gt;</code></td></tr>
<tr><td>ERICA forms</td><td><code>mh_cg_erica_&lt;3_7m|7_9m&gt;</code> / <code>mh_cg_erica_fcm_adm_&lt;3_7m|7_9m&gt;</code></td></tr>
<tr><td>GABI Setup/Receipt</td><td><code>nt_pa_gabi_setup</code> / <code>nt_pa_gabi_rcpt</code></td></tr>
<tr><td>MRI Checklists & Pre/Post Scan Prep</td><td><code>mri_ra_chkl_data</code> / <code>mri_ra_chkl_scan</code> / <code>mri_ra_prep</code></td></tr>
<tr><td>NIH Baby ToolBox</td><td><code>ncl_ch_nbtb</code></td></tr>
<tr><td>Participant / RA Feedback</td><td><code>adm_cg_fb</code> / <code>adm_ra_fb</code></td></tr>
<tr><td>Transitions in Care Questionnaire</td><td><code>sed_cg_tic</code></td></tr>
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

<br>


