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

XCP-D provides several structural morphology measures derived from the fMRIPrep anatomical outputs. These surface-based derivatives are commonly used to assess cortical features such as **thickness**, **curvature**, and **sulcal depth**, often summarized within atlas-defined regions or compared across subjects to study cortical development and brain morphology.

specify location under anat/

<p style="font-size: 15px;">
    <strong>Cortical Thickness</strong> (<code>*_space-fsLR_den-91k_thickness.dscalar.nii</code>)<br>
    CIFTI scalar files containing surface-based maps of cortical thickness (in millimeters) for each hemisphere. Generated from reconstructed cortical surfaces and aligned to the standard <code>fsLR</code> template. Commonly averaged within ROIs or compared across subjects to assess cortical development, aging, or group differences.
<br>
<br>
    <strong>Curvature</strong> (<code>*_space-fsLR_den-91k_curv.dscalar.nii</code>)<br>
    Provides mean surface curvature values representing local cortical folding patterns of the cortex. Positive values correspond to sulci (inward folds) and negative values to gyri (outward folds). Useful for characterizing cortical folding or as a covariate in morphometric analyses.
<br>
<br>
    <strong>Sulcal Depth</strong> (<code>*_space-fsLR_den-91k_sulc.dscalar.nii</code>)<br>
    Measures the relative depth of cortical sulci compared to adjacent gyri. Often used alongside curvature to describe cortical shape and folding complexity.
<br>
<br>
    <strong>Parcellated Structural Measures</strong> (<code>*_space-fsLR_seg-&lt;PARC&gt;_stat-mean_desc-&lt;curv|sulc|thickness&gt;_morph.tsv</code>)<br>
    Tabulated summaries of cortical metrics (curvature, sulcal depth, thickness) within anatomical or functional regions defined by an atlas. Ideal for region-based statistical analysis and group comparisons.
<br>
<br>
    <strong>Pial and White Matter Surfaces</strong> (<code>*_hemi-&lt;L|R&gt;_space-fsLR_den-32k_&lt;pial|white&gt;.surf.gii</code>)<br>
    3D surface models representing the gray–white matter boundary and the pial surface for each hemisphere. Commonly used for visualizing cortical anatomy, computing surface-based metrics, or mapping functional data to anatomical space.
</p>

## Functional Connectivity (XCP-D)

XCP-D produces several derivative outputs designed for functional connectivity (FC) and time series analyses. These include **denoised BOLD data**, **parcellated time series**, and **derived connectivity matrices**, along with **frame displacement and confound files** to support motion correction and data quality assessment. Together, these provide clean and standardized measures of brain activity for both voxelwise and region-based network analyses.


specify location under func/ for xcpd derivs


<p style="font-size: 15px;">
    <strong>Denoised Timeseries</strong> (<code>*_space-fsLR_den-91k_desc-denoised_bold.dtseries.nii</code>; <code>*_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii</code>)<br>
    CIFTI dense time series containing fully preprocessed, temporally filtered, and nuisance-regressed BOLD data. Aligned to the standard <code>fsLR</code> surface template, these files are suitable for voxelwise FC analyses, seed-based correlation maps, or other data-driven connectivity methods.
<br>
<br>
    <strong>Parcellated Timeseries</strong> (<code>*_space-fsLR_seg-&lt;PARC&gt;_stat-mean_timeseries.tsv</code>)<br>
    Tabulated mean BOLD time series for each region in a the following atlases: <a href="https://github.com/PennLINC/AtlasPack">4S-X-56Parcels</a> (nodes 156-1056), Glasser, Gordon, MIDB, MyersLabonte, HCP, and Tian. Also available as CIFTI files (<code>*_stat-mean_timeseries.ptseries.nii</code>), where each column corresponds to a brain region, and each row to a timepoint. Ideal for computing ROI-to-ROI connectivity matrices or performing graph and network analyses.
<br>
<br>
    <strong>Connectivity Matrices</strong> (<code>*_space-fsLR_seg-&lt;PARC&gt;_stat-pearsoncorrelation_relmat.tsv</code>)<br>
    Tab-delimited matrices of pairwise Pearson correlations between atlas regions, computed from the parcellated time series. Useful for quick inspection, validation, or as input for group-level analyses when region-level connectivity is sufficient.
<br>
<br>
    <strong>Motion Detection and Confound Files</strong> (<code>*_&lt;motion|outliers|design&gt;.tsv</code>)<br>
    Include framewise displacement values and nuisance regressor design files. The design files (<code>*_design.tsv</code>) contain one column per regressor (e.g., motion parameters and one-hot indicators for high-motion outlier volumes). Recommended for identifying and filtering low-quality data before group analyses.<br>    
</p>

## Other Useful Derivatives

### Brain Volume and Segmentation ROIs (BIBSNet)

<p style="font-size: 15px;">
    <strong>Brain Segmentations</strong> (<code>sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes.tsv</code>)<br>
    Brain volumes computed for segmented ROIs in native T1w/T2w space.
</p>

<br>