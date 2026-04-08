<p style="color: red; font-size: 1.5em;">3.0 DOCUMENTATION</p>

# PEth Blood Toxicology (Maternal)

<div class="info-block">
  <div class="info-row">
    <div class="info-label"><i class="fa fa-table"></i> Table Name:</div>
    <div class="info-value"><code>bio_bm_biosample_blood</code></div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-tape"></i> Construct:</div>
    <div class="info-value">Drug, Environmental Exposure</div>
  </div>
</div>

<!-- **Construct**: Toxicology screen for substances & environmental exposures (metals, nutrition, toxins, proteins) conducted on blood samples -->

---

<p>
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
<p>For all toxicology screens, continuous variables should be interpreted with caution based on the threshold limits of quantification (LOQs), or the cutoff concentration used to categorize metabolites as positive or negative.</p> 
</div>
</p>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
    <td><b>Child Specific</b></td>
    <td>No</td>
</tr>
<tr><td><b>Respondent</b></td>
<td>Pregnant person</td></tr>
<tr><td><b>Administration</b></td>
<td>Phlebotomist-collected venous blood, which is pipetted onto dried blood spot cards</td></tr>
<tr><td><b>Visits</b></td>
<td>V01</td></tr>
<tr><td><b>Completion Time</b></td>
<td>5 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td>Examine assay ranges and categorical versus continuous measures.</td></tr>
</tbody>
</table>

## Instrument Details

Phosphatidylethanol (PEth) is measured from dried blood spot cards using liquid chromatography–tandem mass spectrometry (LC-MS/MS).
<img src="../images/Fig1_blood.png" width="70%" height="auto" class="center">

PEth is assessed using confirmatory testing only and categorized under a single substance class: Ethanol (`c_ethanol_b`). Results include both a quantitative concentration (`c_peth_b`) and a derived categorical outcome (`c_peth_b_cat`) based on predefined thresholds shown in the table below. Categorical PEth results (`c_peth_b_cat`) are defined as: `0` (Negative), `1` (Positive), or `3` (Canceled). Sample-level results (`c_any_specimen_b`) are derived directly from the PEth confirmatory results.

<p style="margin-bottom: 0; font-size: 0.9em"><b>Blood Assay Thresholds (PEth)</b></p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;"> <thead> <tr> <th>Analyte</th> <th><span class="tooltip tooltip-right">LOD<span class="tooltiptext">Limit of detection</span></span> (ng/mL)</th> <th><span class="tooltip tooltip-right">LOQ<span class="tooltiptext">Limit of quantification</span></span> (ng/mL)</th> <th>Cutoff (ng/mL)</th> <th>Detection Window</th> </tr> </thead> <tbody> <tr> <td>Phosphatidylethanol (PEth)</td> <td>4</td> <td>4</td> <td>20</td> <td>2–4 weeks</td> </tr> </tbody> </table>

<!-- 
<p><b>Final PEth assay results follow these rules</b>:</p>
<ul>
<li>If the PEth test is <b>positive</b> (<code>c_peth_b_cat</code>), the sample level (<code>c_any_specimen_b</code>) is <b>positive</b> (<code>1</code>). </li>
<li>If the PEth confirmatory tests is <b>negative</b> (<code>0</code>), then sample-level (<code>c_any_specimen_b</code>) is <b>negative</b> (<code>0</code>). </li>
<li>If the PEth confirmatory tests is cancelled (<code>3)</code> then sample-level (<code>c_any_specimen_b</code>) is cancelled (<code>3</code>).</li>
</ul> -->

<!-- 
Results are reported at three levels:

Specimen level: Any analyte detected
Class level: Any analyte within a substance class
Analyte level: Individual compound results -->

<p style="margin-bottom: 0; font-size: 0.9em"><b>Screening Result Scoring</b></p>
<table class="compact-table-no-vertical-lines">
    <thead>
      <tr>
        <th>Level</th>
        <th>Result Type</th>
        <th>Example</th>
        <th>Options</th>
       </tr>
    </thead>
    <tbody>
<tr>
<td>Specimen</td>
<td style="word-wrap: break-word; white-space: normal;">Sample-level results</td>
<td><code>c_any_specimen_b</code></td>
<td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=cancelled</td>
</tr>
<tr>
<td>Class</td>
<td style="word-wrap: break-word; white-space: normal;">Confirmatory results (presence of any analyte in class)</td>
<td><code>c_ethanol_b</code></td>
<td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=cancelled</td>
</tr>
<tr>
<td colspan="1" rowspan="3">
<div>Analyte</div>
</td>
</tr>
<tr>
<td>Confirmatory results</td>
<td><code>c_peth_b</code></td>
<td>concentration value</td>
</tr>
<tr>
<td>Confirmatory results - categorical</td>
<td><code>c_peth_b_cat</code></td>
<td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=cancelled</td>
</tr>
</tbody>
</table>



<!-- <p><b>Final PEth assay results follow these rules</b>:</p>
<ul>
<li>If the PEth test is <b>positive</b> (<code>c_peth_b_cat</code>), the sample level (<code>c_any_specimen_b</code>) is <b>positive</b> (<code>1</code>). </li>
<li>If the PEth confirmatory tests is <b>negative</b> (<code>0</code>), then sample-level (<code>c_any_specimen_b</code>) is <b>negative</b> (<code>0</code>). </li>
<li>If the PEth confirmatory tests is cancelled (<code>3)</code> then sample-level (<code>c_any_specimen_b</code>) is cancelled (<code>3</code>).</li>
</ul> -->

<!-- 
is not part of an initial screening panel. -->

<!-- 
PEth results (`c_peth_b_cat`) are *positive*, *negative*, or *canceled* based on the predefined thresholds in the table above. Substance analytes are grouped into classes by analyte screening and confirmatory tests. PEth is confirmatory-testing only:  -->


<!-- 
Negative → <code>c_any_specimen_b = 0</code>      
Positive → <code>c_any_specimen_b = 1</code>      
Canceled → <code>c_any_specimen_b = 3</code> -->
