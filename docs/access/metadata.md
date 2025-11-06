# NBDC Data Dictionary

<a href="../../datacuration/phenotypes/" target="_blank">Tabulated HBCD study data</a> is organized into a **standardized table format** per study instrument/measure, with each table containing a set of **variables** (see [Data Structure Overview](../datacuration/overview.md) for details). The metadata for studies released via the NBDC Data Hub consists of:

 - **Data dictionary**: Provides detailed information about table variables, including variable name, label, description, data type, etc. 
 - **Levels table**: Provides information about the levels for categorical variables (label, order, etc.)

See the following sections for detailed descriptions for each column in the [data dictionary](#data-dictionary-columns) and [levels table](#levels-table).

## Data Dictionary Columns
<p style="font-size: 0.9em; color: #696969ff; font-weight: bold;">
<i style="color: teal;" class="fa-solid fa-lock"></i>&nbsp;= Values do not vary across releases
</p>
<table class="compact-table" style="font-size: 14px; border: 1px solid #4fe2ffff; border-radius: 8px;">
<thead>
<tr>
  <th style="width: 20%;">NAME</th>
  <th style="width: 20%;">LABEL</th>
  <th>DESCRIPTION & POSSIBLE/EXAMPLE VALUES</th>
</tr>
</thead>
<tbody>
<!-- CORE METADATA -->
<tr>
  <td><code>study</code></td>
  <td>Study</td>
  <td style="word-wrap: break-word; white-space: normal;">Part of core (<code>Core</code>) or substudy (<code>Substudy</code>)</td>
</tr>
<tr>
  <td><code>domain</code></td>
  <td>Domain</td>
  <td style="word-wrap: break-word; white-space: normal;">Domains include:<br>
  <i>Behavior/Child-Caregiver Interaction | BioSpecimens | Neurocognition & Language | Novel Tech | Physical Health | Pregnancy/Exposure Including Substance | Social and Environmental Determinants | Tabular EEG | Tabular Imaging</i></td>
</tr>
<tr>
  <td><code>sub_domain</code></td>
  <td>Subdomain</td>
  <td style="word-wrap: break-word; white-space: normal;">Domain subcategory (e.g. <i>Structural MRI</i> within the <i>Imaging</i> domain)</td>
</tr>
<tr>
  <td><code>metric</code></td>
  <td>Metric</td>
  <td style="word-wrap: break-word; white-space: normal;">Imaging & EEG only: Specific metric assessed (e.g. <i>Cortical Thickness</i>)</td>
</tr>
<tr>
  <td><code>atlas</code></td>
  <td>Atlas</td>
  <td style="word-wrap: break-word; white-space: normal;">Imaging only: Atlas used to derive parcellated structural measures and functional timeseries (e.g., <i>Gordon</i> - <a href="../../instruments/mri/#parc" target="_blank">see full list</a>)</td>
</tr>
<tr>
  <td><code>source</code></td>
  <td>Source</td>
  <td style="word-wrap: break-word; white-space: normal;">Source of information. Source values include:<br>
  <i>Biological Mother | Caregiver (Responsible Adult) | Child | General</i></td>
</tr>
<!-- TABLE STRUCTURE -->
<tr>
  <td><i style="color: teal;" class="fa-solid fa-lock"></i>&nbsp; <code>table_name</code></td>
  <td>Table name</td>
  <td style="word-wrap: break-word; white-space: normal;">Coded table name, e.g. <code>sed_bm_demo</code></td>
</tr>
<tr>
  <td><code>table_label</code></td>
  <td>Table label</td>
  <td style="word-wrap: break-word; white-space: normal;">Label for coded table name (e.g. <i>Demographics</i>)</td>
</tr>
<!-- VARIABLE METADATA -->
<tr>
  <td><i style="color: teal;" class="fa-solid fa-lock"></i>&nbsp; <code>name</code></td>
  <td>Variable name</td>
  <td style="word-wrap: break-word; white-space: normal;">Coded variable name within a table (e.g. <code>sed_bm_demo_edu_001</code>)</td>
</tr>
<tr>
  <td><code>label</code></td>
  <td>Variable label</td>
  <td style="word-wrap: break-word; white-space: normal;">Label for coded variable name (e.g. <i>Highest grade completed</i>)</td>
</tr>
<tr>
  <td><i class="fas fa-exclamation-triangle" style="font-size: 1em; margin-left: 6px; color: orange;"></i>&nbsp; <code>instruction</code></td>
  <td>Instruction</td>
  <td style="word-wrap: break-word; white-space: normal;">
    Instructions preceding measure questions (e.g. <i>The next set of questions is about your child's behavior...</i>)<br>
  <i class="fas fa-exclamation-triangle" style="font-size: 1em; color: orange;"></i> <b>CAUTION: Instruction text may be incomplete or misaligned! See <a href="../../changelog/knownissues/#instruction-metadata-read-carefully">known issue</a></b></td>
</tr>
<tr>
  <td><code>header</code></td>
  <td>Header</td>
  <td style="word-wrap: break-word; white-space: normal;">Header/instructions for a set of questions (e.g. <i>For each item that describes your child...</i>)</td>
</tr>
<tr>
  <td><code>note</code></td>
  <td>Note</td>
  <td style="word-wrap: break-word; white-space: normal;">Note displayed to participants (e.g. <i>Enter weight in pounds.</i>)</td>
</tr>
<tr>
  <td><code>unit</code></td>
  <td>Unit</td>
  <td style="word-wrap: break-word; white-space: normal;">Unit of measurement (e.g. <i>m, cm², lbs</i>)</td>
</tr>
<!-- VARIABLE TYPES -->
<tr>
  <td><code>type_var</code></td>
  <td>Variable type</td>
  <td style="word-wrap: break-word; white-space: normal;">Variable types include: <i>administrative | item | derived item | summary score</i><br>
  See <a href="#type_var">Variable Type Definitions</a> below</td>
</tr>
<tr>
  <td><i style="color: teal;" class="fa-solid fa-lock"></i>&nbsp; <code>type_data</code></td>
  <td>Data type</td>
  <td style="word-wrap: break-word; white-space: normal;">Data types include: <i>date | timestamp| time | <span class="tooltip">character<span class="tooltiptext">Only used for categorical columns</span></span> | text | integer | double</i></td>
</tr>
<tr>
  <td><code>type_level</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Level of measurement</td>
  <td style="word-wrap: break-word; white-space: normal;">Levels include: <i>nominal | ordinal | interval | ratio</i></td>
</tr>
<tr>
  <td><code>type_field</code></td>
  <td>Field type</td>
  <td style="word-wrap: break-word; white-space: normal;">Field type in data capture system as presented to participant (e.g. <i>dropdown, radio, checkbox, etc.</i>)</td>
</tr>
<!-- DISPLAY PROPERTIES -->
<tr>
  <td><code>order_display</code></td>
  <td>Display order</td>
  <td style="word-wrap: break-word; white-space: normal;">Display order of item within measure</td>
</tr>
<tr>
  <td><code>branching_logic</code></td>
  <td>Branching logic</td>
  <td style="word-wrap: break-word; white-space: normal;">Branching logic applied to variable/question</td>
</tr>
<tr>
  <td><code>label_es</code></td>
  <td>Label (Spanish)</td>
  <td>Label in Spanish</td>
</tr>
<tr>
  <td><code>instruction_es</code></td>
  <td>Instruction (Spanish)</td>
  <td style="word-wrap: break-word; white-space: normal;">Instruction text in Spanish</td>
</tr>
<tr>
  <td><code>header_es</code></td>
  <td>Header (Spanish)</td>
  <td>Header text in Spanish</td>
</tr>
<tr>
  <td><code>note_es</code></td>
  <td>Note (Spanish)</td>
  <td>Note text in Spanish</td>
</tr>
<!-- IDENTIFIERS & LINKS -->
<tr>
  <td><i style="color: teal;" class="fa-solid fa-lock"></i>&nbsp; <code>identifier_column</code></td>
  <td>Identifier column(s)</td>
  <td style="word-wrap: break-word; white-space: normal;">Columns used for participant identification (i.e. participant & session ID) - see <a href="../../datacuration/phenotypes/#table-organization" target="_blank">Table Organization</a> for details</td>
</tr>
<tr>
  <td><code>url_table</code></td>
  <td>Documentation (table)</td>
  <td style="word-wrap: break-word; white-space: normal;">Link to documentation page</td>
</tr>
<tr>
  <td><code>url_table_warn_use</code></td>
  <td>Responsible Use<br>Warning (table)</td>
  <td style="word-wrap: break-word; white-space: normal;"><a href="../resp_data_use/#warnings" target="_blank">Responsible use warning</a></td>
</tr>
<tr>
  <td><code>url_warn_use</code></td>
  <td>Responsible Use<br>Warning (variable)</td>
  <td style="word-wrap: break-word; white-space: normal;"><a href="../resp_data_use/#warnings" target="_blank">Responsible use warning</a> specific to variable within a table</td>
</tr>
<tr>
  <td><code>url_table_warn_data</code></td>
  <td>Data Warning (table)</td>
  <td style="word-wrap: break-word; white-space: normal;"><a href="../resp_data_use/#warnings" target="_blank">Data warning</a></td>
</tr>
<tr>
  <td><code>url_warn_data</code></td>
  <td>Data Warning (variable)</td>
  <td style="word-wrap: break-word; white-space: normal;"><a href="../resp_data_use/#warnings" target="_blank">Data warning</a> specific to variable within a table</td>
</tr>
<tr>
  <td><code>order_sort</code></td>
  <td>Sort order</td>
  <td style="word-wrap: break-word; white-space: normal;">Standard sort order in table/measure (and column order in database)</td>
</tr>
</tbody>
</table>

#### Additional Information

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
<td>administrative</td>
<td style="word-wrap: break-word; white-space: normal;">Data that gives context to the assessments, e.g. date, language, quality control, etc.</td>
</tr>
<tr>
<td>derived item</td><td style="word-wrap: break-word; white-space: normal;">Derived from original participant data (e.g., combining separate entries for feet and inches into a single derived height variable in inches) - see <a href="../../instruments/demo/basicdemo/" target="_blank">Basic Demographics</a> for more examples</td>
<tr>
<td>item</td><td style="word-wrap: break-word; white-space: normal;">Original data provided by the participant, e.g. questions in a questionnaire</td>
</tr>
<tr><td>summary score</td><td style="word-wrap: break-word; white-space: normal;">Summary and/or score output based on algorithmic conversions of items/raw data</td>
</tr>
</tbody>
</table>
</div>

<!-- Lasso User warnings -->
<div id="add-columns" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">NBDC Data Access Platform User Warnings - Blank & Additional Columns with Download</span>
  <a class="anchor-link" href="#add-columns" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p><b>Blank Columns in NBDC Data Access Platform Query Tool</b><br>
Query Tool searches within the NBDC Data Access Platform currently display columns that are not applicable to HBCD study data, including columns ending with <code>nda</code>, <code>deap</code>, and <code>redcap</code>. Inapplicable columns will be removed in the future and can safely be ignored. Note that columns may also be blank if they have yet to be populated (currently the case for <b>sub_domain</b>, <b>atlas</b>, and <b>metric</b> for example). <b>For reference, only applicable columns are included in the Data Dictionary overview above.</b></p>
<p><b>Additional Columns ('cohort' & 'site') Not Defined in Data Dictionary</b><br>
Dataset downloads contain 2 additional columns not described in the data dictionary. This includes <b>cohort</b> and <b>site</b>, identical to <a href="../../instruments/demo/visitinfo">Visit Information</a> variables <b>par_visit_data_&lt;<i>cohort|site</i>&gt;</b>.</p>
</div>

## Levels Table
<p style="font-size: 0.9em; color: #696969ff; font-weight: bold;">
<i style="color: teal;" class="fa-solid fa-lock"></i>&nbsp;= Values do not vary across releases
</p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px; border: 1px solid #4fe2ffff; border-radius: 8px;">
<thead>
  <tr>
    <th style="width: 20%;">Name</th>
    <th style="width: 10%;">JSON Element</th>
    <th style="width: 70%;">Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><i style="color: teal;" class="fa-solid fa-lock"></i>&nbsp; <code>name</code></td>
    <td>&nbsp;</td>
    <td>Name of the categorical column/variable/question for which value/label pairs are reported</td>
  </tr>
  <tr>
    <td><i style="color: teal;" class="fa-solid fa-lock"></i>&nbsp; <code>value</code></td>
    <td>left hand side</td>
    <td>Value of the level (<b>e.g. "1"</b>)</td>
  </tr>
  <tr>
    <td><i style="color: teal;" class="fa-solid fa-lock"></i>&nbsp; <code>order_level</code></td>
    <td></td>
    <td>Order of response option as displayed to participants (and in data) (<b>e.g. "2"</b>)</td>
  </tr>
  <tr>
    <td><code>label</code></td>
    <td>right hand side</td>
    <td>Label of the level (<b>e.g. "Yes"</b>)</td>
  </tr>
  <tr>
    <td><code>label_es</code></td>
    <td></td>
    <td>Label of the level (Spanish) (<b>e.g. "Si"</b>)</td>
  </tr>
</table>

<br>


