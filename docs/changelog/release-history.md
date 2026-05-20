<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
</style>   

# Release Notes History

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

<div id="1.1-main-updates" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-arrows-rotate"></i></span>
  <span class="text-with-link">
  <span class="text">1.1 Existing Study Data Updates</span>
  <a class="anchor-link" href="#1.1-main-updates" title="updatedfiles">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines"><tbody>
<tr><td colspan="2"><i class="fas fa-id-card header-icon"></i><b>Demographics</b><br><br>
Scoring for AOU and ACS ethno-racial fields included in the Basic Demographics (<code>sed_basic_demographics</code>) table were reviewed. The multiracial options for ACS–Child–Multi Race (<code>child_ethnoracial_acs_by_multi_race</code>) were merged into one due to limited granularity in the <em>child_race</em> field.</td></tr>
<tr><td colspan="2"><i class="fa fa-vial header-icon"></i> <b>Biospecimen & Omics</b><br><br>
Removed 'Specimen ID’ fields from both the Nails & Urine Biospecimen tables; removed time from dates in Nails Results.</td></tr>
<tr><td colspan="2"><i class="fa-solid fa-baby header-icon"></i> <b>Pregnancy Exposure, Including Substance Use</b><br><br>
Medications in Pregnancy & Infant Health instruments  (<code>pex_bm_health*</code>) are now categorized into more detailed components based on <strong>RxNorm IDs</strong> to improve clarity and enable more granular analyses. Additional columns specify: <em>Brand Name</em>, <em>Ingredient</em>, <em>Precise Ingredient</em>, and <em>Multiple Active Ingredients</em>.</td></tr>
<tr><td colspan="2"><i class="fas fa-city header-icon"></i> <b>Social & Environmental Determinants</b><br><br>
Added 'Birth parent sexual orientation' variable to V01 Demographics (<code>sed_bm_demo</code>).</td></tr>
<tr><td colspan="2"><i class="fa fa-brain header-icon"></i> <b>MRI</b><br><br>
Added BrainSwipes QC (<code>img_brainswipes*</code>) results missing from R1.0 (N=8).</td></tr>

<tr><td colspan="2"><b>Summary of Updated Files</b><br>
<i>Formats:</i> <code>.json | .parquet | .tsv</code>
<ul>
<li>Basic Demographics: <code>sed_basic_demographics</code></li>
<li>BioSpecimens: Nails and Urine -  <code>bio_bm_biosample_{nails|urine}_results</code> (+shadow matrix files)</li>
<li>SPM-2: <code>ncl_cg_spm2__inf</code> (+shadow matrix files)</li>
<li>TLFB: <code>pex_ch_tlfb</code> (+shadow matrix files)</li>
<li>PEX Health V2 Preg: <code>pex_bm_healthv2_preg</code> (.json only)</li></td></tr>
</tbody></table>
</div>

<div id="r1.1-resolved-issues" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">1.1 Resolved Known Issues</span>
  <a class="anchor-link" href="#r1.1-resolved-issues" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines">
<tbody>
<tr><td><strong>DEMOGRAPHICS</strong><br><br>
  <strong>Basic Demo</strong> (<code>sed_basic_demographics</code>)
    <ul>
    <li>Added missing income data for applicable participants.</li>
    <li>Mother Race (<code>screen_mother_race</code>): removed duplicate option (#3) for "Black African American".</li>
    <li>Removed gestational age and mother’s age at delivery for post–R1.0 deliveries that did not undergo QC.</li>
    <li>Mother Ethnicity (<code>screen_mother_ethnicity</code>): removed invalid levels (0, 1); retained valid values: 2 (Hispanic), 3 (Non-Hispanic).</li>
    <li>Mother Race &amp; Ethnicity (<code>rc_mother_ethnoracial_aou_race_ethnicity</code>): added missing response option "None of these fully describe me / Other".</li>
    </ul>
<strong>Visit Info</strong> (<code>par_visit_data</code>)
  <ul><li>Added missing <strong>substance use flags</strong> (alcohol, opioids, cannabis, nicotine)</li></ul></td>
</tr>

<tr><td><strong>BIOSPECIMENS</strong><br><br>
  <strong>Nails &amp; Urine</strong>
  <ul><li>Added collection and analysis dates (<em>Collection / Received / Report</em>)</li></ul>
  <strong>Urine</strong>
   <ul><li>Specific gravity correction (<code>bio_spg_u</code>) updated to floating-point values (previously set to '1' as data type 'integer').</li>
  <li>Cotinine (<code>bio_c_cot_u</code>): set all negative values (biologically implausible) to <code>0</code>. </li> 
  <li>Corrected negative gestational age values where needed (n=2 participants).</li></ul>
  </td>
</tr>

<tr><td><strong>EEG</strong>
  <ul><li>HBCD-MADE derivatives <code>*_task-RS_powerSummaryStats.csv</code> removed due to errors caused by pipeline bug.</li></ul></td>
</tr>
<tr><td><strong>NEUROCOGNITION & LANGUAGE</strong><br>
  <ul><li>SPM-2 (<code>ncl_cg_spm2__inf</code>): Added verified summary and T-scores (previously excluded due to conversion errors).</li></ul></td>
</tr>

<tr><td><strong>PREGNANCY & EXPOSURE</strong><br>
<ul>
<li>Health V2– Infancy (<code>pex_bm_healthv2_inf</code>): removed descriptive fields <code>001__00</code>–<code>005__00</code></li>
<li>APA 1/2 (<code>pex_bm_apa</code>): added summary and T-scores for Level 2 domains. </li>
<li>EPDS (<code>pex_bm_epds</code>): removed duplicate item fields (e.g., <code>epds_001</code> and <code>epds_001_01</code>).</li>
<li>TLFB (<code>pex_ch_tlfb</code>): updated substance use flag logic to apply intended criteria (use during or after pregnancy across V01–V02; only correct for alcohol before). Removed all age variables (<em>gestational/adjusted/candidate age</em>).</li>
</ul>
</td>
</tr>
</tbody>
</table>
</div>

---

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

<div id="r1-exclusions" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-filter"></i></span>
  <span class="text-with-link">
  <span class="text">R1.0 Exclusion Criteria & Filters</span>
  <a class="anchor-link" href="#r1-exclusions" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Excluded Participants &amp; Visit Data</strong></p>
<ul>
<li>Participants with no brain rating or brain rating noted as &quot;atypical&quot;</li>
<li>Postnatal Recruitment and Multiple Birth participants</li>
<li>Excluded visits with &#39;LaunchPad Complete&#39; Status set to &#39;Complete&#39; after 2024-07-01</li>
</ul>
<p><strong>Instrument &amp; Field Exclusions</strong></p>
<ul>
<li>Biosensor Receipt Form — <code>sens_ch_rcpt</code></li>
<li>EEG Acquisition Checklists — <code>eeg_ch_chkl</code> / <code>eeg_ch_chkl_&lt;1|2&gt;</code>    </li>
<li>ERICA forms — <code>mh_cg_erica_{3_7m|7_9m}</code> / <code>mh_cg_erica_fcm_adm_{3_7m|7_9m}</code>    </li>
<li>GABI Setup/Receipt — <code>nt_pa_gabi_setup</code> / <code>nt_pa_gabi_rcpt</code>    </li>
<li>MRI Checklists &amp; Pre/Post Scan Prep — <code>mri_ra_chkl_data</code> / <code>mri_ra_chkl_scan</code> / <code>mri_ra_prep</code>    </li>
<li>NIH Baby ToolBox — <code>ncl_ch_nbtb</code></li>
<li>Participant / RA Feedback — <code>adm_cg_fb</code> / <code>adm_ra_fb</code>    </li>
<li>Urgent Events &amp; Participant Alerts — <code>adm_fd_urgent</code> / <code>admin_alert</code></li>
<li>Visit Start / Visit Level Data — <code>visit_start</code> / <code>adm_fd_visitdata</code></li>
<li>Date of Administration — <code>date_taken</code>  </li>
<li>Examiner — <code>examiner</code>  </li>
<li>REDCap Complete status — <code>complete</code>  </li>
<li>Timestamps — <code>timestamp</code> / <code>timestamp_start</code> / <code>timestamp_stop</code> / <code>timestamp_redcap_locked</code>  </li>
<li>Visit Data — <code>visit_stage</code> removed from the <code>visit_data</code> category  </li>
<li>Breast Feeding History Fields — <code>ph_cg_phx_i_bfh</code> – All fields except <code>001</code> excluded  </li>
<li>Height/Weight/Head Circumference BMI — <code>ph_ch_anthro</code> – BMI-related fields removed  </li>
</ul>
</div>


