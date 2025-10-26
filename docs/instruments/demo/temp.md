




### Race & Ethnicity Variables 

Race and ethnicity variables are either computed from administrative records collected during screening using the American Community Survey ([ACS](https://www.census.gov/programs-surveys/acs.html)), or a single item from the <a href="../../SED/demo-cg/" target="_blank">HBCD Demographics</a> instrument based on the All of Us.

For variables that combine race and ethnicity, both the ACC (per current federal standards) and AOU (per OMB standards) variables are computed as follows: anyone identifying as <i>Hispanic/Latino</i> (regardless of their race or other identities selected) is categorized as <i>Hispanic/Latino</i> and all others as <i>non-Hispanic</i>.

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

<p></p>

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<td colspan="3" style="font-size: 1.0em; word-wrap: break-word; white-space: normal;">
<b style="color: teal;">ACS-DERIVED RACE & ETHNICITY VARIABLES</b><br>
Variables computed from administrative records collected during screening using the American Community Survey (<a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>)
</td>
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
<td><code>screen_mother_race_<br>multi___{0-5}</code></td>
<td>Indicator variables from ACS race question:<br>
0 = White<br>
1 = Black or African American<br>
2 = American Indian or Alaskan Native<br>
3 = Asian<br>
4 = Native Hawaiian or other Pacific Islander<br>
5 = Other race</td>
</tr>
</tbody>
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<td colspan="3" style="font-size: 1.0em; word-wrap: break-word; white-space: normal;">
<b style="color: teal;">AOU-DERIVED RACE & ETHNICITY VARIABLES</b><br>
Variables computed from Single All of US (<a href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations">AOU</a>) race and ethnicity item collected as part of the <a href="../../SED/demo-cg/" target="_blank">HBCD Demographics</a> instrument.
</td>
</tr>
  <tr>
    <th style="width: 20%;">Construct</th>
    <th style="width: 20%;">Variable Name</th>
    <th style="width: 40%;">Description/Details</th>
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
<span class="pill-badge" style="font-size: 0.75em;">V02+</span><span> - <i>Variables about the child are available beginning visit V02, post-birth (V01 is prenatal).</i></span>


