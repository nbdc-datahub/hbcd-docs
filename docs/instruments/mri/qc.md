# HBCD MR Quality Control Procedures

## Raw MR Data QC
<div id="scanstsv" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fa-solid fa-location-dot"></i></span>
  <span class="text-with-link">
  <span class="text">Location of Raw MR QC metrics in Release Data: <a href="../../../datacuration/file-based-data/#participant-session-scan-level-data" target="_blank">Scans TSV Files (<code>*_scans.tsv</code>)</a></span>
  <a class="anchor-link" href="#scanstsv" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>The session folder <code>sub-{ID}_ses-{V0X}_scans.tsv</code> files include the following QC metrics. <i>Note: <b>x</b> values for b<b>x</b> below include 0, 500, 1000, 2000, and 3000</i></p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
  <thead>
    <tr>
    <th>Field</th>
    <th>Description</th>
    </tr>
    </thead>
     <tr>
        <td>filename</td>
        <td>Relative paths to files</td>
    </tr>
    <tr>
        <td>acq_time</td>
        <td>Acquisition time</td>
    </tr>
    <tr>
        <td>loris_qc_status</td>
        <td>Pass/Fail mapping from UCSD QC JSON file</td>
    </tr>
    <tr>
        <td>loris_selected</td>
        <td>Whether file is selected for further processing</td>
    </tr>
    <tr>
        <td>site</td>
        <td>Site where the session data was collected</td>
    </tr>
    <tr>
        <td>age</td>
        <td>Age (in years) of participant at time of the scan</td>
    </tr>
    <tr>
        <td>age_adjusted</td>
        <td>Adjusted age (in days) based on the EDD</td>
    </tr>
    <tr>
        <td>head_size</td>
        <td>Head size at the time of the scan</td>
    </tr>
    <tr>
    <td>nrev</td><td><span class="tooltip tooltip-right"><i class="fa-solid fa-eye"></i><span class="tooltiptext">Manual QC Metric</span></span> Number of manual QC reviewers</td>
    </tr>
    <tr><td>revdisp</td><td><span class="tooltip tooltip-right"><i class="fa-solid fa-eye"></i><span class="tooltiptext">Manual QC Metric</span></span> If there was disparity/disagreement between reviewers</td>
    </tr>
    <tr>
        <td>QC</td><td><span class="tooltip tooltip-right"><i class="fa-solid fa-eye"></i><span class="tooltiptext">Manual QC Metric</span></span> Overall manual QC score: 1 (pass), 0 (fail)<br>
        <strong>Note: scans with only automated, and not manual, QC performed have a QC field value of 1</strong></td>
    </tr>
    <tr>
        <td>notes</td><td><span class="tooltip tooltip-right"><i class="fa-solid fa-eye"></i><span class="tooltiptext">Manual QC Metric</span></span> Optional notes from manual QC review</td>
    </tr>
    <tr>
        <td>QU_motion</td>
        <td><span class="tooltip tooltip-right"><i class="fa-solid fa-eye"></i><span class="tooltiptext">Manual QC Metric</span></span> Qualitative manual QC score for motion (<i>sMRI & qMRI</i>)</td>
    </tr>
    <tr>
        <td>QU_sus</td>
        <td><span class="tooltip tooltip-right"><i class="fa-solid fa-eye"></i><span class="tooltiptext">Manual QC Metric</span></span> Qualitative manual QC score for susceptibility artifact (<i>dMRI, fMRI, & field maps</i>)</td>
    </tr>
    <tr>
        <td>QU_cutoff</td>
        <td><span class="tooltip tooltip-right"><i class="fa-solid fa-eye"></i><span class="tooltiptext">Manual QC Metric</span></span> Qualitative manual QC score for FOV cutoff artifact (<i>dMRI, fMRI, & field maps</i>)</td>
    </tr>
    <tr>
        <td>QU_line</td>
        <td><span class="tooltip tooltip-right"><i class="fa-solid fa-eye"></i><span class="tooltiptext">Manual QC Metric</span></span> Qualitative manual QC score for line artifact (<i>dMRI, fMRI, & field maps</i>)</td>
    </tr>
    <tr>
        <td>line_nframes</td>
        <td>Number of frames with line artifacts</td>
    </tr>
    <tr>
        <td>line_&ltmax|mean&gt_score</td>
        <td>Maximum/Mean line artifact score across frames</td>
    </tr>
    <tr>
        <td>line_&ltmax|mean&gt_count</td>
        <td>Maximum/Mean line artifact count across frames</td>
    </tr>
    <tr>
        <td>cutoff</td>
        <td>Sum of dorsal and ventral cutoff scores</td>
    </tr>
    <tr>
        <td>&ltdorsal|ventral&gt_cutoff</td>
        <td>Dorsal/Ventral cutoff score</td>
    </tr>
    <tr>
        <td>brain_&ltmean|std&gt</td>
        <td>Mean/Standard deviation of image intensity within brain mask</td>
    </tr>
    <tr>
        <td>brain_SNR</td>
        <td>Signal-to-noise ratio (mean/stdev) of image intensity within brain mask</td>
    </tr>
    <tr>
        <td>brain_&ltmin|max|median&gt</td>
        <td>Minimum/Maximum/Median image intensity within brain mask</td>
    </tr>
    <tr>
        <td>brain_tSNR_&ltmean|median|std&gt</td>
        <td>Mean/Median/Standard deviation of temporal SNR in brain mask</td>
    </tr>
    <tr>
        <td>mean_&ltmotion|trans|rot&gt</td>
        <td>Average framewise displacement/translation/rotation (mm)</td>
    </tr>
    <tr>
        <td>max_d&ltx|y|z&gt</td>
        <td>Maximum absolute x/y/z translation (mm)</td>
    </tr>
    <tr>
        <td>max_r&ltx|y|z&gt</td>
        <td>Maximum absolute x/y/z rotation (mm)</td>
    </tr>
    <tr>
        <td>subthresh_&lt02|03|04&gt</td>
        <td>Number of seconds with framewise displacement less than 0.2/0.3/0.4 mm</td>
    </tr>
    <tr>
        <td>aqc_motion</td>
        <td>Automated QC motion score for sMRI</td>
    </tr>
    <tr>
        <td>nreps</td>
        <td>Number of repetitions / frames</td>
    </tr>
    <tr>
        <td>brainvol</td>
        <td>Volume of brain mask (mm^3)</td>
    </tr>
    <tr>
        <td>fwhm_x</td>
        <td>Full width half max spatial smoothness in x-axis (left-right)</td>
    </tr>
    <tr>
        <td>b0_&ltmedian|std&gt</td>
        <td>Median/Standard Deviation b=0 intensity in brain mask</td>
    </tr>
    <tr>
        <td>DTerr_&ltmean|median|std&gt</td>
        <td>Mean/Median/STD across frames of RMS residual error relative to RMS signal in brain voxels</td>
    </tr>
    <tr>
        <td>Completed</td>
        <td>Whether series has the expected number of files</td>
    </tr>
    <tr>
        <td>NumberOfFiles</td>
        <td>Number of DICOM files</td>
    </tr>
    <tr>
        <td>HBCD_compliant</td>
        <td>Whether series passes minimal protocol compliance check</td>
    </tr>
    <tr>
        <td>AdditionalInfo</td>
        <td>Notes on classification and protocol compliance</td>
    </tr>
    <tr>
        <td>MD_std</td>
        <td>Standard deviation of mean diffusivity in brain mask</td>
    </tr>
    <tr>
        <td>b0_mean</td>
        <td>Average b=0 intensity in brain mask</td>
    </tr>
    <tr>
        <td>FA_std</td>
        <td>Standard deviation of fractional anisotropy in brain mask</td>
    </tr>
    <tr>
        <td>MD_&ltmean|median&gt</td>
        <td>Mean/Median MD (mean diffusivity) in brain mask</td>
    </tr>
    <tr>
        <td>max_nbad_frames_per_slice</td>
        <td>Maximum number of outlier frames per slice</td>
    </tr>
    <tr>
        <td>max_nbad_frames_per_frame</td>
        <td>Maximum number of outlier frames per slice/frame</td>
    </tr>
    <tr>
        <td>FA_&ltmean|median&gt</td>
        <td>Mean/Median fractional anisotropy in brain mask</td>
    </tr>
    <tr>
        <td>fwhm_z</td>
        <td>Full width half max spatial smoothness in z-axis (inferior-superior)</td>
    </tr>
    <tr>
        <td>nbad_frame_slices</td>
        <td>Number of outlier frame-slices (dMRI)</td>
    </tr>
    <tr>
        <td>nbad_frames</td>
        <td>Number of frames with outlier slices (dMRI)</td>
    </tr>
    <tr>
        <td>nbad_slices</td>
        <td>Number of slices with outlier frames (dMRI)</td>
    </tr>
    <tr>
        <td>fwhm_y</td>
        <td>Full width half max spatial smoothness in y-axis (anterior-posterior)</td>
    </tr>
    <tr>
        <td>qc_status</td>
        <td>Whether review is pending, complete, or has other status</td>
    </tr>
    <tr>
        <td>ngood_frames</td>
        <td>Number of frames without outlier slices (dMRI)</td>
    </tr>
    <tr>
        <td>censor_thresh</td>
        <td>Threshold used for censoring outlier slices (dMRI)</td>
    </tr>
    <tr>
        <td>nframes_b<b>x</b></td>
        <td>Number of b=<b>x</b> frames</td>
    </tr>
    <tr>
        <td>nbad_frame_slices_b<b>x</b></td>
        <td>Number of outlier frame-slices for dMRI b=<b>x</b> frames</td>
    </tr>
    <tr>
        <td>nbad_frames_b<b>x</b></td>
        <td>Number of frames with outlier slices for dMRI b=<b>x</b> frames</td>
    </tr>
    <tr>
        <td>nbad_slices_b<b>x</b></td>
        <td>Number of slices with outlier frames for dMRI b=<b>x</b> frames</td>
    </tr>
    <tr>
        <td>ngood_frames_b<b>x</b></td>
        <td>Number of frames without outlier slices for dMRI b=<b>x</b> frames</td>
    </tr>
    <tr>
        <td>FWHMx_b<b>x</b></td>
        <td>FWHM spatial smoothness in x-axis (left-right) for b=<b>x</b> frames</td>
    </tr>
    <tr>
        <td>FWHMy_b<b>x</b></td>
        <td>FWHM spatial smoothness in y-axis (anterior-posterior) for b=<b>x</b> frames</td>
    </tr>
    <tr>
        <td>FWHMz_b<b>x</b></td>
        <td>FWHM spatial smoothness in z-axis (inferior-superior) for b=<b>x</b> frames</td>
    </tr>
    <tr>
        <td>tSNR_b<b>x</b></td>
        <td>Median temporal SNR in brain mask for for b=<b>x</b> frames</td>
    </tr>
    <tr>
        <td>DTerr_rel_b<b>x</b></td>
        <td>Median DTI RMS residual error for b=<b>x</b> frames across voxels relative to within-voxel RMS b=0 signal</td>
    </tr>
    <tr>
        <td>RSIerr_rel_b<b>x</b></td>
        <td>Median RSI RMS residual error for b=<b>x</b> frames across voxels relative to within-voxel RMS b=0 signal</td>
    </tr>
    <tr>
        <td>DTerr_rel</td>
        <td>Median of DTI RMS residual error for all frames across voxels relative to within-voxel RMS signal</td>
    </tr>
    <tr>
        <td>RSIerr_rel</td>
        <td>Median RSI RMS residual error for all frames across voxels relative to within-voxel RMS signal</td>
    </tr>
    <tr>
        <td>NumberOfFilesMissing</td>
        <td>Number of DICOM files apparently missing (based on gaps in InstanceNumbers)</td>
    </tr>
    <tr>
        <td>Num&ltHead|Neck|Spine&gtCoilElem</td>
        <td>Number of head/neck/spine coil elements</td>
    </tr>
    <tr>
        <td>brain_nvox_max</td>
        <td>Number of voxels within brain mask at maximum image intensity</td>
    </tr>
    <tr>
        <td>brain_fvox_max</td>
        <td>Fraction of voxels within brain mask at maximum image intensity</td>
    </tr>
    <tr>
        <td>nonbrain_&ltmean|std|snr&gt</td>
        <td>Mean/Standard deviation/Signal-to-noise ratio (mean/stdev) image intensity outside brain mask</td>
    </tr>
    <tr>
        <td>NumberOfFilesOrig</td>
        <td>Number of DICOM files received (before excluding non-image, corrupt, or extra files)</td>
    </tr>
    <tr>
        <td>NumberOfFilesExtra</td>
        <td style="word-wrap: break-word; white-space: normal;">Number of extra DICOM files received (non-image, corrupt, or extra files)</td>
    </tr>
</tbody>
</table>
</div>

<p></p>

### Workflow

Raw MRI QC combines **automated** and **manual** checks to evaluate unprocessed data and identify acquisition errors, image artifacts, or corrupted files before downstream processing.

Automated QC is applied to all data. Due to the large data volume and time-intensive nature of manual inspection, **manual visual review is only performed for series that fail automated QC**. Although automated tools detect most quality issues, some artifacts may be missed if misclassified or not assessed as part of automated QC.

**As an additional safeguard, QC is also performed on processed outputs** using tools such as <a href="../brainswipes" target="_blank">BrainSwipes</a>. When issues are identified at this stage, the corresponding raw data are re-reviewed and QC decisions are updated as needed. This iterative process improves QC scoring and utilities over time and helps ensure high data quality while minimizing delays in data release.

### <i class="fa fa-desktop"></i> Automated QC

Automated QC is performed at the HBCD Data Coordinating Center (HDCC) immediately after data upload, beginning with [protocol compliance and completeness checks](#compliance). Data that fail these checks are flagged for review and are not included in the release until resolved. 

<div id="compliance" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
<span class="text">Protocol Compliance & Completeness Checks</span>
  <a class="anchor-link" href="#compliance" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Protocol Compliance</strong></p>
<ul>
    <li>Extract imaging parameters from DICOM headers</li>
    <li>Confirm key parameters (e.g., voxel size, TR, orientation) match the expected protocol for each scanner</li>
    <li>Flag out-of-compliance series for review; sites are contacted if corrective action is needed</li>
</ul>
<p><b>Completeness Checks</b><br>
Completeness checks verify that all expected series are present in each imaging session. For example, dMRI and fMRI require paired EPI field maps for distortion correction. Missing data usually indicate an aborted scan or incomplete data transfer (often resolved by re-sending files). Series included in a valid session include the following:</p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Modality</th>
  <th>Required Series</th>
</tr>
</thead>
<tbody>
<tr>
    <td>Structural MRI (sMRI)</td>
    <td>T1w & T2w</td>
</tr>
<tr>
    <td>Functional MRI (fMRI)</td>
    <td>Resting state (rs) runs 1 & 2, each accompanied by fieldmaps acquired in AP and PA phase encoding directions</td>
</tr>
<tr>
    <td>Diffusion MRI (dMRI)</td>
    <td>Diffusion scans acquired in AP and PA phase encoding directions</td>
</tr>
<tr>
    <td>Quantitative MRI (qMRI)</td>
    <td>3DMagic/QALAS and B1 Map</td>
</tr>
<tr>
    <td>MR Spectroscopy (MRS)</td>
    <td> MRS scan and SVS localizer</td>
</tr>
</tbody>
</table>
</div>

For data that pass compliance checks, the following automated QC metrics available in the release are calculated:

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<i>Automated QC Metrics</i>
<thead>
<tr>
    <th>Modality</th>
    <th>QC Procedures</th>
</tr>
</thead>
<tbody>
<tr>
    <td>sMRI & qMRI</td>
    <td>• Estimate motion artifacts using a deep learning model<br>
     • Compute signal-to-noise ratio (SNR)</td>
</tr>
<tr>
<td>fMRI</td>
<td style="word-wrap: break-word; white-space: normal;">
    • Estimate head motion with average <span class="tooltip">FD<span class="tooltiptext">framewise displacement</span></span> and data (sec) at FD thresholds of 0.2/0.3/0.4 mm (<a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">Power et al., 2012</a>)<br>
    • Detect line artifacts and FOV cutoff<br>
    • Compute spatial smoothness (FWHM) and temporal SNR (tSNR) after motion correction (<a href="https://doi.org/10.1016/j.neuroimage.2005.01.007">Triantafyllou et al., 2005</a>)
</td>
</tr>
<tr>
    <td>dMRI</td>
    <td style="word-wrap: break-word; white-space: normal;">
    • Estimate head motion (framewise displacement, FD)<br>
    • Refine motion estimates via registration to tensor-synthesized images (<a href="https://doi.org/10.1002/hbm.20619">Hagler et al., 2009</a>)<br>
    • Identify dark slices (caused by abrupt head movements) using RMS difference between raw and tensor-fitted data<br>
    • Calculate total slices and frames with motion artifacts<br>
    • Detect line artifacts and field-of-view (FOV) cutoff
  </ul>
</td>
</tr>
<tr>
<td>Field Maps</td>
<td>Detect line artifacts and field-of-view (FOV) cutoff</td>
</tr>
<tr>
<td>All</td>
<td>Compute SNR where applicable</td>
</tr>
</tbody>
</table>

### <i class="fa-solid fa-eye"></i> Manual Review
Data is flagged for manual review based on automated QC results using multivariate prediction and Bayesian classifiers. Only a portion of data therefore undergoes both automated and manual review. When automated QC flags a series, trained technicians perform manual visual review and rate artifact severity on a **0–3 scale** (0 = none, 1 = mild, 2 = moderate, 3 = severe). Series with **severe artifacts (score = 3) are rejected (QC = 0)** and excluded from downstream processing. For remaining series, final selection is informed by manual ratings, reviewer notes, and automated QC scores.

<table class="compact-table-no-vertical-lines">
<i>Manual QC Metrics</i>
<thead>
<tr>
    <th>Modality</th>
    <th>QC Procedures & Scoring</th>
</tr>
</thead>
<tbody>
<tr>
    <td>sMRI</td>
    <td>• Motion artifacts (ripples, blurring), scored 0–3<br>
        • Document additional issues (e.g., intensity inhomogeneity, <span class="tooltip">ghosting<span class="tooltiptext">faint displaced copy of anatomy due to slices outside FOV</span></span>)</td>
</tr>
<tr>
    <td>qMRI</td>
    <td>• Same artifact scoring (0–3)<br>
        • Inspect derived data (parametric maps, ROI analysis, quantitative checks for 3D-QALAS)
    </td>
</tr>
<tr>
    <td>dMRI & fMRI, & field maps</td>
    <td style="word-wrap: break-word; white-space: normal;">
    • Score susceptibility artifacts, FOV cutoff, and horizontal line artifacts (present in the sagittal view)<br>
    • Note susceptibility artifacts, including <span class="tooltip">signal dropout<span class="tooltiptext">common in posterior occipital cortex of infant fMRI data acquired in PA phase encoding direction</span></span>, signal bunching, and warping</td>
</tr> 
<tr>
    <td>MRS</td>
    <td>Visual inspection and overall QC only of SVS localizer (used to define spectroscopy ROI)</td>
</tr>
</tbody>
</table>

### References
<div class="references">
    <p>Dean III, D. C., Tisdall, M. D., Wisnowski, J. L., Feczko, E., Gagoski, B., Alexander, A. L., ... &amp; HBCD MRI Working Group. (2024). Quantifying brain development in the HEALthy Brain and Child Development (HBCD) Study: The magnetic resonance imaging and spectroscopy protocol. <em>Developmental Cognitive Neuroscience</em>, 70, 101452. <a href="https://doi.org/10.1016/j.dcn.2024.101452">https://doi.org/10.1016/j.dcn.2024.101452</a></p>
    <p>Gard, A. M., Hyde, L. W., Heeringa, S. G., West, B. T., & Mitchell, C. (2023). Why weight? Analytic approaches for large-scale population neuroscience data. Developmental Cognitive Neuroscience, 59, 101196. <a href="https://doi.org/10.1016/j.dcn.2023.101196">https://doi.org/10.1016/j.dcn.2023.101196</a></p>
    <p>Hagler, D. J., Jr, Ahmadi, M. E., Kuperman, J., Holland, D., McDonald, C. R., Halgren, E., &amp; Dale, A. M. (2009). Automated white-matter tractography using a probabilistic diffusion tensor atlas: Application to temporal lobe epilepsy. Human Brain Mapping, 30(5), 1535–1547. <a href="https://doi.org/10.1002/hbm.20619">https://doi.org/10.1002/hbm.20619</a></p>
    <p>Power, J. D., Barnes, K. A., Snyder, A. Z., Schlaggar, B. L., &amp; Petersen, S. E. (2012). Spurious but systematic correlations in functional connectivity MRI networks arise from subject motion. NeuroImage, 59(3), 2142–2154. <a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">https://doi.org/10.1016/j.neuroimage.2011.10.018</a></p>
    <p>Triantafyllou, C., Hoge, R. D., Krueger, G., Wiggins, C. J., Potthast, A., Wiggins, G. C., &amp; Wald, L. L. (2005). Comparison of physiological noise at 1.5 T, 3 T and 7 T and optimization of fMRI acquisition parameters. NeuroImage, 26(1), 243–250. <a href="https://doi.org/10.1016/j.neuroimage.2005.01.007">https://doi.org/10.1016/j.neuroimage.2005.01.007</a></p>
</div>