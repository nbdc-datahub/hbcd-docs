<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}

body {
    margin: 3rem;
    font-family: sans-serif;
}
.compact-table-no-vertical-lines th:nth-child(4),
.compact-table-no-vertical-lines td:nth-child(4) {
text-align: center;
}
/* Archive controls */
.archive-controls {
    margin: 1.5rem 0 0.75rem;
    padding: 1rem 1.1rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    background: #f8f9fa;
}

.archive-controls-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    align-items: center;
}

.archive-search {
    flex: 1 1 280px;
    min-width: 220px;
}

.archive-controls input,
.archive-controls select,
.archive-controls button {
    box-sizing: border-box;
    height: 38px;
    border: 1px solid #cfd4da;
    border-radius: 5px;
    background: white;
    padding: 0 0.75rem;
    font: inherit;
    font-size: 0.9rem;
}

.archive-controls input:focus,
.archive-controls select:focus,
.archive-controls button:focus {
    outline: 2px solid rgba(25, 155, 214, 0.25);
    border-color: #199bd6;
}

.archive-controls button {
    cursor: pointer;
    font-weight: 600;
}

.archive-controls button:hover {
    background: #f1f3f5;
}

.archive-status {
    margin-top: 0.65rem;
    font-size: 0.85rem;
    color: #666;
}

.archive-sort {
    cursor: pointer;
    user-select: none;
    white-space: nowrap;
}

.archive-sort:hover {
    text-decoration: underline;
}

.archive-sort::after {
    content: " ↕";
    color: #999;
    font-size: 0.8em;
}

.archive-sort.sorted-asc::after {
    content: " ↑";
    color: #199bd6;
}

.archive-sort.sorted-desc::after {
    content: " ↓";
    color: #199bd6;
}

.archive-empty {
    display: none;
    padding: 2rem 1rem;
    text-align: center;
    color: #777;
    font-size: 0.95rem;
}

.archive-highlight {
    background: #fff3cd;
    border-radius: 2px;
}

@media (max-width: 700px) {
    .archive-controls-row {
    align-items: stretch;
    }

    .archive-controls input,
    .archive-controls select,
    .archive-controls button {
    width: 100%;
    }

    .archive-search {
    flex-basis: 100%;
    }
}
</style>


# Known Issues & Pending Updates 

The tables below summarize known issues affecting the current data release and pending updates across study instruments. Entries are organized by domain and include the expected release in which each fix or update will be implemented. This page is updated regularly as new issues are reported. **To ask a question or report an issue, please submit a ticket through the [Help Center in the NBDC Data Access Platform](https://nbdc.lassoinformatics.com/issue-tracker)**.


<p style="font-size: 1.2em; color: #555; text-align: center; line-height: 2;">
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i> = Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Pending Update
</p>

<div class="archive-controls" aria-label="Archive filters">
  <div class="archive-controls-row">
    <input
      id="archive-search"
      class="archive-search"
      type="search"
      placeholder="Search table, topic, or summary..."
      aria-label="Search archive"
    >
    <select id="archive-domain" aria-label="Filter by domain">
      <option value="">All domains</option>
    </select>
    <select id="archive-br" aria-label="Filter by release">
      <option value="">All releases</option>
    </select>
    <!-- ARCHIVE TYPE -->
    <select id="archive-type" aria-label="Filter by type">
      <option value="">All types</option>
      <option value="issue">Resolved Known Issues</option>
      <option value="update">Completed Pending Updates</option>
    </select>
    <button id="archive-reset" type="button">Clear filters</button>
  </div>
  <div id="archive-status" class="archive-status" aria-live="polite"></div>
  <div id="archive-empty" class="archive-empty">No matching entries found.</div>
</div>

<!-- TABLE -->

<table id="archive-table" class="compact-table-no-vertical-lines archive-table">

<!-- <table class="known-issues-table"> -->
<thead>
<tr>
<th>Domain</th>
<th>Table / Topic</th>
<th>Issue / Update</th>
<th>Target</th>
</tr>
</thead>

<tbody>
<tr>
<td>All/NA</td>
<td>Blank Fields for Siblings</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Family-level (i.e., non-child-specific) instrument fields are currently populated only for the Main Child, not sibling records (e.g., HBCD Multiple Birth – Sibling). Until resolved, users should obtain family-level values for sibling participants from the corresponding Main Child record. See the participant ID mapping in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td>3</td>
</tr>
<tr>
<td>All/NA</td>
<td>Implausible GA</td>
<td><i class="fas fa-bug icon-bug"></i> A small subset of participants have implausible <code>gestational_age</code> (V01 only) values for one or more instrument. Until corrected, review GA distribution to exclude outliers from analysis (should be positive and generally &lt; 45 weeks).</td>
<td>3</td>
</tr>
<tr>
<td>All/NA</td>
<td>Score text</td>
<td><i class="fas fa-bug icon-bug"></i> Text inappropriately located in score fields where score is missing to be moved to corresponding 'notes' field (impacts ecPROMIS-PAGS; MAPS-TL; SPM-2).</td>
<td>3</td>
</tr>
<tr>
<td>All/NA</td>
<td>Incorrect JSONs</td>
<td><i class="fas fa-bug icon-bug"></i> Metadata field values were corrected for several instruments, but are not yet corrected in the JSON files. IN PARTICULAR, PLEASE CHECK <code>type_data</code> CAREFULLY as an incorrect data type may impact analyses. Impacted instruments include: <strong>APA 1/2</strong>, <strong>Bayley-4</strong>, and <strong>EEG Form-2</strong>. See details in <a href="../release-notes/#data-warning">Release Notes</a>.</td>
<td>3</td>
</tr>
<tr>
<td>All/NA</td>
<td>FamilyID</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> A <code>FamilyID</code> field will be added to instruments to identify sibling relationships. Until then, sibling ID mapping (Main Child vs Sibling) is provided in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td>3</td>
</tr>
<tr>
<td>All/NA</td>
<td>Sequence Field</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> The currently included Sequence field is blank across all instruments and will be removed.</td>
<td></td>
</tr>
<tr>
<td>All/NA</td>
<td>Instruction</td>
<td><i class="fas fa-bug icon-bug"></i> The 'instruction' data dictionary element is currently blank.</td>
<td></td>
</tr>
<tr>
<td>BIO</td>
<td>Nails</td>
<td><i class="fas fa-bug icon-bug"></i> Nail type is <code>4</code> (Unknown) in the main results table (<code>*_nails_results</code>) and should be obtained from the specimen table (<code>*_nails_type</code>).</td>
<td>3</td>
</tr>
<tr>
<td>BIO</td>
<td>Blood</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Inclusion of Blood Spot Card Results data from USDTL.</td>
<td>3</td>
</tr>
<tr>
<td>Demo</td>
<td>Basic Demo</td>
<td><i class="fas fa-bug icon-bug"></i> N=14 participants in <code>sed_basic_demographics</code> have a Maternal Age at V01 of 0; exclude these values from analyses until corrected.</td>
<td>3</td>
</tr>
<tr>
<td>Demo</td>
<td>TLFB</td>
<td><i class="fas fa-bug icon-bug"></i> PNR data were incorrectly reported using TLFB versions 1/2 and will be updated to <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3">version 3 specific to PNR</a></td>
<td>3</td>
</tr>
<tr>
<td>Demo</td>
<td>Visit Info</td>
<td><i class="fas fa-bug icon-bug"></i> Harmonize participant status and withdrawal fields</td>
<td>3</td>
</tr>
<tr>
<td>Demo</td>
<td>Basic Demo</td>
<td><i class="fas fa-bug icon-bug"></i> The <code>screen_race_multi__*</code> variables are almost entirely coded as '0' and should not be used for analysis. Users interested in race and ethnicity information should instead use the corresponding derived ACS race and ethnicity variable. Values will be corrected in a future release.</td>
<td>3</td>
</tr>
<tr>
<td>EEG</td>
<td>Age fields</td>
<td><i class="fas fa-bug icon-bug"></i> Chronological and adjusted age fall outside of 3-9 months in N=74 V03 sessions (site entry errors); exclude age values prior to analysis.</td>
<td>3.1</td>
</tr>
<tr>
<td>EEG</td>
<td>MADE v1.7.0</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> HBCD-MADE derivatives processed through updated version v1.7.0</td>
<td>3</td>
</tr>
<tr>
<td>MH</td>
<td>ERICA</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> A future release will include reliability codes integrated into the primary coding dataset. Until then, users must perform this integration manually: see the ERICA Data Warning for instructions. Instructions include cleaning the current files to exclude n=44 participants with incorrect code values (data entry/form errors), capping <code>b_raw</code> values at 3.0 (n=3 participants), and removing the “Locomotor Ability” field (<code>mh_cg_erica_3_9m_locomotor_ability</code>), which has errors, also to be corrected in the next release.</td>
<td>3</td>
</tr>
<tr>
<td>MH</td>
<td>FAD</td>
<td><i class="fas fa-bug icon-bug"></i> N=4 V06 participants with &lt;3 item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td>3</td>
</tr>
<tr>
<td>MH</td>
<td>MAPS-TL (Tod)</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Pro-rated scoring for <code>mh_cg_mapdb__tod</code> not yet implemented; N=16 participants missing scores.</td>
<td>3</td>
</tr>
<tr>
<td>MH</td>
<td>ecPROMIS CC</td>
<td><i class="fas fa-bug icon-bug"></i> N=12 V03 participants with &lt;3 item responses are incorrectly scored as <code>0</code> in <code>mh_cg_pms__cc__inf</code>; set values to null prior to analysis.</td>
<td>3</td>
</tr>
<tr>
<td>MH</td>
<td>MAPS-TL (&lt;1yr)</td>
<td><i class="fas fa-bug icon-bug"></i> N=4 participants with no item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td>3</td>
</tr>
<tr>
<td>MH</td>
<td>ERICA</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Add all age and <code>date_taken</code> fields (currently excluded due to use of coding rather than visit dates).</td>
<td>3</td>
</tr>
<tr>
<td>MH</td>
<td>MAPS-EASI</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of the MAPS-EASI- Toddler</td>
<td>3</td>
</tr>
<tr>
<td>MH</td>
<td>ECHO</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of the Early Child Care and Education</td>
<td></td>
</tr>
<tr>
<td>MH</td>
<td>MCHAT</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of the Modified Checklist for Autism in Toddlers</td>
<td>3</td>
</tr>
<tr>
<td>MRI</td>
<td>Cook&#x27;s Distance</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition Cook's distance values computed for fMRI.</td>
<td>3</td>
</tr>
<tr>
<td>MRI</td>
<td>fmap QC</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Additional QC fields added to the scans TSV files related to line artifacts in fmaps (<code>line2_*</code>)</td>
<td>3</td>
</tr>
<tr>
<td>MRI</td>
<td>QSIRecon</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Tabulated data for QSIRecon (participant data combined across derivative files into single tidy table) will be provided in a future release.</td>
<td>3</td>
</tr>
<tr>
<td>MRI</td>
<td>Postprocessing</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of individual functional network maps (generated with template matching) and <a href="https://modelarrayio.readthedocs.io/en/latest/">ModelArray</a> outputs for XCP-D for efficient voxel-wise statistical modeling.</td>
<td>3</td>
</tr>
<tr>
<td>MRI</td>
<td>Scanner info</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Scanner metadata, currently available within the raw BIDS Scans TSV files, will be additionally provided within the tabulated data for ease of access (see <a href="#infobbox">Participant Derived</a> domain info on this page).</td>
<td>3</td>
</tr>
<tr>
<td>MRI</td>
<td></td>
<td> All 0s for numeric values in tabulated XCP-D derivatives</td>
<td>3</td>
</tr>
<tr>
<td>MRI</td>
<td>Run ID</td>
<td><i class="fas fa-bug icon-bug"></i> The <code>run-{X}</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
<td></td>
</tr>
<tr>
<td>MRI</td>
<td>dMRI metadata</td>
<td><i class="fas fa-bug icon-bug"></i> <code>LargeDelta</code> and <code>SmallDelta</code> in the sidecars currently are set to vendor-specific values (which aren't always correct because the models have their own values) and will be updated to reflect accurate values.</td>
<td></td>
</tr>
<tr>
<td>MRI</td>
<td>Raw QC Metrics</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Raw MR data QC metrics provided in the raw BIDS SCANS TSV files will be combined into a single table across participants/sessions.</td>
<td></td>
</tr>
<tr>
<td>MRI</td>
<td>Source DICOMs</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Add source DICOMs for all imaging modalities.</td>
<td>3</td>
</tr>
<tr>
<td>NCL</td>
<td>Bayley</td>
<td><i class="fas fa-bug icon-bug"></i> Remove invalid scores of <code>-9999</code>; until resolved, users should remove this participant data prior to analysis.</td>
<td>3</td>
</tr>
<tr>
<td>NCL</td>
<td>CDI</td>
<td><i class="fas fa-bug icon-bug"></i> Percentiles incorrectly converted for N=36 cases, resulting in values &gt;100 ('Adjusted Percentile' incorrectly parsed from 'Total Produced' instead of 'Total Produced Percentile-sex (adjusted)')</td>
<td>3</td>
</tr>
<tr>
<td>NCL</td>
<td>Vineland</td>
<td><i class="fas fa-bug icon-bug"></i> The Coping Skills, Domestic, and Written subscales are not administered at V05 because children are too young. However, for some participants, the missing reason is incorrectly coded as "Logic skipped" or "Unknown" in the shadow matrix. In addition, the age of one child is outside of the valid bounds for V05.</td>
<td>3</td>
</tr>
<tr>
<td>NCL</td>
<td>MLDS</td>
<td><i class="fas fa-bug icon-bug"></i> Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) includes implausible values due to data entry errors. Exclude values &gt;168 hours from analysis.</td>
<td></td>
</tr>
<tr>
<td>NCL</td>
<td>CDI-2</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of the MacArthur-Bates CDI-2 Language</td>
<td>3</td>
</tr>
<tr>
<td>NCL</td>
<td>Deferred Imitation</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of instrument: Deferred Imitation Task: Gong and Berry-Go-Round</td>
<td>3</td>
</tr>
<tr>
<td>NT</td>
<td>GABI</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of raw BIDS data for GABI (infant heart rate).</td>
<td>3</td>
</tr>
<tr>
<td>PEX</td>
<td>PEX Health</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ICD codes for the <code>pex_bm_health*</code> tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></td>
<td>3</td>
</tr>
<tr>
<td>PEX</td>
<td>EPDS</td>
<td><i class="fas fa-bug icon-bug"></i> Inconsistent scoring: (1) item responses present, but score is null (N=1); (2) all items null, but score is <code>0</code> (N≥3).</td>
<td>3</td>
</tr>
<tr>
<td>PEX</td>
<td>Healthv2 Preg</td>
<td><i class="fas fa-bug icon-bug"></i> The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping.</td>
<td></td>
</tr>
<tr>
<td>PEX</td>
<td>Healthv2 Preg</td>
<td><i class="fas fa-bug icon-bug"></i> Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank.</td>
<td></td>
</tr>
<tr>
<td>PH</td>
<td>Anthropometrics</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Add sex-specific birth weight to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Sex-Specific Birthweight for GA</a>).</td>
<td>3</td>
</tr>
<tr>
<td>PH</td>
<td>Anthropometrics</td>
<td><i class="fas fa-bug icon-bug"></i> Adjusted age contains N=303 "unknown missing" values that are also missing 'Date of Administration'.</td>
<td>3</td>
</tr>
<tr>
<td>PH</td>
<td>Anthropometrics</td>
<td><i class="fas fa-bug icon-bug"></i> The data dictionary element <code>type_data</code> for <code>average_bmi</code> will be corrected to <code>double</code> (currently=<code>character</code>).</td>
<td>3</td>
</tr>
<tr>
<td>PH</td>
<td>Anthropometrics</td>
<td><i class="fas fa-bug icon-bug"></i> Growth (<code>ph_ch_anthro</code>) filter ranges will be updated to be visit-specific, as current ranges allow biologically implausible values (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Range Checks</a>).</td>
<td>3</td>
</tr>
<tr>
<td>PH</td>
<td>Vision Screener</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Add more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>
<td></td>
</tr>
<tr>
<td>PH</td>
<td>BISQ-SF</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Add Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
<td></td>
</tr>
<tr>
<td>PH</td>
<td>Med History V1</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of V06</td>
<td>3</td>
</tr>
<tr>
<td>PH</td>
<td>Child Nutrition</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of the Child Nutrition Questionnaire.</td>
<td>3</td>
</tr>
<tr>
<td>PH</td>
<td>PEDsQL</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of the PEDsQL</td>
<td>3</td>
</tr>
<tr>
<td>SED</td>
<td>eHITS</td>
<td><i class="fas fa-bug icon-bug"></i> Participants missing all item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td>3</td>
</tr>
<tr>
<td>SED</td>
<td>Demo</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Add household roster fields capturing the sex of listed individuals (adult &amp; child tables).</td>
<td>3</td>
</tr>
<tr>
<td>SED</td>
<td>Demo</td>
<td><i class="fas fa-bug icon-bug"></i> Relationship status was inappropriately collected at V02/V03 for all cohorts and should have been restricted to cases where there was a change in caregiver (i.e. only Alternative Caregiver cohorts should have this field populated). Data for non-ACG cohorts to be excluded.</td>
<td>3</td>
</tr>
<tr>
<td>SED</td>
<td>Demo</td>
<td><i class="fas fa-bug icon-bug"></i> Roster was inappropriately collected at V02/V03 for all cohorts and should have been restricted to V02 PNRs and alternate caregiver cohorts; to be excluded.</td>
<td>3</td>
</tr>
<tr>
<td>SED</td>
<td>GLED</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of Geocoded Linkage from Home and Work Addresses</td>
<td>3</td>
</tr>
<tr>
<td>SED</td>
<td>TIC Questionnaire</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of TIC Questionnaire table</td>
<td>3</td>
</tr>
<tr>
<td>SED</td>
<td>Demo</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of V6 Adult and V6 Child Demographics</td>
<td>3</td>
</tr>
<tr>
<td>SED</td>
<td>Incarceration</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Addition of the Incarceration Questionnaire</td>
<td>3</td>
</tr>
</tbody>
</table>


<script>
document.addEventListener("DOMContentLoaded", function () {
  const table = document.getElementById("archive-table");
  const tbody = table.querySelector("tbody");
  const rows = Array.from(tbody.querySelectorAll("tr"));

  const searchInput = document.getElementById("archive-search");
  const domainSelect = document.getElementById("archive-domain");
  const brSelect = document.getElementById("archive-br");
  const typeSelect = document.getElementById("archive-type");
  const resetButton = document.getElementById("archive-reset");
  const status = document.getElementById("archive-status");

  // Build filter options from the existing table.
  const domains = [...new Set(rows.map(row => row.cells[0]?.textContent.trim()).filter(Boolean))]
    .sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));

  const releases = [...new Set(rows.map(row => row.cells[3]?.textContent.trim()).filter(Boolean))]
    .sort((a, b) => b.localeCompare(a, undefined, { numeric: true }));

  domains.forEach(value => {
    domainSelect.add(new Option(value, value));
  });

  releases.forEach(value => {
    brSelect.add(new Option(value, value));
  });

  let sortColumn = null;
  let sortDirection = "asc";

  function normalize(value) {
    return value.toLowerCase().replace(/\s+/g, " ").trim();
  }

  function applyFilters() {
    const search = normalize(searchInput.value);
    const domain = domainSelect.value;
    const br = brSelect.value;
    const type = typeSelect.value;

    let visible = 0;

    rows.forEach(row => {
      const domainValue = row.cells[0]?.textContent.trim() || "";
      const topicValue = row.cells[1]?.textContent.trim() || "";
      const summaryValue = row.cells[2]?.textContent.trim() || "";
      const brValue = row.cells[3]?.textContent.trim() || "";

      const matchesSearch =
        !search ||
        normalize(topicValue).includes(search) ||
        normalize(summaryValue).includes(search);

      const matchesDomain = !domain || domainValue === domain;
      const matchesBr = !br || brValue === br;
      const matchesType = !type || row.dataset.type === type;

      const show = matchesSearch && matchesDomain && matchesBr && matchesType;

      row.style.display = show ? "" : "none";
      if (show) visible++;
    });

    status.textContent =
      `Showing ${visible} of ${rows.length} record${rows.length === 1 ? "" : "s"}.`;
  }

  function sortRows(column) {
    if (sortColumn === column) {
      sortDirection = sortDirection === "asc" ? "desc" : "asc";
    } else {
      sortColumn = column;
      sortDirection = "asc";
    }

    const index = {
      domain: 0,
      topic: 1,
      summary: 2,
      br: 3
    }[column];

    rows.sort((a, b) => {
      const aValue = a.cells[index]?.textContent.trim() || "";
      const bValue = b.cells[index]?.textContent.trim() || "";

      // Numeric-aware sorting works well for releases such as 21.0, 21.1, 30.0.
      const aNum = parseFloat(aValue);
      const bNum = parseFloat(bValue);

      let comparison;
      if (column === "br" && !Number.isNaN(aNum) && !Number.isNaN(bNum)) {
        comparison = aNum - bNum;
      } else {
        comparison = aValue.localeCompare(bValue, undefined, {
          numeric: true,
          sensitivity: "base"
        });
      }

      return sortDirection === "asc" ? comparison : -comparison;
    });

    rows.forEach(row => tbody.appendChild(row));

    document.querySelectorAll(".archive-sort").forEach(header => {
      header.classList.remove("sorted-asc", "sorted-desc");
    });

    const activeHeader = document.querySelector(
      `.archive-sort[data-sort="${column}"]`
    );

    if (activeHeader) {
      activeHeader.classList.add(
        sortDirection === "asc" ? "sorted-asc" : "sorted-desc"
      );
    }

    applyFilters();
  }

  [searchInput, domainSelect, brSelect, typeSelect].forEach(control => {
    control.addEventListener("input", applyFilters);
    control.addEventListener("change", applyFilters);
  });

  resetButton.addEventListener("click", function () {
    searchInput.value = "";
    domainSelect.value = "";
    brSelect.value = "";
    typeSelect.value = "";
    applyFilters();
  });

  document.querySelectorAll(".archive-sort").forEach(header => {
    header.addEventListener("click", function () {
      sortRows(header.dataset.sort);
    });
    header.setAttribute("role", "button");
    header.setAttribute("tabindex", "0");
    header.addEventListener("keydown", function (event) {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        sortRows(header.dataset.sort);
      }
    });
  });

  // Newest release first by default.
  sortRows("br");
  if (sortDirection === "asc") {
    sortRows("br");
  }
});
</script>