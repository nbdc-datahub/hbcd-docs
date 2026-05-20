<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
</style>   

# 2.0 Release Notes 

<div style="background:#f2f6fc; padding:12px 20px; border-radius:10px; text-align:center; margin-bottom:25px; box-shadow:0 2px 4px rgba(0,0,0,0.05);">
  <span style="font-size:1.1em; font-weight:600; color:#2a5d9f;">
    <i class="fa-solid fa-calendar header-icon"></i>
    Release Date: 2026-02-11
  </span>
</div>
<div style="display:flex; flex-wrap:wrap; gap:20px; justify-content:center; margin:20px 0;">
<div class="card">
<h3>Participants</h3>
<p class="big">3,605</p>
</div>
<!-- Visits -->
<div class="card">
<h3>Total Visits</h3>
<p class="big">8,415</p>
<p class="small">
V01: 3,545 | V02: 2,310<br>
V03: 1,398 | V04: 679<br>
V05: 483</p>
</div>
<!-- By Sex -->
<div class="card">
<h3>By Sex</h3>
<p class="small">
  <i>V02+ visits:</i><br>
  <span class="big" style="font-size:1.2em;">1,159 (F) | 1,271 (M)</span><br><br>
  <i>V01 only:</i><br>
  <span class="big" style="font-size:1.2em;">1,175 (Unknown)</span>
</p>
</div>
</div>

## Key Changes in 2.0

<ul>
<li><b>+40 new instruments across 10 domains</b></li>
<li><b>New cohorts: multiple birth participants and postnatal recruits (PNR)</b></li>
<li><b>Expanded MRI & EEG data (processed derivatives for more participants, no QC restriction on raw BIDS)</b></li>
<li><b>Major data fixes and harmonization updates across multiple domains</b></li>
</ul>

## Participant Population

HBCD enrolls at least 25% of participants with more than minimal substance use during pregnancy, including opioids ([Si et al. 2024](https://doi.org/10.1016/j.dcn.2024.101432)). Enrollment strategies aim to yield a study population representative of individual and geographic characteristics of pregnant and postpartum individuals (18 years or older) in the U.S., including an adequate comparison group for substance-exposed individuals ([Nelson et al. 2024](https://doi.org/10.1016/j.dcn.2024.101441)). 

## Inclusion & Exclusion Criteria

<table class="table-no-vertical-lines">
<thead>
<tr>
  <th>Category</th>
  <th>Criteria / Rules</th>
</tr>
</thead>
<tbody>
<tr>
  <td><b>Participants</b></td>
  <td>
    • Exclude participants with missing or "atypical" brain ratings<br>
    • Exclude inactive participants/sessions
  </td>
</tr>
<tr>
  <td><b>Visits</b></td>
  <td>
    • Exclude visits collected after the January 2026 data freeze
  </td>
</tr>
<tr>
  <td><b>Data Handling Rules</b></td>
  <td>
    • Sex is set to 'Other' for participants with only one active V01 visit<br>
    • Candidate age is set to 'n/a' for V01
  </td>
</tr>
<tr>
  <td><b>Excluded Instruments/Fields</b></td>
  <td>
    • ERICA — <code>mh_cg_erica_{fcm_adm_}{3_7m|7_9m}</code><br>
    • GABI Setup/Receipt — <code>nt_pa_gabi_{setup|rcpt}</code><br>
    • MRI Data & Scan Summary — <code>mri_ra_chkl_{data|scan}</code><br>
    • NIH Baby Toolbox — <code>ncl_ch_nbtb</code><br>
    • Participant & RA Feedback — <code>adm_cg_fb</code> / <code>adm_ra_fb</code><br>
    • Urgent Events & Participant Alerts — <code>adm_fd_urgent</code> / <code>admin_alert</code><br>
    • General excluded fields: examiner, REDCap complete status, timestamps, visit stage/start
  </td>
</tr>
  </tbody>
</table>

## New Cohorts & Instruments

Release data now include **multiple birth participants** (multiple participants from the same birth, e.g. twins) and **postnatal recruits (PNR)** who joined the study after the child is born (complete a modified V01 and V02). Participant IDs for multiples and PNR are provided in the *HBCD Private Release Notes* - see <a href="../../instruments/demo/visitinfo/#multiple-birth-participants" target="_blank">Multiple Birth Participants</a> under Visit Information for details.

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

## MRI & EEG Updates   

<ul>
<li>Raw BIDS data now includes all available data, not restricted to data that only passed raw data quality control.</li>
<li>Raw and processed data included for additional participants and visits.</li>
<li>MRI scanner details now included in the session-level Scans TSV files, including: <code>ScannerManufacturer</code>, <code>ScannerModel</code>, <code>ScannerSoftwareVersion</code>, and <code>ScannerSerialNumber</code>.</li>
<li>New procedures were implemented to remove processed MRI derivatives with serious data quality issues (<a href="../../instruments/mri/#processed-derivatives">see details</a>).</li>
</ul>

## Resolved Known Issues

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
<!-- 
<div id="r2.0res-KI" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">10+ Resolved Known Issues</span>
  <a class="anchor-link" href="#r2.0res-KI" title="Copy link">
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
</div> -->
