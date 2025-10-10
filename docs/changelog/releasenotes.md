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


