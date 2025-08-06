## Naming Conventions




A standardized variable naming convention is used across most tables and fields in the <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> release data. These conventions are adapted from the [ABCD Study](https://docs.abcdstudy.org/latest/documentation/curation/naming.html) and ensure consistency across instruments and derived datasets, allowing for intuitive parsing of variable meaning and structure.

<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">
    Summary
  </span>
</div>
<div class="notification-static-content">
<strong>Naming convention components:</strong> <p style="font-size: 1.2em; font-weight: bold; padding: 10px;">
<code>domain_source_table_<span style="color: teal;">{scale}</span>_item</code>
</p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <th>Component</th>
  <th>Required</th>
  <th>Description</th>
</thead>
<tbody>
<tr>
  <td><b><code>domain</code></b></td>
  <td><i style="color: green;" class="fa-solid fa-check"></i></td>
  <td>Data domain (e.g. biospecimens, imaging)</td>
</tr>
<tr>
  <td><b><code>source</code></b></td>
  <td><i style="color: green;" class="fa-solid fa-check"></i></td>
  <td>Subject/respondent (e.g., child, birth parent)</td>
</tr>
<tr>
  <td><b><code>table</code></b></td>
  <td><i style="color: green;" class="fa-solid fa-check"></i></td>
  <td>Instrument/protocol name</td>
</tr>
<tr>
  <td><b><code><span style="color: teal;">scale</span></code></b></td>
  <td><i style="color: red;" class="fa-solid fa-x"></i></td>
  <td><i>Only if instrument contains multiple scales</i></td>
</tr>
<tr>
  <td><b><code>item</code></b></td>
  <td><i style="color: green;" class="fa-solid fa-check"></i></td>
  <td>Item number, score label, or admin field</td>
</tr>
</tbody>
</table>
<strong>Additional Logic:</strong>
<ul>
    <li>Underscore ( <code>_</code> ) separates main components</li>
    <li>Double/triple underscores ( <code>__</code> ,  <code>___</code> ) separate nested subcomponents</li>
</ul>
<strong>For full component definitions, see details below</strong>
</div>

### Primary Components
The standard variable naming format is comprised of 4 or 5 main components separated by a single underscore ( `_` ): 

 <p style="font-size: 1.8em; font-weight: bold; padding: 10px;" align="center">
<code>domain_source_table_<span style="color: teal;">{scale}</span>_item</code>
</p>

Double ( `__` ) or triple ( `___` ) underscores are used for nesting `table`, `scale`, and/or `item` *subcomponents*, [described below](#subcomponents). Note that variables names will only include the <code><span style="color: teal;">scale</span></code> component if the instrument is composed of multiple scales. 

#### Domain

The `domain` component is an expanded version of <a href="#data-dictionary">NBDC Data Dictionary</a> domains that includes additional options (e.g. Biosensors).

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
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
    <tr><td><code>par</code></td><td style="word-wrap: break-word; white-space: normal;">Participant Information. <i>Note: this is an additional domain not included in NBDC Data Dictionary domains, e.g. <code>par_visit_data</code> (Visit Information), containing dynamic/longitudinal visit-level data, falls under the DD domain <code>Demographics</code></td></tr>
  </tbody>
</table>

#### Source

The `source` component corresponds with <code>source</code> in <a href="#data-dictionary">NBDC Data Dictionary</a> and indicates either the subject (who the protocol element is about) or respondent (who completed the assessment).

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
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

#### Table

Table corresponds to the specific instrument name or protocol element. The values vary by instrument - please refer to the data dictionary.

#### Scale

The <b><code><span style="color: teal;">scale</span></code></b> naming component is the name of a scale within the instrument/protocol element. With the exception of administrative variables <span class="tooltip"><span class="emoji"><i class="fa-solid fa-circle-info"></i></span><span class="tooltiptext">e.g. language or date of administration</span></span>, <b>only variables of instruments with multiple scales contain the <code><span style="color: teal;">scale</span></code> component</b> (<i><a href="#scale">see details</a></i>).

In future releases, scales will use a hyphen (<code>-</code>) instead of a single underscore ( <code>_</code> ) before the scale name. This change ensures all variables have the same number of naming components, making it easier to distinguish main components without needing prior knowledge of whether an instrument contains multiple scales.

<div id="scale" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span style="display: inline-flex; align-items: center;">Scale Details</span>
  <a class="anchor-link" href="#scale" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Study instruments/tables composed of multiple scales will include the <code><span style="color: teal;">{scale}</span></code> naming component in their variable names. This is applicable to the following instruments in the current release:</p>
<br>
<br>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 5%; padding-right: 2px;">Domain</th>
      <th style="width: 30%; padding-right: 2px;">Instrument</th>
      <th style="width: 30%; padding-left: 2px; padding-right: 2px;">Table Name</th>
      <th style="width: 10%; padding-left: 2px;">Example Variable</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="tooltip tooltip-right">BCGI<span class="tooltiptext">Behavior & Child-Caregiver Interaction</span></span></td>
      <td><a href="../../instruments/bcgi/ibqr" target="_blank">IBQ-R (VSF)+BI</a></td>
      <td style="padding-left: 2px; padding-right: 2px;"><code>mh_cg_ibqr</code></td>
      <td style="padding-left: 2px;"><code>mh_cg_ibqr_<span style="color: teal;">beh</span>_001</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right">NCL<span class="tooltiptext">Neurocognition & Language</span></span></td>
      <td><a href="../../instruments/neurocog/spm2" target="_blank">SPM-2</a></td>
      <td style="padding-left: 2px; padding-right: 2px;"><code>ncl_cg_spm2__inf</code></td>
      <td style="padding-left: 2px;"><code>ncl_cg_spm2__inf_<span style="color: teal;">soc</span>_001</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right">PH<span class="tooltiptext">Physical Health</span></span></td>
      <td><a href="../../instruments/physhealth/growth" target="_blank">Growth</a></td>
      <td style="padding-left: 2px; padding-right: 2px;"><code>ph_ch_anthro</code></td>
      <td style="padding-left: 2px;"><code>ph_ch_anthro_<span style="color: teal;">head</span>_001__01</code></td>
    </tr>
    <tr>
      <td rowspan="5"><span class="tooltip tooltip-right">PEX<span class="tooltiptext">Pregnancy & Exposure, Including Substance Use</span></span></td>
      <td style="word-wrap: break-word; white-space: normal;"><a href="../../instruments/#pregexp" target="_blank">Pregnancy Health</a> (ALL),<br>e.g. Healthhx:</td>
      <td style="padding-left: 2px; padding-right: 2px; word-wrap: break-word; white-space: normal;"><code>pex_bm_health_preg__healthhx</code></td>
      <td style="padding-left: 2px; word-wrap: break-word; white-space: normal;"><code>pex_bm_health_<span style="color: teal;">preg__healthhx__preghx</span>_001__01</code></td>
    </tr>
    <tr>
      <td><a href="../../instruments/pregexp/preghealth/end-preg/" target="_blank">Preg Health V2</a></td>
      <td style="padding-left: 2px; padding-right: 2px;"><code>pex_bm_healthv2_preg</code></td>
      <td style="padding-left: 2px;"><code>pex_bm_healthv2_<span style="color: teal;">preg__exp__vacc</span>_018___0</code></td>
    </tr>
    <tr>
      <td><a href="../../instruments/pregexp/preghealth/infanthealth/" target="_blank">Infant Health V2</a></td>
      <td style="padding-left: 2px; padding-right: 2px;"><code>pex_bm_healthv2_inf</code></td>
      <td style="padding-left: 2px;"><code>pex_bm_healthv2_<span style="color: teal;">inf</span>_001__00</code></td>
    </tr>
    <tr>
      <td><a href="../../instruments/pregexp/mh/fam-mh" target="_blank">FAM MH</a></td>
      <td style="padding-left: 2px; padding-right: 2px;"><code>pex_bm_psych</code></td>
      <td style="padding-left: 2px;"><code>pex_bm_psych_<span style="color: teal;">bf</span>_001</code></td>
    </tr>
    <tr>
      <td><a href="../../instruments/pregexp/su/assist" target="_blank">ASSIST V1/2/3</a></td>
      <td style="padding-left: 2px; padding-right: 2px;"><code>pex_bm_assistv1</code></td>
      <td style="padding-left: 2px;"><code>pex_bm_assistv1_<span style="color: teal;">lt__use</span>_001</code></td>
    </tr>
    <tr>
      <td rowspan="3"><span class="tooltip tooltip-right">SED<span class="tooltiptext">Social & Environmental Determinants</span></span></td>
      <td><a href="../../instruments/SED/bfy" target="_blank">BFY</a></td>
      <td style="padding-left: 2px; padding-right: 2px;"><code>sed_bm_bfy</code></td>
      <td style="padding-left: 2px;"><code>sed_bm_bfy_<span style="color: teal;">econstr</span>_001</code></td>
    </tr>
    <tr>
      <td><a href="../../instruments/SED/v01-demo" target="_blank">Demographics</a></td>
      <td style="padding-left: 2px; padding-right: 2px;"><code>sed_bm_demo</code></td>
      <td style="padding-left: 2px;"><code>sed_bm_demo_<span style="color: teal;">residence</span>_001</code></td>
    </tr>
     <tr>
      <td><a href="../../instruments/SED/promis" target="_blank">PROMIS</a></td>
      <td style="padding-left: 2px; padding-right: 2px;"><code>sed_bm_strsup</code></td>
      <td style="padding-left: 2px;"><code>sed_bm_strsup_<span style="color: teal;">socspprt</span>_001</code></td>
    </tr>
  </tbody>
</table>
<p>
</p>
</div>

#### Item

The `item` component will be one of the following:

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <th></th>
  <th>Example Values</th>
</thead>
<tbody>
<tr>
  <td>
  1) <b>Scale item</b>: a 3-digit number corresponding to individual questions in a scale<br>
  2) <b>Score label</b> for individual items in a table<br>
  3) <b>Administrative label</b> for administrative variables <span class="tooltip"><span class="emoji"><i class="fa-solid fa-circle-info"></i></span><span class="tooltiptext">e.g. language or date of administration</span></span><br></td>
  <td>
  1) <code>001</code>; <code>001__01</code>; etc<br>
  2) <code>score</code>; <code>total_score</code>; etc.<br>
  3) <code>administration</code>; <code>location</code>; <span class="tooltip tooltip-left">etc.<span class="tooltiptext"><code>lang</code>; <code>date_taken</code>; <code>candidate_age</code>; <code>gestational_age</code>; <code>adjusted_age</code></span></span><br><br>
  </td></tr>
</tr>
</tbody>
</table>


### Subcomponents

The `table`, <code><span style="color: teal;">scale</span></code>, and `item` components can have additional subcomponents separated by **double ( `__` ) or triple ( `___` ) underscores** to indicate nesting within the main components. Subcomponents distinguish finer details such as **subscales**, **versions**, or **counter types** within a given table or field.

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
