# USDTL Blood Toxicology

{{ readme_summary(instruments.blood) }}
{{ alert_warning(instruments.blood) }}
{{ data_warning(instruments.blood) }}
{{ issues_banner() }}

## Instrument Details

{{ instrument_description(instruments.blood) }}

<div class="table-title">Blood Assay Thresholds PEth</div>
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Analyte</th>
<th>LOD (ng/mL)</th>
<th>LOQ (ng/mL)</th>
<th>Cutoff (ng/mL)</th>
<th>Detection Window</th>
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

{{ hbcd_mods(instruments.blood) }}


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
{{ scoring_contents(instruments.blood) }}
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
<tr>
<td>Specimen</td>
<td>Confirmatory results (presence of any analyte)</td>
<td><code>c_any_specimen_b</code></td>
<td><code>1</code>=positive<br>
    <code>0</code>=negative<br>
    <code>3</code>=cancelled<br>
</td>
</tr>
<tr>
<td>Class</td>
<td>Confirmatory results (presence of any analyte in class - only one class)</td>
<td><code>c_ethanol_b</code></td>
<td><code>1</code>=positive<br>
    <code>0</code>=negative<br>
    <code>3</code>=cancelled<br>
</td>
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
<td><code>1</code>=positive<br>
    <code>0</code>=negative<br>
    <code>3</code>=invalid
</td>
</tr>
</tbody>
</table>
</div>

{{ references(instruments.blood) }}


