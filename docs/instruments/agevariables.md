# Age Variable Definitions

Separate variables reporting age are included in Basic Demographics (global, single-point variables), tabulated data (age variables at time of instrument administration), and file-based metadata (age variables at time of MR/EEG/wearable sensor data acquisition). See details for each below.

## Basic Demographics

[Basic Demographics](demo/basicdemo.md) (`sed_basic_demographics`), derived from multiple sources/instruments, includes global, single-point variables that do not vary over time (e.g. gestational age of the child at delivery). Fields reporting age are computed from administrative records collected at screening, including: **Maternal Age at V01 (MAV01)**, **Maternal Age at Delivery (MAD)**, and **Gestational age at delivery (GAD)**. See full details in Basic Demographics - [Age, Sex, & Other Variables](demo/basicdemo.md#age-sec-other-variables).

## Tabulated Instrument Data

All [tabulated data](../datacuration/phenotypes.md) include the following fields that report the age of the **child participants** at the time of instrument administration.

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th style="width: 20%; padding: 5px; text-align: center;">Name</th>
        <th style="width: 10%; padding: 5px; text-align: center;">Variable Name</th>
        <th style="width: 30%; padding: 5px; text-align: center;">Description</th>
        <th style="width: 20%; padding: 5px; text-align: center;">Unit & Calculation</th>
        <th style="width: 10%; padding: 5px; text-align: center;">Visit(s)</th>
      </tr>
    </thead>
    <tbody>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Gestational Age at Administration (GAA)</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>{instrument}_gestational_age</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Time from the first day of the birth parent's <span class="tooltip">LMP
		<span class="tooltiptext">Last menstrual period, estimated as EDD minus 280 days</span>
	  </span> to the instrument administration date.
    <span class="tooltip">Max 4 week variation
		<span class="tooltiptext">Varies no more than 4 weeks across protocol elements except when protocol exceptions were granted</span>
	  </span>
    </td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Whole weeks, rounded down to the nearest week</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V01 only</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Chronological Age at Administration</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>{instrument}_candidate_age</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Time from birth (with the birthdate jittered up to 7 days to mitigate identification risks) to the date of instrument administration</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><span class="tooltip">Years
		<span class="tooltiptext">Reporting in years, rather than months, ensures consistency across developmental stages (e.g., toddlerhood, childhood), while three-decimal precision compensates for birthdate adjustments, yielding values closer to actual age.</span></span> (to 3 decimal places), calculated by dividing the total days elapsed (rounded down) by 365.25</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V02 onward</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Adjusted Chronological Age at Administration (ACAA)</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>{instrument}_adjusted_age</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Time elapsed between the <span class="tooltip">EDD
		<span class="tooltiptext">estimated date of delivery</span>
	  </span> and date of instrument administration</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Whole weeks, rounded down to the nearest week</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V02 onward</td>
</tr>
</tbody>
</table>

## Raw File-Based Data

Raw <span class="tooltip">file-based data<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> includes MRI, MRS, EEG, and motion/accelerometry data acquired from the child participants ([see details](../datacuration/file-based-data.md#raw-bids)). For visits V02 onward (*data unavailable for prenatal visit V01*), the age of the child at the time of data acquisition is reported in the session- and scan-level `.tsv` files that accompany these data ([see details](../datacuration/file-based-data.md#participant-session-scan-level-data)).

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th style="width: 20%; padding: 5px; text-align: center;">Name</th>
        <th style="width: 10%; padding: 5px; text-align: center;">Variable Name</th>
        <th style="width: 30%; padding: 5px; text-align: center;">Description</th>
        <th style="width: 20%; padding: 5px; text-align: center;">Unit & Calculation</th>
        <th style="width: 10%; padding: 5px; text-align: center;">Visit(s)</th>
      </tr>
    </thead>
    <tbody>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Adjusted Age at Time of Scan</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>age_adjusted</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Time from <span class="tooltip">EDD
		<span class="tooltiptext">estimated date of delivery</span>
	  </span> to the date of data acquisition</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Days (not rounded)</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V02 onward</td>
</tr>
<tr>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Chronological Age at Time of Scan</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><code>age</code></td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">Time from birth (with the birthdate jittered up to 7 days to mitigate identification risks) to the date of data acquisition.</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;"><span class="tooltip">Years
		<span class="tooltiptext">Reporting in years, rather than months, ensures consistency across developmental stages (e.g., toddlerhood, childhood), while 3-decimal precision compensates for birthdate adjustments, yielding values closer to actual age.</span></span> (to three decimal places), calculated by dividing the total days elapsed (rounded down) by 365.25</td>
<td style="padding: 8px; word-wrap: break-word; white-space: normal;">V02 onward</td>
</tr>
</tbody>
</table>