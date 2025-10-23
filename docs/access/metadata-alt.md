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
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; padding: 4px; color: #00819bff; background-color: #ebf8fa57;"><b>CORE METADATA</b></td>
</tr>
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
  <td><code>source</code></td>
  <td>Source</td>
  <td style="word-wrap: break-word; white-space: normal;">Source of information. Source values include:<br>
  <i>Biological Mother | Caregiver (Responsible Adult) | Child | General</i></td>
</tr>
<!-- TABLE STRUCTURE -->
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; padding: 4px; color: #00819bff; background-color: #ebf8fa57;"><b>TABLE-LEVEL INFORMATION</b></td>
</tr>
<tr>
  <td><code>table_name</code><i class="fa-solid fa-lock" title="Does not vary across releases" style="font-size: 1em; margin-left: 6px; color: #727070ff;"></i>
  </td>
  <td>Table name</td>
  <td style="word-wrap: break-word; white-space: normal;">Coded table name, e.g. <code>sed_bm_demo</code></td>
</tr>
<tr>
  <td><code>table_label</code>
  <i class="bi bi-filetype-json" style="font-size: 1.2em; margin-left: 6px;"></i></td>
  <td>Table label</td>
  <td style="word-wrap: break-word; white-space: normal;">Label for coded table name (e.g. <i>Demographics</i>)</td>
</tr>
<!-- VARIABLE METADATA -->
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; padding: 4px; color: #00819bff; background-color: #ebf8fa57;"><b>VARIABLE-LEVEL INFORMATION</b></td>
</tr>
<tr>
  <td><code>name</code>
  <i class="fa-solid fa-lock" title="Does not vary across releases" style="font-size: 1em; margin-left: 6px; color: #727070ff;"></i></td>
  <td>Variable name</td>
  <td style="word-wrap: break-word; white-space: normal;">Coded variable name within a table (e.g. <code>sed_bm_demo_edu_001</code>)</td>
</tr>
<tr>
  <td><code>label</code>
  <i class="bi bi-filetype-json" style="font-size: 1.2em; margin-left: 6px;"></i></td>
  <td>Variable label</td>
  <td style="word-wrap: break-word; white-space: normal;">Label for coded variable name (e.g. <i>Highest grade completed</i>)</td>
</tr>
<tr>
  <td><code>instruction</code>
  <i class="fas fa-exclamation-triangle" style="font-size: 1em; margin-left: 6px; color: orange;"></i></td>
  <td>Instruction</td>
  <td style="word-wrap: break-word; white-space: normal;">Instructions preceding measure questions (e.g. <i>The next set of questions is about your child's behavior...</i>)<br>
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
  <td><code>unit</code>
  <i class="bi bi-filetype-json" style="font-size: 1.2em; margin-left: 6px;"></i></td>
  <td>Unit</td>
  <td style="word-wrap: break-word; white-space: normal;">Unit of measurement (e.g. <i>m, cm², lbs</i>)</td>
</tr>
<!-- VARIABLE TYPES -->
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; padding: 4px; color: #00819bff; background-color: #ebf8fa57;"><b>VARIABLE TYPE & FORMAT</b></td>
</tr>
<tr>
  <td><code>type_var</code>
  <i class="bi bi-filetype-json" style="font-size: 1.2em; margin-left: 6px;"></i></td>
  <td>Variable type</td>
  <td style="word-wrap: break-word; white-space: normal;">Variable types include: <i>administrative | item | derived item | summary score</i><br>
  See <a href="#type_var">Variable Type Definitions</a> below</td>
</tr>
<tr>
  <td><code>type_data</code>
  <i class="fa-solid fa-lock" style="font-size: 1em; margin-left: 6px; color: #727070ff;"></i></td>
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
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; padding: 4px; color: #00819bff; background-color: #ebf8fa57;"><b>DISPLAY PROPERTIES</b></td>
</tr>
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
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; padding: 4px; color: #00819bff; background-color: #ebf8fa57;"><b>IDENTIFIERS & LINKS TO DOCUMENTATION</b></td>
</tr>
<tr>
  <td><code>identifier_column</code>
  <i class="fa-solid fa-lock" style="font-size: 1em; margin-left: 6px; color: #727070ff;"></i></td>
  <td>Identifier column(s)</td>
  <td style="word-wrap: break-word; white-space: normal;">Unique identifier column names for table/variable, including participant and session IDs and sometimes run ID - see <a href="../../datacuration/phenotypes/#table-organization" target="_blank">Table Organization</a> for details</td>
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
