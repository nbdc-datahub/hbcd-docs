<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
.naming-pattern {
  text-align: center;
  font-size: 1.4em;
  font-weight: 600;
  margin: 1em 0;
}

.naming-pattern code {
  background: var(--md-code-bg-color, #f5f5f5);
  padding: 2px 6px;
  border-radius: 4px;
}
.table-name-part {
  text-decoration: underline;
  text-decoration-thickness: 2px;
  text-underline-offset: 0.18em;
}
</style>

# Metadata & Table/Variable Naming Conventions

Tabulated HBCD study data is organized into a standardized table format per study instrument/measure, with each table containing a set of variables. Both the metadata conventions and table/variable naming conventions follow NBDC standards and therefore largely align with the ABCD Study - see [Metadata](https://docs.abcdstudy.org/latest/documentation/curation/metadata.html) and [Naming conventions](https://docs.abcdstudy.org/latest/documentation/curation/naming.html) information within the ABCD data documentation site. Metadata is organized via a data dictionary following NBDC standards, which provides detailed information about table variables, including variable name, label, description, data type, etc. Table/variable naming conventions ensure consistency across instruments and derived datasets and intuitive parsing of variable meaning and structure.

## NBDC Data Dictionary Elements

<div id="lasso" class="banner data-warning" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
<span class="text-with-link">
<span class="text">Warnings, Caveat, & Notes</span>
<a class="anchor-link" href="#lasso" title="Copy link">
  <i class="fa-solid fa-link"></i>
</a>
</span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<div class="info-section">
<div class="info-section-title">
  <b>WARNING: Incorrect Data Types Inferred for CSV/TSV</b>
</div>
<p>
  CSV and TSV files do not contain an embedded data schema. Because column
  metadata are provided separately, import tools in Python and R may infer
  some column types incorrectly. For example:
</p>
<ul>
  <li>
    Categorical codes stored as strings, such as <code>"0"</code> and
    <code>"1"</code> for “No” and “Yes,” may be imported as numbers.
  </li>
  <li>
    Numeric columns may be imported as text when missing values are represented
    as <code>n/a</code>, as required for TSV files by the BIDS specification.
  </li>
</ul>
<p>
  <b>It is therefore critical that you specify column types during import</b>, particularly data type (<code>type_data</code>), using the accompanying metadata. See <a href="../../resources/tools/#nbdctools">NBDCtools</a> for available functions to automate this process (e.g. <a href="https://software.nbdc-datahub.org/NBDCtools/reference/read_dsv_formatted.html"><code>read_dsv_formatted()</code></a> for R users).
</p>
</div>
<div class="info-section">
<div class="info-section-title">
  NBDC Data Access Platform: Blank Columns in Query Tool
</div>
<p>
  Dictionary Query Tool searches within the NBDC Data Access Platform currently display columns that are not applicable to HBCD study data, including columns ending with <code>nda</code>, <code>deap</code>, and <code>redcap</code>. Inapplicable columns will be removed in the future and can safely be ignored. Note that columns may also be blank if they have yet to be populated, currently common for Spanish-specific version (ending with <code>*_es</code>) and variable-level responsible use (<code>url_warn_use</code>) and data warnings (<code>url_warn_data</code>). Only active and applicable columns are included in the data dictionary table below for clarity.
</p>
</div>
<div class="info-section">
<div class="info-section-title">
  NBDC Data Access Platform: Site & Cohort Information
</div>
<p>
  Datasets downloaded from the NBDC Data Access Platform contain two additional fields not listed in the data dictionary, <code>cohort</code> and <code>site</code>, derived directly from <strong>Visit Level Data</strong> table variables (<code>par_visit_data_{cohort/site}</code>) - see the <a href="../../instruments/demo/visitinfo">Visit Level Data</a> page for details.
</p>
</div>
</div>

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

<table class="compact-table-no-vertical-lines dd">
<thead>
<tr>
  <th>Name</th>
  <th>Label</th>
  <th>Description & Possible Values</th>
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
  <td>
    Study domain
    <div class="dd-inline-list">
      e.g., Demographics — see <a href="../../instruments/#instruments-by-domain">Study Instruments</a>
    </div>
  </td>
</tr>

<tr>
  <td><code>source</code></td>
  <td>Source</td>
  <td>
    Source of information
    <div class="dd-inline-list">
        <span>Biological Mother</span>
        <span>Caregiver (Responsible Adult)</span>
        <span>Child</span>
        <span>General</span>
    </div>
  </td>
</tr>

<tr>
  <td><code>study</code></td>
  <td>Study</td>
  <td>
    Study type
    <div class="dd-inline-list">
        <span>Core</span>
        <span>Substudy</span>
    </div>
  </td>
</tr>

<!-- IMAGING -->
<tr class="table-group-row">
  <td colspan="3">Imaging</td>
</tr>

<tr>
  <td><code>atlas</code></td>
  <td>Atlas</td>
  <td>
    MRI atlas used for parcellated structural measures and functional timeseries
    <div class="dd-inline-list">
      e.g., <i>Glasser</i>, <i>Gordon</i> — <a href="../../instruments/mri/fmri/#parc">see full list</a>
    </div>
  </td>
</tr>

<tr>
  <td><code>metric</code></td>
  <td>Metric</td>
  <td>
    Specific assessment metric
    <div class="dd-inline-list">
      e.g., <i>T1 Volume</i>, <i>Cortical Thickness</i>, <i>Sulcal Depth</i>, <i>Neurometabolites</i>
    </div>
  </td>
</tr>

<tr>
  <td><code>sub_domain</code></td>
  <td>Subdomain</td>
  <td>
    Imaging domain subcategory
    <div class="dd-inline-list">
      e.g., <i>Structural MRI</i>, <i>Resting State fMRI</i>, <i>MR Spectroscopy</i>
    </div>
  </td>
</tr>

<!-- TABLE-LEVEL -->
<tr class="table-group-row">
  <td colspan="3">Table-level Information</td>
</tr>

<tr>
  <td><code>table_label</code></td>
  <td>Table label</td>
  <td>
    Human-readable table name
    <div class="dd-inline-list">
      e.g., <i>Demographics</i>
    </div>
  </td>
</tr>

<tr>
  <td><code>table_name</code><i class="fa-solid fa-lock table-icon"></i></td>
  <td>Table name</td>
  <td>
    Database table name
    <div class="dd-inline-list">
      e.g., <code>sed_bm_demo</code>
    </div>
  </td>
</tr>

<tr>
  <td><code>url_table</code></td>
  <td>Documentation</td>
  <td>Link to measure README/documentation page (<a href="../../instruments/">see all</a>)</td>
</tr>

<tr>
  <td><code>url_table_warn_data</code></td>
  <td>Data Warning</td>
  <td>
    Table-level <a href="../../access/resp_data_use/#data-warning">Data Warning</a>
  </td>
</tr>

<tr>
  <td><code>url_table_warn_use</code></td>
  <td>Use Warning</td>
  <td>
    Table-level <a href="../../access/resp_data_use/#alert"> Responsible Use Warning</a>
  </td>
</tr>

<!-- VARIABLE LEVEL -->
<tr class="table-group-row">
  <td colspan="3">Variable-level Information</td>
</tr>

<tr>
  <td><code>description</code> / <code>label</code><i class="fa fa-language table-icon"></i></td>
  <td>Variable label</td>
  <td>
    Human-readable variable name
    <div class="dd-inline-list">
      e.g., <i>Highest grade completed</i>
    </div>
  </td>
</tr>

<tr>
  <td><code>header</code><i class="fa fa-language table-icon"></i></td>
  <td>Header</td>
  <td>
    Header or instructions for a question set
    <div class="dd-inline-list">
      e.g., <i>For each item that describes your child...</i>
    </div>
  </td>
</tr>

<tr>
  <td><code>instruction</code><i class="fa fa-language table-icon"></i></td>
  <td>Instruction</td>
  <td>
    Instruction text preceding items
    <div class="dd-inline-list">
      e.g., <i>The next set of questions is about your child's behavior...</i>
    </div>
  </td>
</tr>

<tr>
<td><code>levels</code><i class="fa fa-language table-icon"></i></td>
<td>Levels</td>
<td>
<b>Value: Label</b> mappings for categorical variables, e.g. 
<span class="tooltip">
  <i>0: FALSE ; 1: TRUE</i>
  <span class="tooltiptext">
    <img src="../levels.png"
         alt="Levels table example"
         style="max-height: 150px;">
  </span>
</span>
</td>
</tr>

<tr>
  <td><code>name</code><i class="fa-solid fa-lock table-icon"></i></td>
  <td>Variable name</td>
  <td>
    Variable name within table
    <div class="dd-inline-list">
      e.g., <code>sed_bm_demo_edu_001</code>
    </div>
  </td>
</tr>
<tr>
  <td><code>note</code><i class="fa fa-language table-icon"></i></td>
  <td>Note</td>
  <td>
    Note displayed to participants
    <div class="dd-inline-list">
      e.g., <i>Enter weight in pounds.</i>
    </div>
  </td>
</tr>
<tr>
  <td><code>type_data</code><i class="fa-solid fa-lock table-icon"></i></td>
  <td>Data type</td>
  <td>
    <div class="dd-inline-list">
        <span>character <i>(for categorical variables)</i></span>
        <span>date</span>
        <span>double</span>
        <span>integer</span>
        <span>text</span>
        <span>time</span>
        <span>timestamp</span>
    </div>
  </td>
</tr>
<tr>
  <td><code>type_level</code></td>
  <td>Level of measurement</td>
  <td>
      <div class="dd-inline-list">
        <span>interval</span>
        <span>nominal</span>
        <span>ordinal</span>
        <span>ratio</span>
    </div>
  </td>
</tr>
<tr>
  <td><code>type_var</code></td>
  <td>Variable type</td>
  <td>
    Variable classification - <a href="#variable-types">see definitions below</a>
    <div class="dd-inline-list">
        <span>administrative</span>
        <span>derived item</span>
        <span>item</span>
        <span>summary score</span>
    </div>
  </td>
</tr>
<tr>
  <td><code>unit</code></td>
  <td>Unit</td>
  <td>
    Measurement unit
    <div class="dd-inline-list">
      e.g., <i>years</i>, <i>cm</i>, <i>lbs</i>
    </div>
  </td>
</tr>
<!-- <tr>
  <td><code>url_warn_data</code></td>
  <td>Data Warning (var)</td>
  <td>Variable-level <a href="../../access/resp_data_use/#data-warning">Data Warning</a></td>
</tr>
<tr>
  <td><code>url_warn_use</code></td>
  <td>Responsible Use Warning (var)</td>
  <td>Variable-level <a href="../../access/resp_data_use/#alert">Responsible Use Warning</a></td>
</tr> -->

<!-- DISPLAY -->
<tr class="table-group-row">
  <td colspan="3">Display Properties / Identifiers / Order</td>
</tr>

<tr>
  <td><code>branching_logic</code></td>
  <td>Branching logic</td>
  <td>Logic controlling whether an item/question is shown</td>
</tr>

<tr>
  <td><code>identifier_column</code><i class="fa-solid fa-lock table-icon"></i></td>
  <td>Identifier column(s)</td>
  <td>
    <a href="../../datacuration/phenotypes/#table-organization">Participant/session identifiers</a>
    <div class="dd-inline-list">
    <span>participant_id</span>
    <span>session_id</span>
    <span>run_id</span>
    </div>

  </td>
</tr>

<tr>
  <td><code>order_display</code></td>
  <td>Display order</td>
  <td>Order in which an item/question is displayed to participants for a given measure</td>
</tr>

<tr>
  <td><code>order_sort</code></td>
  <td>Sort order</td>
  <td>Standard sort order in table/measure (and column order in database)</td>
</tr>

<tr>
  <td><code>type_field</code></td>
  <td>Field type</td>
  <td>  
    Input type presented to participants
    <div class="dd-inline-list">
      e.g., <i>dropdown</i>, <i>radio</i>, <i>checkbox</i>
    </div>
  </td>
</tr>

</tbody>
</table>

### Variable Types

<table class="table-no-vertical-lines dd">
<thead>
<tr>
<th>Variable Type</th>
<th>Description & Possible Values</th>
</tr>
</thead>
<tbody>
<tr>
<td>administrative</td>
<td>Data that gives context to the assessments.
  Possible values include:
  <div class="dd-inline-list">
  <span>adjusted_age</span>
  <span>candidate_age</span>
  <span>gestational_age</span>
  <span>date_taken</span>
  <span>administration</span>
  <span>lang</span>
  <span>location</span>
  </div>
</td>
</tr>
<tr>
  <td>derived item</td>
  <td>
      Derived from original participant data, either directly (e.g., <code>sex</code> from administrative records) or by combining variables (e.g., race and ethnicity)
      <div class="dd-inline-list">
      See <a href="../../instruments/demo/static/">Basic Demographics</a> for examples
      </div>
  </td>
</tr>
<tr>
  <td>item</td>
  <td>Original data provided by the participant, e.g. questions in a questionnaire</td>
</tr>
<tr>
  <td>summary score</td>
  <td>Summary and/or score output based on algorithmic conversions of items/raw data
    <div class="dd-inline-list">
      e.g., <i>summary_score, total_score</i>
    </div>
  </td>
</tr>
</tbody>
</table>


## Naming Conventions

The instrument table and variable names used for tabulated HBCD study data largely follow standardized naming conventions adapted from the [ABCD Study](https://docs.abcdstudy.org/latest/documentation/curation/naming.html). This ensures consistency across instruments and derived datasets, allowing for intuitive parsing of variable meaning and structure.

### Convention Logic & Rules

Variable names are constructed from a set of ordered main components separated by single underscores. Subcomponents, if present, are preceded by double or triple underscores, which represent *subscale*, *version*, or *counter type* and multiselect fields. Main components include:
<div class="naming-pattern"><code><span class="table-components"><span style="background-color: #f500e92c">domain_source_table</span></span>_{scale}_item</code>
</div>

 - The first 3 main components, <code><span style="background-color: #f500e92c">domain_source_table</span></code>, make up the name of the table
 - <code><span style="color: teal;">{scale}</span></code> is only included for instruments that have subscales

<table class="table-no-vertical-lines">
<thead class="table-header">
<tr>
<th width="35%">Naming Component</th>
<th>Possible Values</th>
</tr>
</thead>
<tbody>
<tr>
<td>
  <span class="naming-token"><code>domain</code></span>
  <div class="naming-description">
    Data domain
  </div>
</td>
<td>
<div class="dd-inline-list">
<ul>
    <li><code>bio</code>: Biospecimen &amp; Omics</li>
    <li><code>eeg</code>: Tabular EEG</li>
    <li><code>img</code>: Tabular Imaging</li>
    <li><code>mh</code>: Behavior/Child-Caregiver Interaction</li>
    <li><code>ncl</code>: Neurocognition and Language</li>
    <li><code>nt</code>: Novel Technology &amp; Wearable Sensors</li>
    <li><code>ph</code>: Physical Health</li>
    <li><code>pex</code>: Pregnancy/Exposure Including Substance</li>
    <li><code>sed</code>: Social and Environmental Determinants</li>
</ul>
</div>
</td>
</tr>

<tr>
<td>
    <span class="naming-token"><code>source</code></span>
    <div class="naming-description">
    Respondent <b>OR</b> who the data is about
    </div>
</td>
<td>
<div class="dd-inline-list">
<ul>
    <li><code>bm</code>: Biological Mother</li>
    <li><code>cg</code>: Caregiver (Responsible Adult)</li>
    <li><code>ch</code>: Child</li>
    <li><code>ld</code>: Linked Data</li>
    <li><code>ra</code>: RA (Research Assistant)</li>
</ul>
</div>
</td>
</tr>

<tr>
<td>
    <span class="naming-token"><code>table</code></span>
    <div class="naming-description">
    Instrument name
    </div>
</td>
<td>
<div class="dd-inline-list">
e.g., <code>ibqr</code> — Infant Behavior Questionnaire–Revised (IBQ-R)
</div>
</td>
</tr>

<tr>
<td>
    <span class="naming-token"><code>{scale}</code></span>
    <div class="naming-description">
    Instrument subscale, as applicable
    </div>
</td>
<td>
<div class="dd-inline-list">
e.g., <code>mh_cg_ibqr_<span style="color: teal;"><b>beh</b></span>_001</code> = <b>Behavioral Inhibition</b> subscale
</div>
</td>
</tr>

<tr>
<td>
    <span class="naming-token"><code>item</code></span>
    <div class="naming-description">
    Item number OR admin/score fields
    </div>
</td>
<td>
<div class="dd-inline-list">
<ul>
  <li>Item number example: <code>001</code></li>
  <li>See <a href="#variable-types">Variable Types</a> for details on administrative and summary score fields</li>
</ul>
</div>
</td>
</tr>
</tbody>
</table>

### Exceptions

Some table/variable names deviate from the standard naming conventions. One notable example is [tabulated derivatives](../datacuration/overview.md#tabulated-pipeline-derivatives) generated from processed imaging and EEG data. These tables are named based on the pattern `domain_pipeline_derivative`, where `derivative` corresponds to the basename of the source derivative files. For example:       

- The tabulated BIBSNet file: <code>img_bibsnet<span style="color: teal;">_space-T1w_desc-aseg_volumes</span>.tsv</code>
- Is sourced from: <code>sub-[ID]_ses-[V0X]<span style="color: teal;">_space-T1w_desc-aseg_volumes</span>.tsv</code>

