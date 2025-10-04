# MRI Derivatives Quick Start Guide

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
    <td rowspan="2">XCP-D</td>
    <td><code>space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-curv_morph.tsv</code></td>
</tr>
<tr>
    <td><code>space-fsLR_den-91k_curv.dscalar.nii</code></td>
</tr>
<tr>
    <td rowspan="2">Sulcal Depth</td>
    <td rowspan="2">XCP-D</td>
    <td><code>space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-sulc_morph.tsv</code></td>
</tr>
<tr>
    <td><code>space-fsLR_den-91k_sulc.dscalar.nii</code></td>
</tr>
<tr>
    <td rowspan="2">Cortical thickness</td>
    <td rowspan="2">XCP-D</td>
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
    <th>Relevant Derivative(s)</th>
    <th>Pipeline</th>
 </thead>
<tbody>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Brain volumes computed for segmented ROIs in native T1w/T2w space</td>
    <td><code><span class="subses">SUBSES</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes.tsv</code></td>
    <td>BIBSNet</td>
</tr>
</tbody>
</table>


<pre style="font-size: 10px;" class="folder-tree">
hbcd/
|_ derivatives/ 
   |_ xcp_d/
      |_ sub-<span class="label">{ID}</span>/
         |_ ses-<span class="label">{V0X}</span>/
         |  |_ anat/
         |  |  |_ 
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-sulc_morph.tsv
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-thickness_morph.tsv
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span class="placeholder">&lt;inflated|vinflated&gt;</span>.surf.gii
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span class="placeholder">&lt;midthickness|pial|white&gt;</span>.surf.gii
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_den-91k_<span class="placeholder">&lt;curv|sulc|thickness&gt;</span>.dscalar.nii
</pre>
