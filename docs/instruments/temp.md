#### latest


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
  <td rowspan="5">sMRI & fMRI</td>
  <td rowspan="5"><code>anat/</code><br><code>fmap/</code><br><code>func/</code></td>
  <td>MRIQC - <a href="../../instruments/mri/smri/#mriqc" target="_blank">sMRI</a> & <a href="../../instruments/mri/fmri/#mriqc" target="_blank">fMRI</a></td>
  <td><code>img_mriqc_<span class="blue-text">&lt;T1w|T2w&gt;</span></code><br><code>img_mriqc_bold</code></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/smri/#bibsnet" target="_blank">BIBSNet</a></td>
  <td><code>img_bibsnet_space-<span class="blue-text">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes</code></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#nibabies" target="_blank">Infant fMRIPrep</a></td>
  <td></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#fs-mcribs" target="_blank">FreeSurfer & M-CRIB-S</a></td>
  <td></td>
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
  <td rowspan="2">qMRI</td>
  <td rowspan="2"><code>anat/</code></td>
  <td><a href="../../instruments/mri/qmri/#derivatives" target="_blank">SyMRI</a></td>
  <td></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/qmri/#derivatives" target="_blank">qMRI PostProc</a></td>
  <td></td>
</tr>
<tr>
  <td rowspan="2">dMRI</td>
  <td rowspan="2"><code>dwi/</code></td>
  <td><a href="../../instruments/mri/dmri/#qsiprep" target="_blank">QSIPrep</a></td>
  <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td>
</tr>
<tr>
<td><a href="mri/dmri/#qsirecon" target="_blank">QSIRecon</a></td>
<td></td>
<tr>
  <td>MRS</td>
  <td><code>mrs/</code></td>
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
  <td rowspan="5">sMRI & fMRI</td>
  <td rowspan="5"><code>anat/</code><br><code>fmap/</code><br><code>func/</code></td>
  <td>MRIQC - <a href="../../instruments/mri/smri/#mriqc" target="_blank">sMRI</a> & <a href="../../instruments/mri/fmri/#mriqc" target="_blank">fMRI</a></td>
  <td><code>img_mriqc_<span class="blue-text">&lt;T1w|T2w&gt;</span></code><br><code>img_mriqc_bold</code></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/smri/#bibsnet" target="_blank">BIBSNet</a></td>
  <td><code>img_bibsnet_space-<span class="blue-text">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes</code></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#nibabies" target="_blank">Infant fMRIPrep</a></td>
  <td></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#fs-mcribs" target="_blank">FreeSurfer & M-CRIB-S</a></td>
  <td></td>
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
  <td rowspan="2">qMRI</td>
  <td rowspan="2"><code>anat/</code></td>
  <td><a href="../../instruments/mri/qmri/#derivatives" target="_blank">SyMRI</a></td>
  <td></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/qmri/#derivatives" target="_blank">qMRI PostProc</a></td>
  <td></td>
</tr>
<tr>
  <td rowspan="6">dMRI</td>
  <td rowspan="6"><code>dwi/</code></td>
  <td><a href="../../instruments/mri/dmri/#qsiprep" target="_blank">QSIPrep</a></td>
  <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td>
</tr>
<tr>
<td><a href="mri/dmri/#qsirecon" target="_blank">QSIRecon</a></td>
<td></td>
<tr>
  <td><a href="../../instruments/mri/dmri/#qsirecon-DSIStudio" target="_blank">QSIRecon-DSI Studio</a></td>
  <td></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/dmri/#qsirecon-DIPYDKI" target="_blank">QSIRecon-DIPY DKI</a></td>
  <td></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/dmri/#qsirecon-TORTOISE" target="_blank">QSIRecon-TORTOISE MAP-MRI</a></td>
  <td></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/dmri/#qsirecon-TORTOISE" target="_blank">QSIRecon-TORTOISE Tensor</a></td>
  <td></td>
</tr>
<tr>
  <td>MRS</td>
  <td><code>mrs/</code></td>
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


# ALT


#### MRI table for raw bids, derivs, and derived tabulated

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Modality</th>
  <th>Derivatives</th>
  <th>Tabulated Data</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="10">sMRI & fMRI</td>
  <td>MRIQC - <a href="../../instruments/mri/smri/#mriqc" target="_blank">sMRI</a> & <a href="../../instruments/mri/fmri/#mriqc" target="_blank">fMRI</a></td>
  <td><code>img_mriqc_<span class="blue-text">&lt;T1w|T2w&gt;</span></code><br><code>img_mriqc_bold</code></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/smri/#bibsnet" target="_blank">BIBSNet</a></td>
  <td><code>img_bibsnet_space-<span class="blue-text">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes</code></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#nibabies" target="_blank">Infant fMRIPrep</a></td>
  <td></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#fs-mcribs" target="_blank">FreeSurfer & M-CRIB-S</a></td>
  <td></td>
</tr>
<tr>
  <td rowspan="6"><a href="../../instruments/mri/fmri/#xcpd" target="_blank">XCP-D</a></td>
  <td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-curv_morph</code></td>
</tr>
<tr>
  <td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-sulc_morph</code></td>
</tr>
<tr>
  <td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-thickness_morph</code></td>
</tr>
<tr>
  <td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-alff_bold</code></td>
</tr>
<tr>
  <td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-coverage_bold</code></td>
</tr>
<tr>
  <td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-reho_bold</code></td>
</tr>
<tr>
  <td rowspan="2">qMRI</td>
  <td><a href="../../instruments/mri/qmri/#derivatives" target="_blank">SyMRI</a></td>
  <td></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/qmri/#derivatives" target="_blank">qMRI PostProc</a></td>
  <td></td>
</tr>
<tr>
  <td rowspan="6">dMRI</td>
  <td><a href="../../instruments/mri/dmri/#qsiprep" target="_blank">QSIPrep</a></td>
  <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td>
</tr>
<tr>
<td><a href="mri/dmri/#qsirecon" target="_blank">QSIRecon</a></td>
<td></td>
<tr>
  <td><a href="../../instruments/mri/dmri/#qsirecon-DSIStudio" target="_blank">QSIRecon-DSI Studio</a></td>
  <td></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/dmri/#qsirecon-DIPYDKI" target="_blank">QSIRecon-DIPY DKI</a></td>
  <td></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/dmri/#qsirecon-TORTOISE" target="_blank">QSIRecon-TORTOISE MAP-MRI</a></td>
  <td></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/dmri/#qsirecon-TORTOISE" target="_blank">QSIRecon-TORTOISE Tensor</a></td>
  <td></td>
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
