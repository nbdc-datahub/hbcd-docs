// Assay search functionality (Olink page)
document.getElementById("assaySearch").addEventListener("input", function() {
  const filter = this.value.toUpperCase();
  document.querySelectorAll(".assay-grid span").forEach(el => {
    el.style.display = el.textContent.includes(filter) ? "" : "none";
  });
});

// ==== LISTS ====
const failedAssays = ["BCL2L11", "BID", "CD40LG", "CLEC7A", "HGF", "IDS", "LTA", "MGLL", "PTPRM", "RAB6A"];

const plateEffectAssays = ["ACTN4", "AMN", "CEACAM21", "DGKZ", "EIF5A", "FCRL3", "FXYD5", "GBP2", "ICA1", "IFNG", "IL10RA", "IL11", "IL12RB1", "IL13", "IL15RA", "IL17A", "IL17F", "IL1B", "IL2", "IL20", "IL20RA", "IL22RA1", "IL24", "IL2RB", "IL33", "IL4", "IL5", "ITGB6", "JCHAIN", "JUN", "LAP3", "LTO1", "NCLN", "NFATC3", "NRTN", "PADI2", "PNPT1", "PRDX3", "PRKAB1", "PRKCQ", "RGS8", "SLAMF1", "TANK", "TNFAIP8", "TNFRSF13C", "TPT1"
];

// ==== TAG ASSAYS ====
const assays = document.querySelectorAll("#assayGrid span");

assays.forEach(assay => {
  const name = assay.textContent.trim();

  if (failedAssays.includes(name)) {
    assay.classList.add("failed");
    assay.innerHTML += ' <span style="color:#b00020;">✖</span>';
  }

  if (plateEffectAssays.includes(name)) {
    assay.classList.add("plate");
    assay.innerHTML += ' <span style="color:#e67e22;">▲</span>';
  }
});

// ==== FILTERING ====
const searchInput = document.getElementById("assaySearch");
const qcFilter = document.getElementById("qcFailFilter");
const plateFilter = document.getElementById("plateFilter");

function filterAssays() {
  const searchTerm = searchInput.value.toLowerCase();
  const showFailedOnly = qcFilter.checked;
  const showPlateOnly = plateFilter.checked;

  assays.forEach(assay => {
    const text = assay.textContent.toLowerCase();
    const isFailed = assay.classList.contains("failed");
    const hasPlate = assay.classList.contains("plate");

    const matchesSearch = text.includes(searchTerm);
    const matchesQC = !showFailedOnly || isFailed;
    const matchesPlate = !showPlateOnly || hasPlate;

    assay.style.display = (matchesSearch && matchesQC && matchesPlate)
      ? "inline-block"
      : "none";
  });
}

searchInput.addEventListener("keyup", filterAssays);
qcFilter.addEventListener("change", filterAssays);
plateFilter.addEventListener("change", filterAssays);