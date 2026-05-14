# Pre-Scan Questionnaire & MRI Summary Forms

The following instruments are administered as part of MRI scan sessions for the child participant (V02 - V06):

<table class="table-no-vertical-lines">
<thead>
<tr>
<th>Instrument</th>
<th>Table Name</th>
<th>Construct</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#pre-scan-questionnaire">Pre-Scan Questionnaire</a></td>
<td><code>mri_ra_prep</code></td>
<td>Infant Sleep Environment</td>
</tr>
<tr>
<td><a href="#scan-session-form">MRI Scan Session Summary Form</a></td>
<td><code>mri_ra_chkl_scan</code></td>
<td>Pre-/Post-MRI Tech Checklist-1</td>
</tr>
<tr>
<td><a href="#data-form">MRI Data Summary Form</a></td>
<td><code>mri_ra_chkl_data</code></td>
<td>Pre-/Post-MRI Tech Checklist-2</td>
</tr>
</tbody>
</table>

## Pre-Scan Questionnaire

The Pre-Scan Questionnaire is completed by HBCD Study staff when planning MRI procedures. It captures caregiver-reported sleep routines, habits, and environment, administered remotely by HBCD Study staff. Quality control procedures include monitoring a data dashboard for missingness, coding errors, and data consistency. **Note that missingness may vary across sites.**

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
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Item</th>
<th width="40%">Item Text</th>
<th width="40%">Response Options</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>s1_bsi_002*</code></td>
<td>Which of the following are part of the child's typical sleep routine?</td>
<td><i>(Multi-select field)</i> Bottle feeding; Breast feeding; Bath; Reading; Other</td>
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
<td>Do you think skipping your child's nap prior to the visit would be helpful?</td>
<td>Yes; No</td>
</tr>
<tr>
<td><code>s1_slp_002</code></td>
<td>Length of bedtime routine</td>
<td>0–5, 5–10, 10–20, 20–30, 30–45, 45–60 min; 1+ hr; No routine</td>
</tr>
<tr>
<td><code>s1_slp_003</code></td>
<td>Length of nap routine</td>
<td>0–5, 5–10, 10–20, 20–30, 30–45, 45–60 min; 1+ hr; No routine</td>
</tr>
<tr>
<td><code>s1_slp_004</code></td>
<td>After you set the child to sleep, how long does it take for them to fall asleep?</td>
<td>0–5, 5–10, 10–20, 20–30, 30–45, 45–60 min; 1+ hr; No routine</td>
</tr>
<tr>
<td><code>s1_slp_005</code></td>
<td>Once asleep, how long does your child typically sleep?</td>
<td>0-30, 30-60 min; 1-2 hr; 2+ hrs</td>
</tr>
<tr>
<td><code>s1_slp_006</code></td>
<td>How consistent is your child's nap/sleep schedule?</td>
<td>Very; Somewhat; Not consistent; My child does not have a sleep schedule</td>
</tr>
<tr>
<td><code>s1_slp_007*</code></td>
<td>Which of the following would help your child sleep?</td>
<td><i>(Multi-select field)</i>
Playtime; Breast feeding; Bottle feeding; Eating/drinking something else</td>
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
<td>White noise; Sing lullabies; Listen to music</td>
</tr>
<tr>
<td><code>s1_sls_006*</code></td>
<td>Sleep aids</td>
<td>Stuffed toy; Pacifier; Weighted blanket; Other</td>
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

MRI summary forms are checklists completed by MRI technicians before and after each scan session. Quality control includes visual review to identify errors and missing data. Expand the sections below for an overview of the information included in each form.

<!-- LUCI NOTE: update QC procedures as needed once WG performs QC on data as available in Lasso BR -->

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
<th width="20%">Section</th>
<th>Details Collected</th>
</tr>
</thead>
<tbody>
<tr>
<td>Session Summary</td>
<td>Date of acquisition; candidate age (months); window difference (± days); adjusted chronological age (weeks)</td>
</tr>
<tr>
<td>Participant Info</td>
<td>Scheduled time of scan (24-hour); repeated visit indicator; family arrival time at scanning facility</td>
</tr>
<tr>
<td>Family Prep Pre-Visit</td>
<td>MRI sound exposure; sleep practice (back sleeping, lifting/moving while asleep); medications in past 24 hours (sleep aids, allergy medications, acetaminophen, ibuprofen, cough/cold medicine, antibiotics)</td>
</tr>
<tr>
<td>Travel to Visit</td>
<td>Transportation method; whether baby fell asleep in the car</td>
</tr>
<tr>
<td>Prep at Scan Site</td>
<td>Sleep location; room lighting; sounds played; feeding before scan; caregiver soothing methods; materials used during scan</td>
</tr>
<tr>
<td>Sleep Information</td>
<td>Time to fall asleep; time first asleep; initial sleep position</td>
</tr>
<tr>
<td>Transfer to Scanner</td>
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
<table class="table-no-vertical-lines">
<thead>
<tr>
<th width="20%">Section</th>
<th>Details Collected</th>
</tr>
</thead>
<tbody>
<tr>
<td>Scan Log</td>
<td>Scan start and interruption times, scan quality grade, FIRMM quality metrics (score, time, volumes), and images acquired</td>
</tr>
<tr>
<td>Summary</td>
<td>Reasons for incomplete/unsuccessful scan, whether each modality was acquired, and if the minimum threshold for low motion fMRI data (7 min 30 sec) was acquired</td>
</tr>
<tr>
<td>Post-Scan</td>
<td>Time of family departure</td>
</tr>
</tbody>
</table>
</div>