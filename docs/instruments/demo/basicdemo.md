<p style="font-size: 1.2em;">🚧 UNDER CONSTRUCTION TO BE UPDATED FOR R2.0</p>

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

Basic Demographics is a **derived measure** with information computed from the following sources: 

- **Administrative screening records** collected by HBCD Study staff, as reported by the birth parent, during the enrolment/screening process (e.g. the age and race/ethnicity of the pregnant study participant)
- A subset of <a href="../../SED/demo-cg/" target="_blank">HBCD Demographics instrument (Adult)</a> (`sed_bm_demo`) Social & Environmental Determinants domain instrument variables 

Basic Demographics are **global, visit-agnostic variables** that do not change over time and should be present and consistent across all Visits (V01, V02, etc.) for the adult/caregiver and beginning at Visit V02 for the child (post-birth). *However*, if only V01 data for a given participant is included in the release (due to ongoing enrollment, participant withdrawal, etc.), then items about their child will be missing, as the child is not born until after the V01 visit.

### Age, Sex, & Other Variables

<p style="font-size: 0.9em; color: #555;">
<i class="fa-solid fa-baby"></i>&nbsp;= Variable refers to the child &nbsp;&nbsp;
<span class="pill-badge">V02+</span>&nbsp;= Available beginning Visit V02 (post-birth)
</p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<tfoot><tr><td colspan="3" style="word-wrap: break-word; white-space: normal; padding: 10px 8px 6px 8px;">
  <sup><b>1</b></sup> Years are to 2 decimal places, calculated by dividing the number of whole months (rounded down) by 12</td></tr></tfoot>
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
  <td>Derived from <code>sed_bm_demo_edu_001</code> (HBCD Demographics).</td>
</tr>
<tr>
  <td>Total household income</td>
  <td><code>rc_mother_income</code></td>
  <td>Derived from <code>sed_bm_demo_income_002</code> (HBCD Demographics).</td>
</tr>
<tr>
  <td>Recruitment site</td>
  <td><code>recruitment_site</code></td>
  <td>De-identified site ID derived from administrative records.</td>
</tr>
</tbody>
</table>

<div id="rec-sites" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i style="font-size: 0.9em;" class="fa-solid fa-location-dot"></i></span>
  <span class="text-with-link">
  <span class="text">Recruitment Sites</span>
  <a class="anchor-link" href="#rec-sites" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr style="border-bottom: 2px solid #ccc;">
  <th>Value</th>
  <th>Label</th>
  <th>Site</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>hbcdsite64</td>
<td>Arkansas Children's Hospital (site 1)</td>
</tr>
<tr>
<td>1</td>
<td>hbcdsite02</td>
<td>Arkansas Children's Hospital (site 2 - UAMS)</td>
</tr>
<tr>
<td>2</td>
<td>hbcdsite48</td>
<td>Boston Children's Hospital - Harvard Medical School</td>
</tr>
<tr>
<td>3</td>
<td>hbcdsite95</td>
<td>Cedars Sinai (site 1)</td>
</tr>
<tr>
<td>4</td>
<td>hbcdsite23</td>
<td>Cedars Sinai (site 2 - UCLA)</td>
</tr>
<tr>
<td>5</td>
<td>hbcdsite07</td>
<td>Children's Hospital Los Angeles</td>
</tr>
<tr>
<td>6</td>
<td>hbcdsite09</td>
<td>Children's Hospital of Philadelphia</td>
</tr>
<tr>
<td>7</td>
<td>hbcdsite04</td>
<td>Cincinnati Children's Hospital</td>
</tr>
<tr>
<td>8</td>
<td>hbcdsite20</td>
<td>Emory University School of Medicine</td>
</tr>
<tr>
<td>9</td>
<td>hbcdsite52</td>
<td>Johns Hopkins University</td>
</tr>
<tr>
<td>10</td>
<td>hbcdsite06</td>
<td>New York University</td>
</tr>
<tr>
<td>11</td>
<td>hbcdsite69</td>
<td>Northwestern University</td>
</tr>
<tr>
<td>12</td>
<td>hbcdsite72</td>
<td>Oklahoma State</td>
</tr>
<tr>
<td>13</td>
<td>hbcdsite93</td>
<td>Oregon Health &amp; Science University</td>
</tr>
<tr>
<td>14</td>
<td>hbcdsite78</td>
<td>Pennsylvania State University (site 1 - UP)</td>
</tr>
<tr>
<td>15</td>
<td>hbcdsite53</td>
<td>Pennsylvania State University (site 2 - COM)</td>
</tr>
<tr>
<td>16</td>
<td>hbcdsite79</td>
<td>University of Alabama at Birmingham (site 1)</td>
</tr>
<tr>
<td>17</td>
<td>hbcdsite28</td>
<td>University of Alabama at Birmingham (site 2 - UAT)</td>
</tr>
<tr>
<td>18</td>
<td>hbcdsite77</td>
<td>University of California San Diego</td>
</tr>
<tr>
<td>19</td>
<td>hbcdsite92</td>
<td>University of Maryland</td>
</tr>
<tr>
<td>20</td>
<td>hbcdsite70</td>
<td>University of Minnesota</td>
</tr>
<tr>
<td>21</td>
<td>hbcdsite84</td>
<td>University of New Mexico</td>
</tr>
<tr>
<td>22</td>
<td>hbcdsite29</td>
<td>University of North Carolina (site 1)</td>
</tr>
<tr>
<td>23</td>
<td>hbcdsite27</td>
<td>University of North Carolina (site 2 - Wake Forest)</td>
</tr>
<tr>
<td>24</td>
<td>hbcdsite67</td>
<td>University of Vermont</td>
</tr>
<tr>
<td>25</td>
<td>hbcdsite57</td>
<td>University of Wisconsin</td>
</tr>
<tr>
<td>26</td>
<td>hbcdsite35</td>
<td>Vanderbilt University</td>
</tr>
<tr>
<td>27</td>
<td>hbcdsite26</td>
<td>Washington University in St. Louis</td>
</tr>
<tr>
<td>28</td>
<td>hbcdsite43</td>
<td>Virginia Tech</td>
</tr>
<tr>
<td>29</td>
<td>hbcdsite42</td>
<td>University of Florida</td>
</tr>
</tbody>
</table>
</div>

### Race & Ethnicity Variables

Race and ethnicity variables are either computed from administrative records collected during screening using the American Community Survey ([ACS](https://www.census.gov/programs-surveys/acs.html)), or a single All of Us (<a href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">AOU</a>) race and ethnicity item collected as part of the <a href="../../SED/demo-cg/" target="_blank">HBCD Demographics</a> instrument.

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
  <td>Standard ACS race item. <span class="pill-badge">V02+</span></td>
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
<p>ACS combined variables are constructed from ACS race/ethnicity screening items following current federal standards:</p>
<ul>
<li>Participants identifying as <em>Hispanic or Latino</em> are categorized as such regardless of race.</li>
<li>Individuals selecting more than one race are categorized as <strong>multiracial</strong>.</li>
<li>Multiracial individuals are subcategorized by <strong>ethnicity</strong> (<em>Hispanic</em> vs. <em>non-Hispanic</em>)
  and <strong>race</strong> (<em>Black/African American</em> vs. <em>non-Black/African American</em>).</li>
</ul>
</div>
<p></p>

#### AOU-Derived Variables
*Computed from a single All of Us (<a href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">AOU</a>) race and ethnicity item collected as part of the <a href="../../SED/demo-cg/" target="_blank">HBCD Demographics</a> instrument.*

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

