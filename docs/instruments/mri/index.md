# Overview

HBCD includes the following magnetic resonance imaging (**MRI**) and spectroscopy (**MRS**) data acquired as part of a comprehensive pediatric neuroimaging protocol, meticulously designed to overcome technical challenges of imaging early in life. All modalities are acquired during visits V02, V03, V04, and V06.

<table class="table-no-vertical-lines">
  <thead>
    <tr>
      <th>Modality</th><th>Acronym</th><th>Documentation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Structural MRI</td><td>sMRI</td><td><a href="smri" target="_blank">View README</a></td>
    </tr>
        <tr>
      <td>Quantitative MRI</td>      <td>qMRI</td>      <td><a href="qmri" target="_blank">View README</a></td>
    </tr>
         <tr>      <td>Functional MRI</td>      <td>fMRI</td>      <td><a href="fmri" target="_blank">View README</a></td>
    </tr>
    <tr>
      <td>Diffusion MRI</td>      <td>dMRI</td>      <td><a href="dmri" target="_blank">View README</a></td>
    </tr>
    <tr>
      <td>Magnetic Resonance Spectroscopy</td>      <td>MRS</td>      <td><a href="mrs" target="_blank">View README</a></td>
    </tr>
  </tbody>
</table>

## Release Data

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">Please review the <a href="https://docs.hbcdstudy.org/latest/changelog/issues-updates/" target="_blank">Known Issues & Pending Updates</a> page for updates that may affect data use.</span>
</div>
<p></p>

MRI and MRS release data include the following - <i>see <a href="../../datacuration/overview" target="_blank">Data Structure Overview</a> for explanation of these data types</i>:

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b><i class="fas fa-hammer header-icon"></i> Raw BIDS</b></td>
<td>File-based data in modality-specific formats under subject- and session-specific <code>rawdata/</code> folders</td></tr>
<tr><td><b><i class="fas fa-cog header-icon"></i> Derivatives</b></td>
<td>File-based data in modality-specific formats processed through <a href="../processing" target="_blank">HBCD pipelines</a></td></tr>
<tr><td><b><i class="fas fa-table header-icon"></i> Tabulated Data</b></td>
<td style="word-wrap: break-word; white-space: normal;">Questionnaires and select pipeline derivatives in HBCD-tabulated format - see <a href="../#mri-tab" target="_blank">Tabulated Imaging</a></td></tr>
</tbody></table>


<pre class="folder-tree">
hbcd/
├── rawdata/
│   ├── phenotype/  
│   │   <span class="hashtag"># Tabulated data (forms, questionnaires, and pipeline-derived tables)</span>
│   │   ├── mri_ra_prep           <span class="hashtag"># Pre/post scan preparation</span>
│   │   ├── img_brainswipes_*     <span class="hashtag"># BrainSwipes QC</span>
│   │   ├── img_mriqc_*           <span class="hashtag"># MRIQC outputs (tabulated)</span>
│   │   ├── img_bibsnet_*         <span class="hashtag"># BIBSNet outputs (tabulated)</span>
│   │   ├── img_xcpd_*            <span class="hashtag"># XCP-D outputs (tabulated)</span>
│   │   └── img_osprey_*          <span class="hashtag"># OSPREY (MRS) outputs (tabulated)</span>
│   │
│   └── sub-<span class="label">{ID}</span>/  
│       <span class="hashtag"># Raw BIDS imaging data (file-based)</span>
│       └── ses-<span class="label">{V0X}</span>/
│           ├── anat/             <span class="hashtag"># Structural/qMRI + MRS localizers</span>
│           ├── dwi/              <span class="hashtag"># Diffusion MRI</span>
│           ├── fmap/             <span class="hashtag"># fMRI + qMRI fieldmaps</span>
│           ├── func/             <span class="hashtag"># Functional MRI</span>
│           └── mrs/              <span class="hashtag"># Spectroscopy</span>
│
└── derivatives/
    <span class="hashtag"># Processed pipeline outputs (file-based, modality-specific)</span>
    │
    │ <span class="hashtag"># Structural & functional pipelines</span>
    ├── mriqc/
    ├── bme_x/
    ├── bibsnet/
    ├── nibabies/
    ├── freesurfer/
    ├── mcribs/
    ├── xcp_d/
    │   
    │ <span class="hashtag"># Quantitative MRI</span>
    ├── symri/
    ├── qmri_postproc/
    │
    │ <span class="hashtag"># Diffusion MRI</span>
    ├── qsiprep/
    ├── qsirecon/
    ├── qsirecon-DSIStudio/
    ├── qsirecon-DIPYDKI/
    ├── qsirecon-TORTOISE_model-MAPMRI/
    ├── qsirecon-TORTOISE_model-tensor/
    │
    │ <span class="hashtag"># MRS</span>
    └── osprey/
</pre>

## MRI Protocols

HBCD Study MRI protocols and acquisition parameters are described in <a href="https://doi.org/10.1016/j.dcn.2024.101452">Dean et al. 2024</a>. See the external [HBCD Study MRI Protocols](https://hbcdsequences.readthedocs.io) documentation for full protocols, sequence installation, and operation instructions.


## Exclusion Criteria

### Raw BIDS Data
Acquisition parameters must fall within the ranges specified below in order for data to be included in the release. Inclusion criteria are typically defined as acceptable ranges rather than fixed values due to variations between scanner types. The following values are extracted from BIDS JSON metadata.

<div id="exclusion-criteria-rawbids" class="table-banner" onclick="toggleCollapse(this)"> <span class="emoji"><i class="fa fa-circle-check"></i></span> <span class="text-with-link"> <span class="text">Acquisition Parameter Ranges for Data Release Eligibility</span> <a class="anchor-link" href="#exclusion-criteria-rawbids" title="Copy link"> <i class="fa-solid fa-link"></i> </a> </span> <span class="arrow">▸</span> </div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
  <thead><tr> <th>Scan Type</th> <th>Repetition Time (TR)</th><th>Echo Time (TE)</th><th>Inversion Time (TI)</th><th>Slice Thickness</th><th>Number of Volumes</th></tr></thead>
<tbody>
<tr>
  <td>T1w</td>  <td>2.3 - 2.41</td><td>0.002 - 0.0035</td>  <td>1.06 - 1.1</td><td>0.8</td><td>NA</td>    
  </tr>  <tr><td>T2w</td><td>2.5 - 4.5</td><td>0.09 - 0.15</td><td>0.29 - 0.33</td><td>0.563 - 0.565</td><td>NA</td>  </tr>  
  <tr><td>MRS Localizer</td><td>2.5 - 4.5</td><td>0.09 - 0.15</td><td>0.29 - 0.33</td><td>0.563 - 0.565</td><td>NA</td>  </tr>   
  <tr><td>Diffusion</td><td>4.8</td><td>0.0880 - 0.0980</td><td>NA</td><td>1.7</td><td>≥ 90 (AP + PA)</td>    </tr>  
  <tr><td>EPI Fieldmap</td><td>8.4 - 9.2</td><td>0.064 - 0.0661</td><td>2</td><td>0.563 - 0.565</td><td>NA</td>  </tr>  
  <tr><td>Functional</td><td>1.725</td><td>0.0369 - 0.0371</td><td>NA</td><td>2</td><td>≥ 87 (~2.5 min)</td>     </tr>  
</tbody>
</table>
</div>

### Processed Derivatives

Structural and functional MRI derivatives with an average <a href="../qc/#brainswipes/" target="_blank">BrainSwipes</a> QC score < 0.5 were flagged for expert manual review; data with severe QC issues were excluded from release data. V02 sessions processed using Infant FreeSurfer (`hash-2afa9081`) for surface reconstruction were only partially evaluated - <a href="mri-proc/#warning">see Data Warning</a>.

<div id="manual-review" class="table-banner" onclick="toggleCollapse(this)"> <span class="emoji"><i class="fa fa-circle-check"></i></span> <span class="text-with-link"> <span class="text">Details: Expert Manual Review</span> <a class="anchor-link" href="#manual-review" title="Copy link"> <i class="fa-solid fa-link"></i> </a> </span> <span class="arrow">▸</span> </div>
<div class="table-collapsible-content">
<p>The table below reports the percentage of session folders removed due to structural or functional QC failures for each visit.</p>
<table class="table-no-vertical-lines">
<tfoot><tr><td colspan="5"><b>*</b> Structural QC passed; one or more BOLD runs failed QC</td></tr></tfoot>
<thead>
<tr><th>Visit</th><th>Surface Reconstruction Workflow</th><th>Structural Exclusions (%)</th><th>Functional Exclusions (%)*</th><th>Total</th></tr>
</thead>
<tbody>
<tr><td>V02</td><td>M-CRIB-S</td><td>3%</td><td>16%</td><td>19%</td></tr><tr><td>V02</td><td>Infant FreeSurfer</td><td>19%</td><td>30%</td><td>49%</td></tr><tr><td>V03</td><td>Infant FreeSurfer</td><td>3%</td><td>3%</td><td>6%</td></tr><tr><td>V04</td><td>Infant FreeSurfer</td><td>0%</td><td>3%</td><td>3%</td></tr>
</tbody></table>
</div> 
