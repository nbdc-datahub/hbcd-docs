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
<p>Some participants reported challenges in answering certain questions, such as those related to race and ethnicity (e.g. options did not capture identity) and occupation (i.e. imperfect option for job type and number of hours).</p> 
</div>

## Details

<p>
<div class="table-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Basic Demographics is a <a href="../../../access/metadata/#exceptions-derived" target="_blank">derived table</a>. See HBCD <a href="../../SED/demo-cg/" target="_blank">Adult</a> and <a href="../../SED/demo-ch/" target="_blank">Child</a> Demographics for full demographics.</span>
</div>
</p>

Basic Demographics is a **derived measure** with information computed from: 

- A subset of **V01 Demographics** (`sed_bm_demo`) Social & Environmental Determinants domain instrument variables 
- **Administrative screening records** collected by HBCD Study staff, as reported by the birth parent, during the enrolment/screening process (e.g. the age and race/ethnicity of the pregnant study participant)

Basic Demographics are **global, visit-agnostic variables** that do not change over time and should be present and consistent across all Visits (V01, V02, etc.). *However*, if only V01 data for a given participant is included in the release (due to ongoing enrollment, participant withdrawal, etc.), then items about the child will be missing, as the child is not born until after the V01 visit (all variables about the child are available beginning with V02).


<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th>Construct</th>
        <th>Variable Name</th>
        <th>Source</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Maternal Age at V01 (MAV01)</td>
<td><code>mother_age_v01</code></td>
<td>Admin</td>
<td style="word-wrap: break-word; white-space: normal;">Birth parent's age - <a href="../../agevariables/#basic-demographics">see details</a></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Maternal Age at Delivery (MAD)</td>
<td><code>mother_age_delivery</code></td>
<td>Admin</td>
<td style="word-wrap: break-word; white-space: normal;">Birth parent's age at time of child's delivery - <a href="../../agevariables/#basic-demographics">see details</a></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Gestational Age at Delivery (GAD)</td>
<td><code>gestational_age_delivery</code></td>
<td>Admin</td>
<td style="word-wrap: break-word; white-space: normal;">Age of the child at delivery - <a href="../../agevariables/#basic-demographics">see details</a></td>
</tr>
<tr>
<td>Child sex</td>
<td><code>sex</code></td>
<td>Admin</td>
<td style="word-wrap: break-word; white-space: normal;"><span class="tooltip tooltip-left"><i>Visit V02 onward</i><span class="tooltiptext">Data are not collected prior to birth, i.e. at the prenatal V01 visit, and will be available starting at visit V02</span></span></td>
</tr>
<tr>
<td>Child ethnicity</td>
<td><code>child_ethnicity</code></td>
<td>Admin</td>
<td style="word-wrap: break-word; white-space: normal;"><a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>-standard ethnicity item. Available for Visit V02 onward (post-birth)</td>
</tr>
<tr>
<td>Child race</td>
<td><code>child_race</code></td>
<td>Admin</td>
<td style="word-wrap: break-word; white-space: normal;"><a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>-standard race item. Available for Visit V02 onward (post-birth).</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Child race & ethnicity - multiracial aggregation by Hispanic/non-Hispanic</td>
<td><code>child_ethnoracial_acs_by_multi_ethnicity</code></td>
<td>Admin</td>
<td style="word-wrap: break-word; white-space: normal;">Constructed from <code>child_race</code> and <code>child_ethnicity</code> based on <b>current federal standards.*</b> Multiracial individuals are subcategorized based on whether <i>Hispanic</i> is one of their selected identities. Available for Visit V02 onward (post-birth)</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother ethnicity</td>
<td style="word-wrap: break-word; white-space: normal;"><code>screen_mother_ethnicity</code></td>
<td>Admin</td>
<td style="word-wrap: break-word; white-space: normal;">Participant response to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item about ethnic identity collected during screening.</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race, multi-categorical</td>
<td style="word-wrap: break-word; white-space: normal;"><code>screen_mother_race</code></td>
<td>Admin</td>
<td style="word-wrap: break-word; white-space: normal;">Participant response to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item/question about racial identity collected during screening.</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race & ethnicity - multiracial aggregation by Hispanic/non-Hispanic</td>
<td><code>screen_mother_ethnoracial_acs_by_multi_ethnicity</code></td>
<td>Admin</td>
<td style="word-wrap: break-word; white-space: normal;">Constructed from screening race/ethnicity responses based on <b>current federal standards.*</b> Multiracial individuals are subcategorized based on whether <i>Hispanic</i> is one of their selected identities.</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race & ethnicity - multiracial aggregation by Black/non-Black</td>
<td><code>screen_mother_ethnoracial_acs_by_multi_race</code></td>
<td>Admin</td>
<td style="word-wrap: break-word; white-space: normal;">Constructed from screening race/ethnicity responses based on <b>current federal standards.*</b> Multiracial individuals are subcategorized based on whether <i>Black/African American</i> is one of their selected identities.</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race and ethnicity</td>
<td style="word-break: break-all; white-space: normal;"><code>rc_mother_ethnoracial_aou_race_ethnicity</code></td>
<td>V01 Demo</td>
<td style="word-wrap: break-word; white-space: normal;">Derived from single <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a> race and ethnicity item scored following <a href="https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards">OMB</a> standards: Anyone identifying as Hispanic/Latino (alone or with another group) is categorized as Hispanic/Latino; all others as non-Hispanic.</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race, indicator variables from screening</td>
<td style="word-break: break-all; white-space: normal;"><code>screen_mother_race_multi___{0 - 5}</code></td>
<td>Admin</td>
<td style="word-wrap: break-word; white-space: normal;">Indicator variables from ACS race question:<br>
0 = White<br>
1 = Black or African American<br>
2 = American Indian or Alaskan Native<br>
3 = Asian<br>
4 = Native Hawaiian or other Pacific Islander<br>
5 = Other race</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race, indicator variables from survey item</td>
<td style="word-wrap: break-word; white-space: normal;"><code>rc_mother_race___{0 - 7}</code></td>
<td>V01 Demo</td>
<td style="word-wrap: break-word; white-space: normal;">Indicator variables for responses to <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a> combined race and ethnicity question:<br>
0 = American Indian or Alaskan Native<br>
1 = Asian<br>
2 = Black, African American, or African<br>
3 = Hispanic, Latino, or Spanish<br>
4 = Middle Eastern or North African<br>
5 = Native Hawaiian or other Pacific Islander<br>
6 = White<br>
7 = None of these fully describe me</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother education</td>
<td style="word-wrap: break-word; white-space: normal;"><code>rc_mother_education</code></td>
<td>V01 Demo</td>
<td style="word-wrap: break-word; white-space: normal;">Derived from <code>sed_bm_demo_edu_001</code></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Total combined household income</td>
<td style="word-wrap: break-word; white-space: normal;"><code>rc_mother_income</code></td>
<td>V01 Demo</td>
<td style="word-wrap: break-word; white-space: normal;">Derived from <code>sed_bm_demo_income_002</code></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Recruitment site</td>
<td style="word-wrap: break-word; white-space: normal;"><code>recruitment_site</code></td>
<td>Admin</td>
<td style="word-wrap: break-word; white-space: normal;">De-identified value reflecting recruitment sites</td>
</tr>
<tr>
<td colspan="4" style="word-wrap: break-word; white-space: normal;">
<b>*Current federal standards:</b> if an individual is identified as Hispanic or Latino based on the response to the ethnicity item, they will be categorized as such, regardless of their race. Individuals who select more than one race are categorized as "multiracial."</td>
</tr>
</tbody>
</table>

