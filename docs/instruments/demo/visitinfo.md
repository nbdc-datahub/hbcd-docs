
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

## Details

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
<th>Visit</th>
<th>Age Range of Child Participants</th>
</tr>
</thead>
<tbody>
<tr>
<td>Visit 1 (V01)</td>
<td>Prenatal</td>
</tr>
<tr>
<td>Visit 2 (V02)</td>
<td>0-1 month old</td>
</tr>
<tr>
<td>Visit 3 (V03)</td>
<td>3-9 months old</td>
</tr>
<tr>
<td>Visit 4 (V04)</td>
<td>9-15 months old</td>
</tr>
<tr>
<td>Visit 5 (V05)</td>
<td>10-17 months old</td>
</tr>
<tr>
<td>Visit 6 (V06)</td>
<td>15-30 months old</td>
</tr>
<tr>
<td>Visit 7 (V07)</td>
<td>16-32 months old</td>
</tr>
</tbody>
</table>

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
<td>Visit 1 (V01)</td>
<td>Visit 2 (V02)</td>
<td>Visit 3 (V03)</td>
<td>Visit 4 (V04)</td>
<td>Visit 5 (V05)</td>
<td>Visit 6 (V06)</td>
<td>Visit 7 (V07)</td>
</tr>
<tr>
<td>Prenatal</td>
<td>0-1 month</td>
<td>3-9 months</td>
<td>9-15 months</td>
<td>10-17 months</td>
<td>15-30 months old</td>
<td>16-32 months</td>
</tr>
</tbody>
</table>

Visit information contains all participant visit data, including:

### General Visit Information
 - Label, Stage, Date, Project, and Site
 - If the visit was missed and reason 
 - Withdrawal information (if the participant withdrew from the study, the reason, and date)
 - Protocol violation information (if there was a protocol exception and the date)

 <div id="vars" class="table-banner" onclick="toggleCollapse(this)">
   <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
   <span class="text-with-link">
   <span class="text">General Visit Information Variables</span>
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

### Substance Use Flags

Visit information also includes **substance use flags**, which are single summary variables that indicate substance use status (yes/no) based on any positive reports from the following instruments:

 - The Timeline Follow Back (<a href="../../pregexp/su/tlfb" target="_blank">TLFB</a>) (self-reported use)
 - <a href="../../pregexp/pex" target="_blank">Health V2- Infancy</a> when options 1 (*Neonatal Opioid Withdrawal Syndrome*) and/or 5 (*Fetal Alcohol Syndrome*) were selected for field `007` (self-reported use)
 - <a href="../../biospec/urine" target="_blank">USDTL urine toxicology results</a> (<i>note: <a href="../../biospec/nails" target="_blank">Nail toxicology results</a> were not used in the creation of the substance use flags</i>)
 
<div id="su" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">SU Visit Information Variables</span>
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

### Cohort & Caregiver Types

**Cohort** information (<code>par_visit_data_cohort</code>) includes cohort subtype and caregiver type for each participant.    
Possible values include:

 - HBCD Main Child - Postnatal Recruitment
 - HBCD Main Child - Type {*A-F*}
 - HBCD Multiple Birth - {*Main Child | Postnatal Recruitment | Sibling*}
 - HBCD Multiple Birth - Type {*A-F*}

<div id="cg-types" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Caregiver Type A-F Definitions</span>
  <a class="anchor-link" href="#cg-types" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
    <tr>
        <td>Type A</td>
        <td>Temporary Alternative Caregiver</td>
    </tr>
    <tr>
        <td>Type B</td>
        <td style="word-wrap: break-word; white-space: normal;">Change in Primary Caregiver (Placement Only) Without Change in Legal Custody (But Birth Parent Unable to Complete Visit)</td>
    </tr>
    <tr>
        <td>Type C</td>
        <td>Change in Joint Custody</td>
    </tr>
    <tr>
        <td>Type D</td>
        <td style="word-wrap: break-word; white-space: normal;">Child Removed From Birth Parent and Placed in Foster Care (Change in Placement)</td>
    </tr>
    <tr><td>Type E</td><td>Change in Legal Custody and Placement (e.g. adoption)</td>
    </tr>
    <tr><td>Type F</td><td>Original Consented Parent</td>
    </tr>            
</tbody>
</table>
</div>

