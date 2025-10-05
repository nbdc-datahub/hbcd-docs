<p style="font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

# MRI Derivatives Quick Start Guide

Most MRI-derived measures commonly used for analysis are provided by the **XCP-D** pipeline. XCP-D builds upon **Infant-fMRIPrep** outputs to generate fully preprocessed, denoised, and quality-assessed data suitable for both **functional** and **structural** analyses.

For more details on specific outputs and processing configurations, see:

> <a href="../../../datacuration/file-based-data/#derivatives" target="_blank"><i style="font-size: 0.9em;" class="fa-solid fa-up-right-from-square"></i> HBCD Derivatives</a>: *List of structural and functional MRI pipeline derivatives with links to documentation*<br>
<a href="../../mri/fmri/#xcpd" target="_blank"><i style="font-size: 0.9em;" class="fa-solid fa-up-right-from-square"></i> fMRI Release Data (XCP-D)</a>: *Overview of XCP-D derivatives included in the HBCD release*<br>
<a href="https://hbcd-cbrain-processing.readthedocs.io/latest/tools/xcp_d.html"><i style="font-size: 0.9em;" class="fa-solid fa-up-right-from-square"></i> HBCD Processing Documentation (XCP-D)</a>: *Pipeline parameters and configurations used for HBCD processing*<br>
<a href="https://xcp-d.readthedocs.io/en/latest/outputs.html#outputs-of-xcp-d"><i style="font-size: 0.9em;" class="fa-solid fa-up-right-from-square"></i> Official XCP-D Documentation</a>: *Comprehensive documentation of all XCP-D outputs*

The sections below highlight the XCP-D output files most relevant for functional connectivity and structural morphology analyses.

## Structural Derivatives (XCP-D)

XCP-D provides several structural morphology measures derived from the fMRIPrep anatomical outputs. These surface-based derivatives are commonly used to assess cortical features such as **thickness**, **curvature**, and **sulcal depth**, often summarized within atlas-defined regions or compared across subjects to study cortical development and brain morphology. The following files are highlighted below (<i>see <a href="../../mri/fmri/#xcpd" target="_blank">full outputs</a></i>):

<pre style="font-size: 11px;" class="folder-tree">
hbcd/
|_ derivatives/ 
   |_ xcp_d/
      |_ sub-<span class="label">{ID}</span>/
         |_ ses-<span class="label">{V0X}</span>/
            |_ anat/
            <span class="hashtag">#1</span> |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_den-91k_thickness.dscalar.nii
            <span class="hashtag">#2</span> |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_den-91k_curv.dscalar.nii
            <span class="hashtag">#3</span> |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_den-91k_sulc.dscalar.nii
            <span class="hashtag">#4</span> |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-<span class="placeholder">&lt;curv|sulc|thickness&gt;</span>_morph.tsv
            <span class="hashtag">#5</span> |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span class="placeholder">&lt;pial|white&gt;</span>.surf.gii

<span class="hashtag"># Label Values Legend</span>
<span class="placeholder">&lt;APARC&gt; (anat/ parcellations)</span>: 4S-&lt;156|256|356|...|1056&gt;Parcels, Glasser, Gordon, MIDB, MyersLabonte
</pre>
<p></p>

<details>
  <summary><strong>#1 Cortical Thickness</strong> (<code>*_den-91k_thickness.dscalar.nii</code>)</summary>
  <p>CIFTI scalar files containing surface-based maps of cortical thickness (in millimeters) for each hemisphere. Generated from reconstructed cortical surfaces and aligned to the standard <code>fsLR</code> template. Commonly averaged within ROIs or compared across subjects to assess cortical development, aging, or group differences.</p>
</details>

<details>
  <summary><strong>#2 Curvature</strong> (<code>*_den-91k_curv.dscalar.nii</code>)</summary>
  <p>Provides mean surface curvature values representing local cortical folding patterns of the cortex. Positive values correspond to sulci (inward folds) and negative values to gyri (outward folds). Useful for characterizing cortical folding or as a covariate in morphometric analyses.</p>
</details>

<details>
  <summary><strong>#3 Sulcal Depth</strong> (<code>*_den-91k_sulc.dscalar.nii</code>)</summary>
  <p>Measures the relative depth of cortical sulci compared to adjacent gyri. Often used alongside curvature to describe cortical shape and folding complexity.</p>
</details>

<details>
  <summary><strong>#4 Parcellated Structural Measures</strong> (<code>*_seg-&lt;PARC&gt;_stat-mean_desc-&lt;curv|sulc|thickness&gt;_morph.tsv</code>)</summary>
  <p>Tabulated summaries of cortical metrics (curvature, sulcal depth, thickness) within anatomical or functional regions defined by an atlas. Ideal for region-based statistical analysis and group comparisons.</p>
</details>

<details>
  <summary><strong>#5 Pial and White Matter Surfaces</strong> (<code>*_hemi-&lt;L|R&gt;_space-fsLR_den-32k_&lt;pial|white&gt;.surf.gii</code>)</summary>
  <p>3D surface models representing the gray–white matter boundary and the pial surface for each hemisphere. Commonly used for visualizing cortical anatomy, computing surface-based metrics, or mapping functional data to anatomical space.</p>
</details>

## Functional Connectivity (XCP-D)

XCP-D produces several derivative outputs designed for functional connectivity (FC) and time series analyses. These include **denoised BOLD data**, **parcellated time series**, and **derived connectivity matrices**, along with **frame displacement and confound files** to support motion correction and data quality assessment. Together, these provide clean and standardized measures of brain activity for both voxelwise and region-based network analyses. The following files are highlighted below (<i>see <a href="../../mri/fmri/#xcpd" target="_blank">full outputs</a></i>):

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

<details>
  <summary><strong>#1 Denoised Timeseries</strong> (<code>*_den-91k_desc-denoised{Smoothed}_bold.dtseries.nii</code>)</summary>
  <p>
  CIFTI dense time series containing fully preprocessed, temporally filtered, and nuisance-regressed BOLD data. Aligned to the standard <code>fsLR</code> surface template, these files are suitable for voxelwise FC analyses, seed-based correlation maps, or other data-driven connectivity methods.
  </p>
</details>

<details>
  <summary><strong>#2 Parcellated Timeseries</strong> (<code>*_seg-&lt;PARC&gt;_stat-mean_timeseries.tsv</code>)</summary>
  <p>
  Tabulated mean BOLD time series for each region in a the following atlases: <a href="https://github.com/PennLINC/AtlasPack">4S-{X}-Region Parcels</a>, Glasser, Gordon, MIDB, MyersLabonte, HCP, and Tian. Also available as CIFTI files (<code>*_stat-mean_timeseries.ptseries.nii</code>), where each column corresponds to a brain region, and each row to a timepoint. Ideal for computing ROI-to-ROI connectivity matrices or performing graph and network analyses.
  </p>
</details>

<details>
  <summary><strong>#3 Connectivity Matrices</strong> (<code>*_seg-&lt;PARC&gt;_stat-pearsoncorrelation_relmat.tsv</code>)</summary>
  <p>
  Tab-delimited matrices of pairwise Pearson correlations between atlas regions, computed from the parcellated time series. Useful for quick inspection, validation, or as input for group-level analyses when region-level connectivity is sufficient.
  </p>
</details>

<details>
  <summary><strong>#4 Motion Detection and Confound Files</strong> (<code>*_&lt;design|motion|outliers&gt;.tsv</code>)</summary>
  <p>
  Include framewise displacement values and nuisance regressor design files. The design files (<code>*_design.tsv</code>) contain one column per regressor (e.g., motion parameters and one-hot indicators for high-motion outlier volumes). Recommended for identifying and filtering low-quality data before group analyses.
  </p>
</details>

## Other Useful Derivatives

### Brain Volume and Segmentation ROIs (BIBSNet)

<p style="font-size: 15px;">
    <strong>Brain Segmentations</strong> (<code>sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes.tsv</code>)<br>
    Brain volumes computed for segmented ROIs in native T1w/T2w space.
</p>

<br>