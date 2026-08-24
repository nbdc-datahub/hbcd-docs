<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
</style>

# Dynamic Table

{{ readme_summary(instruments.dynamic) }}
{{ alert_warning(instruments.dynamic) }}
{{ data_warning(instruments.dynamic) }}
{{ issues_banner() }}

---

## Overview

{{ instrument_description(instruments.dynamic) }}

<table class="compact-table-no-vertical-lines static-dynamic-tables">
<thead>
<tr>
  <th>Construct</th>
  <th>Variable Name</th>
  <th>Visit</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Caregiver education</td>
  <td>rc_cg_education</td> 
  <td>V01, V04+</td>
  <td>Highest level of school completed from Demographics (Adult)</td>
</tr>
<tr>
  <td>Household income</td>
  <td>rc_cg_income</td> 
  <td>V01, V04+</td>
  <td>Primary caregiver’s household income from Demographics (Adult)</td>
</tr>
<tr>
  <td>Transitions in Care</td>
  <td>TBD</td> 
  <td></td>
  <td>Flag for transitions in care</td>
</tr>
<tr>
  <td>Caregiver type</td>
  <td>TBD</td> 
  <td>V02+</td>
  <td>Caregiver type at each wave, derived from administrative records</td>
</tr>
<tr>
  <td>Cohort</td>
  <td>data_cohort</td> 
  <td>V02+</td>
  <td>Cohort subtype, derived from administrative records</td>
</tr>
<tr>
  <td>Site</td>
  <td>site</td> 
  <td>V01+</td>
  <td>Location (site) at visit</td>
</tr>
<tr>
  <td>Missed Visit</td>
  <td>TBD</td> 
  <td>V02+</td>
  <td>Missed study visit</td>
</tr>
<tr>
  <td>Gestational Age at Visit</td>
  <td>TBD</td> 
  <td>V01+</td>
  <td>TBD</td>
</tr>
<tr>
  <td>Total Household 1 Roster- Adult</td>
  <td>TBD</td> 
  <td>V01</td>
  <td>Total number of people (adults+children) in Household 1, from Demographics (Adult)</a></td>
</tr>
<tr>
  <td>Total Household 1 Roster- Child</td>
  <td>TBD</td> 
  <td>V04+</td>
  <td>Total number of people (adults+children) in Household 1, from Demographics (Child)</td>
</tr>
<tr>
  <td>Caregiver marital/partner status</td>
  <td>TBD</td> 
  <td>V01, V04+</td>
  <td>Caregiver marital/partner status, from Demographics (Adult)</td>
</tr>
<tr>
  <td>Urban Rural Classification</td>
  <td>urban_urbanclassification</td> 
  <td></td>
  <td></td>
</tr>
<tr>
  <td>Social Vulnerability Index</td>
  <td>svi_theme4_prcntile</td> 
  <td></td>
  <td>SVI– Housing Type/Transportation national percentiles 1 to 100</td>
</tr>
<tr>
  <td>Substance use flags</td>
  <td>su_flag_*</td> 
  <td></td>
  <td>SU flags derived from multiple instruments- see details below</td>
</tr>
</tbody>
</table>


{{ suppx(instruments.dynamic, "1") }}


<table class="table-no-vertical-lines">
<thead>
<tr>
<th>Substance</th>
<th>Rolled Up Flag</th>
<th>Urine/Nail SU Flag</th>
<th>TLFB SU Flag</th>
<th>HealthV2 SU Flag</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Alcohol</strong></td>
<td><code>alcohol</code></td>
<td><code>bio_bm_ethanol</code></td>
<td><code>tlfb_bm_alcohol</code></td>
<td><code>healthv2_ch_fas</code></td>
</tr>
<tr>
<td><strong>Nicotine</strong></td>
<td><code>nicotine</code></td>
<td><code>bio_bm_{nails|urine}_nicotine</code></td>
<td><code>tlfb_bm_nicotine</code></td>
<td>—</td>
</tr>
<tr>
<td><strong>Cannabis</strong></td>
<td><code>cannabis</code></td>
<td><code>bio_bm_{nails|urine}_cannabinoid</code></td>
<td><code>tlfb_bm_cannabis</code></td>
<td>—</td>
</tr>
<tr>
<td><strong>Opioids</strong></td>
<td><code>opioid</code></td>
<td><code>bio_bm_{nails|urine}_opioid</code></td>
<td><code>tlfb_bm_opioid</code></td>
<td><code>healthv2_ch_nows</code></td>
</tr>
<tr>
<td><strong>Stimulants</strong></td>
<td><code>stimulant</code></td>
<td><code>bio_bm_{nails|urine}_stim</code></td>
<td><code>tlfb_bm_stimulant</code></td>
<td>—</td>
</tr>
</tbody>
</table>

---

{{ references(instruments.dynamic) }}













<!-- 

##### Prenatal Exposure Thresholds

Prenatal exposure thresholds that define when an instrument-specific report is considered positive for prenatal exposure are outlined in [Gurka et al. 2025 - Table 2](https://www.sciencedirect.com/science/article/pii/S1878929324001555?via%3Dihub#tbl0010). For each substance, the derived SU flag is positive if one or more of the corresponding instrument-specific reports are positive.


The thresholds below define when an instrument-specific report is considered positive for prenatal exposure. For each substance, the derived SU flag is positive if one or more of the corresponding instrument-specific reports are positive.

- **Alcohol**
    - TLFB: Self-reported use ≥7 standard drinks per week for ≥2 weeks during pregnancy (weeks 3–9)
    - TLFB: Self-reported use ≥3 standard drinks per occasion on ≥2 occasions during pregnancy (weeks 3–9)
    - Health V2: Diagnosis of Fetal Alcohol Syndrome (FAS)
    - Urine: Positive alcohol toxicology result

- **Opioids**
    - TLFB: Self-reported use of prescribed (including medications for opioid use disorder) or illicit opioids for ≥2 weeks during pregnancy (weeks 3–9)
    - Health V2: Diagnosis of Neonatal Opioid Withdrawal Syndrome (NOWS)
    - Urine: Positive opioid toxicology result

- **Cannabis**
    - TLFB: Self-reported cannabis use for ≥4 weeks during pregnancy (weeks 3–9)
    - Urine: Positive cannabis toxicology result

- **Nicotine**
    - TLFB: Self-reported nicotine or nicotine product use for ≥4 weeks during pregnancy (weeks 3–9)
    - Urine: Positive nicotine toxicology result -->


<!-- 
<div id="su" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-sliders"></i></span>
  <span class="text-with-link">
  <span class="text">Prenatal Exposure Thresholds</span>
  <a class="anchor-link" href="#su" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>The thresholds below define when an instrument-specific report is considered positive for prenatal exposure. For each substance, the derived SU flag is positive if one or more of the corresponding instrument-specific reports are positive.</p>
<table class="compact-table-no-vertical-lines"> 
<thead> <tr> 
<th>Substance</th>
<th>Source</th>
<th>Instrument-Specific Exposure Thresholds</th>
</tr> </thead>
<tbody>
<tr> 
<td rowspan="4"><strong>Alcohol</strong></td>
<td>TLFB</td> <td>Self-reported use ≥7 standard drinks per week for ≥2 weeks during pregnancy (weeks 3-9)</td></tr>
<tr><td>TLFB</td> <td>Self-reported use ≥3 standard drinks per occasion on ≥2 occasions during pregnancy (weeks 3-9)</td> </tr>
<tr><td>Health V2</td> <td>Diagnosis of Fetal Alcohol Syndrome (FAS)</td></tr>
<tr><td>Urine</td> <td>Positive alcohol toxicology result</td>
</tr>
<tr>
<td rowspan="3"><strong>Opioids</strong></td>
<td>TLFB</td>
<td>Self-reported use of <span class="tooltip">prescribed<span class="tooltiptext">including medications for opioid use disorder</span></span> or illicit opioids for ≥2 weeks during pregnancy (weeks 3-9)</td></tr>
<tr>
<td>Health V2</td> 
<td>Diagnosis of Neonatal Opioid Withdrawal Syndrome (NOWS)</td>
</tr>
<tr>
<td>Urine</td> <td>Positive opioid toxicology result</td>
</tr>
<tr>
<td rowspan="2"><strong>Cannabis</strong></td> <td>TLFB</td> <td>Self-reported cannabis use for ≥4 weeks during pregnancy (weeks 3-9)</td> </tr>
<tr> <td>Urine</td> <td>Positive cannabis toxicology result</td> </tr> 
<tr> <td rowspan="2"><strong>Nicotine</strong></td> <td>TLFB</td> <td>Self-reported nicotine or nicotine product use for ≥4 weeks during pregnancy (weeks 3-9)</td> </tr> 
<tr> <td>Urine</td> <td>Positive nicotine toxicology result</td> </tr> 
</tbody> </table>
<p>© Copyright 2025 by Elsevier. All rights reserved. Used/adapted with permission from <a href="https://doi.org/10.1016/j.dcn.2024.101494">Gurka et al. 2025</a></p>
</div>
<p></p> -->



<!-- <span class="table-title">SU Flag Variable Summary <i>(all variable names are prefixed with <code>su_flag_</code>, omitted below for readability)</i></span> -->



<!-- The following variables are computed from administrative records collected during screening or instruments such as the Demographics measure ([Adult](../../instruments/SED/demo-cg.md) or [Child](../../instruments/SED/demo-ch.md)). Sources are noted in the Description field and otherwise can be assumed to be derived from administrative records. -->



<!-- **Substance use (SU) flag** variables indicate whether a participant met study-defined criteria for prenatal exposure to Alcohol, Nicotine, Cannabis, Opioids, or Stimulants ([Gurka et al., 2025](https://doi.org/10.1016/j.dcn.2024.101494)). Variables include instrument-specific and rolled up SU flags aggregate evidence across instruments to provide a single indicator per substance. Source study instruments include:

- [Timeline Follow Back (TLFB)](https://docs.hbcdstudy.org/2.1/instruments/pregexp/su/tlfb): Self-reported use
- [Health V2- Infancy](https://docs.hbcdstudy.org/2.1/instruments/pregexp/pex): Diagnosis of Neonatal Opioid Withdrawal Syndrome (NOWS) or Fetal Alcohol Syndrome (FAS)
- [Nail](https://docs.hbcdstudy.org/2.1/instruments/biospec/nails) and/or [Urine](https://docs.hbcdstudy.org/2.1/instruments/biospec/urine) positive toxicology results -->


<!-- 
### ORIG
**Cohort** information (<code>data_cohort</code>) includes cohort subtypes and [caregiver Type A-E](#caregiver-types) for each participant. Cohort subtypes are split into **Main Child** and **Multiple Birth**, with additional labeling for *Postnatal Recruits* (*PNR*) and Multiple Birth siblings (*Main Child* vs. *Sibling*):

* **HBCD Main Child**

    * HBCD Main Child
    * HBCD Main Child - Postnatal Recruitment
    * HBCD Main Child - Type *A - E*

* **HBCD Multiple Birth**

    * HBCD Multiple Birth - Main Child
    * HBCD Multiple Birth - Postnatal Recruitment
    * HBCD Multiple Birth - Postnatal Recruitment - Sibling
    * HBCD Multiple Birth - Sibling
    * HBCD Multiple Birth - Type *A - E*

##### Caregiver Types

- **Type A:** Temporary alternative caregiver
- **Type B:** Change in primary caregiver (placement only) without change in legal custody (Birth Parent unable to complete visit)
- **Type C:** Change in joint custody
- **Type D:** Change in placement (Child removed from birth parent and placed in foster care)
- **Type E:** Change in legal custody and placement (e.g., adoption)

##### Postnatal Recruits (PNR)

Postnatal Recruits are enrolled in the study after the child is born and complete a modified V01 and V02. The PNR cohort is only denoted for the V02 visit, with all subsequent visits falling under the same cohort as a standard participant. To check if a participant was part of a PNR cohort, users can either check the cohort at V02 or refer to the [PNR participant list](https://hbcd-docs-private.lassoinformatics.com/participant_lists/PNR_participants-supplemental.csv) available to DUC-authorized users via the [HBCD Private Release Notes](https://hbcd-docs-private.lassoinformatics.com/#download).

##### Multiple Birth Participants

Multiple Birth cohorts include siblings/twins enrolled as <b>Main Child</b> and <b>Sibling</b> participants. Instruments or instrument fields that are specific to the caregiver and not child will be identical across siblings. For twins and triplets, age variables will also be identical (including those derived from jittered date of birth). See the supplemental [Multibirth participant list](https://hbcd-docs-private.lassoinformatics.com/participant_lists/multi_birth_participants-supplemental.csv), including mapping between sibling participant IDs, is available available to DUC-authorized users via the [HBCD Private Release Notes](https://hbcd-docs-private.lassoinformatics.com/#download). -->
