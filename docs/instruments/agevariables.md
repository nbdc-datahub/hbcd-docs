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

Age variables describe the child’s age at either instrument administration for tabulated instrument data or data acquisition for file-based data (*MR, EEG, and biosensor data, provided within [session- and scan-level metadata files](../datacuration/file-based-data.md#participant-session-scan-level-data)*). **All variables below refer to the child.**

<span class="pill-badge" style="background-color: pink;">V01</span>&nbsp;= Available Visit V01 only (prenatal) &nbsp;&nbsp;
<span class="pill-badge">V02+</span>&nbsp;= Available Visit V02 onward (post-birth)
</p>

<!-- TABULATED DATA -->
#### <i class="fa-solid fa-table header-icon"></i> TABULATED DATA <i>(age at instrument administration)</i>
<table class="table-no-vertical-lines">
<thead>
<tr>
</tr>
<tr>
<th>Variable</th>
<th>Description</th>
<th>Visit</th>
</tr>
</thead>
<tbody>

<tr>
<td>
Gestational Age<br>at Administration<br>
<code>gestational_age</code>
</td>
<td style="word-wrap: break-word; white-space: normal;">
<ul>
  <li>Time in completed weeks (rounded down) between <span class="tooltip tooltip-right">LMP<span class="tooltiptext">First day of the birth parent's last menstrual period (estimated as EDD − 280 days)</span></span> and the V01 administration date.</li>
  <li>Values are expected to vary by ≤4 weeks across protocol elements, except in approved protocol exceptions.</li>
  <li><b>Note:</b> May be negative if collected prior to the <span class="tooltip">EDD<span class="tooltiptext">Estimated Date of Delivery</span></span>.</li>
</ul>
</td>
<td><span class="pill-badge" style="background-color: pink;">V01</span></td>
</tr>

<tr>
<td>
Chronological Age<br>at Administration<br>
<code>candidate_age</code>
</td>
<td style="word-wrap: break-word; white-space: normal;">
<ul>
  <li>Age in years (3 decimal places) at administration, calculated as: total elapsed days (rounded down) ÷ 365.25.</li>
  <li>Based on a jittered DOB (±7 days) to protect participant privacy.</li>
</ul>
</td>
<td><span class="pill-badge">V02+</span></td>
</tr>

<tr>
<td>
Adjusted Chronological Age<br>at Administration<br>
<code>adjusted_age</code>
</td>
<td style="word-wrap: break-word; white-space: normal;">
<ul>
  <li>Time in completed weeks (rounded down) between <span class="tooltip">EDD<span class="tooltiptext">Estimated Date of Delivery</span></span> 
and the administration date.</li>
  <li>Aligns preterm and full-term infants to a common developmental reference.</li>
</ul>
</td>
<td><span class="pill-badge">V02+</span></td>
</tr>
</tbody>
</table>


#### <i class="fa-solid fa-folder-open header-icon"></i> FILE-BASED DATA <i>(age at data acquisition)</i>

<!-- FILE-BASED DATA -->
<table class="table-no-vertical-lines">
<thead>
<tr>
<th>Variable</th>
<th>Description</th>
<th>Visit</th>
</tr>
</thead>
<tbody>

<tr>
<td>
Adjusted Age at Time of Scan<br>
<code>age_adjusted</code>
</td>
<td style="word-wrap: break-word; white-space: normal;">Time in days between <span class="tooltip">EDD<span class="tooltiptext">Estimated Date of Delivery</span></span> and the acquisition date.
</td>
<td><span class="pill-badge">V02+</span></td>
</tr>

<tr>
<td>
Chronological Age at Time of Scan<br>
<code>age</code>
</td>
<td style="word-wrap: break-word; white-space: normal;">Age in years (3 decimal places) at acquisition, calculated as: total elapsed days (rounded down) ÷ 365.25. Based on a jittered DOB (±7 days) to protect participant privacy.
</td>
<td><span class="pill-badge">V02+</span></td>
</tr>

</tbody>
</table>


