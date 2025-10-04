<p style="font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

# MRI Derivatives Quick Start Guide

## XCP-D Functional Connectivity Outputs

The **XCP-D** pipeline produces a wide range of outputs derived from fMRIPrep-preprocessed data. For most functional connectivity (FC) analyses, users will primarily work with the **denoised timeseries**, **parcellated timeseries**, and **quality assessment metrics**. See full HBCD derivative file outputs [here](../mri//fmri.md#xcpd).

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
</p>


## Structural Data

### Curvature, Sulcal Depth, and Cortical Thickness

 <table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
 <thead>
    <th>Data/Metric of Interest</th>
    <th>Pipeline</th>
    <th>Relevant Derivative(s) - <code>sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_</code></th>
 </thead>
<tbody>
<tr>
    <td rowspan="2">Curvature</td>
    <td rowspan="2"><a href="../../mri/fmri/#xcpd">XCP-D</a></td>
    <td><code>space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-curv_morph.tsv</code></td>
</tr>
<tr>
    <td><code>space-fsLR_den-91k_curv.dscalar.nii</code></td>
</tr>
<tr>
    <td rowspan="2">Sulcal Depth</td>
    <td rowspan="2"><a href="../../mri/fmri/#xcpd">XCP-D</a></td>
    <td><code>space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-sulc_morph.tsv</code></td>
</tr>
<tr>
    <td><code>space-fsLR_den-91k_sulc.dscalar.nii</code></td>
</tr>
<tr>
    <td rowspan="2">Cortical thickness</td>
    <td rowspan="2"><a href="../../mri/fmri/#xcpd">XCP-D</a></td>
    <td><code>space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-thickness_morph.tsv</code></td>
</tr>
<tr>
    <td><code>space-fsLR_den-91k_thickness.dscalar.nii</code></td>
</tr>
</tbody>
</table>

### Brain Volume and Segmentation ROIs

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
 <thead>
    <th>Data/Metric of Interest</th>
    <th>Pipeline</th>
    <th>Relevant Derivative(s)</th>
 </thead>
<tbody>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Brain volumes computed for segmented ROIs in native T1w/T2w space</td>
    <td><a href="../../mri/smri/#bibsnet">BIBSNet</a></td>
    <td><code>sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes.tsv</code></td>
</tr>
</tbody>
</table>
