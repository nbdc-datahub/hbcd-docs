# Age Variable Definitions

Separate variables reporting age are included in Basic Demographics (global, single-point variables), tabulated data (age variables at time of instrument administration), and file-based metadata (age variables at time of MR/EEG/wearable sensor data acquisition). See details for each below.

## Basic Demographics

Basic Demographics (`sed_basic_demographics`), derived from multiple sources/instruments, includes global, single-point variables that do not vary over time (e.g. gestational age of the child at delivery). Fields reporting age are computed from administrative records collected at screening and include: **Maternal Age at V01 (MAV01)**, **Maternal Age at Delivery (MAD)**, and **Gestational age at delivery (GAD)**.<br>
See full details in **Basic Demographics - [Age, Sex, & Other Variables](demo/basicdemo.md#age-sec-other-variables)**.

## Tabulated & File-Based Data
[Tabulated data](../datacuration/phenotypes.md) includes age variables quantifying the age of the child at the time of instrument administration. Similarly, metadata for [raw file-based data](../datacuration/file-based-data.md#raw-bids) (including MR, EEG, and wearable sensor recordings) report the age of the child at the time of data acquisition (available within session and scan TSV metadata files - [see details](../datacuration/file-based-data.md#participant-session-scan-level-data)). With the exception of **Gestational Age at Administration** reported during the prenatal V01 visit, age variables are available post-birth for visits V02 onward.

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<tbody>
<tr>
  <td style="color: teal;"><b>Tabulated Data Variables</b></td>
  <td><b>Details</b></td>
</tr>
<tr>
<td>Gestational Age at Administration<br><code>gestational_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time elapsed (whole weeks, rounded down) between the birth parent's LMP<sup><b>1</b></sup> and date of instrument administration. Varies no more than 4 weeks across protocol elements except when protocol exceptions were granted. <b>V01 only</b>
</td>
</tr>
<tr>
<td>Chronological Age at Administration<br><code>candidate_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Age in years<sup><b>2</b></sup> at time of instrument administration. Computed with jittered DOB (up to 7 days).</td>
</tr>
<tr>
<td>Adjusted Chronological Age at Administration<br><code>adjusted_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time elapsed (whole weeks, rounded down) between <span class="tooltip">EDD<span class="tooltiptext">estimated date of delivery</span></span> and date of instrument administration.</td>
</tr>
<tr>
  <td style="color: teal;"><b>File-Based Data Variables</b></td>
  <td><b>Details</b></td>
</tr>
<tr>
<td>Adjusted Age at Time of Scan<br><code>age_adjusted</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time in days elapsed between <span class="tooltip">EDD<span class="tooltiptext">estimated date of delivery</span></span> and date of data acquisition</td>
</tr>
<tr>
<td>Chronological Age at Time of Scan<br><code>age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Age in years<sup><b>2</b></sup> at time of data acquisition. Computed with jittered DOB (up to 7 days).</td>
</tr>
</tbody>
<tfoot><tr><td colspan="2" style="word-wrap: break-word; white-space: normal;">
  <sup><b>1</b></sup> LMP: first day of the birth parent's last menstrual period, estimated as EDD minus 280 days<br>
  <sup><b>2</b></sup> Years are to 3 decimal places, calculated by dividing the total days elapsed (rounded down) by 365.25</td>
</tr></tfoot>
</table>