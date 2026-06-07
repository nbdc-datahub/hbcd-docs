<style>
.wy-nav-content {
    width: 95% !important;
    max-width: 95% !important;
    flex-grow: 1 !important;
}
</style>

# NBDC Data Dictionary

Tabulated HBCD study data is organized into a standardized table format per study instrument/measure, with each table containing a set of variables (see [Data Structure Overview](../datacuration/overview.md) for details). Metadata is organized via a data dictionary following NBDC standards (similar to the [ABCD Study](https://docs.abcdstudy.org/latest/documentation/curation/metadata.html)), which provides detailed information about table variables, including variable name, label, description, data type, etc. All data dictionary elements are outlined below. 

<div id="lasso" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
    <span class="text">NBDC Platform Caveats & Notes</span>
    <a class="anchor-link" href="#lasso" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<div class="info-section">
<div class="info-section-title">
  Blank Columns in Query Tool
</div>
<p>
  Dictionary Query Tool searches within the NBDC Data Access Platform currently display columns that are not applicable to HBCD study data, including columns ending with <code>nda</code>, <code>deap</code>, and <code>redcap</code>. Inapplicable columns will be removed in the future and can safely be ignored. Note that columns may also be blank if they have yet to be populated (currently common for columns ending with <code>*_es</code>). Note that only applicable columns are included in the data dictionary table above.
</p>
</div>
<div class="info-section">
<div class="info-section-title">
  Site & Cohort Information
</div>
<p>
  Datasets downloaded from the NBDC Data Access Platform contain two additional fields not listed in the data dictionary, <code>cohort</code> and <code>site</code>, derived directly from <strong>Visit Level Data</strong> table variables (<code>par_visit_data_{cohort/site}</code>) - see the <a href="../../instruments/demo/visitinfo" target="_blank">Visit Level Data</a> page for details.
</p>
</div>
</div>

## Data Dictionary Elements

<div class="table-legend">
  <span class="legend-item">
    <i class="fa-solid fa-lock legend-icon"></i>
    Values do not vary across releases
  </span>

  <span class="legend-item">
    <i class="fa fa-language legend-icon"></i>
    Column available in Spanish (e.g., <code>label_es</code>)
  </span>
</div>




## Variable Types

<table class="table-no-vertical-lines dd">
<thead>
<tr>
<th>Variable Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>administrative</td><td>Data that gives context to the assessments, e.g. date, language, quality control, etc.</td>
</tr>
<tr>
  <td>derived item</td>
  <td>
      Derived from original participant data, either directly (e.g., <code>sex</code> from administrative records) or by combining variables (e.g., race and ethnicity); see <a href="../../instruments/demo/basicdemo/" target="_blank">Basic Demographics</a> for examples.
  </td>
</tr>
<tr>
<td>item</td><td>Original data provided by the participant, e.g. questions in a questionnaire</td>
</tr>
<tr><td>summary score</td><td>Summary and/or score output based on algorithmic conversions of items/raw data</td>
</tr>
</tbody>
</table>



