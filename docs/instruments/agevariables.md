# Age Variable Definitions

Separate variables reporting age are included in Basic Demographics (global, single-point variables), tabulated data (age variables at time of instrument administration), and file-based metadata (age variables at time of MR/EEG/wearable sensor data acquisition). See details for each below.

## Basic Demographics

Basic Demographics (`sed_basic_demographics`), derived from multiple sources/instruments, includes global, single-point variables that do not vary over time (e.g. gestational age of the child at delivery). Fields reporting age are computed from administrative records collected at screening and include: **Maternal Age at V01 (MAV01)**, **Maternal Age at Delivery (MAD)**, and **Gestational age at delivery (GAD)**.<br>
See full details in **Basic Demographics - [Age, Sex, & Other Variables](demo/basicdemo.md#age-sec-other-variables)**.

## Tabulated Instrument Data

All [tabulated data](../datacuration/phenotypes.md) include the following fields that report the **child's age** at the time of instrument administration.

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

## Raw File-Based Data

Raw file-based data includes MR, EEG, and wearable sensor data acquired from the child ([see details](../datacuration/file-based-data.md#raw-bids)). For visits V02 onward (*data unavailable for prenatal visit V01*), the age of the child at the time of data acquisition is reported in the session- and scan-level `.tsv` files that accompany these data ([see details](../datacuration/file-based-data.md#participant-session-scan-level-data)).

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead>
  <tr>
    <th>Name</th>
    <th>Variable Name</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Adjusted Age at Time of Scan</td>
<td><code>age_adjusted</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time in days (not rounded) from <span class="tooltip">EDD<span class="tooltiptext">estimated date of delivery</span></span> to the date of data acquisition</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Chronological Age at Time of Scan</td>
<td><code>age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time from birth (DOB jittered up to 7 days to mitigate identification risks) to the date of data acquisition.<br>
UNITS: Years (to three decimal places), calculated by dividing the total days elapsed (rounded down) by 365.25</td>
</tr>
</tbody>
</table>