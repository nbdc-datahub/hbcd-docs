# USDTL Nails Toxicology

{{ readme_summary(instruments.nails) }}
{{ alert_warning(instruments.nails) }}
{{ data_warning(instruments.nails) }}
{{ issues_banner() }}

---

## Instrument Details

{{ instrument_description(instruments.nails) }}
{{ hbcd_mods(instruments.nails) }}

<div id="nails-table1" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-table"></i></span>
  <span class="text-with-link">
  <span class="text">Nail Assay Thresholds</span>
  <a class="anchor-link" href="#nails-table1" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>The detection window for all analytes is 3-6 and 10-14 months for finger and toe nails, respectively, with the exception of Ethyl glucuronide (finger nails: 3; toe nails: no consensus). "Cutoff" is the threshold to classify results as positive or negative for an analyte.</p>
{{ csv_table("nails-table1-assay-thresholds.csv") }}
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
{{ scoring_contents(instruments.nails) }}
<table class="table-no-vertical-lines">
    <thead>
      <tr>
        <th>Level</th>
        <th>Result Type</th>
        <th>Example</th>
        <th>Possible Values</th>
       </tr>
    </thead>
    <tbody>
<tr>
<td>Specimen</td>
<td>Confirmatory results (presence of any analyte)</td>
<td><code>c_any_specimen_n</code></td>
<td rowspan="3"><code>1</code>=positive
    <br><code>0</code>=negative<br>
    <code>3</code>=invalid
</td>
</tr>
<tr>
<td>Class</td>
<td>Confirmatory results (presence of any analyte in class)</td>
<td><code>c_any_stim_n</code></td>
</tr>
<tr>
<td colspan="1" rowspan="3">
<div>Analyte</div>
</td>
<td>Screening results</td>
<td><code>s_amp_n</code></td>
</tr>
<tr>
<td>Confirmatory results</td>
<td><code>c_amp_n</code></td>
<td>concentration value; -999</td>
</tr>
<tr>
<td>Confirmatory results - categorical</td>
<td><code>c_amp_n_cat</code>*</td>
<td><code>1</code>=positive<br>
    <code>0</code>=negative<br>
    <code>3</code>=invalid<br>
    <code>4</code>=screen negative</td>
</tr>
</tbody>
</table>
<p>*<i>Note: Categorical confirmatory test variable for alcohol follows a different convention and is <code>c_ethanol_n</code>.</i></p>
</div>

{{ references(instruments.nails) }}
