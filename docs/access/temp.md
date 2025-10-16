variables refer to fields, column headers within tables

add separate section/table showing correspondance to JSON metadata

add separate section explaining type_var

Possible values include: 

administrative: Data that gives context to the assessments, e.g. date of assessment, language, quality control, etc.

item - Original data provided by the participant, e.g. questions in a questionnaire

derived item - Derived from original data provided by the participant - e.g. if the participant filled in two fields to enter their height in feet and inches, a derived item could integrate this information into one field that provides the height in inches

summary score> - ummary and/or score output based on algorithmic conversions of items/raw data


Derivative element in BIDS JSON set to <i>true</i> if <i>type_var</i> = <i>summary score</i> or <i>derived item</i>


<!-- LEGEND -->
<div class="table-legend">
  <p><strong>Legend:</strong></p>
  <ul>
    <li><i class="fa-solid fa-lock"></i> Values do not vary across releases</li>
    <li><i class="bi bi-filetype-json"></i> Defined or corresponds to field in BIDS JSON</li>
    <li><i class="fas fa-exclamation-triangle" style="color:orange;"></i> Known issue — see <a href="../../changelog/knownissues/#instruction-metadata-read-carefully">details</a></li>
  </ul>
</div>



<table class="compact-table" style="font-size: 14px;">
<thead>
<tr>
  <th style="width: 15%;">Name</th>
  <th style="width: 20%;">Label</th>
  <th>Description & Possible/Example Values</th>
  <th style="width: 3%; text-align:center;">Note</th>
</tr>
</thead>
<tbody>
<!-- CORE METADATA -->
<tr>
  <td><code>study</code></td>
  <td>Study</td>
  <td style="word-wrap: break-word; white-space: normal;">Part of core (<code>Core</code>) or substudy (<code>Substudy</code>).</td>
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
  <td style="text-align:center;"><i class="fa-solid fa-lock"></i></td>
</tr>
<tr>
  <td><code>table_label</code></td>
  <td>Table label</td>
  <td style="word-wrap: break-word; white-space: normal;">Label for coded table name, e.g. <i>Demographics</i></td>
  <td style="text-align:center;"><i class="bi bi-filetype-json"></i></td>
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
  <td style="text-align:center;"><i class="bi bi-filetype-json"></i></td>
</tr>
<tr>
  <td><code>instruction</code></td>
  <td>Instruction</td>
  <td style="word-wrap: break-word; white-space: normal;">Instructions preceding measure questions (e.g. <i>The next set of questions is about your child's behavior...</i>)</td>
  <td style="text-align:center;"><i class="fas fa-exclamation-triangle" style="color:orange;"></i></td>
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
  <td style="text-align:center;"><i class="bi bi-filetype-json"></i></td>
</tr>

<!-- VARIABLE TYPES -->
<tr>
  <td><code>type_var</code></td>
  <td>Variable type</td>
  <td style="word-wrap: break-word; white-space: normal;">Possible values include: <i>administrative</i>; <i>item</i>; <i>derived item</i>; <i>summary score</i> - <a href="">see details</a></td>
  <td style="text-align:center;"><i class="bi bi-filetype-json"></i></td>
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
  <td>Responsible Use Warning (table)</td>
  <td style="word-wrap: break-word; white-space: normal;"><a href="../resp_data_use/#warnings" target="_blank">Responsible use warning</a></td>
  <td></td>
</tr>
<tr>
  <td><code>url_warn_use</code></td>
  <td>Responsible Use Warning (variable)</td>
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


