<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
</style>

# Basic Demographics

{{ alert_warning(instruments.basic_demo) }}
{{ data_warning(instruments.basic_demo) }}
{{ issues_banner() }}

---  

{{ instrument_description(instruments.basic_demo) }}

---

<!-- ## Age, Sex, & Other Variables -->

{{ suppx(instruments.basic_demo, "1") }}

<table class="compact-table-no-vertical-lines static-dynamic-tables">
<thead>
<tr>
  <th>Construct</th>
  <th>Variable</th>
  <th>Visit</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Maternal age at V01</td>
<td>mother_age_v01</td>
<td>V01</td>
<td>
Birth parent's age in years (2 decimal places) at V01 visit<br>
<i>Formula: Number of whole months (rounded down) divided by 12</i>
</td>
</tr>
<tr>
<td>Maternal age at delivery</td>
<td>mother_age_delivery</td>
<td>V02</td>
<td>
Birth parent's age in years (2 decimal places) at time of child's delivery<br>
<i>Formula: Number of whole months (rounded down) divided by 12</i>
</td>
</tr>
<tr>
<td>Gestational age at delivery</td>
<td>gestational_age_delivery</td>
<td>V02</td>
<td>Age of child at delivery
<br>
<i>Formula: Whole weeks (rounded down) between LMP and child's DOB</i>
</td>
</tr>
<tr>
  <td>Child sex</td>
  <td>sex</td> 
  <td>V02</td>
  <td>Derived from administrative records</td>
</tr>
<tr>
  <td>Birth mother education</td>
  <td>rc_mother_education</td> 
  <td>V01</td>
  <td>Derived from the Demographics Form (sed_bm_demo_edu_001)</td>
</tr>
<tr>
  <td>Total household income</td>
  <td>rc_mother_income</td>
  <td>V01</td>
  <td>Derived from the Demographics Form (sed_bm_demo_income_002)</td>
</tr>
<tr>
  <td>Recruitment site</td>
  <td>recruitment_site</td> 
  <td>V01</td>
  <td>De-identified site ID derived from administrative records</td>
</tr>
</tbody>
</table>

---

<!-- ## Race & Ethnicity - ACS/Administrative Records -->

{{ suppx(instruments.basic_demo, "2") }}

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
<td>Child ethnicity</td>
<td>child_ethnicity</td>
<td>V02</td>
<td>Standard ACS ethnicity item</td>
</tr>
<tr>
<td>Child race</td>
<td>child_race</td>
<td>V02</td>
<td>Standard ACS race item</td>
</tr>
<tr>
<td>Child race/ethnicity, multiracial aggregation by ethnicity</td>
<td>child_ethnoracial_acs_by_multi_ethnicity</td>
<td>V02</td>
<td>Child combined race and ethnicity constructed from ACS items, with multiracial aggregation by Hispanic distinction</td>
</tr>
<tr>
<td>Birth mother race</td>
<td>screen_mother_race</td>
<td>V01</td>
<td>Standard ACS race item</td>
</tr>
<tr>
<td>Birth mother ethnicity</td>
<td>screen_mother_ethnicity</td>
<td>V01</td>
<td>Standard ACS ethnicity item</td>
</tr>
<tr>
  <td>Mother race indicator<br>variables (0–5)</td>
  <td>screen_mother_race_<br>multi___{0–5}</td>
  <td>V01</td>
  <td>
    Indicator variables from ACS race item:<br>
    0 = <b>White<br>
    1 = <b>Black or African American</b><br>
    2 = <b>American Indian or Alaska Native</b><br>
    3 = <b>Asian</b><br>
    4 = <b>Native Hawaiian or Other Pacific Islander</b><br>
    5 = <b>Other race</b>
  </td>
</tr>
<tr>
<td>Mother race/ethnicity, multiracial aggregation by ethnicity</td>
<td>screen_mother_ethnoracial_acs_by_multi_ethnicity</td>
<td>V01</td>
<td>Maternal combined race and ethnicity constructed from ACS items, with multiracial aggregation by Hispanic distinction</td>
</tr>
<tr>
<td>Mother race/ethnicity, multiracial aggregation by race</td>
<td>screen_mother_ethnoracial_acs_by_multi_race</td>
<td>V01</td>
<td>Maternal combined race and ethnicity constructed from ACS items, with multiracial aggregation by Black/non-Black distinction</td>
</tr>
</tbody>
</table>

---

<!-- ## Race & Ethnicity - All of US -->
{{ suppx(instruments.basic_demo, "3") }}

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
  <td>Mother race indicators (0–7)</td>
  <td>rc_mother_race___{0–7}</td>
  <td>V01</td>
  <td>
    AOU item race indicators:<br>
    0=American Indian or Alaska Native<br>
    1=Asian<br>
    2=Black, African American, or African<br>
    3=Hispanic, Latino, or Spanish<br>
    4=Middle Eastern or North African<br>
    5=Native Hawaiian or Other Pacific Islander<br>
    6=White<br>
    7=None of these fully describe me</b>
  </td>
</tr>
<tr>
  <td>Mother race/ethnicity</td>
  <td>rc_mother_ethnoracial_aou_race_ethnicity</td>
  <td>V01</td>
  <td>Aggregated maternal race/ethnicity constructed from AOU item. Participants are classified as either Hispanic or Non-Hispanic ({Asian|Black|White}).
</td>
</tr>
</tbody>
</table>

{{ references(instruments.basic_demo) }}
