# Visit Information

{{ alert_warning(instruments.visit_info) }}
{{ data_warning(instruments.visit_info) }}
{{ issues_banner() }}

----

{{ instrument_description(instruments.visit_info) }}

---

{{ suppx(instruments.visit_info, "1") }}

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

{{ references(instruments.visit_info) }}



<!-- 
## Substance Use Flags

**Substance use (SU) flag** variables indicate whether a participant met study-defined criteria for prenatal exposure to Alcohol, Nicotine, Cannabis, Opioids, or Stimulants ([Gurka et al., 2025](https://doi.org/10.1016/j.dcn.2024.101494)). Variables include instrument-specific and rolled up SU flags aggregate evidence across instruments to provide a single indicator per substance. Source study instruments include:

- [Timeline Follow Back (TLFB)](https://docs.hbcdstudy.org/2.1/instruments/pregexp/su/tlfb): Self-reported use
- [Health V2- Infancy](https://docs.hbcdstudy.org/2.1/instruments/pregexp/pex): Diagnosis of Neonatal Opioid Withdrawal Syndrome (NOWS) or Fetal Alcohol Syndrome (FAS)
- [Nail](https://docs.hbcdstudy.org/2.1/instruments/biospec/nails) and/or [Urine](https://docs.hbcdstudy.org/2.1/instruments/biospec/urine) positive toxicology results -->

<!-- 

## HBCD Cohorts
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


#### Caregiver Types

- **Type A:** Temporary alternative caregiver
- **Type B:** Change in primary caregiver (placement only) without change in legal custody (Birth Parent unable to complete visit)
- **Type C:** Change in joint custody
- **Type D:** Change in placement (Child removed from birth parent and placed in foster care)
- **Type E:** Change in legal custody and placement (e.g., adoption)


#### Postnatal Recruits (PNR)

Postnatal Recruits are enrolled in the study after the child is born and complete a modified V01 and V02. The PNR cohort is only denoted for the V02 visit, with all subsequent visits falling under the same cohort as a standard participant. To check if a participant was part of a PNR cohort, users can either check the cohort at V02 or refer to the [PNR participant list](https://hbcd-docs-private.lassoinformatics.com/participant_lists/PNR_participants-supplemental.csv) available to DUC-authorized users via the [HBCD Private Release Notes](https://hbcd-docs-private.lassoinformatics.com/#download).

#### Multiple Birth Participants

Multiple Birth cohorts include siblings/twins enrolled as <b>Main Child</b> and <b>Sibling</b> participants. Instruments or instrument fields that are specific to the caregiver and not child will be identical across siblings. For twins and triplets, age variables will also be identical (including those derived from jittered date of birth). See the supplemental [Multibirth participant list](https://hbcd-docs-private.lassoinformatics.com/participant_lists/multi_birth_participants-supplemental.csv), including mapping between sibling participant IDs, is available available to DUC-authorized users via the [HBCD Private Release Notes](https://hbcd-docs-private.lassoinformatics.com/#download). -->