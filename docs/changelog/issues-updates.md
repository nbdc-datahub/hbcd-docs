<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>

# Known Issues & Pending Updates 

The tables below summarize known issues affecting the current data release and pending updates across study instruments. Entries are organized by domain and include the expected release in which each fix or update will be implemented. This page is updated regularly as new issues are reported. **To ask a question or report an issue, please submit a ticket through the [Help Center in the NBDC Data Access Platform](https://nbdc.lassoinformatics.com/issue-tracker)**.

---

<p style="font-size: 1.2em; color: #555; text-align: center; line-height: 2;">
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i> = Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Pending Update &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.1em;"></i> = Target Release for Fix
</p>
    
---

### Behavior & Child-Caregiver Interaction

<table class="compact-table-no-vertical-lines issues">
<thead>
<tr>
<th>Table</th>
<th>Summary</th>
<th><i class="fa-solid fa-location-crosshairs icon-crosshairs"></i></th></tr>
</thead>
<tbody>

<tr>
<td>ecPROMIS CC</td>
<td><i class="fas fa-bug icon-bug"></i>
N=12 V03 participants with &lt;3 item responses are incorrectly scored as <code>0</code> in <code>mh_cg_pms__cc__inf</code>; set values to null prior to analysis.</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>

<tr>
<td>ERICA</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>
Addition of all age and <code>date_taken</code> fields (currently excluded due to use of coding rather than visit dates).</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>

<tr>
<td>ERICA</td>
<td>
<i class="fa-solid fa-rotate icon-rotate"></i>
A future release will integrate reliability codes into the primary coding dataset. Until then, users must perform this integration manually - see the ERICA <a href="../../instruments/bcgi/erica/#warning">Data Warning</a> for instructions.
Instructions include cleaning the current files to exclude n=44 participants with incorrect code values (data entry/form errors) and capping <code>b_raw</code> values at 3.0 (n=3 participants), also to be corrected in the next release.
</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>

<tr>
<td>FAD</td>
<td><i class="fas fa-bug icon-bug"></i>
N=4 V06 participants with &lt;3 item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>

<tr>
<td>MAPS-TL (&lt;1yr)</td>
<td><i class="fas fa-bug icon-bug"></i>
N=4 participants with no item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>

<tr>
<td>MAPS-TL (Tod)</td>
<td><i class="fas fa-bug icon-bug"></i>
Pro-rated scoring for <code>mh_cg_mapdb__tod</code> not yet implemented; N=16 participants missing scores.</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>

</tbody></table>

### Biospecimens & Omics
<table class="compact-table-no-vertical-lines issues">
<thead>
<tr>
<th>Table</th>
<th>Summary</th>
<th><i class="fa-solid fa-location-crosshairs icon-crosshairs"></i></th></tr>
</thead>
<tbody>
<tr>
<td>Nails</td>
<td><i class="fas fa-bug icon-bug"></i> Nail type is <code>4</code> (Unknown) in the main results table (<code>*_nails_results</code>) and should be obtained from the specimen table (<code>*_nails_type</code>).</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
</tbody></table>


### Demographics
<table class="compact-table-no-vertical-lines issues">
<thead>
<tr>
<th>Table</th>
<th>Summary</th>
<th><i class="fa-solid fa-location-crosshairs icon-crosshairs"></i></th></tr>
</thead>
<tbody>

<tr>
<td>Basic Demo</td>
<td><i class="fas fa-bug icon-bug"></i> N=14 participants in <code>sed_basic_demographics</code> have a Maternal Age at V01 of 0; exclude these values from analyses until corrected.</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td>RESTRUCTURE</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>
Demographics domain tables will be restructured to organize variables as either longitudinal measures that change over time or global, static measures such as sex assigned at birth.</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
</tbody></table>

### EEG & MRI
<table class="compact-table-no-vertical-lines issues">
<thead>
<tr>
<th>Table/Topic</th>
<th>Summary</th>
<th><i class="fa-solid fa-location-crosshairs icon-crosshairs"></i></th></tr>
</thead>
<tbody>

<tr>
<td>EEG age fields</td>
<td><i class="fas fa-bug icon-bug"></i> Chronological and adjusted age fall outside of 3-9 months in N=74 V03 sessions (site entry errors); exclude age values prior to analysis.</td>
<td><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>

<tr>
<td>MRI Run ID</td>
<td><i class="fas fa-bug icon-bug"></i> Run ID may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
<td><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr>
<td>QSIRecon</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Tabulated data for QSIRecon (participant data combined across derivative files into single tidy table) will be provided in a future release.</td>
<td><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr>
<td>Scanner Info</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> MRI scanner information across participants will be provided in a dedicated 'MRI Info' table similar to the <a href="https://docs.abcdstudy.org/latest/documentation/imaging/admin.html#mr_y_adm__info">ABCD study </a>.</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td>Source DICOMs</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Add source DICOMs for all MRI imaging modalities.</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
</tbody></table>


### General
<table class="compact-table-no-vertical-lines issues">
<thead>
<tr>
<th>Table</th>
<th>Summary</th>
<th><i class="fa-solid fa-location-crosshairs icon-crosshairs"></i></th></tr>
</thead>
<tbody>

<tr>
<td>Implausible GA</td>
<td><i class="fas fa-bug icon-bug"></i>
Some participants have implausible <code>gestational_age</code> values at V01 for one or more instruments. Until corrected, review GA distribution to exclude outliers from analysis (should be positive and generally &lt; 45 weeks).</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td>Instruction</td>
<td><i class="fas fa-bug icon-bug"></i>
The 'instruction' data dictionary element is currently blank.</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td>Multibirth Cohorts</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>
Missing instrument fields for Sibling cohorts will be populated and <em>FamilyID</em> will be added to help identify siblings - <a href="https://docs.hbcdstudy.org/latest/instruments/demo/visitinfo/#warning">see details</a>.</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td>Score text</td>
<td><i class="fas fa-bug icon-bug"></i>
Score fields may contain text when score values are missing; to be moved to 'notes' field (impacts ecPROMIS-PAGS; MAPS-TL; SPM-2).</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td>Sequence Field</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>
The currently included Sequence field is blank across all instruments and will be removed.</td>
<td><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
</tbody></table>

### Neurocognition &amp; Language
<table class="compact-table-no-vertical-lines issues">
<thead>
<tr>
<th>Table</th>
<th>Summary</th>
<th><i class="fa-solid fa-location-crosshairs icon-crosshairs"></i></th></tr>
</thead>
<tbody>

<tr>
<td>Bayley-4</td>
<td><i class="fas fa-bug icon-bug"></i>
Remove invalid scores of <code>-9999</code>; until resolved, users should remove this participant data prior to analysis.
</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>

<tr>
<td>MLDS</td>
<td><i class="fas fa-bug icon-bug"></i>
Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) includes implausible values: exclude values &gt;168 hours from analysis.</td>
<td><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
</tbody></table>

### Physical Health
<table class="compact-table-no-vertical-lines issues">
<thead>
<tr>
<th>Table</th>
<th>Summary</th>
<th><i class="fa-solid fa-location-crosshairs icon-crosshairs"></i></th></tr>
</thead>
<tbody>

<tr>
<td>Growth</td>
<td><i class="fas fa-bug icon-bug"></i> The data dictionary element <code>type_data</code> for <code>average_bmi</code> will be corrected to <code>double</code> (currently=<code>character</code>).</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td>Growth</td>
<td><i class="fas fa-bug icon-bug"></i> <code>ph_ch_anthro</code> filter ranges allow biologically implausible values (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Range Checks</a>) and will updated to be age/visit-specific </td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td>Growth</td>
<td><i class="fas fa-bug icon-bug"></i> Adjusted age contains N=303 "unknown missing" values that are also missing 'Date of Administration'.</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td>BISQ-SF</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>
Add Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
<td><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>

<tr>
<td>Growth</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>
Add sex-specific birth weight to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Sex-Specific Birthweight for GA</a>).</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td>Vision Screener</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>
Add more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>
<td><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr>
<td>ecPROMIS- Sleep</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>
Add <code>ph_cg_pms__sleep</code>  summary scores</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
</tbody></table>


### Pregnancy & Environmental Exposure
<table class="compact-table-no-vertical-lines issues">
<thead>
<tr>
<th>Table</th>
<th>Summary</th>
<th><i class="fa-solid fa-location-crosshairs icon-crosshairs"></i></th></tr>
</thead>
<tbody>

<tr>
<td>EPDS</td>
<td><i class="fas fa-bug icon-bug"></i>
Inconsistent scoring: (1) item responses present, but score is null (N=1); (2) all items null, but score is <code>0</code> (N≥3).</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td>Healthv2 Preg</td>
<td><i class="fas fa-bug icon-bug"></i>
The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping.</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td>Healthv2 Preg</td>
<td><i class="fas fa-bug icon-bug"></i>
Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank.</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td>TLFB</td>
<td><i class="fas fa-bug icon-bug"></i>
PNR data were incorrectly reported using TLFB versions 1/2 and will be updated to <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3">version 3 specific to PNR</a>.</td>
<td><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr>
<td>PEX Health</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>
ICD codes for the <code>pex_bm_health*</code>  tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>
</tbody></table>

### Social & Environmental Determinants
<table class="compact-table-no-vertical-lines issues">
<thead>
<tr>
<th>Table</th>
<th>Summary</th>
<th><i class="fa-solid fa-location-crosshairs icon-crosshairs"></i></th></tr>
</thead>
<tbody>

<tr>
<td>Demo</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Add household roster fields capturing the sex of listed individuals (adult &amp; child tables).</td>
<td><span class='pr-pill pr-general'>3</span></td>
</tr>

</tbody></table><!-- END KNOWN_ISSUES_TABLE -->