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

The instrument table and variable names used for <a href="../../datacuration/phenotypes/" target="_blank">tabulated HBCD study data</a> largely follow standardized naming conventions adapted from the [ABCD Study](https://docs.abcdstudy.org/latest/documentation/curation/naming.html). This ensures consistency across instruments and derived datasets, allowing for intuitive parsing of variable meaning and structure.

## Convention Logic & Rules

Variable names are constructed from a set of ordered **main components** separated by single underscores. **Subcomponents**, if present, are preceded by double or triple underscores, which represent *subscale*, *version*, or *counter type* and multiselect fields (common in [Demographics](../instruments/SED/demo-cg.md)), respectively. Main components include:
<div class="naming-pattern"><code><span class="table-components"><span style="background-color: #f500e92c">domain_source_table</span></span>_<span class="tooltip">{scale}<span class="tooltiptext">Optional: only applies if instrument contains subscales</span></span>_item</code>
</div>

 - The first 3 main components, <code><span style="background-color: #f500e92c">domain_source_table</span></code>, make up the name of the table
 - <code><span style="color: teal;">{scale}</span></code> is only included for instruments that have subscales
 - See component descriptions and example values in table below

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
e.g., <code>ibqr</code> — Infant Behavior Questionnaire–Revised (<a href="../../instruments/bcgi/ibqr/#instrument-details" target="_blank">IBQ-R</a>)
</div>
</td>
</tr>

<tr>
<td>
    <span class="naming-token"><code><span class="tooltip">{scale}<span class="tooltiptext">Optional: only applies if instrument contains subscales</span></span></code></span>
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
    Item # <b>OR</b> admin/score fields
    </div>
</td>
<td>
<div class="dd-inline-list">
<ul>
  <li>Item number example: <code>001</code></li>
  <li>See <a href="../metadata/#variable-types" target="_blank">Variable Types</a> for details on administrative and summary score fields</li>
</ul>
</div>
</td>
</tr>

</tbody>
</table>

<div id="example" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
    <span class="text">Example</span>
    <a class="anchor-link" href="#example" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>For example, the variable name <code>mh_cg_ibqr_beh_001</code> is constructed as follows:</p>
<ul>
<li><code>mh</code> → domain (Behavior &amp; Caregiver-Child Interaction)</li>
<li><code>cg</code> → source (Caregiver)</li>
<li><code>ibqr</code> → table (the <a href="../../instruments/bcgi/ibqr/" target="_blank">IBQ-R</a>)</li>
<li><code>beh</code> → scale (Behavioral Inhibition subscale)</li>
<li><code>001</code> → item number</li>
</ul>
</div>

## Exceptions

Some table/variable names deviate from the standard naming conventions and will be standardized in the future. Main exceptions include:

##### Demographics Domain
The [Demographics domain](../instruments/index.md#demo), which contains derived table data, does not have a unique domain code, resulting in unconventional table names. Includes:  `sed_basic_demographics` and `par_visit_data`.

##### Biospecimens Domain
The [Biospecimen domain](../instruments/index.md#biospec) `table` naming component includes additional underscores for subcomponents, e.g. <code>bio_bm_biosample_nails_results</code>, where `table` corresponds to `biosample_nails_results` instead of `biosample`.

##### Tabulated Pipeline Derivatives  
[Tabulated derivatives](../datacuration/overview.md#tabulated-pipeline-derivatives) generated from processed imaging and EEG data use the following naming convention, where `derivative` corresponds to the basename of the source derivative files:
<div class="naming-pattern"><code>domain_pipeline_derivative</code></div>

For example, the [BIBSNet](../instruments/mri/smri.md#bibsnet) tabulated file:
<code>img_bibsnet<span style="color: teal;">_space-T1w_desc-aseg_volumes</span>.tsv</code>    
is sourced from:
<code>sub-[ID]_ses-[V0X]<span style="color: teal;">_space-T1w_desc-aseg_volumes</span>.tsv</code>
