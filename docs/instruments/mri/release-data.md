# MR Release Data
{{ issues_banner() }}

---

MRI and MRS release data includes:

- **[Raw BIDS](#raw-mr-bids)**: Raw imaging/spectroscopy data in the standardized BIDS format
- **[Derivatives](#derivatives)**: Processed, analysis-ready imaging/spectroscopy pipeline outputs
- **[Tabular Imaging](../index.md#imaging-tabular-imaging)**: Questionnaires, technician forms from scan session, and tabulated pipeline derivatives

---

## Raw MR BIDS

<div id="bids-conversion" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fas fa-arrows-rotate"></i>
</span>
<span class="text-with-link">
    <span class="text">BIDS Conversion Procedures</span>
    <a class="anchor-link" href="#bids-conversion" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>For MRI, DICOM images are converted using an HBCD-customized version of <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a>. For MRS, vendor-specific formats (Siemens `.dat`, Philips data/list, GE P-file) are converted using <a href="https://github.com/DCAN-Labs/hbcd_mrs_to_nii_conversion">spec2nii v0.7.0</a>. Additional post-processing is performed for MRI to ensure consistency across vendors. This includes converting QALAS to five 3D NIfTI files (labeled by inversion time) and hardcoding missing or inconsistent metadata fields for various modalities as follows:</p>
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
    <tr><td><code>{Small|Large}Delta</code></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td></td> <td></td><td></td><td></td></tr>
    <tr><td><code>RepetitionTime</code></td> <td></td> <td></td> <td></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td></td>    </tr>
      <tr>      <td><code>T2Prep</code></td><td></td> <td></td> <td></td> <td></td> <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>      <tr><td><code>InversionTime</code></td><td></td><td></td><td></td><td></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>    </tr>
  </tbody>
</table>
</div>

<div id="acquisition-criteria" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
<i class="fa-solid fa-asterisk"></i>
</span>
<span class="text-with-link">
  <span class="text">Acquisition Criteria</span>
  <a class="anchor-link" href="#acquisition-criteria" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Acquisition specs, extracted post-BIDS conversion from JSON metadata, must fall within the ranges specified below in order to be included in the release or any downstream pipeline processing. Note that inclusion criteria are typically defined as acceptable ranges rather than fixed values due to variations between scanner types.</p>
<table class="table-no-vertical-lines">
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
<p></p>

Each participant/session folder within `rawdata/` contains raw imaging data organized into modality-specific subfolders (`anat/`, `func/`, etc.), with filenames encoding acquisition details (task, direction, run, etc.).

<pre class="folder-tree">
<span><a href="../../../datacuration/overview/#filetrees"><i class="fa fa-circle-info"></i> How To Read File Trees →</a></span>

hbcd/
└── rawdata/
    └── sub-[ID]/
        └── ses-[V0X]/
            ├── anat/
            │   ├── *_<span class="var">{T1w|T2w}</span>.nii.gz                      <span class="hashtag"># Structural MRI T1w & T2w</span>
            │   ├── *_inv-<span class="var">{0-4}</span>_QALAS.nii.gz                <span class="hashtag"># Quantitative MRI (QALAS)</span>
            │   └── *_acq-mrsLoc<span class="var">{Ax|Cor}</span>_run-{X}_T2w.nii.gz <span class="hashtag"># MRS localizers</span>
            │
            ├── func/
            │   └── *_task-rest_dir-PA_run-{X}_bold.nii.gz  <span class="hashtag"># Resting-state fMRI runs</span>
            │
            ├── fmap/
            │   ├── *_dir-<span class="var">{AP|PA}</span>_run-{X}_epi.nii.gz        <span class="hashtag"># fMRI fieldmaps acquired AP/PA for each run</span>
            │   ├── *_acq-<span class="var">{anat|famp}</span>_run-{X}_TB1TFL.nii.gz <span class="hashtag"># qMRI Siemens B1+ fieldmaps</span>
            │   └── *_acq-<span class="var">{tr1|tr2}</span>_run-{X}_TB1AFI.nii.gz   <span class="hashtag"># qMRI GE/Philips B1+ fieldmaps</span>
            │
            ├── dwi/
            │   ├── *_dir-<span class="var">{AP|PA}</span>_run-{X}_dwi.nii.gz        <span class="hashtag"># Diffusion MRI</span>
            │   ├── *_dir-<span class="var">{AP|PA}</span>_run-{X}_dwi.bval
            │   ├── *_dir-<span class="var">{AP|PA}</span>_run-{X}_dwi.bvec
            │   └── *_dir-<span class="var">{AP|PA}</span>_run-{X}_sbref.nii.gz
            │
            └── mrs/ <span class="hashtag"># Acquired via shortTE and HERCULES</span>
                ├── *_acq-<span class="var">{shortTE|hercules}</span>_run-{X}_svs.nii.gz    <span class="hashtag"># Spectroscopy (SVS)</span>
                └── *_acq-<span class="var">{shortTE|hercules}</span>_run-{X}_ref.nii.gz    <span class="hashtag"># Reference scans</span>
</pre>

---

## Derivatives

Processed pipeline outputs are organized under specific folders named by processing pipeline as follows. See modality-specific subpages for details.

<pre class="folder-tree">
hbcd/
└── derivatives/
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

<div id="deriv-exclusions" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Processed Data Exclusion/Removal</span>
  <a class="anchor-link" href="#deriv-exclusions" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>
Structural and functional MRI derivatives with an average BrainSwipes QC score < 0.5 were flagged for expert manual review. Session data with confirmed severe structural issues were excluded from the release, including structural/functional pipelines outlined <a href="../sfmri-processing/#multistep-processing-workflow">here</a>, Osprey (MRS), and qMRI-PostProc. Sessions flagged for functional issues ONLY (at least one severely failing BOLD run) were only removed from Infant fMRIPrep and XCP-D derivatives. </p>
<p><b>Note that V02 sessions processed using Infant FreeSurfer (<code>hash-2afa9081</code>) for surface reconstruction should not be used for analysis - <a href="../fmri/#data-warning">see Data Warning</a>.</b></p>
<p>
The table below reports the percentage of session folders removed due to QC failures for each visit.
</p>
<table class="table-no-vertical-lines">
<tfoot><tr><td colspan="5"><b>*</b> Structural QC passed; one or more BOLD runs failed QC</td></tr></tfoot>
<thead>
<tr><th>Visit</th><th>Surface Reconstruction Workflow</th><th>Structural Exclusions (%)</th><th>Functional Exclusions (%)*</th><th>Total</th></tr>
</thead>
<tbody>
<tr><td>V02</td><td>M-CRIB-S</td><td>3%</td><td>16%</td><td>19%</td></tr><tr><td>V02</td><td>Infant FreeSurfer</td><td>19%</td><td>30%</td><td>49%</td></tr><tr><td>V03</td><td>Infant FreeSurfer</td><td>3%</td><td>3%</td><td>6%</td></tr><tr><td>V04</td><td>Infant FreeSurfer</td><td>0%</td><td>3%</td><td>3%</td></tr>
</tbody></table>
</div>

<!-- 
## Tabular Imaging

The data provided in the Tablar Imaging domain includes forms, questionnaires, and tabulated pipeline derivatives. Tabulated files are listed <a href="../../#imaging-tabular-imaging">here</a> and displayed in BIDS folder structure below:

<pre class="folder-tree">
hbcd/
└── rawdata/
    └── phenotype/  
        ├── mri_ra_prep           <span class="hashtag"># Pre/post scan preparation</span>
        ├── img_brainswipes_*     <span class="hashtag"># BrainSwipes QC</span>
        ├── img_mriqc_*           <span class="hashtag"># MRIQC outputs (tabulated)</span>
        ├── img_bibsnet_*         <span class="hashtag"># BIBSNet outputs (tabulated)</span>
        ├── img_xcpd_*            <span class="hashtag"># XCP-D outputs (tabulated)</span>
        └── img_osprey_*          <span class="hashtag"># OSPREY (MRS) outputs (tabulated)</span>
</pre>

--- -->
