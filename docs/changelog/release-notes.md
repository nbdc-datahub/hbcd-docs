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

### Participant Population

HBCD enrolls at least 25% of participants with more than minimal substance use during pregnancy, including opioids ([Si et al. 2024](https://doi.org/10.1016/j.dcn.2024.101432)). Enrollment strategies aim to yield a study population representative of individual and geographic characteristics of pregnant and postpartum individuals (18 years or older) in the U.S., including an adequate comparison group for substance-exposed individuals ([Nelson et al. 2024](https://doi.org/10.1016/j.dcn.2024.101441)). 

<!-- There are siblings enrolled in HBCD, some of whom are twins or triplets (multiples). IDs for multiples are provided in the *HBCD Private Release Notes* - see <a href="../../instruments/demo/visitinfo/#multiple-birth-participants" target="_blank">Multiple Birth Participants</a> under Visit Information for details. -->


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


[Go to full list of instruments organized by domain →](../instruments/index.md#instruments-by-domain)

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




### 2.0 INFO - New Cohorts & Instruments

A number of new instruments were incorporated into R2.0 as well. Click to expand infobox below to view the full list.  

<div id="2.0-new-tables" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-table"></i></span>
  <span class="text-with-link">
  <span class="text">+ 40 New Instruments Across 10 Domains</span>
  <a class="anchor-link" href="#2.0-new-tables" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
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
<td><a href="../../instruments/#adm" target="_blank"> Administrative</a></td>
<td><span class="tooltip"><i class="fas fa-layer-group header-icon"></i><span class="tooltiptext">Concatenated data</span></span> Study Navigator Contact Form </td>
  <td>Recruitment/Retention</td>
</tr>
<tr>
<td rowspan="7"><a href="../../instruments/#mh" target="_blank"> Behavior & Caregiver-Child Interaction</a></td>
<td>CHAOS</td><td>Family Organization</td>
</tr>
<tr><td>ecPROMIS CH-CG Relationship <b>[1-5 year]</b></td><td>Child-Caregiver Interaction</td></tr>
<tr><td>ecPROMIS Peer Relationships</td><td>Peer Relationships</td></tr>
<tr><td>ecPROMIS Self-Regulation</td><td>Self-Regulation and Flexibility</td></tr>
<tr><td>FAD (GF6+)</td><td>Global Functioning of Family Unit</td></tr>
<tr><td>ECBQ (VSF)+BI</td><td>Early Childhood Behavior + Inhibition</td></tr>
<tr><td>MAPS-TL <b>[Toddlerhood & Preschool]</td> <td>Irritability</td></tr>
<tr>
<td><a href="../../instruments/#biospec" target="_blank">Biospecimen & Omics</a></td>
<td><span class="tooltip"><i class="fas fa-layer-group header-icon"></i><span class="tooltiptext">Concatenated data</span></span> Illumina GDA GWAS</td>
<td>GWAS, EWAS, Transcriptome</td>
</tr>
<tr><td rowspan="4"><a href="../../instruments/#ncl" target="_blank">Neurocognition & Language</a></td>
<td>Bayley-4 Scales</td><td>Child Development (Cognitive, Language, Motor)</td>
</tr>
<tr><td>MacArthur-Bates CDI-I</td><td>Language Development (Words & Gestures)</td></tr>
<tr><td>SPM-2 <b>[Toddler]</b></td>  <td>Sensory Processing/Integration</td></tr>
<tr><td>Vineland Adaptive Behavior</td><td>Adaptive Behavior</td></tr>
<tr><td rowspan="7"><a href="../../instruments/#ph" target="_blank"> Physical Health</a></td>
<td>Brief Infant Sleep Questionnaire</td><td>Sleep</td>
</tr>
<tr><td>ecPROMIS Physical Activity/Greenspace</td> <td>Physical Activity</td></tr>
<tr><td>ecPROMIS Sleep</td> <td>Sleep</td></tr>
<tr><td>Medical History</td><td>Medical History</td></tr>
<tr><td>Infant Nutrition Questionnaire</td><td>Nutrition</td></tr>
<tr><td>Screen-Based Media Use (<i>ScreenQ</i>)</td><td>Media Use</td></tr>
<tr><td>Vision Screener</td><td>Vision</td></tr>
<tr><td rowspan="2"><a href="../../instruments/#pex" target="_blank"> Pregnancy & Exposure</a></td>
<td>ASSIST <b>[V4]</b></td>  <td>Substance Use Post-Pregnancy</td></tr>
<tr><td>Substance Use Patterns</td>  <td>Substance Use in Pregnancy</td></tr>
<tr><td rowspan="12"><a href="../../instruments/#sed" target="_blank"> Social & Environment</a></td>
<td><span class="tooltip"><i class="fas fa-layer-group header-icon"></i><span class="tooltiptext">Concatenated data</span></span> Geocoded Linkage</td>  <td>Neighborhood Measures</td></tr>
<tr><td>ACEs</td>  <td>Adverse Childhood Experiences</td></tr>
<tr><td>Child Demographics</td><td>Demographics</td></tr>
<tr><td>Composite Abuse Scale (CABr-SF)</td>  <td>Intimate Partner Violence</td></tr>
<tr><td>Current Employment</td><td>Current Employment</td></tr>  
<tr><td>HOME-21 IT</td><td>Child’s Home Environment</td></tr>  
<tr><td>Household Chemical Exposures</td> <td>Household Chemical Exposures</td></tr>  
<tr><td>Lead Exposures</td><td>Lead Exposures</td></tr> 
<tr><td>PACES <b>[&lt;18]</b></td><td>Protective Factors</td></tr>  
<tr><td>Second Hand Smoke Exposure</td> <td>Second Hand Smoke Exposure</td></tr>
<tr><td>Transition in Care Screener</td><td>Recruitment/Retention</td></tr>
<tr><td>Vancouver Index of Acculturation (VIA)</td><td>Acculturation</td></tr> 
<td rowspan="2"><a href="../../instruments/#eeg" target="_blank"> EEG</a></td>
<td>EEG Acquisition Checklist + Reattempt 1/2</td><td>Acquisition Checklists</td></tr>
<tr><td>ERP SummaryStats</td><td>Tabulated HBCD-MADE derivatives</td></tr>
<tr>
<td><a href="../../instruments/#mri" target="_blank"> MRI</a></td>
<td>Pre-Scan Questionnaire</td><td>Infant Sleep Environment</td>
</tr>
<tr>
<td><a href="../../instruments/#sensors" target="_blank"> Novel Tech & Wearables</a></td>
<td>Biosensor Receipt & Setup</td><td>Administrative</td></tr>
</tr>
</tbody>
</table>
</div>

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