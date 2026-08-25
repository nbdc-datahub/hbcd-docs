<style>
.wy-nav-content {
    width: 95% !important;
    max-width: 95% !important;
    flex-grow: 1 !important;
}
</style>

# Age Variable Definitions
This page defines how age is represented for the child and birth parent across HBCD datasets. 

## Basic Demographics
The Basic Demographics table contains global, static variables derived across administrative and instrument data. Age variables include the child's **Gestational Age at Delivery** as well as age variables specific to the birth parent, including **Maternal Age at V01** and **Maternal Age at Delivery**. See documentation under the derived [Static Table](demo/static.md#age-sex-other-variables) measure for details.

## Tabulated Instrument Data
Age variables within tabulated instrument data describe the child’s age at instrument administration.

<div class="infobox" style="background-color: #fff8e1; border-left: 4px solid #ffa500;">
  <i class="fas fa-exclamation-triangle" style="color: #ffa500;"></i>
    &nbsp;<b>Note:</b>
  <ul>
  <li>LMP (first day of the birth parent's last menstrual period) is estimated as EDD (Estimated Date of Delivery) − 280 days</li>
  <li>Adjusted Chronological Age may be negative if collected prior to the EDD</li>
 </ul>
</div>

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Variable Name</th>
<th>Variable Label</th>
<th>Description</th>
<th>Visit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Gestational Age at Administration</td>
<td><code>gestational_age</code></td>
<td>Number of weeks (rounded down) between LMP and the V01 administration date. May vary by ≤4 weeks across protocol elements.</td>
<td>V01</td>
</tr>
<tr>
<td>Chronological Age at Administration</td>
<td><code>candidate_age</code></td>
<td>Age in years (3 decimal places) at administration based on a jittered DOB (±7 days) to protect participant privacy. Calculated as: total elapsed days (rounded down) ÷ 365.25</td>
<td>V02+</td>
</tr>
<tr>
<td>Adjusted Chronological Age at Administration</td>
<td><code>adjusted_age</code></td>
<td>Number of weeks (rounded down) between EDD and the administration date. Aligns preterm and full-term infants to a common developmental reference.
</td>
<td>V02+</td>
</tr>
</tbody>
</table>

## File-Based Data
Age variables within file-based data, provided within higher-level [session- and scan-level metadata](../datacuration/file-based-data.md#participant-session-scan-level-data), describe the child’s age on day of scan/data acquisition for MR, EEG, and biosensor data.

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Variable Name</th>
<th>Variable Label</th>
<th>Description</th>
<th>Visit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Adjusted Age at Time of Scan</td>
<td><code>age_adjusted</code></td>
<td>Time in days between EDD and the acquisition date</td>
<td>V02+</td>
</tr>
<tr>
<td>Chronological Age at Time of Scan</td>
<td><code>age</code></td>
<td>Age in years (3 decimal places) at acquisition, based on a jittered DOB (±7 days) to protect participant privacy. Calculated as: total elapsed days (rounded down) ÷ 365.25</td>
<td>V02+</td>
</tr>
</tbody>
</table>


