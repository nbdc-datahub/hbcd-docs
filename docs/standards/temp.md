<style>
.wy-nav-content {
    width: 95% !important;
    max-width: 95% !important;
    flex-grow: 1 !important;
}
.dd-values {
  margin: 0.25em 0 0 1.2em;
  padding: 0;
  font-size: 0.9em;
}

.dd-values li {
  margin: 0.1em 0;
}

.dd-note {
  color: #6b7280;
  font-size: 0.9em;
}
.dd-inline-list {
  margin-top: 0.2em;
  font-size: 0.9em;
  color: #6b7280;
}
.dd-inline-list span:not(:last-child)::after {
  content: "·";
  margin: 0 0.6em;
}
</style>


# NBDC Data Dictionary

## NEW

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
      e.g., <i>Glasser</i>, <i>Gordon</i> — <a href="../../instruments/mri/fmri/#parc" target="_blank">see full list</a>
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
  <td>Data Warning (table)</td>
  <td>
    Table-level <a href="../../access/resp_data_use/#warnings" target="_blank">Data Warning</a>
  </td>
</tr>

<tr>
  <td><code>url_table_warn_use</code></td>
  <td>Responsible Use Warning (table)</td>
  <td>
    Table-level <a href="../../access/resp_data_use/#warnings" target="_blank"> Responsible Use Warning</a>
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
    <b>Value: Label</b> mappings for categorical variables
    <div class="dd-inline-list">
      e.g. <span class="tooltip"><i>0: FALSE ; 1: TRUE</i>
        <span class="tooltiptext">
          <img src="../levels.png" alt="Levels table example" style="max-height: 200px;">
        </span>
      </span>
    </div>
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

<tr>
  <td><code>url_warn_data</code></td>
  <td>Data Warning (var)</td>
  <td>Variable-level <a href="../../access/resp_data_use/#warnings" target="_blank">Data Warning</a></td>
</tr>

<tr>
  <td><code>url_warn_use</code></td>
  <td>Resp Use Warning (var)</td>
  <td>Variable-level <a href="../../access/resp_data_use/#warnings" target="_blank">Responsible Use Warning</a></td>
</tr>

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
    Participant/session identifiers
    <div class="dd-inline-list">
      <a href="../../datacuration/phenotypes/#table-organization" target="_blank">See details</a>
    </div>
  </td>
</tr>

<tr>
  <td><code>identifier_column</code><i class="fa-solid fa-lock table-icon"></i></td>
  <td>Identifier column(s)</td>
  <td>Columns used for participant identification (i.e. participant & session ID)- <a href="../../datacuration/phenotypes/#table-organization" target="_blank">see details</a></td>
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
