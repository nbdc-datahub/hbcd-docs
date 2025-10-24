<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<thead>
  <tr>
    <th>Variable</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Maternal Age at V01 (MAV01)<br><code>mother_age_v01</code></td>
<td style="word-wrap: break-word; white-space: normal;">Birth parent's age - <a href="../../agevariables/#basic-demographics">see details</a>. <i>Source: Admin</i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Maternal Age at Delivery (MAD)<br><code>mother_age_delivery</code></td>
<td style="word-wrap: break-word; white-space: normal;">Birth parent's age at time of child's delivery - <a href="../../agevariables/#basic-demographics">see details</a>. <i>Source: Admin</i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Gestational Age at Delivery (GAD)<br><code>gestational_age_delivery</code></td>
<td style="word-wrap: break-word; white-space: normal;">Age of the child at delivery - <a href="../../agevariables/#basic-demographics">see details</a>. <i>Source: Admin</i></td>
</tr>
<tr>
<td>Child sex<br><code>sex</code></td>
<td style="word-wrap: break-word; white-space: normal;">Available for Visit V02 onward (post-birth). <i>Source: Admin</i></td>
</tr>
<tr>
<td>Child ethnicity<br><code>child_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;"><a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>-standard ethnicity item. Available for Visit V02 onward (post-birth). <i>Source: Admin</i></td>
</tr>
<tr>
<td>Child race<br><code>child_race</code></td>
<td style="word-wrap: break-word; white-space: normal;"><a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>-standard race item. Available for Visit V02 onward (post-birth). <i>Source: Admin</i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Child race & ethnicity - multiracial aggregation by Hispanic/non-Hispanic<br><code>child_ethnoracial_acs_by_multi_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">Constructed from <code>child_race</code> and <code>child_ethnicity</code> based on <b>current federal standards.*</b> Multiracial individuals are subcategorized based on whether <i>Hispanic</i> is one of their selected identities. Available for Visit V02 onward (post-birth). <i>Source: Admin</i></td>
</tr>
<tr>
<td>Mother ethnicity<br><code>screen_mother_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">Participant response to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item about ethnic identity collected during screening. <i>Source: Admin</i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race, multi-categorical<br><code>screen_mother_race</code></td>
<td style="word-wrap: break-word; white-space: normal;">Participant response to <a href="https://www.census.gov/programs-surveys/acs.html">ACS</a> item/question about racial identity collected during screening. <i>Source: Admin</i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race & ethnicity - multiracial aggregation by Hispanic/non-Hispanic<br><code>screen_mother_ethnoracial_acs_by_multi_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">Constructed from screening race/ethnicity responses based on <b>current federal standards.*</b> Multiracial individuals are subcategorized based on whether <i>Hispanic</i> is one of their selected identities. <i>Source: Admin</i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race & ethnicity - multiracial aggregation by Black/non-Black<br><code>screen_mother_ethnoracial_acs_by_multi_race</code></td>
<td style="word-wrap: break-word; white-space: normal;">Constructed from screening race/ethnicity responses based on <b>current federal standards.*</b> Multiracial individuals are subcategorized based on whether <i>Black/African American</i> is one of their selected identities. <i>Source: Admin</i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race and ethnicity<br><code>rc_mother_ethnoracial_aou_race_ethnicity</code></td>
<td style="word-wrap: break-word; white-space: normal;">Derived from single <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a> race and ethnicity item scored following <a href="https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards">OMB</a> standards: Anyone identifying as Hispanic/Latino (alone or with another group) is categorized as Hispanic/Latino; all others as non-Hispanic. <i>Source: HBCD Demographics</i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race, indicator variables from screening<br><code>screen_mother_race_multi___{0 - 5}</code></td>
<td style="word-wrap: break-word; white-space: normal;">Indicator variables from ACS race question:<br>
0 = White<br>
1 = Black or African American<br>
2 = American Indian or Alaskan Native<br>
3 = Asian<br>
4 = Native Hawaiian or other Pacific Islander<br>
5 = Other race<br>
<i>Source: Admin</i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Mother race, indicator variables from survey item<br><code>rc_mother_race___{0 - 7}</code></td>
<td style="word-wrap: break-word; white-space: normal;">Indicator variables for responses to <a class="in-cell-link" href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations" target="_blank">All of Us</a> combined race and ethnicity question:<br>
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
<td>Mother education<br><code>rc_mother_education</code></td>
<td style="word-wrap: break-word; white-space: normal;">Derived from <code>sed_bm_demo_edu_001</code>. <i>Source: HBCD Demographics</i></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Total combined household income<br><code>rc_mother_income</code></td>
<td style="word-wrap: break-word; white-space: normal;">Derived from <code>sed_bm_demo_income_002</code>. <i>Source: HBCD Demographics</i></td>
</tr>
<tr>
<td>Recruitment site</td>
<td style="word-wrap: break-word; white-space: normal;"><code>recruitment_site</code><br>De-identified value reflecting recruitment sites. <i>Source: Admin</i></td>
</tr>
<tr>
<td colspan="2" style="word-wrap: break-word; white-space: normal;">
<b>*Current federal standards:</b> if an individual is identified as Hispanic or Latino based on the response to the ethnicity item, they will be categorized as such, regardless of their race. Individuals who select more than one race are categorized as "multiracial."</td>
</tr>
</tbody>
</table>

