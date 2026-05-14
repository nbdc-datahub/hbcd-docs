<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>

# NBDC Data Dictionary

Tabulated HBCD study data is organized into a standardized table format per study instrument/measure, with each table containing a set of variables (see [Data Structure Overview](../datacuration/overview.md) for details). Metadata is organized via a data dictionary, which provides detailed information about table variables, including variable name, label, description, data type, etc. All data dictionary elements are outlined below.

## Data Dictionary Elements

<p style="font-size: 0.9em; color: #696969ff; font-weight: bold;">
<i style="color: teal;" class="fa-solid fa-lock"></i>&nbsp;= Values do not vary across releases&nbsp;&nbsp;
<i style="color: teal;" class="fa fa-language"></i>&nbsp;= Column available in Spanish (includes <code>label_es</code>, <code>instruction_es</code>, <code>header_es</code>, <code>note_es</code>)
</p>
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #f0dcfb;">
<tr style="border-bottom:2px solid #ccc;">
  <th style="width: 20%;">NAME</th>
  <th style="width: 20%;">LABEL</th>
  <th>DESCRIPTION & POSSIBLE/EXAMPLE VALUES</th>
</tr>
</thead>
<tbody>
<!-- CORE METADATA -->
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>CORE METADATA</b></td>
</tr>
<tr>
  <td><code>study</code></td>
  <td>Study</td>
  <td>Part of core (<code>Core</code>) or substudy (<code>Substudy</code>)</td>
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
<!-- IMAGING -->
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>IMAGING & EEG</b></td>
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
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>TABLE-LEVEL INFORMATION</b></td>
</tr>
<tr>
  <td><code>table_name</code>&nbsp; <i style="color: teal;" class="fa-solid fa-lock"></i></td>
  <td>Table name</td>
  <td>Table name (e.g. <code>sed_bm_demo</code>)</td>
</tr>
<tr>
  <td><code>table_label</code></td>
  <td>Table label</td>
  <td>Human-readable label for table name (e.g. <i>Demographics</i>)</td>
</tr>
<tr>
  <td><code>url_table</code></td>
  <td>Documentation (table)</td>
  <td>Link to documentation page</td>
</tr>
<tr>
  <td><code>url_table_warn_use</code></td>
  <td>Resp Use Warning (table)</td>
  <td>Responsible Use Warning (<a href="../../access/resp_data_use/#warnings" target="_blank">see details</a>)</td>
</tr>
<tr>
  <td><code>url_table_warn_data</code></td>
  <td>Data Warning (table)</td>
  <td>Data Warning (<a href="../../access/resp_data_use/#warnings" target="_blank">see details</a>)</td>
</tr>
<!-- VAR LEVEL -->
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>VARIABLE-LEVEL INFORMATION</b></td>
</tr>
<tr>
  <td><code>name</code>&nbsp; <i style="color: teal;" class="fa-solid fa-lock"></i></td>
  <td>Variable name</td>
  <td>Variable name within a table (e.g. <code>sed_bm_demo_edu_001</code>)</td>
</tr>
<tr>
  <td><code>label</code>&nbsp; <i style="color: teal;" class="fa fa-language"></i>/<br><code>description</code></td>
  <td>Variable label</td>
  <td>Human-readable label for variable (e.g. <i>Highest grade completed</i>)</td>
</tr>

<tr>
  <td><code>levels</code>&nbsp; <i style="color: teal;" class="fa fa-language"></i></td>
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
  <td><code>instruction</code>&nbsp; <i style="color: teal;" class="fa fa-language"></i></td>
  <td>Instruction</td>
  <td>
    Instructions preceding form items (e.g. <i>The next set of questions is about your child's behavior...</i>)</td>
<!-- POTENTIALLY ADD IN FUTURE TO INSTRUCTION DESCRIPTION: <i class="fas fa-exclamation-triangle" style="font-size: 1em; color: orange;"></i> and <i class="fas fa-exclamation-triangle" style="font-size: 1em; color: orange;"></i> <b>CAUTION: Text may be incomplete/misaligned! See <a href="../../changelog/issues-updates/#known-issues">Known Issues: Instruction Metadata</a></b> -->
</tr>
<tr>
  <td><code>header</code>&nbsp; <i style="color: teal;" class="fa fa-language"></i></td>
  <td>Header</td>
  <td>Header/instructions for a set of questions (e.g. <i>For each item that describes your child...</i>)</td>
</tr>
<tr>
  <td><code>note</code>&nbsp; <i style="color: teal;" class="fa fa-language"></i></td>
  <td>Note</td>
  <td>Note displayed to participants (e.g. <i>Enter weight in pounds.</i>)</td>
</tr>
<tr>
  <td><code>unit</code></td>
  <td>Unit</td>
  <td>Unit of measurement (e.g. <i>years, cm, lbs, etc.</i>)</td>
</tr>
<tr>
  <td><code>url_warn_use</code></td>
  <td>Resp Use Warning (var)</td>
  <td>Responsible Use Warning (<a href="../resp_data_use/#warnings" target="_blank">see details</a>) - variable-specific</td>
</tr>
<tr>
  <td><code>url_warn_data</code></td>
  <td>Data Warning (var)</td>
  <td>Data Warning (<a href="../resp_data_use/#warnings" target="_blank">see details</a>) - variable-specific</td>
</tr>
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>VARIABLE TYPE & FORMAT</b></td>
</tr>
<tr>
  <td><code>type_var</code></td>
  <td>Variable type</td>
  <td>Includes: <i>administrative; item; derived item; summary score</i> -  <a href="#type_var">see details</a></td>
</tr>
<tr>
  <td><code>type_data</code>&nbsp; <i style="color: teal;" class="fa-solid fa-lock"></i></td>
  <td>Data type</td>
  <td>Includes: <i>date; timestamp; time; <span class="tooltip">character<span class="tooltiptext">Only used for categorical columns</span></span>; text; integer; double</i></td>
</tr>
<tr>
  <td><code>type_level</code></td>
  <td>Level of measurement</td>
  <td>Includes: <i>nominal; ordinal; interval; ratio</i></td>
</tr>
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>DISPLAY PROPERTIES</b></td>
</tr>
<tr>
  <td><code>type_field</code></td>
  <td>Field type</td>
  <td>Field type presented to participant (e.g. <i>dropdown, radio, checkbox, etc.</i>)</td>
</tr>
<tr>
  <td><code>order_display</code></td>
  <td>Display order</td>
  <td>Order in which item is displayed to participants within a given measure</td>
</tr>
<tr>
  <td><code>branching_logic</code></td>
  <td>Branching logic</td>
  <td>Branching logic applied to variable/question</td>
</tr>
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>IDENTIFIERS & ORDER</b></td>
</tr>
<tr>
  <td><code>identifier_column</code>&nbsp; <i style="color: teal;" class="fa-solid fa-lock"></i></td>
  <td>Identifier column(s)</td>
  <td>Columns used for participant identification (i.e. participant & session ID)- <a href="../../datacuration/phenotypes/#table-organization" target="_blank">see details</a></td>
</tr>
<tr>
  <td><code>order_sort</code></td>
  <td>Sort order</td>
  <td>Standard sort order in table/measure (and column order in database)</td>
</tr>
</tbody>
</table>

<!-- Type variable values -->
<div id="type_var" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i style="margin-right: 4px;" class="fa fa-book"></i></span>
  <span class="text-with-link">
  <span class="text">Variable Type (<code>type_var</code>) Definitions</span>
  <a class="anchor-link" href="#type_var" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
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
</div>

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
<p>Dictionary Query Tool searches within the NBDC Data Access Platform currently display columns that are not applicable to HBCD study data, including columns ending with <code>nda</code>, <code>deap</code>, and <code>redcap</code>. Inapplicable columns will be removed in the future and can safely be ignored. Note that columns may also be blank if they have yet to be populated (currently common for columns ending with <code>*_es</code>). <b>For reference, only applicable columns are included in the Data Dictionary overview above.</b></p>
</div>
<!-- 
## Levels Table
<p style="font-size: 0.9em; color: #696969ff; font-weight: bold;">
<i style="color: teal;" class="fa-solid fa-lock"></i>&nbsp;= Values do not vary across releases
</p>
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #f0dcfb;">
<tr style="border-bottom:2px solid #ccc;">
  <th style="width: 20%;">Name</th>
  <th style="width: 10%;">JSON Element</th>
  <th style="width: 70%;">Description</th>
</tr>
</thead>
<tbody>
  <tr>
    <td><code>name</code>&nbsp; <i style="color: teal;" class="fa-solid fa-lock"></i></td>
    <td>&nbsp;</td>
    <td>Name of the categorical column/variable/question for which value/label pairs are reported</td>
  </tr>
  <tr>
    <td><code>value</code>&nbsp; <i style="color: teal;" class="fa-solid fa-lock"></i></td>
    <td>left hand side</td>
    <td>Value of the level (<b>e.g. "1"</b>)</td>
  </tr>
  <tr>
    <td><code>order_level</code>&nbsp; <i style="color: teal;" class="fa-solid fa-lock"></i></td>
    <td></td>
    <td>Order of response option as displayed to participants (and in data) (<b>e.g. "2"</b>)</td>
  </tr>
  <tr><td><code>label</code> / <code>label_es</code></td><td>right hand side</td>
    <td>Label (English/Spanish) of the level (<b>e.g. "Yes" / "Si"</b>)</td>
  </tr>
</table> -->

## Additional Information: Site & Cohort

When using datasets downloaded from the NBDC Data Access Platform, two additional variables not listed in the data dictionary, `cohort` and `site`, are included. These are derived from the <a href="../../instruments/demo/visitinfo" target="_blank">Visit Level Data</a> (`par_visit_data`) table. 

- **`cohort`** — Derived from `par_visit_data_cohort`. See <a href="../../instruments/demo/visitinfo/#cohort-caregiver-types" target="_blank">Cohort & Caregiver Types</a> for details.  
- **`site`** — Derived from `par_visit_data_site`, indicating the site where each visit occurred (which may vary between visits). Note that this differs from `recruitment_site` in <a href="../../instruments/demo/basicdemo/" target="_blank">Basic Demographics</a>, which refers to the site at time of recruitment.

The following table (expand to view) shows the global mapping between site IDs across variables in different datasets. 

<div id="sites" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i style="font-size: 0.9em;" class="fa-solid fa-location-dot"></i></span>
  <span class="text-with-link">
  <span class="text">Global Site ID Mapping</span>
  <a class="anchor-link" href="#sites" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width:100%;border-collapse:collapse;table-layout:fixed;">
<thead>
<tr style="border-bottom:2px solid #ccc;"><th>Basic Demographics Site ID</th><th>Visit Level Data Site ID</th><th>Site Name</th></tr>
</thead>
<tbody>
<tr><td>0</td><td>hbcdsite64</td><td>Arkansas Children's Hospital (site 1)</td></tr>
<tr><td>1</td><td>hbcdsite02</td><td>Arkansas Children's Hospital (site 2 - UAMS)</td></tr>
<tr><td>2</td><td>hbcdsite48</td><td>Boston Children's Hospital - Harvard Medical School</td></tr>
<tr><td>3</td><td>hbcdsite95</td><td>Cedars Sinai (site 1)</td></tr>
<tr><td>4</td><td>hbcdsite23</td><td>Cedars Sinai (site 2 - UCLA)</td></tr>
<tr><td>5</td><td>hbcdsite07</td><td>Children's Hospital Los Angeles</td></tr>
<tr><td>6</td><td>hbcdsite09</td><td>Children's Hospital of Philadelphia</td></tr>
<tr><td>7</td><td>hbcdsite04</td><td>Cincinnati Children's Hospital</td></tr>
<tr><td>8</td><td>hbcdsite20</td><td>Emory University School of Medicine</td></tr>
<tr><td>9</td><td>hbcdsite52</td><td>Johns Hopkins University</td></tr>
<tr><td>10</td><td>hbcdsite06</td><td>New York University</td></tr>
<tr><td>11</td><td>hbcdsite69</td><td>Northwestern University</td></tr>
<tr><td>12</td><td>hbcdsite72</td><td>Oklahoma State</td></tr>
<tr><td>13</td><td>hbcdsite93</td><td>Oregon Health &amp; Science University</td></tr>
<tr><td>14</td><td>hbcdsite78</td><td>Pennsylvania State University (site 1 - UP)</td></tr>
<tr><td>15</td><td>hbcdsite53</td><td>Pennsylvania State University (site 2 - COM)</td></tr>
<tr><td>16</td><td>hbcdsite79</td><td>University of Alabama at Birmingham (site 1)</td></tr>
<tr><td>17</td><td>hbcdsite28</td><td>University of Alabama at Birmingham (site 2 - UAT)</td></tr>
<tr><td>18</td><td>hbcdsite77</td><td>University of California San Diego</td></tr>
<tr><td>19</td><td>hbcdsite92</td><td>University of Maryland</td></tr>
<tr><td>20</td><td>hbcdsite70</td><td>University of Minnesota</td></tr>
<tr><td>21</td><td>hbcdsite84</td><td>University of New Mexico</td></tr>
<tr><td>22</td><td>hbcdsite29</td><td>University of North Carolina (site 1)</td></tr>
<tr><td>23</td><td>hbcdsite27</td><td>University of North Carolina (site 2 - Wake Forest)</td></tr>
<tr><td>24</td><td>hbcdsite67</td><td>University of Vermont</td></tr>
<tr><td>25</td><td>hbcdsite57</td><td>University of Wisconsin</td></tr>
<tr><td>26</td><td>hbcdsite35</td><td>Vanderbilt University</td></tr>
<tr><td>27</td><td>hbcdsite26</td><td>Washington University in St. Louis</td></tr>
<tr><td>28</td><td>hbcdsite43</td><td>Virginia Tech</td></tr>
<tr><td>29</td><td>hbcdsite42</td><td>University of Florida</td></tr>
</tbody>
</table>
</div>