# Overview

HBCD includes the following magnetic resonance imaging (**MRI**) and spectroscopy (**MRS**) data acquired as part of a comprehensive pediatric neuroimaging protocol, meticulously designed to overcome technical challenges of imaging early in life. All modalities are acquired during visits V02, V03, V04, and V06.

<style>
.toc-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  gap: 0.1rem;
}
.toc-card {
  display: block;
  padding: 1rem;
  border-radius: 12px;
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  text-decoration: none;
  transition: all 0.2s ease;
}
.toc-card:hover {
  transform: translateY(-2px);
  border-color: var(--md-primary-fg-color);
}
.toc-title {font-weight: 600;}
.toc-sub {font-size: 0.9em; opacity: 0.7;}
</style>

<div class="toc-grid">
<a href="smri" class="toc-card"><div class="toc-title">Structural MRI</div><div class="toc-sub">sMRI</div></a>
<a href="qmri" class="toc-card"><div class="toc-title">Quantitative MRI</div><div class="toc-sub">qMRI</div></a>
<a href="fmri" class="toc-card"><div class="toc-title">Functional MRI</div><div class="toc-sub">fMRI</div></a>
<a href="dmri" class="toc-card"><div class="toc-title">Diffusion MRI</div><div class="toc-sub">dMRI</div></a>
<a href="mrs" class="toc-card"><div class="toc-title">MR Spectroscopy</div><div class="toc-sub">MRS</div></a>
</div>

<!-- <table class="table-no-vertical-lines">
<tbody>
<tr><td><a href="smri" target="_blank">Structural MRI (sMRI)</a></td></tr>
<tr><td><a href="qmri" target="_blank">Quantitative MRI (qMRI)</a></td></tr>
<tr><td><a href="fmri" target="_blank">Functional MRI (fMRI)</a></td></tr>
<tr><td><a href="dmri" target="_blank">Diffusion MRI (dMRI)</a></td></tr>
<tr><td><a href="mrs" target="_blank">Magnetic Resonance Spectroscopy (MRS)</a></td></tr>
</tbody></table> -->

 <!-- - <a href="smri" target="_blank">Structural MRI (sMRI)</a>
 - <a href="qmri" target="_blank">Quantitative MRI (qMRI)</a>
 - <a href="fmri" target="_blank">Functional MRI (fMRI)</a>
 - <a href="dmri" target="_blank">Diffusion MRI (dMRI)</a>
 - <a href="mrs" target="_blank">Magnetic Resonance Spectroscopy (MRS)</a> -->

## MRI Protocols
HBCD Study MRI protocols and acquisition parameters are described in <a href="https://doi.org/10.1016/j.dcn.2024.101452">Dean et al. 2024</a>. See the external [HBCD Study MRI Protocols](https://hbcdsequences.readthedocs.io) documentation for full protocols, sequence installation, and operation instructions.

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

## Raw MR BIDS
Each participant/session folder within `rawdata/` contains raw imaging data organized into modality-specific subfolders (e.g., `anat/`, `func/`, `dwi/`), with filenames encoding acquisition details (task, direction, run, etc.). See <a href="../../../datacuration/file-based-data/#raw-bids" target="_blank">File-Based Data</a> for a general introduction to BIDS.

<div id="bids-conversion" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span><span class="text-with-link"><span class="text">BIDS Conversion Procedures</span>
  <a class="anchor-link" href="#bids-conversion" title="Copy link"><i class="fa-solid fa-link"></i></a></span><span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>For MRI, DICOM images are converted using an HBCD-customized version of <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a>. For MRS, vendor-specific formats (Siemens <code>.dat</code>, Philips data/list, GE P-file) are converted using <a href="https://github.com/DCAN-Labs/hbcd_mrs_to_nii_conversion">spec2nii v0.7.0</a>.</p>
<p>Additional post-processing is performed for MRI to ensure consistency across vendors. This includes converting QALAS to five 3D NIfTI files (labeled by inversion time) and hardcoding missing or inconsistent metadata fields for various modalities as follows:</p>
<table class="compact-table-no-vertical-lines">
  <thead>
    <tr>
      <th>Field</th>
      <th>DWI <span style="font-weight:normal;">(Philips)</span></th>
      <th>EPI <span style="font-weight:normal;">(Philips)</span></th>
      <th>BOLD <span style="font-weight:normal;">(Philips)</span></th>
      <th>T1w <span style="font-weight:normal;">(Philips & GE)</span></th>
      <th>QALAS <span style="font-weight:normal;">(Philips, Siemens, GE)</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>PhaseEncodingDirection</code></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td></td> <td></td>
    </tr>
    <tr>
      <td><code>TotalReadoutTime</code></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td></td> <td></td>
    </tr>
    <tr><td><code>SliceTiming</code></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td></td> <td></td></tr>
    <tr><td><code>&lt;Small|Large&gt;Delta</code></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td></td> <td></td><td></td><td></td></tr>
    <tr><td><code>RepetitionTime</code></td> <td></td> <td></td> <td></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td></td>    </tr>
      <tr>      <td><code>T2Prep</code></td><td></td> <td></td> <td></td> <td></td> <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>      <tr><td><code>InversionTime</code></td><td></td><td></td><td></td><td></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>    </tr>
  </tbody>
</table>
</div>
<p></p>

<table class="table-no-vertical-lines">
<thead><tr><th>Folder</th><th>Modality</th><th>Key Files</th></tr></thead>
<tbody>
<tr><td rowspan="3"><code>anat/</code></td><td>sMRI</td><td>T1w, T2w</td></tr>
<tr><td>qMRI</td><td>QALAS (<code>inv-0</code> → <code>inv-4</code>) files</td></tr>
<tr><td>MRS</td><td>Localizers (<code>aqc-mrsLocAx</code>, <code>aqc-mrsLocCor</code>)</td></tr>
<tr><td><code>func/</code></td><td>fMRI</td><td>Resting-state BOLD runs</td></tr>
<tr><td rowspan="2"><code>fmap/</code></td><td>fMRI</td>
<td>EPI fieldmap pairs acquired in AP/PA directions for each <code>func/</code> BOLD run</td></tr>
<tr><td>qMRI</td><td>B1+ fieldmaps</td></tr>
<tr><td><code>dwi/</code></td><td>dMRI</td><td>DWI; gradient magnitude/direction (<code>.bval</code>/<code>.bvec</code>); single-band reference images (<code>*_sbref.nii.gz</code>)</li></ul></td></tr>
<tr><td><code>mrs/</code></td><td>MRS</td>
<td style="word-wrap: break-word; white-space: normal;">Metabolite spectra and water reference scans (<code>{svs|ref}.nii.gz</code>), each acquired via short echo time and HERCULES edited spectra (<code>acq-{shortTE|hercules}</code>)</td>
</tr></tbody></table>

#### Raw BIDS Folder Structure

<pre class="folder-tree">
<span><a style="color: white;" href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: white;" class="fa fa-circle-info"></i> How To Read File Trees →</a></span>
<span class="hashtag"># All NIfTI files include sidecar JSON metadata ({FILENAME}.json)</span>
hbcd/
└── rawdata/
    └── sub-{ID}/
        └── ses-{V0X}/
            ├── anat/
            │   ├── *_<span class="placeholder">&lt;T1w|T2w&gt;</span>.nii.gz                      <span class="hashtag"># Structural MRI</span>
            │   ├── *_inv-<span class="placeholder">&lt;0-4&gt;</span>_QALAS.nii.gz                <span class="hashtag"># Quantitative MRI (QALAS)</span>
            │   └── *_acq-mrsLoc<span class="placeholder">&lt;Ax|Cor&gt;</span>_run-{X}_T2w.nii.gz <span class="hashtag"># MRS localizers</span>
            │
            ├── func/
            │   └── *_task-rest_dir-PA_run-{X}_bold.nii.gz  <span class="hashtag"># Resting-state fMRI</span>
            │
            ├── fmap/
            │   ├── *_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-{X}_epi.nii.gz        <span class="hashtag"># fMRI fieldmaps</span>
            │   ├── *_acq-<span class="placeholder">&lt;anat|famp&gt;</span>_run-{X}_TB1TFL.nii.gz <span class="hashtag"># qMRI Siemens B1+ fieldmaps</span>
            │   └── *_acq-<span class="placeholder">&lt;tr1|tr2&gt;</span>_run-{X}_TB1AFI.nii.gz   <span class="hashtag"># qMRI GE/Philips B1+ fieldmaps</span>
            │
            ├── dwi/
            │   ├── *_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-{X}_dwi.nii.gz        <span class="hashtag"># Diffusion MRI</span>
            │   ├── *_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-{X}_dwi.bval
            │   ├── *_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-{X}_dwi.bvec
            │   └── *_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-{X}_sbref.nii.gz
            │
            └── mrs/
                ├── *_acq-<span class="placeholder">&lt;shortTE|hercules&gt;</span>_run-{X}_svs.nii.gz <span class="hashtag"># Spectroscopy (SVS)</span>
                └── *_acq-<span class="placeholder">&lt;shortTE|hercules&gt;</span>_run-{X}_ref.nii.gz <span class="hashtag"># Reference scans</span>
</pre>


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
