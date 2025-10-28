# Age Variable Definitions

This page defines how age is represented across HBCD datasets. Separate variables quantify (1) the child’s age at different points in the study during instrument administration, data acquisition, and at birth (i.e. gestational age) and (2) the mother's age at the scheduled V01 visit and delivery. 

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead>
<tr>
<th><strong>Dataset Type</strong></th>
<th><strong>Description</strong></th>
<th><strong>Variables</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tabulated Data</strong></td>
<td>Age at time of instrument administration</td>
<td><code>candidate_age</code><br><code>adjusted_age</code><br><code>gestational_age</code></td>
</tr>
<tr>
<td><strong>File-Based Data</strong></td>
<td>Age at MR, EEG, or wearable data acquisition</td>
<td><code>age</code><br><code>age_adjusted</code></td>
</tr>
<tr>
<td><strong>Basic Demographics</strong></td>
<td>Global, single-point age variables derived from administrative data</td>
<td><code>mother_age_v01</code><br><code>mother_age_delivery</code><br><code>gestational_age_delivery</code></td>
</tr>
</tbody>
</table>

## Overview of Age Variable Contexts

- **Administration**: The date a study instrument was completed.  
- **Data acquisition**: The date of MR, EEG, or wearable sensor recording.  
- **Adjusted age**: Computed relative to the **Estimated Date of Delivery (EDD)** to align preterm and full-term infants to a common developmental reference.  
- **Chronological age**: Computed using a **jittered date of birth (DOB)** shifted by up to 7 days to protect participant privacy without affecting analyses.  

---

## <i class="fa-solid fa-table"></i> Tabulated Data

Age variables in [tabulated datasets](../datacuration/phenotypes.md) describe the child’s age at the time of **instrument administration** or **data acquisition** for tabulated data computed from brain imaging and EEG pipeline derivatives (<a href="../../datacuration/overview/#warning" target="_blank">see details</a>). Note that the variables listed here are not applicable to the derived <a href="../#demo" target="_blank">Demographics domain</a> datasets; see [Basic Demographics](#basic-demographics) below. 

<p style="font-size: 0.9em; color: #555;">
<span class="pill-badge">V01</span>&nbsp;= Available for only Visit V01 (prenatal period) &nbsp;&nbsp;
<span class="pill-badge">V02+</span>&nbsp;= Available beginning Visit V02 (post-birth)
</p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead>
<tr>
<th><strong>Tabulated Data Variable</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Gestational Age at Administration<br><code>gestational_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Time elapsed (whole weeks, rounded down) between the <span class="tooltip">LMP<span class="tooltiptext">First day of the birth parent's last menstrual period, estimated as EDD minus 280 days</span></span> and the date of instrument administration. Varies no more than 4 weeks across protocol elements except when protocol exceptions were granted. <span class="pill-badge">V01</span>
</td>
</tr>
<tr>
<td>Chronological Age at Administration<br><code>candidate_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Age in years<sup><b>1</b></sup> at the time of instrument administration. Computed using a jittered DOB randomly shifted by up to 7 days to protect participant privacy. <span class="pill-badge">V02+</span>
</td>
</tr>
<tr>
<td>Adjusted Chronological Age at Administration<br><code>adjusted_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Time elapsed (whole weeks, rounded down) between the <span class="tooltip">EDD<span class="tooltiptext">Estimated Date of Delivery</span></span> and the date of instrument administration. <span class="pill-badge">V02+</span>
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

## <i class="fa-solid fa-folder-open"></i> File-Based Metadata

Age variables in [raw file-based datasets](../datacuration/file-based-data.md#raw-bids) describe the child’s age at the time of **data acquisition** for MR, EEG, and wearable sensor recordings. These values are stored in [session/scan-level TSV metadata files](../datacuration/file-based-data/#participant-session-scan-level-data).  

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead>
<tr>
<th><strong>File-Based Data Variable</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Adjusted Age at Time of Scan (<code>age_adjusted</code>)</td>
<td style="word-wrap: break-word; white-space: normal;">
  Time in days elapsed between the <span class="tooltip">EDD<span class="tooltiptext">Estimated Date of Delivery</span></span> and the date of data acquisition. <span class="pill-badge">V02+</span>
</td>
</tr>
<tr>
<td>Chronological Age at Time of Scan (<code>age</code>)</td>
<td style="word-wrap: break-word; white-space: normal;">
  Age in years<sup><b>1</b></sup> at the time of data acquisition. Computed using a jittered DOB randomly shifted by up to 7 days to protect participant privacy. <span class="pill-badge">V02+</span>
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

**Basic Demographics** (`sed_basic_demographics`), derived from multiple sources and instruments, provides **global, single-point variables** that do not vary over time (for example, gestational age at delivery). Fields reporting age are computed from administrative records collected at screening and include:  

- **Maternal Age at V01 (MAV01)**  
- **Maternal Age at Delivery (MAD)**  
- **Gestational Age at Delivery (GAD)**  

See full details in [**Basic Demographics – Age, Sex, & Other Variables**](demo/basicdemo.md#age-sex-other-variables).

> **Note:** Visit-level data in `par_visit_data` do not include age variables.



