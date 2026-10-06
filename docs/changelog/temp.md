<!-- TABLE -->
<table id="archive-table" class="compact-table-no-vertical-lines">
<thead>
<tr>
<th class="archive-sort" data-sort="domain" width="5%">Domain</th>
<th class="archive-sort" data-sort="topic">Table/Topic</th>
<th class="archive-sort" data-sort="summary" width="60%">Summary</th>
</thead>
<tbody>

<!-- BR30.1 -->
<tr>
<td>PEX</td>
<td>EPDS</td>
<td><i class="fas fa-bug icon-bug"></i> Inconsistent scoring: (1) item responses present, but score is null (N=1); (2) all items null, but score is <code>0</code> (N≥3).</td>

<tr>
<td>Demo</td>
<td>Static table</td>
<td><i class="fas fa-bug icon-bug"></i> Corrected values for the <code>screen_race_multi__*</code> variables (formerly were almost entirely coded as '0').</td>
</tr>

</tbody>
</table>







<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Issue Resolved (Table/Topic)</th>
<th>Summary</th>
</tr>
</thead>
<tbody>

<tr class="domain-row">
<td colspan="2"><strong>Participant Derived</strong></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> Basic Demo</td>
<td>N=14 participants in <code>sed_basic_demographics</code> have a Maternal Age at V01 of 0; exclude these values from analyses until corrected.</td>
</tr>
<tr>

<td><i class="fas fa-bug icon-bug"></i> Static table</td>
<td>The <code>screen_race_multi__*</code> variables are almost entirely coded as '0' and should not be used for analysis. Users interested in race and ethnicity information should instead use the corresponding derived ACS race and ethnicity variable. Values will be corrected in a future release.</td>
</tr>

<tr>
<td><i class="fas fa-bug icon-bug"></i> TLFB</td>
<td>PNR data were incorrectly reported using TLFB versions 1/2 and will be updated to <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3">version 3 specific to PNR</a></td>
</tr>

<tr>
<td><i class="fas fa-bug icon-bug"></i> Visit Info</td>
<td>Harmonize participant status and withdrawal fields</td>
</tr>

<!-- MRI -->

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Raw QC Metrics</td>
<td>Raw MR data QC metrics provided in the raw BIDS SCANS TSV files will be combined into a single table across participants/sessions.</td>
</tr>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Scanner info</td>
<td>Scanner metadata, currently available within the raw BIDS Scans TSV files, will be additionally provided within the tabulated data for ease of access (see <a href="#infobbox">Participant Derived</a> domain info on this page).</td>
</tr>

<tr class="domain-row">
<td colspan="2"><strong>Neurocognition &amp; Language</strong></td>
</tr>

<tr>
<td><i class="fas fa-bug icon-bug"></i> CDI</td>
<td>Percentiles incorrectly converted for N=36 cases, resulting in values &gt;100 ('Adjusted Percentile' incorrectly parsed from 'Total Produced' instead of 'Total Produced Percentile-sex (adjusted)')</td>
</tr>

<tr>
<td><i class="fas fa-bug icon-bug"></i> MLDS</td>
<td>Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) includes implausible values due to data entry errors. Exclude values &gt;168 hours from analysis.</td>
</tr>


<tr class="domain-row">
<td colspan="2"><strong>Physical Health</strong></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> Anthropometrics</td>

<td>Adjusted age contains N=303 "unknown missing" values that are also missing 'Date of Administration'.</td>

</tr>

<tr>

<td><i class="fas fa-bug icon-bug"></i> Anthropometrics</td>

<td>The data dictionary element <code>type_data</code> for <code>average_bmi</code> will be corrected to <code>double</code> (currently=<code>character</code>).</td>

</tr>

<tr>

<td><i class="fa-solid fa-rotate icon-rotate"></i> Anthropometrics</td>

<td>Add sex-specific birth weight to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Sex-Specific Birthweight for GA</a>).</td>

</tr>

<tr>

<td><i class="fa-solid fa-rotate icon-rotate"></i> BISQ-SF</td>

<td>Add Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>

</tr>

<tr>

<td><i class="fa-solid fa-rotate icon-rotate"></i> Child Nutrition</td>

<td>Addition of the Child Nutrition Questionnaire.</td>

</tr>

<tr>

<td><i class="fa-solid fa-rotate icon-rotate"></i> Med History V1</td>

<td>Addition of V06</td>

</tr>

<tr>

<td><i class="fa-solid fa-rotate icon-rotate"></i> PEDsQL</td>

<td>Addition of the PEDsQL</td>

</tr>

<tr>

<td><i class="fa-solid fa-rotate icon-rotate"></i> Vision Screener</td>

<td>Add more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>

</tr>

<tr class="domain-row">

<td colspan="2"><strong>Pregnancy &amp; Environmental Exposure</strong></td>

</tr>

<tr>

<td><i class="fas fa-bug icon-bug"></i> EPDS</td>

<td>Inconsistent scoring: (1) item responses present, but score is null (N=1); (2) all items null, but score is <code>0</code> (N≥3).</td>

</tr>

<tr>

<td><i class="fas fa-bug icon-bug"></i> Healthv2 Preg</td>

<td>The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping.</td>

</tr>

<tr>

<td><i class="fas fa-bug icon-bug"></i> Healthv2 Preg</td>

<td>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank.</td>

</tr>

<tr>

<td><i class="fa-solid fa-rotate icon-rotate"></i> PEX Health</td>

<td>ICD codes for the <code>pex_bm_health*</code> tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></td>

</tr>

<tr class="domain-row">

<td colspan="2"><strong>Social &amp; Environmental Determinants</strong></td>

</tr>

<tr>

<td><i class="fas fa-bug icon-bug"></i> Demo</td>

<td>Roster was inappropriately collected at V02/V03 for all cohorts and should have been restricted to V02 PNRs and alternate caregiver cohorts; to be excluded.</td>

</tr>

<tr>
<td><i class="fas fa-bug icon-bug"></i> eHITS</td>
<td>Participants missing all item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> GLED</td>
<td>Addition of Geocoded Linkage from Home and Work Addresses</td>
</tr>
</tbody>
</table>
