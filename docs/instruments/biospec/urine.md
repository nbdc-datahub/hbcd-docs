# USDTL Urine Toxicology (Maternal)

{{ readme_summary(instruments.urine) }}
{{ alert_warning(instruments.urine) }}
{{ data_warning(instruments.urine) }}
{{ issues_banner() }}

---

## Instrument Details

{{ instrument_description(instruments.urine) }}

<table class="compact-table">
<thead><tr><th rowspan="2">Creatinine (mg/dL)</th><th colspan="5" style="text-align: center;">Specific Gravity</th></tr>
<tr><th>1.000</th><th>1.001</th><th>1.002</th><th>1.003–1.019</th><th>≥1.020</th></tr></thead>
<tbody>
<tr><td>0–1.9</td><td>Substituted</td><td>Substituted</td><td>Invalid</td><td>Invalid</td><td>Substituted</td></tr>
<tr><td>2.0–19.9</td><td>Invalid</td><td>Invalid</td><td>Dilute</td><td>Normal</td><td>Normal</td></tr>
<tr><td>&gt;20</td><td colspan="5" class="muted-cell">Normal — Specific Gravity not required</td></tr>
</tbody>
</table>

<div id="urine-table1" class="banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-table"></i></span><span class="text-with-link">
<span class="text">Urine Assay Thresholds for Analytes</span><a class="anchor-link" href="#urine-table1" title="Copy link">
<i class="fa-solid fa-link"></i></a></span><span class="arrow">▸</span>
</div>
<div class="collapsible-content">
{{ csv_table("bio/urine-assay-thresholds.csv") }}
</div>

<div id="scoring" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fa fa-calculator"></i>
</span>
<span class="text-with-link">
    <span class="text">Scoring Procedures</span>
    <a class="anchor-link" href="#scoring" title="Copy link">
        <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content">
{{ scoring_contents(instruments.urine) }}
<table class="table-no-vertical-lines">
    <thead>
      <tr>
        <th>Level</th>
        <th>Result Type</th>
        <th>Example</th>
        <th>Options</th>
        </tr>
    </thead>
    <tbody>
<tr><td>Specimen</td>
<td>Confirmatory results (presence of any analyte)</td>
<td><code>c_any_specimen_u</code></td>
<td rowspan="3"><code>1</code>=positive
    <br><code>0</code>=negative<br>
    <code>3</code>=invalid
</td>
</tr>
<tr><td>Class</td>
<td>Confirmatory results (presence of any analyte in class)</td><td><code>c_any_stim_u</code></td>
</tr>
<tr>
<td rowspan="3">Analyte</td><td>Screening results</td><td><code>s_amp_u</code></td></tr>
<tr><td>Confirmatory results</td><td><code>c_amp_u</code></td><td>concentration value</td></tr>
<tr><td>Confirmatory results - categorical</td><td><code>c_amp_u_cat</code>⁠<sup>1</sup></td>
<td><code>1</code>=positive<br>
    <code>0</code>=negative<br>
    <code>3</code>=invalid<br>
    <code>4</code>=screen negative
</td>
</tr>
</tbody>
<tfoot>
<tr>
  <td colspan="4" style="border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
    <sup><b>1</b></sup>Note: the categorical confirmatory test variable for nicotine follows the convention <code>c_nicotine_u</code></td></tr>
</tfoot>
</table>
</div>

{{ references(instruments.urine) }}






<!-- 
<div class="collapsible-content">
<p><b>Final results for each substance follow these rules:</b></p>
<ul>
  <li>
    <b>Positive results:</b> If any confirmatory test for a substance analyte (e.g., Amphetamine/<code>c_amp_u</code>) is positive, then the corresponding class-level (<code>c_any_stim_u</code>) and overall sample-level (<code>c_any_specimen_u</code>) results are also positive.
  </li>
  <li>
    <b>Negative results:</b> If all confirmatory tests for analytes in a class are negative (e.g., <code>c_ethglu_u</code>, <code>c_ethsyl_u</code>), then the class-level result (e.g., <code>c_etgeia_u</code>) is negative. If all classes are negative, the overall sample-level (<code>c_any_specimen_u</code>) result is negative.
  </li>
  <li>
    <b>Invalid results:</b> If any confirmatory test for a substance analyte is invalid, then the corresponding class-level and overall sample-level results are also invalid.
  </li>
</ul>
<table class="table-no-vertical-lines">
    <thead>
      <tr>
        <th>Level</th>
        <th>Result Type</th>
        <th>Example</th>
        <th>Options</th>
       </tr>
    </thead>
    <tbody>
<tr><td>Specimen</td>
<td>Confirmatory results (presence of any analyte)</td>
<td><code>c_any_specimen_u</code></td>
<td rowspan="3"><code>1</code>=positive
    <br><code>0</code>=negative<br>
    <code>3</code>=invalid
</td>
</tr>
<tr><td>Class</td>
<td>Confirmatory results (presence of any analyte in class)</td><td><code>c_any_stim_u</code></td>
</tr>
<tr>
<td rowspan="3">Analyte</td><td>Screening results</td><td><code>s_amp_u</code></td></tr>
<tr><td>Confirmatory results</td><td><code>c_amp_u</code></td><td>concentration value</td></tr>
<tr><td>Confirmatory results - categorical</td><td><code>c_amp_u_cat</code>⁠<sup>1</sup></td>
<td><code>1</code>=positive<br>
    <code>0</code>=negative<br>
    <code>3</code>=invalid<br>
    <code>4</code>=screen negative
</td>
</tr>
</tbody>
<tfoot>
<tr>
  <td colspan="4" style="border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
    <sup><b>1</b></sup>Note: the categorical confirmatory test variable for nicotine follows the convention <code>c_nicotine_u</code></td></tr>
</tfoot>
</table>
</div> -->
