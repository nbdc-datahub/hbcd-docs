#### MRI table for raw bids, derivs, and derived tabulated

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Modality</th>
  <th>Raw</th>
  <th>Derivatives</th>
  <th>Tabulated Data</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="5">Structural & Functional MRI</td>
  <td rowspan="5"><code>anat/</code><br><code>fmap/</code><br><code>func/</code></td>
  <td>MRIQC - <a href="../../instruments/mri/smri/#mriqc" target="_blank">sMRI</a> & <a href="../../instruments/mri/fmri/#mriqc" target="_blank">fMRI</a></td>
  <td style="text-align: center;"><i style="color: green;" class="fa-solid fa-check"></i></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/smri/#bibsnet" target="_blank">BIBSNet</a></td>
  <td style="text-align: center;"><i style="color: green;" class="fa-solid fa-check"></i></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#nibabies" target="_blank">Infant fMRIPrep</a></td>
  <td style="text-align: center;"><i style="color: red;" class="fa-solid fa-xmark"></i></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#fs-mcribs" target="_blank">FreeSurfer & M-CRIB-S</a></td>
  <td style="text-align: center;"><i style="color: red;" class="fa-solid fa-xmark"></i></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#xcpd" target="_blank">XCP-D</a></td>
  <td style="text-align: center;"><i style="color: green;" class="fa-solid fa-check"></i></td>
</tr>
<tr>
  <td rowspan="2">Quantitative MRI</td>
  <td rowspan="2"><code>anat/</code></td>
  <td><a href="../../instruments/mri/qmri/#derivatives" target="_blank">SyMRI</a></td>
  <td style="text-align: center;"><i style="color: red;" class="fa-solid fa-xmark"></i></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/qmri/#derivatives" target="_blank">qMRI PostProc</a></td>
  <td style="text-align: center;"><i style="color: red;" class="fa-solid fa-xmark"></i></td>
</tr>
<tr>
  <td rowspan="6">Diffusion MRI</td>
  <td rowspan="6"><code>dwi/</code></td>
  <td><a href="../../instruments/mri/dmri/#qsiprep" target="_blank">QSIPrep</a></td>
  <td style="text-align: center;"><i style="color: green;" class="fa-solid fa-check"></i></td>
</tr>
<tr>
<td><a href="mri/dmri/#qsirecon" target="_blank">QSIRecon</a></td>
  <td style="text-align: center;"><i style="color: red;" class="fa-solid fa-xmark"></i></td>
<tr>
  <td><a href="../../instruments/mri/dmri/#qsirecon-DSIStudio" target="_blank">QSIRecon-DSI Studio</a></td>
  <td style="text-align: center;"><i style="color: red;" class="fa-solid fa-xmark"></i></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/dmri/#qsirecon-DIPYDKI" target="_blank">QSIRecon-DIPY DKI</a></td>
  <td style="text-align: center;"><i style="color: red;" class="fa-solid fa-xmark"></i></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/dmri/#qsirecon-TORTOISE" target="_blank">QSIRecon-TORTOISE MAP-MRI</a></td>
  <td style="text-align: center;"><i style="color: red;" class="fa-solid fa-xmark"></i></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/dmri/#qsirecon-TORTOISE" target="_blank">QSIRecon-TORTOISE Tensor</a></td>
  <td style="text-align: center;"><i style="color: red;" class="fa-solid fa-xmark"></i></td>
</tr>
<tr>
  <td>MRS</td>
  <td><code>mrs/</code></td>
  <td><a href="../../instruments/mri/mrs/#derivatives" target="_blank">OSPREY-BIDS</a></td>
  <td style="text-align: center;"><i style="color: green;" class="fa-solid fa-check"></i></td>
</tr>
</tbody>
</table>

## tables

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr><td colspan="4" style="color: teal;"><b>Instrument Data</b></td></tr>
<tr>
<th style="width: 5%;"></th>
<th style="width: 30%;">Instrument</th>
<th style="width: 30%;">Construct</th>
<th style="width: 30%;"><span class="tooltip tooltip-left"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="mri/questionnaire" target="_blank">Pre-Scan Questionnaire</a></td>
  <td>Sleeping Scan Prep</td>
  <td><code>img_ra_prep</code></td>
</tr>
<tr>
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="mri/qc/#brainswipes" target="_blank">BrainSwipes</a></td>
  <td>Manual QC</td>
  <td><code>img_brainswipes_xcpd-bold</code></td>
</tr>
<tr><td colspan="2" style="border-top: 2px solid #cce7e7;"></td></tr>
</tbody>
<tr><td colspan="4" style="color: teal;"><b>Pipeline Derivatives in Tabulated Form</b></td></tr>
<thead>
  <tr>
    <th style="width: 5%;"></th>
    <th style="width: 30%;">Modality</th>
    <th style="width: 30%;">Pipeline</th>
    <th style="width: 30%;"><span class="tooltip tooltip-left"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name</th>
  </tr>
</thead>
<tbody>
<tr>
  <td rowspan="3"><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td rowspan="3">sMRI & fMRI</td>
  <td>MRIQC - <a href="../../instruments/mri/smri/#mriqc" target="_blank">sMRI</a> & <a href="../../instruments/mri/fmri/#mriqc" target="_blank">fMRI</a></td>
  <td><code>img_mriqc_<span class="blue-text">&lt;T1w|T2w&gt;</span></code><br><code>img_mriqc_bold</code></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/smri/#bibsnet" target="_blank">BIBSNet</a></td>
  <td><code>img_bibsnet_space-<span class="blue-text">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes</code></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#xcpd" target="_blank">XCP-D</a></td>
  <td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-curv_morph</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-sulc_morph</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-thickness_morph</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-alff_bold</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-coverage_bold</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-reho_bold</code>
  </td>
</tr>
<tr>
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td>dMRI</td>
  <td><a href="../../instruments/mri/dmri/#qsiprep" target="_blank">QSIPrep</a></td>
  <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td>
</tr>
<tr>
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td>MRS</td>
  <td><a href="../../instruments/mri/mrs/#derivatives" target="_blank">OSPREY-BIDS</a></td>
      <td>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_AlphaCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_CSFWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_TissCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_rawWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_amplMets_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_tCr_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_qm_processed_spectra</code><br>
    <code>img_osprey_unedited_qm_processed_spectra</code>
    </td>
</tr>
<tr>
  <td colspan="4">
    <strong>Label Values Legend</strong><br>
    <b style="color: #0077cc;">&lt;PARC&gt;</b> (parcellations): 4S-{1-10}56Parcels, Glasser, Gordon, MIDB, MyersLabonte, HCP, Tian (HCP & Tian functional only)<br>
    <b style="color: #0077cc;">&lt;Q&gt;</b> (quantification method): HERCULES_diff1, HERCULES_diff2, HERCULES_sum, unedited_A
  </td>
</tr>
</tbody>
</table>

<br>
<br>
<br>
<br>

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Modality</th>
  <th>Pipeline</th>
  <th>Tabulated Data</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="3">sMRI & fMRI</td>
  <td>MRIQC - <a href="../../instruments/mri/smri/#mriqc" target="_blank">sMRI</a> & <a href="../../instruments/mri/fmri/#mriqc" target="_blank">fMRI</a></td>
  <td><code>img_mriqc_<span class="blue-text">&lt;T1w|T2w&gt;</span></code><br><code>img_mriqc_bold</code></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/smri/#bibsnet" target="_blank">BIBSNet</a></td>
  <td><code>img_bibsnet_space-<span class="blue-text">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes</code></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#xcpd" target="_blank">XCP-D</a></td>
  <td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-curv_morph</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-sulc_morph</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-thickness_morph</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-alff_bold</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-coverage_bold</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-reho_bold</code>
  </td>
</tr>
<tr>
  <td>dMRI</td>
  <td><a href="../../instruments/mri/dmri/#qsiprep" target="_blank">QSIPrep</a></td>
  <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td>
</tr>
<tr>
  <td>MRS</td>
  <td><a href="../../instruments/mri/mrs/#derivatives" target="_blank">OSPREY-BIDS</a></td>
      <td>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_AlphaCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_CSFWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_TissCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_rawWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_amplMets_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_tCr_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_qm_processed_spectra</code><br>
    <code>img_osprey_unedited_qm_processed_spectra</code>
    </td>
</tr>
<tr>
  <td colspan="4">
    <strong>Label Values Legend</strong><br>
    <b style="color: #0077cc;">&lt;PARC&gt;</b> (parcellations): 4S-{1-10}56Parcels, Glasser, Gordon, MIDB, MyersLabonte, HCP, Tian (HCP & Tian functional only)<br>
    <b style="color: #0077cc;">&lt;Q&gt;</b> (quantification method): HERCULES_diff1, HERCULES_diff2, HERCULES_sum, unedited_A
  </td>
</tr>
</tbody>
</table>
