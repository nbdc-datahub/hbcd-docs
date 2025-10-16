# NBDC Data Dictionary

**Tabulated HBCD data is organized into a standardized table format, each of which contains a set of variables** (see [Data Structure Overview](../datacuration/overview.md) for details). The metadata for studies released via the NBDC Data Hub consists of:

 - **Data dictionary**: Provides detailed information about the tables and table variables, including variable name, label, description, data type, and other relevant information. 
 - **Levels table**: Provides information about the levels of categorical variables (label, order, etc.)

**Below are the definitions for the columns in the data dictionary and levels tables.**

### Data Dictionary Columns
<!-- DD -->
<table class="compact-table" style="font-size: 14px;">
<thead>
<tr>
  <th style="width: 15%;">NAME</th>
  <th style="width: 20%;">LABEL</th>
  <th>DESCRIPTION & POSSIBLE/EXAMPLE VALUES</th>
  <th style="width: 3%; text-align:center;"><a href="#legend">NOTE</a></th>
</tr>
</thead>
<tbody>
<!-- CORE METADATA -->
<tr>
  <td><code>study</code></td>
  <td>Study</td>
  <td style="word-wrap: break-word; white-space: normal;">Part of core (<code>Core</code>) or substudy (<code>Substudy</code>)</td>
  <td></td>
</tr>
<tr>
  <td><code>domain</code></td>
  <td>Domain</td>
  <td style="word-wrap: break-word; white-space: normal;">e.g. <i>Demographics, Biospecimens</i>, etc. – <a href="#domain-source-values">see full list</a></td>
  <td></td>
</tr>
<tr>
  <td><code>source</code></td>
  <td>Source</td>
  <td style="word-wrap: break-word; white-space: normal;">Source of information, e.g.: <i>Biological Mother, Child</i>, etc. - <a href="#domain-source-values">see list</a></td>
  <td></td>
</tr>
<!-- TABLE STRUCTURE -->
<tr>
  <td><code>table_name</code></td>
  <td>Table name</td>
  <td style="word-wrap: break-word; white-space: normal;">Coded table name, e.g. <code>sed_bm_demo</code></td>
  <td style="text-align:center;"><i class="fa-solid fa-lock" style="font-size: 1.2em;"></i></td>
</tr>
<tr>
  <td><code>table_label</code></td>
  <td>Table label</td>
  <td style="word-wrap: break-word; white-space: normal;">Label for coded table name, e.g. <i>Demographics</i></td>
  <td style="text-align:center;"><i style="font-size: 1.4em;" class="bi bi-filetype-json"></i></td>
</tr>
<!-- VARIABLE METADATA -->
<tr>
  <td><code>name</code></td>
  <td>Variable name</td>
  <td style="word-wrap: break-word; white-space: normal;">Coded variable name within a table, e.g. <code>sed_bm_demo_edu_001</code></td>
  <td style="text-align:center;"><i class="fa-solid fa-lock"></i></td>
</tr>
<tr>
  <td><code>label</code></td>
  <td>Variable label</td>
  <td style="word-wrap: break-word; white-space: normal;">Label for coded variable name, e.g. <i>Highest grade completed</i></td>
  <td style="text-align:center;"><i style="font-size: 1.4em;" class="bi bi-filetype-json"></i></td>
</tr>
<tr>
  <td><code>instruction</code></td>
  <td>Instruction</td>
  <td style="word-wrap: break-word; white-space: normal;">Instructions preceding measure questions (e.g. <i>The next set of questions is about your child's behavior...</i>)</td>
  <td style="text-align:center;"><i class="fas fa-exclamation-triangle" style="color:orange; font-size: 1.3em;"></i></td>
</tr>
<tr>
  <td><code>header</code></td>
  <td>Header</td>
  <td style="word-wrap: break-word; white-space: normal;">Header/instructions for a set of questions (e.g. <i>For each item that describes your child...</i>)</td>
  <td></td>
</tr>
<tr>
  <td><code>note</code></td>
  <td>Note</td>
  <td style="word-wrap: break-word; white-space: normal;">Note displayed to participants (e.g. <i>Enter weight in pounds.</i>)</td>
  <td></td>
</tr>
<tr>
  <td><code>unit</code></td>
  <td>Unit</td>
  <td style="word-wrap: break-word; white-space: normal;">Unit of measurement (e.g. <i>m, cm², lbs</i>)</td>
  <td style="text-align:center;"><i style="font-size: 1.4em;" class="bi bi-filetype-json"></i></td>
</tr>
<!-- VARIABLE TYPES -->
<tr>
  <td><code>type_var</code></td>
  <td>Variable type</td>
  <td style="word-wrap: break-word; white-space: normal;">Possible values include: <i>administrative</i>; <i>item</i>; <i>derived item</i>; <i>summary score</i> - <a href="">see details</a></td>
  <td style="text-align:center;"><i style="font-size: 1.4em;" class="bi bi-filetype-json"></i></td>
</tr>
<tr>
  <td><code>type_data</code></td>
  <td>Data type</td>
  <td style="word-wrap: break-word; white-space: normal;">Possible values include: <i>date; timestamp; time; character; text; integer; double</i> (character only used for categorical columns)</td>
  <td style="text-align:center;"><i class="fa-solid fa-lock"></i></td>
</tr>
<tr>
  <td><code>type_level</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Level of measurement</td>
  <td style="word-wrap: break-word; white-space: normal;">Possible values: <i>nominal; ordinal; interval; ratio</i></td>
  <td></td>
</tr>
<tr>
  <td><code>type_field</code></td>
  <td>Field type</td>
  <td style="word-wrap: break-word; white-space: normal;">Field type in data capture system as presented to participant (e.g. <i>dropdown; radio; checkbox</i>)</td>
  <td></td>
</tr>
<!-- DISPLAY PROPERTIES -->
<tr>
  <td><code>order_display</code></td>
  <td>Display order</td>
  <td style="word-wrap: break-word; white-space: normal;">Display order of item within measure</td>
  <td></td>
</tr>
<tr>
  <td><code>branching_logic</code></td>
  <td>Branching logic</td>
  <td style="word-wrap: break-word; white-space: normal;">Branching logic applied to variable/question</td>
  <td></td>
</tr>
<tr>
  <td><code>label_es</code></td>
  <td>Label (Spanish)</td>
  <td>Label in Spanish</td>
  <td></td>
</tr>
<tr>
  <td><code>instruction_es</code></td>
  <td>Instruction (Spanish)</td>
  <td style="word-wrap: break-word; white-space: normal;">Instruction text in Spanish</td>
  <td></td>
</tr>
<tr>
  <td><code>header_es</code></td>
  <td>Header (Spanish)</td>
  <td>Header text in Spanish</td>
  <td></td>
</tr>
<tr>
  <td><code>note_es</code></td>
  <td>Note (Spanish)</td>
  <td>Note text in Spanish</td>
  <td></td>
</tr>
<!-- IDENTIFIERS & LINKS -->
<tr>
  <td><code>unique_identifiers</code></td>
  <td>Identifier column(s)</td>
  <td style="word-wrap: break-word; white-space: normal;">Unique identifier column names for table or variable within table</td>
  <td style="text-align:center;"><i class="fa-solid fa-lock"></i></td>
</tr>
<tr>
  <td><code>url_table</code></td>
  <td>Documentation (table)</td>
  <td style="word-wrap: break-word; white-space: normal;">Link to documentation page</td>
  <td></td>
</tr>
<tr>
  <td><code>url_table_warn_use</code></td>
  <td>Responsible Use<br>Warning (table)</td>
  <td style="word-wrap: break-word; white-space: normal;"><a href="../resp_data_use/#warnings" target="_blank">Responsible use warning</a></td>
  <td></td>
</tr>
<tr>
  <td><code>url_warn_use</code></td>
  <td>Responsible Use<br>Warning (variable)</td>
  <td style="word-wrap: break-word; white-space: normal;"><a href="../resp_data_use/#warnings" target="_blank">Responsible use warning</a> specific to variable within a table</td>
  <td></td>
</tr>
<tr>
  <td><code>url_table_warn_data</code></td>
  <td>Data Warning (table)</td>
  <td style="word-wrap: break-word; white-space: normal;"><a href="../resp_data_use/#warnings" target="_blank">Data warning</a></td>
  <td></td>
</tr>
<tr>
  <td><code>url_warn_data</code></td>
  <td>Data Warning (variable)</td>
  <td style="word-wrap: break-word; white-space: normal;"><a href="../resp_data_use/#warnings" target="_blank">Data warning</a> specific to variable within a table</td>
  <td></td>
</tr>
<tr>
  <td><code>order_sort</code></td>
  <td>Sort order</td>
  <td style="word-wrap: break-word; white-space: normal;">Standard sort order in table/measure (and column order in database)</td>
  <td></td>
</tr>
</tbody>
</table>
<!-- LEGEND -->
<table id="legend" class="compact-table-no-vertical-lines" style="border: 2px solid #4fe2ffff; border-radius: 8px; border-collapse: collapse; line-height: 1.0;">
<tbody>
<tr>
<td><b>LEGEND</b></td>
<td style="text-align: center; padding-left: 30px"><i style="font-size: 1.2em;" class="fa-solid fa-lock"></i></td>
<td style="padding-left: 5px">Values do not vary across releases</td></tr>
<tr>
<td></td>
<td style="text-align: center; padding-left: 30px"><i style="font-size: 1.3em;" class="bi bi-filetype-json"></i></td>
<td style="padding-left: 5px">Table/variable element corresponds to field in BIDS JSON - see <a href="#json">Corresponding Data Dictionary Elements in JSONs</a></td></tr>
<tr>
<td></td><td style="text-align: center; padding-left: 30px"><i class="fas fa-exclamation-triangle" style="color:orange; font-size: 1.2em;"></i></td>
<td style="padding-left: 5px">CAUTION: Instruction text may be incomplete or misaligned! Review the <a href="../../changelog/knownissues/#instruction-metadata-read-carefully">known issue</a> before use.</td></tr>
</tbody>
</table>

<!-- JSON -->
<div id="json" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i style="font-size: 1.1em;" class="bi bi-filetype-json"></i></span>
  <span class="text-with-link">
  <span class="text">Corresponding Data Dictionary Elements in JSONs</span>
  <a class="anchor-link" href="#json" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines">
<thead>
  <tr><th>Data Dictionary Element</th><th>Corresponding Element in BIDS JSON</th>
  </tr>
</thead>
<tbody>
<tr><td><code>table_label</code></td><td><i>MeasurementToolMetadata > Description</i></td></tr>
<tr><td><code>label</code></td><td><i>Description</i></td></tr>
<tr><td><code>unit</code></td><td><i>Units</i></td></tr>
<tr><td><code>type_var</code></td><td><i>Derivative</i> set to <i>True</i> in JSON if <code>type_var</code> = <i>summary score</i> or <i>derived item</i></td></tr>
</tbody>
</table>
</div>

<!-- Type variable values -->
<div id="type_var" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i style="margin-right: 4px;" class="fa fa-book"></i></span>
  <span class="text-with-link">
  <span class="text">Variable Type (<code>type_var</code>): Possible Values Explained</span>
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
<td>administrative</td>
<td style="word-wrap: break-word; white-space: normal;">Data that gives context to the assessments, e.g. date, language, quality control, etc.</td>
</tr>
<tr>
<td>item</td><td style="word-wrap: break-word; white-space: normal;">Original data provided by the participant, e.g. questions in a questionnaire</td>
</tr>
<tr><td>derived item</td><td style="word-wrap: break-word; white-space: normal;">Derived from original data provided by the participant - e.g. if the participant filled in two fields to enter their height in feet and inches, a derived item could integrate this information into one field that provides the height in inches</td></tr>
<tr><td>summary score</td><td style="word-wrap: break-word; white-space: normal;">Summary and/or score output based on algorithmic conversions of items/raw data</td>
</tr>
</tbody>
</table>
</div>

### Levels Definitions

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th>Name</th>
        <th>JSON Element</th>
        <th>Description</th>
        <th>Example</th>
        <th style="width: 3%; text-align:center;"><a href="#legend">NOTE</a></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>name</code></td>
        <td>&nbsp;</td>
        <td style="word-wrap: break-word; white-space: normal;">Name of the categorical column/variable/question for which value/label pairs are reported</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-lock"></i></td>
      </tr>
      <tr>
        <td><code>value</code></td>
        <td>left hand side</td>
        <td>Value of the level</td>
        <td>1</td>
        <td style="text-align:center;"><i class="fa-solid fa-lock"></i></td>
      </tr>
      <tr>
        <td><code>order_level</code></td>
        <td></td>
        <td style="word-wrap: break-word; white-space: normal;">Order of response option (in data and how they were displayed to participants)</td>
        <td>2</td>
        <td style="text-align:center;"><i class="fa-solid fa-lock"></i></td>
      </tr>
      <tr>
        <td><code>label</code></td>
        <td>right hand side</td>
        <td>Label of the level</td>
        <td>Yes</td>
        <td></td>
      </tr>
      <tr>
        <td><code>label_es</code></td>
        <td></td>
        <td>Label of the level (Spanish)</td>
        <td>Si</td>
        <td></td>
      </tr>
</table>

<div id="add-columns" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Lasso User Warnings - Blank Columns & Additional Columns with Download</span>
  <a class="anchor-link" href="#add-columns" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p><b>Blank Columns in Lasso Query Tool</b><br>
<p>Column names appended with <b>*_es</b> are currently blank in the Lasso Dictionary Query Tool and will become available in a future release. Some columns in the data dictionary are not applicable to HBCD study data. These columns will appear in Lasso Portal queries, but will have blank values. Examples include <b>atlas</b>, <b>metric</b>, <b>sub_domain</b>, columns including <b>nda/deap/redcap</b>, etc. These columns can be safely ignored.</p>
<p><b>Additional Columns ('cohort' & 'site') Not Defined in Data Dictionary</b><br>
Dataset downloads contain 2 additional columns not described in the data dictionary. This includes <b>cohort</b> and <b>site</b>, identical to <a href="../../instruments/demo/visitinfo">Visit Information</a> variables <b>par_visit_data_&lt;<i>cohort|site</i>&gt;</b>.</p>
</div>


