<p style="font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

# MRI Derivatives Quick Start Guide

## XCP-D Functional Connectivity Outputs

The **XCP-D** pipeline produces a wide range of outputs derived from fMRIPrep-preprocessed data. For most functional connectivity (FC) analyses, users will primarily work with the **denoised timeseries**, **parcellated timeseries**, and **quality assessment metrics**. See full HBCD derivative file outputs [here](../mri//fmri.md#xcpd).

<p style="font-size: 15px;">
    <strong>Denoised Timeseries</strong> (<code>*space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii</code>)<br>
    Fully preprocessed, temporally filtered, and nuisance-regressed BOLD time series in standard or native space. Suitable for voxelwise FC analyses, seed-based correlation maps, or other data-driven connectivity methods.
<br>
<br>
    <strong>Parcellated Timeseries</strong> (<code>*atlas-*_timeseries.tsv</code>)<br>
    Contain mean time series extracted from brain regions defined by a parcellation atlas (Gordon, Glasser, etc.). Columns correspond to regions (nodes), and rows correspond to timepoints. Ideal for computing region-to-region (ROI-to-ROI) connectivity matrices or performing graph/network analyses.
<br>
<br>
    <strong>Connectivity Matrices</strong> (<code>*atlas-*_correlation.tsv</code>)<br>
    Precomputed correlation matrices derived from the parcellated time series. Useful for quick inspection, validation, or as input to group-level analyses when region-level connectivity is sufficient.
<br>
<br>
    <strong>Quality Control and Confound Files</strong> (<code>*desc-confounds_timeseries.tsv</code>, <code>*desc-qcvars.tsv</code>)<br>
    Contain nuisance regressors (e.g., motion parameters, aCompCor components, global signal) and quality control metrics (e.g., framewise displacement, DVARS, tSNR). Recommended for identifying and filtering low-quality scans or participants before group analyses.
<br>
<br>
    <strong>Standard-Space Derivatives</strong> (<code>space-MNI152NLin6Asym_desc-denoised_bold.nii.gz</code>)<br>
    Denoised BOLD data transformed to MNI standard space for cross-subject alignment. Recommended for group-level and atlas-based connectivity analyses where spatial correspondence is required.
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
