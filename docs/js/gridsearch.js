// ==== LISTS ====
const failedAssays = ["BCL2L11", "BID", "CD40LG", "CLEC7A", "HGF", "IDS", "LTA", "MGLL", "PTPRM", "RAB6A"];

// ==== TAG ASSAYS ====
const assays = document.querySelectorAll("#assayGrid span");

assays.forEach(assay => {
  const name = assay.textContent.trim();

  if (failedAssays.includes(name)) {
    assay.classList.add("failed");
    assay.innerHTML += ' <span style="color:#b00020;">✖</span>';
  }
});

// ==== FILTERING ====
const searchInput = document.getElementById("assaySearch");
const qcFilter = document.getElementById("qcFailFilter");

function filterAssays() {
  const searchTerm = searchInput.value.toLowerCase();
  const showFailedOnly = qcFilter.checked;

  assays.forEach(assay => {
    const text = assay.textContent.toLowerCase();
    const isFailed = assay.classList.contains("failed");

    const matchesSearch = text.includes(searchTerm);
    const matchesQC = !showFailedOnly || isFailed;

    assay.style.display = (matchesSearch && matchesQC)
      ? "inline-block"
      : "none";
  });
}

// events
searchInput.addEventListener("keyup", filterAssays);
qcFilter.addEventListener("change", filterAssays);