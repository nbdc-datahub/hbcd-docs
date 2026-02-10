# Basic Demographics Information

<div class="info-block">
  <div class="info-row">
    <div class="info-label"><i class="fa fa-table"></i> Table Name:</div>
    <div class="info-value"><code>sed_basic_demographics</code></div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-tape"></i> Construct:</div>
    <div class="info-value">Derived Demographics</div>
  </div>
</div>

---------------------------------------------

<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Responsible Use Warning</span>
  <a class="anchor-link" href="#alert" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p>When using HBCD data, all data users must agree to responsible use as described in the DUC. When conceptualizing studies, analyzing data, and communicating findings from studies that use variables such as race, ethnicity, country of origin, and socioeconomic data, it is critical to consider strategies to avoid stigmatization of any groups and perpetuating harmful biases.</p> 
<p>Race and ethnicity are collected as a part of the HBCD protocol to reflect social experiences (i.e., representing social constructs), and should not be conceptualized as biological, natural, intrinsic, or fixed categories of people. In addition, researchers sometimes use race/ethnicity variables as a proxy for unmeasured social experiences or environmental exposures. HBCD measures a wide variety of social experiences and environmental exposures. In analyzing HBCD data, race/ethnicity should not be used as a proxy for measured variables.</p>
</div>

## Details

<p>
<div class="table-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Basic Demographics is a <a href="../../../access/metadata/#type_var" target="_blank">derived table</a>. See <a href="../../SED/demo-cg/" target="_blank">Demographics</a> and <a href="../../SED/demo-ch/" target="_blank">Child Demographics</a> instruments for full demographic information.</span>
</div>
</p>

Basic Demographics is a **derived measure** with information computed from the following sources: 

- **Administrative screening records** collected by HBCD Study staff, as reported by the birth parent, during the enrolment/screening process (e.g. the age and race/ethnicity of the pregnant study participant)
- The <a href="../../SED/demo-cg/" target="_blank"><b>Demographics</b></a> instrument (`sed_bm_demo`) within the Social & Environmental Determinants domain 

Basic Demographics are **global, visit-agnostic variables** that do not change over time and should be present and consistent across all Visits (V01, V02, etc.) for the adult/caregiver and beginning at Visit V02 for the child (post-birth). Note that if only V01 data for a given adult participant is included in the release (due to ongoing enrollment, participant withdrawal, etc.), then items about their child will be missing, as the child is not born until after the V01 visit.

### Age, Sex, & Other Variables

<p style="font-size: 0.9em; color: #555;">
<i class="fa-solid fa-baby"></i>&nbsp;= Variable refers to the child &nbsp;&nbsp;
<span class="pill-badge">V02+</span>&nbsp;= Available beginning Visit V02 (post-birth)
</p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<tfoot><tr><td colspan="3" style="word-wrap: break-word; white-space: normal; padding: 10px 8px 6px 8px;">
  <sup><b>1</b></sup> Years are to 2 decimal places, calculated by dividing the number of whole months (rounded down) by 12
  </td></tr></tfoot>
<thead>
<tr style="background-color: #f8f9f9;">
  <th style="width: 20%;">Construct</th>
  <th style="width: 20%;">Variable Name</th>
  <th style="width: 60%;">Description / Details</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Maternal Age at V01 (MAV01)</td>
  <td><code>mother_age_v01</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Birth parent's age in years<sup><b>1</b></sup> at scheduled date of the V01 visit. Derived from administrative records.</td>
</tr>
<tr>
  <td>Maternal Age at Delivery (MAD)</td>
  <td><code>mother_age_delivery</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Birth parent's age in years<sup><b>1</b></sup> at time of their child's delivery. Derived from administrative records.</td>
</tr>
<tr>
  <td><i class="fa-solid fa-baby"></i>&nbsp;Gestational age at delivery (GAD)</td>
  <td><code>gestational_age_delivery</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Time elapsed (whole weeks, rounded down) between the birth parent's <span class="tooltip tooltip-left">LMP<span class="tooltiptext">First day of the birth parent's last menstrual period</span></span> and child's DOB. Derived from administrative records. <span class="pill-badge">V02+</span></td>
</tr>
<tr>
  <td><i class="fa-solid fa-baby"></i>&nbsp;Child sex</td>
  <td><code>sex</code></td>
  <td>Derived from administrative records. <span class="pill-badge">V02+</span></td>
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

<p style="font-size: 0.9em; color: #555;">
<i class="fa-solid fa-baby"></i>&nbsp;= Variable refers to the child &nbsp;&nbsp;
<span class="pill-badge">V02+</span>&nbsp;= Available beginning Visit V02 (post-birth)
</p>

#### ACS-Derived Variables
*Race and ethnicity variables computed from administrative records collected during screening using the [ACS](https://www.census.gov/programs-surveys/acs.html).*

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
  <td><i class="fa-solid fa-baby"></i>&nbsp;Child ethnicity</td>
  <td><code>child_ethnicity</code></td>
  <td>Standard ACS ethnicity item. <span class="pill-badge">V02+</span></td>
</tr>
<tr style="background-color: #f9f9f9;">
  <td><i class="fa-solid fa-baby"></i>&nbsp;Child race</td>
  <td><code>child_race</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Standard ACS race item. <span class="pill-badge">V02+</span></td>
</tr>
<tr style="background-color: #ffffff;">
  <td><i class="fa-solid fa-baby"></i>&nbsp;Child race &amp; ethnicity<br>– multiracial aggregation by ethnicity</td>
  <td><code>child_ethnoracial_<br>acs_by_multi_ethnicity</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Derived from ACS race/ethnicity screening responses, with multiracial individuals subcategorized by <b>ethnicity</b> - see <a href="#fedstandards">ACS Combined Race & Ethnicity Logic</a>. <span class="pill-badge">V02+</span></td>
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
  <td style="word-wrap: break-word; white-space: normal;">Derived from ACS race/ethnicity screening responses, with multiracial individuals subcategorized by <b>ethnicity</b> - see <a href="#fedstandards">ACS Combined Race & Ethnicity Logic</a>.</td>
</tr>
<tr style="background-color: #ffffff;">
  <td>Mother race &amp; ethnicity<br>– multiracial aggregation by race</td>
  <td><code>screen_mother_ethnoracial_<br>acs_by_multi_race</code></td>
    <td style="word-wrap: break-word; white-space: normal;">Derived from ACS race/ethnicity screening responses, with multiracial individuals subcategorized by <b>race</b> - see <a href="#fedstandards">ACS Combined Race & Ethnicity Logic</a>.</td>
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

<div id="fedstandards" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i style="font-size: 0.9em;" class="fa fa-calculator"></i></span>
  <span class="text-with-link">
  <span class="text">ACS Combined Race & Ethnicity Logic</span>
  <a class="anchor-link" href="#fedstandards" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
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
  <td style="word-wrap: break-word; white-space: normal;">
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

