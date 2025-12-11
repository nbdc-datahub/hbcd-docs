# Visit Level Data

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

## General Visit Level Data
 - Label, Stage, Date, Project, and Site
 - If the visit was missed and reason 
 - Withdrawal information (if the participant withdrew from the study, the reason, and date)
 - Protocol violation information (if there was a protocol exception and the date)

 <div id="vars" class="table-banner" onclick="toggleCollapse(this)">
   <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
   <span class="text-with-link">
   <span class="text">General Visit Level Data Variables</span>
   <a class="anchor-link" href="#vars" title="Copy link">
   <i class="fa-solid fa-link"></i>
   </a>
   </span>
   <span class="arrow">▸</span>
 </div>
 <div class="table-collapsible-content">
 <table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
 <thead>
 <tr>
 <th>Name</th>
 <th>Description</th>
</tr>
 </thead>
 <tbody>
  <tr>
 <td><code>par_visit_data_site</code></td>
 <td>The candidate site.</td>
 </tr>
  <tr>
 <td><code>par_visit_data_project</code></td>
 <td>The candidate project name.</td>
 </tr>
 <tr>
 <td><code>par_visit_data_participant_withdrawal</code></td>
 <td>Tells if the participant withdrawn from the study.</td>
 </tr>
 <tr>
 <td><code>par_visit_data_participant_withdrawal_date</code></td>
 <td>If withdrawn, the date.</td>
 </tr>
 <tr>
 <td><code>par_visit_data_participant_withdrawal_reason</code></td>
 <td>If withdrawn, the reason why.</td>
 </tr>
 <tr>
 <td><code>par_visit_data_protocol_exception</code></td>
 <td>Tells if there was a protocol exception.</td>
 </tr>
 <tr>
 <td><code>par_visit_data_protocol_exception_date</code></td>
 <td>If protocol exception, the date.</td>
 </tr>
  <tr>
 <td><code>par_visit_data_visit_missed</code></td>
 <td>Tells if the visit was missed.</td>
 </tr>
 <tr>
 <td><code>par_visit_data_reason_visit_missed</code></td>
 <td>If the visit was missed, the reason why.</td>
 </tr>
 </tbody>
 </table>
 </div>
<p></p>

## Substance Use Flags

Visit Level Data also includes **substance use flags**, which are single summary variables that indicate substance use status (yes/no) based on any positive reports from the following instruments:

 - The Timeline Follow Back (<a href="../../pregexp/su/tlfb" target="_blank">TLFB</a>) (self-reported use)
 - <a href="../../pregexp/pex" target="_blank">Health V2- Infancy</a> when options 1 (*Neonatal Opioid Withdrawal Syndrome*) and/or 5 (*Fetal Alcohol Syndrome*) were selected for field `007` (self-reported use)
 - <a href="../../biospec/urine" target="_blank">USDTL urine toxicology results</a> (<i>note: <a href="../../biospec/nails" target="_blank">Nail toxicology results</a> were not used in the creation of the substance use flags</i>)
 
<div id="su" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">SU Visit Level Data Variables</span>
  <a class="anchor-link" href="#su" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</thead>
</tr>
<tbody>
<tr>
<td><code>par_visit_data_su_flag_bio_cannabinoid</code></td>
<td>Substance Use in Urine Biosample - cannabinoid</td>
</tr>
<tr>
<td><code>par_visit_data_su_flag_bio_opioid</code></td>
<td>Substance Use in Urine Biosample - opioid</td>
</tr>
<tr>
<td><code>par_visit_data_su_flag_bio_stim</code></td>
<td>Substance Use in Urine Biosample - stimulant</td>
</tr>
<tr>
<td><code>par_visit_data_su_flag_healthv2_fas</code></td>
<td>Substance Use in Health V2 instrument - FAS</td>
</tr>
<tr>
<td><code>par_visit_data_su_flag_healthv2_nows</code></td>
<td>Substance Use in Health V2 instrument - NOWS</td>
</tr>
<tr>
<td><code>par_visit_data_su_flag_tlfb_alcohol</code></td>
<td>Substance Use in TLFB instrument - alcohol</td>
</tr>
<tr>
<td><code>par_visit_data_su_flag_tlfb_cannabis</code></td>
<td>Substance Use in TLFB instrument - cannabis</td>
</tr>
<tr>
<td><code>par_visit_data_su_flag_tlfb_nicotine</code></td>
<td>Substance Use in TLFB instrument - nicotine</td>
</tr>
<tr>
<td><code>par_visit_data_su_flag_tlfb_opioid</code></td>
<td>Substance Use in TLFB instrument - opioid</td>
</tr>
<tr>
<td><code>par_visit_data_su_flag_tlfb_stimulant</code></td>
<td>Substance Use in TLFB instrument - stimulant</td>
</tr>
</tbody>
</table>
</div>
<p></p>

## Cohort & Caregiver Types

### HBCD Cohorts
**Cohort** information (<code>par_visit_data_cohort</code>) includes cohort subtypes and caregiver type (*Type A-F* - [see details](#cg-types)) for each participant. Cohort subtypes are split into **Main Child** and **Multiple Birth**, with additional labeling for *Postnatal Recruits* (*PNR*) and Multiple Birth siblings (*Main Child* vs. *Sibling*):

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
  <th>Cohort</th>
  <th>Cohort Subtype Label</th>
  <th>Value</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="3"><b>HBCD Main Child</b></td>
  <td>HBCD Main Child</td>
  <td>0</td>
</tr>
<tr><td>HBCD Main Child - PNR</td><td>1</td></tr>
<tr><td>HBCD Main Child - Type <i>A - E</i></td><td><i>2 - 6</i> &nbsp; (<i>A→2, &nbsp; B→3, &nbsp; C→4, &nbsp; D→5 &nbsp; E→6</i>)</td></tr>
</tbody>
<tbody>
<tr>
  <td rowspan="5"><b>HBCD Multiple Birth</b></td>
  <td>HBCD Multiple Birth - Main Child</td><td>7</td>
</tr>
    <tr><td>HBCD Multiple Birth - PNR</td><td>8</td></tr>
    <tr><td>HBCD Multiple Birth - PNR - Sibling</td><td>9</td></tr>
    <tr><td>HBCD Multiple Birth - Sibling</td><td>10</td></tr>
    <tr><td>HBCD Multiple Birth - Type <i>A - E</i></td><td><i>11 - 15</i> &nbsp; (<i>A→11, &nbsp; B→12, &nbsp; C→13, &nbsp; D→14, &nbsp; E→15</i>)</td></tr>
</tbody>
</table>

### Postnatal Recruits & Multiple Birth Participants

These cohort subtypes are defined below. Click the links to download participant lists for each, available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.

<table class="table-no-vertical-lines">
  <thead>
    <tr>
      <th>Cohort Subtype</th>
      <th>Description</th>
      <th>Download</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td>Multiple Birth</td>
    <td style="word-wrap: break-word; white-space: normal;">Siblings/twins enrolled in the study, categorized as <b>Main Child</b> and <b>Sibling</b>.</td>
    <td style="text-align: center;"><a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/multi_birth_participants-supplemental.csv"><i class="fa-solid fa-download"></i></a></td>
  </tr>
    <tr>
    <td>Postnatal Recruits (PNR)</td>
    <td style="word-wrap: break-word; white-space: normal;">Participants enrolled in the study after the child is born (complete a modified V01 and V02).</td>
    <td style="text-align: center;"><a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/PNR_participants-supplemental.csv"><i class="fa-solid fa-download"></i></a></td>
  </tr>
  </tbody>
  </table>

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text"><i>Blank Fields in Sibling Data (Multiple Birth Cohorts)</i></span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Certain fields are expected to be the same between siblings, such as caregiver/maternal instrument data that isn't child-specific (e.g. <a href="../../SED/demo-cg/">Adult Demographics</a>). For twins/triplets, all <a href="../../agevariables/" target="_blank">age variables</a> will also be the same, including those computed with a jittered DOB.</p>
<p><strong>However, non-child-specific instrument data are only populated for the Main Child in the current release.</strong> Future release data will be updated to provide more complete information - see <a href="../../../changelog/pending/#multiple-birth-participants" target="_blank">Pending Updates</a> for details. In the meantime, users will need to source blank <strong>Sibling</strong> data fields from the corresponding Main Child data for non-child-specific instrument tables. Please refer to the participant list mapping Main Child to Sibling IDs provided above - <a href="#postnatal-recruits-multiple-birth-participants">above</a>.</p>
</div>

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
    <tr><td><b>Type F</b></td><td>Original Consented Parent</td>
    </tr>            
</tbody>
</table>
