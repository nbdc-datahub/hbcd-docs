<style>
  /* Known Issues tables */
.compact-table-no-vertical-lines {
  width: 100%;
  table-layout: fixed;
  border-collapse: collapse;
}
/* Consistent column widths across every section */
.compact-table-no-vertical-lines th:nth-child(1),
.compact-table-no-vertical-lines td:nth-child(1) {
  width: 4%;
  text-align: center;
}
.compact-table-no-vertical-lines th:nth-child(2),
.compact-table-no-vertical-lines td:nth-child(2) {
  width: 18%;
}
.compact-table-no-vertical-lines th:nth-child(3),
.compact-table-no-vertical-lines td:nth-child(3) {
  width: 68%;
}
.compact-table-no-vertical-lines th:nth-child(4),
.compact-table-no-vertical-lines td:nth-child(4) {
  width: 10%;
  text-align: center;
}
/* Keep long content from forcing columns wider */
.compact-table-no-vertical-lines th,
.compact-table-no-vertical-lines td {
  box-sizing: border-box;
  vertical-align: top;
}
/* Let long code/field names wrap rather than expanding the table */
.compact-table-no-vertical-lines code {
  overflow-wrap: anywhere;
  word-break: break-word;
}
/* Keep target pills visually centered */
.compact-table-no-vertical-lines td:last-child {
  text-align: center;
  white-space: nowrap;
}

/* KNOWN ISSUES FILTER */
.archive-controls {
  margin: 1.5rem 0 1rem;
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

.archive-empty {
  display: none;
  padding: 2rem 1rem;
  text-align: center;
  color: #777;
  font-size: 0.95rem;
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

The tables below summarize known issues affecting the current data release and pending updates across study instruments. Entries are organized by domain and include the expected release in which each fix or update will be implemented. This page is updated regularly as new issues are reported. 

<p>
<div class="banner">
<span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
<span class="text">Report issues via the <a href="https://nbdc-datashare.lassoinformatics.com/help-center">Help Center in the NBDC Data Access Platform</a> (<a href="https://nbdc.lassoinformatics.com/issue-tracker">see instructions</a>).</span>
</div>
</p>

---
<p style="font-size: 1.2em; color: #555; text-align: center; line-height: 2;">
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i> = Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Pending Update
</p>

<div class="archive-controls" aria-label="Known issues filters">
  <div class="archive-controls-row">
    <input
      id="ki-search"
      class="archive-search"
      type="search"
      placeholder="Search table/topic or summary..."
      aria-label="Search known issues"
    >

    <select id="ki-domain" aria-label="Filter by domain">
      <option value="">All domains</option>
    </select>

    <select id="ki-target" aria-label="Filter by target release">
      <option value="">All targets</option>
    </select>

    <select id="ki-type" aria-label="Filter by type">
      <option value="">All types</option>
      <option value="issue">Known Issues</option>
      <option value="update">Pending Updates</option>
    </select>
    <button id="ki-reset" type="button">Clear filters</button>
  </div>
  <div id="ki-status" class="archive-status" aria-live="polite"></div>
</div>

<div id="ki-empty" class="archive-empty">No matching issues or updates found.</div>


<!-- BEGIN KNOWN_ISSUES_TABLE -->
### All Data / General

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th>
<th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Instruction</td>
<td>The 'instruction' data dictionary element is currently blank.</td>
<td><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Sequence Field</td>
<td>The currently included Sequence field is blank across all instruments and will be removed.</td>
<td><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


### Behavior &amp; Child-Caregiver Interaction

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th>
<th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ECHO</td>
<td>Addition of the Early Child Care and Education</td>
<td><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


### EEG

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th>
<th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Age fields</td>
<td>Chronological and adjusted age fall outside of 3-9 months in N=74 V03 sessions (site entry errors); exclude age values prior to analysis.</td>
<td><span class='pill'>3.1</span></td>
</tr>
</tbody></table>


### MRI

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th>
<th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Run ID</td>
<td>The <code>run-{X}</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
<td><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>dMRI metadata</td>
<td><code>LargeDelta</code> and <code>SmallDelta</code> in the sidecars currently are set to vendor-specific values (which aren't always correct because the models have their own values) and will be updated to reflect accurate values.</td>
<td><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Raw QC Metrics</td>
<td>Raw MR data QC metrics provided in the raw BIDS SCANS TSV files will be combined into a single table across participants/sessions.</td>
<td><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


### Neurocognition &amp; Language

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th>
<th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>MLDS</td>
<td>Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) includes implausible values due to data entry errors. Exclude values &gt;168 hours from analysis.</td>
<td><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


### Physical Health

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th>
<th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>BISQ-SF</td>
<td>Add Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
<td><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Vision Screener</td>
<td>Add more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>
<td><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


### Pregnancy &amp; Environmental Exposure

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th></th><th>Table/Topic</th>
<th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Healthv2 Preg</td>
<td>The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping.</td>
<td><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Healthv2 Preg</td>
<td>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank.</td>
<td><span class='pill'>TBD</span></td>
</tr>
</tbody></table><!-- END KNOWN_ISSUES_TABLE -->




  <br>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const container = document.querySelector(".wy-nav-content") || document.body;

  const searchInput = document.getElementById("ki-search");
  const domainSelect = document.getElementById("ki-domain");
  const targetSelect = document.getElementById("ki-target");
  const typeSelect = document.getElementById("ki-type");
  const resetButton = document.getElementById("ki-reset");
  const status = document.getElementById("ki-status");
  const emptyMessage = document.getElementById("ki-empty");

  if (!searchInput) return;

  // Each domain section is an <h3> heading immediately followed (in document
  // order) by its known-issues table.
  const sections = Array.from(container.querySelectorAll("h3"))
    .map(heading => {
      let table = heading.nextElementSibling;
      while (table && table.tagName !== "TABLE") {
        table = table.nextElementSibling;
      }
      const clone = heading.cloneNode(true);
      clone.querySelectorAll(".headerlink").forEach(link => link.remove());
      return { heading, table, domain: clone.textContent.trim() };
    })
    .filter(section => section.table && section.table.classList.contains("compact-table-no-vertical-lines"));

  sections.forEach(section => {
    domainSelect.add(new Option(section.domain, section.domain));
  });

  const targets = new Set();
  sections.forEach(section => {
    section.table.querySelectorAll("tbody tr").forEach(row => {
      const value = row.cells[3]?.textContent.trim();
      if (value) targets.add(value);
    });
  });

  Array.from(targets)
    .sort((a, b) => {
      const numA = parseFloat(a.replace(/^R/i, ""));
      const numB = parseFloat(b.replace(/^R/i, ""));
      if (!Number.isNaN(numA) && !Number.isNaN(numB) && a.toUpperCase() !== "TBD" && b.toUpperCase() !== "TBD") {
        return numA - numB;
      }
      return a.localeCompare(b, undefined, { numeric: true, sensitivity: "base" });
    })
    .forEach(value => targetSelect.add(new Option(value, value)));

  function normalize(value) {
    return value.toLowerCase().replace(/\s+/g, " ").trim();
  }

  function rowType(row) {
    return row.querySelector(".icon-bug") ? "issue" : "update";
  }

  function applyFilters() {
    const search = normalize(searchInput.value);
    const domain = domainSelect.value;
    const target = targetSelect.value;
    const type = typeSelect.value;

    let totalVisible = 0;
    let sectionsVisible = 0;

    sections.forEach(section => {
      if (domain && section.domain !== domain) {
        section.heading.style.display = "none";
        section.table.style.display = "none";
        return;
      }

      let visibleInSection = 0;

      section.table.querySelectorAll("tbody tr").forEach(row => {
        const topicValue = row.cells[1]?.textContent.trim() || "";
        const summaryValue = row.cells[2]?.textContent.trim() || "";
        const targetValue = row.cells[3]?.textContent.trim() || "";

        const matchesSearch =
          !search ||
          normalize(topicValue).includes(search) ||
          normalize(summaryValue).includes(search) ||
          normalize(section.domain).includes(search);

        const matchesTarget = !target || targetValue === target;
        const matchesType = !type || rowType(row) === type;

        const show = matchesSearch && matchesTarget && matchesType;
        row.style.display = show ? "" : "none";
        if (show) visibleInSection++;
      });

      const showSection = visibleInSection > 0;
      section.heading.style.display = showSection ? "" : "none";
      section.table.style.display = showSection ? "" : "none";

      if (showSection) sectionsVisible++;
      totalVisible += visibleInSection;
    });

    status.textContent =
      `Showing ${totalVisible} item${totalVisible === 1 ? "" : "s"} across ${sectionsVisible} domain${sectionsVisible === 1 ? "" : "s"}.`;
    emptyMessage.style.display = totalVisible === 0 ? "block" : "none";
  }

  [searchInput, domainSelect, targetSelect, typeSelect].forEach(control => {
    control.addEventListener("input", applyFilters);
    control.addEventListener("change", applyFilters);
  });

  resetButton.addEventListener("click", function () {
    searchInput.value = "";
    domainSelect.value = "";
    targetSelect.value = "";
    typeSelect.value = "";
    applyFilters();
  });

  applyFilters();
});
</script>

