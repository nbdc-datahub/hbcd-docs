## Instrument & Measure-Specific

Age fields for [tabulated data](../datacuration/phenotypes.md) and file-based data report the age of the **child** at the time of instrument administration/data acquisition.

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<tfoot><tr><td colspan="3" style="word-wrap: break-word; white-space: normal;">
  <sup><b>1</b></sup> LMP: first day of the birth parent's last menstrual period, estimated as EDD minus 280 days<br>
  <sup><b>2</b></sup> Years are to 3 decimal places, calculated by dividing the total days elapsed (rounded down) by 365.25</td></tr></tfoot>
<thead>
  <tr>
    <th>Name</th>
    <th>Variable Name</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Gestational Age at Administration (GAA)</td>
<td><code>gestational_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time elapsed (whole weeks, rounded down) between the birth parent's LMP<sup><b>1</b></sup> and date of instrument administration. <span class="tooltip">Max 4 week variation<span class="tooltiptext">Varies no more than 4 weeks across protocol elements except when protocol exceptions were granted</span></span>. <b>V01 only</b>
</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Chronological Age at Administration</td>
<td><code>candidate_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time from birth (DOB jittered up to 7 days to mitigate identification risks) in years<sup><b>2</b></sup> to date of instrument administration. <b>Visits V02+</b></td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Adjusted Chronological Age at Administration (ACAA)</td>
<td><code>adjusted_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time elapsed (whole weeks, rounded down) between <span class="tooltip">EDD<span class="tooltiptext">estimated date of delivery</span></span> and date of instrument administration. <b>Visits V02+</b></td>
</tr>
</tbody>
</table>


