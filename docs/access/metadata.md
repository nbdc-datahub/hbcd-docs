# Metadata & Naming Conventions

## NBDC Data Dictionary

<span class="tooltip">Tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> HBCD data is organized into a standardized table format, each of which contains a set of variables. The metadata for studies released via the NBDC Data Hub consists of:

 - **Data dictionary**: Provides detailed information about the variables in the tabulated data resource, including the variable name, label, description, data type, and other relevant information. 
 - **Levels table**: Provides information about the levels of categorical variables in the tabulated format data (label, order, etc.)

Below are the definitions for the columns in the data dictionary and levels table. Note that some columns also correspond to elements in the BIDS JSON files that accompany all <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> data (hover over <i class="bi bi-filetype-json" style="font-size:18px; color: teal;"></i> icon for details in table below).

<p>
<div class="table-banner" style="background-color: #dde6fe;">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
<span class="text"> See <a href="../../datacuration/overview/" target="_blank">here</a> for overview of tabulated vs file-based data.</span>
</div>
</p>

### Data Dictionary & Levels Column Definitions

<p>
<div id="metadata" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">CAUTION: Instruction text may be incomplete or misaligned! Review the <a href="../../changelog/knownissues/#instruction-metadata-caution-please-read-carefully">known issue</a> before use.
 </span>
</div>
</p>

<div id="nbdc-dd" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-book"></i></span>
  <span class="text-with-link">
  <span class="text">Data Dictionary Column Definitions</span>
  <a class="anchor-link" href="#nbdc-dd" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th style="width: 5%;">Name</th>
        <th style="width: 20%;">Label</th>
        <th style="width: 25%;">Description</th>
        <th style="width: 30%;"><b>{ </b>Possible Values<b> }</b> / Example(s)</th>
        <th style="width: 5%;"><span class="tooltip tooltip-left">Mutable<span class="tooltiptext">Values may vary across releases</span></span></th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td><code>study</code></td>
        <td>Study</td>
        <td style="word-wrap: break-word; white-space: normal;">Indicates whether table/measure is a core components of the study or belongs to a substudy / anxiliary study</td>
        <td><b>{</b> Core; Substudy <b>}</b></td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>domain</code></td>
        <td>Domain</td>
        <td>Domain/<a href="https://hbcdstudy.org/workgroups-and-committees/">HBCD Workgroup</a></td>
        <td style="word-wrap: break-word; white-space: normal;">
        <b>{</b> Behavior/Child-Caregiver Interaction;<br>Biospecimens;<br>Demographics;<br>Neurocognition & Language;<br>Novel Tech;<br>Physical Health;<br>Pregnancy/Exposure Including Substance;<br>Social & Environmental Determinants;<br>Tabular EEG;<br>Tabular imaging <b>}</b>
        </td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>source</code></td>
        <td>Source</td>
        <td style="word-wrap: break-word; white-space: normal;">Source of information for this table/measure</td>
        <td style="word-wrap: break-word; white-space: normal;"><b>{</b> Biological Mother;<br>Caregiver (Responsible Adult);<br>Child;<br>General <b>}</b></td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>table_name</code></td>
        <td>Table name</td>
        <td>Name of table/measure</td>
        <td><code>mh_p_cbcl</code></td>
        <td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
    </tr>
    <tr>
        <td><code>table_label</code>&nbsp;
            <span class="tooltip tooltip-right"><i class="bi bi-filetype-json" style="font-size:18px;"></i>
            <span class="tooltiptext">Corresponds to <i>MeasurementToolMetadata</i> > <i>Description</i> in BIDS JSON</span></span>
        </td>
        <td>Table label</td>
        <td style="word-wrap: break-word; white-space: normal;">Label for table/measure</td>
        <td style="word-wrap: break-word; white-space: normal;">Child Behavior Checklist [Parent]</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>name</code></td>
        <td>Variable name</td>
        <td style="word-wrap: break-word; white-space: normal;">Name of column/variable/question</td>
        <td><code>mh_p_cbcl__aggr_001</code></td>
        <td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;"><code>label</code>&nbsp;
          <span class="tooltip tooltip-right"><i class="bi bi-filetype-json" style="font-size:18px;"></i>
          <span class="tooltiptext">Corresponds to <i>Description</i> in BIDS JSON</span></span>
        </td>
        <td>Variable label</td>
        <td style="word-wrap: break-word; white-space: normal;">Label for column/variable/question</td>
        <td style="word-wrap: break-word; white-space: normal;">"Demands a lot of attention"</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>instruction</code></td>
        <td>Instruction</td>
        <td style="word-wrap: break-word; white-space: normal;">Instructions preceding table/measure questions</td>
        <td style="word-wrap: break-word; white-space: normal;">"The next set of questions is about your child's behavior in different situations and contexts. Please fill in a response to all questions."</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>header</code></td>
        <td>Header</td>
        <td style="word-wrap: break-word; white-space: normal;">Header/instructions for a set of questions</td>
        <td style="word-wrap: break-word; white-space: normal;">"Below is a list of items that describe children and youths. For each item that describes your child <span class="tooltip"><strong>...</strong>
        <span class="tooltiptext">... now or within the past 6 months, please choose whether the item is very true or often true of your child, somewhat or sometimes true of your child, or not true of your child. Please answer all items as well as you can, even if some do not seem to apply to your child."</span>
      </span>
     </td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>note</code></td>
        <td>Note</td>
        <td style="word-wrap: break-word; white-space: normal;">Note displayed to participants</td>
        <td style="word-wrap: break-word; white-space: normal;">"Enter weight in pounds."</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;"><code>unit</code>&nbsp;
          <span class="tooltip tooltip-right"><i class="bi bi-filetype-json" style="font-size:18px;"></i>
          <span class="tooltiptext">Corresponds to <i>Units</i> in BIDS JSON</span></span>
        </td>
        <td>Unit</td>
        <td style="word-wrap: break-word; white-space: normal;">Unit of measurement</td>
        <td style="word-wrap: break-word; white-space: normal;">m, cm2, lbs</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>type_var</code>&nbsp;
          <span class="tooltip tooltip-right"><i class="bi bi-filetype-json" style="font-size:18px;"></i>
          <span class="tooltiptext">Derivative element in BIDS JSON set to <i>true</i> if <i>type_var</i> = <i>summary score</i> or <i>derived item</i></span></span>
        </td>
        <td>Variable type</td>
        <td style="word-wrap: break-word; white-space: normal;">Type of column/variable/question</td>
        <td style="word-wrap: break-word; white-space: normal;"><b>{</b>
            <span class="tooltip">administrative
            <span class="tooltiptext">Data that gives context to the assessments, e.g. date of assessment, language, quality control, etc.</span>
          </span>;
          <span class="tooltip">item
            <span class="tooltiptext">Original data provided by the participant, e.g. questions in a questionnaire</span>
          </span>; 
          <span class="tooltip">derived item
            <span class="tooltiptext">Derived from original data provided by the participant - e.g. if the participant filled in two fields to enter their height in feet and inches, a derived item could integrate this information into one field that provides the height in inches</span>
          </span>; <span class="tooltip">summary score
            <span class="tooltiptext">Summary and/or score output based on algorithmic conversions of items/raw data</span>
          </span><b> }</b>
      </td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>type_data</code></td>
        <td>Data type</td>
        <td style="word-wrap: break-word; white-space: normal;">Data type (in database)</td>
        <td style="word-wrap: break-word; white-space: normal;"><b>{</b> date; timestamp; time;
      <span class="tooltip">character
        <span class="tooltiptext">Character only used for categorical columns</span>
      </span>;
      text; integer; double <b>}</b></td>
    </td>
        <td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
    </tr>
    <tr>
        <td><code>type_level</code></td>
        <td style="word-wrap: break-word; white-space: normal;">Level of measurement</td>
        <td style="word-wrap: break-word; white-space: normal;">Measurement level/scale type</td>
        <td style="word-wrap: break-word; white-space: normal;"><b>{</b> nominal; ordinal; interval; ratio <b>}</b></td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>type_field</code></td>
        <td>Field type</td>
        <td style="word-wrap: break-word; white-space: normal;">Field type in data capture system as presented to participant</td>
        <td style="word-wrap: break-word; white-space: normal;">dropdown; radio; checkbox</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>order_display</code></td>
        <td>Display order</td>
        <td style="word-wrap: break-word; white-space: normal;">Display order of item within measure</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>branching_logic</code></td>
        <td>Branching logic</td>
        <td style="word-wrap: break-word; white-space: normal;">Branching logic applied to column/variable/question</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>    
    </tr>
    <tr>
        <td><code>label_es</code></td>
        <td>Label (Spanish)</td>
        <td>Label (Spanish)</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>instruction_es</code></td>
        <td>Instruction (Spanish)</td>
        <td>Instruction (Spanish)</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>header_es</code></td>
        <td>Header (Spanish)</td>
        <td>Header (Spanish)</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>note_es</code></td>
        <td>Note (Spanish)</td>
        <td>Note (Spanish)</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>unique_identifiers</code></td>
        <td>Identifier column(s)</td>
        <td style="word-wrap: break-word; white-space: normal;">Unique identifier column names (variable/table)</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
    </tr>
    <tr>
        <td><code>url_table</code></td>
        <td style="word-wrap: break-word; white-space: normal;">Documentation for table</td>
        <td style="word-wrap: break-word; white-space: normal;">Link to <a href="../../instruments" target="_blank">study instrument documentation</a></td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>url_table_warn_use</code></td>
        <td style="word-wrap: break-word; white-space: normal;">Responsible Use Warning (table)</td>
        <td style="word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">responsible use warning</a> (table)</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>url_table_warn_data</code></td>
        <td>Data Warning (table)</td>
        <td style="word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">data warning</a> (table)</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>url_warn_use</code></td>
        <td style="word-wrap: break-word; white-space: normal;">Responsible Use Warning (variable)</td>
        <td style="word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">responsible use warning</a> (variable)</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>url_warn_data</code></td>
        <td style="word-wrap: break-word; white-space: normal;">Data Warning (variable)</td>
        <td style="word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">data warning</a> (variable)</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
        <td><code>order_sort</code></td>
        <td>Sort order</td>
        <td style="word-wrap: break-word; white-space: normal;">Standard sort order in table/measure (and ⇒ column order in data/database)</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
</tbody>
</table>
</div>

<div id="levels" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-book"></i></span>
  <span class="text-with-link">
  <span class="text">Levels Definitions</span>
  <a class="anchor-link" href="#levels" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th>Name</th>
        <th>JSON Element</th>
        <th>Description</th>
        <th>Example</th>
        <th><span class="tooltip tooltip-left">Mutable<span class="tooltiptext">Values may vary across releases</span></span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>name</code></td>
        <td>&nbsp;</td>
        <td style="word-wrap: break-word; white-space: normal;">Name of the categorical column/variable/question for which value/label pairs are reported</td>
        <td>&nbsp;</td>
        <td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
      </tr>
      <tr>
        <td><code>value</code></td>
        <td>left hand side</td>
        <td>Value of the level</td>
        <td>1</td>
        <td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
      </tr>
      <tr>
        <td><code>order_level</code></td>
        <td></td>
        <td style="word-wrap: break-word; white-space: normal;">Order of response option (in data and how they were displayed to participants)</td>
        <td>2</td>
        <td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
      </tr>
      <tr>
        <td><code>label</code></td>
        <td>right hand side</td>
        <td>Label of the level</td>
        <td>Yes</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      </tr>
      <tr>
        <td><code>label_es</code></td>
        <td></td>
        <td>Label of the level (Spanish)</td>
        <td>Si</td>
        <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      </tr>
</table>
</div>

### Lasso User Warnings - HBCD

<div id="add-columns" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Additional Columns ('cohort' & 'site') Not Defined in Data Dictionary</span>
  <a class="anchor-link" href="#add-columns" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<ul>
<p>Dataset downloads contain 2 additional columns not described in the data dictionary. This includes <b>cohort</b> and <b>site</b>, identical to <a href="../../instruments/demo/visitinfo">Visit Information</a> variables <b>par_visit_data_&lt;<i>cohort|site</i>&gt;</b>.</p>
</div>

<div id="blank-columns" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Blank Columns in Lasso Query Tool</span>
  <a class="anchor-link" href="#blank-columns" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Column names appended with <b>*_es</b> are currently blank in the Lasso Dictionary Query Tool and will become available in a future release. Some columns in the data dictionary are not applicable to HBCD study data. These columns will appear in Lasso Portal queries, but will have blank values. Examples include <b>atlas</b>, <b>metric</b>, <b>sub_domain</b>, columns including <b>nda/deap/redcap</b>, etc. These columns can be safely ignored.</p>
</div>

## Naming Conventions

A standardized naming convention is used across most tables and fields in the <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> release data. These conventions are adapted from the [ABCD Study](https://docs.abcdstudy.org/latest/documentation/curation/naming.html) and ensure consistency across instruments and derived datasets, allowing for intuitive parsing of variable meaning and structure.

### Convention Logic & Rules

The standard variable naming format is comprised of 4 or 5 main components: 

 <p style="font-size: 1.8em; font-weight: bold; padding: 10px;" align="center">
<code>domain_source_table_<span style="color: teal;">{scale}</span>_item</code>
</p>

 - **Main components** are generally separated by a single underscore ( `_` ). Most instruments with multiple scales will additionally include the <code><span style="color: teal;">scale</span></code> component (this component is otherwise optional and not included in all variable names).   
 - **Subcomponents** are separated by double ( `__` ) underscores to indicate nested components of `table`, <code><span style="color: teal;">scale</span></code>, and/or `item`. Subcomponents distinguish finer details such as *subscales*, *versions*, or *counter types*. Multiselect fields are preceded by triple underscores ( `___` ), mainly relevant for [V01 Demographics](../instruments/SED/v01-demo.md) (`sed_bm_demo`) variables.
 
### Naming Component Definitions

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <th style="width: 10%;">Component</th>
  <th style="width: 45%;">Definition</th>
  <th style="width: 35%;">Example Values</th>
</thead>
<tbody>
<tr>
  <td><b><code>domain</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;">Data domain (e.g. biospecimens, imaging)</td>
  <td><span class="tooltip"><code>bio</code><span class="tooltiptext">Biospecimens</span></span>;
  <span class="tooltip"><code>img</code><span class="tooltiptext">Imaging/MRI</span></span>;
  <span class="tooltip"><code>sed</code><span class="tooltiptext">Social & Environmental Determinants</span></span>;
  <span class="tooltip"><code>pex</code><span class="tooltiptext">Pregnancy & Exposures, Including Substance Use</span></span>;
  <i><a href="#domain-source-values">see full list</a></i></td>
</tr>
<tr>
  <td><b><code>source</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;"><span class="tooltip">Subject<span class="tooltiptext">who the protocol element is about</span></span>/<span class="tooltip">respondent<span class="tooltiptext">who completed the assessment</span></span> (e.g., child, birth parent)</td>
  <td><span class="tooltip"><code>bm</code><span class="tooltiptext">Biological Mother</span></span>;
    <span class="tooltip"><code>ch</code><span class="tooltiptext">Child</span></span>; <i><a href="#domain-source-values">see full list</a></i>
  </td>
</tr>
<tr>
<td><b><code>table</code></b></td>
<td>Instrument/protocol element name</td>
<td>Varies by instrument</td></tr>
</tr>
<tr>
<td><b><code><span style="color: teal;">{scale}</span></code></b></td>
<td style="word-wrap: break-word; white-space: normal;">Name of scale within instrument/protocol element - <i>only if instrument contains multiple scales</i></td>
<td style="word-wrap: break-word; white-space: normal;">Varies by instrument - <i><a href="#scale">see details</a></i></td></tr>
</tr>
<tr>
  <td><b><code>item</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;">Will either be an item number corresponding to individual questions in a scale <b>or</b> admin field/score label for administrative/summary score variables - <a href="#exceptions-admin"><i>see details</i></a></td>
  <td style="word-wrap: break-word; white-space: normal;"><code>001</code>; <code>001__01</code>; etc.<br>
    <b>or</b> <a href="#exceptions-admin">admin field/score label</a>
</tr>
</tbody>
</table>

#### Details<span class="hint">(Click sections to expand)</span>

<div id="domain-source-values" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Domain & Source: Possible Values</span>
  <a class="anchor-link" href="#domain-source-values" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<div style="display: flex; gap: 30px; align-items: flex-start;">
  <table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <caption style="caption-side: top; font-weight: bold; padding-bottom: 8px;">
    Possible Values:  <code>domain</code>
    </caption>
    <tbody>
      <tr><td><code>bio</code></td><td>BioSpecimens</td></tr>
      <tr><td><code>eeg</code></td><td>Tabular EEG</td></tr>
      <tr><td><code>mh</code></td><td>Behavior/Child-Caregiver Interaction</td></tr>
      <tr><td><code>img</code></td><td>Tabular Imaging</td></tr>
      <tr><td><code>ncl</code></td><td>Neurocognition and Language</td></tr>
      <tr><td><code>nt</code></td><td>Novel Tech (<i>Novel Technology & Wearable Sensors</i>)</td></tr>
      <tr><td><code>pex</code></td><td>Pregnancy/Exposure Including Substance</td></tr>
      <tr><td><code>ph</code></td><td>Physical Health</td></tr>
      <tr><td><code>sed</code></td><td>Social and Environmental Determinants</td></tr>
    </tbody>
  </table>
  <table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <caption style="caption-side: top; font-weight: bold; padding-bottom: 8px;">
    Possible Values:  <code>source</code>
    </caption>
    <tbody>
      <tr><td><code>bm</code></td><td>Biological Mother</td></tr>
      <tr><td><code>cg</code></td><td>Caregiver (Responsible Adult)</td></tr>
      <tr><td><code>ch</code></td><td>Child</td></tr>
      <tr><td><code>ld</code></td><td>Linked Data</td></tr>
      <tr><td><code>ra</code></td><td>RA (research assistant)</td></tr>
    </tbody>
  </table>
</div>
</div>

<div id="scale" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Scale Details</span>
  <a class="anchor-link" href="#scale" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Most variables of instruments/tables composed of multiple scales include an additional naming component for <code><span style="color: teal;">scale</span></code> (with the exception of administrative/summary score variables - <a href="#exceptions-admin"><i>see details</i></a>). The following instruments in the current release are examples of tables that include the scale component in their variable names. Note that this is not a comprehensive list.</p>
<br>
<br>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th>Domain</th>
      <th>Instrument</th>
      <th>Table Name</th>
      <th>Example Variable</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="tooltip tooltip-right">BCGI<span class="tooltiptext">Behavior & Child-Caregiver Interaction</span></span></td>
      <td><a href="../../instruments/bcgi/ibqr" target="_blank">IBQ-R (VSF)+BI</a></td>
      <td><code>mh_cg_ibqr</code></td>
      <td><code>mh_cg_ibqr_<span style="color: teal;">beh</span>_001</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right">PEX<span class="tooltiptext">Pregnancy & Exposure, Including Substance Use</span></span></td>
      <td><a href="../../instruments/pregexp/mh/fam-mh" target="_blank">FAM MH</a></td>
      <td><code>pex_bm_psych</code></td>
      <td><code>pex_bm_psych_<span style="color: teal;">bf</span>_001</code></td>
    </tr>
    <tr>
      <td rowspan="2"><span class="tooltip tooltip-right">SED<span class="tooltiptext">Social & Environmental Determinants</span></span></td>
      <td><a href="../../instruments/SED/bfy" target="_blank">BFY</a></td>
      <td><code>sed_bm_bfy</code></td>
      <td><code>sed_bm_bfy_<span style="color: teal;">econstr</span>_001</code></td>
    </tr>
     <tr>
      <td><a href="../../instruments/SED/promis" target="_blank">PROMIS</a></td>
      <td><code>sed_bm_strsup</code></td>
      <td><code>sed_bm_strsup_<span style="color: teal;">socspprt</span>_001</code></td>
    </tr>
  </tbody>
</table>
</div>

### Exceptions<span class="hint">(Click sections to expand)</span>

Some variables do not fully follow the standard naming convention, which will be improved in future releases. Notable exceptions are as follows (*click to expand*):

<div id="exceptions-admin" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Administrative & Summary Score Variables</span>
  <a class="anchor-link" href="#exceptions-admin" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Administrative (e.g., language or date of administration) and summary score (e.g., sums or means of individual items in a table) variables include <strong>administrative fields</strong> and <strong>score labels</strong> in place of <code>item</code> (or <code><span style="color: teal;">{scale}</span>_item</code> where relevant). Admin and score labels often include single underscores, but represent single main components. For example, possible values include:</p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
  <td><b>Admin fields</b></td>
  <td  style="word-wrap: break-word; white-space: normal;"><code>administration</code>; <code>location</code>; <code>lang</code>; <code>date_taken</code>; <code>candidate_age</code>; <code>gestational_age</code>; <code>adjusted_age</code></td>
</tr>
<tr>
  <td><b>Score labels</b></td>
  <td><code>score</code>; <code>summary_score</code>; <code>total_score</code>; etc.</td>
</tr>
</tbody>
</table>
</div>

<div id="exceptions-derived" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Derived Variables</span>
  <a class="anchor-link" href="#exceptions-derived" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Derived tables, including Basic Demographics (<code>sed_basic_demographics</code>), containing global, static variables, and Visit Information (<code>par_visit_data</code>), containing dynamic/longitudinal visit-level data, do not follow the naming conventions outlined above. For example, both fall under the domain <code>Demographics</code> and source <code>General</code> in the <a href="#nbdc-data-dictionary">NBDC Data Dictionary</a>, but use <code>sed_basic</code> (in reference to Social &amp; Environmental Determinants from which the Basic Demographics information is derived) and <code>par_visit</code> (for participant information from visit-level data) in place of the <code>domain_source</code> naming components. </p>
</div>

<div id="exceptions-biospec" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Biospecimens</span>
  <a class="anchor-link" href="#exceptions-biospec" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Biospecimen names are largely descriptive, e.g. <code>bio_bm_biosample_nails_results</code> and <code>bio_bm_biosample_urine</code> table names.</p>
</div>

<div id="exceptions-mri" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Tabulated MRI, MRS, & EEG Data</span>
  <a class="anchor-link" href="#exceptions-mri" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Tabulated data derived from <a href="../../instruments/#mri" target="_blank">MRI & MRS</a> and <a href="../../instruments/#eeg" target="_blank">EEG</a> file-based data follow a unique naming convention. All files begin with the <strong>domain</strong> (<code>img</code> or <code>eeg</code>) in accordance with the conventions described above, but the following elements are the pipeline name (<code>pipeline</code>) and basename of the derivative output by that pipeline (<code>derivative</code>):</p> 
<p style="font-size: 1.4em; font-weight: bold; padding: 10px;" align="center">
<code>domain_pipeline_derivative</code>
</p>
<p>For example, the following subject/session-level <a href="../../instruments/mri/fmri/#xcpd" target="_blank">XCP-D derivatives</a> are combined into a single tabulated file:</p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<tr>
<td><b>File-based derivatives</b></td>
<td><code>sub-{ID}_ses-{V0X}_task-rest_dir-PA_run-{X}<span style="color: teal;">_space-fsLR_seg_Gordon_stat-alff_bold</span>.tsv</code> </td>
</tr>
<tbody>
<tr>
<td><b>Tabulated file</b></td>
<td><code>img_xcpd<span style="color: teal;">_space-fsLR_seg_Gordon_stat-alff_bold</span>.tsv</code></td>
</tbody>
</table>
</ul>
</div>

### Example

Let's break down the following example: `ncl_cg_spm2__inf_soc_001`

- `ncl`: [Neurocognition & Language](../instruments/index.md#neurocog) (*domain*)
- `cg`: Caregiver (*source*)
- `spm2__inf`: nested table name
    - `spm2`: the [SPM-2](../instruments/neurocog/spm2.md) instrument (*table*)
    - `inf`: Infant version of SPM-2 (*table subcomponent*)
- `soc`: scale for metrics of socialization (*scale*)
- `001`: item number (*item*)


## Study Design Logic: Child-Centric Data Structure

The HBCD Study organizes data around the Child ID as the central key. All caregiver-provided data (e.g., from biological mothers or other caregivers) is nested under the corresponding Child ID. This structure supports the study’s goal of enabling longitudinal analyses of child development by:

- **Simplifying child-focused analysis**: Researchers can track each child’s data over time without remapping caregiver information.
- **Handling multi-birth cases cleanly**: When a caregiver reports on multiple children (e.g., twins), each child’s data remains distinct, avoiding complex joins or disambiguation.
