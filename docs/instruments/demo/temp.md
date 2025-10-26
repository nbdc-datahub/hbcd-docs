For variables that combine race and ethnicity: anyone identifying as <i>Hispanic/Latino</i> (regardless of their race or other identities selected) is categorized as <i>Hispanic/Latino</i> and all others as <i>non-Hispanic</i>.


both the ACC (per current federal standards) and AOU (per OMB standards) variables are computed 




Derived from single All of Us race and ethnicity item scored following OMB standards: Anyone identifying as Hispanic/Latino (alone or with another group) is categorized as Hispanic/Latino and all others as non-Hispanic.


<span class="pill-badge" style="font-size: 0.75em;">V02+</span><span> - <i>Variables about the child are available beginning visit V02, post-birth (V01 is prenatal).</i></span>
<table class="compact-table-no-vertical-lines">
<thead>
  <tr>
    <th style="width: 1%;"></th>
    <th style="padding-left: 0;">Construct</th>
    <th>Variable Name</th>
    <th>Description/Details</th>
  </tr>
</thead>
<tbody>
<tr>
<td></td>
<td style="padding-left: 0;">Maternal Age at {V01/Delivery}</td>
<td><code>mother_age_v01</code><br><code>mother_age_delivery</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Birth parent's age at V01 visit (MAV01)/delivery (MAD).<br>
  <i>See <a href="../../agevariables/#basic-demographics" target="_blank">Age Variables <i style="font-size: 0.8em;" class="fa-solid fa-arrow-up-right-from-square"></i></a> for full documentation of age fields.</td>
</tr>
<tr>
<td style="padding-left: 0; padding-right: 0; text-align: center;"><i class="fa-solid fa-baby"></i></td>
<td style="padding-left: 0;">Gestational Age at Delivery</td>
<td><code>gestational_age_delivery</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Child's gestational age at delivery (GAD). <span class="pill-badge">V02+</span><br>
  <i>See <a href="../../agevariables/#basic-demographics" target="_blank">Age Variables <i style="font-size: 0.8em;" class="fa-solid fa-arrow-up-right-from-square"></i></a> for full documentation of age fields.</i></td>
</tr>
<tr>
<td style="padding-left: 0; padding-right: 0; text-align: center;"><i class="fa-solid fa-baby"></i></td>
<td style="padding-left: 0;">Child sex</td>
<td><code>sex</code></td>
<td>Derived from admin records. <span class="pill-badge">V02+</span></td>
</tr>
<tr>
<td></td>
<td style="padding-left: 0;">Mother education</td>
<td><code>rc_mother_education</code></td>
<td>Derived from <code>sed_bm_demo_edu_001</code> (HBCD Demographics).</td>
</tr>
<tr>
<td></td>
<td style="padding-left: 0;">Total household income</td>
<td><code>rc_mother_income</code></td>
<td>Derived from <code>sed_bm_demo_income_002</code> (HBCD Demographics).</td>
</tr>
<tr>
<td></td>
<td style="padding-left: 0;">Recruitment site</td><td><code>recruitment_site</code></td><td style="word-wrap: break-word; white-space: normal;">De-identified site ID derived from administrative records.</td></tr>
</tbody>
</table>