<style>
.naming-pattern {
  text-align: center;
  font-size: 1.4em;
  font-weight: 600;
  margin: 1em 0;
}

.naming-pattern code {
  background: var(--md-code-bg-color, #f5f5f5);
  padding: 2px 6px;
  border-radius: 4px;
}
.table-name-part {
  text-decoration: underline;
  text-decoration-thickness: 2px;
  text-underline-offset: 0.18em;
}
</style>

# Naming Conventions

The instrument table and variable names used for <a href="../../datacuration/phenotypes/">tabulated HBCD study data</a> largely follow standardized naming conventions adapted from the [ABCD Study](https://docs.abcdstudy.org/latest/documentation/curation/naming.html). This ensures consistency across instruments and derived datasets, allowing for intuitive parsing of variable meaning and structure.

## Convention Logic & Rules

Variable names are constructed from a set of ordered main components separated by single underscores. Subcomponents, if present, are preceded by double or triple underscores, which represent *subscale*, *version*, or *counter type* and multiselect fields. Main components include:
<div class="naming-pattern"><code><span class="table-components"><span style="background-color: #f500e92c">domain_source_table</span></span>_{scale}_item</code>
</div>

 - The first 3 main components, <code><span style="background-color: #f500e92c">domain_source_table</span></code>, make up the name of the table
 - <code><span style="color: teal;">{scale}</span></code> is only included for instruments that have subscales

<table class="table-no-vertical-lines">
<thead class="table-header">
<tr>
<th width="35%">Naming Component</th>
<th>Possible Values</th>
</tr>
</thead>
<tbody>
<tr>
<td>
  <span class="naming-token"><code>domain</code></span>
  <div class="naming-description">
    Data domain
  </div>
</td>
<td>
<div class="dd-inline-list">
<ul>
    <li><code>bio</code>: Biospecimen &amp; Omics</li>
    <li><code>eeg</code>: Tabular EEG</li>
    <li><code>img</code>: Tabular Imaging</li>
    <li><code>mh</code>: Behavior/Child-Caregiver Interaction</li>
    <li><code>ncl</code>: Neurocognition and Language</li>
    <li><code>nt</code>: Novel Technology &amp; Wearable Sensors</li>
    <li><code>ph</code>: Physical Health</li>
    <li><code>pex</code>: Pregnancy/Exposure Including Substance</li>
    <li><code>sed</code>: Social and Environmental Determinants</li>
</ul>
</div>
</td>
</tr>

<tr>
<td>
    <span class="naming-token"><code>source</code></span>
    <div class="naming-description">
    Respondent <b>OR</b> who the data is about
    </div>
</td>
<td>
<div class="dd-inline-list">
<ul>
    <li><code>bm</code>: Biological Mother</li>
    <li><code>cg</code>: Caregiver (Responsible Adult)</li>
    <li><code>ch</code>: Child</li>
    <li><code>ld</code>: Linked Data</li>
    <li><code>ra</code>: RA (Research Assistant)</li>
</ul>
</div>
</td>
</tr>

<tr>
<td>
    <span class="naming-token"><code>table</code></span>
    <div class="naming-description">
    Instrument name
    </div>
</td>
<td>
<div class="dd-inline-list">
e.g., <code>ibqr</code> — Infant Behavior Questionnaire–Revised (IBQ-R)
</div>
</td>
</tr>

<tr>
<td>
    <span class="naming-token"><code>{scale}</code></span>
    <div class="naming-description">
    Instrument subscale, as applicable
    </div>
</td>
<td>
<div class="dd-inline-list">
e.g., <code>mh_cg_ibqr_<span style="color: teal;"><b>beh</b></span>_001</code> = <b>Behavioral Inhibition</b> subscale
</div>
</td>
</tr>

<tr>
<td>
    <span class="naming-token"><code>item</code></span>
    <div class="naming-description">
    Item number OR admin/score fields
    </div>
</td>
<td>
<div class="dd-inline-list">
<ul>
  <li>Item number example: <code>001</code></li>
  <li>See <a href="../metadata/#variable-types">Variable Types</a> for details on administrative and summary score fields</li>
</ul>
</div>
</td>
</tr>
</tbody>
</table>

## Exceptions

Some table/variable names deviate from the standard naming conventions and will be standardized in the future. Main exceptions include the following. See [Study Instruments](../instruments/index.md) for more details about each domain. This includes, for example, Demographics, which are derived data tables with unconventional table naming (`sed_basic_demographics` and `par_visit_data`).      
[Tabulated derivatives](../datacuration/overview.md#tabulated-pipeline-derivatives) generated from processed imaging and EEG data also follow slightly different conventions (where `derivative` corresponds to the basename of the source derivative files):
<div class="naming-pattern"><code>domain_pipeline_derivative</code></div>

For example, the BIBSNet tabulated file:
<code>img_bibsnet<span style="color: teal;">_space-T1w_desc-aseg_volumes</span>.tsv</code>    
is sourced from:
<code>sub-[ID]_ses-[V0X]<span style="color: teal;">_space-T1w_desc-aseg_volumes</span>.tsv</code>
