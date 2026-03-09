<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>

# Pre-Scan Questionnaire & Summary Forms

The following tables include the **Pre-Scan Questionnaire** with information collected about the child's sleep habits and environment as well as **MRI Summary Forms** with administrative information entered by the MRI technician on the day of the visit.

<table class="table-no-vertical-lines">
<thead>
<tr>
<th>Table</th>
<th>Construct</th>
<th>Table Name</th>
</tr>
</thead>
<tr>
<td><b>Pre-Scan Questionnaire</b></td>
<td>Infant Sleep Environment</td>
<td><code>mri_ra_prep</code></td>
</tr>
<tr>
<td><b>MRI Scan Session Summary Form</b> (<i>Pre/Post MRI Tech Checklist-1</i>)</td>
<td>Administrative Pre-/Post-MRI Tech Checklists</td>
<td><code>mri_ra_chkl_scan</code></td>
</tr>
<tr>
<td><b>MRI Data Summary Form</b> (<i>Pre/Post MRI Tech Checklist-2</i>)</td>
<td>Administrative Pre-/Post-MRI Tech Checklists</td>
<td><code>mri_ra_chkl_data</code></td>
</tr>
</tbody>
</table>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>Yes </td></tr>
<tr><td><b>Respondent</b></td>
<td>HBCD Study staff/Research Assistant or Primary Caregiver on Child <i>(entered by Research Assistant)</i></td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">HBCD Study staff <i>(administered remotely for Pre-Scan Questionnaire and in-person for MRI Summary Forms)</i></td></tr>
<tr><td><b>Visits</b></td>
<td>V02, V03</td></tr>
<tr><td><b>QC Procedures</b></td>
<td style="word-wrap: break-word; white-space: normal;">Monitor data dashboard for variable missingness, possible coding errors, scoring verification when needed, and data consistency.</td></tr>      
</tbody>
</table>

## Pre-Scan Questionnaire

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>There are missing data that is not equal across sites.</p> 
</div>

This instrument is completed by research assistants when planning for MRI strategies. It describes the caregiver reported sleep routines, habits, and environment. Expand the section below for a summary of key item questions and response options. 

<div id="items" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-circle-info"></i></span>
<span class="text-with-link">
  <span class="text">Pre-Scan Questionnaire Items Summary</span>
    <a class="anchor-link" href="#items" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p style="font-size: 1.0em; color: #555;">
<i class="fa fa-square-check" style="color: #00aeae;"></i>&nbsp;= Multi-select (Check all that apply)
</p>
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Item</th>
<th>Item Text</th>
<th>Response Options</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>s1_bsi_002*</code></td>
<td>Which of the following are part of the child's typical sleep routine? <i class="fa fa-square-check" style="color: #00aeae;"></i></td>
<td>Bottle feeding; Breast feeding; Bath; Reading; Other</td>
</tr>
<tr>
<td><code>s1_bsi_003*</code></td>
<td>Time child usually falls asleep at bedtime</td>
<td><i>NA (enter text)</i></td>
</tr>
<tr>
<td><code>s1_bsi_004*</code></td>
<td>Time child usually falls asleep for their longest nap</td>
<td><i>NA (enter text)</i></td>
</tr>
<tr>
<td><code>s1_slp_001</code></td>
<td style="word-wrap: break-word; white-space: normal;">Do you think skipping your child's nap prior to the visit would be helpful?</td>
<td>Yes; No</td>
</tr>
<tr>
<td><code>s1_slp_002</code></td>
<td>Length of bedtime routine</td>
<td style="word-wrap: break-word; white-space: normal;">0–5, 5–10, 10–20, 20–30, 30–45, 45–60 min; 1+ hr; No routine</td>
</tr>
<tr>
<td><code>s1_slp_003</code></td>
<td>Length of nap routine</td>
<td style="word-wrap: break-word; white-space: normal;">0–5, 5–10, 10–20, 20–30, 30–45, 45–60 min; 1+ hr; No routine</td>
</tr>
<tr>
<td><code>s1_slp_004</code></td>
<td>After you set the child to sleep, how long does it take for them to fall asleep?</td>
<td style="word-wrap: break-word; white-space: normal;">0–5, 5–10, 10–20, 20–30, 30–45, 45–60 min; 1+ hr; No routine</td>
</tr>
<tr>
<td><code>s1_slp_005</code></td>
<td>Once asleep, how long does your child typically sleep?</td>
<td style="word-wrap: break-word; white-space: normal;">0-30, 30-60 min; 1-2 hr; 2+ hrs</td>
</tr>
<tr>
<td><code>s1_slp_006</code></td>
<td>How consistent is your child's nap/sleep schedule?</td>
<td style="word-wrap: break-word; white-space: normal;">Very; Somewhat; Not consistent; My child does not have a sleep schedule</td>
</tr>
<tr>
<td><code>s1_slp_007*</code></td>
<td>Which of the following would help your child sleep? <i class="fa fa-square-check" style="color: #00aeae;"></i></td>
<td style="word-wrap: break-word; white-space: normal;">Playtime; Breast feeding; Bottle feeding; Eating/drinking something else</td>
</tr>
<tr>
<td><code>s1_sls_001*</code></td>
<td>Social</td>
<td>Alone; With mother; With sibling; Other</td>
</tr>
<tr>
<td><code>s1_sls_002*</code></td>
<td>Bed</td>
<td>Crib; Bassinet; Dock-a-tot; In bed; Other</td>
</tr>
<tr>
<td><code>s1_sls_003*</code></td>
<td>Lighting</td>
<td>Dimmed lights; Night light; Dark</td>
</tr>
<tr>
<td><code>s1_sls_004*</code></td>
<td>Noise level</td>
<td>Noisy; Moderate; Quiet</td>
</tr>
<tr>
<td><code>s1_sls_005*</code></td>
<td>Soothing sounds</td>
<td style="word-wrap: break-word; white-space: normal;">White noise; Sing lullabies; Listen to music</td>
</tr>
<tr>
<td><code>s1_sls_006*</code></td>
<td>Sleep aids</td>
<td style="word-wrap: break-word; white-space: normal;">Stuffed toy; Pacifier; Weighted blanket; Other</td>
</tr>
<tr>
<td><code>s1_sls_007</code></td>
<td>Comfort preference</td>
<td>Arms or legs {wrapped; free}</td>
</tr>
<tr>
<td><code>s1_sls_008*</code></td>
<td>Sleep position</td>
<td>Supine; Prone; Side</td>
</tr>
<tr>
<td><code>s1_soa_001</code></td>
<td>Child is curious when in a new setting</td>
<td>Always; Sometimes; Never</td>
</tr>
<tr>
<td><code>s1_soa_002</code></td>
<td>Child is comfortable sleeping in a new setting (ex. Vacation, relative's house)</td>
<td>Always; Sometimes; Never</td>
</tr>
<tr>
<td><code>s1_soa_003</code></td>
<td>Child is comfortable sleeping alone</td>
<td>Always; Sometimes; Never</td>
</tr>
<tr>
<td><code>s1_soa_004</code></td>
<td>Child wakes easily upon light or sound</td>
<td>Always; Sometimes; Never</td>
</tr>
<tr>
<td><code>s1_soa_005</code></td>
<td>Child fusses during his/her sleep time</td>
<td>Always; Sometimes; Never</td>
</tr>
<tr>
<td><code>s1_soa_006</code></td>
<td>Child easily opens up to new people</td>
<td>Always; Sometimes; Never</td>
</tr>
</tbody>
</table>
</div>

## MRI Scan Session & Data Summary Forms 

Click to expand the sections below for an overview of the information provided in the release from each of the MRI summary forms:

<div id="scan-session-form" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-circle-info"></i></span>
<span class="text-with-link">
  <span class="text">MRI Scan Session Summary Form</span>
    <a class="anchor-link" href="#scan-session-form" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Section</th>
<th>Details Collected</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Scan Session Summary</strong></td>
<td style="word-wrap: break-word; white-space: normal;">Date of acquisition; candidate age (months); window difference (± days); adjusted chronological age at administration (weeks)</td>
</tr>
<tr>
<td><strong>Participant Information</strong></td>
<td style="word-wrap: break-word; white-space: normal;">Scheduled time of scan (24-hour); repeated visit indicator; family arrival time at scanning facility</td>
</tr>
<tr>
<td><strong>Family Preparations Before Visit</strong></td>
<td style="word-wrap: break-word; white-space: normal;">MRI sound exposure; sleep practice (back sleeping, lifting/moving while asleep); medications in past 24 hours (sleep aids, allergy medications, acetaminophen, ibuprofen, cough/cold medicine, antibiotics)</td>
</tr>
<tr>
<td><strong>Travel to Visit</strong></td>
<td>Transportation method; whether baby fell asleep in the car</td>
</tr>
<tr>
<td><strong>Preparations at Scan Site</strong></td>
<td style="word-wrap: break-word; white-space: normal;">Sleep location; room lighting; sounds played; feeding before scan; caregiver soothing methods; materials used during scan</td>
</tr>
<tr>
<td><strong>Sleep Information</strong></td>
<td>Time to fall asleep; time first asleep; initial sleep position</td>
</tr>
<tr>
<td><strong>Transfer to Scanner</strong></td>
<td>Transfer method; whether child woke during transfer</td>
</tr>
</tbody>
</table>
</div>

<div id="data-form" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-circle-info"></i></span>
<span class="text-with-link">
  <span class="text">MRI Data Summary Form</span>
    <a class="anchor-link" href="#data-form" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Section</th>
<th>Details Collected</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Scan Log</strong></td>
<td style="word-wrap: break-word; white-space: normal;">Scan start and interruption times, scan quality grade, FIRMM quality metrics (score, time, volumes), and images acquired</td>
</tr>
<tr>
<td><strong>Summary</strong></td>
<td style="word-wrap: break-word; white-space: normal;">Reasons for incomplete/unsuccessful scan, whether each modality was acquired, and if the minimum threshold for low motion fMRI data (7 min 30 sec) was acquired</td>
</tr>
<tr>
<td><strong>Post-Scan</strong></td>
<td style="word-wrap: break-word; white-space: normal;">Time of family departure</td>
</tr>
</tbody>
</table>
</div>

