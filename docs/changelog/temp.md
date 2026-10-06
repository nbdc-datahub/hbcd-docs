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
<td>SED</td>
<td>eHITS</td>
<td><i class="fas fa-bug icon-bug"></i> Participants missing all item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
</tr>
<tr>
<td>PEX</td>
<td>EPDS</td>
<td><i class="fas fa-bug icon-bug"></i> Inconsistent scoring: (1) item responses present, but score is null (N=1); (2) all items null, but score is <code>0</code> (N≥3).</td>

<tr>
<td>Demo</td>
<td>Static table</td>
<td><i class="fas fa-bug icon-bug"></i> Corrected values for the <code>screen_race_multi__*</code> variables (formerly were almost entirely coded as '0').</td>
</tr>


<tr data-type="update">
<td>EEG</td>
<td>MADE v1.7.0</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> HBCD-MADE derivatives processed through updated version v1.7.0</td>
</tr>



</tbody>
</table>




<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>ID</th>
<th>Table/Topic</th>
<th>Summary</th>
</tr>
</thead>
<tbody>

<tr class="domain-row">
<td colspan="3"><strong>All Data / General</strong></td>
</tr>
<tr>
<td>ID-83</td>
<td><i class="fas fa-bug icon-bug"></i> Incorrect JSONs</td>
<td>Metadata field values were corrected for several instruments, but are not yet corrected in the JSON files. IN PARTICULAR, PLEASE CHECK <code>type_data</code> CAREFULLY as an incorrect data type may impact analyses. Impacted instruments include: <strong>APA 1/2</strong>, <strong>Bayley-4</strong>, and <strong>EEG Form-2</strong>. See details in <a href="../release-notes/#data-warning">Release Notes</a>.</td>
</tr>
<tr>
<td>ID-142</td>
<td><i class="fas fa-bug icon-bug"></i> Instruction</td>
<td>The 'instruction' data dictionary element is currently blank.</td>
</tr>
<tr>
<td>ID-22</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Blank Fields for Siblings</td>
<td>Family-level (i.e., non-child-specific) instrument fields are currently populated only for the Main Child, not sibling records (e.g., HBCD Multiple Birth – Sibling). Until resolved, users should obtain family-level values for sibling participants from the corresponding Main Child record. See the participant ID mapping in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
</tr>
<tr>
<td>ID-84</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> FamilyID</td>
<td>A <code>FamilyID</code> field will be added to instruments to identify sibling relationships. Until then, sibling ID mapping (Main Child vs Sibling) is provided in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
</tr>
<tr>
<td>ID-110</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Sequence Field</td>
<td>The currently included Sequence field is blank across all instruments and will be removed.</td>
</tr>
<tr class="domain-row">
<td colspan="3"><strong>Behavior &amp; Child-Caregiver Interaction</strong></td>
</tr>
<tr>
<td>ID-27</td>
<td><i class="fas fa-bug icon-bug"></i> ecPROMIS CC</td>
<td>N=12 V03 participants with &lt;3 item responses are incorrectly scored as <code>0</code> in <code>mh_cg_pms__cc__inf</code>; set values to null prior to analysis.</td>
</tr>
<tr>
<td>ID-24</td>
<td><i class="fas fa-bug icon-bug"></i> FAD</td>
<td>N=4 V06 participants with &lt;3 item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
</tr>
<tr>
<td>ID-30</td>
<td><i class="fas fa-bug icon-bug"></i> MAPS-TL (&lt;1yr)</td>
<td>N=4 participants with no item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
</tr>
<tr>
<td>ID-146</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ECHO</td>
<td>Addition of the Early Child Care and Education</td>
</tr>
<tr>
<td>ID-68</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> MAPS-EASI</td>
<td>Addition of the MAPS-EASI- Toddler</td>
</tr>
<tr>
<td>ID-26</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> MAPS-TL (Tod)</td>
<td>Pro-rated scoring for <code>mh_cg_mapdb__tod</code> not yet implemented; N=16 participants missing scores.</td>
</tr>
<tr>
<td>ID-69</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> MCHAT</td>
<td>Addition of the Modified Checklist for Autism in Toddlers</td>
</tr>
<tr class="domain-row">
<td colspan="3"><strong>Biospecimens &amp; Omics</strong></td>
</tr>
<tr>
<td>ID-42</td>
<td><i class="fas fa-bug icon-bug"></i> Nails</td>
<td>Nail type is <code>4</code> (Unknown) in the main results table (<code>*_nails_results</code>) and should be obtained from the specimen table (<code>*_nails_type</code>).</td>
</tr>
<tr>
<td>ID-44</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Blood</td>
<td>Inclusion of Blood Spot Card Results data from USDTL.</td>
</tr>
<tr class="domain-row">
<td colspan="3"><strong>Demographics</strong></td>
</tr>
<tr>
<td>ID-34</td>
<td><i class="fas fa-bug icon-bug"></i> Basic Demo</td>
<td>N=14 participants in <code>sed_basic_demographics</code> have a Maternal Age at V01 of 0; exclude these values from analyses until corrected.</td>
</tr>
<tr>
<td>ID-81</td>
<td><i class="fas fa-bug icon-bug"></i> Static table</td>
<td>The <code>screen_race_multi__*</code> variables are almost entirely coded as '0' and should not be used for analysis. Users interested in race and ethnicity information should instead use the corresponding derived ACS race and ethnicity variable. Values will be corrected in a future release.</td>
</tr>
<tr>
<td>ID-37</td>
<td><i class="fas fa-bug icon-bug"></i> TLFB</td>
<td>PNR data were incorrectly reported using TLFB versions 1/2 and will be updated to <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3">version 3 specific to PNR</a></td>
</tr>
<tr>
<td>ID-79</td>
<td><i class="fas fa-bug icon-bug"></i> Visit Info</td>
<td>Harmonize participant status and withdrawal fields</td>
</tr>
<tr class="domain-row">
<td colspan="3"><strong>EEG</strong></td>
</tr>
<tr>
<td>ID-55</td>
<td><i class="fas fa-bug icon-bug"></i> Age fields</td>
<td>Chronological and adjusted age fall outside of 3-9 months in N=74 V03 sessions (site entry errors); exclude age values prior to analysis.</td>
</tr>
<tr>
<td>ID-655</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> MADE v1.7.0</td>
<td>HBCD-MADE derivatives processed through updated version v1.7.0</td>
</tr>
<tr class="domain-row">
<td colspan="3"><strong>MRI</strong></td>
</tr>
<tr>
<td>ID-154</td>
<td><i class="fas fa-bug icon-bug"></i> dMRI metadata</td>
<td><code>LargeDelta</code> and <code>SmallDelta</code> in the sidecars currently are set to vendor-specific values (which aren't always correct because the models have their own values) and will be updated to reflect accurate values.</td>
</tr>
<tr>
<td>ID-128</td>
<td><i class="fas fa-bug icon-bug"></i> Run ID</td>
<td>The <code>run-{X}</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
</tr>
<tr>
<td>ID-667</td>
<td><i class="fas fa-bug icon-bug"></i> Tabulated XCP-D</td>
<td>All 0s for numeric values in tabulated XCP-D derivatives</td>
</tr>
<tr>
<td>ID-87</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Postprocessing</td>
<td>Addition of individual functional network maps (generated with template matching) and <a href="https://modelarrayio.readthedocs.io/en/latest/">ModelArray</a> outputs for XCP-D for efficient voxel-wise statistical modeling.</td>
</tr>
<tr>
<td>ID-86</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> QSIRecon</td>
<td>Tabulated data for QSIRecon (participant data combined across derivative files into single tidy table) will be provided in a future release.</td>
</tr>
<tr>
<td>ID-155</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Raw QC Metrics</td>
<td>Raw MR data QC metrics provided in the raw BIDS SCANS TSV files will be combined into a single table across participants/sessions.</td>
</tr>
<tr>
<td>ID-108</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Scanner info</td>
<td>Scanner metadata, currently available within the raw BIDS Scans TSV files, will be additionally provided within the tabulated data for ease of access (see <a href="#infobbox">Participant Derived</a> domain info on this page).</td>
</tr>
<tr>
<td>ID-657</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Source DICOMs</td>
<td>Add source DICOMs for all imaging modalities.</td>
</tr>
<tr class="domain-row">
<td colspan="3"><strong>Neurocognition &amp; Language</strong></td>
</tr>
<tr>
<td>ID-54</td>
<td><i class="fas fa-bug icon-bug"></i> Bayley</td>
<td>Remove invalid scores of <code>-9999</code>; until resolved, users should remove this participant data prior to analysis.</td>
</tr>
<tr>
<td>ID-78</td>
<td><i class="fas fa-bug icon-bug"></i> CDI</td>
<td>Percentiles incorrectly converted for N=36 cases, resulting in values &gt;100 ('Adjusted Percentile' incorrectly parsed from 'Total Produced' instead of 'Total Produced Percentile-sex (adjusted)')</td>
</tr>
<tr>
<td>ID-119</td>
<td><i class="fas fa-bug icon-bug"></i> MLDS</td>
<td>Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) includes implausible values due to data entry errors. Exclude values &gt;168 hours from analysis.</td>
</tr>
<tr>
<td>ID-661</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> CDI-2</td>
<td>Addition of the MacArthur-Bates CDI-2 Language</td>
</tr>
<tr>
<td>ID-63</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Deferred Imitation</td>
<td>Addition of instrument: Deferred Imitation Task: Gong and Berry-Go-Round</td>
</tr>
<tr class="domain-row">
<td colspan="3"><strong>Novel Tech &amp; Wearable Sensors</strong></td>
</tr>
<tr>
<td>ID-654</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> GABI</td>
<td>Addition of raw BIDS data for GABI (infant heart rate).</td>
</tr>
<tr class="domain-row">
<td colspan="3"><strong>Physical Health</strong></td>
</tr>
<tr>
<td>ID-33</td>
<td><i class="fas fa-bug icon-bug"></i> Anthropometrics</td>
<td>Adjusted age contains N=303 "unknown missing" values that are also missing 'Date of Administration'.</td>
</tr>
<tr>
<td>ID-47</td>
<td><i class="fas fa-bug icon-bug"></i> Anthropometrics</td>
<td>The data dictionary element <code>type_data</code> for <code>average_bmi</code> will be corrected to <code>double</code> (currently=<code>character</code>).</td>
</tr>
<tr>
<td>ID-20</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Anthropometrics</td>
<td>Add sex-specific birth weight to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Sex-Specific Birthweight for GA</a>).</td>
</tr>
<tr>
<td>ID-134</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> BISQ-SF</td>
<td>Add Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
</tr>
<tr>
<td>ID-62</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Child Nutrition</td>
<td>Addition of the Child Nutrition Questionnaire.</td>
</tr>
<tr>
<td>ID-662</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Med History V1</td>
<td>Addition of V06</td>
</tr>
<tr>
<td>ID-70</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> PEDsQL</td>
<td>Addition of the PEDsQL</td>
</tr>
<tr>
<td>ID-109</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Vision Screener</td>
<td>Add more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>
</tr>
<tr class="domain-row">
<td colspan="3"><strong>Pregnancy &amp; Environmental Exposure</strong></td>
</tr>
<tr>
<td>ID-46</td>
<td><i class="fas fa-bug icon-bug"></i> EPDS</td>
<td>Inconsistent scoring: (1) item responses present, but score is null (N=1); (2) all items null, but score is <code>0</code> (N≥3).</td>
</tr>
<tr>
<td>ID-137</td>
<td><i class="fas fa-bug icon-bug"></i> Healthv2 Preg</td>
<td>The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping.</td>
</tr>
<tr>
<td>ID-138</td>
<td><i class="fas fa-bug icon-bug"></i> Healthv2 Preg</td>
<td>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank.</td>
</tr>
<tr>
<td>ID-43</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> PEX Health</td>
<td>ICD codes for the <code>pex_bm_health*</code> tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></td>
</tr>
<tr class="domain-row">
<td colspan="3"><strong>Social &amp; Environmental Determinants</strong></td>
</tr>
<tr>
<td>ID-60</td>
<td><i class="fas fa-bug icon-bug"></i> Demo</td>
<td>Roster was inappropriately collected at V02/V03 for all cohorts and should have been restricted to V02 PNRs and alternate caregiver cohorts; to be excluded.</td>
</tr>
<tr>
<td>ID-38</td>
<td><i class="fas fa-bug icon-bug"></i> eHITS</td>
<td>Participants missing all item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
</tr>
<tr>
<td>ID-64</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Demo</td>
<td>Addition of V6 Adult and V6 Child Demographics</td>
</tr>
<tr>
<td>ID-66</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> GLED</td>
<td>Addition of Geocoded Linkage from Home and Work Addresses</td>
</tr>
<tr>
<td>ID-668</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Incarceration</td>
<td>Remove Incarceration Questionnaire (sample sizes currently too small, sensititive info included, etc.)</td>
</tr>
<tr>
<td>ID-67</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Incarceration</td>
<td>Addition of the Incarceration Questionnaire</td>
</tr>
</tbody>
</table>