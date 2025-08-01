# Metadata & Naming Conventions

## NBDC Data Dictionary

<span class="tooltip">Tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> HBCD data is organized into a standardized table format, each of which contains a set of variables. The metadata for studies released via the NBDC Data Hub consists of:

 - **Data dictionary**: Provides detailed information about the variables in the tabulated data resource, including the variable name, label, description, data type, and other relevant information. 
 - **Levels table**: Provides information about the levels of categorical variables in the tabulated format data (label, order, etc.)

Below are the definitions for the columns in the data dictionary and levels table. Note that some columns also correspond to elements in the BIDS JSON files that accompany all <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> data (hover over <i class="bi bi-filetype-json" style="font-size:18px; color:blue;"></i> icon for details in table below).

<p>
<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">
    See <a href="../../../datacuration/overview/">here</a> for overview of tabulated vs file-based data.
  </span>
</div>
</p>

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

A unified naming convention has been applied to most table and field names in the <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> release data (see overview of tabulated vs. <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> data [here](../datacuration/overview.md)). HBCD largely follows the same naming conventions as ABCD ([see details](https://docs.abcdstudy.org/latest/documentation/curation/naming.html)), adapted for HBCD study measures. This convention is designed to provide clarity and consistency across the dataset, making it easier for users to understand the structure and content of the data. 

### Primary Components

The **standard variable naming format** is comprised of 4 components, separated by a single underscore ( `_` ):

<p style="font-size: 1.8em; font-weight: bold;" align="center">
<code>domain_source_table_item</code>
</p>

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <th style="width: 5%;"></th>
  <th style="width: 60%;">Definition</th>
  <th style="width: 25%;">Example Values</th>
</thead>
<tbody>
<tr>
  <td><b><code>domain</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;">Expanded version of <a href="#data-dictionary">NBDC Data Dictionary</a> <code>domain</code> values that includes additional domains (e.g. Biosensors)</td>
  <td>
  <span class="tooltip"><code>bio</code><span class="tooltiptext">Biospecimens</span></span>;
  <span class="tooltip"><code>img</code><span class="tooltiptext">Imaging/MRI</span></span> (<i><a href="#domain">see full list</a></i>)</td>
</tr>
<tr>
  <td><b><code>source</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;">Corresponds with <code>source</code> in <a href="#data-dictionary">NBDC Data Dictionary</a>; indicates either the subject (who the protocol element is about) or respondent (who completed the assessment).</td>
  <td>
    <span class="tooltip"><code>bm</code><span class="tooltiptext">Biological Mother</span></span>;
    <span class="tooltip"><code>ch</code><span class="tooltiptext">Child</span></span> (<i><a href="#source">see full list</a></i>)
  </td>
</tr>
<tr>
<td><b><code>table</code></b></td>
<td>Specific instrument name/protocol element.</td>
<td style="word-wrap: break-word; white-space: normal;">(varies by instrument)</td></tr>
</tr>
<tr>
<td><b><code>item</code></b></td>
<td style="word-wrap: break-word; white-space: normal;">The item component will be one of the following:<br>
  1) a 3-digit number corresponding to individual questions in a scale<br>
  2) an administrative variable<br>
  3) a summary scores for individual items in a table</td>
<td style="word-wrap: break-word; white-space: normal;"> 1) <code>001</code><br>
  2) <code>administration</code>, <code>lang</code>, etc.<br>
  3) <code>summary_score</code></td></tr>
</tr>
</tbody>
</table>

<div id="domain" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span style="display: inline-flex; align-items: center;">
   Domain Values
  </span>
  <a class="anchor-link" href="#domain" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th>Keyword</th>
      <th>Domain</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>bio</code></td><td>BioSpecimens</td></tr>
    <tr><td><code>eeg</code></td><td>Tabular EEG</td></tr>
    <tr><td><code>mh</code></td><td>Behavior/Child-Caregiver Interaction</td></tr>
    <tr><td><code>img</code></td><td>Tabular Imaging</td></tr>
    <tr><td><code>ncl</code></td><td>Neurocognition and Language</td></tr>
    <tr><td><code>nt</code></td><td><span class="tooltip">Novel Tech<span class="tooltiptext">Novel Technology & Wearable Sensors</span></span></td></tr>
    <tr><td><code>pex</code></td><td>Pregnancy/Exposure Including Substance</td></tr>
    <tr><td><code>ph</code></td><td>Physical Health</td></tr>
    <tr><td><code>sed</code></td><td>Social and Environmental Determinants</td></tr>
    <tr><td><code>par</code></td><td style="word-wrap: break-word; white-space: normal;">Participant Information<br><i>Note: this is an additional domain not included in NBDC Data Dictionary domains, e.g. <code>par_visit_data</code> (Visit Information), containing dynamic/longitudinal visit-level data, falls under the DD domain <code>Demographics</code></td></tr>
  </tbody>
</table>
</div>

<div id="source" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span style="display: inline-flex; align-items: center;">
   Source Values
  </span>
  <a class="anchor-link" href="#source" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th>Keyword</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>bm</code></td><td>Biological Mother</td></tr>
    <td><code>cg</code></td><td>Caregiver (Responsible Adult)</td>
    <tr><td><code>ch</code></td><td>Child</td></tr>
    <tr><td><code>cl</code></td><td>Clinician</td></tr>
    <tr><td><code>fd</code></td><td>Family Data</td></tr>
    <tr><td><code>ld</code></td><td>Linked Data</td></tr>
    <tr><td><code>ra</code></td><td>RA (research assistant)</td></tr>
    <tr><td><code>si</code></td><td>Sibling</td></tr>
    <tr><td><code>te</code></td><td>Teacher</td></tr>
    <tr><td><code>basic</code></td><td>General information. <i>Not included in NBDC Data Dictionary source options, e.g. for <code>sed_basic_demographics</code> (derived demographics information), the DD source is <code>General</code></i>.</td></tr>
    <tr><td><code>visit</code></td><td>Visit information. <i>Not included in NBDC Data Dictionary source options, e.g. for <code>par_visit_data</code> (visit-level data), the DD source is <code>General</code></i>.</td></tr>
  </tbody>
</table>
</div>

### Subcomponents

The `table` and `item` components can have additional subcomponents separated by **double underscores ( `__` )** to indicate nesting within the four main components. Subcomponents distinguish finer details such as **subscales**, **versions**, or **counter types** within a given table or field.

For example, for the table name `ncl_cg_spm2__inf`, the double underscore separates the instrument (`spm2`) from its subcomponent/version (`inf`), i.e., the infant-specific version of SPM-2:

 - `ncl` (domain): <a href="../../instruments/#neurocog">Neurocognition & Language</a>
 - `cg` (source): Caregiver
 - `spm2` (table): the <a href="../../instruments/neurocog/spm2">SPM-2</a> instrument
    - `inf` (table subcomponent): infant version of SPM-2

### Exceptions

Some variables do not fully follow the standard naming convention, though this will be improved in future releases. Notable exceptions include tabulated data for [MRI & MRS](../instruments/index.md#mri) and [EEG](../instruments/index.md#eeg) derived from associated <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> data. 

All files begin with the **domain** (`img` or `eeg`) in accordance with the conventions described above, but the following elements may differ:

 - In place of **source**, which for all MRI and EEG data is Child/`ch`, the pipeline name is typically given (e.g. `bibsnet`, `xcpd`, `osprey`, `made`, etc.)
 - In place of **table_item**, the keywords typically match the name of the pipeline derivative file from which the table was generated (see full lists of file-based derivatives for each pipeline [here](../datacuration/derivatives.md)). 

## Study Design Logic: Child-Centric Data Structure

The HBCD Study organizes data around the Child ID as the central key. All caregiver-provided data (e.g., from biological mothers or other caregivers) is nested under the corresponding Child ID. This structure supports the study’s goal of enabling longitudinal analyses of child development by:

- **Simplifying child-focused analysis**: Researchers can track each child’s data over time without remapping caregiver information.
- **Handling multi-birth cases cleanly**: When a caregiver reports on multiple children (e.g., twins), each child’s data remains distinct, avoiding complex joins or disambiguation.
