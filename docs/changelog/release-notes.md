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

Release data now include the addition of the following instruments:

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

### 2.1 Resolved Known Issues & Updates

<p style="font-size: 1.1em; color: #555; text-align: center;">
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i> = Resolved Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Completed Pending Update</p>

##### General
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th>
<th>Topic</th>
<th>Summary</th>
</tr>
</thead>
<tbody>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Language</td>
<td>Added language of administration across all instruments where applicable</td>
</tr>

</tbody>
</table>

##### Administrative
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th>
<th>Table</th>
<th>Summary</th>
</tr>
</thead>
<tbody>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Study Navigators</td>
<td>SUBSTANCE_USE and OTHER checkbox fields populated</td>
</tr>

</tbody>
</table>


##### Behavior & Caregiver-Child Interaction
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th>
<th>Table</th>
<th>Summary</th>
</tr>
</thead>
<tbody>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ECBQ</td>
<td>Coding for "Does not apply" changed to 8 to match the IBQ-R.</td>
</tr>

</tbody>
</table>

##### Biospecimens & Omics

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
</tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Nails</td>
<td>Added unit (mg) for <code>nails_results_nail_weight</code> variable.</td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Nails &amp; Urine</td>
<td>Removed quotes in data dictionary level values causing the downloaded to have double quotes, e.g. 1=""positive""</td>
</tr>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Urine</td>
<td>Added creatinine results (<code>bio_creat_u</code>).</td>
</tr>
</tbody></table>

##### Demographics

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th>
<th>Summary</th>
</tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Basic Demo</td>
<td>Removed internal data dictionary <code>recruitment_site</code> categories not present in data (<code>30-32</code>: Sampled, USDTL, and BAH)</td>
</tr>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Visit Inf</td>
<td>Added a derived/rolled up substance use flag for Stimulants based on positive instrument-specific Stimulant results</td>
</tr>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Visit Info</td>
<td>SU flags now include Nail toxicology results in addition to Urine</td>
</tr>
</tbody></table>


##### EEG

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table</th>
<th>Summary</th>
</tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>.set files</td>
<td>Updated .set files to include subject release IDs</td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>MADE</td>
<td>Added missing FACE/MMN tabulated data for N=3 V04 session derivatives</td>
</tr>
</tbody></table>

##### MRI

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
</tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Raw BIDS</td>
<td>Corrected 2 corrupted bold runs in V02 raw BIDs</td>
</tr>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>XCP-D</td>
<td>Corrected tabulated XCP-D Myers-Labonte tables (<code>img_xcpd_hash-{X}_space-fsLR_seg-MyersLabonte_stat-mean_desc-_morph</code>) metadata to have a <code>sub_domain</code> value of <code>Structural MRI</code></td>
</tr>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>BrainSwipes</td>
<td>Addition of complete BrainSwipes QC results</td>
</tr>

</tbody></table>

##### Neurocognition & Language

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
</tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Vineland</td>
<td>Corrected subset of variables with typo in the spelling of "receptive"</td>
</tr>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Bayley-4</td>
<td>Added item-level scores</td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Vineland</td>
<td>Added language field</td>
</tr>
</tbody></table>


##### Physical Health

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
</tr>
</thead>
<tbody>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Growth</td>
<td>Added age-based z-scores to <code>ph_ch_anthro</code></td>
</tr>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ecPROMIS-PAGS</td>
<td>Added scores to <code>ph_cg_pms__pags</code></td>
</tr>

</tbody></table>

##### Pregnancy & Environmental Exposure

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
</tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>APA 1/2</td>
<td>APA Level 2 was sometimes administered despite unmet gating criteria (e.g., missing Level 1 responses). These cases were not scored (“No additional inquiry required”) even when Level 2 responses were present. Level 2 item data was removed to avoid confusion.</td>
</tr>

</tbody></table>


##### Social & Environmental Determinants

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
</tr>
</thead>
<tbody>


<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>C-PACEs</td>
<td>Corrected summary scores</td>
</tr>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Demo (adult table)</td>
<td>Added (1) V01 household income (<code>income_002</code>); (2) Other Biological Parent information variables; (3) <code>work_{002–004}_post</code> (worked for pay + for X hours while pregnant) and <code>work_004__01</code> (job held ≥1 month since V01)</td>
</tr>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Demo</td>
<td>Re-addition of variables <code>sed_bm_demo_residence_{001|002}</code></td>
</tr>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>eHITS</td>
<td>Set values to null for participants missing all item responses that were incorrectly scored as <code>0</code></td>
</tr>

<!-- <tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Child Demo</td>
<td>see <a href="https://docs.hbcdstudy.org/latest/instruments/SED/demo-ch/#warning">Data Warning</a> ("Household Roster")</td>
</tr> -->


</tbody></table>






<!-- #### ORIG COMBINED
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Domain</th>
<th>Table/Topic</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr>
<td><i>NA/General</i></td>
<td>Language</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Added language of administration across all instruments where applicable</td>
</tr>
<tr>
<td>ADM</td>
<td>Study Navigators</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> SUBSTANCE_USE and OTHER checkbox fields populated</td>
</tr>
<tr>
<td>MH</td>
<td>ECBQ</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Coding for "Does not apply" changed to 8 to match the IBQ-R.</td>
</tr>
</tbody>
</table> -->


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