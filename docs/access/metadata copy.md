


### Field Names

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <th></th>
  <th style="width: 50%;">Definition</th>
  <th style="width: 50%;">Example Values <span class="tooltip tooltip-left"><span class="emoji"><i class="fa-solid fa-circle-info"></i></span><span class="tooltiptext" style="font-size: 0.9em;">for tables provided in the current release only</span></span>
</thead>
<tbody>
<tr>
  <td><b><code>scale</code></b></td>
  <td>Name of scale or subscale within instrument/protocol element</td>
  <td><span class="tooltip"><code>herit</code><span class="tooltiptext">heritage information</span></span>;
  <span class="tooltip"><code>lang</code><span class="tooltiptext">languages spoken</span></span>;
  <span class="tooltip"><code>administration</code><span class="tooltiptext">instrument administration</span></span>; etc.
  </td>
</tr>
</tbody>
</table>


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
<li><strong><a href="../../instruments/#mri">MRI & MRS</a> and <a href="../../instruments/#eeg">EEG</a></strong> <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> data derived from <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> sources. These are clearly associated with their respective domains (e.g., MRI, EEG) and pertain exclusively to the Child.</li>
<li><strong>Derived tables</strong>: including Basic Demographics (<code>sed_basic_demographics</code>, containing global, static variables) and Visit Information (<code>par_visit_data</code>, containing dynamic/longitudinal visit-level data) - <a href="../../instruments/#demo">see details</a>.</li>
</div>


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





## NOTES

For example, <code>img_ra_prep</code> would refer to MRI-related data entered by an <span class="tooltip">RA<span class="tooltiptext">research assistant</span></span>, representing procedural details as opposed to direct input from a child or caregiver.

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
<li><strong><a href="../../instruments/#mri">MRI & MRS</a> and <a href="../../instruments/#eeg">EEG</a></strong> <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> data derived from <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> sources. These are clearly associated with their respective domains (e.g., MRI, EEG) and pertain exclusively to the Child.</li>
<li><strong>Derived tables</strong>: including Basic Demographics (<code>sed_basic_demographics</code>, containing global, static variables) and Visit Information (<code>par_visit_data</code>, containing dynamic/longitudinal visit-level data) - <a href="../../instruments/#demo">see details</a>.</li>
</div>