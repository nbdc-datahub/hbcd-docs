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
  <td><code>table_name</code>&nbsp; <i style="color: teal;" class="fa-solid fa-lock"></i></td>
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
  <td><code>name</code>&nbsp; <i style="color: teal;" class="fa-solid fa-lock"></i></td>
  <td>Variable name</td>
  <td style="word-wrap: break-word; white-space: normal;">Coded variable name within a table (e.g. <code>sed_bm_demo_edu_001</code>)</td>
</tr>
<tr>
  <td><code>label</code></td>
  <td>Variable label</td>
  <td style="word-wrap: break-word; white-space: normal;">Label for coded variable name (e.g. <i>Highest grade completed</i>)</td>
</tr>
<tr>
  <td><code>instruction</code>&nbsp; <i class="fas fa-exclamation-triangle" style="font-size: 1em; color: orange;"></i></td>
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
  <td><code>type_data</code>&nbsp; <i style="color: teal;" class="fa-solid fa-lock"></i></td>
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
  <td><code>identifier_column</code>&nbsp; <i style="color: teal;" class="fa-solid fa-lock"></i></td>
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
<td>administrative</td><td style="word-wrap: break-word; white-space: normal;">Data that gives context to the assessments, e.g. date, language, quality control, etc.</td>
</tr>
<tr><td>derived item</td><td style="word-wrap: break-word; white-space: normal;">Derived from original participant data (e.g., combining separate entries for feet and inches into a single derived height variable in inches) - see <a href="../../instruments/demo/basicdemo/" target="_blank">Basic Demographics</a> for more examples</td></tr>
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
</table>

<div id="site-levels" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Extraneous Recruitment Site Levels in Basic Demographics</span>
  <a class="anchor-link" href="#site-levels" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>In the Basic Demographics table (<code>sed_basic_demographics</code>), the variable <code>recruitment_site</code> includes three additional levels that do not represent study sites: <code>30=Sampled</code>; <code>31=USDTL</code>; <code>32=BAH</code>. These levels, used for internal purposes, appear only as possible values in the data dictionary, but are not used in the actual tabulated data. In other words, all participant records in the Basic Demographics table will have <code>recruitment_site</code> values ranging only from 0 to 29, corresponding to the study sites - see full list of recruitment sites <a href="#sites">below</a>.</p>
</div>

## Additional Information: Site & Cohort

Datasets downloaded from the NBDC Data Access Platform include two additional columns not described in the NBDC Data Dictionary: `cohort` and `site`, derived from the <a href="../../instruments/demo/visitinfo" target="_blank">Visit Information</a> variables `par_visit_data_cohort` and `par_visit_data_site`.

Click to expand the following section to see the global mapping between site IDs used to specify visit-specific site information in `site`/`par_visit_data_site` as well as recruitment sites included in <a href="../../instruments/demo/basicdemo/" target="_blank">Basic Demographics</a> (`sed_basic_demographics_recruitment_site`).

<div id="sites" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i style="font-size: 0.9em;" class="fa-solid fa-location-dot"></i></span>
  <span class="text-with-link">
  <span class="text">Site IDs</span>
  <a class="anchor-link" href="#sites" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width:100%;border-collapse:collapse;table-layout:fixed;">
<thead>
<tr style="border-bottom:2px solid #ccc;"><th>Basic Demographics Site Codes</th><th>Site ID</th><th>Site</th></tr>
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