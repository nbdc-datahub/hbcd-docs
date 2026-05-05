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

**All variables below refer to the child and describe the child’s age at either:**

- **Instrument administration** for tabulated instrument data
- **Time of scan/data acquisition** for file-based data (MR, EEG, and biosensor data, provided within [session- and scan-level metadata files](../datacuration/file-based-data.md#participant-session-scan-level-data))

---
<p style="text-align: center;">
<span class="pill-badge" style="background-color: pink;">V01</span>&nbsp;= Available Visit 1 only (prenatal) &nbsp;&nbsp;
<span class="pill-badge">V02+</span>&nbsp;= Available Visit 2 onward (post-birth)
</p>

<!-- TABULATED DATA -->
#### <i class="fa-solid fa-table header-icon"></i> TABULATED DATA 
<table class="compact-table-no-vertical-lines" style="font-size: 16px;">
<thead>
<tr>
</tr>
<tr>
<th>Variable Name</th>
<th>Variable Label</th>
<th>Description</th>
<th>Visit</th>
</tr>
</thead>
<tbody>

<tr>
<td>
  Gestational Age<br>
  <span class="subtle">at Administration</span>
</td>
<td><code>gestational_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
<ul>
  <li>Number of weeks (rounded down) between <span class="tooltip tooltip-right">LMP<span class="tooltiptext">First day of the birth parent's last menstrual period, estimated as EDD − 280 days</span></span> and the V01 administration date</li>
  <li>May vary by ≤4 weeks across protocol elements (except for protocol exceptions)</li>
  <li><i><b>Note:</b> May be negative if collected prior to the <span class="tooltip">EDD<span class="tooltiptext">Estimated Date of Delivery</span></span></i></li>
</ul>
</td>
<td><span class="pill-badge" style="background-color: pink;">V01</span></td>
</tr>
<tr>
<td>
  Chronological Age<br>
  <span class="subtle">at Administration</span>
</td>
<td><code>candidate_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
<ul>
  <li>Age in years (3 decimal places) at administration</li>
  <li>Calculated as: total elapsed days (rounded down) ÷ 365.25</li>
  <li>Based on a jittered DOB (±7 days) to protect participant privacy</li>
</ul>
</td>
<td><span class="pill-badge">V02+</span></td>
</tr>

<tr>
<td>
  Adjusted Chronological Age<br>
  <span class="subtle">at Administration</span>
</td>
<td><code>adjusted_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
<ul>
  <li>Number of weeks (rounded down) between <span class="tooltip">EDD<span class="tooltiptext">Estimated Date of Delivery</span></span> 
and the administration date</li>
  <li>Aligns preterm and full-term infants to a common developmental reference</li>
</ul>
</td>
<td><span class="pill-badge">V02+</span></td>
</tr>
</tbody>
</table>


#### <i class="fa-solid fa-folder-open header-icon"></i> FILE-BASED DATA

<!-- FILE-BASED DATA -->
<table class="compact-table-no-vertical-lines" style="font-size: 16px;">
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
<td>
  Adjusted Age
  <span class="subtle">at Time of Scan</span>
</td>
<td><code>age_adjusted</code></td>
<td>
    <ul>
    <li>Time in days between <span class="tooltip">EDD<span class="tooltiptext">Estimated Date of Delivery</span></span> and the acquisition date</li>
    </ul>
</td>
<td><span class="pill-badge">V02+</span></td>
</tr>

<tr>
<td>
  Chronological Age 
  <span class="subtle">at Time of Scan</span>
</td>
<td><code>age</code></td>
<td>
    <ul>
        <li>Age in years (3 decimal places) at acquisition</li>
        <li>Calculated as: total elapsed days (rounded down) ÷ 365.25</li>
        <li>Based on a jittered DOB (±7 days) to protect participant privacy</li>
    </ul>
</td>
<td><span class="pill-badge">V02+</span></td>
</tr>

</tbody>
</table>


