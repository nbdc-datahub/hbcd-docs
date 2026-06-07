<style>
/* .wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
} */
  .naming-pattern {
  text-align: center;
  font-size: 1.6em;
  font-weight: 600;
  margin: 1em 0;
}
.naming-pattern code {
  background: var(--md-code-bg-color, #f5f5f5);
  padding: 2px 6px;
  border-radius: 4px;
}
.suffix {
  color: teal;
  font-weight: 500;
}
</style>

# Naming Conventions

The instrument table and variable names used for <a href="../../datacuration/phenotypes/" target="_blank">tabulated HBCD study data</a> largely follow standardized naming conventions adapted from the [ABCD Study](https://docs.abcdstudy.org/latest/documentation/curation/naming.html). This ensures consistency across instruments and derived datasets, allowing for intuitive parsing of variable meaning and structure.

## Convention Logic & Rules

Variable names are constructed from a set of ordered **main components** separated by single underscores. **Subcomponents**, if present, are preceded by double or triple underscores, which represent *subscale*, *version*, or *counter type* and multiselect fields (common in [Demographics](../instruments/SED/demo-cg.md)), respectively. Main components include:

<div class="naming-pattern">
<code>domain_source_table_<span class="tooltip">{scale}<span class="tooltiptext">Optional: only applies to multi-scale instruments</span></span>_item</code>
</div>

<table class="table-no-vertical-lines dd">
<thead>
<tr>
  <th>Component</th>
  <th>Description & Possible Values</th>
</tr>
</thead>
<tbody>

<tr>
  <td><code>domain</code></td>
  <td>
    Data domain the variable belongs to.
    <div class="dd-inline-list">
      <span><code>bio</code>: BioSpecimens &amp; Omics</span>
      <span><code>eeg</code>: Tabular EEG</span>
      <span><code>img</code>: Tabular Imaging</span>
      <span><code>mh</code>: Behavior/Child-Caregiver Interaction</span>
      <span><code>ncl</code>: Neurocognition and Language</span>
      <span><code>nt</code>: Novel Technology &amp; Wearable Sensors</span>
      <span><code>ph</code>: Physical Health</span>
      <span><code>pex</code>: Pregnancy/Exposure Including Substance</span>
      <span><code>sed</code>: Social and Environmental Determinants</span>
    </div>
  </td>
</tr>

<tr>
  <td><code>source</code></td>
  <td>
    Indicates either the respondent (who completed the assessment) or who the measurement refers to.
    <div class="dd-inline-list">
      <span><code>bm</code>: Biological Mother</span>
      <span><code>cg</code>: Caregiver (Responsible Adult)</span>
      <span><code>ch</code>: Child</span>
      <span><code>ld</code>: Linked Data</span>
      <span><code>ra</code>: RA (research assistant)</span>
    </div>
  </td>
</tr>

<tr>
  <td><code>table</code></td>
  <td>
    The instrument or protocol element name.
    <div class="dd-inline-list">
      e.g., <code>ibqr</code> — Infant Behavior Questionnaire–Revised
    </div>
  </td>
</tr>

<tr>
  <td><code>scale</code> <span class="subtle">(optional)</span></td>
  <td>
    Used only when an instrument contains multiple scales.
    <div class="dd-inline-list">
      e.g., <code>beh</code> in <code>mh_cg_ibqr_<span style="color: teal;">beh</span>_001</code> (<a href="../../instruments/bcgi/ibqr/#instrument-details" target="_blank">IBQ-R</a>) indicates the Behavioral Inhibition subscale
    </div>
  </td>
</tr>

<tr>
  <td><code>item</code></td>
  <td>
    Instrument item number (e.g., <code>001</code>), but may be replaced by administrative or summary score fields
    <div class="dd-inline-list">
      See <a href="../metadata/#variable-types" target="_blank">Variable Types</a> for details
    </div>
  </td>
</tr>
</tbody>
</table>

For example, the variable name `mh_cg_ibqr_beh_001` is constructed as follows:

- `mh` → domain (Behavior & Caregiver-Child Interaction)
- `cg` → source (Caregiver)
- `ibqr` → table (the <a href="../../instruments/bcgi/ibqr/" target="_blank">IBQ-R</a>)
- `beh` → scale (Behavioral Inhibition subscale)
- `001` → item number

## Exceptions

Some table/variable names deviate from the standard naming conventions and will be standardized in the future. Main exceptions include:

 - [Demographics domain](../instruments/index.md#demo): <code>sed_basic_demographics</code> and <code>par_visit_data</code>
 - [Biospecimen domain](../instruments/index.md#biospec), e.g. <code>bio_bm_biosample_nails_results</code>
 - [Tabulated derivatives](../datacuration/overview.md#tabulated-pipeline-derivatives) derived from processed imaging and EEG data follow the naming convention `domain_pipeline_derivative`, where `derivative` corresponds to the basename of the source derivative files
    - For example, <code>img_xcpd<span style="color: teal;">_space-fsLR_seg_Gordon_stat-alff_bold</span>.tsv</code> contains participant data aggregated across <code>sub-[ID]_ses-[V0X]_task-rest_dir-PA_run-{X}<span style="color: teal;">_space-fsLR_seg_Gordon_stat-alff_bold</span>.tsv</code>  <a href="../../instruments/mri/fmri/#xcp-d" target="_blank">XCP-D</a> derivatives.