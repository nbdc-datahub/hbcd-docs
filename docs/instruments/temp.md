## Instrument & Measure-Specific

[Tabulated data](../datacuration/phenotypes.md) includes age variables quantifying the age of the child at the time of instrument administration. Similarly, metadata for [raw file-based data](../datacuration/file-based-data.md#raw-bids) (including MR, EEG, and wearable sensor recordings) report the age of the child at the time of data acquisition. With the exception of **Gestational Age at Administration** reported during the prenatal V01 visit, age variables are only available for visits V02 onward, post-birth.

For file-based data, the age of the child at the time of data acquisition is reported in the session- and scan-level `.tsv` files that accompany these data ([see details](../datacuration/file-based-data.md#participant-session-scan-level-data)).

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead>
  <tr>
    <th>Name</th>
    <th>Variable Name</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
<tr><td colspan="3"><b>TABULATED DATA</b></td></tr>
<tr>
<td>Gestational Age at Administration (GAA)</td>
<td><code>gestational_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time elapsed (whole weeks, rounded down) between the birth parent's LMP<sup><b>1</b></sup> and date of instrument administration. <span class="tooltip">Max 4 week variation<span class="tooltiptext">Varies no more than 4 weeks across protocol elements except when protocol exceptions were granted</span></span>. <b>V01 only</b>
</td>
</tr>
<tr>
<td>Chronological Age at Administration</td>
<td><code>candidate_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Age in years<sup><b>2</b></sup> at time of instrument administration. Computed with jittered DOB (up to 7 days).</td>
</tr>
<tr>
<td>Adjusted Chronological Age at Administration (ACAA)</td>
<td><code>adjusted_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time elapsed (whole weeks, rounded down) between <span class="tooltip">EDD<span class="tooltiptext">estimated date of delivery</span></span> and date of instrument administration.</td>
</tr>
<tr><td colspan="3"><b>FILE-BASED METADATA</b></td></tr>
<tr>
<td>Adjusted Age at Time of Scan</td>
<td><code>age_adjusted</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time in days (not rounded) from <span class="tooltip">EDD<span class="tooltiptext">estimated date of delivery</span></span> to the date of data acquisition</td>
</tr>
<tr>
<td>Chronological Age at Time of Scan</td>
<td><code>age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Age in years<sup><b>2</b></sup> at time of data acquisition. Computed with jittered DOB (up to 7 days).</td>
</tr>
</tbody>
<tfoot><tr><td colspan="3" style="word-wrap: break-word; white-space: normal;">
  <sup><b>1</b></sup> LMP: first day of the birth parent's last menstrual period, estimated as EDD minus 280 days<br>
  <sup><b>2</b></sup> Years are to 3 decimal places, calculated by dividing the total days elapsed (rounded down) by 365.25</td>
</tr></tfoot>
</table>






<br>

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead>
  <tr>
    <th>Name</th>
    <th>Variable Name</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
<tr><td colspan="3"><b>TABULATED DATA</b></td></tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Gestational Age at Administration (GAA)</td>
<td><code>gestational_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time elapsed (whole weeks, rounded down) between the birth parent's LMP<sup><b>1</b></sup> and date of instrument administration. <span class="tooltip">Max 4 week variation<span class="tooltiptext">Varies no more than 4 weeks across protocol elements except when protocol exceptions were granted</span></span>. <b>V01 only</b>
</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Chronological Age at Administration</td>
<td><code>candidate_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Age in years<sup><b>2</b></sup> at time of instrument administration. Based on DOB jittered up to 7 days.</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Adjusted Chronological Age at Administration (ACAA)</td>
<td><code>adjusted_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time elapsed (whole weeks, rounded down) between <span class="tooltip">EDD<span class="tooltiptext">estimated date of delivery</span></span> and date of instrument administration.</td>
</tr>
<tr><td colspan="3"><b>FILE-BASED METADATA</b></td></tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Adjusted Age at Time of Scan</td>
<td><code>age_adjusted</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time in days (not rounded) from <span class="tooltip">EDD<span class="tooltiptext">estimated date of delivery</span></span> to the date of data acquisition</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Chronological Age at Time of Scan</td>
<td><code>age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Age in years<sup><b>2</b></sup> at time of data acquisition. Based on DOB jittered up to 7 days.</td>
</tr>
</tbody>
<tfoot><tr><td colspan="3" style="word-wrap: break-word; white-space: normal;">
  <sup><b>1</b></sup> LMP: first day of the birth parent's last menstrual period, estimated as EDD minus 280 days<br>
  <sup><b>2</b></sup> Years are to 3 decimal places, calculated by dividing the total days elapsed (rounded down) by 365.25. DOB is jittered up to 7 days to mitigate identification risks</td>
</tr></tfoot>
</table>


