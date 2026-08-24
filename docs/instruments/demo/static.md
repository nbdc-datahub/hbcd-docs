<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
</style>

# Static Table

{{ readme_summary(instruments.static) }}
{{ alert_warning(instruments.static) }}
{{ data_warning(instruments.static) }}
{{ issues_banner() }}

---  

{{ instrument_description(instruments.static) }}

<!-- ## Age, Sex, & Other Variables  -->
{{ suppx(instruments.static, "1") }}


<!-- HARD-CODED TABLE -->

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
  <td>Recruitment site</td>
  <td>recruitment_site</td> 
  <td>V01</td>
  <td>Site ID derived from administrative records</td>
</tr>
<tr>
  <td>Area Deprivation Index</td>
  <td>adi_national_prcnt</td> 
  <td></td>
  <td>Geocoded in national percentile in ADI 1% – 100%</td>
</tr>
<tr>
  <td>Birth mother education</td>
  <td>rc_mother_education</td> 
  <td>V01</td>
  <td>Highest level of school completed derived from the Demographics Form</td>
</tr>
<tr>
  <td>Household income</td>
  <td>rc_mother_income</td>
  <td>V01</td>
  <td>Household income derived from the Demographics Form</td>
</tr>
</tbody>
</table>

---

<!-- ## Race & Ethnicity - ACS/Administrative Records -->
{{ suppx(instruments.static, "2") }}

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
<td>Child race indicators (0-5)</td>
<td>acs_child_race_multi___{0 - 5}</td>
<td>V01</td>
<td>Child race collected at V01 pregnancy check-in</td>
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
{{ suppx(instruments.static, "3") }}

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
<tr>
  <td>Child race indicators (0–7)</td>
  <td>rc_child_race___{0–7}</td>
  <td>V04</td>
  <td>AOU item race indicators (values mirror Mother race indicators)</td>
</tr>
</tbody>
</table>
</tbody>
</table>


{{ references(instruments.static) }}





<!-- Unless stated otherwise in the description, the following variables such as sex and age are computed from administrative records collected during screening. Variables such as education and income are derived from the [Demographics](../../instruments/SED/demo-cg.md) instrument (Adult Form), noted in the description. -->


<!-- Race and ethnicity variables are computed from [ACS](https://www.census.gov/programs-surveys/acs.html) race and ethnicity items derived from administrative records collected during screening. Combined race and ethnicity variables are constructed following current federal standards. Participants who identify as **Hispanic or Latino** are categorized as `Hispanic`, regardless of race. Participants who select more than one race are categorized as **Multiracial**, with aggregation performed by either **ethnicity** based on Hispanic identity (*Multiracial (Hispanic)* or *Multiracial (non-Hispanic)*) or **race** based on Black/African American identity (*Multiracial (Black)* or *Multiracial (non-Black)*). -->


<!-- A second set of race and ethnicity variables are computed from a single All of Us (<a href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations">AOU</a>) race/ethnicity item collected as part of the <a href="../../../instruments/SED/demo-cg/">Demographics</a> instrument. For AOU-derived variables, combined race and ethnicity variables are constructed following [OMB](https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards) standards: Participants who identify as Hispanic/Latino (alone or with another group) are categorized as *Hispanic or Latino*; all others are categorized as non-Hispanic (*Non-Hispanic {Asian|Black|White}*). -->