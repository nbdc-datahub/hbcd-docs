<p style="font-size: 1.2em;">🚧 UNDER CONSTRUCTION TO BE UPDATED FOR R2.0 - <i style="color: red;">per Natalie: Basic Demo will be transitioned into "Static" and "Dynamic" tables</i></p>

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

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</i></span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Some participants reported challenges in answering certain questions, such as those related to race and ethnicity (e.g. options did not capture identity).</p> 
</div>

## Details

<p>
<div class="table-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Basic Demographics is a <a href="../../../access/metadata/#exceptions-derived" target="_blank">derived table</a>. See HBCD <a href="../../SED/demo-cg/" target="_blank">Adult</a> and <a href="../../SED/demo-ch/" target="_blank">Child</a> Demographics for full demographics.</span>
</div>
</p>

Basic Demographics is a **derived measure** with information computed from: 

- **Administrative screening records** collected by HBCD Study staff, as reported by the birth parent, during the enrolment/screening process (e.g. the age and race/ethnicity of the pregnant study participant)
- A subset of <a href="../../SED/demo-cg/" target="_blank">HBCD Demographics instrument (Adult)</a> (`sed_bm_demo`) Social & Environmental Determinants domain instrument variables 

Basic Demographics are **global, visit-agnostic variables** that do not change over time and should be present and consistent across all Visits (V01, V02, etc.) for the adult/caregiver and beginning at Visit V02 for the child (post-birth). *However*, if only V01 data for a given participant is included in the release (due to ongoing enrollment, participant withdrawal, etc.), then items about their child will be missing, as the child is not born until after the V01 visit. 

### Age, Sex, & Other Variables

<table class="compact-table-no-vertical-lines">
<thead>
  <tr>
    <th>Construct</th>
    <th>Variable Name</th>
    <th>Description/Details</th>
  </tr>
</thead>
<tbody>
<tr>
<td>Maternal Age at {V01/Delivery}</td>
<td><code>mother_age_v01</code><br><code>mother_age_delivery</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Birth parent's age at V01 visit (MAV01)/delivery (MAD).<br>
  <i>See <a href="../../agevariables/#basic-demographics" target="_blank">Age Variables <i style="font-size: 0.8em;" class="fa-solid fa-arrow-up-right-from-square"></i></a> for full documentation of age fields.</td>
</tr>
<tr>
<td>Gestational Age at Delivery <i class="fa-solid fa-baby"></i></td>
<td><code>gestational_age_delivery</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Child's gestational age at delivery (GAD). <span class="pill-badge">V02+</span><br>
  <i>See <a href="../../agevariables/#basic-demographics" target="_blank">Age Variables <i style="font-size: 0.8em;" class="fa-solid fa-arrow-up-right-from-square"></i></a> for full documentation of age fields.</i></td>
</tr>
<tr>
<td>Child sex <i class="fa-solid fa-baby"></i></td>
<td><code>sex</code></td>
<td>Derived from admin records. <span class="pill-badge">V02+</span></td>
</tr>
<tr>
<td>Mother education</td>
<td><code>rc_mother_education</code></td>
<td>Derived from <code>sed_bm_demo_edu_001</code> (HBCD Demographics).</td>
</tr>
<tr><td>Total household income</td><td><code>rc_mother_income</code></td><td>Derived from <code>sed_bm_demo_income_002</code> (HBCD Demographics).</td></tr>
<tr><td>Recruitment site</td><td><code>recruitment_site</code></td><td style="word-wrap: break-word; white-space: normal;">De-identified site ID derived from administrative records.</td></tr>
</tbody>
</table>
<span class="pill-badge" style="font-size: 0.75em;">V02+</span><span> - <i>Variables about the child are available beginning visit V02, post-birth (V01 is prenatal).</i></span>

### ACS Race & Ethnicity Variables 

The following variables are derived from administrative records collected during screening using the American Community Survey [ACS](https://www.census.gov/programs-surveys/acs.html).     
<p></p>

<table class="compact-table-no-vertical-lines">
<thead>
</tr>
  <tr>
    <th style="width: 20%;">Construct</th>
    <th style="width: 20%;">Variable Name</th>
    <th style="width: 40%;">Description/Details</th>
  </tr>
</thead>
<tbody>
<tr>
<td>Child ethnicity <i class="fa-solid fa-baby"></i></td>
<td><code>child_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">ACS ethnicity item. <span class="pill-badge">V02+</span></td>
</tr>
<tr>
<td>Child race <i class="fa-solid fa-baby"></i></td>
<td><code>child_race</code></td>
<td style="word-wrap: break-word; white-space: normal;">ACS race item. <span class="pill-badge">V02+</span></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Child race & ethnicity- multiracial aggregation by ethnicity <i class="fa-solid fa-baby"></i></td>
<td><code>child_ethnoracial_<br>acs_by_multi_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">Constructed from screening race/ethnicity responses following <a href="#fedstandards">current federal standards <i class="fa fa-circle-info"></i></a>, with multiracial individuals subcategorized by ethnicity. <span class="pill-badge">V02+</span></td>
</tr>
<tr>
<td>Mother ethnicity</td>
<td><code>screen_mother_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">Standard ACS ethnicity item.</td>
</tr>
<tr>
<td>Mother race</td>
<td><code>screen_mother_race</code></td>
<td style="word-wrap: break-word; white-space: normal;">Standard ACS race item.</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race & ethnicity- multiracial aggregation by ethnicity</td>
<td style="word-wrap: break-word; white-space: normal;"><code>screen_mother_ethnoracial_<br>acs_by_multi_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">Constructed from screening race/ethnicity responses following <a href="#fedstandards">current federal standards <i class="fa fa-circle-info"></i></a>, with multiracial individuals subcategorized by ethnicity.</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race & ethnicity- multiracial aggregation by race</td>
<td><code>screen_mother_ethnoracial_<br>acs_by_multi_race</code></td>
<td style="word-wrap: break-word; white-space: normal;">Constructed from screening race/ethnicity responses following <a href="#fedstandards">current federal standards <i class="fa fa-circle-info"></i></a>, with multiracial individuals subcategorized by race.</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race indicator variables (0-5)</td>
<td><code>screen_mother_race_multi___{0-5}</code></td>
<td>Indicator variables from ACS race question:<br>
0 = White<br>
1 = Black or African American<br>
2 = American Indian or Alaskan Native<br>
3 = Asian<br>
4 = Native Hawaiian or other Pacific Islander<br>
5 = Other race</td>
</tr>
</tbody>
</table>
<span class="pill-badge" style="font-size: 0.75em;">V02+</span><span> - <i>Variables about the child are available beginning visit V02, post-birth (V01 is prenatal).</i></span>

<table id="fedstandards" class="compact-table-no-vertical-lines" style="border: 2px solid #006c6c5b; border-radius: 8px; border-collapse: collapse; font-size: 1.0em;">
<tbody>
<tr><td style="word-wrap: break-word; white-space: normal;">
<i class="fa fa-circle-info" style="color: #0066cc;"></i> <span style="font-size: 1.1em;"><b>Current federal standards</b> for combining race and ethnicity variables from screening:</span>
  <ul style="margin-top: 5px; margin-bottom: 5px;">
  <li>Participants who identify as <em>Hispanic or Latino</em> in the ACS are categorized as such regardless of their race.</li>
  <li>Individuals who select more than one race are categorized as <strong>multiracial</strong>.</li>
  <li>Multiracial participants are subcategorized by <strong>ethnicity</strong> (<em>Hispanic</em> vs. <em>non-Hispanic</em>) and <strong>race</strong> (<em>Black/African American</em> vs. <em>non-Black/African American</em>).</li>
  </ul>
</td></tr>
</tbody>
</table>

### AOU Race & Ethnicity Variables

The following race and ethnicity variables are derived from a single All of US ([AOU](https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations)) race and ethnicity item derived from the <a href="../../SED/demo-cg/" target="_blank">HBCD Demographics instrument (Adult)</a>.

<table class="compact-table-no-vertical-lines">
<thead>
  <tr>
    <th>Construct</th>
    <th>Variable Name</th>
    <th>Description/Details</th>
  </tr>
</thead>
<tbody>
<tr>
<td>Mother race & ethnicity</td>
<td><code>rc_mother_ethnoracial_<br>aou_race_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">
Derived from single All of Us race and ethnicity item scored following <a href="https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards">OMB</a> standards: <i>Anyone identifying as Hispanic/Latino (alone or with another group) is categorized as Hispanic/Latino and all others as non-Hispanic.</i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race, indicator<br>variables from survey item</td>
<td><code>rc_mother_race___{0-7}</code></td>
<td style="word-wrap: break-word; white-space: normal;">
Indicator variables for All of Us combined race/ethnicity question:<br>
    0 = American Indian or Alaskan Native<br>
    1 = Asian<br>
    2 = Black, African American, or African<br>
    3 = Hispanic, Latino, or Spanish<br>
    4 = Middle Eastern or North African<br>
    5 = Native Hawaiian or other Pacific Islander<br>
    6 = White<br>
    7 = None of these fully describe me
</td>
</tr>
</tbody>
</table>
