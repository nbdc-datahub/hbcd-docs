<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
/* RELEASE DATE BANNER */
.release-banner {
  background: #f2f6fc;
  padding: 12px 20px;
  border-radius: 10px;
  text-align: center;
  margin-bottom: 25px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}
.release-banner .release-text {
  font-size: 1.1em;
  font-weight: 600;
  color: #2a5d9f;
}
.release-banner .release-icon {
  margin-right: 8px;
  vertical-align: 1px;
}

/* STATS GRID */
.stats-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin: 24px 0;
  align-items: stretch;
}
.card {
  flex: 1 1 260px;
  display: flex;
  flex-direction: column;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  padding: 22px;
  border-radius: 14px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.05);
  text-align: center;
}
.card h3 {
  margin: 0 0 18px 0;
  font-size: 0.95rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #6b7280;
}
.metric {
  font-size: 2.4rem;
  font-weight: 700;
  line-height: 1;
  color: #1d4f91;
  margin-bottom: auto;
}
.metric-sub {
  font-size: 1.15rem;
  font-weight: 600;
  color: #1d4f91;
  margin: 8px 0;
}
.detail {
  margin-top: 18px;

  font-size: 0.9rem;
  line-height: 1.5;

  color: #4b5563;
}
.muted {
  color: #6b7280;
  font-weight: 500;
}
</style>

# Release Notes & History

## Release 2.1

<div class="release-banner">
  <span class="release-text">
    <i class="fa-solid fa-calendar release-icon"></i>
    Release Date: 2026-08-14
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

<div id="data-warning" class="banner data-warning" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
<span class="text-with-link">
  <span class="text">Updates to data dictionary not yet incorporated into JSON metadata files</span>
  <a class="anchor-link" href="#data-warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content" style="background-color: #fcfaed;">
<p>For Release 2.1, updates were applied to the data dictionary information available via query tools within the NBDC Data Access Platform and DEAP. For users who download tabulated data in their original BIDS folder structure (e.g. via the "All Study Data" option), note that the metadata within these JSON files do not yet contain these updates. This is planned for a future release.</p>
<p>A detailed summary of differences between the online data dictionaries and JSON file data is available <a href="https://hbcd-docs-internal.readthedocs.io/latest/changelog/versions/BR2X/BR21.3/#data-dictionary-updates">here</a>.</p>
</div>

---

<p style="font-size: 1.1em; color: #555; text-align: center;">
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i> = Resolved Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Completed Pending Update</p>

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th style="width: 20%; white-space: nowrap;">Topic/Instrument</th>
<th>Summary of Changes</th>
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
<td><i class="fas fa-bug icon-bug"></i> Removed quotes in data dictionary level values causing double quotes in downloaded data, e.g. 1=""positive""</td>
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
<td><i class="fas fa-bug icon-bug"></i> Removed internal dictionary <code>recruitment_site</code> categories not present in data (<code>30-32</code>: Sampled, USDTL, and BAH)</td>
</tr>
<tr>
<td>Visit Info</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> New derived/rolled up substance use flag for Stimulants</td>
</tr>

<tr>
<td>Visit Info</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> SU flags now include Nail toxicology results in addition to Urine</td>
</tr>

<tr class="table-group-row">
  <td colspan="3">EEG</td>
</tr>
<tr>
<td>HBCD-MADE</td>
<td><i class="fas fa-bug icon-bug"></i> Added missing FACE/MMN tabulated data for N=3 V04 session derivatives</td>
</tr>
<tr>
<td>.set files</td>
<td><i class="fas fa-bug icon-bug"></i> Updated .set files to include subject release IDs</td>
</tr>


<tr class="table-group-row">
  <td colspan="3">MRI</td>
</tr>
<tr>
<td>Raw BIDS</td>
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
<td>SPM-2</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Added raw and T-scores</td>
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
<tr>
<td>ecPROMIS-Sleep</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Added <code>ph_cg_pms__sleep</code> summary scores</td>
</tr>

<tr class="table-group-row">
  <td colspan="3">Pregnancy & Environmental Exposure</td>
</tr>

<tr>
<td>APA 1/2</td>
<td><i class="fas fa-bug icon-bug"></i> Removed APA L2 item data in cases where L2 was administered despite unmet gating criteria (missing L1 responses and scoring)</td>
</tr>

<tr class="table-group-row">
  <td colspan="3">Social & Environmental Determinants/td>
</tr>
<tr>
<td>C-PACEs</td>
<td><i class="fas fa-bug icon-bug"></i> Corrected summary scores</td>
</tr>

<tr>
<td>Demographics (Adult)</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Added V01 household income (<code>income_002</code>)<br>
  <i class="fa-solid fa-rotate icon-rotate"></i> Added Other Biological Parent information variables<br>
  <i class="fa-solid fa-rotate icon-rotate"></i> Added <code>work_{002–004}_post</code> (worked for pay + for X hours while pregnant)<br>
  <i class="fa-solid fa-rotate icon-rotate"></i> Added <code>work_004__01</code> (job held ≥1 month since V01)<br>
  <i class="fa-solid fa-rotate icon-rotate"></i> Re-addition of variables <code>sed_bm_demo_residence_{001|002}</code>
  </td>
</tr>
</tbody></table>


### 2.1 Inclusion & Exclusion Criteria

##### Participants
- DCC participants excluded
- Only CH Profiles included — Exclusion by PSCID prefix (PI, QI, XI, YI)
- Only 'Active' participants included
- Only selected 'Multiple Birth' profiles are included (based on clean-up procedures)
- Only selected 'Postnatal Recruitment' profiles are included (based on clean-up procedures)
- No sites excluded as of 2.0
- Participant exclusion if 'Brain Rating' is 'Abnormal'
- Participant excluded due to 'Examiner' not 'REDCap' on REDCap surveys (possible modification of data between REDCap and LORIS, or data entered directly into LORIS)

##### Visits
- Only data from visits whose status is set to 'LaunchPad Complete' up to '2025-07-01' for 2.0 release and '2026-07-01' for 3.0 release (YYYY-MM-DD)
- Forced insertion/exclusion of participants (based on 'LaunchPad Complete' date after July 1, 2024 exceptions granted for 1.0 release only)

##### Instruments
- GABI Setup/Receipt — `nt_pa_gabi_{setup|rcpt}`
- NIH Baby Toolbox — `ncl_ch_nbtb`
- Participant & RA Feedback — `adm_cg_fb` / `adm_ra_fb`
- Urgent Events & Participant Alerts — `adm_fd_urgent` / `admin_alert`

##### Variables
- Informant (`informant`), Validity (`validity`), Duration (`duration`), and Window Difference (`window_difference`)
- Open text, descriptive, and line variables
- Impossible or selected Extreme/Outlier values filtered out
- Select Item/Score-level fields (hardcoded per instrument)

---

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
  <a href="https://docs.hbcdstudy.org/r2.0/changelog/release-notes/#release-20">
    View Release Notes
  </a>
</td>
</tr>

<tr>
<td><strong>1.1</strong></td>
<td>2025-10-10</td>
<td>
  <a href="https://docs.hbcdstudy.org/r1.1/changelog/releasenotes/#version-r11">
    View Release Notes
  </a>
</td>
</tr>

<tr>
<td><strong>1.0</strong></td>
<td>2025-06-26</td>
<td>
  <a href="https://docs.hbcdstudy.org/r1.0/changelog/versions/R1/">
    View Release Notes
  </a>
</td>
</tr>
</tbody>
</table>