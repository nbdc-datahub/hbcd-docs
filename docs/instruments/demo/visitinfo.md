# Visit Information

<div class="info-block">
  <div class="info-row">
    <div class="info-label"><i class="fa fa-table"></i> Table Name:</div>
    <div class="info-value"><code>par_visit_data</code></div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-tape"></i> Construct:</div>
    <div class="info-value">Derived Visit Information</div>
  </div>
</div>

---------------------------------------------

**Visit Level Data includes: [General Visit Information](#general-visit-information), [Substance Use Flags](#substance-use-flags), and [Cohort & Caregiver Types](#cohort-caregiver-types).**

## Age Of Child at Each Visit
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
<td><b>Visit 1 (V01)</b></td>
<td><b>Visit 2 (V02)</b></td>
<td><b>Visit 3 (V03)</b></td>
<td><b>Visit 4 (V04)</b></td>
<td><b>Visit 5 (V05)</b></td>
<td><b>Visit 6 (V06)</b></td>
<td><b>Visit 7 (V07)</b></td>
</tr>
<tr>
<td>Prenatal</td>
<td>0-1 month</td>
<td>3-9 months</td>
<td>9-15 months</td>
<td>10-17 months</td>
<td>15-30 months</td>
<td>16-32 months</td>
</tr>
</tbody>
</table>

## General Visit Information
General visit information includes site, project, and information about missed visits and participant withdrawal.

<div id="gen" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-table"></i></span>
  <span class="text-with-link">
  <span class="text">General Visit Level Data Variables</span>
  <a class="anchor-link" href="#gen" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
 <table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
 <thead>
 <tr>
 <th>Name</th>
 <th>Description</th>
</tr>
 </thead>
 <tbody>
  <tr>
 <td>par_visit_data_site</td>
 <td>The candidate site.</td>
 </tr>
  <tr>
 <td>par_visit_data_project</td>
 <td>The candidate project name.</td>
 </tr>
 <tr>
 <td>par_visit_data_participant_withdrawal</td>
 <td>Tells if the participant withdrawn from the study.</td>
 </tr>
  <tr>
 <td>par_visit_data_visit_missed</td>
 <td>Tells if the visit was missed.</td>
 </tr>
<tr>
 <td>par_visit_data_visit_missed_date (<i>to be added in future release</i>)</td>
 <td>Date of missed visit</td>
 </tr>
 <tr>
 <td>par_visit_data_reason_visit_missed</td>
 <td>If the visit was missed, the reason why.</td>
 </tr>
 </tbody>
 </table>
 </div>

## Substance Use Flags

### Instrument-Specific SU Flags

**SU flags** indicate whether a participant met study-defined criteria for prenatal exposure to **Alcohol, Nicotine, Cannabis, Opioids, or Stimulants.** Instrument-specific flags are generated from positive reports in the instruments listed below. See  [Gurka et al., 2025](https://doi.org/10.1016/j.dcn.2024.101494) for full methodological details.


<table class="table-no-vertical-lines" style="width:100%; table-layout:fixed;"> 
<thead> <tr> 
<th>Instrument</th>
<th>SU Flag Variables</th>
<th>Positive Report</th>
</tr> </thead>
<tbody>
<tr>
<td>Biospecimen - <a href="../../biospec/urine" target="_blank">Urine</a><sup><b>1</b></sup></td>
<td><code>su_flag_bio_bm_&lt;<span class="tooltip">SUBSTANCE<span class="tooltiptext">ethanol; nicotine; cannabinoid; opioid; stim</span></span>&gt;</code></td>
<td style="word-wrap: break-word; white-space: normal;">Positive USDTL urine toxicology result</td>
</tr>
<tr>
<td>Timeline Follow Back (<a href="../../pregexp/su/tlfb" target="_blank">TLFB</a>)</td>
<td><code>su_flag_tlfb_bm_&lt;<span class="tooltip">SUBSTANCE<span class="tooltiptext">alcohol; nicotine; cannabis; opioid; stimulant</span></span>&gt;</code></td>
<td style="word-wrap: break-word; white-space: normal;">Self-reported use</td>
</tr>
<tr>
<td><strong><a href="../../pregexp/pex" target="_blank">Health V2 - Infancy</a></strong></td>
<td><code>su_flag_healthv2_ch_&lt;fas|nows&gt;</code></td>
<td style="word-wrap: break-word; white-space: normal;">Diagnosis of <span class="tooltip to">NOWS<span class="tooltiptext">Neonatal Opioid Withdrawal Syndrome</span></span> or <span class="tooltip">FAS<span class="tooltiptext">Fetal Alcohol Syndrome</span></span></td>
</tr>
</tbody>
<tfoot>
<tr>
  <td colspan="3" style="word-wrap: break-word; white-space: normal; border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
    <sup><b>1</b></sup> <i><a href="../../biospec/nails" target="_blank">Nails</a> Biospecimen results will additionally be integrated into creation of SU flags in a future release</i>
  </td>
</tr>
</tfoot>
</table>

### Derived SU Flags

In addition to the above, the following derived SU flags **aggregate evidence across instruments** to provide a single indicator per substance. **A derived SU flag is reported as "Yes" if one or more contributing instrument-specific flags are positive.**

<table class="table-no-vertical-lines" style="width:100%; table-layout:fixed;"> 
<thead>
<tr> 
<th style="width:20%">Substance</th>
<th style="width:25%">Derived SU Flag</th>
<th style="width:55%">Contributing Instrument Flags</th>
</tr>
</thead>
<tbody>
<tr>
<td>Alcohol</td>
<td><code>su_flag_alcohol</code></td>
<td>
<code>su_flag_bio_ethanol</code> (Urine toxicology)<br>
<code>su_flag_tlfb_alcohol</code> (TLFB self-report)<br>
<code>su_flag_healthv2_fas</code> (Health V2 – FAS diagnosis)
</td>
</tr>
<tr>
<td>Nicotine</td>
<td><code>su_flag_nicotine</code></td>
<td>
<code>su_flag_bio_nicotine</code> (Urine toxicology)<br>
<code>su_flag_tlfb_nicotine</code> (TLFB self-report)
</td>
</tr>
<tr>
<td>Cannabis</td>
<td><code>su_flag_cannabis</code></td>
<td>
<code>su_flag_bio_cannabinoid</code> (Urine toxicology)<br>
<code>su_flag_tlfb_cannabis</code> (TLFB self-report)
</td>
</tr>
<tr>
<td>Opioids</td>
<td><code>su_flag_opioid</code></td>
<td>
<code>su_flag_bio_opioid</code> (Urine toxicology)<br>
<code>su_flag_tlfb_opioid</code> (TLFB self-report)<br>
<code>su_flag_healthv2_nows</code> (Health V2 – NOWS diagnosis)
</td>
</tr>
</tbody>
</table>

<div id="su" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-sliders"></i></span>
  <span class="text-with-link">
  <span class="text">Prenatal Exposure Thresholds</span>
  <a class="anchor-link" href="#su" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>The thresholds below define the criteria used to determine whether an instrument-specific report is considered positive for prenatal exposure. <b>For each substance, only one of the listed exposure thresholds must be met for the derived SU flag to be positive</b>.</p>

<table class="compact-table-no-vertical-lines" style="width:100%; table-layout:fixed;"> 
<thead> <tr> 
<th>Substance</th>
<th>Data Source</th>
<th>Exposure Threshold
<i>(Substance use flagged as positive if ≥1 criterion is met)</i></th>
</tr> </thead>
<tbody>
<tr> 
<td rowspan="4"><strong>Alcohol</strong></td>
<td>TLFB</td> <td>Self-reported use ≥7 standard drinks per week for ≥2 weeks during pregnancy (Wk 03-09)</td></tr>
<tr><td>TLFB</td> <td>Self-reported use ≥3 standard drinks per occasion on ≥2 occasions during pregnancy (Wk 03-09)</td> </tr>
<tr><td>Health V2-Infancy</td> <td>Diagnosis of Fetal Alcohol Syndrome (FAS)</td></tr>
<tr><td>Urine</td> <td>Positive alcohol toxicology result</td>
</tr>
<tr>
<td rowspan="3"><strong>Opioids</strong></td>
<td>TLFB</td>
<td style="word-wrap: break-word; white-space: normal;">Self-reported use of prescribed (including medications for opioid use disorder) or illicit opioids for ≥2 weeks during pregnancy (Wk 03-09)</td></tr>
<tr>
<td>Health V2-Infancy</td> 
<td>Diagnosis of Neonatal Opioid Withdrawal Syndrome (NOWS)</td>
</tr>
<tr>
<td>Urine</td> <td>Positive opioid toxicology result in research-collected biospecimen</td>
</tr>
<tr>
<td rowspan="2"><strong>Cannabis</strong></td> <td>TLFB</td> <td>Self-reported cannabis use for ≥4 weeks during pregnancy (Wk 03-09)</td> </tr>
<tr> <td>Urine</td> <td>Positive cannabis toxicology result</td> </tr> 
<tr> <td rowspan="2"><strong>Nicotine</strong></td> <td>TLFB</td> <td>Self-reported nicotine or nicotine product use for ≥4 weeks during pregnancy (Wk 03-09)</td> </tr> 
<tr> <td>Urine</td> <td>Positive nicotine toxicology result</td> </tr> 
</tbody> </table>

<p>© Copyright 2025 by Elsevier. All rights reserved. Used/adapted with permission from <a href="https://doi.org/10.1016/j.dcn.2024.101494">Gurka et al., Dev Cogn Neurosci. 2025</a>.</p>
</div>
<p></p>


## Cohort & Caregiver Types

<div class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text">See <a href="../../../changelog/releasenotes/#participant-population-inclusionexclusion-criteria" target="_blank">Release Notes</a> for participant population inclusion/exclusion information.</span>
</div>

### HBCD Cohorts
**Cohort** information (<code>par_visit_data_cohort</code>) includes cohort subtypes and caregiver type (*Type A-E* - [see details](#caregiver-types)) for each participant. Cohort subtypes are split into **Main Child** and **Multiple Birth**, with additional labeling for *Postnatal Recruits* (*PNR*) and Multiple Birth siblings (*Main Child* vs. *Sibling*):

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
  <th>Cohort</th>
  <th>Cohort Subtype Label</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="3"><b>HBCD Main Child</b></td>
  <td>HBCD Main Child</td>
</tr>
<tr><td>HBCD Main Child - Postnatal Recruitment<b>*</b></td></tr>
<tr><td>HBCD Main Child - Type <i>A - E</i></td>
</tr>
</tbody>
<tbody>
<tr>
  <td rowspan="5"><b>HBCD Multiple Birth</b></td>
  <td>HBCD Multiple Birth - Main Child</td>
</tr>
    <tr><td>HBCD Multiple Birth - Postnatal Recruitment<b>*</b></td></tr>
    <tr><td>HBCD Multiple Birth - Postnatal Recruitment<b>*</b> - Sibling</td></tr>
    <tr><td>HBCD Multiple Birth - Sibling</td></tr>
    <tr><td>HBCD Multiple Birth - Type <i>A - E</i></td></tr>
</tbody>
<tfoot><tr><td colspan="3"><b>*</b> PNR is only available for V02 - <a href="#postnatal-recruits-pnr">see details</a></td></tr></tfoot>
</table>

### Postnatal Recruits (PNR)

<a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/PNR_participants-supplemental.csv"><i class="fa-solid fa-download"></i> &nbsp; Download participant list</a> <i>(available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>)</i>

Postnatal Recruits are enrolled in the study after the child is born and complete a modified V01 and V02. **The PNR cohort is only denoted for the V02 visit**, with all subsequent visits falling under the same cohort as a standard participant. To check if a participant was part of a PNR cohort, users can either check the cohort at V02 or refer to the provided participant list.

### Multiple Birth Participants
<a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/multi_birth_participants-supplemental.csv"><i class="fa-solid fa-download"></i> &nbsp; Download participant list</a> <i>(available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>)</i>

Multiple Birth cohorts include siblings/twins enrolled as <b>Main Child</b> and <b>Sibling</b> participants. Certain data fields, such as caregiver or maternal instrument data that are not child-specific (e.g., <a href="../../SED/demo-cg/">Adult Demographics</a>), are expected to be identical across siblings. For twins and triplets, all <a href="../../agevariables/" target="_blank">age variables</a> will also be identical, including those derived from jittered date of birth.

The downloadable participant list maps each **Main Child** to their corresponding **Sibling** IDs. In the current release, some multiples are incomplete (missing partner ID appears as <code>na</code> in the file):

 - 33 **Main Child** participants do not yet have their paired **Sibling** included, and
 - 4 **Sibling** participants do not yet have their paired **Main Child** included.

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)"> <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span> <span class="text-with-link"> <span class="text"><i>Blank Fields in Sibling Data (Multiple Birth Cohorts)</i></span> <a class="anchor-link" href="#warning" title="Copy link"> <i class="fa-solid fa-link"></i> </a> </span> <span class="arrow">▸</span> </div> <div class="warning-collapsible-content"> <p><strong>In the current release, family/maternal-level (i.e. non-child-specific) instrument fields are only populated for the Main Child.</strong> These values should be identical for all siblings, and in a future release, <b>HBCD Main Child</b> data will be copied to the sibling profile (e.g. <b>HBCD Multiple Birth - Sibling</b>) for non-child-specific elements so that the information is populated consistently across participants. In addition, a new Data Dictionary element (<b>familyID</b>) will be incorporated to help identify siblings.</p>
<p>Until then, users should obtain non-child-specific values for any <strong>Sibling</strong> participant by referencing the corresponding <strong>Main Child</strong> in the mapping file. These data are unavailable for the <strong>4 siblings</strong> whose Main Child is not yet included in the release.</p> </div>

### Caregiver Types

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
    <tr>
        <td><b>Type A</b></td>
        <td>Temporary Alternative Caregiver</td>
    </tr>
    <tr>
        <td><b>Type B</b></td>
        <td style="word-wrap: break-word; white-space: normal;">Change in Primary Caregiver (Placement Only) Without Change in Legal Custody (But Birth Parent Unable to Complete Visit)</td>
    </tr>
    <tr>
        <td><b>Type C</b></td>
        <td>Change in Joint Custody</td>
    </tr>
    <tr>
        <td><b>Type D</b></td>
        <td style="word-wrap: break-word; white-space: normal;">Child Removed From Birth Parent and Placed in Foster Care (Change in Placement)</td>
    </tr>
    <tr><td><b>Type E</b></td><td>Change in Legal Custody and Placement (e.g. adoption)</td>
    </tr>            
</tbody>
</table>


 ## References

<div class="references">
    <p>Gurka, K. K., Burris, H. H., Ciciolla, L., Coles, C. D., Massey, S. H., Newman, S., Rajagopalan, V., Smith, L. M., Zilverstand, A., Bandoli, G., & HBCD Pregnancy Exposures, Including Substances Workgroup. (2025). Assessment of maternal health and behavior during pregnancy in the HEALthy Brain and Child Development Study: Rationale and approach. <em>Developmental Cognitive Neuroscience</em>, 71(101494), 101494. <a href="https://doi.org/10.1016/j.dcn.2024.101494">https://doi.org/10.1016/j.dcn.2024.101494</a></p>
</div>




<!-- 
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>par_visit_data_su_flag_alcohol</td>
<td style="word-wrap: break-word; white-space: normal;">Rolled up Alcohol flag from Biological Mother across sources (Biospecimen, TLFB Self-report, Health V2 FAS)</td>
</tr>
<tr>
<td>par_visit_data_su_flag_bio_bm_cannabinoid</td>
<td>Substance Use in Urine Biosample from Biological Mother - cannabinoid</td>
</tr>
<tr>
<td>par_visit_data_su_flag_bio_bm_ethanol</td>
<td>Substance Use in Urine Biosample from Biological Mother - ethanol</td>
</tr>
<tr>
<td>par_visit_data_su_flag_bio_bm_nicotine</td>
<td>Substance Use in Urine Biosample from Biological Mother - nicotine</td>
</tr>
<tr>
<td>par_visit_data_su_flag_bio_bm_opioid</td>
<td>Substance Use in Urine Biosample from Biological Mother - opioid</td>
</tr>
<tr>
<td>par_visit_data_su_flag_bio_bm_stim</td>
<td>Substance Use in Urine Biosample from Biological Mother - stimulant</td>
</tr>
<tr>
<td>par_visit_data_su_flag_cannabis</td>
<td style="word-wrap: break-word; white-space: normal;">Rolled up Cannabis flag from Biological Mother across sources (Biospecimen, TLFB Self-report)</td>
</tr>
<tr>
<td>par_visit_data_su_flag_healthv2_ch_fas</td>
<td>Substance Use in Health V2 instrument from Biological Mother - FAS</td>
</tr>
<tr>
<td>par_visit_data_su_flag_healthv2_ch_nows</td>
<td>Substance Use in Health V2 instrument from Biological Mother - NOWS</td>
</tr>
<tr>
<td>par_visit_data_su_flag_nicotine</td>
<td style="word-wrap: break-word; white-space: normal;">Rolled up Nicotine flag from Biological Mother across sources (Biospecimen, TLFB Self-report)</td>
</tr>
<tr>
<td>par_visit_data_su_flag_opioid</td>
<td style="word-wrap: break-word; white-space: normal;">Rolled up Opioid flag from Biological Mother across sources (Biospecimen, TLFB Self-report, Health V2 NOWS)</td>
</tr>
<tr>
<td>par_visit_data_su_flag_stimulant</td>
<td style="word-wrap: break-word; white-space: normal;">Rolled up Stimulant flag from Biological Mother across sources (Biospecimen, TLFB Self-report)</td>
</tr>
<tr>
<td>par_visit_data_su_flag_tlfb_bm_alcohol</td>
<td>Substance Use in TLFB instrument from Biological Mother - alcohol</td>
</tr>
<tr>
<td>par_visit_data_su_flag_tlfb_bm_cannabis</td>
<td>Substance Use in TLFB instrument from Biological Mother - cannabis</td>
</tr>
<tr>
<td>par_visit_data_su_flag_tlfb_bm_nicotine</td>
<td>Substance Use in TLFB instrument from Biological Mother - nicotine</td>
</tr>
<tr>
<td>par_visit_data_su_flag_tlfb_bm_opioid</td>
<td>Substance Use in TLFB instrument from Biological Mother - opioid</td>
</tr>
<tr>
<td>par_visit_data_su_flag_tlfb_bm_stimulant</td>
<td>Substance Use in TLFB instrument from Biological Mother - stimulant</td>
</tr>
</tbody>
</table> -->