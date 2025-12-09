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

<div id="age-contexts" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i style="font-size: 0.9em;" class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Overview of Age Variable Contexts</span>
  <a class="anchor-link" href="#age-contexts" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<ul>
<li><strong>Administration</strong>: The date a study instrument was completed.  </li>
<li><strong>Data acquisition</strong>: The date of MR, EEG, or wearable sensor recording.  </li>
<li><strong>Adjusted age</strong>: Computed relative to the <strong>Estimated Date of Delivery (EDD)</strong> to align preterm and full-term infants to a common developmental reference.  </li>
<li><strong>Chronological age</strong>: Computed using a <strong>jittered date of birth (DOB)</strong> randomly shifted by up to 7 days to protect participant privacy without affecting analyses.  </li>
</ul>
</div>

---

## <i class="fa-solid fa-table"></i> Tabulated Data

Most <a href="../../datacuration/phenotypes/" target="_blank">tabulated datasets</a> include the following age variables describing the child’s age at the time of **instrument administration** (or **data acquisition** for tabulated data computed from imaging/EEG pipeline derivatives <a href="../../datacuration/overview/#warning" target="_blank"><i style="font-size: 0.85em;" class="fa-solid fa-arrow-up-right-from-square"></i></a>). The primary exception is tabulated data within the <a href="../#demo" target="_blank">Demographics domain</a> datasets; see [Basic Demographics](#basic-demographics) below. 

<p style="font-size: 0.9em; color: #555;">
<i class="fa-solid fa-baby"></i>&nbsp;= Variable refers to the child &nbsp;&nbsp;
<span class="pill-badge" style="background-color: pink;">V01</span>&nbsp;= Available Visit V01 only (prenatal) &nbsp;&nbsp;
<span class="pill-badge">V02+</span>&nbsp;= Available Visit V02 onward (post-birth)
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
<td><i class="fa-solid fa-baby"></i>&nbsp; Gestational Age at Administration<br><code style="margin-left: 19px;">gestational_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Time elapsed (<b>whole weeks</b>, rounded down) between the <span class="tooltip tooltip-left">LMP<span class="tooltiptext">First day of the birth parent's last menstrual period, estimated as EDD minus 280 days</span></span> and date of instrument administration. Varies no more than 4 weeks across protocol elements except when protocol exceptions were granted. <span class="pill-badge" style="background-color: pink;">V01</span>
</td>
</tr>
<tr>
<td><i class="fa-solid fa-baby"></i>&nbsp; Chronological Age at Administration<br><code style="margin-left: 19px;">candidate_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Age in <b>years<sup><b>1</b></sup></b> at the time of instrument administration. Computed using a jittered DOB shifted by up to 7 days to protect participant privacy. <span class="pill-badge">V02+</span>
</td>
</tr>
<tr>
<td><i class="fa-solid fa-baby"></i>&nbsp; Adjusted Chronological Age at Administration<br><code style="margin-left: 19px;">adjusted_age</code></td>
<td style="word-wrap: break-word; white-space: normal;">
  Time elapsed (<b>whole weeks</b>, rounded down) between the <b>EDD</b> and date of instrument administration. <span class="pill-badge">V02+</span>
</td>
</tr>
</tbody>
<tfoot>
<tr>
  <td colspan="2" style="word-wrap: break-word; white-space: normal; border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
    <sup><b>1</b></sup> Years are to three decimal places, calculated by dividing the total days elapsed (rounded down) by 365.25.
  </td>
</tr>
</tfoot>
</table>

## <i class="fa-solid fa-folder-open"></i> File-Based Metadata

Age variables in [raw file-based datasets](../datacuration/file-based-data.md#raw-bids) describe the child’s age at the time of **data acquisition** for MR, EEG, and wearable sensor recordings. These values are stored in [session/scan-level TSV metadata files](../datacuration/file-based-data.md#participant-session-scan-level-data).  

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead>
<tr>
<th><strong>File-Based Data Variable</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><i class="fa-solid fa-baby"></i>&nbsp; Adjusted Age at Time of Scan (<code>age_adjusted</code>)</td>
<td style="word-wrap: break-word; white-space: normal;">
  Time in <b>days</b> elapsed between the <b>EDD</b> and date of data acquisition. <span class="pill-badge">V02+</span>
</td>
</tr>
<tr>
<td><i class="fa-solid fa-baby"></i>&nbsp; Chronological Age at Time of Scan (<code>age</code>)</td>
<td style="word-wrap: break-word; white-space: normal;">
  Age in <b>years<sup><b>1</b></sup></b> at the time of data acquisition. Computed using a jittered DOB shifted by up to 7 days to protect participant privacy. <span class="pill-badge">V02+</span>
</td>
</tr>
</tbody>
<tfoot>
<tr>
  <td colspan="2" style="word-wrap: break-word; white-space: normal; border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
    <sup><b>1</b></sup> Years are to three decimal places, calculated by dividing the total days elapsed (rounded down) by 365.25.
  </td>
</tr>
</tfoot>
</table>

## Basic Demographics

Datasets within the <a href="../#demo" target="_blank">Demographics <i style="font-size: 0.8em;" class="fa-solid fa-arrow-up-right-from-square"></i></a> domain, including Basic Demographics (`sed_basic_demographics`) and Visit Level Data (`par_visit_data`), combine information from multiple sources, including administrative data and study instruments. <a href="../demo/basicdemo/" target="_blank">Basic Demographics</a> (which provides global, single-point variables that do not vary over time, such as participant race/ethnicity) includes a distinct set of age variables that follow slightly different logic than those used in standard instrument datasets described above (e.g., how years and LMP-based ages are calculated). Visit Level Data does not include age variables.

<i>From <a href="../demo/basicdemo/#age-sex-other-variables" target="_blank">Basic Demographics – Age, Sex, & Other Variables</a>:</i>
<table class="compact-table-no-vertical-lines" style="width: 100%; table-layout: fixed; font-size: 15px; border: 2px solid #0086a0ff; border-radius: 8px; border-collapse: collapse;">
  <caption style="caption-side: top; padding: 6px; text-align: left; font-size: 0.9em; color: #555;">
    <i class="fa-solid fa-baby"></i>&nbsp;= Variable refers to the child &nbsp;&nbsp;
    <span class="pill-badge">V02+</span>&nbsp;= Available beginning Visit V02 (post-birth)
  </caption>
<thead>
<tr style="background-color: #f8f9f9;">
  <th style="width: 20%;">Construct</th>
  <th style="width: 20%;">Variable Name</th>
  <th style="width: 60%;">Description / Details</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Maternal Age at V01 (MAV01)</td>
  <td><code>mother_age_v01</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Birth parent's age in years<sup><b>1</b></sup> at scheduled date of the V01 visit. Derived from administrative records.</td>
</tr>
<tr>
  <td>Maternal Age at Delivery (MAD)</td>
  <td><code>mother_age_delivery</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Birth parent's age in years<sup><b>1</b></sup> at time of their child's delivery. Derived from administrative records.</td>
</tr>
<tr>
  <td><i class="fa-solid fa-baby"></i>&nbsp;Gestational age at delivery (GAD)</td>
  <td><code>gestational_age_delivery</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Time elapsed (whole weeks, rounded down) between the birth parent's <span class="tooltip tooltip-left">LMP<span class="tooltiptext">First day of the birth parent's last menstrual period</span></span> and child's DOB. Derived from administrative records. <span class="pill-badge">V02+</span></td>
</tr>
</tbody>
<tfoot><tr><td colspan="3" style="word-wrap: break-word; white-space: normal; padding: 10px 8px 6px 8px;">
  <sup><b>1</b></sup> Years are to 2 decimal places, calculated by dividing the number of whole months (rounded down) by 12</td></tr></tfoot>
</table>



