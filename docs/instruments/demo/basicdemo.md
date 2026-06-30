<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>

# Basic Demographics

{{ readme(instruments.basic_demo) }}
{{ alert_warning(instruments.basic_demo) }}
{{ issues_banner_macro() }}

---

Basic Demographics is a **derived measure** with information computed from the following sources: 

- **Administrative screening records** collected by HBCD Study staff, as reported by the birth parent, during the enrolment/screening process (e.g. the age and race/ethnicity of the pregnant study participant)
- **Demographics** instruments (Social & Environmental Determinants), including <a href="../../SED/demo-cg/" target="_blank">Adult</a> (`sed_bm_demo`) and <a href="../../SED/demo-ch/" target="_blank">Child</a> (`sed_ch_demo`)

Basic Demographics includes global, visit-agnostic variables that do not change over time and should be consistent across all visits for the adult/caregiver and beginning at Visit 2 for the child (post-birth). Note that if only V01 data for a given adult participant is included in the release (due to ongoing enrollment, participant withdrawal, etc.), then items about their child will be missing, as the child is not born until after the V01 visit.

---

<p style="text-align: center; margin-bottom: 0; padding-bottom: 0;">
<span class="pill-badge" style="font-size: 0.8em;">V02+</span>&nbsp;= Child-specific, available Visit 2 onward (post-birth)</p>

### Age Variables 

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
  <th style="width: 25%;">Construct</th>
  <th>Variable Name</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Maternal Age at V01</td>
  <td><code>mother_age_v01</code></td>
  <td>
    <ul>
      <li>Birth parent's age in years (2 decimal places) at V01 visit</li>
      <li>Calculated by dividing the number of whole months (rounded down) by 12</li>
      <li>Derived from administrative records</li>
    </ul>
  </td>
</tr>
<tr>
  <td>Maternal Age at Delivery</td>
  <td><code>mother_age_delivery</code></td>
  <td>
    <ul>
      <li>Birth parent's age in years (2 decimal places) at time of their child's delivery</li>
      <li>Calculated by dividing the number of whole months (rounded down) by 12</li>
      <li>Derived from administrative records</li>
    </ul>
  </td>
</tr>
<tr>
<td>Gestational Age at Delivery <span class="pill-badge" style="font-size: 0.8em;">V02+</span></td>
  <td><code>gestational_age_delivery</code></td>
  <td>
    <ul>
      <li>Age of child at delivery</li>
      <li>Calculated as: # whole weeks (rounded down) between <span class="tooltip tooltip-top">LMP<span class="tooltiptext">First day of the birth parent's last menstrual period</span></span> and child's DOB</li>
      <li>Derived from administrative records</li>
    </ul>
  </td>
</tr>
</tbody>
</table>

### Sex & Other Variables

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
  <th>Construct</th>
  <th>Variable Name</th>
  <th>Description / Details</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Child sex &nbsp; <span class="pill-badge" style="font-size: 0.8em;">V02+</span></td>
  <td><code>sex</code></td>
  <td>Derived from administrative records.</td>
</tr>
<tr>
  <td>Mother education</td>
  <td><code>rc_mother_education</code></td>
  <td>Derived from <code>sed_bm_demo_edu_001</code> (<i><a href="../../SED/demo-cg/" target="_blank">Demographics</a></i>) at V01</td>
</tr>
<tr>
  <td>Total household income</td>
  <td><code>rc_mother_income</code></td>
  <td>Derived from <code>sed_bm_demo_income_002</code> (<i><a href="../../SED/demo-cg/" target="_blank">Demographics</a></i>) at V01</td>
</tr>
<tr>
  <td>Recruitment site</td>
  <td><code>recruitment_site</code></td>
  <td>De-identified site ID derived from administrative records.</td>
</tr>
</tbody>
</table>

### Race & Ethnicity Variables

Race and ethnicity variables are either computed from administrative records collected during screening using the American Community Survey ([ACS](https://www.census.gov/programs-surveys/acs.html)), or a single All of Us (<a href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">AOU</a>) race and ethnicity item collected as part of the <a href="../../SED/demo-cg/" target="_blank">Demographics</a> instrument.

#### ACS-Derived Variables
*Race and ethnicity variables computed from administrative records collected during screening using the [ACS](https://www.census.gov/programs-surveys/acs.html).*

<table class="compact-table-no-vertical-lines">
<thead>
  <tr>
    <th>Construct</th>
    <th>Variable Name</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
<tr>
  <td>Child ethnicity &nbsp; <span class="pill-badge" style="font-size: 0.8em;">V02+</span></td>
  <td><code>child_ethnicity</code></td>
  <td>Standard ACS ethnicity item</td>
</tr>
<tr>
  <td>Child race &nbsp; <span class="pill-badge" style="font-size: 0.8em;">V02+</span></td>
  <td><code>child_race</code></td>
  <td>Standard ACS race item</td>
</tr>
<tr>
  <td>Child race & ethnicity– multiracial aggregation by ethnicity &nbsp; <span class="pill-badge" style="font-size: 0.8em;">V02+</span></td>
  <td><code>child_ethnoracial_<br>acs_by_multi_ethnicity</code></td>
  <td>Derived from ACS race/ethnicity screening responses, with multiracial individuals subcategorized by <b>ethnicity</b> - see <a href="#fedstandards">ACS Combined Race & Ethnicity Logic</a>.</td>
</tr>
<tr style="background-color: #f9f9f9;">
  <td>Mother ethnicity</td>
  <td><code>screen_mother_ethnicity</code></td>
  <td>Standard ACS ethnicity item.</td>
</tr>
<tr style="background-color: #ffffff;">
  <td>Mother race</td>
  <td><code>screen_mother_race</code></td>
  <td>Sandard ACS race item.</td>
</tr>
<tr style="background-color: #f9f9f9;">
  <td>Mother race &amp; ethnicity<br>– multiracial aggregation by ethnicity</td>
  <td><code>screen_mother_ethnoracial_<br>acs_by_multi_ethnicity</code></td>
  <td>Derived from ACS race/ethnicity screening responses, with multiracial individuals subcategorized by <b>ethnicity</b> - see <a href="#fedstandards">ACS Combined Race & Ethnicity Logic</a>.</td>
</tr>
<tr style="background-color: #ffffff;">
  <td>Mother race &amp; ethnicity<br>– multiracial aggregation by race</td>
  <td><code>screen_mother_ethnoracial_<br>acs_by_multi_race</code></td>
    <td>Derived from ACS race/ethnicity screening responses, with multiracial individuals subcategorized by <b>race</b> - see <a href="#fedstandards">ACS Combined Race & Ethnicity Logic</a>.</td>
</tr>
<tr style="background-color: #f9f9f9;">
  <td>Mother race indicator<br>variables (0–5)</td>
  <td><code>screen_mother_race_<br>multi___{0–5}</code></td>
  <td>
    Indicator variables from ACS race item:<br>
    0 = <b>White</b><br>
    1 = <b>Black or African American</b><br>
    2 = <b>American Indian or Alaska Native</b><br>
    3 = <b>Asian</b><br>
    4 = <b>Native Hawaiian or Other Pacific Islander</b><br>
    5 = <b>Other race</b>
  </td>
</tr>
</tbody>
</table>

<div id="fedstandards" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i style="font-size: 0.9em;" class="fa fa-calculator"></i></span>
  <span class="text-with-link">
  <span class="text">ACS Combined Race & Ethnicity Logic</span>
  <a class="anchor-link" href="#fedstandards" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><b>ACS combined variables are constructed from ACS race and ethnicity screening items following current federal standards:</b></p>
<ul>
<li>Participants who identify as <b>Hispanic or Latino</b> under ethnicity are categorized as <i>Hispanic</i> regardless of race.</li>
<li>Individuals selecting more than one race are categorized as <b>Multiracial</b> and subcategorized by <b>ethnicity</b> and <b>race</b> (<code>*_ethnoracial_acs_by_multi_&lt;ethnicity/race&gt;</code>):
    <ul>
    <li><b>By ethnicity</b>: based on Hispanic identity as <i>Multiracial (Hispanic)</i> or <i>Multiracial (non-Hispanic)</i></li>
    <li><b>By race</b>: based on Black/African American identity as <i>Multiracial (Black)</i> or <i>Multiracial (non-Black)</i></li>
    </ul>
    </li>
</ul>
<p><b>Value Labels for Child/Mother ACS Race, Ethnicity, & Combined Race & Ethnicity<b>*</b> Variables:</b></p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tfoot><tr><td colspan="4"><b>*</b> <i>Note: combined variables for the Child currently only include multiracial aggregation by <b>ethnicity</b>.</i></td></tr></tfoot>
<thead>
  <tr>
    <th>Value</th>
    <th>Ethnicity</th>
    <th>Race</th>
    <th>Race & ethnicity– multiracial aggregation by ethnicity/race</th>
  </tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">0</td>
<td>Hispanic</td>
<td>White</td>
<td>Hispanic</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td>Non-Hispanic</td>
<td>Black or African American</td>
<td>White (non-Hispanic)</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td>Unknown</td>
<td>American Indian or Alaskan Native</td>
<td>Asian/Pacific Islander (non-Hispanic)</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td>&nbsp;</td>
<td>Asian</td>
<td>Black (non-Hispanic)</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td>&nbsp;</td>
<td>Native Hawaiian or other Pacific Islander</td>
<td><i>By ethnicity:</i> Multiracial (Hispanic);<br><i>By race:</i> Multiracial (Black)</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td>&nbsp;</td>
<td>Two or More Races</td>
<td><i>By ethnicity:</i> Multiracial (non-Hispanic);<br><i>By race:</i> Multiracial (non-Black)</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td>&nbsp;</td>
<td>Other race</td>
<td>Other (non-Hispanic)</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td>&nbsp;</td>
<td>Unknown</td>
<td>Unknown</td>
</tr>
</tbody>
</table>
</div>
<p></p>

#### AOU-Derived Variables
*Computed from a single All of Us (<a href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">AOU</a>) race and ethnicity item collected as part of the <a href="../../SED/demo-cg/" target="_blank">Demographics</a> instrument.*

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead>
  <tr style="background-color: #f8f9f9;">
    <th style="width: 20%;">Construct</th>
    <th style="width: 20%;">Variable Name</th>
    <th style="width: 60%;">Description / Details</th>
  </tr>
</thead>
<tbody>
<tr style="background-color: #ffffff;">
  <td>Mother race &amp; ethnicity</td>
  <td><code>rc_mother_ethnoracial_<br>aou_race_ethnicity</code></td>
  <td>
    Derived from the single All of Us (<a href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">AOU</a>) 
    race and ethnicity item, scored following 
    <a href="https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards" target="_blank">OMB</a> standards:
    <i>Anyone identifying as Hispanic/Latino (alone or with another group) is categorized as Hispanic/Latino; all others are non-Hispanic.</i>
  </td>
</tr>
<tr style="background-color: #f9f9f9;">
  <td>Mother race indicator<br>variables (0–7)</td>
  <td><code>rc_mother_race___{0–7}</code></td>
  <td>
    Indicator variables for AOU combined race/ethnicity item:<br>
    0 = <b>American Indian or Alaska Native</b><br>
    1 = <b>Asian</b><br>
    2 = <b>Black, African American, or African</b><br>
    3 = <b>Hispanic, Latino, or Spanish</b><br>
    4 = <b>Middle Eastern or North African</b><br>
    5 = <b>Native Hawaiian or Other Pacific Islander</b><br>
    6 = <b>White</b><br>
    7 = <b>None of these fully describe me</b>
  </td>
</tr>
</tbody>
</table>

