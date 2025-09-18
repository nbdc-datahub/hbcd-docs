<p><strong><span class="emoji"><i class="fa-regular fa-lightbulb"></i></span> Also see <a href="eeg">EEG Overview page</a></strong></p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th></th>
      <th>Modality</th>
      <th>Name</th>
      <th><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table or <span class="tooltip tooltip-right"><i class="fa-solid fa-folder-open"></i><span class="tooltiptext">File-Based Data</span></span> Folder Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
        <td>All</td>
        <td style="word-wrap: break-word; white-space: normal;"><a href="mri/questionnaire" target="_blank">Pre-Scan Questionnaire</a></td>
        <td><code>img_ra_prep</code></td>
    </tr>
    <tr>
        <td><span class="tooltip tooltip-right"><i class="fa-solid fa-folder-open"></i><span class="tooltiptext">File-Based Data</span></span> - <strong><i>Raw BIDS</i></strong></td>
        <td><a href="../datacuration/rawbids/#anat" target="_blank">sMRI</a></td>
        <td></td>
        <td><i>rawdata/sub-&lt;label&gt;/ses-&lt;label&gt;/anat/</i></td>
    </tr>
    <tr>
        <td><span class="tooltip tooltip-right"><i class="fa-solid fa-folder-open"></i><span class="tooltiptext">File-Based Data</span></span> - <strong><i>Raw BIDS</i></strong></td>
        <td><a href="../datacuration/rawbids/#eeg" target="_blank">fMRI</a></td>
        <td></td>
        <td><i>rawdata/sub-&lt;label&gt;/ses-&lt;label&gt;/{func|fmap}/</i></td>
    </tr>
  </tbody>
  </table>



### MRI ALT


  <p><strong><span class="emoji"><i class="fa-regular fa-lightbulb"></i></span> Also see 
    <a href="mri">Overview & MRI Protocols</a> and 
    <a href="mri/qc"> HBCD MR Quality Control Procedures</a></strong>
  </p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <!-- First header row -->
    <tr>
      <th rowspan="2">Name</th>
      <th style="text-align: center;" colspan="2"><span class="tooltip tooltip-right">File-Based Data<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span></th>
      <th style="width: 60%;" rowspan="2">Table Name(s)</th>
    </tr>
    <!-- Second header row -->
    <tr>
      <th style="width: 10%;">
        <i class="fas fa-hammer"></i> Raw Data
      </th>
      <th style="width: 10%;">
        <i class="fas fa-cog"></i> Derivatives
      </th>
    </tr>
  </thead>
    <tbody>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="mri/questionnaire" target="_blank">Pre-Scan Questionnaire</a></td>
      <td colspan="2"><i>Tabulated data only</i><br><strong>Construct</strong>: Sleeping Scan Prep</td>
      <td><code>img_ra_prep</code></td>
    <!-- sMRI -->
    <tr>
    <td><span class="tooltip tooltip-right"><a href="mri/smri" target="_blank">sMRI</a><span class="tooltiptext">Structural MRI</span></span></td>
    <td><a href="../datacuration/rawbids/#anatomical-anat" target="_blank"><code>anat/</code></a></td>
    <td>
      •<a href="../datacuration/derivatives/#bibsnet-bibsnet" target="_blank">BIBSNet</a><br>
      •<a href="../datacuration/derivatives/#mriqc-mriqc" target="_blank">MRIQC</a><br>
      •<a href="../datacuration/derivatives/#infant-fmriprep-nibabies" target="_blank">Infant-fMRIPrep</a><br>
      •<a href="../datacuration/derivatives/#xcp-d-xcp_d" target="_blank">XCP-D</a>
    </td>
    <td><code>img_brainswipes_xcpd-T2w</code><br>
        <code>img_mriqc_<span class="blue-text">&lt;T1w|T2w&gt;</span></code><br>
        <code>img_bibsnet_space-<span class="blue-text">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-A&gt;</span>_stat-mean_desc-curv_morph</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-A&gt;</span>_stat-mean_desc-sulc_morph</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-A&gt;</span>_stat-mean_desc-thickness_morph</code>
    </td>
    </tr>
    <!-- fMRI -->
    <tr>
    <td><span class="tooltip tooltip-right"><a href="mri/fmri" target="_blank">fMRI</a>
    <span class="tooltiptext">Functional MRI</span>
    </span>
    </td>
    <td>
        •<a href="../datacuration/rawbids/#functional-func-and-fieldmaps-fmap" target="_blank"><code>func/</code></a><br>
        •<a href="../datacuration/rawbids/#functional-func-and-fieldmaps-fmap" target="_blank"><code>fmap/</code></a>
    </td>
    <td>
        •<a href="../datacuration/derivatives/#infant-fmriprep-nibabies" target="_blank">Infant-fMRIPrep</a><br>
        •<a href="../datacuration/derivatives/#xcp-d-xcp_d" target="_blank">XCP-D</a>
    </td>
    <td><code>img_brainswipes_xcpd-bold</code><br>
        <code>img_mriqc_bold</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-F&gt;</span>_stat-alff_bold</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-F&gt;</span>_stat-coverage_bold</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-F&gt;</span>_stat-reho_bold</code>
    </td></tr>
    <!-- dMRI -->
    <tr>
    <td>
        <a href="mri/dmri" target="_blank">dMRI</a>
    </td>
    <td><a href="../datacuration/rawbids/#diffusion-dwi" target="_blank"><code>dwi/</code></a></td>
    <td>
        •<a href="../datacuration/derivatives/#qsiprep-qsiprep" target="_blank">QSIPrep</a><br>
        •<a href="../datacuration/derivatives/#qsirecon" target="_blank">QSIRecon</a>
    </td>
    <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td>
    </tr>
    <!-- qMRI -->
    <tr>
    <td>
        <a href="mri/qmri" target="_blank">qMRI</a>
    </td>
    <td><code>anat/</code></td>
    <td>
        • <a href="../datacuration/derivatives/#symri-symri" target="_blank">SyMRI</a><br>
        • <a href="../datacuration/derivatives/#qmri-postproc-qmri_postproc" target="_blank">qMRI Postproc</a>
    </td>
    <td>N/A</td>
    </tr>
    <!-- MRS -->
    <tr>
    <td><a href="mri/mrs" target="_blank">MRS</a></td>
    <td><code>mrs/</code></td>
    <td><a href="../datacuration/derivatives/#osprey-bids-osprey" target="_blank">OSPREY-BIDS</a></td>
    <td>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code><br>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_AlphaCorrWaterScaled_Voxel_1_Basis_1</code><br>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_CSFWaterScaled_Voxel_1_Basis_1</code><br>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_TissCorrWaterScaled_Voxel_1_Basis_1</code><br>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_rawWaterScaled_Voxel_1_Basis_1</code><br>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_amplMets_Voxel_1_Basis_1</code><br>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_tCr_Voxel_1_Basis_1</code><br>
        <code>img_osprey_HERCULES_qm_processed_spectra</code><br>
        <code>img_osprey_unedited_qm_processed_spectra</code>
    </td>
    </tr>
</tbody>
</table>
<details open>
<summary>Label Values Legend</summary>
<p style="margin-bottom: 0; padding-bottom: 0; font-size: smaller;">
  <b style="color: #0077cc;">SEG-A</b>: 4S{1-10}00Parcels, Glasser, Gordon, MIDB, MyersLabonte<br>
  <b style="color: #0077cc;">SEG-F</b>: 4S{1-10}00Parcels, Glasser, Gordon, MIDB, MyersLabonte, HCP, Tian<br>
  <b style="color: #0077cc;">PROC</b>: HERCULES_diff1, HERCULES_diff2, HERCULES_sum, unedited_A
</p>
</details>
