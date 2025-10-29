## latest

<div id="eeg-alt" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-bolt"></i></span>
  <span class="text-with-link">
  <span class="text">EEG-ALT</span>
  <a class="anchor-link" href="#eeg-alt" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><i class="fas fa-folder-open"></i> <b>FILE-BASED DATA</b><br>
File-based EEG data for all tasks includes <a href="eeg/#rawbids" target="_blank">raw BIDS</a> (<code>eeg/</code> folders) and processed <a href="eeg/#made" target="_blank">HBCD-MADE</a> pipeline derivatives.</p>
<p><i class="fa-solid fa-table"></i> <b>TABULATED DATA</b></p>
<p style="font-size: 0.9em; color: #555;">
<i style="color: teal;" class="fa-solid fa-diagram-project"></i>&nbsp;= Pipeline derivatives in tabulated format (<i><a href="../datacuration/overview/#warning" target="_blank">see details</a></i>)
</p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Table</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="eeg/qc" target="_blank">Quality Control Metrics</a> (capping quality, artifacts, etc.)</td>
  <td><code>eeg_qc_task-<span class="blue-text">&lt;MMN|FACE|RS|VEP&gt;</span></code></td>
</tr>
<tr>
<td><i style="color: teal;" class="fa-solid fa-diagram-project"></i> HBCD-MADE Preprocessing Reports (HBCD tabulated format)</td>
<td><code>eeg_made_task-<span class="blue-text">&lt;MMN|FACE|RS|VEP&gt;</span>_acq-eeg_preprocessingReport</code></td>
</tr>
<tr>
<td><i style="color: teal;" class="fa-solid fa-diagram-project"></i> HBCD-MADE ERP Summary Statistics (HBCD tabulated format)</td>
<td><code>eeg_made_task-<span class="blue-text">&lt;MMN|FACE|VEP&gt;</span>_acq-eeg_ERPSummaryStats</code></td>
</tr>
<tr>
</tbody>
</table>
<div style="margin-top: 8px; font-size: 0.9em; background-color: #f9f9f9; border-left: 4px solid #ccc; padding: 6px 10px; border-radius: 6px;">
  <b><i class="fa-solid fa-key"></i> Task Key:</b><br>
  <code>MMN</code>: Auditory Mismatch Negativity &nbsp;&nbsp;|&nbsp;&nbsp;
  <code>FACE</code>: Faces &nbsp;&nbsp;|&nbsp;&nbsp;
  <code>RS</code>: Video Resting State &nbsp;&nbsp;|&nbsp;&nbsp;
  <code>VEP</code>: Visual Evoked Potential
</div>
</div>



<p>EEG tasks include:</a>
<ul>
<li>Auditory Mismatch Negativity (<a href="eeg/mmn" target="_blank">MMN</a>)</li>
<li>Faces (<a href="eeg/face" target="_blank">FACE</a>)</li>
<li>Video Resting State (<a href="eeg/rs" target="_blank">RS</a>)</li>
<li>Visual Evoked Potential (<a href="eeg/vep" target="_blank">VEP</a>)</li>
</ul>







## EEG DRAFT

<p style="font-size: 0.9em; color: #555;">
<i style="color: teal;" class="fa-solid fa-diagram-project"></i>&nbsp;= Pipeline derivatives in tabulated format
</p>

<p><i class="fas fa-folder-open"></i> <b>FILE-BASED DATA</b></p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tfoot>
<tr>
  <td colspan="4" style="word-wrap: break-word; white-space: normal; border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
    <sup><b>1</b></sup> Whenever possible, pipeline derivatives are also provided in the HBCD tabulated format to match other instruments - <a href="../datacuration/overview/#warning" target="_blank">see details</a>
  </td>
</tr>
</tfoot>
<thead>
<tr>
  <th>Task</th>
  <th>Raw BIDS</th>
  <th>Pipeline Derivatives</th>
  <th>Tabulated Derivatives<sup><b>1</b></sup></th>
</tr>
</thead>
<tbody>
<tr>
<td><i style="color: teal;" class="fa-solid fa-diagram-project"></i>&nbsp; All Tasks</td>
<td><code>eeg/</code></td>
<td><a href="eeg/#made" target="_blank">HBCD-MADE</a></td>
<td><code>eeg_made_task-<span class="blue-text">&lt;MMN|FACE|RS|VEP&gt;</span>_acq-eeg_preprocessingReport</code><br>
    <code>eeg_made_task-<span class="blue-text">&lt;MMN|FACE|VEP&gt;</span>_acq-eeg_ERPSummaryStats</code>
</td>
</tr>
<tr>
  <td>All Tasks</td>
  <td colspan="2"><i>NA</i> - EEG Quality Control Metrics</td>
  <td><code>eeg_qc_task-<span class="blue-text">&lt;MMN|FACE|RS|VEP&gt;</span></code></td>
</tr>
</tbody>
</table>

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Task</th>
  <th>Instrument</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td>All Tasks</td>
  <td>EEG QC</td>
  <td>EEG QC</td>
  <td><code>eeg_qc_task-&lt;TASK&gt;</code></td>
</tr>
</tbody>
</table>


## EEG FINAL 

<p><i class="fas fa-folder-open"></i> <b>FILE-BASED DATA</b></p>
File-based EEG data for all tasks includes <a href="eeg/#rawbids" target="_blank">raw BIDS</a> (under subject/session-level `eeg/` folders) and derivatives processed through the <a href="eeg/#made" target="_blank">HBCD-MADE</a> pipeline.

<p><i class="fa-solid fa-table"></i> <b>TABULATED DATA</b></p>
<p style="font-size: 0.9em; color: #555;">
<i style="color: teal;" class="fa-solid fa-diagram-project"></i>&nbsp;= HBCD-MADE pipeline derivatives in tabulated format for a given task
</p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
<th>Table</th>
<th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Raw data QC (capping quality, StimTracker artifact, etc.)</td>
  <td><code>eeg_qc_task-&lt;TASK&gt;</code></td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">
    <i style="color: teal;" class="fa-solid fa-diagram-project"></i> Auditory Mismatch Negativity (<a href="eeg/mmn" target="_blank">MMN</a>) Task:  HBCD-MADE outputs</td>
  <td><code>eeg_made_task-MMN_acq-eeg_preprocessingReport</code><br>
    <code>eeg_made_task-MMN_acq-eeg_ERPSummaryStats</code>
</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">
    <i style="color: teal;" class="fa-solid fa-diagram-project"></i> <a href="eeg/faces" target="_blank">Face</a> Task: HBCD-MADE outputs</td>
  <td><code>eeg_made_task-FACE_acq-eeg_preprocessingReport</code><br>
    <code>eeg_made_task-FACE_acq-eeg_ERPSummaryStats</code>
</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">
    <i style="color: teal;" class="fa-solid fa-diagram-project"></i> Video Resting State (<a href="eeg/videors" target="_blank">RS</a>): HBCD-MADE outputs</td>
  <td><code>eeg_made_task-RS_acq-eeg_preprocessingReport</code>
</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">
    <i style="color: teal;" class="fa-solid fa-diagram-project"></i> Visual Evoked Potential (<a href="eeg/vep" target="_blank">VEP</a>) Task: HBCD-MADE outputs</td>
  <td><code>eeg_made_task-VEP_acq-eeg_preprocessingReport</code><br>
    <code>eeg_made_task-VEP_acq-eeg_ERPSummaryStats</code>
</td>
</tr>
</tbody>
</table>





<br>


<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th>EEG Task</th>
      <th><span class="tooltip tooltip-bottom"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name / <span class="tooltip tooltip-left"><i class="fa-solid fa-folder-open"></i><span class="tooltiptext">File-Based Data</span></span> Folder</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="eeg/mmn" target="_blank">Auditory Mismatch Negativity (MMN)</a></td>
      <td><code>eeg_made_task-MMN_acq-eeg_preprocessingReport</code><br><code>eeg_made_task-MMN_acq-eeg_ERPSummaryStats</code><br><code>eeg_qc_task-MMN</code></td>
    </tr>
    <tr>
      <td><a href="eeg/faces" target="_blank">Faces (Face)</a></td>
      <td><code>eeg_made_task-FACE_acq-eeg_preprocessingReport</code><br><code>eeg_made_task-FACE_acq-eeg_ERPSummaryStats</code><br><code>eeg_qc_task-FACE</code></td>
    </tr>
    <tr>
      <td><a href="eeg/videors" target="_blank">Video Resting State (RS)</a></td>
      <td><code>eeg_made_task-RS_acq-eeg_preprocessingReport</code><br><code>eeg_qc_task-RS</code></td>
    </tr>
    <tr>
      <td><a href="eeg/vep" target="_blank">Visual Evoked Potential (VEP)</a></td>
      <td><code>eeg_made_task-VEP_acq-eeg_preprocessingReport</code><br><code>eeg_made_task-VEP_acq-eeg_ERPSummaryStats</code><br><code>eeg_qc_task-VEP</code></td>
    </tr>
  </tbody>
</table>


