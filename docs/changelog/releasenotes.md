# Release Notes & History

## General Rules Applied to All Data

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
    <td><strong>Exclusions applied to all data</strong></td>
    <td>Inactive participants/sessions excluded</td>
</tr>
<tr>
  <td><strong>Field Conversions</strong></td>
  <td>• Empty fields are replaced with 'n/a'<br>
      • Sex is set to 'Other' for participants with only one active Visit 1 (V01) visit<br>
      • 'Candidate_Age' values are replaced with 'n/a' for Visit 1 (V01)
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

### <i class="fa-solid fa-arrows-rotate" style="margin-right: 8px;"></i> 1.1 Updates & Improvements to Existing Data

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 16px;">
  <tbody>
<tr><td colspan="2"><strong><i>Instrument/Measure (<code>Table Name</code>) Updates:</i></strong></td></tr>
    <!-- Basic Demographics -->
    <tr>
      <td style="width: 40px; text-align: center;">
        <a href="../../../instruments/#demo" title="Basic Demographics" target="_blank"><i class="fas fa-id-card"></i></a>
      </td>
      <td style="padding: 8px 4px; vertical-align: top; word-wrap: break-word; white-space: normal;">
        <strong>Basic Demographics</strong> 
        (<a href="../../instruments/demo/basicdemo" target="_blank"><code>sed_basic_demographics</code></a>)<br>
        <span class="update-text">Reviewed scoring for AOU and ACS EthnoRacial fields. The multiracial options for <strong>ACS – Child – Multi Race</strong> (<code>child_ethnoracial_acs_by_multi_race</code>) were merged into one due to limited granularity in the <em>child_race</em> field.
      </td>
    </tr>
    <!-- Biospec-->
    <tr style="border-bottom: 1px solid #e0e0e0;">
      <td style="width: 40px; text-align: center;">
        <a href="../../instruments/#biospec" title="Biospec" target="_blank"><i class="fas fa-vial"></i></a>
      </td>
      <td style="padding: 8px 4px; vertical-align: top;">
        <strong>Biospecimens Nails & Urine</strong> 
        (<code>bio_bm_biosample_*</code>)<br>
        <span class="update-text">Removed 'Specimen ID’ fields from all Biospecimen tables and time from dates in 'Nails Results.'</span>
      </td>
    </tr>
    <!-- BrainSwipes QC -->
    <tr style="border-bottom: 1px solid #e0e0e0;">
      <td style="width: 40px; text-align: center;">
        <a href="../../instruments/#mri" title="MRI Data" target="_blank"><i class="fas fa-magnet"></i></a>
      </td>
      <td style="padding: 8px 4px; vertical-align: top;">
        <strong>BrainSwipes QC</strong> 
        (<a href="../../instruments/mri/qc/#brainswipes" target="_blank"><code>img_brainswipes*</code></a>)<br>
        <span class="update-text">Added QC results missing from R1.0 (<strong>N=8</strong>).</span>
      </td>
    </tr>
    <!-- Pregnancy & Infant Health -->
    <tr style="border-bottom: 1px solid #e0e0e0;">
      <td style="width: 40px; text-align: center;">
        <a href="../../instruments/#pex" title="Pregnancy & Infant Health" target="_blank"><i class="fa-solid fa-baby"></i></a>
      </td>
      <td style="padding: 8px 4px; vertical-align: top; word-wrap: break-word; white-space: normal;">
        <strong>Pregnancy & Infant Health</strong> 
        (<a href="../../instruments/pregexp/pex" target="_blank"><code>pex_bm_health*</code></a>)<br>
        <span class="update-text">Medications are now categorized into more detailed components based on <strong>RxNorm IDs</strong> to improve clarity and enable more granular analyses.  
        Additional columns specify: <em>Brand Name</em>, <em>Ingredient</em>, <em>Precise Ingredient</em>, and <em>Multiple Active Ingredients</em>.</span>
      </td>
    </tr>
    <!-- V01 Demographics -->
    <tr style="border-bottom: 1px solid #e0e0e0;">
      <td style="width: 40px; text-align: center;">
        <a href="../../instruments/#socenvdet" title="Demographics" target="_blank"><i class="fas fa-city"></i></a>
      </td>
      <td style="padding: 8px 4px; vertical-align: top;">
        <strong>V01 Demographics</strong> 
        (<a href="../../instruments/SED/v01-demo" target="_blank"><code>sed_bm_demo</code></a>)<br>
        <span class="update-text">Added <strong>Birth Parent Sexual Orientation</strong> variable.</span>
      </td>
    </tr>
  </tbody>
</table>

<div id="updatedfiles" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-screwdriver-wrench"></i></span>
  <span class="text-with-link">
  <span class="text">Fill List of Updated Files</span>
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

### <i class="fa-solid fa-arrows-rotate" style="margin-right: 8px;"></i> 1.1 Resolved Known Issues By Domain

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
<strong>Basic Demographics (<code>sed_basic_demographics</code>)</strong>
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
<strong>Visit Information (<code>par_visit_data</code>)</strong>
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
<p style="font-size: 1.0em;"><strong>Urine (<code>bio_bm_biosample_urine</code>)</strong></p>
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
      <strong>Negative Gestational Ages</strong><br>
      The two participants with negative gestational ages in the urine biosample dataset (caused by inaccurate collection dates of the biosample) have been removed. - IS THIS RIGHT OR WERE THEY CORRECTED SOMEHOW?</td>
  </tr>  
</tbody>
</table>
</div>

<div id="r1.1eeg" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><a href="../../instruments/#eeg" target="_blank"><i class="fa fa-bolt"></i></a></span>
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
  <span class="emoji"><a href="../../instruments/#neurocog" target="_blank"><i class="fa fa-brain"></i></a></span>
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

<div id="participant-visits" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-filter"></i></span>
  <span class="text-with-link">
  <span class="text">Participant & Visit Exclusions</span>
  <a class="anchor-link" href="#participant-visits" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
  <td><strong>Excluded Participants</strong></td>
  <td> • Participants with no brain rating or brain rating noted as "atypical"<br>
       • Postnatal Recruitment participants<br>
       • Multiple Birth participants
  </td>
</tr>
<tr>
    <td><strong>Excluded Visit Data</strong></td>
    <td> • Visits with 'LaunchPad Complete' Status set to 'Complete' after 2024-07-01.</td>
</tr>
</tbody>
</table>
</div>

<div id="r1-exclusions" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-filter"></i></span>
  <span class="text-with-link">
  <span class="text">Instrument & Field Exclusions</span>
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
