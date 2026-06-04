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

### Key Changes in 2.1

<!-- 
2.0 INFO:

<ul>
<li>New participant cohorts included: multiple birth participants and postnatal recruits (PNR)</li>
<li>+40 new instruments across 10 domains</li>
<li>Expanded MRI & EEG data (processed derivatives for more participants, no QC restriction on raw BIDS)</li>
<li>Major data fixes and harmonization updates across multiple domains</li>
</ul> -->

### Inclusion & Exclusion Criteria

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

### New Instruments

Release data now include the addition of the following new instruments:

[Go to full list of instruments organized by domain →](../instruments/instruments.md)

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
<td>ERICA</td>
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

### 2.0 INFO - MRI & EEG Updates   

<ul>
<li>Raw BIDS data now includes all available data, not restricted to data that only passed raw data quality control.</li>
<li>Raw and processed data included for additional participants and visits.</li>
<li>MRI scanner details now included in the session-level Scans TSV files, including: <code>ScannerManufacturer</code>, <code>ScannerModel</code>, <code>ScannerSoftwareVersion</code>, and <code>ScannerSerialNumber</code>.</li>
<li>New procedures were implemented to remove processed MRI data with serious data quality issues (<a href="../../instruments/mri/#processed-derivatives">see details</a>).</li>
</ul>

### 2.0 INFO - Resolved Known Issues

<table class="table-no-vertical-lines">
<thead>
<tr>
<th>Domain</th>
<th>Updates</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>General</b></td>
<td>• Standardized Parquet precision by regenerating all data in a single step (<code>type_data</code> = <i>double</i>)</td>
</tr>
<tr>
<td><b>Demographics</b></td>
<td>
<b>Basic Demographics (<code>sed_basic_demographics</code>)</b><br>
• Removed invalid <code>screen_mother_race</code> response option (2 = <i>Hawaiian</i>)<br>
• Removed ACS Child Multi-Race (duplicate coding to <code>child_ethnoracial_acs_by_multi_ethnicity</code>)<br>
• Removed Child Multi-Ethnicity V01 data<br><br>
<b>Visit Data (<code>par_visit_data</code>)</b><br>
• Set withdrawal dates for participants who did not withdraw to null (from 12/26/1999)<br>
• Removed V02 urine toxicology substance use flags (urine not collected at V02)<br>
• Corrected TLFB substance use flags for missing V02 visits ('no' → null)
</td>
</tr>
<tr>
<td><b>Biospecimen &amp; Omics</b></td>
<td>
<b>Urine Toxicology</b><br>
• Restored missing values for cotinine (<code>*_results_bio_c_cot_u</code>) incorrectly set to 0 (N = 18)
</td>
</tr>
<tr>
<td><b>Neurocognition &amp; Language</b></td>
<td>
<b>SPM-2 (<code>ncl_cg_spm2__inf</code>)</b><br>
• Added age fields (gestational, adjusted, candidate)<br>
• Added missing status scores
</td>
</tr>
<tr>
<td><b>Pregnancy &amp; Exposure</b></td>
<td>
<b>APA 1/2 (<code>pex_bm_apa_anger_*</code>)</b><br>
• Added missing T-scores and total scores for Anger subscale<br><br>
<b>TLFB (<code>pex_ch_tlfb</code>)</b><br>
• Added age variables (gestational / adjusted / candidate age)
</td>
</tr>
<tr>
<td><b>Social &amp; Environmental</b></td>
<td>
<b>eHITS (<code>sed_bm_ehits</code>)</b><br>
• Corrected score calculations (<code>score</code>, <code>total_score</code>)
</td>
</tr>
</tbody>
</table>

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