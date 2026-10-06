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



<div class="admin-note" markdown="1">
LUCI NOTES: 

- 3.0 release notes are under construction currently
-  update Release Date
</div>


## Release 3.0

<div class="release-banner">
  <span class="release-text">
    <i class="fa-solid fa-calendar release-icon"></i>
    Release Date: 2026-11-XX
  </span>
</div>

<div class="stats-grid">
  <div class="card">
    <h3>Participants</h3>
    <div class="metric">
      5,467
    </div>
  </div>
  <div class="card">
    <h3>Total Visits</h3>
    <div class="metric">
      16,853
    </div>
    <div class="detail">
      <b>V01</b>: 4,672  |   <b>V02</b>: 3,820
      <br>
      <b>V03</b>: 2,792 | <b>V04</b>: 1,909
      <br>
      <b>V05</b>: 1,784  |   <b>V06</b>: 686
      <br>
      <b>V07</b>: 587  |   <b>V07a</b>: 603
    </div>
  </div>
  <div class="card">
    <h3>By Sex</h3>
    <div class="metric-sub">
      848 Unknown <span class="muted">[V01]</span>
    </div>
    <div class="metric-sub">
      2,568 F | 2,051 M M <span class="muted">[V02+]</span>
    </div>
  </div>
</div>

### 3.0 New Domain: *Participant Derived*

The **Demographics** domain has been replaced with the domain **Participant Derived**. Through Release 2.1, the Demographics domain included two tables containing derived participant information, *Visit Info* (visit-specific information) and *Basic Demographics* (general participant information derived from SED Demographics and administrative records). For Release 3.0, the Demographics domain has been renamed **Participant Derived**, with information organized into static and dynamic tables:

- **Static Participant Information**: information that remains constant across visits, such as sex assigned at birth and race/ethnicity
- **Dynamic Participant Information**: information that may change over time and is therefore represented longitudinally


### 3.0 New Measures

Release data now include the addition of the following measures, expanded data types, versions, and/or visits:

<table class="table-no-vertical-lines">
<thead>
<tr>
<th width="35%">Domain</th>
<th>Measure</th>
</tr>
</thead>
<tbody>
</tr>
<tr>
<td rowspan="2">
<i class="fa fa-people-arrows table-icon-left"></i>
<a href="../../instruments/#behavior-caregiver-child-interaction">Behavior &amp; Child-Caregiver Interaction</a></td>
<td>MAPS-EASI- Toddler</td>
</tr>
<tr><td>Modified Checklist for Autism in Toddlers (MCHAT)</td></tr>

<tr>
<td>
<i class="fa fa-vial table-icon-left"></i>
<a href="../../instruments/#biospecimen-omics">Biospecimen & Omics</a></td>
<td>USDTL Blood Toxicology</td></tr>

<tr>
<td rowspan="3">
<i class="fa fa-brain table-icon-left"></i>
<a href="../../instruments/#imaging">Imaging</a></td>
<td>Addition of source DICOMs for all imaging modalities</td>
</tr>
<tr><td>Addition of <a href="https://modelarrayio.readthedocs.io/en/latest/">ModelArray</a> outputs for XCP-D for efficient voxel-wise statistical modeling.</td></tr>
<tr><td>Addition of tabulated pipeline derivatives for QSIRecon.</td></tr>

<tr>
<td rowspan="2">
<i class="fa-solid fa-puzzle-piece table-icon-left"></i>
<a href="../../instruments/#neurocognition-language">Neurocognition & Language</a></td>
<td>Deferred Imitation Task: Gong and Berry-Go-Round</td>
</tr>
<tr><td>MacArthur-Bates CDI-2 Language</td></tr>

<tr>
<td>
<i class="fa fa-microchip table-icon-left"></i>
<a href="../../instruments/#novel-technologies-wearable-sensors">Novel Technology & Wearable Sensors</a></td>
<td>GABI (infant heart rate) raw BIDS data</td>
</tr>

<tr>
<td rowspan="3">
<i class="fa fa-heart-pulse table-icon-left"></i>
<a href="../../instruments/#physical-health">Physical Health</a></td>
<td>Child Nutrition Questionnaire</td>
</tr>
<tr><td>PEDsQL</td></tr>
<tr><td>Med History V1 - addition of V06</td></tr>


<tr>
<td>
<i class="fas fa-city table-icon-left"></i>
<a href="../../instruments/#social-environmental-determinants">Social & Environmental Determinants</a></td>
<td>V6 Adult and V6 Child Demographics</td>
</tr>

</tbody>
</table>


### 3.0 Resolved Known Issues & Updates

<p style="font-size: 1.1em; color: #555; text-align: center;">
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i> = Resolved Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Completed Pending Update</p>

##### All Data / General

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th style="width: 20%; white-space: nowrap;">Topic</th>
<th>Summary of Changes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Incorrect JSONs</td>
<td><i class="fas fa-bug icon-bug"></i> Corrected JSON metadata (e.g. <code>type_data</code>) for several instruments (APA 1/2, Bayley-4, EEG Form-2, etc.).</td>
</tr>
<tr>
<td>Instruction</td>
<td><i class="fas fa-bug icon-bug"></i> Populated the previously blank instruction data dictionary element.</td>
</tr>
<tr>
<td>Blank Fields for Siblings</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Corrected family-level (i.e., non-child-specific) instrument fields so that they are now populated for sibling records, including HBCD Multiple Birth – Sibling records.</td>
</tr>
<tr>
<td>FamilyID</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Added FamilyID across tables to identify sibling relationships/enable mapping between Main Child and Sibling records.
</td>
</tr>
<tr>
<td>Sequence Field</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Removed the previously included Sequence field, which was blank across instruments.
</td>
</tr>
</tbody></table>

##### Behavior &amp; Child-Caregiver Interaction

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th style="width: 20%; white-space: nowrap;">Measure</th>
<th>Summary of Changes</th>
</tr>
</thead>
<tbody>
<tr>
<td>ecPROMIS CC</td>
<td><i class="fas fa-bug icon-bug"></i>
Corrected scoring for N=12 V03 participants with fewer than 3 item responses in <code>mh_cg_pms__cc__inf</code> (previously '0'; now 'null').
</td>
</tr>
<tr>
<td>FAD</td>
<td><i class="fas fa-bug icon-bug"></i>
Corrected scoring for N=4 V06 participants with fewer than 3 item responses (previously '0'; now 'null').
</td>
</tr>
<tr>
<td>MAPS-TL (&lt;1yr)</td>
<td><i class="fas fa-bug icon-bug"></i>
Corrected scoring for N=4 participants with no item responses (previously '0'; now 'null').
</td>
</tr>
<tr>
<td>MAPS-TL (Tod)</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>
Implemented pro-rated scoring for <code>mh_cg_mapdb__tod</code>, resolving missing scores for N=16 participants.</td>
</tr>
</tbody></table>

##### Biospecimens &amp; Omics

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th style="width: 20%; white-space: nowrap;">Measure</th>
<th>Summary of Changes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Nails</td>
<td><i class="fa-solid fa-bug icon-bug"></i>
Corrected nail type in main results table (<code>*_nails_results</code>) (formerly reported as 4 (Unknown)).
</td>
</tr>
</tbody></table>

##### EEG

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th style="width: 20%; white-space: nowrap;">Topic</th>
<th>Summary of Changes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Age fields</td>
<td><i class="fa-solid fa-bug icon-bug"></i>
Corrected chronological and adjusted age values for N=74 V03 sessions that fell outside the expected 3–9 month range due to site entry errors.
</td>
</tr>
<tr>
<td>MADE v1.7.0</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>
HBCD-MADE derivatives processed through updated version v1.7.0.</td>
</tr>
</tbody></table>

##### Imaging

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Topic</th>
<th>Summary of Changes</th>
</tr>
</thead>
<tbody>
<tr>
<td>dMRI metadata</td>
<td><i class="fa-solid fa-bug icon-bug"></i>
Corrected <code>LargeDelta</code> and <code>SmallDelta</code> in metadata to reflect accurate model-specific rather than vendor-specific values.
</td>
</tr>
<tr>
<td>Run ID</td>
<td><i class="fa-solid fa-bug icon-bug"></i>
Corrected <code>run-{X}</code> assignments so that they reflect chronological acquisition order.
</td>
</tr>

<tr>
<td>Raw QC Metrics</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>
Raw MR data QC metrics in raw BIDS SCANS TSV files are now combined into a single table across participants/sessions.</td>
</tr>

<tr>
<td>Scanner info</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>
Scanner info in raw BIDS SCANS TSV files are now combined into a single table across participants/sessions.</td>
</tr>

</tbody></table>


##### Neurocognition & Language

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th style="width: 20%; white-space: nowrap;">Topic</th>
<th>Summary of Changes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bayley</td>
<td><i class="fa-solid fa-bug icon-bug"></i>
Removed participant data with invalid scores of <code>-9999</code>. 
</td>
</tr>

<tr>
<td>CDI</td>
<td><i class="fa-solid fa-bug icon-bug"></i>
Corrected percentile calculations for N=36 cases in which 'Adjusted Percentile' had been incorrectly parsed from 'Total Produced' rather than 'Total Produced Percentile-sex (adjusted)'.
</td>
</tr>

</tbody></table>











### 3.0 Inclusion & Exclusion Criteria

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
<td><strong>2.1</strong></td>
<td>2026-08-14</td>
<td>
  <a href="https://docs.hbcdstudy.org/r2.1/changelog/release-notes/#release-21">
    View Release Notes
  </a>
</td>
</tr>

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