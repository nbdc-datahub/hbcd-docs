# HBCD Study Protocol Overview

## Study Timeline & Visits

<img src="https://hbcdstudy.org/wp-content/uploads/2025/03/HBCD_Timeline_March2025_Updated.png" 
alt="Age of Child participants at each Visit number: Visit 1 (V01) = Prenatal; Visit 2 (V02) = 0-1 month old; Visit 3 (V03) = 3-9 months old; Visit 4 (V04) = 9-15 months old; Visit 5 (V05) = 10-17 months old;  Visit 6 (V06) = 15-30 months old; Visit 7 (V07) = 16-32 months old" width="90%" height="auto" class="center">

<span class="table-title">The age range of the child participant at each visit (V0X) is as follows:</span>
<table class="table-no-vertical-lines">
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

## Participant Population

HBCD enrolls at least 25% of participants with more than minimal substance use during pregnancy, including opioids ([Si et al. 2024](https://doi.org/10.1016/j.dcn.2024.101432)). Enrollment strategies aim to yield a study population representative of individual and geographic characteristics of pregnant and postpartum individuals (18 years or older) in the U.S., including an adequate comparison group for substance-exposed individuals ([Nelson et al. 2024](https://doi.org/10.1016/j.dcn.2024.101441)). 

## Study Design Logic: Child-Centric Data Structure

The HBCD Study organizes data around the Child ID as the primary key, meaning each caregiver and child share the same participant ID, with all caregiver-reported data nested under the corresponding Child ID. This structure supports longitudinal analyses by enabling straightforward tracking of each child’s data over time without needing to remap caregiver information. It also simplifies multi-birth cases: when a caregiver reports on multiple children, each child is assigned a unique record, so each child's data remains distinct (avoiding complex joins or disambiguation).

## Spanish Translations
All surveys used in the HBCD Study were translated into Spanish by <a href="https://burgtranslations.com/our-services/">BURG Translations</a> and reviewed by the Spanish Language Committee (SLC) to ensure clarity and accessibility for a broad Spanish-speaking population. Instruments from third-party publishers (e.g., Bayley, CDI, BTB, Vineland) were excluded from this process, and the third party's translation was used.
