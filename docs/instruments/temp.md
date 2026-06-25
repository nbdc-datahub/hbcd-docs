

<!-- MRI -->
<div id="mri" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-brain"></i></span>
  <span class="text-with-link">
    <span class="text">Imaging & Tabular Imaging</span>
    <a class="anchor-link" href="#mri" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<!-- FILE-BASED IMAGING DATA -->
<span class="table-title"><i class="fa-solid fa-folder-open header-icon"></i> Imaging Domain</span>
<p>See <a href="mri/#release-data" target="_blank">Release Data</a> summary and other sections of the MR Overview page as well as <a href="mri/qc/" target="_blank">MR Quality Control</a>.</p>
<table class="compact-table-no-vertical-lines index">
<thead>
<tr>
<th>Modality</th>
<th>Acronym</th>
<th style="text-align: center;">README</th>
<th>Raw BIDS <span class="subtle">(see <a href="mri/rawbids/" target="_blank">Raw MR BIDS</a>)</span></th>
<th>Pipeline Derivatives <span class="subtle">(see <a href="../standards/processing/" target="_blank">Processing Pipelines</a>)</span></th>
</tr>
</thead>
<tbody>
<tr>
  <td>Structural MRI</td>  <td>sMRI</td>
  <td style="text-align: center;"><a href="mri/smri" target="_blank"></a><i class="fa-brands fa-readme table-icon"></i></td>
  <td><code>anat/</code></td>
  <td>MRIQC • BIBSNet</td>
</tr>
<tr>
  <td>Functional MRI</td>  <td>fMRI</td>
  <td style="text-align: center;"><a href="mri/fmri" target="_blank"></a><i class="fa-brands fa-readme table-icon"></i></td>
  <td><code>func/</code>, <code>fmap/</code></td>
  <td>
    MRIQC • Infant fMRIPrep + FreeSurfer / M-CRIB-S • XCP-D</td>
</tr>
<tr>
  <td>Quantitative MRI</td>  <td>qMRI</td>
  <td style="text-align: center;"><a href="mri/qmri" target="_blank"></a><i class="fa-brands fa-readme table-icon"></i></td>
  <td><code>anat/</code>, <code>fmap/</code></td>
  <td>SyMRI & qMRI PostProc</td>
</tr>
<tr>
  <td>Diffusion MRI</td>  <td>dMRI</td>
  <td style="text-align: center;"><a href="mri/dmri" target="_blank"></a><i class="fa-brands fa-readme table-icon"></i></td>
  <td><code>dwi/</code></td>
  <td>QSIPrep & QSIRecon (DSI Studio, DIPY DKI, TORTOISE)</td>
</tr>
<tr>
  <td>MR Spectroscopy</td>  <td>MRS</td>
  <td style="text-align: center;"><a href="mri/mrs" target="_blank"></a><i class="fa-brands fa-readme table-icon"></i></td>
  <td><code>mrs/</code></td>
  <td>OSPREY-BIDS</td>
</tr>
</tbody>
</table>


<!-- TABULATED DATA -->
<span class="table-title"><i class="fa-solid fa-table header-icon"></i> Tabular Imaging Domain</span>
<div class="table-legend">
  <span class="legend-item">
    <i class="fa-solid fa-diagram-project legend-icon"></i> = 
    Tabulated pipeline derivatives (<a href="../datacuration/overview/#tabulated-pipeline-derivatives" target="_blank"><i>see details</i></a>)
  </span>
</div>

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Table</th>
<th>Construct</th>
<th>Table Name</th>
</tr>
</thead>
<tbody>

<tr>
<td><a href="mri/summary-forms" target="_blank">MRI Data Summary Form</a></td>
<td>Admin</td>
<td><code>mri_ra_chkl_data</code></td>
</tr>
<tr>
<td><a href="mri/summary-forms" target="_blank">MRI Scan Session Summary Form</a></td>
<td>Admin</td>
<td><code>mri_ra_chkl_scan</code></td>
</tr>
<tr>
<td><a href="mri/prescan-questionnaire" target="_blank">Pre/Post Scan Prep</a></td>
<td>Infant Sleep</td>
<td><code>mri_ra_prep</code></td>
</tr>
<tr>
<td><a href="mri/qc#brainswipes" target="_blank">BrainSwipes</a></td>
<td>Manual QC</td>
<td>
<code>img_brainswipes_xcpd_hash-0f306a2f+0ef9c88a_T2w</code><br>
<code>img_brainswipes_xcpd_hash-0f306a2f+0ef9c88a_bold</code><br>
<code>img_brainswipes_xcpd_hash-2afa9081+0ef9c88a_T1w</code><br>
<code>img_brainswipes_xcpd_hash-2afa9081+0ef9c88a_bold</code><br>
</td>
</tr>
<tr>
<td>MRIQC</td><td><i class="fa-solid fa-diagram-project header-icon"></i></td>
<td><code>img_mriqc_T1w</code><br><code>img_mriqc_T2w</code><br><code>img_mriqc_bold</code></td>
</tr>
<tr>
<td>BIBSNet</td><td><i class="fa-solid fa-diagram-project header-icon"></i></td>
<td><code>img_bibsnet_space-T1w_desc-aseg_volumes</code><br><code>img_bibsnet_space-T2w_desc-aseg_volumes</code></td>
</tr>
<tr>
  <td>XCP-D</td>
  <td><i class="fa-solid fa-diagram-project header-icon"></i></td>
  <td>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-mean_desc-curv_morph</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-mean_desc-sulc_morph</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-mean_desc-thickness_morph</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-alff_bold</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-coverage_bold</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-reho_bold</code>
  <br><br>
  <code><span class="blue-text">{HASH}</span></code>  values: <code>0f306a2f+0ef9c88a</code>; <code>2afa9081+0ef9c88a</code><br>
  <code><span class="blue-text">{PARC}</span></code>  values: <code>Glasser</code>, <code>Gordon</code>, etc - <a href="mri/fmri/#parc" target="_blank">see full atlas list →</a></code><br><br>
  <a href="mri/tables/xcpd.html" target="_blank">See full file list →</a></td>
</tr>
<tr>
  <td>QSIPrep</td>
  <td><i class="fa-solid fa-diagram-project header-icon"></i></td>
  <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td>
</tr>
<tr>
<td>OSPREY-BIDS</td>
<td><i class="fa-solid fa-diagram-project header-icon"></i></td>
<td>
<code><span class="blue-text"># HERCULES diff1, diff2, and sum files</span></code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_AlphaCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_CSFWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_TissCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_rawWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_amplMets_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_tCr_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_qm_processed_spectra</code><br><br>
    <code><span class="blue-text"># Unedited files</span></code><br>
    <code>img_osprey_unedited_A_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_AlphaCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_CSFWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_TissCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_rawWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_amplMets_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_tCr_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_qm_processed_spectra</code><br><br>
    <a href="mri/tables/osprey.html" target="_blank">See full file list →</a>
    </td>
</tr>
</tbody>
</table>



<br><br><br><br><br>
<table class="compact-table-no-vertical-lines index">
<thead>
<tr>
<th>Table</th>
<th>Construct</th>
<th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<a href="mri/mri-forms/#mri-scan-session-data-summary-forms" target="_blank">
MRI Scan Session Summary Form <br> MRI Data Summary Form
</a></td>
<td>Pre-MRI Tech Checklist 1<br>
Post-MRI Tech Checklist 2</td>
<td><code>mri_ra_chkl_scan</code><br>
    <code>mri_ra_chkl_data</code>
</td>
</tr>
<!-- <tr>
<td><a href="mri/mri-forms/#mri-scan-session-data-summary-forms" target="_blank">MRI Scan Session Summary Form</a></td>
<td>Pre-MRI Tech Checklist 1</td>
<td><code>mri_ra_chkl_scan</code></td>
</tr>
<tr>
<td><a href="mri/mri-forms/#mri-scan-session-data-summary-forms" target="_blank">MRI Data Summary Form</a></td>
<td>Post-MRI Tech Checklist 2</td>
<td><code>mri_ra_chkl_data</code></td>
</tr> -->
<tr>
<td><a href="mri/prescan-questionnaire" target="_blank">Pre/Post Scan Prep</a></td>
<td>Infant Sleep</td>
<td><code>mri_ra_prep</code></td>
</tr>
<tr>
<td><a href="mri/qc#brainswipes" target="_blank">BrainSwipes</a></td>
<td>Manual QC</td>
<td>
<code>img_brainswipes_xcpd_hash-0f306a2f+0ef9c88a_<span class="blue-text">{T2w|bold}</span></code><br>
<code>img_brainswipes_xcpd_hash-2afa9081+0ef9c88a_<span class="blue-text">{T1w|bold}</span></code>
<!-- 
<code>img_brainswipes_xcpd_hash-0f306a2f+0ef9c88a_T2w</code><br>
<code>img_brainswipes_xcpd_hash-0f306a2f+0ef9c88a_bold</code><br>
<code>img_brainswipes_xcpd_hash-2afa9081+0ef9c88a_T1w</code><br>
<code>img_brainswipes_xcpd_hash-2afa9081+0ef9c88a_bold</code><br> -->
</td>
</tr>
</tbody>
</table>
<!-- PIPELINE DERIVATIVES -->
<p class="subtle">Tabulated Pipeline Derivatives (<a href="../datacuration/overview/#tabulated-pipeline-derivatives" target="_blank"><i>see details</i></a>)</p>
<table class="table-no-vertical-lines index">
<thead>
<tr>
<th>Processing Pipeline Source</th>
<th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>MRIQC</td>
<td><code>img_mriqc_T1w</code><br><code>img_mriqc_T2w</code><br><code>img_mriqc_bold</code></td>
</tr>
<tr>
<td>BIBSNet</td>
<td><code>img_bibsnet_space-T1w_desc-aseg_volumes</code><br><code>img_bibsnet_space-T2w_desc-aseg_volumes</code></td>
</tr>
<tr>
  <td>XCP-D</td>
  <td>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-mean_desc-curv_morph</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-mean_desc-sulc_morph</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-mean_desc-thickness_morph</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-alff_bold</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-coverage_bold</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-reho_bold</code>
  <br><br>
  <code><span class="blue-text">{HASH}</span></code>  values: <code>0f306a2f+0ef9c88a</code>; <code>2afa9081+0ef9c88a</code><br>
  <code><span class="blue-text">{PARC}</span></code>  values: <code>Glasser</code>, <code>Gordon</code>, etc - <a href="mri/fmri/#parc" target="_blank">see full atlas list →</a></code><br><br>
  <a href="mri/tables/xcpd.html" target="_blank">See full file list →</a></td>
</tr>
<tr>
  <td>QSIPrep</td>
  <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td>
</tr>
<tr>
<td>OSPREY-BIDS</td>
<td>
<code><span class="blue-text"># HERCULES diff1, diff2, and sum files</span></code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_AlphaCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_CSFWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_TissCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_rawWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_amplMets_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_tCr_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_qm_processed_spectra</code><br><br>
    <code><span class="blue-text"># Unedited files</span></code><br>
    <code>img_osprey_unedited_A_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_AlphaCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_CSFWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_TissCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_rawWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_amplMets_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_tCr_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_qm_processed_spectra</code><br><br>
    <a href="mri/tables/osprey.html" target="_blank">See full file list →</a>
    </td>
</tr>
</tbody>
</table>
</div>
