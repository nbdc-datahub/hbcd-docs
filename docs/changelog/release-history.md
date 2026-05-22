<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
.meta-note {
  font-size: 0.9em;
  color: #5f6b7a;
  background: #f7f9fc;
  border-left: 4px solid #d6e2f5;
  padding: 8px 12px;
  margin: 10px 0 20px 0;
  border-radius: 6px;
  line-height: 1.4;
}
</style>   

# Release Notes History

## Release 1

<div class="stats-grid">
  <div class="card">
    <h3>Participants</h3>
    <div class="metric">
      1,426
    </div>
  </div>
  <div class="card">
    <h3>Total Visits</h3>
    <div class="metric">
      2,207
    </div>
    <div class="detail">
      V01: 1,426 | V02: 660 | V03: 121
    </div>
  </div>
  <div class="card">
    <h3>By Sex</h3>
    <div class="metric-sub">
      328 F · 338 M <span class="muted">[V02+]</span>
    </div>
  </div>
</div>

<div id="r1-filters" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-info-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Release 1 Inclusion & Exclusion Criteria</span>
  <a class="anchor-link" href="#r1-filters" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines" style="font-size: 16px;">
<thead>
<tr>
  <th colspan="2"><i>Items listed below are filtered/excluded from release data unless stated otherwise</i></th>
</tr>
</thead>
<tbody>
<tr>
<td><b>Participants</b></td>
<td>
<ul>
<li>DCC participants excluded</li>
<li>Only CH Profiles included - Exclusion by PSCID prefix (PI, QI, XI, YI)</li>
<li>Only 'Active' participants included</li>
<li>'Multiple Birth' and 'Postnatal Recruitment' participants excluded</li>
<li>Participant exclusion if 'Brain Rating' is 'Abnormal'</li>
<li>Participant excluded due to 'Examiner' not 'REDCap' on REDCap surveys (possible modification of data between REDCap and LORIS, or data entered directly into LORIS) </li>
</ul>
  </td>
</tr>
<tr>
  <td><b>Visits</b></td>
  <td>
   <ul>
   <li>Excluded visits with 'LaunchPad Complete' Status set to 'Complete' after 2024-07-01</li>
    <li>Forced insertion/exclusion of participants (based on 'LaunchPad Complete' date after July 1, 2024 exceptions granted for 1.0 release only)</li>
    </ul>
  </td>
</tr>
<tr>
<td><b>Instruments</b></td>
<td>
    <ul>
    <li>Biosensor Receipt Form — <code>sens_ch_rcpt</code></li>
    <li>EEG Acquisition Checklists — <code>eeg_ch_chkl</code> / <code>eeg_ch_chkl_&lt;1|2&gt;</code>    </li>
    <li>ERICA forms — <code>mh_cg_erica_{3_7m|7_9m}</code> / <code>mh_cg_erica_fcm_adm_{3_7m|7_9m}</code>    </li>
    <li>GABI Setup/Receipt — <code>nt_pa_gabi_setup</code> / <code>nt_pa_gabi_rcpt</code>    </li>
    <li>MRI Checklists &amp; Pre/Post Scan Prep — <code>mri_ra_chkl_data</code> / <code>mri_ra_chkl_scan</code> / <code>mri_ra_prep</code>    </li>
    <li>NIH Baby ToolBox — <code>ncl_ch_nbtb</code></li>
    <li>Participant / RA Feedback — <code>adm_cg_fb</code> / <code>adm_ra_fb</code>    </li>
    <li>Urgent Events & Participant Alerts — <code>adm_fd_urgent</code> / <code>admin_alert</code></li>
    <li>Visit Start / Visit Level Data — <code>visit_start</code> / <code>adm_fd_visitdata</code></li>
    </ul>
</td>
</tr>
<tr>
<td><b>Variables</b></td>
<td>
    <ul>
    <li>Informant (<code>informant</code>), Validity (<code>validity</code>), Duration (<code>duration</code>), and Window Difference (<code>window_difference</code>)</li>
    <li>Open text, descriptive, and line variables</li>
    <li>Impossible or selected Extreme/Outlier values filtered out</li>
    <li>Select Item/Score-level fields (hardcoded per instrument)</li>
    </ul>
</td>
</tr>
</tbody>
</table>
</div>

---

### Version R1.1 [Release Date: 2025-10-10]

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
<table class="table-no-vertical-lines">
<tbody>
<tr><td><strong>DEMOGRAPHICS</strong><br>
    <ul>
    <li>After review of scoring for AOU and ACS ethno-racial fields in Basic Demographics</strong> (<code>sed_basic_demographics</code>), the multiracial options for ACS–Child–Multi Race (<code>child_ethnoracial_acs_by_multi_race</code>) were merged into one due to limited granularity in the <em>child_race</em> field.</li>
    </ul></td>
</tr>
<tr><td><strong>BIOSPECIMENS</strong><br>
  <ul><li>Removed 'Specimen ID’ fields from both the Nails & Urine Biospecimen tables; removed time from dates in Nails Results.</li></ul>
  </td>
</tr>
<tr><td><strong>PREGNANCY & EXPOSURE</strong>
<ul>
<li>Medications in Pregnancy & Infant Health instruments  (<code>pex_bm_health*</code>) are now categorized into more detailed components based on <strong>RxNorm IDs</strong> to improve clarity and enable more granular analyses. Additional columns specify: <em>Brand Name</em>, <em>Ingredient</em>, <em>Precise Ingredient</em>, and <em>Multiple Active Ingredients</em></li>
</ul>
</td>
<tr><td><strong>SOCIAL & ENV DETERMINANTS</strong>
<ul><li>'Birth parent sexual orientation' variable added to V01 Demographics (<code>sed_bm_demo</code>).</li></ul>
</td></tr>
<tr><td><strong>MRI</strong>
<ul><li>BrainSwipes QC (<code>img_brainswipes*</code>) results missing from R1.0 (N=8) added.</li></ul>
</td></tr>
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
  <strong>Basic Demographics</strong> (<code>sed_basic_demographics</code>)
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

### Version R1.0 [Release Date: 2025-06-26]
