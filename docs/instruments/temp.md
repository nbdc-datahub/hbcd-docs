

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<tbody>
<tr style="background-color: #e9f7f7;">
  <td style="color: teal;"><b>🧾 Tabulated Data Variables</b></td>
  <td><b>Details</b></td>
</tr>
<tr>
<td>Gestational Age at Administration<br><code>gestational_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Time elapsed (whole weeks, rounded down) between the 
  <span class="tooltip">LMP<span class="tooltiptext">first day of the birth parent's last menstrual period, estimated as EDD – 280 days</span></span> 
  and the date of instrument administration. Varies no more than 4 weeks across protocol elements except when protocol exceptions were granted. <b>V01 only</b>
</td>
</tr>
<tr>
<td>Chronological Age at Administration<br><code>candidate_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Age in years<sup><b>1</b></sup> at the time of instrument administration. Computed using a 
  <span class="tooltip">jittered DOB<span class="tooltiptext">date of birth randomly shifted by up to 7 days to protect participant privacy</span></span>.
</td>
</tr>
<tr>
<td>Adjusted Chronological Age at Administration<br><code>adjusted_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Time elapsed (whole weeks, rounded down) between the 
  <span class="tooltip">EDD<span class="tooltiptext">estimated date of delivery</span></span> 
  and the date of instrument administration.
</td>
</tr>

<tr><td colspan="2" style="border-top: 2px solid #cce7e7;"></td></tr>

<tr style="background-color: #e9f7f7;">
  <td style="color: teal;"><b>💾 File-Based Data Variables</b></td>
  <td><b>Details</b></td>
</tr>
<tr>
<td>Adjusted Age at Time of Scan<br><code>age_adjusted</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Time in days elapsed between the 
  <span class="tooltip">EDD<span class="tooltiptext">estimated date of delivery</span></span> 
  and the date of data acquisition.
</td>
</tr>
<tr>
<td>Chronological Age at Time of Scan<br><code>age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Age in years<sup><b>1</b></sup> at the time of data acquisition. Computed using a 
  <span class="tooltip">jittered DOB<span class="tooltiptext">date of birth randomly shifted by up to 7 days to protect participant privacy</span></span>.
</td>
</tr>
</tbody>
<tfoot>
<tr>
  <td colspan="2" style="word-wrap: break-word; white-space: normal; border-top: 2px solid #cce7e7; padding-top: 6px;">
    <sup><b>1</b></sup> Years are to three decimal places, calculated by dividing the total days elapsed (rounded down) by 365.25.
  </td>
</tr>
</tfoot>
</table>
