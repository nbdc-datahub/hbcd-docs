<style>
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

---

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

<!-- BEGIN KNOWN_ISSUES_TABLE -->
<table class="compact-table-no-vertical-lines archive-table" data-domain="All Data / General">
<caption class="archive-table-title">All Data / General</caption>
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-domain="All Data / General" data-type="issue">
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Instruction</td>
<td>The 'instruction' data dictionary element is currently blank.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr data-domain="All Data / General" data-type="update">
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Sequence Field</td>
<td>The currently included Sequence field is blank across all instruments and will be removed.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


<table class="compact-table-no-vertical-lines archive-table" data-domain="Behavior &amp; Child-Caregiver Interaction">
<caption class="archive-table-title">Behavior &amp; Child-Caregiver Interaction</caption>
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-domain="Behavior &amp; Child-Caregiver Interaction" data-type="update">
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ECHO</td>
<td>Addition of the Early Child Care and Education</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


<table class="compact-table-no-vertical-lines archive-table" data-domain="EEG">
<caption class="archive-table-title">EEG</caption>
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-domain="EEG" data-type="issue">
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Age fields</td>
<td>Chronological and adjusted age fall outside of 3-9 months in N=74 V03 sessions (site entry errors); exclude age values prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>3.1</span></td>
</tr>
</tbody></table>


<table class="compact-table-no-vertical-lines archive-table" data-domain="MRI">
<caption class="archive-table-title">MRI</caption>
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-domain="MRI" data-type="issue">
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Run ID</td>
<td>The <code>run-{X}</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr data-domain="MRI" data-type="issue">
<td><i class="fas fa-bug icon-bug"></i></td>
<td>dMRI metadata</td>
<td><code>LargeDelta</code> and <code>SmallDelta</code> in the sidecars currently are set to vendor-specific values (which aren't always correct because the models have their own values) and will be updated to reflect accurate values.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr data-domain="MRI" data-type="update">
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Raw QC Metrics</td>
<td>Raw MR data QC metrics provided in the raw BIDS SCANS TSV files will be combined into a single table across participants/sessions.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


<table class="compact-table-no-vertical-lines archive-table" data-domain="Neurocognition &amp; Language">
<caption class="archive-table-title">Neurocognition &amp; Language</caption>
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-domain="Neurocognition &amp; Language" data-type="issue">
<td><i class="fas fa-bug icon-bug"></i></td>
<td>MLDS</td>
<td>Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) includes implausible values due to data entry errors. Exclude values &gt;168 hours from analysis.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


<table class="compact-table-no-vertical-lines archive-table" data-domain="Physical Health">
<caption class="archive-table-title">Physical Health</caption>
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-domain="Physical Health" data-type="update">
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>BISQ-SF</td>
<td>Add Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr data-domain="Physical Health" data-type="update">
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Vision Screener</td>
<td>Add more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


<table class="compact-table-no-vertical-lines archive-table" data-domain="Pregnancy &amp; Environmental Exposure">
<caption class="archive-table-title">Pregnancy &amp; Environmental Exposure</caption>
<thead>
<tr>
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-domain="Pregnancy &amp; Environmental Exposure" data-type="issue">
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Healthv2 Preg</td>
<td>The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr data-domain="Pregnancy &amp; Environmental Exposure" data-type="issue">
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Healthv2 Preg</td>
<td>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table><!-- END KNOWN_ISSUES_TABLE -->





<script>
document.addEventListener("DOMContentLoaded", function () {
  // Each domain gets its own <table class="archive-table" data-domain="...">
  // with a <caption> as its title. Rows carry their own data-domain/data-type
  // so filtering doesn't depend on column position.
  const tables = Array.from(document.querySelectorAll(".archive-table"));
  const rows = tables.flatMap(t => Array.from(t.querySelectorAll("tbody tr")));

  const searchInput = document.getElementById("archive-search");
  const domainSelect = document.getElementById("archive-domain");
  const brSelect = document.getElementById("archive-br");
  const typeSelect = document.getElementById("archive-type");
  const resetButton = document.getElementById("archive-reset");
  const status = document.getElementById("archive-status");
  const emptyMessage = document.getElementById("archive-empty");

  // Build filter options from the existing tables.
  const domains = [...new Set(rows.map(row => row.dataset.domain).filter(Boolean))]
    .sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));

  const releases = [...new Set(rows.map(row => row.cells[3]?.textContent.trim()).filter(Boolean))]
    .sort((a, b) => b.localeCompare(a, undefined, { numeric: true }));

  domains.forEach(value => {
    domainSelect.add(new Option(value, value));
  });

  releases.forEach(value => {
    brSelect.add(new Option(value, value));
  });

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
      const topicValue = row.cells[1]?.textContent.trim() || "";
      const summaryValue = row.cells[2]?.textContent.trim() || "";
      const brValue = row.cells[3]?.textContent.trim() || "";

      const matchesSearch =
        !search ||
        normalize(topicValue).includes(search) ||
        normalize(summaryValue).includes(search);

      const matchesDomain = !domain || row.dataset.domain === domain;
      const matchesBr = !br || brValue === br;
      const matchesType = !type || row.dataset.type === type;

      const show = matchesSearch && matchesDomain && matchesBr && matchesType;

      row.style.display = show ? "" : "none";
      if (show) visible++;
    });

    // Hide a domain's whole table (title included, via its <caption>) when
    // none of its rows match.
    tables.forEach(table => {
      const tableVisible = Array.from(table.querySelectorAll("tbody tr"))
        .some(row => row.style.display !== "none");
      table.style.display = tableVisible ? "" : "none";
    });

    status.textContent =
      `Showing ${visible} of ${rows.length} record${rows.length === 1 ? "" : "s"}.`;
    emptyMessage.style.display = visible === 0 ? "block" : "none";
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

  applyFilters();
});
</script>