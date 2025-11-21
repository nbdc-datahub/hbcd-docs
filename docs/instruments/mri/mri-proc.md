# MRI Processing & Derivatives Guide

Below we describe the processing streams for structural and functional MRI, which are more involved and include multiple pipelines. For a high-level overview of processing across modalities, see <a href="../../processing/">HBCD Processing Pipelines</a>.

## Structural & Functional MRI Processing Overview

<p> <div class="table-banner"> <span class="emoji"><i class="fa-solid fa-circle-info"></i><i class="fa fa-person-cane"></i></span> <span class="text">Full pipeline configuration details are available on the <a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0_dev2/tool_details.html">HBCD Processing site&nbsp;<i style="font-size: 1.0em;" class="fa-solid fa-up-right-from-square"></i></a></span> </div> </p>

HBCD **structural and functional MRI** data are processed through a standardized sequence of BIDS App pipelines. Each pipeline builds on the derivatives from the previous step, as outlined below. 

<style> .pipeline-step { transition: all 0.25s ease; } .pipeline-step:hover { transform: translateY(-3px); box-shadow: 0 4px 10px rgba(100, 100, 255, 0.2); } </style> <div style="display: flex; align-items: center; justify-content: center; gap: 16px; flex-wrap: wrap; font-size: 0.95em;"> <div style="text-align: center;"> <a href="https://bibsnet.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #a9bffcff; border-radius: 12px; background-color: #dde6fe; color: #222;"> <strong>BIBSNet</strong><br> <small>Segmentation & masks</small> </div> </a> </div> <span style="font-size: 20px;"><i class="fa-solid fa-arrow-right"></i></span> <div style="text-align: center;"> <a href="https://nibabies.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #a89df9ff; border-radius: 12px; background-color: #dcd8fb; color: #222;"> <strong>Infant-fMRIPrep</strong><br> <small><i>Surface reconstruction, preprocessing & confounds</i></small> </div> </a> </div> <span style="font-size: 20px;"><i class="fa-solid fa-arrow-right"></i></span> <div style="text-align: center;"> <a href="https://xcp-d.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #d794fcff; border-radius: 12px; background-color: #f0dcfb; color: #222;"> <strong>XCP-D</strong><br> <small>Post-processing & denoising</small> </div> </a> </div> </div>

In brief, BIBSNet performs preprocessing on structural T1w/T2w images to generate brain tissue segmentations and masks. These are fed into Infant-fMRIPrep, which produces minimally pre-processed outputs including confound files and motion-corrected data in age-specific MNI volumetric atlas as well as fs_LR32k surface space. From these outputs, the XCP-D pipeline runs nuisance regression/denoising, parcellates the fMRI data, and computes summary measures.

## BIBSNet
BIBSNet is a deep learning model optimized for infant MRI brain tissue segmentation (<a href="https://doi.org/10.1101/2023.03.22.533696">Hendrickson et al. 2024</a>). The <a href="https://bibsnet.readthedocs.io/en/latest/">BIBSNet pipeline</a> generates native-space brain segmentations and brain masks (as well as <code>volumes.tsv</code> files with ROI volume statistics), which are fed into Infant fMRIPrep for use in anatomical preprocessing and surface reconstruction.

<div id="bibsnet" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">BIBSNet Derivatives (<code>bibsnet/</code>)</span>
  <a class="anchor-link" href="#bibsnet" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ bibsnet/
        |__ sub-<span class="label">{ID}</span>/
            |__ ses-<span class="label">{V0X}</span>/
                |__ anat/
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_dseg.nii.gz <span class="hashtag">(+JSON)</span>
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes.tsv <span class="hashtag">(+JSON)</span>         
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_brain-mask.nii.gz <span class="hashtag">(+JSON)</span>
</pre>
</div>

## Infant fMRIPrep
<a href="https://nibabies.readthedocs.io/en/latest/">Infant-fMRIPrep</a> (also known as NiBabies) adapts <em>fMRIPrep</em> for infant data using age-appropriate templates and two surface reconstruction methods optimized for early development (<a href="https://doi.org/10.1101/2025.05.14.654069">Goncalves et al., 2025</a>). Pipeline outputs from minimal structural and functional MRI processing include visual quality assessment reports, preprocessed derivatives, and confounds to be used for denoising in subsequent processing procedures (<i>see <a href="https://nibabies.readthedocs.io/en/latest/outputs.html">pipeline documentation</a></i>).

<div id="nibabies" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa-solid fa-diagram-project"></i></span>
<span class="text-with-link"><span class="text">Infant fMRIPrep Processing Overview</span>
<a class="anchor-link" href="#nibabies" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
<span class="arrow">▸</span></div>
<div class="table-collapsible-content">
<p><b>Anatomical Preprocessing</b><br>
T1w and T2w images are denoised, bias-corrected, and normalized to the MNI Infant template (0–4.5 yr), then to MNI152 for compatibility with adult datasets. <b><i>Surface reconstruction</i></b> is performed via one of the following methods:</p>
<table class="table-no-vertical-lines">
<tbody>
<tr>
<td><b>M-CRIB-S</b></td>
<td style="word-wrap: break-word; white-space: normal;">T2w-based method for neonates (<a href="https://doi.org/10.1038/s41598-020-61326-2">Adamson et al., 2020</a>). Infant fMRIPrep runs a modified <code>MCRIBReconAll</code> workflow that uses the BIBSNet-derived brain segmentation. <i>Optimal age range per <a href="https://doi.org/10.1101/2025.05.14.654069">Goncalves et al., 2025</a>: ≤ 5 months</i></td>
</tr> <tr>
<td><b>Infant FreeSurfer</b></td>
<td style="word-wrap: break-word; white-space: normal;">T1w-based method for infants 0-2 years old (<a href="https://doi.org/10.1016/j.neuroimage.2020.116946">Zöllei et al., 2020</a>). Infant fMRIPrep executes <code>infant_recon_all</code> with its default configuration. <i>Optimal age range per <a href="https://doi.org/10.1101/2025.05.14.654069">Goncalves et al., 2025</a>: ≥ 3 months</i></td>
</tr> </tbody>
</table>
<p><b>Functional Processing</b></p>
<ul>
  <li>Motion and distortion correction using fieldmap-based estimation.</li>
  <li>Alignment of functional to anatomical space via boundary-based registration.</li>
  <li>Confound estimation: framewise displacement (FD) and DVARS for motion, CompCor physiological noise regressors, global signals (mean CSF, white matter, and whole brain), and derived regressors (e.g. motion outlier flags for frames exceeding 0.5 mm FD or 1.5 standardized DVARS thresholds)</li>
  <li>Resampling of BOLD data to subject and fsLR-space surfaces, with grayordinates (91k) for surface-based analyses.</li>
</ul>
</div>

<div id="nibabies-derivs" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
  <span class="text">Infant fMRIPrep Derivatives (<code>nibabies-&lt;0f306a2f|2afa9081&gt;/</code>)</span>
  <a class="anchor-link" href="#nibabies-derivs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<pre class="folder-tree" style="font-size: 11px;">
hbcd/
|_ derivatives/ 
   |_ nibabies-<span class="placeholder">&lt;HASH&gt;</span>/
      |_ sub-<span class="label">{ID}</span>/
      |  |_ figures/
      |  |_ ses-<span class="label">{V0X}</span>/
      |     |_ log/
      |     |
      |     |_ anat/
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_desc-preproc_T2w.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_from-<span class="placeholder">&lt;MNI&gt;</span>_to-T2w_mode-image_xfm.h5
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_from-T2w_to-<span class="placeholder">&lt;MNI&gt;</span>_mode-image_xfm.h5
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_from-T2w_to-fsnative_mode-image_xfm.txt
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_from-fsnative_to-T2w_mode-image_xfm.txt
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;HEM&gt;</span>_<span class="placeholder">&lt;METRIC&gt;</span>.shape.gii
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;HEM&gt;</span>_<span class="placeholder">&lt;SURF&gt;</span>.surf.gii
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;HEM&gt;</span>_<span class="placeholder">&lt;inflated|sphere&gt;</span>.surf.gii
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;HEM&gt;</span>_space-dhcpAsym_den-32k_<span class="placeholder">&lt;SURF&gt;</span>.surf.gii
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;HEM&gt;</span>_space-<span class="placeholder">&lt;dhcpAsym|fsaverage&gt;</span>_den-32k_sphere.surf.gii
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_desc-brain_mask.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_desc-preproc_T2w.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_space-<span class="placeholder">&lt;SPACE&gt;</span>_dseg.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_space-<span class="placeholder">&lt;SPACE&gt;</span>_label-<span class="placeholder">&lt;CSF|GM|WM&gt;</span>_probseg.nii.gz
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_space-T2w_desc-ribbon_mask.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_space-fsLR_den-91k_<span class="placeholder">&lt;METRIC&gt;</span>.dscalar.nii <span class="hashtag">(+JSON)</span>
      |     |
      |     |_ fmap/
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_fmapid-auto<span class="label">{X}</span>_desc-coeff_fieldmap.nii.gz
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_fmapid-auto<span class="label">{X}</span>_desc-epi_fieldmap.nii.gz
      |     |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_fmapid-auto<span class="label">{X}</span>_desc-preproc_fieldmap.nii.gz <span class="hashtag">(+JSON)</span>
      |     |
      |     |_ func/ <span class="hashtag">(ALL +JSON)</span>
      |        |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_desc-brain_mask.nii.gz
      |        |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_desc-confounds_timeseries.tsv
      |        |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_desc-<span class="placeholder">&lt;coreg|hmc&gt;</span>_boldref.nii.gz
      |        |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_desc-preproc_bold.nii.gz
      |        |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_from-boldref_to-T2w_mode-image_desc-coreg_xfm.txt
      |        |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_from-boldref_to-auto<span class="label">{X}</span>_mode-image_xfm.txt
      |        |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_from-orig_to-boldref_mode-image_desc-hmc_xfm.txt
      |        |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;HEM&gt;</span>_space-fsnative_bold.func.gii
      |        |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-<span class="placeholder">&lt;SPACE&gt;</span>_boldref.nii.gz
      |        |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-<span class="placeholder">&lt;SPACE&gt;</span>_desc-brain_mask.nii.gz
      |        |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-<span class="placeholder">&lt;SPACE&gt;</span>_desc-preproc_bold.nii.gz
      |        |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_bold.dtseries.nii
      |    
      |__ <span class="subses">SUBSES</span>_<span class="placeholder">&lt;HASH&gt;</span>.html

<span class="hashtag"># Label Values Legend</span>
<span class="subses">SUBSES</span>: sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>
<span class="placeholder">HASH</span>: 0f306a2f | 2afa9081
<span class="placeholder">HEM</span>: L | R
<span class="placeholder">MNI</span>: MNI152NLin6Asym_res-2 | MNIInfant+1
<span class="placeholder">SPACE</span>: MNI152NLin6Asym_res-2 | T2w
<span class="placeholder">SURF</span>: midthickness | pial | white
</pre>
</div>

## M-CRIB-S & FreeSurfer Surface Reconstruction Methods
Infant fMRIPrep supports two infant-specific surface reconstruction workflows (*[see details above](#nibabies)*): **M-CRIB-S** (used to process **V02** data) and **Infant FreeSurfer** (used to process **V02**, **V03**, and **V04** data). Derivatives include **unique hash IDs** to indicate which surface reconstruction method was used within Infant fMRIPrep for a given dataset:
<table class="table-no-vertical-lines">
<thead> <tr> <th>Method</th> <th>Hash ID</th> <th>Description</th> <th>Visits <i>(Age Range in Months)</i></th> </tr> </thead>
<tbody>
<tr>
<td>M-CRIB-S</td>
<td><a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0_dev2/tools/nibabies_25.2.0-0f306a2f.html">0f306a2f</a></td>
<td>T2w-based method for neonates</td>
<td>V02 <i>(0-1 m)</i></td>
</tr> <tr>
<td>Infant FreeSurfer</td>
<td><a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0_dev2/tools/nibabies_25.2.0-2afa9081.html">2afa9081</a></td> <td>T1w-based method for infants 0-2 years old</td>
<td>V02 <i>(0-1 m)</i>, V03 <i>(3-9 m)</i>, V04 <i>(9-15 m)</i></td>
</tr> </tbody>
</table>

Below we summarize the processing workflows and resulting derivative folder names. Note that downstream outputs such as XCP-D include a second hash indicating the XCP-D processing configuration, which is always `0ef9c88a` for this release:
<p align="center">
  <img src="../images/proc-hashes.png" alt="Detailed MRI Processing Workflow">
</p>

#### Derivatives
The M-CRIB-S and FreeSurfer derivative folders are generated from the [intermediate FreeSurfer-like folders](https://nibabies.readthedocs.io/en/latest/outputs.html#surface-reconstruction) produced by Infant fMRIPrep during surface reconstruction. When M-CRIB-S is used, Infant fMRIPrep still creates a FreeSurfer-structured folder containing the M-CRIB-S results mapped to the standard <a href="https://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllOutputFiles">recon-all</a> layout; these appear in the release under <code>freesurfer-0f306a2f/</code>.

<div id="fs" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">FreeSurfer (<code>freesurfer-&lt;0f306a2f|2afa9081&gt;/</code>) Source Directories</span>
  <a class="anchor-link" href="#fs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ freesurfer-<span class="placeholder">&lt;HASH&gt;</span>/
        |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>/
            |__ label/
            |   |__ <span class="placeholder">&lt;HEM&gt;</span>.<span class="placeholder">&lt;ATLAS&gt;</span>.annot
            |   |__ <span class="placeholder">&lt;HEM&gt;</span>.<span class="placeholder">&lt;ATLAS&gt;</span>.auto.nomask.annot
            |   |__ <span class="placeholder">&lt;HEM&gt;</span>.cortex.label
            |
            |__ mri/
            |   |__ T2.mgz
            |   |__ <span class="placeholder">&lt;ATLAS&gt;</span>+aseg.mgz
            |   |__ aseg.mgz
            |   |__ aseg.<span class="placeholder">&lt;ASEGVAR&gt;</span>.mgz
            |   |__ brain.mgz
            |   |__ brainmask.mgz
            |   |__ <span class="placeholder">&lt;HEM&gt;</span>.ribbon.mgz
            |   |__ norm.mgz
            |   |__ orig.mgz
            |   |__ ribbon.mgz
            |
            |__ scripts/
            |   |__ mcribs.log
            |
            |__ stats/
            |   |__ aseg.stats
            |   |__ brainvol.stats
            |   |__ <span class="placeholder">&lt;HEM&gt;</span>.<span class="placeholder">&lt;ATLAS&gt;</span>.stats
            |   |__ <span class="placeholder">&lt;HEM&gt;</span>.curv.stats
            |
            |__ surf/
                |__ <span class="placeholder">&lt;HEM&gt;</span>.<span class="placeholder">&lt;AREA&gt;</span>
                |__ <span class="placeholder">&lt;HEM&gt;</span>.inflated
                |__ <span class="placeholder">&lt;HEM&gt;</span>.inflated.<span class="placeholder">&lt;CURVVAR&gt;</span>
                |__ <span class="placeholder">&lt;HEM&gt;</span>.orig
                |__ <span class="placeholder">&lt;HEM&gt;</span>.smoothwm
                |__ <span class="placeholder">&lt;HEM&gt;</span>.smoothwm.<span class="placeholder">&lt;CURVVAR&gt;</span>.crv
                |__ <span class="placeholder">&lt;HEM&gt;</span>.smoothwm.<span class="placeholder">&lt;CURVVAR&gt;</span>
                |__ <span class="placeholder">&lt;HEM&gt;</span>.sphere
                |__ <span class="placeholder">&lt;HEM&gt;</span>.sphere.<span class="placeholder">&lt;SPHEREVAR&gt;</span>
                |__ <span class="placeholder">&lt;HEM&gt;</span>.<span class="placeholder">&lt;METRIC&gt;</span>
                |__ <span class="placeholder">&lt;HEM&gt;</span>.<span class="placeholder">&lt;SURF&gt;</span>

<span class="hashtag"># Label Values Legend</span>
<span class="placeholder">HASH</span>: 0f306a2f | 2afa9081
<span class="placeholder">HEM</span>: lh | rh
<span class="placeholder">ATLAS</span>: aparc | aparc+DKTatlas
<span class="placeholder">ASEGVAR</span>: internal | presurf | presurf.preunwmfix 
<span class="placeholder">AREA</span>: area | area.mid | area.pial
<span class="placeholder">CURVVAR</span>: H | K | BE | C | FI | K1 | K2 | S 
<span class="placeholder">SPHEREVAR</span>: reg | reg2 
<span class="placeholder">METRIC</span>: curv | sulc | thickness | volume
<span class="placeholder">SURF</span>: midthickness | pial | white
</pre>
</div>

<div id="mcribs" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">M-CRIB-S (<code>mcribs-0f306a2f/</code>) Source Directories</span>
  <a class="anchor-link" href="#mcribs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<pre class="folder-tree" style="font-size: 11px;">
hbcd/
|__ derivatives/ 
    |__ mcribs-0f306a2f/
        |__ sub-<span class="label">{ID}</span>_ses-V02/
            |__ RawT2/
            |   |__ sub-<span class="label">{ID}</span>_ses-V02.nii.gz
            |
            |__ RawT2RadiologicalIsotropic/
            |   |__ sub-<span class="label">{ID}</span>_ses-V02.nii.gz_symlink_s3_object
            |
            |__ SurfReconDeformable/
            |   |__ sub-<span class="label">{ID}</span>_ses-V02/
            |       |__ meshes/
            |       |   |__ <span class="placeholder">&lt;MESH&gt;</span>.vtp
            |       |   |__ pial-<span class="placeholder">&lt;HEM&gt;</span>.vtp
            |       |   |__ pial-<span class="placeholder">&lt;HEM&gt;</span>-reordered.vtp
            |       |   |__ white-<span class="placeholder">&lt;HEM&gt;</span>.<span class="placeholder">&lt;SUFFIX&gt;</span>
            |       |
            |       |__ recon/
            |       |   |__ cortical-hull-dmap.nii.gz
            |       |   |__ regions.nii.gz 
            |       |
            |       |__ temp/
            |           |__ brain-mask.nii.gz
            |           |__ cerebrum-<span class="placeholder">&lt;HEM&gt;</span>-dmap.nii.gz
            |           |__ cerebrum-<span class="placeholder">&lt;HEM&gt;</span>-hull-<span class="placeholder">{X}</span>.vtp
            |           |__ cerebrum-<span class="placeholder">&lt;HEM&gt;</span>-iso.vtp
            |           |__ <span class="placeholder">&lt;STRUCT&gt;</span>-mask-<span class="placeholder">{X}</span>.nii.gz
            |           |__ <span class="placeholder">&lt;TISSUE&gt;</span>-<span class="placeholder">{X}</span>.vtp
            |           |__ <span class="placeholder">&lt;TISSUE&gt;</span>-<span class="placeholder">{X}</span>-output_<span class="placeholder">{X}</span>.vtp
            |           |__ <span class="placeholder">&lt;pial|white&gt;</span>-foreground.nii.gz
            |           |__ ventricles-dmap.nii.gz
            |           |__ t2w-image.nii.gz_symlink_s3_object
            |
            |__ TissueSeg/
            |   |__ sub-<span class="label">{ID}</span>_ses-V02_all_labels.nii.gz
            |   |__ sub-<span class="label">{ID}</span>_ses-V02_all_labels_manedit.nii.gz_symlink_s3_object
            |   |__ sub-<span class="label">{ID}</span>_ses-V02_brain_mask.nii.gz
            |   |__ sub-<span class="label">{ID}</span>_ses-V02_t2w_restore.nii.gz_symlink_s3_object
            |
            |__ TissueSegDrawEM/
            |   |__ sub-<span class="label">{ID}</span>_ses-V02/
            |       |__ N4/
            |           |__ sub-<span class="label">{ID}</span>_ses-V02.nii.gz_symlink_s3_object
            |
            |__ freesurfer/ <span class="hashtag"># Only M-CRIB-S–unique files</span>
            |   |__ sub-<span class="label">{ID}</span>_ses-V02/
            |       |__ mri/
            |           |__ brain.mgz_symlink_s3_object
            |           |__ orig.mgz_symlink_s3_object
            |
            |__ logs/
            |   |__ sub-<span class="label">{ID}</span>_ses-V02.log
            |
            |__ command.txt

<span class="hashtag"># Label Values Legend</span>
<span class="placeholder">HEM</span>: lh | rh
<span class="placeholder">STRUCT</span>: brain | cerebrum-{lh/rh} | corpus-callosum | cortex | deep-gray-matter | gray-matter | ventricles | white-matter
<span class="placeholder">TISSUE</span>: cerebrum-lh | cerebrum-rh | pial | white 
<span class="placeholder">MESH</span>: internal | pial | white | pial+internal | white+internal
<span class="placeholder">SUFFIX</span>: CortexMask.curv | Normals.surf | RegionId.curv | vtp 
</pre>
</div>

<div id="mcribs-vs-fs" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
<span class="text">Restoring Symlink Files Present in M-CRIB-S Derivatives</span>
  <a class="anchor-link" href="#mcribs-vs-fs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>When downloaded, the symlink files present within the M-CRIB-S derivatives (<code>mcribs-0f306a2f/</code>), appended with <code>*_symlink_s3_object</code>, appear as text files that contain the S3 object path instead of the actual file content. If needed, you may restore these files as symlinks via the following terminal command, which restores all symlink files within your locally downloaded directory and renames them without <code>*_symlink_s3_object</code> to match the original sourcedata filenames:</p>
<div class="copy-box">
  <div class="copy-text-container">
    <span id="specific-text-code">find . -type f -name "*_symlink_s3_object" -print | while read path ; do
  symval=$(cat "$path")
  symdir=$(dirname "$path")
  symbase=$(basename "$path" _symlink_s3_object)
  ln -s "$symval" "$symdir/$symbase" && rm -f "$path" || break
done</span>
  <button class="copy-button">Copy</button>
  </div>
</div>
<p>To simply print the commands needed to restore individual symlinks without making any changes to the local data, run the following command:</p>
<div class="copy-box">
<div class="copy-text-container">
  <span id="specific-text-code">find . -type f -name "*_symlink_s3_object" -print | while read path ; do
symval=$(cat "$path")
symdir=$(dirname "$path")
symbase=$(basename "$path" _symlink_s3_object)
echo ln -s "$symval" "$symdir/$symbase" '&&' rm -f "$path"
done</span>
<button class="copy-button">Copy</button>
</div>
</div>
</div>

## XCP-D
<a href="https://xcp-d.readthedocs.io/en/latest/">XCP-D</a> performs functional MRI post-processing and noise regression from Infant-fMRIPrep derivatives, producing cleaned and parcellated data ready for analysis. Atlases used for parcellation are described under <a href="#parc">MRI Derivatives: Quickstart Guide</a>. See the XCP-D documentation on <a href="https://xcp-d.readthedocs.io/en/latest/outputs.html#functional-timeseries-and-connectivity-matrices">"HBCD mode" functional outputs</a>.

<div id="xcpd" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa-solid fa-diagram-project"></i></span>
<span class="text-with-link"><span class="text">XCP-D Processing Overview</span>
<a class="anchor-link" href="#xcpd" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
<span class="arrow">▸</span></div>
<div class="table-collapsible-content">
<p><b>Anatomical Processing</b><br>
Native-space T2w images are transformed into standard MNI152NLin6Asym space (1 mm³ resolution).
Morphometric surfaces (fsLR-space) from Infant fMRIPrep are copied to the XCP-D derivatives. HCP-style midthickness, inflated, and very-inflated surfaces are generated from the white-matter and pial surface meshes and mapped to fsLR space.</p> 
<p><b>Functional Processing</b><br>
For each BOLD run, XCP-D performs a series of cleanup and quality-control steps:</p>
<ul>
<li>First 4 volumes (dummy scans) are removed.</li>
<li>Motion correction: Framewise displacement (FD) is calculated per Power et al. (2014); volumes with FD &gt; 0.3 mm flagged as high-motion outliers.</li>
<li>Nuisance regression: 36 confound regressors (motion, tissue, and global signals plus derivatives) regressed out following the 36P strategy.</li>
<li>Despiking and filtering: Data despiked, temporally filtered (0.01–0.08 Hz), and smoothed (6 mm FWHM).</li>
<li>Censoring: High-motion volumes are interpolated and later censored to minimize motion artifacts.</li>
<li>Amplitude of Low-Frequency Fluctuations (ALFF) and Regional Homogeneity (ReHo) metrics computed from cleaned data.</li> 
<li>Parcellated time series are extracted for <a href="#parc">each atlas</a> and pairwise functional connectivity is calculated as the Pearson correlation between regional time series.</li>
<li>Postprocessed derivatives are concatenated across runs.</li>
</ul>
</div>

<div id="xcpd-derivs" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">XCP-D Derivatives (<code>xcp_d-&lt;0f306a2f|2afa9081&gt;+0ef9c88a/</code>)</span>
  <a class="anchor-link" href="#xcpd-derivs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<pre style="font-size: 10px;" class="folder-tree">
hbcd/
|_ derivatives/ 
   |_ xcp_d-<span class="placeholder">&lt;HASH&gt;</span>/
      |_ sub-<span class="label">{ID}</span>/
         |_ ses-<span class="label">{V0X}</span>/
         |  |_ anat/
         |  |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_desc-preproc_T2w.nii.gz
         |  |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-<span class="placeholder">&lt;METRIC&gt;</span>_morph.tsv
         |  |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span class="placeholder">&lt;inflated|vinflated&gt;</span>.surf.gii
         |  |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span class="placeholder">&lt;midthickness|pial|white&gt;</span>.surf.gii
         |  |  |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_run-<span class="label">{X}</span>_space-fsLR_den-91k_<span class="placeholder">&lt;METRIC&gt;</span>.dscalar.nii
         |  |
         |  |_ func/ <span class="hashtag"># All func files have JSONs with exception of .hdf5 & *linc_qc.tsv</span>
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_desc-abcc_qc.hdf5 <span class="hashtag">(No JSON)</span>
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_<span class="placeholder">&lt;motion|outliers&gt;</span>.tsv
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_space-fsLR_den-91k_desc-<span class="placeholder">&lt;DENOISED&gt;</span>_bold.dtseries.nii
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_den-91k_stat-mean_timeseries.ptseries.nii
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-mean_timeseries.tsv
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-pearsoncorrelation_relmat.tsv
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_desc-abcc_qc.hdf5 <span class="hashtag">(No JSON)</span>
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_desc-linc_qc.tsv <span class="hashtag">(No JSON)</span>
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_<span class="placeholder">&lt;design|motion|outliers&gt;</span>.tsv
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_desc-<span class="placeholder">&lt;DENOISED&gt;</span>_bold.dtseries.nii
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_stat-<span class="placeholder">&lt;STAT&gt;</span>_boldmap.dscalar.nii
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_stat-alff_desc-smooth_boldmap.dscalar.nii
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_den-91k_stat-coverage_boldmap.pscalar.nii
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_den-91k_stat-mean_timeseries.ptseries.nii
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_den-91k_stat-pearsoncorrelation_boldmap.pconn.nii
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-<span class="placeholder">&lt;STAT&gt;</span>_bold.tsv
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-coverage_bold.tsv
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-mean_timeseries.tsv
         |     |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-pearsoncorrelation_relmat.tsv
         |  
         |_ figures/
         |_ <span class="subses">SUBSES</span>_hash-<span class="placeholder">&lt;HASH&gt;</span>_executive_summary.html
         |_ sub-<span class="label">{ID}</span>.html

<span class="hashtag"># Label Values Legend</span>
<span class="subses">SUBSES</span>: sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>
<span class="placeholder">&lt;HASH&gt;</span>: 0f306a2f+0ef9c88a | 2afa9081+0ef9c88a
<span class="placeholder">&lt;METRIC&gt;</span>: curv | sulc | thickness
<span class="placeholder">&lt;DENOISED&gt;</span>: denoised | denoisedSmoothed
<span class="placeholder">&lt;STAT&gt;</span>: alff | reho
<span class="placeholder">&lt;APARC&gt;</span>: 4S-&lt;156|256|...|1056&gt;Parcels | Glasser | Gordon | MIDB | MyersLabonte
<span class="placeholder">&lt;PARC&gt;</span>: 4S-&lt;156|256|...|1056&gt;Parcels, Glasser, Gordon, MIDB, MyersLabonte, HCP, Tian
</pre>
</div>

## MRI Derivatives Quick Start Guide

Below is a summary of key MRI derivatives used for **structural morphology** and **resting-state functional MRI (rsfMRI) functional connectivity** analyses. Key derivatives, produced by the **XCP-D** pipeline, include volumetric and surface-based time series for each participant. The data release also includes dense and parcellated time series with at least 2.5 minutes of low-motion data (FD>0.3), functional connectivity matrices, regional homogeneity values, and amplitude of low-frequency fluctuation values. 

<div id="struc" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-cubes"></i></span>
  <span class="text-with-link">
  <span class="text">Structural Morphology: Key Derivatives for Analysis</span>
  <a class="anchor-link" href="#struc" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; border-bottom: 1px solid #6b6b6b66;">Curvature, Sulcal Depth, & Cortical Thickness</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>anat/*_space-fsLR_den-91k_<span style="color: teal;">&lt;curv|sulc|thickness&gt;</span>.dscalar.nii</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Vertex-wise cortical morphology analyses (e.g., folding, curvature, thickness comparisons).</p>
<p class="details">
These CIFTI scalar files contain surface-based structural metrics derived from reconstructed L/R cortical surfaces, aligned to the fsLR template (~64k vertices per hemisphere).  
<ul style="margin-top: 0; font-size: 0.9em;">
<li><b>Curvature</b>: Characterizes cortical folding and morphology; often used as a covariate in morphometric analyses.</li>
<li><b>Sulcal depth</b>: Complements curvature to describe cortical shape and folding complexity.</li>
<li><b>Cortical thickness</b>: Distance between pial and white matter surfaces (mm); typically averaged within ROIs or compared across participants to study development, aging, or group effects.</li>
</ul>
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; border-bottom: 1px solid #6b6b6b66;">Parcellated Structural Measures</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>anat/*_space-fsLR_seg-<span style="color: teal;">&lt;PARC&gt;</span>_stat-mean_desc-<span style="color: teal;">&lt;curv|sulc|thickness&gt;</span>_morph.tsv</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Region-based (ROI-level) analyses such as group comparisons or developmental modeling.</p>
<p class="details">
Tabulated summaries of cortical metrics (curvature, sulcal depth, thickness) within anatomical regions defined by 
<a href="#parc">parcellation atlases</a>. These files provide regional averages for statistical modeling or visualization.
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Midthickness, Pial, and White Matter Surfaces</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>anat/*_hemi-<span style="color: teal;">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span style="color: teal;">&lt;midthickness|pial|white&gt;</span>.surf.gii</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Visualizing cortical anatomy or mapping functional data to anatomical space.</p>
<p class="details">
3D surface models representing the midthickness, gray–white matter boundary, and pial surfaces for each hemisphere.  
Useful for rendering structural data, computing surface-based metrics, or visualizing functional overlays.
</p>
</div>



<div id="fc" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-globe"></i></span>
  <span class="text-with-link">
  <span class="text">Functional Connectivity: Key Derivatives for Analysis</span>
  <a class="anchor-link" href="#fc" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px;  padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Dense Timeseries</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>func/*_task-rest_space-fsLR_den-91k_desc-<span style="color: teal;">&lt;denoised|denoisedSmoothed&gt;</span>_bold.dtseries.nii</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Voxelwise or seed-based FC analyses, timeseries analysis via sliding windows or markov chains, etc.</p>
<p class="details">
CIFTI dense time series containing fully preprocessed, temporally filtered, and nuisance-regressed BOLD data.
These files combine the left and right surfaces, aligned to the standard fsLR surface template, with the subcortical volume annotated by subcortical structure.
Each greyordinate (~96k total) represents a vertex or voxel with pre-processed resting-state functional MRI time-series.
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Parcellated Timeseries</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>func/*_task-rest_space-fsLR_seg-<span style="color: teal;">&lt;PARC&gt;</span>_stat-mean_timeseries.tsv</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> ROI-to-ROI connectivity or network analyses using mean BOLD signals per region.</p>
<p class="details">
Tabulated mean BOLD time series for each region in the 
<a href="#parc">parcellation atlases</a>.  
Also available as CIFTI <code>.ptseries.nii</code> files, where columns = regions and rows = timepoints.
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Connectivity Matrices</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>func/*_task-rest_space-fsLR_seg-<span style="color: teal;">&lt;PARC&gt;</span>_stat-pearsoncorrelation_relmat.tsv</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Quick inspection, validation, or as input to network and graph analyses.</p>
<p class="details">
Tab-delimited matrices of pairwise Pearson correlations between atlas regions, computed from parcellated time series using all available low-motion data (motion censored with a framewise displacement threshold of 0.3 mm). These matrices form the foundation for ROI-to-ROI connectivity analyses.
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Motion Detection and Confound Files</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>func/*_task-rest_dir-PA_run-{X}_<span style="color: teal;">&lt;design|motion|outliers&gt;</span>.tsv</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-triangle-exclamation"></i> <b>Required for:</b> Motion assessment and filtering low-quality data prior to group analyses.</p>
<p class="details">
Includes framewise displacement values and nuisance regressor design files.  
Design files contain one column per regressor (e.g., motion parameters, high-motion outlier volume indicators).  
See the <a href="https://xcp-d.readthedocs.io/en/latest/outputs.html#other-outputs-include-quality-control-framewise-displacement-and-confounds-files" target="_blank">XCP-D documentation</a> for details.
</p>
</div>
<style>
.filename {
  background-color: #f8f9fa;
  border: 1px solid #e1e4e8;
  border-radius: 6px;
  padding: 6px 10px;
  font-family: monospace;
  font-size: 0.95em;
  margin-bottom: 6px;
  overflow-x: auto;
}
.recommended {
  background-color: #eef6ff;
  padding: 6px 10px;
  font-size: 0.9em;
  border-radius: 4px;
  margin: 4px 0 10px;
}
.details {
  margin-top: 0;
  font-size: 0.95em;
  color: #333;
}
</style>

<div id="parc" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-book-atlas"></i></span>
  <span class="text-with-link">
  <span class="text">Parcellations</span>
  <a class="anchor-link" href="#parc" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><i>See <a href="https://xcp-d.readthedocs.io/en/latest/outputs.html#parcellations-and-atlases">Parcellations & Atlases</a> in the XCP-D documentation for more details.</i></p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Atlas</th>
  <th>Description</th>
  <th>Recommended Use</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Glasser</td>
  <td style="word-wrap: break-word; white-space: normal;">Population-level multimodal anatomical atlas (<a href="https://doi.org/10.1038/nature18933">Glasser et al., 2016</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Population-level structure and surface-based morphology.</td>
</tr>
<tr>
  <td>Gordon</td>
  <td style="word-wrap: break-word; white-space: normal;">333-ROI template from rs-fMRI boundary detection for 120 young adults with 14 minutes of data collected on average  (<a href="https://doi.org/10.1093/cercor/bhu239">Gordon et al., 2016</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Functional network mapping and group-level FC analyses.</td>
</tr>
<tr>
  <td>HCP</td>
  <td style="word-wrap: break-word; white-space: normal;">360-ROI atlas parcellated from combining task, rest, and diffusion MRI data of 210 young adults (<a href="https://doi.org/10.1016/j.neuroimage.2013.04.127">Glasser et al., 2013</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Cross-modal structural-functional alignment.</td>
</tr>
<tr>
  <td>MIDB</td>
  <td style="word-wrap: break-word; white-space: normal;">Precision atlas derived from ABCD data, 75% probability threshold (<a href="https://doi.org/10.1038/s41593-024-01596-5">Hermosillo et al., 2024</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Individualized functional network mapping.</td>
</tr>
<tr>
  <td>Myers-Labonte</td>
  <td style="word-wrap: break-word; white-space: normal;">Infant probabilistic atlas, 50% probability threshold (<a href="https://doi.org/10.1101/2023.11.10.566629">Meyers et al., 2023</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Infant individualized functional network mapping.</td>
</tr>
<tr>
  <td>Tian</td>
  <td style="word-wrap: break-word; white-space: normal;">Subcortical parcellation atlas (<a href="https://doi.org/10.1038/s41593-020-00711-6">Tian et al., 2020</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Subcortical connectivity analyses.</td>
</tr>
<tr>
  <td><span class="tooltip tooltip-right">4S<span class="tooltiptext">Schaefer Supplemented with Subcortical Structures</span></span> Atlas</td>
  <td style="word-wrap: break-word; white-space: normal;">Integrated multimodal atlas combining cortical (at ten resolutions, 100-1000 parcels), subcortical, and cerebellar structures (<a href="https://github.com/PennLINC/AtlasPack">AtlasPack</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Cross-modality alignment across XCP-D, QSIPrep, and ASLPrep outputs.</td>
</tr>
</tbody>
</table>
</div>

## References
<div class="references">
<p>Adamson, C. L., Alexander, B., Ball, G., Beare, R., Cheong, J. L. Y., Spittle, A. J., Doyle, L. W., Anderson, P. J., Seal, M. L., & Thompson, D. K. (2020). Parcellation of the neonatal cortex using Surface-based Melbourne Children’s Regional Infant Brain atlases (M-CRIB-S). <em>Scientific Reports</em>, 10(1), 4359. <a href="https://doi.org/10.1038/s41598-020-61326-2">https://doi.org/10.1038/s41598-020-61326-2</a></p>
<p>Goncalves, M., Moser, J., Madison, T. J., McCollum, R., Lundquist, J. T., Fayzullobekova, B., Hadera, L., Pham, H. H. N., Moore, L. A., Houghton, A., Conan, G., Styner, M. A., Alexopoulos, D., Smyser, C. D., Stoyell, S. M., Koirala, S., Nelson, S. M., Weldon, K. B., Lee, E., … Fair, D. A. (2025). FMRIPrep Lifespan: Extending A robust pipeline for functional MRI preprocessing to developmental neuroimaging. <em>In bioRxivorg.</em> <a href="https://doi.org/10.1101/2025.05.14.654069">https://doi.org/10.1101/2025.05.14.654069</a></p>
<p>Hendrickson, T. J., Reiners, P., Moore, L. A., Lundquist, J. T., Fayzullobekova, B., Perrone, A. J., Lee, E. G., Moser, J., Day, T. K. M., Alexopoulos, D., Styner, M., Kardan, O., Chamberlain, T. A., Mummaneni, A., Caldas, H. A., Bower, B., Stoyell, S., Martin, T., Sung, S., … Feczko, E. (2024). BIBSNet: A deep learning Baby image brain segmentation network for MRI scans. <em>In bioRxivorg</em>. <a href="https://doi.org/10.1101/2023.03.22.533696">https://doi.org/10.1101/2023.03.22.533696</a></p>
<p>Zöllei, L., Iglesias, J. E., Ou, Y., Grant, P. E., & Fischl, B. (2020). Infant FreeSurfer: An automated segmentation and surface extraction pipeline for T1-weighted neuroimaging data of infants 0-2 years. <em>NeuroImage</em>, 218(116946), 116946. <a href="https://doi.org/10.1016/j.neuroimage.2020.116946">https://doi.org/10.1016/j.neuroimage.2020.116946</a></p>
</div>
 
