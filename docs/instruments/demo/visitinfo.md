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

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">This data has known issues - <a href="../../../changelog/knownissues/#demographics" target="_blank">see details</a>.</span>
</div>
<p></p>

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
General visit information includes site, project, and information about missed visits and participant withdrawal:
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
 <td>par_visit_data_visit_missed_date</td>
 <td>Date of missed visit</td>
 </tr>
 <tr>
 <td>par_visit_data_reason_visit_missed</td>
 <td>If the visit was missed, the reason why.</td>
 </tr>
 </tbody>
 </table>

## Substance Use Flags

Visit Level Data also includes **substance use flags**, which are single-summary variables that indicate substance use status (yes/no) based on any positive reports from the following instruments:

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
</table>
</div>
<p></p>

## Cohort & Caregiver Types

### HBCD Cohorts
**Cohort** information (<code>par_visit_data_cohort</code>) includes cohort subtypes and caregiver type (*Type A-F* - [see details](#caregiver-types)) for each participant. Cohort subtypes are split into **Main Child** and **Multiple Birth**, with additional labeling for *Postnatal Recruits* (*PNR*) and Multiple Birth siblings (*Main Child* vs. *Sibling*):

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
<tr><td>HBCD Main Child - PNR<b>*</b></td><td>1</td></tr>
<tr><td>HBCD Main Child - Type <i>A - E</i></td><td><i>2 - 6</i> &nbsp; (<i>A→2, &nbsp; B→3, &nbsp; C→4, &nbsp; D→5 &nbsp; E→6</i>)</td></tr>
</tbody>
<tbody>
<tr>
  <td rowspan="5"><b>HBCD Multiple Birth</b></td>
  <td>HBCD Multiple Birth - Main Child</td><td>7</td>
</tr>
    <tr><td>HBCD Multiple Birth - PNR<b>*</b></td><td>8</td></tr>
    <tr><td>HBCD Multiple Birth - PNR<b>*</b> - Sibling</td><td>9</td></tr>
    <tr><td>HBCD Multiple Birth - Sibling</td><td>10</td></tr>
    <tr><td>HBCD Multiple Birth - Type <i>A - E</i></td><td><i>11 - 15</i> &nbsp; (<i>A→11, &nbsp; B→12, &nbsp; C→13, &nbsp; D→14, &nbsp; E→15</i>)</td></tr>
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

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)"> <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span> <span class="text-with-link"> <span class="text"><i>Blank Fields in Sibling Data (Multiple Birth Cohorts)</i></span> <a class="anchor-link" href="#warning" title="Copy link"> <i class="fa-solid fa-link"></i> </a> </span> <span class="arrow">▸</span> </div> <div class="warning-collapsible-content"> <p><strong>In the current release, non-child-specific instrument fields are populated only for the Main Child.</strong> These values should be identical for all siblings, and future releases will populate them consistently across participants (see <a href="../../../changelog/pending/#multiple-birth-participants" target="_blank">Pending Updates</a>).</p> <p>Until then, users should obtain non-child-specific values for any <strong>Sibling</strong> participant by referencing the corresponding <strong>Main Child</strong> in the mapping file. These data are unavailable for the <strong>4 siblings</strong> whose Main Child is not yet included in the release.</p> </div>

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
