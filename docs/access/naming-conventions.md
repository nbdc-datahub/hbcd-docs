# Naming Conventions

A standardized naming convention is used across most tables and fields in the <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> release data. These conventions are adapted from the [ABCD Study](https://docs.abcdstudy.org/latest/documentation/curation/naming.html) and ensure consistency across instruments and derived datasets, allowing for intuitive parsing of variable meaning and structure.

## Convention Logic & Rules

The standard variable naming format is comprised of 4 or 5 main components: 

<p style="font-size: 1.8em; font-weight: bold; padding: 10px;" align="center">
<code>domain_source_table_<span style="color: teal;">{scale}</span>_item</code>
</p>

 - **Main components** are generally separated by a single underscore ( `_` ). Most instruments with multiple scales will additionally include the <code><span style="color: teal;">scale</span></code> component (this component is otherwise optional and not included in all variable names).   
 - **Subcomponents** are separated by double ( `__` ) underscores to indicate nested components of `table`, <code><span style="color: teal;">scale</span></code>, and/or `item`. Subcomponents distinguish finer details such as *subscales*, *versions*, or *counter types*. Multiselect fields are preceded by triple underscores ( `___` ), mainly relevant for [V01 Demographics](../instruments/SED/v01-demo.md) (`sed_bm_demo`) variables.
 
## Naming Component Definitions

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <th style="width: 10%;">Component</th>
  <th style="width: 45%;">Definition</th>
  <th style="width: 35%;">Example Values</th>
</thead>
<tbody>
<tr>
  <td><b><code>domain</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;">Data domain (e.g. biospecimens, imaging)</td>
  <td><span class="tooltip"><code>bio</code><span class="tooltiptext">Biospecimens</span></span>;
  <span class="tooltip"><code>img</code><span class="tooltiptext">Imaging/MRI</span></span>;
  <span class="tooltip"><code>sed</code><span class="tooltiptext">Social & Environmental Determinants</span></span>;
  <span class="tooltip"><code>pex</code><span class="tooltiptext">Pregnancy & Exposures, Including Substance Use</span></span>;
  <i><a href="#domain-source-values">see full list</a></i></td>
</tr>
<tr>
  <td><b><code>source</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;"><span class="tooltip">Subject<span class="tooltiptext">who the protocol element is about</span></span>/<span class="tooltip">respondent<span class="tooltiptext">who completed the assessment</span></span> (e.g., child, birth parent)</td>
  <td><span class="tooltip"><code>bm</code><span class="tooltiptext">Biological Mother</span></span>;
    <span class="tooltip"><code>ch</code><span class="tooltiptext">Child</span></span>; <i><a href="#domain-source-values">see full list</a></i>
  </td>
</tr>
<tr>
<td><b><code>table</code></b></td>
<td>Instrument/protocol element name</td>
<td>Varies by instrument</td></tr>
</tr>
<tr>
<td><b><code><span style="color: teal;">{scale}</span></code></b></td>
<td style="word-wrap: break-word; white-space: normal;">Name of scale within instrument/protocol element - <i>only if instrument contains multiple scales</i></td>
<td style="word-wrap: break-word; white-space: normal;">Varies by instrument - <i><a href="#scale">see details</a></i></td></tr>
</tr>
<tr>
  <td><b><code>item</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;">Will either be an item number corresponding to individual questions in a scale <b>or</b> admin field/score label for administrative/summary score variables - <a href="#exceptions-admin"><i>see details</i></a></td>
  <td style="word-wrap: break-word; white-space: normal;"><code>001</code>; <code>001__01</code>; etc.<br>
    <b>or</b> <a href="#exceptions-admin">admin field/score label</a>
</tr>
</tbody>
</table>

### Details<span class="hint">(Click sections to expand)</span>

<div id="domain-source-values" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Domain & Source: Possible Values</span>
  <a class="anchor-link" href="#domain-source-values" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<div style="display: flex; gap: 30px; align-items: flex-start;">
  <table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <caption style="caption-side: top; font-weight: bold; padding-bottom: 8px;">
    Possible Values:  <code>domain</code>
    </caption>
    <tbody>
      <tr><td><code>bio</code></td><td>BioSpecimens</td></tr>
      <tr><td><code>eeg</code></td><td>Tabular EEG</td></tr>
      <tr><td><code>mh</code></td><td>Behavior/Child-Caregiver Interaction</td></tr>
      <tr><td><code>img</code></td><td>Tabular Imaging</td></tr>
      <tr><td><code>ncl</code></td><td>Neurocognition and Language</td></tr>
      <tr><td><code>nt</code></td><td>Novel Tech (<i>Novel Technology & Wearable Sensors</i>)</td></tr>
      <tr><td><code>pex</code></td><td>Pregnancy/Exposure Including Substance</td></tr>
      <tr><td><code>ph</code></td><td>Physical Health</td></tr>
      <tr><td><code>sed</code></td><td>Social and Environmental Determinants</td></tr>
    </tbody>
  </table>
  <table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <caption style="caption-side: top; font-weight: bold; padding-bottom: 8px;">
    Possible Values:  <code>source</code>
    </caption>
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

<div id="scale" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Scale Details</span>
  <a class="anchor-link" href="#scale" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Most variables of instruments/tables composed of multiple scales include an additional naming component for <code><span style="color: teal;">scale</span></code> (with the exception of administrative/summary score variables - <a href="#exceptions-admin"><i>see details</i></a>). The following instruments in the current release are examples of tables that include the scale component in their variable names. Note that this is not a comprehensive list.</p>
<br>
<br>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th>Domain</th>
      <th>Instrument</th>
      <th>Table Name</th>
      <th>Example Variable</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="tooltip tooltip-right">BCGI<span class="tooltiptext">Behavior & Child-Caregiver Interaction</span></span></td>
      <td><a href="../../instruments/bcgi/ibqr" target="_blank">IBQ-R (VSF)+BI</a></td>
      <td><code>mh_cg_ibqr</code></td>
      <td><code>mh_cg_ibqr_<span style="color: teal;">beh</span>_001</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right">PEX<span class="tooltiptext">Pregnancy & Exposure, Including Substance Use</span></span></td>
      <td><a href="../../instruments/pregexp/mh/fam-mh" target="_blank">FAM MH</a></td>
      <td><code>pex_bm_psych</code></td>
      <td><code>pex_bm_psych_<span style="color: teal;">bf</span>_001</code></td>
    </tr>
    <tr>
      <td rowspan="2"><span class="tooltip tooltip-right">SED<span class="tooltiptext">Social & Environmental Determinants</span></span></td>
      <td><a href="../../instruments/SED/bfy" target="_blank">BFY</a></td>
      <td><code>sed_bm_bfy</code></td>
      <td><code>sed_bm_bfy_<span style="color: teal;">econstr</span>_001</code></td>
    </tr>
     <tr>
      <td><a href="../../instruments/SED/promis" target="_blank">PROMIS</a></td>
      <td><code>sed_bm_strsup</code></td>
      <td><code>sed_bm_strsup_<span style="color: teal;">socspprt</span>_001</code></td>
    </tr>
  </tbody>
</table>
</div>

## Exceptions<span class="hint">(Click sections to expand)</span>

Some variables do not fully follow the standard naming convention, which will be improved in future releases. Notable exceptions are as follows (*click to expand*):

<div id="exceptions-admin" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Administrative & Summary Score Variables</span>
  <a class="anchor-link" href="#exceptions-admin" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Administrative (e.g., language or date of administration) and summary score (e.g., sums or means of individual items in a table) variables include <strong>administrative fields</strong> and <strong>score labels</strong> in place of <code>item</code> (or <code><span style="color: teal;">{scale}</span>_item</code> where relevant). Admin and score labels often include single underscores, but represent single main components. For example, possible values include:</p>
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
</div>

<div id="exceptions-derived" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Derived Variables</span>
  <a class="anchor-link" href="#exceptions-derived" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Derived tables, including Basic Demographics (<code>sed_basic_demographics</code>), containing global, static variables, and Visit Information (<code>par_visit_data</code>), containing dynamic/longitudinal visit-level data, do not follow the naming conventions outlined above. For example, both fall under the domain <code>Demographics</code> and source <code>General</code> in the <a href="#nbdc-data-dictionary">NBDC Data Dictionary</a>, but use <code>sed_basic</code> (in reference to Social &amp; Environmental Determinants from which the Basic Demographics information is derived) and <code>par_visit</code> (for participant information from visit-level data) in place of the <code>domain_source</code> naming components. </p>
</div>

<div id="exceptions-biospec" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Biospecimens</span>
  <a class="anchor-link" href="#exceptions-biospec" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Biospecimen names are largely descriptive, e.g. <code>bio_bm_biosample_nails_results</code> and <code>bio_bm_biosample_urine</code> table names.</p>
</div>

<div id="exceptions-mri" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Tabulated MRI, MRS, & EEG Data</span>
  <a class="anchor-link" href="#exceptions-mri" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Tabulated data derived from <a href="../../instruments/#mri" target="_blank">MRI & MRS</a> and <a href="../../instruments/#eeg" target="_blank">EEG</a> file-based data follow a unique naming convention. All files begin with the <strong>domain</strong> (<code>img</code> or <code>eeg</code>) in accordance with the conventions described above, but the following elements are the pipeline name (<code>pipeline</code>) and basename of the derivative output by that pipeline (<code>derivative</code>):</p> 
<p style="font-size: 1.4em; font-weight: bold; padding: 10px;" align="center">
<code>domain_pipeline_derivative</code>
</p>
<p>For example, the following subject/session-level <a href="../../instruments/mri/fmri/#xcpd" target="_blank">XCP-D derivatives</a> are combined into a single tabulated file:</p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<tr>
<td><b>File-based derivatives</b></td>
<td><code>sub-{ID}_ses-{V0X}_task-rest_dir-PA_run-{X}<span style="color: teal;">_space-fsLR_seg_Gordon_stat-alff_bold</span>.tsv</code> </td>
</tr>
<tbody>
<tr>
<td><b>Tabulated file</b></td>
<td><code>img_xcpd<span style="color: teal;">_space-fsLR_seg_Gordon_stat-alff_bold</span>.tsv</code></td>
</tbody>
</table>
</ul>
</div>

## Example

Let's break down the following example: `ncl_cg_spm2__inf_soc_001`

- `ncl`: [Neurocognition & Language](../instruments/index.md#neurocog) (*domain*)
- `cg`: Caregiver (*source*)
- `spm2__inf`: nested table name
    - `spm2`: the [SPM-2](../instruments/neurocog/spm2.md) instrument (*table*)
    - `inf`: Infant version of SPM-2 (*table subcomponent*)
- `soc`: scale for metrics of socialization (*scale*)
- `001`: item number (*item*)


## Study Design Logic: Child-Centric Data Structure

The HBCD Study organizes data around the Child ID as the central key. All caregiver-provided data (e.g., from biological mothers or other caregivers) is nested under the corresponding Child ID. This structure supports the study’s goal of enabling longitudinal analyses of child development by:

- **Simplifying child-focused analysis**: Researchers can track each child’s data over time without remapping caregiver information.
- **Handling multi-birth cases cleanly**: When a caregiver reports on multiple children (e.g., twins), each child’s data remains distinct, avoiding complex joins or disambiguation.