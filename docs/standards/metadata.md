<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
</style>

# NBDC Data Dictionary

Tabulated HBCD study data is organized into a standardized table format per study instrument/measure, with each table containing a set of variables (see [Data Structure Overview](../datacuration/overview.md) for details). Metadata is organized via a data dictionary, which provides detailed information about table variables, including variable name, label, description, data type, etc. All data dictionary elements are outlined below.

## Data Dictionary Elements

<!-- Lasso User warnings -->
<div id="add-columns" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">NBDC Data Access Platform User Warnings - Blank Columns in Query Tool</span>
  <a class="anchor-link" href="#add-columns" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Dictionary Query Tool searches within the NBDC Data Access Platform currently display columns that are not applicable to HBCD study data, including columns ending with <code>nda</code>, <code>deap</code>, and <code>redcap</code>. Inapplicable columns will be removed in the future and can safely be ignored. Note that columns may also be blank if they have yet to be populated (currently common for columns ending with <code>*_es</code>). <b>For reference, only applicable columns are included in the data dictionary overview on this page.</b></p>
</div>

<p style="font-size: 0.9em; color: #696969ff; font-weight: bold;">
<i class="fa-solid fa-lock table-icon"></i>&nbsp;= Values do not vary across releases&nbsp;&nbsp;
<i class="fa fa-language table-icon"></i>&nbsp;= Column available in Spanish (includes <code>label_es</code>, <code>instruction_es</code>, <code>header_es</code>, <code>note_es</code>)
</p>

<table class="table-no-vertical-lines">
<thead>
<tr style="border-bottom:2px solid #ccc;">
  <th>NAME</th>
  <th>LABEL</th>
  <th>DESCRIPTION & POSSIBLE/EXAMPLE VALUES</th>
</tr>
</thead>
<tbody>
<!-- CORE METADATA -->
<tr class="table-group-row">
  <td colspan="3">Core Metadata</td>
</tr>

<tr>
  <td><code>domain</code></td>
  <td>Domain</td>
  <td>e.g. <i>Demographics</i>- see <a href="../../instruments/#instruments-by-domain">Instruments by Domain</a> for full list</td>
</tr>

<tr>
  <td><code>source</code></td>
  <td>Source</td>
  <td>Source of information <i>(Biological Mother; Caregiver (Responsible Adult); Child; General)</i></td>
</tr>

<tr>
  <td><code>study</code></td>
  <td>Study</td>
  <td>Part of core (<code>Core</code>) or substudy (<code>Substudy</code>)</td>
</tr>

<!-- IMAGING -->
<tr class="table-group-row">
  <td colspan="3">Imaging</td>
</tr>

<tr>
  <td><code>atlas</code></td>
  <td>Atlas</td>
  <td><a href="../../instruments/mri/fmri/#parc" target="_blank">MRI atlas</a> used for parcellated structural measures and functional timeseries (e.g., <i>Gordon</i>)</td>
</tr>
<tr>
  <td><code>metric</code></td>
  <td>Metric</td>
  <td>Specific metric assessed (e.g. MRI <i>Cortical Thickness</i>)</td>
</tr>
<tr>
  <td><code>sub_domain</code></td>
  <td>Subdomain</td>
  <td>Domain subcategory (e.g. <i>Structural MRI</i> within the <i>Imaging</i> domain)</td>
</tr>

<!-- TABLE-LEVEL -->
<tr class="table-group-row">
  <td colspan="3">Table-level Information</td>
</tr>

<tr>
  <td><code>table_label</code></td>
  <td>Table label</td>
  <td>Human-readable label for table name (e.g. <i>Demographics</i>)</td>
</tr>

<tr>
  <td><code>table_name</code><i class="fa-solid fa-lock table-icon"></i></td>
  <td>Table name</td>
  <td>Table name (e.g. <code>sed_bm_demo</code>)</td>
</tr>

<tr>
  <td><code>url_table</code></td>
  <td>Documentation (table)</td>
  <td>Link to documentation page</td>
</tr>
<tr>
  <td><code>url_table_warn_data</code></td>
  <td>Data Warning (table)</td>
  <td>Data Warning (<a href="../../access/resp_data_use/#warnings" target="_blank">see details</a>)</td>
</tr>
<tr>
  <td><code>url_table_warn_use</code></td>
  <td>Resp Use Warning (table)</td>
  <td>Responsible Use Warning (<a href="../../access/resp_data_use/#warnings" target="_blank">see details</a>)</td>
</tr>

<!-- VAR LEVEL -->
<tr class="table-group-row">
  <td colspan="3">Variable-level Information</td>
</tr>

<tr>
  <td><code>description</code></td>
  <td>Variable label</td>
  <td>Human-readable label for variable (e.g. <i>Highest grade completed</i>). <i>Alternative name: <code>label</code><i class="fa fa-language table-icon"></i></i></td>
</tr>

<tr>
  <td><code>header</code><i class="fa fa-language table-icon"></i></td>
  <td>Header</td>
  <td>Header/instructions for a set of questions (e.g. <i>For each item that describes your child...</i>)</td>
</tr>

<tr>
  <td><code>instruction</code><i class="fa fa-language table-icon"></i></td>
  <td>Instruction</td>
  <td>
    Instructions preceding form items (e.g. <i>The next set of questions is about your child's behavior...</i>)</td>
</tr>

<tr>
  <td><code>levels</code><i class="fa fa-language table-icon"></i></td>
  <td>Levels</td>
  <td>
    Embedded tables with Value:Label options for categorical variables
    <span class="tooltip">
      <i class="fa-solid fa-eye"></i>
      <span class="tooltiptext">
        <img src="../levels.png" alt="Levels table example" style="max-height: 200px;">
      </span>
    </span>
  </td>
</tr>

<tr>
  <td><code>name</code><i class="fa-solid fa-lock table-icon"></i></td>
  <td>Variable name</td>
  <td>Variable name within a table (e.g. <code>sed_bm_demo_edu_001</code>)</td>
</tr>

<tr>
  <td><code>note</code><i class="fa fa-language table-icon"></i></td>
  <td>Note</td>
  <td>Note displayed to participants (e.g. <i>Enter weight in pounds.</i>)</td>
</tr>

<tr>
  <td><code>type_data</code><i class="fa-solid fa-lock table-icon"></i></td>
  <td>Data type</td>
  <td>Includes: <i>date; timestamp; time; <span class="tooltip">character<span class="tooltiptext">Only used for categorical columns</span></span>; text; integer; double</i></td>
</tr>
<tr>
  <td><code>type_level</code></td>
  <td>Level of measurement</td>
  <td>Includes: <i>nominal; ordinal; interval; ratio</i></td>
</tr>
<tr>
  <td><code>type_var</code></td>
  <td>Variable type</td>
  <td>Includes: <i>administrative; item; derived item; summary score</i> -  <a href="#variable-types">see details</a></td>
</tr>

<tr>
  <td><code>unit</code></td>
  <td>Unit</td>
  <td>Unit of measurement (e.g. <i>years, cm, lbs, etc.</i>)</td>
</tr>

<tr>
  <td><code>url_warn_data</code></td>
  <td>Data Warning (var)</td>
  <td>Data Warning (<a href="../resp_data_use/#warnings" target="_blank">see details</a>) - variable-specific</td>
</tr>

<tr>
  <td><code>url_warn_use</code></td>
  <td>Resp Use Warning (var)</td>
  <td>Responsible Use Warning (<a href="../resp_data_use/#warnings" target="_blank">see details</a>) - variable-specific</td>
</tr>


<!-- DISPLAY PROPERTIES -->
<tr class="table-group-row">
  <td colspan="3">Display Properties / Identifiers / Order</td>
</tr>

<tr>
  <td><code>branching_logic</code></td>
  <td>Branching logic</td>
  <td>Branching logic applied to variable/question</td>
</tr>

<tr>
  <td><code>identifier_column</code><i class="fa-solid fa-lock table-icon"></i></td>
  <td>Identifier column(s)</td>
  <td>Columns used for participant identification (i.e. participant & session ID)- <a href="../../datacuration/phenotypes/#table-organization" target="_blank">see details</a></td>
</tr>

<tr>
  <td><code>order_display</code></td>
  <td>Display order</td>
  <td>Order in which item is displayed to participants within a given measure</td>
</tr>

<tr>
  <td><code>order_sort</code></td>
  <td>Sort order</td>
  <td>Standard sort order in table/measure (and column order in database)</td>
</tr>

<tr>
  <td><code>type_field</code></td>
  <td>Field type</td>
  <td>Field type presented to participant (e.g. <i>dropdown, radio, checkbox, etc.</i>)</td>
</tr>

</tbody>
</table>

### Variable Types

<table class="table-no-vertical-lines">
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
<tr><td>derived item</td><td>Derived from original participant data (e.g., combining separate entries for feet and inches into a single derived height variable in inches) - see <a href="../../instruments/demo/basicdemo/" target="_blank">Basic Demographics</a> for more examples</td></tr>
<tr>
<td>item</td><td>Original data provided by the participant, e.g. questions in a questionnaire</td>
</tr>
<tr><td>summary score</td><td>Summary and/or score output based on algorithmic conversions of items/raw data</td>
</tr>
</tbody>
</table>

### Site & Cohort Information

Datasets downloaded from the NBDC Data Access Platform contain two additional fields not listed in the data dictionary, `cohort` and `site`. These are derived from the <a href="../../instruments/demo/visitinfo" target="_blank">Visit Level Data</a> table variables `par_visit_data_cohort` and `par_visit_data_site`. 

- **`cohort`**: study cohort, e.g. HBCD Main Child vs. HBCD Multiple Birth (see <a href="../../instruments/demo/visitinfo/#cohort-caregiver-types" target="_blank">Cohort & Caregiver Types</a> for details)  
- **`site`**: site where visit occurred (distinct from site at time of recruitment - see `recruitment_site` in <a href="../../instruments/demo/basicdemo/" target="_blank">Basic Demographics</a>)

