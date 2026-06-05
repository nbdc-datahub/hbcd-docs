<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
</style>

# Release Notes & History

## Release 2.1

<div class="release-banner">
  <span class="release-text">
    <i class="fa-solid fa-calendar release-icon"></i>
    Release Date: 2026-06-01 <span style="color: red;">(UPDATE)</span>
  </span>
</div>

<div class="stats-grid">
  <div class="card">
    <h3>Participants</h3>
    <div class="metric">
      3,605
    </div>
  </div>
  <div class="card">
    <h3>Total Visits</h3>
    <div class="metric">
      8,415
    </div>
    <div class="detail">
      V01: 3,545 | V02: 2,310 | V03: 1,398<br>
      V04: 679 | V05: 483
    </div>
  </div>
  <div class="card">
    <h3>By Sex</h3>
    <div class="metric-sub">
      1,175 Unknown <span class="muted">[V01]</span>
    </div>
    <div class="metric-sub">
      1,159 F | 1,271 M <span class="muted">[V02+]</span>
    </div>
  </div>
</div>

### 2.1 Key Changes

<!-- 
2.0 INFO:

<ul>
<li>New participant cohorts included: multiple birth participants and postnatal recruits (PNR)</li>
<li>+40 new instruments across 10 domains</li>
<li>Expanded MRI & EEG data (processed derivatives for more participants, no QC restriction on raw BIDS)</li>
<li>Major data fixes and harmonization updates across multiple domains</li>
</ul> -->

### 2.1 Inclusion & Exclusion Criteria

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
<li>Only selected 'Multiple Birth' profiles are included (based on clean-up procedures)</li>
<li>Only selected 'Postnatal Recruitment' profiles are included (based on clean-up procedures)</li>
<li>No sites excluded as of 2.0 </li>
<li>Participant exclusion if 'Brain Rating' is 'Abnormal'</li>
<li>Participant excluded due to 'Examiner' not 'REDCap' on REDCap surveys (possible modification of data between REDCap and LORIS, or data entered directly into LORIS) </li>
</ul>
  </td>
</tr>
<tr>
  <td><b>Visits</b></td>
  <td>
   <ul>
    <li>Only data from visits whose status is set to ‘LaunchPad Complete’ up to '2025-07-01' for 2.0 release and '2026-07-01' for 3.0 release (YYYY-MM-DD)</li>
    <li>Forced insertion/exclusion of participants (based on 'LaunchPad Complete' date after July 1, 2024 exceptions granted for 1.0 release only)</li>
    </ul>
  </td>
</tr>
<tr>
<td><b>Instruments</b></td>
<td>
    <ul>
    <li>GABI Setup/Receipt — <code>nt_pa_gabi_{setup|rcpt}</code></li>
    <li>NIH Baby Toolbox — <code>ncl_ch_nbtb</code></li>
    <li>Participant & RA Feedback — <code>adm_cg_fb</code> / <code>adm_ra_fb</code></li>
    <li>Urgent Events &amp; Participant Alerts — <code>adm_fd_urgent</code> / <code>admin_alert</code></li>
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

<!-- OLD NOTES for 2.0 prior to updates from Santiago - Instrument & Field Exclusions - 

- Fields including *examiner*, *REDCap Complete status*, *timestamps*, *visit stage*, and *visit start* -->

### 2.1 New Instruments

Release data now include the addition of the following instruments:

<table class="table-no-vertical-lines">
<thead>
<tr>
<th>Domain</th>
<th>Instrument</th>
<th>Construct</th>
</tr>
</thead>
<tbody>

<tr>
<td>Behavior & Caregiver-Child Interaction</td>
<td>ERICA (<code>mh_cg_erica{_rel}_3_9m</code>; raw scores only)</td>
<td>Emotional Regulation</td>
</tr>

<tr>
<td>Biospecimen & Omics</td>
<td>Olink Explore 384 Inflammation 1 Panel</td>
<td>Maternal Inflammation</td>
</tr>

<tr>
<td rowspan="2">Tabulated Imaging</td>
<td>MRI Data Summary Form</a></td>
<td>Pre-/Post-MRI Tech Checklist 2</td>
</tr>
<tr>
<td>MRI Scan Session Summary Form</td>
<td>Pre-/Post-MRI Tech Checklist 1</td>
</tr>

</tbody>
</table>

<a href="../../instruments/" class="button-link"> All instruments by domain →</a>

### 2.1 Resolved Known Issues & Updates

<p style="font-size: 1.1em; color: #555; text-align: center;">
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i> = Resolved Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Completed Pending Update</p>

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Topic</th>
<th>Summary</th>
</tr>
</thead>
<tbody>

<tr class="table-group-row">
  <td colspan="3">General</td>
</tr>

<tr>
<td>Language</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Added language of administration across all instruments where applicable</td>
</tr>

<tr class="table-group-row">
  <td colspan="3">Administrative</td>
</tr>
<tr>
<td>Study Navigators</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> SUBSTANCE_USE and OTHER checkbox fields populated</td>
</tr>

<tr class="table-group-row">
  <td colspan="3">Behavior & Caregiver-Child Interaction</td>
</tr>
<tr>
<td>ECBQ</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>  Coding for "Does not apply" changed to 8 to match the IBQ-R.</td>
</tr>

<tr class="table-group-row">
  <td colspan="3">Biospecimens & Omics</td>
</tr>

<tr>
<td>Nails</td>
<td><i class="fas fa-bug icon-bug"></i> Added unit (mg) for <code>nails_results_nail_weight</code> variable.</td>
</tr>
<tr>
<td>Nails &amp; Urine</td>
<td><i class="fas fa-bug icon-bug"></i> Removed quotes in data dictionary level values causing the downloaded to have double quotes, e.g. 1=""positive""</td>
</tr>
<tr>
<td>Urine</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Added creatinine results (<code>bio_creat_u</code>).</td>
</tr>

<tr class="table-group-row">
  <td colspan="3">Demographics</td>
</tr>
<tr>
<td>Basic Demo</td>
<td><i class="fas fa-bug icon-bug"></i> Removed internal data dictionary <code>recruitment_site</code> categories not present in data (<code>30-32</code>: Sampled, USDTL, and BAH)</td>
</tr>
<tr>
<td>Visit Inf</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Added a derived/rolled up substance use flag for Stimulants based on positive instrument-specific Stimulant results</td>
</tr>

<tr>
<td>Visit Info</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> SU flags now include Nail toxicology results in addition to Urine</td>
</tr>

<tr class="table-group-row">
  <td colspan="3">EEG & MRI</td>
</tr>

<tr>
<td>EEG .set files</td>
<td><i class="fas fa-bug icon-bug"></i> Updated .set files to include subject release IDs</td>
</tr>
<tr>
<td>HBCD-MADE (EEG)</td>
<td><i class="fas fa-bug icon-bug"></i> Added missing FACE/MMN tabulated data for N=3 V04 session derivatives</td>
</tr>

<tr>
<td>Raw BIDS (MRI)</td>
<td><i class="fas fa-bug icon-bug"></i> Corrected 2 corrupted bold runs in V02 raw BIDs</td>
</tr>

<tr>
<td>XCP-D</td>
<td><i class="fas fa-bug icon-bug"></i> Corrected <code>sub_domain</code> values in tabulated XCP-D Myers-Labonte metadata to <code>Structural MRI</code></td>
</tr>

<tr>
<td>BrainSwipes</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of complete BrainSwipes MRI QC results</td>
</tr>

<tr class="table-group-row">
  <td colspan="3">Neurocognition & Language</td>
</tr>
<tr>
<td>Vineland</td>
<td><i class="fas fa-bug icon-bug"></i> Corrected subset of variables with typo in the spelling of "receptive"</td>
</tr>
<tr>
<td>Bayley-4</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Added item-level scores</td>
</tr>
<tr>
<td>Vineland</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Added language field</td>
</tr>

<tr class="table-group-row">
  <td colspan="3">Physical Health</td>
</tr>
<tr>
<td>Growth</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Added age-based z-scores to <code>ph_ch_anthro</code></td>
</tr>
<tr>
<td>ecPROMIS-PAGS</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Added scores to <code>ph_cg_pms__pags</code></td>
</tr>

<tr class="table-group-row">
  <td colspan="3">Pregnancy & Environmental Exposure</td>
</tr>

<tr>
<td>APA 1/2</td>
<td><i class="fas fa-bug icon-bug"></i> APA Level 2 was sometimes administered despite unmet gating criteria (e.g., missing Level 1 responses). These cases were not scored (“No additional inquiry required”) even when Level 2 responses were present. Level 2 item data was removed to avoid confusion.</td>
</tr>

<tr class="table-group-row">
  <td colspan="3">Social & Environmental Determinants/td>
</tr>
<tr>
<td>C-PACEs</td>
<td><i class="fas fa-bug icon-bug"></i> Corrected summary scores</td>
</tr>

<tr>
<td>Demo (adult table)</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Added (1) V01 household income (<code>income_002</code>); (2) Other Biological Parent information variables; (3) <code>work_{002–004}_post</code> (worked for pay + for X hours while pregnant) and <code>work_004__01</code> (job held ≥1 month since V01)</td>
</tr>

<tr>
<td>Demo</td>
<td><i class="fas fa-bug icon-bug"></i> Re-addition of variables <code>sed_bm_demo_residence_{001|002}</code></td>
</tr>

<tr>
<td>eHITS</td>
<td><i class="fas fa-bug icon-bug"></i>Set values to null for participants missing all item responses that were incorrectly scored as <code>0</code></td>
</tr>

<!-- <tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Child Demo</td>
<td>see <a href="https://docs.hbcdstudy.org/latest/instruments/SED/demo-ch/#warning">Data Warning</a> ("Household Roster")</td>
</tr> -->

</tbody></table>


## Release History

Prior release notes are available via prior versions of this site as follows (also accessible via [flyout menu](../help/citation.md#view-archived-release-documentation)).

<table class="table-no-vertical-lines">
<thead>
<tr>
<th>Version</th>
<th>Release Date</th>
<th>Release Notes</th>
</tr>
</thead>
<tbody>

<tr>
<td><strong>2.0</strong></td>
<td>2026-02-11</td>
<td>
  <a href="https://docs.hbcdstudy.org/r2.0/changelog/release-notes/#release-20" target="_blank">
    View Release Notes
  </a>
</td>
</tr>

<tr>
<td><strong>1.1</strong></td>
<td>2025-10-10</td>
<td>
  <a href="https://docs.hbcdstudy.org/r1.1/changelog/releasenotes/#version-r11" target="_blank">
    View Release Notes
  </a>
</td>
</tr>

<tr>
<td><strong>1.0</strong></td>
<td>2025-06-26</td>
<td>
  <a href="https://docs.hbcdstudy.org/r1.0/changelog/versions/R1/" target="_blank">
    View Release Notes
  </a>
</td>
</tr>
</tbody>
</table>