<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
.pr-pill {
  display: inline-block;
  padding: 2px 8px;
  font-size: 1em;
  font-weight: 600;
  border-radius: 999px;
  line-height: 1;
  white-space: nowrap;
}
/* Version-specific styling */
.pr-general {
  background-color: #e6f0ff;
  color: #1a4fb3;
}
/* TBD PILL*/
.pr-tbd {
  background-color: #f1f3f5;
  color: #666;
  font-style: italic;
}

/* ICONS */
.icon-rotate {
  color: #199bd6;
  margin-right: 0.4em;
  font-size: 1em;
}
.icon-bug {
  color: #f97316;
  margin-right: 0.4em;
  font-size: 1em;
}
</style>

# Known Issues & Pending Updates 

The tables below summarize known issues affecting the current data release and pending updates across study instruments. Entries are organized by domain and include the expected release in which each fix or update will be implemented. This page is updated regularly as new issues are identified and updates are planned.

To ask a question or report an issue, please submit a ticket through the [Help Center in the NBDC Data Access Platform →](https://nbdc.lassoinformatics.com/issue-tracker).

---

<p style="font-size: 1.2em; color: #555; text-align: center; line-height: 2;">
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i> = Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Pending Update &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.1em;"></i> = Target Release for Fix
</p>
    
---

### Behavior & Child-Caregiver Interaction

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ERICA</td>
<td>Addition of all age and <code>date_taken</code> fields (currently excluded due to use of coding rather than visit dates).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i><i class="fas fa-bug icon-bug"></i></td>
<td>ERICA</td>
<td>
A future release will include reliability codes integrated into the primary coding dataset. Until then, users must perform this integration manually: <b>see the ERICA <a href="../../instruments/bcgi/erica/#warning">Data Warning</a> for instructions.</b>
<br>
Instructions include cleaning the current files to exclude n=44 participants with incorrect code values (data entry/form errors) and capping <code>b_raw</code> values at 3.0 (n=3 participants). These issues will also be corrected in future release data.
</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>

</tbody></table>


<!-- 

### ORIG

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ERICA</td>
<td>Addition of all age and <code>date_taken</code> fields (currently excluded due to use of coding rather than visit dates).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ERICA</td>
<td>Integrate reliability codes into the primary coding dataset. <b>Users must perform integration themselves for current release data - see <a href="../../instruments/bcgi/erica/#warning">Data Warning</a> for instructions.</b></td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>ERICA</td>
<td>Users should clean the <code>mh_cg_erica_3_9m</code> (primary coding data file) as follows (fixes coming in a future release):
<ul>
  <li>
    Exclude n=44 participants with incorrect code values (data entry/form errors): 
    <a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/ERICA_2.1_DataError_EXCLUSIONS.csv"><code>ERICA_2.1_DataError_EXCLUSIONS.csv</code></a>
    (<a href="https://hbcd-docs-private.lassoinformatics.com">HBCD Private Release Notes</a>)
  </li>
  <li>
    Cap <code>b_raw</code> values at 3.0 (n=3 participants)
  </li>
</ul>
</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>

</tbody></table> -->
