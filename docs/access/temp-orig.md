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
    <td style="word-wrap: break-word; white-space: normal;">Possible values include: {<i>nominal; ordinal; interval; ratio</i>}</td>
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
    <td>Documentation<br>for table</td>
    <td style="word-wrap: break-word; white-space: normal;">Link to <a href="../../instruments" target="_blank">study instrument documentation</a></td>
    <td></td>
</tr>
<tr>
    <td><code>url_table_warn_use</code></td>
    <td style="word-wrap: break-word; white-space: normal;">Responsible Use<br>Warning (table)</td>
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
<td style="word-wrap: break-word; white-space: normal;">Responsible Use<br>Warning (variable)</td>
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