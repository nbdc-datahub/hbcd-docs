




### Race & Ethnicity Variables 

Race and ethnicity variables are either computed from administrative records collected during screening using the American Community Survey ([ACS](https://www.census.gov/programs-surveys/acs.html)), or a single item from the <a href="../../SED/demo-cg/" target="_blank">HBCD Demographics</a> instrument based on the All of Us.

#### ACS-Derived Race & Ethnicity Variables
These are computed from administrative records collected during screening using the American Community Survey (<a href="https://www.census.gov/programs-surveys/acs.html">ACS</a>).

<table id="fedstandards" class="compact-table-no-vertical-lines" style="border: 2px solid #006c6c5b; border-radius: 8px; border-collapse: collapse; font-size: 1.0em;">
<tbody>
<tr><td style="word-wrap: break-word; white-space: normal;">
<span style="margin-bottom: 0; padding-bottom: 0;"><i id="fedstandards" style="color: teal;" class="fa fa-circle-info"></i> <b>Combined race & ethnicity variables</b> are constructed from ACS race/ethnicity item following current federal standards:</span>
  <ul style="margin-top: 0; padding-top: 0; font-size: 0.9em;">
  <li>Participants who identify as <em>Hispanic or Latino</em> in the ACS ethnicity item are categorized as such regardless of their race.</li>
  <li>Individuals who select more than one race are categorized as <strong>multiracial</strong>.</li>
  <li>Multiracial participants are subcategorized by <strong>ethnicity</strong> (<em>Hispanic</em> vs. <em>non-Hispanic</em>) and <strong>race</strong> (<em>Black/African American</em> vs. <em>non-Black/African American</em>).</li>
  </ul>
</td></tr>
</tbody>
</table>

<table class="compact-table-no-vertical-lines">
<thead>
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
</table>
<p></p>
---------------

### AOU-Derived Race & Ethnicity Variables
These are computed from Single All of US (<a href="https://support.researchallofus.org/hc/en-us/articles/360039299632-Race-and-ethnicity-generalizations">AOU</a>) race and ethnicity item collected as part of the <a href="../../SED/demo-cg/" target="_blank">HBCD Demographics</a> instrument.

<table class="compact-table-no-vertical-lines">
<thead>
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
