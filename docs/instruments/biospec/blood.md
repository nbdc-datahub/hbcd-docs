# USDTL Blood Toxicology Results

**Full Name**: USDTL Blood Toxicology results        
**Short/Alternative Names**: Blood            
**Table Names**: `bio_bm_biosample_blood`         
**Construct**: Toxicology screen for substances & environmental exposures (metals, nutrition, toxins, proteins) conducted on blood samples

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
<br>
<p><b>Continuous Variables</b><br>
For all toxicology screens, continuous variables should be interpreted with caution based on the threshold limits of quantification (LOQs), or the cutoff concentration used to categorize metabolites as positive or negative. LOQs are provided in <a href="#table1">Table 1. Blood Assay Thresholds PEth</a>.</p> 
</div>
</p>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
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

Processing of Blood Spot Cards consists of preparing 3x 1/8” punches of dried blood spot followed by extraction using an organic solvent. Detection of PETH in the extract is accomplished with a single pass using LCMSMS:
<img src="../images/Fig1_blood.png" width="70%" height="auto" class="center">

Based on the predefined threshold outlined in [Table 1](#table1), the PEth test (`c_peth_b_cat`) is determined to be positive, negative, or canceled. Substance analytes are grouped into classes by analyte screening tests and confirmatory tests. PEth is confirmatory-testing only: 

 - **Confirmatory test**: 20phsphtdetbsp (`c_peth_b_cat`) 
 - **Class**: Ethanol (`c_ethanol_b`)

<div id="table1" class="table-banner">
  <span class="emoji"><i class="fa fa-table"></i></span>
  <span class="text-with-link">
  <span class="text">Table 1. Blood Assay Thresholds PEth</span>
  <a class="anchor-link" href="#table1" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
</div>
<div class="table-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
    <tr>
    <th style="width: 30%;">Analyte</th>
    <th style="width: 20%;"><span class="tooltip tooltip-bottom">LOD
                <span class="tooltiptext">Limit of detection</span>
            </span> (ng/mL)</th>
    <th style="width: 10%;"><span class="tooltip tooltip-bottom">LOQ
                <span class="tooltiptext">Limit of quantification</span>
            </span> (ng/mL)</th>
    <th style="width: 10%;">Cutoff (ng/mL)</th>
    <th style="width: 40%;">Detection Window</th>
    </tr>
</thead>
<tbody>
<tr>
    <td>Phosphatidylethanol</td>
    <td>4</td>
    <td>4</td>
    <td>20</td>
    <td>2-4 weeks</td>
</tr>
</tbody>
</table>
</div>


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
<div class="table-collapsible-content">
<p><b>Final PEth assay results follow these rules</b>:</p>
<ul>
<li>If the PEth test is positive (<code>c_peth_b_cat</code>), the sample level (<code>c_any_specimen_b</code>) is positive (value = 1). </li>
<li>If the PEth confirmatory tests is negative (value = 0), then sample-level (<code>c_any_specimen_b</code>) is negative (0). </li>
<li>If the PEth confirmatory tests is cancelled (value = 3) then sample-level (<code>c_any_specimen_b</code>) is cancelled (value = 3).</li>
</ul>
<p><b>Table 2. Screening Result Scoring</b></p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
    <thead>
      <tr>
        <th style="width: 10%; text-align: center;">Level</th>
        <th style="width: 50%; text-align: center;">Result Type</th>
        <th style="width: 10%; text-align: center;">Example</th>
        <th style="width: 20%; text-align: center;">Options</th>
       </tr>
    </thead>
    <tbody>
<tr>
<td>Specimen</td>
<td style="word-wrap: break-word; white-space: normal;">Confirmatory results (presence of any analyte)</td>
<td><code>c_any_specimen_b</code></td>
<td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=cancelled</td>
</tr>
<tr>
<td>Class</td>
<td style="word-wrap: break-word; white-space: normal;">Confirmatory results (presence of any analyte in class - only one class)</td>
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
</div>
<br>