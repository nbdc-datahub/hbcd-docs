// Search/filter toolbar for the Known Issues & Pending Updates page.
// No-ops on any other page since the required elements won't be present.
(function () {
  const sections = Array.from(document.querySelectorAll(".ki-domain-section"));
  const searchInput = document.getElementById("ki-search");
  const domainSelect = document.getElementById("ki-domain-filter");
  const issueToggle = document.getElementById("ki-filter-issue");
  const pendingToggle = document.getElementById("ki-filter-pending");
  const resetBtn = document.getElementById("ki-reset");
  const noResults = document.getElementById("ki-no-results");

  if (!sections.length || !searchInput || !domainSelect || !issueToggle || !pendingToggle) {
    return;
  }

  // Populate the domain dropdown from whatever domains are actually on the page.
  const domains = Array.from(new Set(sections.map((s) => s.dataset.domain))).sort((a, b) =>
    a.localeCompare(b)
  );
  domains.forEach((domain) => {
    const opt = document.createElement("option");
    opt.value = domain;
    opt.textContent = domain;
    domainSelect.appendChild(opt);
  });

  function applyFilters() {
    const term = searchInput.value.trim().toLowerCase();
    const selectedDomain = domainSelect.value;
    const showIssues = issueToggle.checked;
    const showPending = pendingToggle.checked;

    let anyVisible = false;

    sections.forEach((section) => {
      const domainMatches = selectedDomain === "all" || section.dataset.domain === selectedDomain;
      let sectionHasVisibleRow = false;

      const rows = section.querySelectorAll("tbody tr");
      rows.forEach((row) => {
        const typeMatches = row.dataset.type === "issue" ? showIssues : showPending;
        const textMatches = !term || row.textContent.toLowerCase().includes(term);
        const visible = domainMatches && typeMatches && textMatches;
        row.style.display = visible ? "" : "none";
        if (visible) sectionHasVisibleRow = true;
      });

      const sectionVisible = domainMatches && sectionHasVisibleRow;
      section.style.display = sectionVisible ? "" : "none";
      if (sectionVisible) anyVisible = true;
    });

    if (noResults) {
      noResults.style.display = anyVisible ? "none" : "";
    }
  }

  searchInput.addEventListener("input", applyFilters);
  domainSelect.addEventListener("change", applyFilters);
  issueToggle.addEventListener("change", applyFilters);
  pendingToggle.addEventListener("change", applyFilters);

  if (resetBtn) {
    resetBtn.addEventListener("click", () => {
      searchInput.value = "";
      domainSelect.value = "all";
      issueToggle.checked = true;
      pendingToggle.checked = true;
      applyFilters();
    });
  }

  applyFilters();
})();
