


<table class="compact-table">
<thead>
<tr>
<th>Name</th>
<th>Label</th>
<th>Description & Possible/Example Values</th>
<th style="width: 1%;"><span class="tooltip tooltip-left">Note<span class="tooltiptext">Hover over icon to see more info</span></span></th>
</tr>
</thead>
<tbody>
<tr>
    <td><code>study</code></td>
    <td>Study</td>
    <td style="word-wrap: break-word; white-space: normal;">Part of core (<code>Core</code>) or substudy (<code>Substudy</code>)</td>
    <td></td>
</tr>
<tr>
    <td><code>domain</code></td>
    <td>Domain</td>
    <td style="word-wrap: break-word; white-space: normal;">Domain/<a href="https://hbcdstudy.org/workgroups-and-committees/">HBCD Workgroup</a> (e.g <i>Demographics; Behavior/Child-Caregiver Interaction; Biospecimens; Tabular imaging, etc.</i>)
    </td>
    <td></td>
</tr>
<tr>
    <td><code>source</code></td>
    <td>Source</td>
    <td style="word-wrap: break-word; white-space: normal;">Source of information.<br>
    Includes: {<i>Biological Mother; Caregiver (Responsible Adult); Child; General</i>}</td>
    <td></td>
</tr>
<tr>
    <td><code>table_name</code></td>
    <td>Table name</td>
    <td>Name of table/measure (e.g. <code>sed_bm_demo</code>)</td>
    <td style="text-align: center;"><span class="tooltip tooltip-left"><i class="fa-solid fa-lock"></i><span class="tooltiptext">Values do not vary across releases</span></span></td>
</tr>
<tr>
    <td><code>table_label</code></td>
    <td>Table label</td>
    <td style="word-wrap: break-word; white-space: normal;">Label for table (e.g. <i>Demographics</i> for table <code>sed_bm_demo</code>)</td>
    <td style="text-align: center;"><span class="tooltip tooltip-left"><i class="bi bi-filetype-json" style="font-size:17px;"></i><span class="tooltiptext">Corresponds to <i>MeasurementToolMetadata</i> > <i>Description</i> in BIDS JSON</span></span></td>
</tr>
<tr>
    <td><code>name</code></td>
    <td>Variable name</td>
    <td style="word-wrap: break-word; white-space: normal;">Name of column/variable/question (e.g. <code>sed_bm_demo_edu_001</code>)</td>
    <td style="text-align: center;"><span class="tooltip tooltip-left"><i class="fa-solid fa-lock"></i><span class="tooltiptext">Values do not vary across releases</span></span></td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;"><code>label</code></td>
    <td>Variable label</td>
    <td style="word-wrap: break-word; white-space: normal;">Label for column/variable/question (e.g. <i>What is the highest grade or level of school you have completed or the highest degree you have received?</i>)</td>
    <td style="text-align: center;"><span class="tooltip tooltip-left"><i class="bi bi-filetype-json" style="font-size:17px;"></i>
    <span class="tooltiptext">Corresponds to <i>Description</i> in BIDS JSON</span></span></td>
</tr>
<tr>
    <td><code>instruction</code></td>
    <td>Instruction</td>
    <td style="word-wrap: break-word; white-space: normal;">Instructions preceding table/measure questions (e.g. <i>The next set of questions is about your child's behavior in different situations and contexts. Please fill in a response to all questions.</i>)</td>
    <td style="text-align: center;"><span class="tooltip tooltip-left"><i style="color: orange; font-size: 1.2em;" class="fas fa-exclamation-triangle"></i><span class="tooltiptext">See <a href="../../changelog/knownissues/#instruction-metadata-read-carefully">known issue</a></span></span></td>
</tr>
<tr>
    <td><code>header</code></td>
    <td>Header</td>
    <td style="word-wrap: break-word; white-space: normal;">Header/instructions for a set of questions (e.g. <i>Below is a list of items that describe children and youths. For each item that describes your child...</i>)</td>
    <td></td>
</tr>
<tr>
    <td><code>note</code></td>
    <td>Note</td>
    <td style="word-wrap: break-word; white-space: normal;">Note displayed to participants (e.g. <i>Enter weight in pounds.</i>)</td>
    <td></td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;"><code>unit</code></td>
    <td>Unit</td>
    <td style="word-wrap: break-word; white-space: normal;">Unit of measurement (e.g. <i>m, cm2, lbs</i>)</td>
    <td style="text-align: center;"><span class="tooltip tooltip-left"><i class="bi bi-filetype-json" style="font-size:17px;"></i>
        <span class="tooltiptext">Corresponds to <i>Units</i> in BIDS JSON</span></span></td>
</tr>
<tr>
<td><code>type_var</code></td>
    <td>Variable type</td>
    <td style="word-wrap: break-word; white-space: normal;">Possible values include: 
    <span class="tooltip">administrative<span class="tooltiptext">
    Data that gives context to the assessments, e.g. date of assessment, language, quality control, etc.</span></span>;
    <span class="tooltip">item<span class="tooltiptext">Original data provided by the participant, e.g. questions in a questionnaire</span></span>; 
    <span class="tooltip">derived item<span class="tooltiptext">Derived from original data provided by the participant - e.g. if the participant filled in two fields to enter their height in feet and inches, a derived item could integrate this information into one field that provides the height in inches</span></span>; 
    <span class="tooltip">summary score<span class="tooltiptext">Summary and/or score output based on algorithmic conversions of items/raw data</span></span></td>
    <td style="text-align: center;"><span class="tooltip tooltip-left"><i class="bi bi-filetype-json" style="font-size:17px;"></i>
    <span class="tooltiptext">Derivative element in BIDS JSON set to <i>true</i> if <i>type_var</i> = <i>summary score</i> or <i>derived item</i></span></span></td>
</tr>
<tr>
    <td><code>type_data</code></td>
    <td>Data type</td>
    <td style="word-wrap: break-word; white-space: normal;">
    Possible values include: date; timestamp; time; <span class="tooltip">character<span class="tooltiptext">Character only used for categorical columns</span></span>; text; integer; double</td>
    </td>
    <td style="text-align: center;"><span class="tooltip tooltip-left"><i class="fa-solid fa-lock"></i><span class="tooltiptext">Values do not vary across releases</span></span></td>
</tr>
<tr>
    <td><code>type_level</code></td>
    <td>Level of measurement</td>
    <td style="word-wrap: break-word; white-space: normal;">Possible values include: nominal; ordinal; interval; ratio</td>
    <td></td>
</tr>
<tr>
    <td><code>type_field</code></td>
    <td>Field type</td>
    <td style="word-wrap: break-word; white-space: normal;">Field type in data capture system as presented to participant (e.g. <i>dropdown; radio; checkbox</i></td>
    <td></td>
</tr>
<tr>
    <td><code>order_display</code></td>
    <td>Display order</td>
    <td>Display order of item within measure</td>
    <td></td>
</tr>
<tr>
    <td><code>branching_logic</code></td>
    <td>Branching logic</td>
    <td style="word-wrap: break-word; white-space: normal;">Branching logic applied to column/variable/question</td>
    <td></td>    
</tr>
<tr>
    <td><code>label_es</code></td>
    <td>Label (Spanish)</td>
    <td>Label (Spanish)</td>
    <td></td>
</tr>
<tr>
    <td><code>instruction_es</code></td>
    <td>Instruction (Spanish)</td>
    <td>Instruction (Spanish)</td>
    <td></td>
</tr>
<tr>
    <td><code>header_es</code></td>
    <td>Header (Spanish)</td>
    <td>Header (Spanish)</td>
    <td></td>
</tr>
<tr>
    <td><code>note_es</code></td>
    <td>Note (Spanish)</td>
    <td>Note (Spanish)</td>
    <td></td>
</tr>
<tr>
    <td><code>unique_identifiers</code></td>
    <td>Identifier column(s)</td>
    <td style="word-wrap: break-word; white-space: normal;">Unique identifier column names (variable/table)</td>
    <td style="text-align: center;"><span class="tooltip tooltip-left"><i class="fa-solid fa-lock"></i><span class="tooltiptext">Values do not vary across releases</span></span></td>
</tr>
<tr>
    <td><code>url_table</code></td>
    <td>Documentation for table</td>
    <td style="word-wrap: break-word; white-space: normal;">Link to <a href="../../instruments" target="_blank">study instrument documentation</a></td>
    <td></td>
</tr>
<tr>
    <td><code>url_table_warn_use</code></td>
    <td style="word-wrap: break-word; white-space: normal;">Responsible Use Warning (table)</td>
    <td style="word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">responsible use warning</a> (table)</td>
    <td></td>
</tr>
<tr>
    <td><code>url_table_warn_data</code></td>
    <td>Data Warning (table)</td>
    <td style="word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">data warning</a> (table)</td>
    <td></td>
</tr>
<tr>
<td><code>url_warn_use</code></td>
<td style="word-wrap: break-word; white-space: normal;">Responsible Use Warning (variable)</td>
<td style="word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">responsible use warning</a> (variable)</td>
<td></td>
</tr>
<tr>
<td><code>url_warn_data</code></td>
<td style="word-wrap: break-word; white-space: normal;">Data Warning (variable)</td>
<td style="word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">data warning</a> (variable)</td>
<td></td>
</tr>
<tr>
<td><code>order_sort</code></td>
<td>Sort order</td>
<td style="word-wrap: break-word; white-space: normal;">Standard sort order in table/measure (and ⇒ column order in database)</td>
<td></td>
</tr>
</tbody>
</table>

