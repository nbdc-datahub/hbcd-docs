# Growth

<div class="info-block">
  <div class="info-row">
    <div class="info-label"><i class="fa fa-table"></i> Table Name:</div>
    <div class="info-value"><code>ph_ch_anthro</code></div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-maximize"></i> Full Name:</div>
    <div class="info-value">Height/Weight/Head Circumference</div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-tape"></i> Construct:</div>
    <div class="info-value">Growth</div>
  </div>
</div>

---------------------------------------------

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</i></span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p><b>Z-Scores Excluded From Current Release</b><br>
Because dates of birth are jittered and calculated chronologic and adjusted ages are ±7 days, we do not provide z-scores in the current data release. Further, <b>we do NOT recommend calculating z-scores using V02 data</b>. Caution is recommended when calculating Z-scores using data from subsequent visits. Future data releases will have z-scores calculated with age in days for investigators wanting to compare to normative growth metrics.</p>
<p><b>Range Checks For Growth</b><br>
Range checks were performed to identify and exclude extreme out-of-range values. Values outside of the following valid ranges were converted to 'n/a'. <i>Note that these ranges are not age-specific, i.e. the same ranges were used for all visits.</i></p>
<table class="table-no-vertical-lines" style="font-size: 15px;">
<tbody>
<tr>
<td><b>Name</b></td>
<td><code>ph_ch_anthro_len_001__03</code></td>
<td><code>ph_ch_anthro_head_001__03</code></td>
<td><code>ph_ch_anthro_wei_001__03</code></td>
</tr>
<tr>
<td><b>Description</b></td>
<td>Average length (in cm)</td>
<td>Head circumference (cm)</td>
<td>Average weight (in kg)</td>
</tr>
<tr>
<td><b>Valid Range</b></td>
<td>30 to 130 cm</td>
<td>25 to 55 cm</td>
<td>0.5 to 30 kg</td>
</tr>
</tbody>
</table>
<p><b>Sex-Specific Birthweight for Gestational Age</b><br>
Sex-specific birthweight for gestational age centiles and z-scores will be calculated in future data releases using Intergrowth curves (<a href="https://doi.org/10.1016/S0140-6736(14)60932-6">Villar et al. 2014</a>). In the meantime, data users can use these growth curves or ones of their choice to calculate centiles and small/large for gestational age variables. 
</div>

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">This data has known issues - <a href="../../../changelog/knownissues/" target="_blank">see details</a>.</span>
</div>
<p></p>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>Yes</td></tr>
<tr><td><b>Respondent</b></td>
<td>NA</td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">HBCD Study Staff, in person.</td></tr>
<tr><td><b>Visits</b></td>
<td>V02, V03, V04, V06, V08</td></tr>
<tr><td><b>Completion Time</b></td>
<td>5 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;">Monitor data dashboard for variable missingness, possible coding errors, scoring verification when needed, and data consistency.</td></tr>
</tbody>
</table>

## Instrument Details

Growth is a standard direct measure of child growth, including height or length (in cm), weight (in kg), and head circumference (cm). In older children, it will also include abdominal circumference (cm). 

## References

<div class="references">
    <p>Villar, J., Cheikh Ismail, L., Victora, C. G., Ohuma, E. O., Bertino, E., Altman, D. G., Lambert, A., Papageorghiou, A. T., Carvalho, M., Jaffer, Y. A., Gravett, M. G., Purwar, M., Frederick, I. O., Noble, A. J., Pang, R., Barros, F. C., Chumlea, C., Bhutta, Z. A., Kennedy, S. H., & International Fetal and Newborn Growth Consortium for the 21st Century (INTERGROWTH-21st). (2014). <i>International standards for newborn weight, length, and head circumference by gestational age and sex: the Newborn Cross-Sectional Study of the INTERGROWTH-21st Project</i>. Lancet, 384(9946), 857–868. <a href="https://doi.org/10.1016/S0140-6736(14)60932-6">https://doi.org/10.1016/S0140-6736(14)60932-6</a></p>
</div>