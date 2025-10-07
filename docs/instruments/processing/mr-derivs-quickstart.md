# MRI Derivatives Quick Start Guide

Most MRI-derived measures commonly used for analysis are provided by the **BIBSNet** and **XCP-D** pipelines. XCP-D builds upon **Infant-fMRIPrep** outputs to generate fully preprocessed, denoised, and quality-assessed data suitable for both **functional** and **structural** analyses.

For more details on specific outputs and processing configurations, see:

> <a href="../../../datacuration/file-based-data/#derivatives" target="_blank"><i style="font-size: 0.9em;" class="fa-solid fa-up-right-from-square"></i> HBCD Derivatives</a>: *List of structural and functional MRI pipeline derivatives with links to documentation*<br>
<a href="../../mri/fmri/#xcpd" target="_blank"><i style="font-size: 0.9em;" class="fa-solid fa-up-right-from-square"></i> fMRI Release Data (XCP-D)</a>: *Overview of XCP-D derivatives included in the HBCD release*<br>
<a href="https://hbcd-cbrain-processing.readthedocs.io/latest/tools/xcp_d.html"><i style="font-size: 0.9em;" class="fa-solid fa-up-right-from-square"></i> HBCD Processing Documentation (XCP-D)</a>: *Pipeline parameters and configurations used for HBCD processing*<br>
<a href="https://xcp-d.readthedocs.io/en/latest/outputs.html#outputs-of-xcp-d"><i style="font-size: 0.9em;" class="fa-solid fa-up-right-from-square"></i> Official XCP-D Documentation</a>: *Comprehensive documentation of all XCP-D outputs*

The sections below highlight the XCP-D output files most relevant for functional connectivity and structural morphology analyses.

## Structural Derivatives 

### BIBSNet

BIBSNet ([see full list of HBCD derivative outputs](../mri/smri.md#bibsnet)) provides brain volumes computed for segmented ROIs in native T1w/T2w space in `*_space-<T1w|T2w>_desc-aseg_volumes.tsv`, with each tab-delimited column representing volumes for each BIBSnet structure. BIBSnet is an automated segmentation pipeline that creates Freesurfer segmentation labels, so each BIBSnet structure reflects a Freesurfer label – see the [BIBSNet documentation](https://bibsnet.readthedocs.io/en/latest/) for more details.

### XCP-D 

XCP-D provides several structural morphology measures derived from the fMRIPrep anatomical outputs within the `anat/` folder. These surface-based derivatives are commonly used to assess cortical features such as **thickness**, **curvature**, and **sulcal depth**, often summarized within atlas-defined regions or compared across subjects to study cortical development and brain morphology. The following files are highlighted below (<i>see <a href="../../mri/fmri/#xcpd" target="_blank">full outputs</a></i>):

<pre style="font-size: 11px;" class="folder-tree">
hbcd/
|_ derivatives/ 
   |_ xcp_d/
      |_ sub-<span class="label">{ID}</span>/
         |_ ses-<span class="label">{V0X}</span>/
            |_ anat/
            <span class="hashtag">#1</span> |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_den-91k_<span class="placeholder">&lt;curv|sulc|thickness&gt;</span>.dscalar.nii
            <span class="hashtag">#2</span> |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-mean_desc-<span class="placeholder">&lt;curv|sulc|thickness&gt;</span>_morph.tsv
            <span class="hashtag">#3</span> |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span class="placeholder">&lt;midthickness|pial|white&gt;</span>.surf.gii

<span class="hashtag"># Label Values Legend</span>
<span class="placeholder">&lt;PARC&gt; (anat/ parcellations)</span>: 4S-&lt;156|256|356|...|1056&gt;Parcels, Glasser, Gordon, MIDB, MyersLabonte
</pre>
<p></p>

<div id="s1" class="table-compact-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-folder-open"></i></span>
  <span class="text-with-link">
    <span class="text">#1 Curvature, Sulcal Depth, & Cortical Thickness</span>
    <a class="anchor-link" href="#s1" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content" style="margin-bottom: 3px;">
  <p>
    These three <strong>surface-based structural metrics</strong> are provided as CIFTI scalar files derived from reconstructed left and right cortical surfaces and aligned to the standard fsLR template (~64k vertices per hemisphere). 
    Each vertex encodes <i>curvature</i>, <i>sulcal depth</i>, and <i>cortical thickness</i>, respectively. 
    Average ROI values for standard parcellations are available in the parcellated structural measures.
  </p>
  <table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <tbody>
      <tr>
        <td style="word-wrap: break-word; white-space: normal;">
          <strong>Curvature</strong> (<code>*_space-fsLR_den-91k_curv.dscalar.nii</code>)<br>
          Represents local cortical folding. Positive values correspond to sulci (inward folds) and negative values to gyri (outward folds). Useful for characterizing cortical morphology or as a covariate in morphometric analyses.
        </td>
      </tr> 
      <tr>
        <td style="word-wrap: break-word; white-space: normal;">
          <strong>Sulcal Depth</strong> (<code>*_space-fsLR_den-91k_sulc.dscalar.nii</code>)<br>
          Measures the relative depth of sulci compared to adjacent gyri. Positive values indicate deeper sulci; negative values indicate more prominent gyri. Often used with curvature to describe cortical shape and folding complexity.
        </td>
      </tr> 
      <tr>
        <td style="word-wrap: break-word; white-space: normal;">
          <strong>Cortical Thickness</strong> (<code>*_space-fsLR_den-91k_thickness.dscalar.nii</code>)<br>
          Reflects the distance (mm) between corresponding vertices on the pial and white matter surfaces. Commonly averaged within ROIs or compared across subjects to study cortical development, aging, or group differences.          
        </td>
      </tr>  
    </tbody>
  </table>
</div>

<div id="s2" class="table-compact-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-folder-open"></i></span>
  <span class="text-with-link">
  <span class="text">#2 Parcellated Structural Measures</span>
  <a class="anchor-link" href="#s2" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content" style="margin-bottom: 3px;">
<p><code>sub-{ID}_ses-{V0X}_run-{X}_space-fsLR_seg-&lt;PARC&gt;_stat-mean_desc-&lt;curv|sulc|thickness&gt;_morph.tsv</code></p>
<p>Tabulated summaries of cortical metrics (curvature, sulcal depth, thickness) within anatomical or functional regions defined by an atlas. Ideal for region-based statistical analysis and group comparisons.</p>
</div>

<div id="s3" class="table-compact-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-folder-open"></i></span>
  <span class="text-with-link">
  <span class="text">#3 Midthickness, Pial, and White Matter Surfaces</span>
  <a class="anchor-link" href="#s3" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content" style="margin-bottom: 3px;">
<p><code>sub-{ID}_ses-{V0X}_run-{X}_hemi-&lt;L|R&gt;_space-fsLR_den-32k_&lt;midthickness|pial|white&gt;.surf.gii</code><p>
<p>3D surface models representing the midthickness, gray–white matter boundary, and the pial surface for each hemisphere. Commonly used for visualizing cortical anatomy, computing surface-based metrics, or mapping functional data to anatomical space.</p>
</div>

## Functional Connectivity

### XCP-D

XCP-D produces several derivative outputs designed for resting state functional MRI functional connectivity (FC) and time series analyses, available within the `func/` subfolder. These include **denoised BOLD data**, **parcellated time series**, and **derived connectivity matrices**, along with **frame displacement and confound files** to support motion correction and data quality assessment. Together, these provide clean and standardized measures of resting state brain measures for both voxelwise and region-based network analyses. The following files are highlighted below (<i>see <a href="../../mri/fmri/#xcpd" target="_blank">full outputs</a></i>):

<pre style="font-size: 11px;" class="folder-tree">
hbcd/
|_ derivatives/ 
   |_ xcp_d/
      |_ sub-<span class="label">{ID}</span>/
         |_ ses-<span class="label">{V0X}</span>/
            |_ func/
            <span class="hashtag">#1</span> |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_space-fsLR_den-91k_desc-<span class="placeholder">&lt;denoised|denoisedSmoothed&gt;</span>_bold.dtseries.nii  
            <span class="hashtag">#2</span> |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-mean_timeseries.tsv
            <span class="hashtag">#3</span> |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-pearsoncorrelation_relmat.tsv
            <span class="hashtag">#4</span> |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_<span class="placeholder">&lt;design|motion|outliers&gt;</span>.tsv

<span class="hashtag"># Label Values Legend</span>
<span class="placeholder">&lt;PARC&gt; (func/ parcellations)</span>: 4S-&lt;156|256|...|1056&gt;Parcels, Glasser, Gordon, MIDB, MyersLabonte, HCP, Tian
</pre>
<p></p>

<div id="f1" class="table-compact-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-folder-open"></i></span>
  <span class="text-with-link">
  <span class="text"><strong>#1 Denoised Timeseries</strong></span>
  <a class="anchor-link" href="#f1" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content" style="margin-bottom: 3px;">
<p><code>*_den-91k_desc-denoised{Smoothed}_bold.dtseries.nii</code></p>
<p>CIFTI dense time series containing fully preprocessed, temporally filtered, and nuisance-regressed BOLD data. These files combine the left and right surfaces, aligned to the standard fsLR surface template, with the subcortical volume annotated by subcortical structure. Each “greyordinate (vertex/voxel)” within these files contains a pre-processed resting-state functional MRI time-series for a total of approximately 96 thousand greyordinates. Denoised timeseries files are suitable for computing voxelwise FC analyses, seed-based correlation maps, other data-driven connectivity methods, or for timeseries analysis via sliding windows or markov chains.</p>
</div>

<div id="f2" class="table-compact-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-folder-open"></i></span>
  <span class="text-with-link">
  <span class="text"><strong>#2 Parcellated Timeseries</strong></span>
  <a class="anchor-link" href="#f2" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content" style="margin-bottom: 3px;">
<p><code>*_seg-&lt;PARC&gt;_stat-mean_timeseries.tsv</code></p>
<p>Tabulated mean BOLD time series – organized as tab seperated values – for each region in the following atlases: <a href="https://github.com/PennLINC/AtlasPack">4S</a> (nodes 156-1056), Glasser, Gordon, MIDB, MyersLabonte, HCP, and Tian. Also available as CIFTI files (<code>*_stat-mean_timeseries.ptseries.nii</code>), where each column corresponds to a brain region, and each row to a timepoint. Ideal for computing ROI-to-ROI connectivity matrices or for timeseries analysis via sliding windows or markov chains.</p>
</div>

<div id="f3" class="table-compact-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-folder-open"></i></span>
  <span class="text-with-link">
  <span class="text"><strong>#3 Connectivity Matrices</strong></span>
  <a class="anchor-link" href="#f3" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content" style="margin-bottom: 3px;">
<p><code>*_seg-&lt;PARC&gt;_stat-pearsoncorrelation_relmat.tsv</code></p>
<p>Tab-delimited matrices of pairwise Pearson correlations between atlas regions, computed from the parcellated time series. Useful for quick inspection, validation, as input for group-level analyses, or performing network and graph analyses.</p>
</div>

<div id="f4" class="table-compact-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-folder-open"></i></span>
  <span class="text-with-link">
  <span class="text"><strong>#4 Motion Detection and Confound Files</strong></span>
  <a class="anchor-link" href="#f4" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content" style="margin-bottom: 3px;">
<p><code>*_&lt;design|motion|outliers&gt;.tsv</code></p>
<p>Include framewise displacement values and nuisance regressor design files. The design files (<code>*_design.tsv</code>) contain one column per regressor (e.g., motion parameters and one-hot indicators for high-motion outlier volumes). Recommended for identifying and filtering low-quality data before group analyses. See <a href="https://xcp-d.readthedocs.io/en/latest/outputs.html#other-outputs-include-quality-control-framewise-displacement-and-confounds-files">this section</a> of the XCP-D documentation for details.</p>
</div>


<br>