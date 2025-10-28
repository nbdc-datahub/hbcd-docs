# Age Variable Definitions

Separate variables reporting age are included in Basic Demographics (global, single-point variables), tabulated data (age variables at time of instrument administration), and file-based metadata (age variables at time of MR/EEG/wearable sensor data acquisition). See details for each below.

## Tabulated & File-Based Data

Age variables are included across both **[raw file-based](../datacuration/file-based-data.md#raw-bids)** and **[tabulated](../datacuration/phenotypes.md)** datasets to describe the child’s age at the time of data collection.


<i class="fa-solid fa-folder-open"></i> <b>File-based data</b><br>
Age variables reflect age at the time of <i>data acquisition</i> for MR, EEG, and wearable sensors - available within <a href="../../datacuration/file-based-data/#participant-session-scan-level-data">session/scan TSV metadata files</a>. <i>Available for visits V02 and later (post-birth).</i>

<i class="fa-solid fa-table"></i> <b>Tabulated data</b><br>
Age variables reflect age at the time of <i>administration</i> (or <i>data acquisition</i> for brain imaging data) for study instruments and measures. <i>Available for visits V02 and later (post-birth) with the exception of <b>Gestational Age at Administration</b> collected only at the prenatal V01 visit.</i> **Note:**
<ul style="margin-top: -4px;">
<li>For tabulated data computed from brain imaging pipeline derivatives (<a href="../../datacuration/overview/#warning" target="_blank">see details</a>), age reflects time of <i>data acquisition</i>. Tabulated EEG data do not include fields for age.</li> 
<li>The age fields described here are not applicable to derived <a href="../#demo" target="_blank">Demographics domain</a> data - <a href="#basic-demographics">see details below</a></li>
</ul>

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<tbody>
<tr style="background-color: #009e9e34;">
  <td style="color: teal;"><i class="fa-solid fa-table"></i> <b>Tabulated Data Variables</b></td>
  <td><b>Details</b></td>
</tr>
<tr>
<td>Gestational Age at Administration<br><code>gestational_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Time elapsed (whole weeks, rounded down) between the  
  <span class="tooltip tooltip-left">LMP<span class="tooltiptext">First day of the birth parent's last menstrual period, estimated as EDD minus 280 days</span></span> and the date of instrument administration. Varies no more than 4 weeks across protocol elements except when protocol exceptions were granted. <b>V01 only</b>
</td>
</tr>
<tr>
<td>Chronological Age at Administration<br><code>candidate_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Age in years<sup><b>1</b></sup> at the time of instrument administration. Computed using a jittered DOB randomly shifted by up to 7 days to protect participant privacy.
</td>
</tr>
<tr>
<td>Adjusted Chronological Age at Administration<br><code>adjusted_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Time elapsed (whole weeks, rounded down) between the 
  <span class="tooltip">EDD<span class="tooltiptext">Estimated Date of Delivery</span></span> 
  and the date of instrument administration.
</td>
</tr>
<tr><td colspan="2" style="border-top: 2px solid #cce7e7;"></td></tr>

<tr style="background-color: #009e9e34;">
  <td style="color: teal;"><i class="fa-solid fa-folder-open"></i> <b>File-Based Data Variables</b></td>
  <td><b>Details</b></td>
</tr>
<tr>
<td>Adjusted Age at Time of Scan<br><code>age_adjusted</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Time in days elapsed between the 
  <span class="tooltip">EDD<span class="tooltiptext">Estimated Date of Delivery</span></span> 
  and the date of data acquisition.
</td>
</tr>
<tr>
<td>Chronological Age at Time of Scan<br><code>age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Age in years<sup><b>1</b></sup> at the time of data acquisition. Computed using a jittered DOB randomly shifted by up to 7 days to protect participant privacy.
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


## Basic Demographics

Basic Demographics (`sed_basic_demographics`), derived from multiple sources/instruments, includes global, single-point variables that do not vary over time (e.g. gestational age of the child at delivery). Fields reporting age are computed from administrative records collected at screening and include: **Maternal Age at V01 (MAV01)**, **Maternal Age at Delivery (MAD)**, and **Gestational age at delivery (GAD)**.<br>
See full details in **Basic Demographics - [Age, Sex, & Other Variables](demo/basicdemo.md#age-sex-other-variables)**.

Visit Information (`par_visit_data`) does not include variables for age.


