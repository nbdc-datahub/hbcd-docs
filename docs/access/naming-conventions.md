# Naming Conventions

The instrument table and variable names used for <a href="../../datacuration/phenotypes/" target="_blank">tabulated HBCD study data</a> largely follow standardized naming conventions adapted from the [ABCD Study](https://docs.abcdstudy.org/latest/documentation/curation/naming.html). This ensures consistency across instruments and derived datasets, allowing for intuitive parsing of variable meaning and structure.

## Convention Logic & Rules

The standard variable naming format is comprised of 4 or 5 **main components** separated by a single underscore ( `_` ). The <code><span style="color: teal;">scale</span></code> component is only present in a subset of instruments that contain multiple scales:

<p style="font-size: 1.8em; font-weight: bold; padding: 10px;" align="center">
<code>domain_source_table_<span style="color: teal;">{scale}</span>_item</code>
</p>
 
Variable names may also include **subcomponents**, separated by double ( `__` ) underscores to indicate nested components of `table`, <code><span style="color: teal;">scale</span></code>, and/or `item`. Subcomponents distinguish finer details such as *subscales*, *versions*, or *counter types*. Finally, **multiselect fields** are preceded by triple underscores ( `___` ), mainly relevant for [V01 Demographics](../instruments/SED/v01-demo.md) (`sed_bm_demo`) variables.
 
## Naming Component Definitions

Details of individual naming components are as follows:

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
  <td><code>domain</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Data domain, e.g. <code>bio</code> (Biospecimens), <code>img</code> (Imaging) - see <a href="#values-key">values key</a></td>
</tr>
<tr>
  <td><code>source</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Can either be the subject/who the protocol element is about <b>OR</b> respondent/who completed the assessment. Examples include <code>cg</code> (Caregiver), <code>ch</code> (Child), etc. - see <a href="#values-key">values key</a></td>
</tr>
<tr>
<td><b><code>table</code></b></td>
<td>Instrument/protocol element name</td>
</tr>
<tr>
<td><b><code><span style="color: teal;">{scale}</span></code></b></td>
<td style="word-wrap: break-word; white-space: normal;">
Name of scale within instrument/protocol element for instruments with multiple scales (not including <a href="#administrative-summary-score-variables">administrative/summary score variables</a>). For example, the IBQ-R (VSF)+BI includes <a href="../../instruments/bcgi/ibqr/#instrument-details" target="_blank">4 scales</a>, each indicated by a separate <i>scale</i> component (e.g. Behavioral Inhibition scale annotated by a value of <code><span style="color: teal;">beh</span></code> in variable name <code>mh_cg_ibqr_<span style="color: teal;">beh</span>_001</code>).</td>
</tr>
<tr>
<td><b><code>item</code></b></td>
<td style="word-wrap: break-word; white-space: normal;">Will either be an item number corresponding to individual questions in a scale (e.g. <code>001</code>) <b>or</b> admin field/score label for administrative/summary score variables - <a href="#administrative-summary-score-variables"><i>see details</i></a></td>
</tr>
</tbody>
</table>

<div id="values-key" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-key"></i></span>
  <span class="text-with-link">
  <span class="text">Values Key: <code>domain</code> & <code>source</code></span>
  <a class="anchor-link" href="#values-key" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content" style="background-color: white;">
<div style="display: flex; gap: 24px; align-items: flex-start; padding-top: 5px;">
<table class="compact-table-no-vertical-lines" style="flex: 1; padding-left: 20px;">
<thead>
    <tr><th>Domain Values</th><th>Description</th></tr>
</thead>
<tbody>
    <tr><td><code>bio</code></td><td>BioSpecimens</td></tr>
    <tr><td><code>mh</code></td><td>Behavior/Child-Caregiver Interaction</td></tr>
    <tr><td><code>eeg</code></td><td>Tabular EEG</td></tr>
    <tr><td><code>img</code></td><td>Tabular Imaging</td></tr>
    <tr><td><code>ncl</code></td><td>Neurocognition and Language</td></tr>
    <tr><td><code>nt</code></td><td>Novel Tech</td></tr>
    <tr><td><code>pex</code></td><td>Pregnancy/Exposure Including Substance</td></tr>
    <tr><td><code>ph</code></td><td>Physical Health</td></tr>
    <tr><td><code>sed</code></td><td>Social and Environmental Determinants</td></tr>
</tbody>
</table>

<table class="compact-table-no-vertical-lines" style="flex: 1;">
<thead>
    <tr><th>Source Values</th><th>Description</th></tr>
</thead>
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

<div id="example" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Example</span>
  <a class="anchor-link" href="#example" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Let's break down the following example: <code>ncl_cg_spm2__inf_soc_001</code></p>
<ul>
<li><code>ncl</code>: <a href="../../instruments/#neurocog">Neurocognition &amp; Language</a> (<em>domain</em>)</li>
<li><code>cg</code>: Caregiver (<em>source</em>)</li>
<li><code>spm2__inf</code>: nested table name<ul>
<li><code>spm2</code>: the <a href="../../instruments/neurocog/spm2">SPM-2</a> instrument (<em>table</em>)</li>
<li><code>inf</code>: Infant version of SPM-2 (<em>table subcomponent</em>)</li>
</ul>
</li>
<li><code>soc</code>: scale for metrics of socialization (<em>scale</em>)</li>
<li><code>001</code>: item number (<em>item</em>)</li>
</ul>
</div>

## Exceptions

Some variables deviate from the standard naming conventions. These exceptions are temporary and will be standardized in future releases.

- **Derived data** — variables such as <code>sed_basic_demographics</code> and <code>par_visit_data</code> in the [Demographics domain](../instruments/index.md#demo)
- **Biospecimen data**, e.g. <code>bio_bm_biosample_nails_results</code> ([see instrument list](../instruments/index.md#biospec))
- **Tabulated MRI and EEG derivatives** ([see details](../datacuration/overview.md#warning)):  
Follow the naming convention <code>domain_pipeline_derivative</code>, where:  
    - <code>domain</code>: either <code>img</code> or <code>eeg</code>  
    - <code>pipeline</code>: processing pipeline name  
    - <code>derivative</code>: basename of the derivative output files sourced across participants to generate the tabulated data

### Administrative & Summary Score Variables

Administrative and summary score <a href="../metadata/#type_var" target="_blank">variable types</a> include **administrative fields** and **score labels** in place of the `item` naming component, respectively. Admin and score labels often include single underscores (e.g. `date_taken` and `summary_score`), but still represent single main components. Possible values include:
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

## Study Design Logic: Child-Centric Data Structure

The HBCD Study organizes data around the Child ID as the central key. All caregiver-provided data (e.g., from biological mothers or other caregivers) is nested under the corresponding Child ID. This structure supports the study’s goal of enabling longitudinal analyses of child development by:

- **Simplifying child-focused analysis**: Researchers can track each child’s data over time without remapping caregiver information.
- **Handling multi-birth cases cleanly**: When a caregiver reports on multiple children (e.g., twins), each child’s data remains distinct, avoiding complex joins or disambiguation.