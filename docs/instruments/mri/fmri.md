# Functional MRI (fMRI)

<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text">
    Additional Resources
  </span>
</div>
<div class="notification-static-content">
<p> 
• <a href="..">Overview & MR Protocols</a><br>
• <a href="../qc">Quality Control Procedures</a><br>
</p>
</div>

## Release Data

<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Responsible Use Warning</i></span>
  <a class="anchor-link" href="#alert" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p>Head motion is a serious issue for neuroimaging, and especially for resting state fMRI. It creates brain-wide artifactual effects including elevated short-distance connectivity and attenuated long-distance connectivity (<a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">Power et al. 2012</a>). In order to guard against artifactual effects due to head motion, researchers typically implement a variety of strategies that operate at multiple points of the data collection and processing pipeline, with guidance regularly evolving over time (<a href="https://doi.org/10.1016/j.neuroimage.2013.08.048">Power et al. 2014</a>; <a href="https://doi.org/10.1016/j.neuroimage.2014.10.044">2015</a>; <a href="https://doi.org/10.1016/j.neuroimage.2012.08.052">Satterthwaite et al. 2013</a>; <a href="https://doi.org/10.1093/cercor/bhw253">Siegel et al. 2017</a>; <a href="https://doi.org/10.1016/j.neuroimage.2020.116866">Gratton et al. 2020</a>). Some of these strategies include discarding entire runs of data that exceed certain motion thresholds and discarding individual functional imaging frames that are proximal to motion events (i.e., “motion censoring”). These strategies in particular typically lead to the exclusion of some participants from further analysis for lack of sufficient data.</p> <p>Levels of head motion differ according to demographic factors such as sex, race/ethnicity, and SES (<a href="https://doi.org/10.1007/s11682-022-00665-2">Cosgrove et al., 2022</a>). Therefore, strategies to deal with head motion may introduce questions of fairness and may lead to differential exclusions across demographic groups. In addition, motion censoring causes sessions to vary by the amount of data remaining. Such variability may continue to inflate findings especially in the presence of conditions that may correlate with the motion artifact like autism or ADHD (<a href="https://doi.org/10.1093/cercor/bhw403">Eggebrecht, 2017</a>). The amount of data remaining influences the variation in the connectivity calculations by affecting the degrees of freedom. Therefore, even after motion censoring, issues concerning fairness may persist when examining factors that might be affected by motion like sex, race/ethnicity, SES, and BMI (<a href="https://doi.org/10.1007/s11682-022-00665-2">Cosgrove et al., 2022</a>). One strategy that avoids this confound is to strictly control the degrees of freedom, where functional connectivity measures are calculated with the exact same amount of data. Researchers should assess whether control of artifactual effects of head motion effects can be achieved by alternative means that mitigate this impact. Examples of such strategies could include data augmentation approaches such as sampling from other datasets, data processing strategies like the include use of ICA-based denoising (<a href="https://doi.org/10.1016/j.neuroimage.2015.02.064">Pruim et al., 2015a</a>; <a href="https://doi.org/10.1016/j.neuroimage.2015.02.063">2015b</a>), use of bootstrap aggregation (<a href="https://doi.org/10.1101/2024.06.22.600221">Ramduny et al., 2024</a>), or the creation of “pseudo-rest” by removing task signals from the task data (<a href="https://doi.org/10.1016/j.neuroimage.2006.11.051">Fair et al. 2007</a>), or post-hoc approaches like propensity weighting.</p> 
<p>Researchers interested in examining brain-behavior associations or multivariate predictions should follow strategies such as those in <a href="https://doi.org/10.1093/cercor/bhw403">Eggebrecht 2017</a> to: 1) assess how missing data impacts dependent, independent variables and covariates, 2) examine the association between the degrees of freedom and non-FC variables, 3) use trimmed FC measures when needed to mitigate artifacts due to data quality.</p>
</div>

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</i></span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p><b>Philips signal intensity clipping - Overview</b><br>
A subset of Philips fMRI scans is affected by a signal intensity clipping issue. Due to a scaling error during real-time reconstruction, raw pixel intensity values above 4095 are capped, resulting in hyperintense regions that obscure gray/white matter signal. This artifact can significantly impact BOLD registration and derived measures such as ROI-to-ROI correlations.</p>
<p><b>Detection and Prevalence</b><br>
The artifact was initially detected during HBCD pilot scanning through manual quality control (QC) and addressed with a protocol patch applied at most Philips sites prior to the start of the HBCD main study. However, the patch was implemented later (October 2024) at sites VAN and CCH, leading to residual cases at these locations. Severe cases typically fail manual QC (QC=0), while less severe cases often pass (QC=1), as they may not be visually apparent. Overall, ~20% of scans from VAN and CCH show some degree of clipping, with ~6% classified as severe enough to fail QC. Updates to real-time reconstruction are in development to recover affected data. In the meantime, only scans that pass QC, including those with mild clipping, are included in the release.</p>
<p><b>How to Identify Affected Scans</b><br>
Clipping severity can be estimated using the ratio of median to maximum image intensity and the fraction of voxels at maximum intensity within the brain mask (both available in the <a href="../../../datacuration/file-based-data/#participant-session-scan-level-data"><code>scans.tsv</code> file</a>):</p> 
<ul>
<li><i>Severe clipping</i>: (brain_median / brain_max) > 0.8 AND brain_fvox_max > 0.001</li> 
<li><i>Potential clipping</i>: (brain_median / brain_max) > 0.5 AND brain_fvox_max > 0.001</li> 
</ul>
</div>

Functional MRI release data include both **file-based** (raw and processed data files in modality-specific formats) and **tabulated** (instrument and derived data in a standardized table format) data.      
<i>See the <a href="../../../datacuration/overview" target="_blank">Data Structure Overview</a> for a full explanation of these data types.</i>

 - <i class="fa fa-hammer"></i> <a href="../../../datacuration/file-based-data/#raw-bids" target="_blank">Raw BIDS</a> stored under subject- and session-specific <code>func/</code> and <code>fmap/</code> folders 
 - <i class="fas fa-cog"></i> <a href="../../../datacuration/file-based-data/#processed-derivatives" target="_blank">Processed derivatives</a> generated by various pipelines
 - <i class="fas fa-table"></i> <a href="../../../datacuration/phenotypes" target="_blank">Tabulated data</a> derived from pipeline outputs — see the full list of tables <a href="../../#mri" target="_blank">here</a>

<div id="rawbids" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dde6fe;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">Raw BIDS Files (<code>func/</code> & <code>fmap/</code>)</span>
  <a class="anchor-link" href="#rawbids" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>BOLD functional resting state data are located under <code>func/</code>. Each BOLD run has an associated pair of EPI fieldmaps acquired for distortion correction under <code>fmap/</code> in AP and PA (<code>dir-&lt;AP|PA&gt;</code>) phase encoding directions. <strong>Siemens, GE, and Philips additionally include B1 fieldmaps</strong> - see <a href="https://bids-specification.readthedocs.io/en/stable/appendices/qmri.html">qMRI BIDS specifications</a> for details. <i>See <a href="../../../datacuration/file-based-data/#bids-conversion-procedures">BIDS Conversion Procedures</a>.</i></p>
<pre class="folder-tree">
hbcd/
|__ rawdata/ 
    |__ sub-<span class="label">{ID}</span>/
        |__ ses-<span class="label">{V0X}</span>/ <span class="hashtag"># All files are accompanied by sidecar JSONs</span>
            |__ func/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_bold.nii.gz 
            |
            |__ fmap/
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_epi.nii.gz
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-<span class="placeholder">&lt;anat|fmap&gt;</span>_run-<span class="label">{X}</span>_TB1TFL.nii.gz <span class="hashtag"># B1 fmap (Siemens only)</span>
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-<span class="placeholder">&lt;tr1|tr2&gt;</span>_run-<span class="label">{X}</span>_TB1AFI.nii.gz   <span class="hashtag"># B1 fmap (GE & Philips only)</span>
</pre>
</div>

<div id="mriqc" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">MRIQC Derivatives (<code>mriqc/</code>)</span>
  <a class="anchor-link" href="#mriqc" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>MRIQC extracts image quality metrics (IQMs) from functional MRI data and also generates visual <code>.html</code> reports.<br><a href="https://mriqc.readthedocs.io/en/latest/about.html"><i class="fa-solid fa-book"></i> Go to pipeline documentation</a></p>
<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ mriqc/
        |__ sub-<span class="label">{ID}</span>/
        |   |__ ses-<span class="label">{V0X}</span>/
        |       |__ func/
        |           |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_bold.json
        |        
        |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_bold.html
</pre>
</div>

<div id="nibabies" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
  <span class="text">Infant fMRIPrep Derivatives (<code>nibabies/</code>)</span>
  <a class="anchor-link" href="#nibabies" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Infant-fMRIPrep (also known as NiBabies) outputs from minimal structural and functional MRI processing include visual quality assessment reports, preprocessed derivatives, and confounds to be used for denoising in subsequent processing procedures.<br><a href="https://nibabies.readthedocs.io/en/latest/outputs.html"><i class="fa-solid fa-book"></i> Go to pipeline documentation</a></p>
<pre class="folder-tree" style="font-size: 11px;">
hbcd/
|_ derivatives/ 
   |_ nibabies/
      |_ sub-<span class="label">{ID}</span>/
      |  |_ figures/
      |  |_ ses-<span class="label">{V0X}</span>/
      |     |_ log/
      |     |
      |     |_ anat/
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_desc-preproc_T2w.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_from-<span class="placeholder">&lt;MNI152NLin6Asym_res-2|MNIInfant+1&gt;</span>_to-T2w_mode-image_xfm.h5
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_from-T2w_to-<span class="placeholder">&lt;MNI152NLin6Asym_res-2|MNIInfant+1&gt;</span>_mode-image_xfm.h5
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_from-T2w_to-fsnative_mode-image_xfm.txt
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_from-fsnative_to-T2w_mode-image_xfm.txt
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_<span class="placeholder">&lt;curv|sulc|thickness&gt;</span>.shape.gii
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_<span class="placeholder">&lt;inflated|midthickness|pial|sphere|white&gt;</span>.surf.gii
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-dhcpAsym_den-32k_midthickness.surf.gii
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-dhcpAsym_den-32k_pial.surf.gii
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-dhcpAsym_den-32k_white.surf.gii
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-<span class="placeholder">&lt;dhcpAsym|fsaverage&gt;</span>_den-32k_sphere.surf.gii
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_desc-brain_mask.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_desc-preproc_T2w.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_dseg.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-<span class="placeholder">&lt;MNI152NLin6Asym_res-2|T2w&gt;</span>_label-<span class="placeholder">&lt;CSF|GM|WM&gt;</span>_probseg.nii.gz
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-T2w_desc-<span class="placeholder">&lt;aparcaseg|aseg&gt;</span>_dseg.nii.gz
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-T2w_dseg.nii.gz
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-T2w_desc-ribbon_mask.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_den-91k_<span class="placeholder">&lt;curv|sulc|thickness&gt;</span>.dscalar.nii <span class="hashtag">(+JSON)</span>
      |     |
      |     |_ fmap/
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_fmapid-auto00000<span class="label">{X}</span>_desc-coeff_fieldmap.nii.gz
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_fmapid-auto00000<span class="label">{X}</span>_desc-epi_fieldmap.nii.gz
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_fmapid-auto00000<span class="label">{X}</span>_desc-preproc_fieldmap.nii.gz <span class="hashtag">(+JSON)</span>
      |     |
      |     |_ func/ <span class="hashtag">(ALL +JSON)</span>
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_desc-brain_mask.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_desc-confounds_timeseries.tsv
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_desc-coreg_boldref.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_desc-hmc_boldref.nii.gz 
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_desc-preproc_bold.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_from-boldref_to-T2w_mode-image_desc-coreg_xfm.txt
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_from-boldref_to-auto00000_mode-image_xfm.txt
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_from-orig_to-boldref_mode-image_desc-hmc_xfm.txt
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsnative_bold.func.gii
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_boldref.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_desc-brain_mask.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_desc-preproc_bold.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-T2w_boldref.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-T2w_desc-brain_mask.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-T2w_desc-preproc_bold.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_bold.dtseries.nii
      |    
      |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.html
</pre>
</div>

<div id="fs-mcribs" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">M-CRIB-S (<code>mcribs/</code>) & FreeSurfer (<code>freesurfer/</code>) Source Directories</span>
  <a class="anchor-link" href="#fs-mcribs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>The <code>mcribs/</code> and <code>freesurfer/</code> derivatives folders are sourced from intermediate FreeSurfer-like folders generated by Infant-fMRIPrep during surface reconstruction - <a href="https://nibabies.readthedocs.io/en/latest/outputs.html#surface-reconstruction">see details</a>. Infant fMRIPrep supports three surface reconstruction methods, each optimized for a specific age range (see <a href="https://doi.org/10.1101/2025.05.14.654069">Goncalves et al., 2025</a> for details):</p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th>Surface Reconstruction Method</th>
      <th>Optimal Age Range</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>M-CRIB-S</td>
    <td>≤ 5 months</td>
    <td style="word-wrap: break-word; white-space: normal;">Neonate method based on the Melbourne Children’s Regional Infant Brain atlases (<a href="https://doi.org/10.1038/s41598-020-61326-2">Adamson et al. 2020</a>)</td>
<tr>
<tr>
    <td>Infant FreeSurfer</td>
    <td>≥ 3 months</td>
    <td style="word-wrap: break-word; white-space: normal;">Modified version of FreeSurfer optimized for infants 0–2 years (<a href="https://doi.org/10.1016/j.neuroimage.2020.116946">Zöllei et al. 2020</a>)</td>
<tr>
<tr>
    <td>FreeSurfer</td>
    <td>≥ 10 months</td>
    <td style="word-wrap: break-word; white-space: normal;">Standard FreeSurfer, developed from adult data (<a href="https://doi.org/10.1006/nimg.1998.0395">Dale et al. 1998</a>)</td>
<tr>
</tbody>
</table>
<p>The current HBCD release includes Infant-fMRIPrep derivatives for <strong>visit V02 (0–1 months) using M-CRIB-S for surface reconstruction</strong>. When M-CRIB-S is used, the <code>freesurfer/</code> folder is generated by mapping outputs from <code>mcribs/</code> to follow the structure of FreeSurfer’s <a href="https://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllOutputFiles">recon-all</a> for compatibility. As a result, files in <code>freesurfer/</code> are identical to the corresponding source files in <code>mcribs/</code>, the only differences being:<br>
 • M-CRIB-S FS: contains 2 symlink in place of regular files<br>
 • Derivatives FS: includes 3 additional files, <code>scripts/mcribs.log</code> and <code>surf/<span class="placeholder">&lt;l|r&gt;</span>h.midthickness</code></p>
<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ <span class="subses">freesurfer/</span>
    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>/
    |       |__ label/
    |       |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc+DKTatlas.annot
    |       |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc+DKTatlas.auto.nomask.annot
    |       |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc.annot
    |       |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc.auto.nomask.annot
    |       |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.cortex.label
    |       |
    |       |__ mri/
    |       |   |__ T2.mgz
    |       |   |__ aparc+<span class="placeholder">&lt;DKTatlas&gt;</span>+aseg.mgz
    |       |   |__ aseg.mgz
    |       |   |__ aseg.<span class="placeholder">&lt;internal|presurf|presurf.preunwmfix&gt;</span>.mgz
    |       |   |__ brain.mgz
    |       |   |__ brainmask.mgz
    |       |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.ribbon.mgz
    |       |   |__ norm.mgz
    |       |   |__ orig.mgz
    |       |   |__ ribbon.mgz
    |       |
    |       |__ scripts/
    |       |   |__ mcribs.log
    |       |
    |       |__ stats/
    |       |   |__aseg.stats
    |       |   |__brainvol.stats
    |       |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc+DKTatlas.stats
    |       |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc.stats
    |       |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.curv.stats
    |       |
    |       |__ surf/
    |           |__ <span class="placeholder">&lt;lh|rh&gt;</span>.<span class="placeholder">&lt;area|area.mid|area.pial&gt;</span>
    |           |__ <span class="placeholder">&lt;lh|rh&gt;</span>.curv
    |           |__ <span class="placeholder">&lt;lh|rh&gt;</span>.inflated
    |           |__ <span class="placeholder">&lt;lh|rh&gt;</span>.inflated.<span class="placeholder">&lt;H|K&gt;</span>
    |           |__ <span class="placeholder">&lt;lh|rh&gt;</span>.midthickness
    |           |__ <span class="placeholder">&lt;lh|rh&gt;</span>.orig
    |           |__ <span class="placeholder">&lt;lh|rh&gt;</span>.pial
    |           |__ <span class="placeholder">&lt;lh|rh&gt;</span>.smoothwm
    |           |__ <span class="placeholder">&lt;lh|rh&gt;</span>.smoothwm.<span class="placeholder">&lt;BE|C|FI|H|K|K1|K2|S&gt;</span>.crv
    |           |__ <span class="placeholder">&lt;lh|rh&gt;</span>.smoothwm.<span class="placeholder">&lt;H|K&gt;</span>
    |           |__ <span class="placeholder">&lt;lh|rh&gt;</span>.sphere
    |           |__ <span class="placeholder">&lt;lh|rh&gt;</span>.sphere.<span class="placeholder">&lt;reg|reg2&gt;</span>
    |           |__ <span class="placeholder">&lt;lh|rh&gt;</span>.<span class="placeholder">&lt;sulc|thickness|volume|white&gt;</span>
    |
    |__ <span class="subses">mcribs/</span>
        |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>/
            |__ RawT2/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.nii.gz
            |
            |__ RawT2RadiologicalIsotropic/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.nii.gz_symlink_s3_object
            |
            |__ SurfReconDeformable/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>/
            |       |__ meshes/
            |       |   |__ <span class="placeholder">&lt;internal|pial+internal|pial|white+internal|white&gt;</span>.vtp
            |       |   |__ pial-<span class="placeholder">&lt;lh|rh&gt;</span>-reordered.vtp
            |       |   |__ pial-<span class="placeholder">&lt;lh|rh&gt;</span>.vtp
            |       |   |__ white-<span class="placeholder">&lt;lh|rh&gt;</span>.CortexMask.curv
            |       |   |__ white-<span class="placeholder">&lt;lh|rh&gt;</span>.Normals.surf
            |       |   |__ white-<span class="placeholder">&lt;lh|rh&gt;</span>.RegionId.curv
            |       |   |__ white-<span class="placeholder">&lt;lh|rh&gt;</span>.vtp
            |       |
            |       |__ recon/
            |       |   |__ cortical-hull-dmap.nii.gz
            |       |   |__ regions.nii.gz 
            |       |
            |       |__ temp/
            |           |__ <span class="placeholder">&lt;brain|cortex&gt;</span>-mask.nii.gz
            |           |__ cerebrum-<span class="placeholder">&lt;1|2|3&gt;</span>.vtp
            |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-<span class="placeholder">&lt;1|2|3&gt;</span>.vtp
            |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-2-output_<span class="placeholder">#</span>.vtp
            |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-dmap.nii.gz
            |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-hull-<span class="placeholder">#</span>.vtp
            |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-iso.vtp
            |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-mask.nii.gz
            |           |__ corpus-callosum-mask-<span class="placeholder">&lt;1|2|3&gt;</span>.nii.gz
            |           |__ deep-gray-matter-mask-<span class="placeholder">&lt;1|2&gt;</span>.nii.gz
            |           |__ gray-matter-mask-<span class="placeholder">&lt;1|2&gt;</span>.nii.gz
            |           |__ pial-<span class="placeholder">&lt;#|#-output_#&gt;</span>.vtp
            |           |__ pial-foreground.nii.gz
            |           |__ t2w-image.nii.gz_symlink_s3_object
            |           |__ ventricles-dmap.nii.gz
            |           |__ ventricles-mask-<span class="placeholder">&lt;1|2&gt;</span>.nii.gz
            |           |__ white-<span class="placeholder">&lt;#|#-output_#&gt;</span>.vtp
            |           |__ white-foreground.nii.gz
            |           |__ white-matter-mask-<span class="placeholder">&lt;1|2&gt;</span>.nii.gz
            |
            |__ TissueSeg/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_all_labels.nii.gz
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_all_labels_manedit.nii.gz_symlink_s3_object
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_brain_mask.nii.gz
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_t2w_restore.nii.gz_symlink_s3_object
            |
            |__ TissueSegDrawEM/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>/
            |       |__ N4/
            |           |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.nii.gz_symlink_s3_object
            |
            |__ freesurfer/ <span class="hashtag"># Only files unique to M-CRIB-S FreeSurfer subfolder displayed</span>
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>/
            |       |__ label/
            |       |__ mri/
            |       |   |__ brain.mgz_symlink_s3_object
            |       |   |__ orig.mgz_symlink_s3_object
            |       |__ stats/
            |       |__ surf/
            |
            |__ logs/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.log
            |
            |__ command.txt
</pre>
<div id="symlinks" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dde6fe7e;">
  <span class="emoji"><i class="fas fa-rotate-left"></i></span>
  <span class="text-with-link">
  <span class="text">Restoring Symlink Files</span>
  <a class="anchor-link" href="#symlinks" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>The M-CRIB-S folders contain four symlink files, which serve as references to data stored elsewhere. When these files are uploaded to the release bucket, they are renamed with the suffix <code>*_symlink_s3_object</code> to distinguish them from regular files. When downloaded, these symlink files appear as text files because they contain the S3 object path instead of the actual file content. To restore them as symlinks, run one of the following commands in the terminal:</p>
<p>Option 1: This command simply prints what commands to run to restore individual symlinks and does not change anything:</p>
<div class="copy-box">
  <div class="copy-text-container">
    <span id="specific-text-code">find . -type f -name "*_symlink_s3_object" -print | while read path ; do
  symval=$(cat "$path")
  symdir=$(dirname "$path")
  symbase=$(basename "$path" _symlink_s3_object)
  echo ln -s "$symval" "$symdir/$symbase" '&&' rm -f "$path"
done
    </span>
    <button class="copy-button">Copy</button>
  </div>
</div>
<p>Option 2: This restores all symlink files within the directory and renames them without <code>*_symlink_s3_object</code> to match the original sourcedata filenames:</p>
<div class="copy-box">
  <div class="copy-text-container">
    <span id="specific-text-code">find . -type f -name "*_symlink_s3_object" -print | while read path ; do
  symval=$(cat "$path")
  symdir=$(dirname "$path")
  symbase=$(basename "$path" _symlink_s3_object)
  ln -s "$symval" "$symdir/$symbase" && rm -f "$path" || break
done</span>
    <button class="copy-button">Copy</button>
  </div>
</div>
</div>
</div>

<div id="xcpd" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #fbe6f7">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">XCP-D Derivatives (<code>xcp_d/</code>)</span>
  <a class="anchor-link" href="#xcpd" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>XCP-D performs functional MRI post-processing and noise regression from Infant-fMRIPrep derivatives.<br><a href="https://xcp-d.readthedocs.io/en/latest/"><i class="fa-solid fa-book"></i> Go to pipeline documentation</a></p>
<pre style="font-size: 10px;" class="folder-tree">
hbcd/
|_ derivatives/ 
   |_ xcp_d/
      |_ sub-<span class="label">{ID}</span>/
         |_ ses-<span class="label">{V0X}</span>/
         |  |_ anat/
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_desc-preproc_T2w.nii.gz
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-curv_morph.tsv
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-sulc_morph.tsv
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-thickness_morph.tsv
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span class="placeholder">&lt;inflated|vinflated&gt;</span>.surf.gii
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span class="placeholder">&lt;midthickness|pial|white&gt;</span>.surf.gii
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_den-91k_<span class="placeholder">&lt;curv|sulc|thickness&gt;</span>.dscalar.nii
         |  |
         |  |_ func/ <span class="hashtag"># All func files have JSONs with exception of .hdf5 & *linc_qc.tsv</span>
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_desc-abcc_qc.hdf5 <span class="hashtag">(No JSON)</span>
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_<span class="placeholder">&lt;motion|outliers&gt;</span>.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_space-fsLR_den-91k_desc-denoised_bold.dtseries.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_den-91k_stat-mean_timeseries.ptseries.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-mean_timeseries.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-pearsoncorrelation_relmat.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_desc-abcc_qc.hdf5 <span class="hashtag">(No JSON)</span>
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_desc-linc_qc.tsv <span class="hashtag">(No JSON)</span>
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_<span class="placeholder">&lt;design|motion|outliers&gt;</span>.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_desc-denoised_bold.dtseries.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_stat-alff_boldmap.dscalar.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_stat-alff_desc-smooth_boldmap.dscalar.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_stat-reho_boldmap.dscalar.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_den-91k_stat-coverage_boldmap.pscalar.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_den-91k_stat-mean_timeseries.ptseries.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_den-91k_stat-pearsoncorrelation_boldmap.pconn.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-alff_bold.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-coverage_bold.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-mean_timeseries.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-pearsoncorrelation_relmat.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-reho_bold.tsv
         |  
         |_ figures/
         |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_executive_summary.html
         |_ sub-<span class="label">{ID}</span>.html

<span class="hashtag"># Label Values Legend</span>
<span class="placeholder">&lt;APARC&gt; (anat/ parcellations)</span>: 4S-&lt;1|2|3|4|5|6|7|8|9|10&gt;56Parcels, Glasser, Gordon, MIDB, MyersLabonte
<span class="placeholder">&lt;PARC&gt; (func/ parcellations)</span>: 4S-&lt;1|2|3|4|5|6|7|8|9|10&gt;56Parcels, Glasser, Gordon, MIDB, MyersLabonte, HCP, Tian
</pre>
</div>

## Data Acquisition

<div style="display: flex; align-items: center; gap: 20px;">
  <!-- Text on the left -->
  <div style="flex: 1;">
    <p>
      Whole-brain functional activity is measured by functional magnetic resonance imaging (fMRI). 
      The blood oxygen level dependent (BOLD) signal is measured at each voxel in 2mm isotropic space 
      with a repetition time (TR) of 1725 ms and multi-band (MB) factor of 4. 
    </p>
    <p>
      A minimum of two resting state (rs) fMRI runs are acquired during sleep (for infants &lt;30 months old) lasting 
      7.5 minutes each (<b>Figure 1A</b>). <a href="https://firmm.readthedocs.io/">FIRMM software</a> 
      (Dosenbach et al. 2017) is used to monitor motion, as quantified by framewise displacement (FD), 
      in real time, and additional runs are acquired as needed to obtain a minimum total of 7.5 minutes of 
      low-motion (FD &lt;0.3 mm) data across runs (<b>Figure 1B</b>).
    </p>
    <p>
      Each rsfMRI run is additionally preceded by acquisition of single shot spin-echo (SE) EPI images with same 
      and reversed polarity phase encoding gradients with which to perform distortion correction (<b>Figure 1C</b>). 
      Additional details are available at <a href="https://doi.org/10.1016/j.dcn.2024.101452">Dean et al. 2024</a>.
    </p>
  </div>

  <!-- Image on the right -->
  <div style="flex: 1; text-align: center;">
    <img src="../images/Deanetal2024_fMRI.jpg" style="max-width:100%; height:auto;">
    <p style="font-size: 0.9em; margin-top: 5px;">
      <b>Figure 1.</b> HBCD fMRI Acquisition Protocol 
      (<i><a href="https://doi.org/10.1016/j.dcn.2024.101452">Dean et al., 2024</a></i>)
    </p>
  </div>
</div>

## Data Processing

Functional MRI data is processed through [infant-fMRIPrep](https://nibabies.readthedocs.io/en/latest/) and subsequently [XCP-D](https://xcp-d.readthedocs.io/en/latest/usage.html) as described in detail on the [HBCD Processing webpage](https://hbcd-cbrain-processing.readthedocs.io/latest/tool_details.html#tool-names). In brief, infant-fMRIPrep produces minimally pre-processed outputs including confound files (with motion parameters, average signals for ROIs like CSF, etc.) and motion-corrected data in age-specific MNI volumetric atlas as well as fs_LR32k surface space. From these outputs, the XCP-D pipeline runs nuisance regression/denoising, parcellates the fMRI data, and computes summary measures.

Volumetric and surface-based time series will be made available for each subject. The data release also includes dense and parcellated time series with at least 2.5 minutes of low-motion data (FD>0.3), functional connectivity matrices, regional homogeneity values, and amplitude of low-frequency fluctuation values. All parcellated derivatives are generated from a variety of parcellation schemes. See the folder trees above for a full list of [XCP-D](#xcpd) and [Infant fMRIPrep](#nibabies) included in the release.

## References
<div class="references">
   <p>Cosgrove KT, McDermott TJ, White EJ, Mosconi MW, Thompson WK, Paulus MP, Cardenas-Iniguez C, Aupperle RL. Limits to the generalizability of resting-state functional magnetic resonance imaging studies of youth: An examination of ABCD Study® baseline data. <i>Brain Imaging Behav</i> 16, 1919-1925, 2022. <a href="https://doi.org/10.1007/s11682-022-00665-2" target="_blank">doi: 10.1007/s11682-022-00665-2</a></p>
  <p>Dean III, D. C., Tisdall, M. D., Wisnowski, J. L., Feczko, E., Gagoski, B., Alexander, A. L., ... &amp; HBCD MRI Working Group. (2024). Quantifying brain development in the HEALthy Brain and Child Development (HBCD) Study: The magnetic resonance imaging and spectroscopy protocol. <em>Developmental Cognitive Neuroscience</em>, 70, 101452. <a href="https://doi.org/10.1016/j.dcn.2024.101452">10.1016/j.dcn.2024.101452</a></p>
  <p>Dosenbach, N. U. F., Koller, J. M., Earl, E. A., Miranda-Dominguez, O., Klein, R. L., Van, A. N., Snyder, A. Z., Nagel, B. J., Nigg, J. T., Nguyen, A. L., Wesevich, V., Greene, D. J., & Fair, D. A. (2017). Real-time motion analytics during brain MRI improve data quality and reduce costs. <em>NeuroImage</em>, 161, 80-93. <a href="https://doi.org/10.1016/j.neuroimage.2017.08.025">https://doi.org/10.1016/j.neuroimage.2017.08.025</a></p>
  <p>Eggebrecht, A. T., Elison, J. T., Feczko, E., Todorov, A., Wolff, J. J., Kandala, S., Adams, C. M., Snyder, A. Z., Lewis, J. D., Estes, A. M., Zwaigenbaum, L., Botteron, K. N., McKinstry, R. C., Constantino, J. N., Evans, A., Hazlett, H. C., Dager, S., Paterson, S. J., Schultz, R. T., … Pruett, J. R., Jr. (2017). Joint attention and brain functional connectivity in infants and toddlers. <i>Cerebral Cortex (New York, N.Y.: 1991)</i>, 27(3), 1709–1720. <a href="https://doi.org/10.1093/cercor/bhw403" target="_blank">doi: 10.1093/cercor/bhw403</a></p>
  <p>Fair, D. A., Schlaggar, B. L., Cohen, A. L., Miezin, F. M., Dosenbach, N. U. F., Wenger, K. K., Fox, M. D., Snyder, A. Z., Raichle, M. E., & Petersen, S. E. (2007). A method for using blocked and event-related fMRI data to study “resting state” functional connectivity. <i>NeuroImage</i>, 35(1), 396–405. <a href="https://doi.org/10.1016/j.neuroimage.2006.11.051" target="_blank">doi: 10.1016/j.neuroimage.2006.11.051</a></p>
  <p>Gratton, C., Dworetsky, A., Coalson, R. S., Adeyemo, B., Laumann, T. O., Wig, G. S., Kong, T. S., Gratton, G., Fabiani, M., Barch, D. M., Tranel, D., Miranda-Dominguez, O., Fair, D. A., Dosenbach, N. U. F., Snyder, A. Z., Perlmutter, J. S., Petersen, S. E., & Campbell, M. C. (2020). Removal of high frequency contamination from motion estimates in single-band fMRI saves data without biasing functional connectivity. <i>NeuroImage</i>, 217(116866), 116866. <a href="https://doi.org/10.1016/j.neuroimage.2020.116866" target="_blank">doi: 10.1016/j.neuroimage.2020.116866</a></p>
  <p>Power, J. D., Barnes, K. A., Snyder, A. Z., Schlaggar, B. L., & Petersen, S. E. (2012). Spurious but systematic correlations in functional connectivity MRI networks arise from subject motion. <i>NeuroImage</i>, 59(3), 2142–2154. <a href="https://doi.org/10.1016/j.neuroimage.2011.10.018" target="_blank">doi: 10.1016/j.neuroimage.2011.10.018</a></p>
  <p>Power, J. D., Mitra, A., Laumann, T. O., Snyder, A. Z., Schlaggar, B. L., & Petersen, S. E. (2014). Methods to detect, characterize, and remove motion artifact in resting state fMRI. <i>NeuroImage</i>, 84, 320–341. <a href="https://doi.org/10.1016/j.neuroimage.2013.08.048" target="_blank">doi: 10.1016/j.neuroimage.2013.08.048</a></p>
  <p>Power, J. D., Schlaggar, B. L., & Petersen, S. E. (2015). Recent progress and outstanding issues in motion correction in resting state fMRI. <i>NeuroImage</i>, 105, 536–551. <a href="https://doi.org/10.1016/j.neuroimage.2014.10.044" target="_blank">doi: 10.1016/j.neuroimage.2014.10.044</a></p>
  <p>Pruim RHR, Mennes M, van Rooij D, Llera A, Buitelaar JK, Beckmann CF. ICA-AROMA: A robust ICA-based strategy for removing motion artifacts from fMRI data. <i>Neuroimage</i> 112, 267-277, 2015a. <a href="https://doi.org/10.1016/j.neuroimage.2015.02.064" target="_blank">doi: 10.1016/j.neuroimage.2015.02.064</a></p>
  <p>Pruim RHR, Mennes M, Buitelaar JK, Beckmann CF. Evaluation of ICA-AROMA and alternative strategies for motion artifact removal in resting state fMRI. <i>Neuroimage</i> 112, 278-287, 2015b. <a href="https://doi.org/10.1016/j.neuroimage.2015.02.063" target="_blank">doi: 10.1016/j.neuroimage.2015.02.063</a></p>
  <p>Ramduny, J., Uddin, L. Q., Vanderwal, T., Feczko, E., Fair, D. A., Kelly, C., & Baskin-Sommers, A. (2024). Increasing the representation of minoritized youth for inclusive and reproducible brain-behavior associations. <i>bioRxiv</i>. <a href="https://doi.org/10.1101/2024.06.22.600221" target="_blank">doi: 10.1101/2024.06.22.600221</a></p>
  <p>Satterthwaite TD, Elliott MA, Gerraty RT, Ruparel K, Loughead J, Calkins ME, Eickhoff SB, Hakonarson H, Gur RC, Gur RE, Wolf DH. An improved framework for confound regression and filtering for control of motion artifact in the preprocessing of resting-state functional connectivity data. <i>Neuroimage</i> 64, 240-256, 2013. <a href="https://doi.org/10.1016/j.neuroimage.2012.08.052" target="_blank">doi: 10.1016/j.neuroimage.2012.08.052</a></p>
  <p>Siegel JS, Mitra A, Laumann TO, Seitzman BA, Raichle M, Corbetta M, Snyder AZ. Data Quality Influences Observed Links Between Functional Connectivity and Behavior. <i>Cereb Cortex</i> 27, 4492-4502, 2017. <a href="https://doi.org/10.1093/cercor/bhw253" target="_blank">doi: 10.1093/cercor/bhw253</a></p>
</div>
<br>