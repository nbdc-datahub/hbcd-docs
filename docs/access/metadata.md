# Metadata & Naming Conventions

## NBDC Data Dictionary

HBCD data is organized into tables, each of which contains a set of variables. The metadata for studies released via the NBDC Data Hub consists of:

 - **Data dictionary**: Provides detailed information about the variables in the tabulated data resource, including the variable name, label, description, data type, and other relevant information. 
 - **Levels table**: Provides information about the levels of categorical variables in the tabulated data (label, order, etc.)

Below are the definitions for the columns in the data dictionary and levels table. Note that some columns also correspond to elements in the BIDS JSON files that accompany all tabulated data (hover over <i class="bi bi-filetype-json" style="font-size:18px; color:blue;"></i> icon for details in table below).

### Data Dictionary & Levels Column Definitions

<p>
<div id="metadata" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text">CAUTION – INSTRUCTION TEXT MAY BE INCOMPLETE OR MISALIGNED: Please review the details of this known issue carefully <a href="../../changelog/knownissues/#instruction-metadata-caution-please-read-carefully">HERE</a> before use.
 </span>
</div>
</p>

#### Data Dictionary
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
    <thead>
      <tr>
        <th style="width: 5%; border: 1px solid #ddd; padding: 5px; text-align: center;">Name</th>
        <th style="width: 20%; border: 1px solid #ddd; padding: 5px; text-align: center;">Label</th>
        <th style="width: 25%; border: 1px solid #ddd; padding: 5px; text-align: center;">Description</th>
        <th style="width: 30%; border: 1px solid #ddd; padding: 5px; text-align: center;"><b>{ </b>Possible Values<b> }</b> / Example(s)</th>
        <th style="width: 5%; border: 1px solid #ddd; padding: 5px; word-wrap: break-word; white-space: normal; text-align: center;">
            <span class="tooltip tooltip-left">Mutable
                <span class="tooltiptext">Values may vary between releases</span>
            </span></th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>study</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Study</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Indicates whether table/measure is a core components of the study or belongs to a substudy / anxiliary study</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><b>{</b> Core; Substudy <b>}</b></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>domain</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Domain</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Domain/<a href="https://hbcdstudy.org/workgroups-and-committees/">HBCD Workgroup</a></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">
        <b>{</b> Behavior/Child-Caregiver Interaction;<br>Biospecimens;<br>Demographics;<br>Neurocognition & Language;<br>Novel Tech;<br>Physical Health;<br>Pregnancy/Exposure Including Substance;<br>Social & Environmental Determinants;<br>Tabular EEG;<br>Tabular imaging <b>}</b>
        </td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>source</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Source</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Source of information for this table/measure</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><b>{</b> Biological Mother;<br>Caregiver (Responsible Adult);<br>Child;<br>General <b>}</b></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>table_name</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Table name</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Name of table/measure</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>mh_p_cbcl</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NO</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>table_label</code>&nbsp;
            <span class="tooltip tooltip-right"><i class="bi bi-filetype-json" style="font-size:18px;"></i>
            <span class="tooltiptext">Corresponds to <i>MeasurementToolMetadata</i> > <i>Description</i> in BIDS JSON</span></span>
        </td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Table label</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Label for table/measure</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Child Behavior Checklist [Parent]</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>name</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Variable name</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Name of column/variable/question</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>mh_p_cbcl__aggr_001</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NO</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>label</code>&nbsp;
          <span class="tooltip tooltip-right"><i class="bi bi-filetype-json" style="font-size:18px;"></i>
          <span class="tooltiptext">Corresponds to <i>Description</i> in BIDS JSON</span></span>
        </td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Variable label</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Label for column/variable/question</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">"Demands a lot of attention"</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>instruction</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Instruction</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Instructions preceding table/measure questions</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">"The next set of questions is about your child's behavior in different situations and contexts. Please fill in a response to all questions."</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>header</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Header</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Header/instructions for a set of questions</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">"Below is a list of items that describe children and youths. For each item that describes your child <span class="tooltip"><strong>...</strong>
        <span class="tooltiptext">... now or within the past 6 months, please choose whether the item is very true or often true of your child, somewhat or sometimes true of your child, or not true of your child. Please answer all items as well as you can, even if some do not seem to apply to your child."</span>
      </span>
     </td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>note</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Note</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Note displayed to participants</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">"Enter weight in pounds."</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>unit</code>&nbsp;
          <span class="tooltip tooltip-right"><i class="bi bi-filetype-json" style="font-size:18px;"></i>
          <span class="tooltiptext">Corresponds to <i>Units</i> in BIDS JSON</span></span>
        </td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Unit</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Unit of measurement</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">m, cm2, lbs</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>type_var</code>&nbsp;
          <span class="tooltip tooltip-right"><i class="bi bi-filetype-json" style="font-size:18px;"></i>
          <span class="tooltiptext">Derivative element in BIDS JSON set to <i>true</i> if <i>type_var</i> = <i>summary score</i> or <i>derived item</i></span></span>
        </td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Variable type</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Type of column/variable/question</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><b>{</b>
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
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>type_data</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Data type</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Data type (in database)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><b>{</b> date; timestamp; time;
      <span class="tooltip">character
        <span class="tooltiptext">Character only used for categorical columns</span>
      </span>;
      text; integer; double <b>}</b></td>
    </td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NO</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>type_level</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Level of measurement</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Measurement level/scale type</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><b>{</b> nominal; ordinal; interval; ratio <b>}</b></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>type_field</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Field type</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Field type in data capture system as presented to participant</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">dropdown; radio; checkbox</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>order_display</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Display order</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Display order of item within measure</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>branching_logic</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Branching logic</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Branching logic applied to column/variable/question</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>label_es</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Label (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Label (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>instruction_es</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Instruction (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Instruction (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>header_es</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Header (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Header (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>note_es</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Note (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Note (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>unique_identifiers</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Identifier column(s)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Unique identifier column names (variable/table)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NO</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>url_table</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Documentation for table</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Link to <a href="../../instruments" target="_blank">study instrument documentation</a></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>url_table_warn_use</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Responsible Use Warning (table)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">responsible use warning</a> (table)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>url_table_warn_data</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Data Warning (table)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">data warning</a> (table)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>url_warn_use</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Responsible Use Warning (variable)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">responsible use warning</a> (variable)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>url_warn_data</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Data Warning (variable)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Link to <a href="../resp_data_use/#warnings" target="_blank">data warning</a> (variable)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
    <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>order_sort</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Sort order</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Standard sort order in table/measure (and ⇒ column order in data/database)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
    </tr>
</tbody>
</table>


#### Levels Table
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
    <thead>
      <tr>
        <th style="width: 10%; text-align: center;">Name</th>
        <th style="width: 10%; text-align: center;">JSON Element</th>
        <th style="width: 35%; text-align: center;">Description</th>
        <th style="width: 10%; text-align: center;">Example</th>
        <th style="width: 5%; text-align: center;">
      <span class="tooltip tooltip-left">Mutable
        <span class="tooltiptext">Can change across releases</span>
      </span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>name</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Name of the categorical column/variable/question for which value/label pairs are reported</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">&nbsp;</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NO</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>value</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">left hand side</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Value of the level</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">1</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NO</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>order_level</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">
          <span class="tooltip">Position of the level
            <span class="tooltiptext">The order is used both to indicate in which order the response options were displayed to the participant and how they should be ordered in the data/visualizations</span>
          </span></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">2</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NO</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>label</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">right hand side</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Label of the level</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Yes</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
      </tr>
      <tr>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"><code>label_es</code></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;"></td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Label of the level (Spanish)</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Si</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">YES</td>
      </tr>
</table>


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

### Table Names

A unified naming convention has been applied to most table names in the tabulated release data (see overview of tabulated vs. file-based data [here](../datacuration/overview.md)). This convention is designed to provide clarity and consistency across the dataset, making it easier for users to understand the structure and content of the data. The **standard table name format** is:

<p style="font-size: 1.8em; font-weight: bold;" align="center">
<code>domain_source_table</code>
</p>

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <th></th>
  <th>Definition</th>
  <th>Possible Values <span class="tooltip tooltip-right"><span class="emoji"><i class="fa-solid fa-circle-info"></i></span><span class="tooltiptext" style="font-size: 0.9em;">for tables provided in the current release only</span></span>
</thead>
<tbody>
<tr>
  <td><b><code>domain</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;">Corresponds with <code>domain</code> in <a href="#data-dictionary">NBDC Data Dictionary</a> (e.g. MRI, Biospecimens, etc.)</td>
  <td>
    <span class="tooltip"><code>bio</code><span class="tooltiptext">Biospecimens</span></span>;
    <span class="tooltip"><code>eeg</code><span class="tooltiptext">EEG</span></span>;
    <span class="tooltip"><code>mh</code><span class="tooltiptext">Behavior/Child-Caregiver Interaction</span></span>;
    <span class="tooltip"><code>mri</code><span class="tooltiptext">MRI</span></span>;
    <span class="tooltip"><code>ncl</code><span class="tooltiptext">Neurocognition and Language</span></span>;
    <span class="tooltip"><code>nt</code><span class="tooltiptext">Novel Tech</span></span>;
    <span class="tooltip"><code>pex</code><span class="tooltiptext">Pregnancy/Exposure Including Substance</span></span>;
    <span class="tooltip"><code>ph</code><span class="tooltiptext">Physical Health</span></span>;
    <span class="tooltip"><code>sed</code><span class="tooltiptext">Social & Environmental Determinants</span></span>
  </td>
</tr>
<tr>
  <td><b><code>source</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;">Corresponds with <code>source</code> in <a href="#data-dictionary">NBDC Data Dictionary</a> (e.g. child vs birth parent)</td>
  <td>
    <span class="tooltip"><code>basic</code><span class="tooltiptext">General</span></span>;
    <span class="tooltip"><code>bm</code><span class="tooltiptext">Biological Mother</span></span>;
    <span class="tooltip"><code>cg</code><span class="tooltiptext">Caregiver (Responsible Adult)</span></span>;
    <span class="tooltip"><code>ch</code><span class="tooltiptext">Child</span></span>;
    <span class="tooltip"><code>visit</code><span class="tooltiptext">General</span></span>
  </td>
</tr>
<tr>
<td><b><code>table</code></b></td>
<td>Specific instrument name/protocol element</td>
<td>Varies by instrument; see full data dictionary for details.</td></tr>
</tbody>
</table>

<p>
<div id="domain-source" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span style="display: inline-flex; align-items: center;">
    <img src="../images/universal-access-accessibility-icon.png" 
        alt="Accessibility icon" 
        width="24" 
        style="vertical-align: middle; margin-right: 0.4em;" />
    Accessibility Feature: Show possible values in table format
  </span>
  <a class="anchor-link" href="#domain-source" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th></th>
      <th>Code</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <!-- domain values -->
    <tr>
      <td rowspan="9"><b>Domain</b></td>
      <td><code>bio</code></td><td>Biospecimens</td>
    </tr>
    <tr><td><code>eeg</code></td><td>EEG</td></tr>
    <tr><td><code>mh</code></td><td>Behavior/Child-Caregiver Interaction</td></tr>
    <tr><td><code>mri</code></td><td>MRI</td></tr>
    <tr><td><code>ncl</code></td><td>Neurocognition and Language</td></tr>
    <tr><td><code>nt</code></td><td>Novel Tech</td></tr>
    <tr><td><code>pex</code></td><td>Pregnancy/Exposure Including Substance</td></tr>
    <tr><td><code>ph</code></td><td>Physical Health</td></tr>
    <tr><td><code>sed</code></td><td>Social & Environmental Determinants</td></tr>
    <!-- source values -->
    <tr>
      <td rowspan="4"><b>Source</b></td>
      <tr><td><code>bm</code></td><td>Biological Mother</td></tr>
    </tr>
    <td><code>cg</code></td><td>Caregiver (Responsible Adult)</td>
    <tr><td><code>ch</code></td><td>Child</td></tr>
  </tbody>
</table>
</div>
</p>

<div id="exceptions" class="warning-banner warning-static-banner">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Exceptions</span>
  <a class="anchor-link" href="#exceptions" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
</div>
<div class="warning-static-content">
<p>Some tables in this release do not follow the standard naming convention precisely, which will be improved in future releases. Notable exceptions include:<br>
<ul>
<li><strong><a href="../../instruments/#mri">MRI & MRS</a> and <a href="../../instruments/#eeg">EEG</a></strong> tabulated data derived from file-based sources. These are clearly associated with their respective domains (e.g., MRI, EEG) and pertain exclusively to the Child.</li>
<li><strong>Derived tables</strong>: including Basic Demographics (<code>sed_basic_demographics</code>, containing global, static variables) and Visit Information (<code>par_visit_data</code>, containing dynamic/longitudinal visit-level data) - <a href="../../instruments/#demo">see details</a>.</li>
</div>

### Field Names

The field names within a table are all prepended by the table name (as described [above](#table-names)) followed by *scale* and *item* like so:

<p align="center">
<img src="../images/field-naming.png" alt="field naming convention: domain_source_table_scale_item"  width="400">
</p>

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <th></th>
  <th>Definition</th>
  <th>Example Values <span class="tooltip tooltip-right"><span class="emoji"><i class="fa-solid fa-circle-info"></i></span><span class="tooltiptext" style="font-size: 0.9em;">for tables provided in the current release only</span></span>
</thead>
<tbody>
<tr>
  <td><b><code>scale</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;">Name of scale or subscale</td>
  <td><span class="tooltip"><code>herit</code><span class="tooltiptext">heritage information</span></span>;
  <span class="tooltip"><code>lang</code><span class="tooltiptext">languages spoken</span></span>;
  <span class="tooltip"><code>administration</code><span class="tooltiptext">instrument administration</span></span>; etc.
  </td>
</tr>
<tr>
<td><b><code>item</code></b></td>
<td>Item in scale</td>
<td><code>001</code>; <code>001__01</code>; <code>mean</code>; <code>standard</code>; etc.</td></tr>
</tbody>
</table>

### Double Underscores 

Table and field names may contain additional sub-elements separated by **double underscores ( `__` )**, which indicate a more granular level of specificity. This extends the core naming convention:

 - **Single underscores ( `_` )** separate high-level components like **domain**, **source**, and **table** in the table names.
 - **Double underscores ( `__` )** distinguish finer details such as **subscales**, **versions**, or **counter types** within a given table or field.

<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">
    Example: <a href="../../instruments/#neurocog">Neurocognition & Language</a> Tables
  </span>
</div>
<div class="notification-static-content">
<div style="display: flex; gap: 2em; align-items: flex-start; margin-bottom: 2em;">
  <div style="flex: 1;">
    <p>
    <br>
    <br>
      The table name <code>ncl_ch_mlds</code> follows the basic structure and refers to data from the
      Multilingual Language Development Screener (<strong>MLDS</strong>).
    </p>
  </div>
  <div style="flex: 1;">
    <p><strong>Breakdown of <code>ncl_ch_mlds</code>:</strong></p>
    <table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
      <thead>
        <tr>
          <th style="width: 20%;">Component</th>
          <th style="width: 20%;">Naming Element</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code><b>ncl</b></code></td>
          <td><code>domain</code></td>
          <td>Neurocognition & Language</td>
        </tr>
        <tr>
          <td><code><b>ch</b></code></td>
          <td><code>source</code></td>
          <td>Child</td>
        </tr>
        <tr>
          <td><code><b>mlds</b></code></td>
          <td><code>table</code></td>
          <td>MLDS instrument</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div style="display: flex; gap: 2em; align-items: flex-start;">
  <div style="flex: 1;">
    <p>
      Now consider a more complex example: <code>ncl_cg_spm2__inf</code>, the table name for the Sensory Processing Measure – Infant/Toddler (<strong>SPM-2</strong>). Here, the double underscore separates the instrument identifier (<code>spm2</code>) from its subscale or version (<code>inf</code>), indicating this table
      contains data from the <strong>infant-specific version</strong> of the <strong>SPM-2</strong> instrument.
    </p>
  </div>
  <div style="flex: 1;">
    <p><strong>Breakdown of <code>ncl_cg_spm2__inf</code>:</strong></p>
    <table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
      <thead>
        <tr>
          <th style="width: 20%;">Component</th>
          <th style="width: 20%;">Naming Element</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code><b>ncl</b></code></td>
          <td><code>domain</code></td>
          <td>Neurocognition & Language</td>
        </tr>
        <tr>
          <td><code><b>cg</b></code></td>
          <td><code>source</code></td>
          <td>Caregiver</td>
        </tr>
        <tr>
          <td><code><b>spm2</b></code></td>
          <td><code>table</code></td>
          <td>SPM2 instrument</td>
        </tr>
        <tr>
          <td><code><b>inf</b></code></td>
          <td><code>subtable</code></td>
          <td>Infant version</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>

## Study Design Logic: Child-Centric Data Structure

The HBCD Study organizes data around the Child ID as the central key. All caregiver-provided data (e.g., from biological mothers or other caregivers) is nested under the corresponding Child ID. This structure supports the study’s goal of enabling longitudinal analyses of child development by:

- **Simplifying child-focused analysis**: Researchers can track each child’s data over time without remapping caregiver information.
- **Handling multi-birth cases cleanly**: When a caregiver reports on multiple children (e.g., twins), each child’s data remains distinct, avoiding complex joins or disambiguation.