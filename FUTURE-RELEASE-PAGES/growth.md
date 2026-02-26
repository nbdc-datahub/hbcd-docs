<div id="scoring" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-calculator"></i></span>
  <span class="text-with-link">
  <span class="text">Scoring Procedures</span>
  <a class="anchor-link" href="#scoring" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Age-based z-scores for growth measurements were calculated using the <a href="https://github.com/CDC-DNPAO/WHOanthro">WHOanthro</a> R package. Chronological age at administration (<code>candidate_age</code>), available for tabulated data (<a href="../../agevariables/#tabulated-data" see details</a>), is jittered by 0-7 days. To ensure precision and prevent potential errors, the z-scores were calculated using age computed from a <i>non-jittered</i> date of birth. No adjustments were made for premature birth.</p>
</div>