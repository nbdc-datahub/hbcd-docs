<p style="font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

# MRI Derivatives Quick Start Guide

## Structural Derivatives (XCP-D)

The **XCP-D** pipeline produces a wide range of outputs derived from fMRIPrep-preprocessed data. Most structural analyses focus on **cortical thickness**, **curvature**, and **sulcal depth** files, often summarized within atlas-defined regions or compared across subjects to study cortical morphology and brain development.

<p style="font-size: 15px;">
    <strong>Cortical Thickness</strong> (<code>*hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_midthickness.surf.gii</code>)<br>
    Surface-based maps of cortical thickness (in millimeters) for each hemisphere. Generated from reconstructed cortical surfaces and aligned to the standard fsLR template. Commonly averaged within ROIs or compared across subjects to assess cortical development, aging, or group differences.
<br>
<br>
    <strong>Curvature</strong> (<code>*space-fsLR_den-91k_curv.dscalar.nii</code>)<br>
    Measures of mean surface curvature, representing local folding patterns of the cortex. Positive values correspond to sulci (inward folds) and negative values to gyri (outward folds). Useful for studying cortical folding patterns or as a control variable in morphometric analyses.
<br>
<br>
    <strong>Sulcal Depth</strong> (<code>*space-fsLR_den-91k_sulc.dscalar.nii</code>)<br>
    Quantifies the depth of cortical sulci relative to the surrounding gyri. Often used as an index of cortical morphology and can complement curvature measures in structural analyses.
<br>
<br>
    <strong>Pial and White Matter Surfaces</strong> (<code>*_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span class="placeholder">&lt;pial|white&gt;</span>.surf.gii</code>)<br>
    Three-dimensional surface models of the gray–white matter and pial boundaries for each hemisphere. Useful for visualizing cortical features, computing surface-based metrics, or projecting functional data onto anatomy.
<br>
<br>
    <strong>Surface Area and Volume Metrics</strong> (<code>*_hemi-*_area.shape.gii</code>, <code>*_hemi-*_volume.shape.gii</code>)<br>
    Contain vertexwise estimates of cortical surface area and local gray matter volume. Commonly used in structural covariance analyses or region-level morphometric studies.
<br>
<br>
    <strong>Parcellated Structural Measures</strong> (<code>*_atlas-*_hemi-*_stats.tsv</code>)<br>
    Tabulated summaries (mean, median, standard deviation) of cortical measures (thickness, curvature, sulcal depth, area) within anatomical or functional ROIs defined by an atlas. Ideal for region-based statistical analysis and group comparisons.
</p>


## Functional Connectivity (XCP-D)

For most functional connectivity (FC) analyses, users will primarily work with the **denoised timeseries**, **parcellated timeseries**, and **quality assessment metrics**. See full HBCD derivative file outputs [here](../mri//fmri.md#xcpd).

<p style="font-size: 15px;">
    <strong>Denoised Timeseries</strong> (<code>*space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii</code>)<br>
    Fully preprocessed, temporally filtered, and nuisance-regressed BOLD time series in standard or native space. Suitable for voxelwise FC analyses, seed-based correlation maps, or other data-driven connectivity methods.
<br>
<br>
    <strong>Parcellated Timeseries</strong> (<code>*space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_den-91k_stat-mean_timeseries.ptseries.nii</code>)<br>
    Mean time series extracted from brain regions defined by a parcellation atlas (including 4S{X}56Parcels, Glasser, Gordon, MIDB, MyersLabonte, HCP, and Tian). Columns correspond to regions (nodes), and rows correspond to timepoints. Ideal for computing region-to-region (ROI-to-ROI) connectivity matrices or performing graph/network analyses.
<br>
<br>
    <strong>Connectivity Matrices</strong> (<code>*space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-pearsoncorrelation_relmat.tsv</code>)<br>
    Precomputed correlation matrices derived from the parcellated time series. Useful for quick inspection, validation, or as input to group-level analyses when region-level connectivity is sufficient.
<br>
<br>
    <strong>Quality Control and Confound Files</strong> (<code>*_<span class="placeholder">&lt;motion|outliers&gt;</span>.tsv</code>; <code>*_design.tsv</code>)<br>
    Contains framewise displacement for motion correction (<code>*<span class="placeholder">&lt;motion|outliers&gt;</span>.tsv</code>) and nuisance regressor (<code>*_design.tsv</code>) files with one column for each nuisance regressor, including one-hot encoded regressors indicating each of the high-motion outlier volumes. Recommended for identifying and filtering low-quality scans or participants before group analyses.
<br>
<br>
    <em>Most functional connectivity analyses rely on the denoised and parcellated timeseries files, which provide clean and interpretable measures of brain activity across regions or voxels.</em>
</p>


## Other Useful Derivatives

### Brain Volume and Segmentation ROIs (BIBSNet)

<p style="font-size: 15px;">
    <strong>Brain Segmentations</strong> (<code>sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes.tsv</code>)<br>
    Brain volumes computed for segmented ROIs in native T1w/T2w space.
</p>

<br>