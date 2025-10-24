<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<thead>
  <tr>
    <th style="width: 30%;">Variable</th>
    <th style="width: 70%;">Description</th>
  </tr>
</thead>
<tbody>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Maternal Age at V01 (MAV01)</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>mother_age_v01</code><br>Birth parent's age - <a href="../../agevariables/#basic-demographics">see details</a>. <i>Source: Admin</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Maternal Age at Delivery (MAD)</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>mother_age_delivery</code><br>Birth parent's age at time of child's delivery - <a href="../../agevariables/#basic-demographics">see details</a>. <i>Source: Admin</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Gestational Age at Delivery (GAD)</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>gestational_age_delivery</code><br>Age of the child at delivery - <a href="../../agevariables/#basic-demographics">see details</a>. <i>Source: Admin</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Child sex</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>sex</code><br>Available for Visit V02 onward (post-birth). <i>Source: Admin</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Child ethnicity</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>child_ethnicity</code><br><a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>-standard ethnicity item. Available for Visit V02 onward (post-birth). <i>Source: Admin</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Child race</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>child_race</code><br><a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>-standard race item. Available for Visit V02 onward (post-birth). <i>Source: Admin</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Child race & ethnicity – multiracial aggregation by Hispanic/non-Hispanic</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>child_ethnoracial_acs_by_multi_ethnicity</code><br>Constructed from <code>child_race</code> and <code>child_ethnicity</code> based on <b>current federal standards.*</b> Multiracial individuals are subcategorized based on whether <i>Hispanic</i> is one of their selected identities. Available for Visit V02 onward (post-birth). <i>Source: Admin</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother ethnicity</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>screen_mother_ethnicity</code><br>Participant response to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item about ethnic identity collected during screening. <i>Source: Admin</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race, multi-categorical</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>screen_mother_race</code><br>Participant response to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item/question about racial identity collected during screening. <i>Source: Admin</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race & ethnicity – multiracial aggregation by Hispanic/non-Hispanic</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>screen_mother_ethnoracial_acs_by_multi_ethnicity</code><br>Constructed from screening race/ethnicity responses based on <b>current federal standards.*</b> Multiracial individuals are subcategorized based on whether <i>Hispanic</i> is one of their selected identities. <i>Source: Admin</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race & ethnicity – multiracial aggregation by Black/non-Black</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>screen_mother_ethnoracial_acs_by_multi_race</code><br>Constructed from screening race/ethnicity responses based on <b>current federal standards.*</b> Multiracial individuals are subcategorized based on whether <i>Black/African American</i> is one of their selected identities. <i>Source: Admin</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race & ethnicity (All of Us standard)</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>rc_mother_ethnoracial_aou_race_ethnicity</code><br>Derived from single <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a> race and ethnicity item scored following <a href="https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards">OMB</a> standards: Anyone identifying as Hispanic/Latino (alone or with another group) is categorized as Hispanic/Latino; all others as non-Hispanic. <i>Source: HBCD Demographics</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race, indicator variables from screening</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>screen_mother_race_multi___{0 - 5}</code><br>Indicator variables from ACS race question:<br>
0 = White<br>
1 = Black or African American<br>
2 = American Indian or Alaskan Native<br>
3 = Asian<br>
4 = Native Hawaiian or other Pacific Islander<br>
5 = Other race<br>
<i>Source: Admin</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race, indicator variables from survey item</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>rc_mother_race___{0 - 7}</code><br>Indicator variables for responses to <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a> combined race and ethnicity question:<br>
0 = American Indian or Alaskan Native<br>
1 = Asian<br>
2 = Black, African American, or African<br>
3 = Hispanic, Latino, or Spanish<br>
4 = Middle Eastern or North African<br>
5 = Native Hawaiian or other Pacific Islander<br>
6 = White<br>
7 = None of these fully describe me<br>
<i>Source: HBCD Demographics</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother education</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>rc_mother_education</code><br>Derived from <code>sed_bm_demo_edu_001</code>. <i>Source: HBCD Demographics</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Total combined household income</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>rc_mother_income</code><br>Derived from <code>sed_bm_demo_income_002</code>. <i>Source: HBCD Demographics</i></td>
</tr>

<tr>
<td style="word-wrap: break-word; white-space: normal;">Recruitment site</td>
<td style="word-wrap: break-word; white-space: normal;">
<code>recruitment_site</code><br>De-identified value reflecting recruitment sites. <i>Source: Admin</i></td>
</tr>

<tr>
<td colspan="2" style="word-wrap: break-word; white-space: normal;">
<b>*Current federal standards:</b> if an individual is identified as Hispanic or Latino based on the response to the ethnicity item, they will be categorized as such, regardless of their race. Individuals who select more than one race are categorized as "multiracial."
</td>
</tr>

</tbody>
</table>