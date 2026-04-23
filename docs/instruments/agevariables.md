<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>

# Age Variable Definitions

This page defines how age is represented for the child and birth parent across HBCD datasets. 

## Basic Demographics

The Basic Demographics table contains global, static variables derived across administrative and instrument data. Age variables include the child's **Gestational Age at Delivery** as well as age variables specific to the birth parent, including **Maternal Age at V01** and **Maternal Age at Delivery**. See documentation under [Basic Demographics](demo/basicdemo.md#age-variables) for details.

## Tabulated Instrument & File-Based Data

Age variables in tabulated instrument data describe the child's age at the time of instrument administration. Age variables in file-based MR, EEG, and biosensor data, provided within [session- and scan-level metadata files](../datacuration/file-based-data.md#participant-session-scan-level-data), describe the child's age at the time of data acquisition. **All variables outlined below are specific to the child.** 

<span class="pill-badge" style="background-color: pink;">V01</span>&nbsp;= Available Visit V01 only (prenatal) &nbsp;&nbsp;
<span class="pill-badge">V02+</span>&nbsp;= Available Visit V02 onward (post-birth)
</p>
<table class="table-no-vertical-lines">
<tbody>
<tr><td colspan="2"><i class="fa-solid fa-table header-icon"></i> <b>TABULATED DATA <i>(age of child at time of instrument administration)</i></b></td></tr>
<tr><td>Gestational Age at Administration<br><code>gestational_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Time elapsed (whole weeks, rounded down) between the <span class="tooltip tooltip-left">LMP<span class="tooltiptext">First day of the birth parent's last menstrual period, estimated as EDD minus 280 days</span></span> and date of instrument administration. Varies no more than 4 weeks across protocol elements except when protocol exceptions were granted. Note that instruments not administered at V01 will have null values for gestational age. <span class="pill-badge" style="background-color: pink;">V01</span></td>
</tr>
<tr>
<td>Chronological Age at Administration<br><code>candidate_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
Age in years (to three decimal places, calculated by dividing the total days elapsed, rounded down, by 365.25) at the time of instrument administration. Computed using a jittered DOB shifted by up to 7 days to protect participant privacy. <span class="pill-badge">V02+</span></td>
</tr>
<tr><td>Adjusted Chronological Age at Administration<br><code>adjusted_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Computed relative to the EDD to align preterm and full-term infants to a common developmental reference: time elapsed (whole weeks rounded down) between EDD and date of administration.<span class="pill-badge">V02+</span></td></tr>
<tr><td colspan="2">
  <br>
  <i class="fa-solid fa-folder-open header-icon"></i> <b>FILE-BASED DATA  <i>(age of child at time of MR/EEG/biosensor data acquisition)</i></b></td></tr>
<tr>
<td>Adjusted Age at Time of Scan<br><code>age_adjusted</code></td>
<td style="word-wrap: break-word; white-space: normal;">Time in days elapsed between the EDD and date of data acquisition. <span class="pill-badge">V02+</span></td>
</tr>
<tr>
<td>Chronological Age at Time of Scan<br><code>age</code></td>
<td style="word-wrap: break-word; white-space: normal;">Age in years (to three decimal places, calculated by dividing the total days elapsed, rounded down, by 365.25) at the time of data acquisition. Computed using a jittered DOB shifted by up to 7 days to protect participant privacy. <span class="pill-badge">V02+</span><td>
</tr>
<div>
</tr>
</tbody>
</table>
