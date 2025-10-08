# Known Issues



---

## Issue Summary

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
<th>Domain</th>
<th>Issue</th>
<th>Fix Version</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>General</td>
<td>Instruction Metadata</td>
<td>TBD</td>
<td>🟡</td>
</tr>
<tr>
<td>Demographics</td>
<td>Mother Race Levels</td>
<td>R2.0</td>
<td>🟢</td>
</tr>
<tr>
<td>Demographics</td>
<td>Child Multi-Race / Multi-Ethnicity (ACS)</td>
<td>R2.0</td>
<td>🟢</td>
</tr>
<tr>
<td>Imaging Data</td>
<td>Run ID Order May Be Incorrect</td>
<td>R2.0</td>
<td>🟢</td>
</tr>
<tr>
<td>Neurocognition &amp; Language</td>
<td>SPM-2 Age Fields / Scores</td>
<td>R2.0</td>
<td>🟢</td>
</tr>
<tr>
<td>Pregnancy &amp; Exposure</td>
<td>ICD Labels Missing</td>
<td>R2.0</td>
<td>🟢</td>
</tr>
<tr>
<td>Social &amp; Environmental</td>
<td>PhenX Discrimination Survey Missing Data</td>
<td>R2.0</td>
<td>🟢</td>
</tr>
<tr>
<td>Visit Information</td>
<td>Invalid Withdrawal Dates</td>
<td>TBD</td>
<td>🟡</td>
</tr>
</tbody>
</table>

---



---

## Basic Demographics (`sed_basic_demographics`)

<details>
<summary><span style="color:#f97316;"><i class="fas fa-bug"></i></span> <b>Mother Race (<code>screen_mother_race</code>)</b> <span class="badge" style="background-color:#f59e0b; color:white;">Fix: R2.0</span></summary>

Erroneous inclusion of two levels for Hawaiian race (`2` = *Hawaiian*; `7` = *Native Hawaiian or Other Pacific Islander*).  
The `2 = Hawaiian` code was not a valid response option and can be ignored; no participants selected it.

</details>

<details>
<summary><span style="color:#f97316;"><i class="fas fa-bug"></i></span> <b>Child Multi-Race / Multi-Ethnicity (ACS)</b> <span class="badge" style="background-color:#f59e0b; color:white;">Fix: R2.0</span></summary>

**(#1)** Variables have the same data and levels. *Child Multi-Race* will be removed to resolve duplication.  
**(#2)** Variables are populated at V01 (before birth). V01 data will be removed in R2.0.

</details>

---

## 🧠 Imaging Data

<details>
<summary><span style="color:#be7215;"><i class="fas fa-bug"></i></span> <b>Run ID Order May Be Incorrect</b> <span class="badge" style="background-color:#f59e0b; color:white;">Fix: R2.0</span></summary>

For HBCD BIDS data with multiple runs, the `run-<label>` field may not reflect chronological acquisition order.  
This affects both **raw and processed** imaging/biosignal data as well as **derived tabulated** data.  

Despite this, data remain internally consistent — e.g., run IDs match between raw and processed datasets.

</details>

---

## 🗣️ Neurocognition & Language

<details>
<summary><span style="color:#f97316;"><i class="fas fa-bug"></i></span> <b>SPM-2 Age (<code>ncl_cg_spm2__inf</code>)</b> <span class="badge" style="background-color:#f59e0b; color:white;">Fix: R2.0</span></summary>

**(#1)** Age fields not currently included — refer to corresponding age variables in related datasets for the same time point.  
**(#2)** *T-scores* are now provided (see [1.1 Resolved Known Issues](../../changelog/releasenotes/#r1.1ngl)), but **STATUS SCORE** remains missing for all but one subscale. This will be added in R2.0.

</details>

---

## 🤰 Pregnancy & Exposure (Including Substance Use)

<details>
<summary><span style="color:#f97316;"><i class="fas fa-bug"></i></span> <b>ICD Code Names / Labels Inconsistently Provided</b> <span class="badge" style="background-color:#f59e0b; color:white;">Fix: R2.0</span></summary>

In cases where ICD codes are provided, corresponding names/labels are sometimes missing.  
Users can use external packages to merge ICD labels if needed:
- [Stata](https://www.stata.com/features/overview/icd/)
- [SAS](https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp)
- [R](https://www.rdocumentation.org/packages/icd/versions/3.3)

</details>

---

## 🌍 Social & Environmental Determinants

<details>
<summary><span style="color:#f97316;"><i class="fas fa-bug"></i></span> <b>Blank Cells in PhenX Discrimination Survey</b> <span class="badge" style="background-color:#f59e0b; color:white;">Fix: R2.0</span></summary>

For the PhenX+ Discrimination survey, the multi-select question  
(`sed_bm_phx__discr.006`: *"What do you think is the main reason for these experiences? If more than one main reason, check all that apply."*)  
is blank for some participants. This will be corrected in R2.0.

</details>

---

## 📅 Visit Information

<details>
<summary><span style="color:#f97316;"><i class="fas fa-bug"></i></span> <b>Invalid Participant Withdrawal Dates</b> <span class="badge" style="background-color:#9ca3af; color:white;">Expected Fix: TBD</span></summary>

Participants who did **not** withdraw from the study (value = “no” for `par_visit_data_participant_withdrawal`) have a sentinel value of `12/26/1999` in `par_visit_data_participant_withdrawal_date`.  
This indicates *no withdrawal* and can be safely ignored.  

Participants who withdrew (value = “yes”) have valid withdrawal dates and are unaffected.

</details>
