# HBCD MR Quality Control Procedures

## Raw MR Data QC

Raw MR QC includes **automated** and **manual** checks to evaluate unprocessed MRI data. The purpose is to detect acquisition errors, artifacts, or corrupted files early so that problematic scans are excluded from the released raw BIDS dataset and downstream processing ([see details](../processing/index.md#file-selection-for-processing)). 

### Automated QC

Automated QC is performed at the HBCD Data Coordinating Center (HDCC) immediately after data upload. It consists of three main steps:

<div id="protocol-compliance" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
<span class="text">Protocol Compliance</span>
  <a class="anchor-link" href="#protocol-compliance" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<ul>
    <li>Extract imaging parameters from DICOM headers</li>
    <li>Confirm key parameters (e.g., voxel size, TR, orientation) match the expected protocol for each scanner</li>
    <li>Flag out-of-compliance series for review; sites are contacted if corrective action is needed</li>
</ul>
</div>

<div id="completeness" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
  <span class="text">Completeness Checks</span>
  <a class="anchor-link" href="#completeness" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Completeness checks verify that all expected series are present in each imaging session. For example, dMRI and fMRI require paired EPI field maps for distortion correction. Missing data usually indicate an aborted scan or incomplete data transfer (often resolved by re-sending files). Series included in a valid session include the following:</p>
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

<div id="autoQC-metrics" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
<span class="text">Automated QC Metrics</span>
  <a class="anchor-link" href="#autoQC-metrics" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
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
</div>

### Manual Review

Automated metrics flag series for manual review using multivariate prediction and Bayesian classifiers. Trained technicians then score artifact severity on a **0–3 scale** (0 = none, 1 = mild, 2 = moderate, 3 = severe). Series with **severe artifacts (score = 3) are rejected** (QC = 0) and excluded from processing. Data are selected from the remaining series based on manual ratings, notes, and automated scores (e.g., ≥60% usable diffusion encoding volumes). Manual QC metrics include the following:
<table class="compact-table-no-vertical-lines">
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

### Location of Raw Data QC Results in Data Release
All quality control metrics are available in the `*_scans.tsv` file provided per participant session ([see details](../../datacuration/file-based-data.md#participant-session-scan-level-data)). The main QC score field, `QC`, is the overall manual QC score and will be a value of either 1 (pass) or 0 (fail). If the scan was not flagged for manual review and only has automated QC data, the `QC` field automatically has value of 1. 

<div id="scanstsv" class="table-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fa fa-table"></i></span>
  <span class="text-with-link">
  <span class="text">Full list of fields included in <code>scans.tsv</code> files</span>
  <a class="anchor-link" href="#scanstsv" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
  <thead>
    <tr>
    <th>Field</th>
    <th style="text-align: center;"><span class="tooltip tooltip-right"><i class="fa-solid fa-eye"></i><span class="tooltiptext">Manual QC</span></span> / <span class="tooltip tooltip-right"><i class="fa-solid fa-desktop"></i><span class="tooltiptext">Automated QC</span></span></th>
    <th>Description</th>
    </tr>
    </thead>
    <tr>
        <td>filename</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td>Relative paths to files</td>
    </tr>
    <tr>
        <td>acq_time</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td>Acquisition time</td>
    </tr>
    <tr>
        <td>loris_qc_status</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td>Pass Fail mapping from UCSD QC JSON file</td>
    </tr>
    <tr>
        <td>loris_selected</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Whether the file is selected for further processing</td>
    </tr>
    <tr>
        <td>site</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Site where the session data was collected</td>
    </tr>
    <tr>
        <td>age</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Age (in years) of the candidate at the time of the scan</td>
    </tr>
    <tr>
        <td>age_adjusted</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Adjusted age (in days) based on the EDD</td>
    </tr>
    <tr>
        <td>head_size</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Head size at the time of the scan</td>
    </tr>
    <tr>
        <td>nrev</td>
        <td><i class="fa-solid fa-eye"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of manual QC reviewers</td>
    </tr>
    <tr>
        <td>revdisp</td>
        <td><i class="fa-solid fa-eye"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">If there was disparity/disagreement between reviewers</td>
    </tr>
    <tr>
        <td>QC</td>
        <td><i class="fa-solid fa-eye"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Overall manual QC score: 1 (pass), 0 (fail)</td>
    </tr>
    <tr>
        <td>notes</td>
        <td><i class="fa-solid fa-eye"></td>
        <td style="word-wrap: break-word; white-space: normal;">Optional notes from manual QC review</td>
    </tr>
    <tr>
        <td>QU_motion</td>
        <td><i class="fa-solid fa-eye"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Qualitative manual QC score for motion (<i>sMRI & qMRI</i>)</td>
    </tr>
    <tr>
        <td>QU_sus</td>
        <td><i class="fa-solid fa-eye"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Qualitative manual QC score for susceptibility artifact (<i>dMRI, fMRI, & field maps</i>)</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">QU_cutoff</td>
        <td><i class="fa-solid fa-eye"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Qualitative manual QC score for FOV cutoff artifact (<i>dMRI, fMRI, & field maps</i>)</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">QU_line</td>
        <td><i class="fa-solid fa-eye"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Qualitative manual QC score for line artifact (<i>dMRI, fMRI, & field maps</i>)</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">line_nframes</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of frames with line artifacts</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">line_&ltmax|mean&gt_score</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">&ltMaximum|Average&gt line artifact score across frames</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">line_&ltmax|mean&gt_count</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">&ltMaximum|Average&gt line artifact count across frames</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">cutoff</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Sum of dorsal and ventral cutoff scores</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">&ltdorsal|ventral&gt_cutoff</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">&ltDorsal|Ventral&gt cutoff score</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">brain_&ltmean|std&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">&ltAverage|Standard deviation&gt image intensity within brain mask</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">brain_SNR</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Signal-to-noise ratio (mean/stdev) of image intensity within brain mask</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">brain_&ltmin|max|median&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">&ltMinimum|Maximum|Median&gt image intensity within brain mask</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">brain_tSNR_&ltmean|median|std&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">&ltAverage|Median|Standard deviation&gt temporal SNR in brain mask</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">mean_&ltmotion|trans|rot&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Average framewise &ltdisplacement|translation|rotation&gt (mm)</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">max_d&ltx|y|z&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Maximum absolute &ltx|y|z&gt translation (mm)</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">max_r&ltx|y|z&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Maximum absolute &ltx|y|z&gt rotation (mm)</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">subthresh_&lt02|03|04&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of seconds with framewise displacement less than &lt0.2|0.3|0.4&gt mm</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">aqc_motion</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Automated QC motion score for sMRI</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">nreps</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of repetitions / frames</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">brainvol</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Volume of brain mask (mm^3)</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">fwhm_x</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Full width half max spatial smoothness in x-axis (left-right)</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">b0_&ltmedian|std&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">&ltMedian|Standard Deviation&gt b=0 intensity in brain mask</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">DTerr_&ltmean|median|std&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">&ltAverage|Median|Standard deviation&gt across frames of RMS residual error relative to RMS signal in brain voxels</td>
    </tr>
    <tr>
        <td>Completed</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Whether the series has the expected # of files</td>
    </tr>
    <tr>
        <td>NumberOfFiles</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of DICOM files</td>
    </tr>
    <tr>
        <td>HBCD_compliant</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Whether the series passes a minimal protocol compliance check</td>
    </tr>
    <tr>
        <td>AdditionalInfo</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Notes related to classification and protocol compliance</td>
    </tr>
    <tr>
        <td>MD_std</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Standard deviation of mean diffusivity in brain mask</td>
    </tr>
    <tr>
        <td>b0_mean</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Average b=0 intensity in brain mask</td>
    </tr>
    <tr>
        <td>FA_std</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Standard deviation of fractional anisotropy in brain mask</td>
    </tr>
    <tr>
        <td>MD_&ltmean|median&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">&ltAverage|Median&gt mean diffusivity in brain mask</td>
    </tr>
    <tr>
        <td>max_nbad_frames_per_&ltslice|frame&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Maximum # of outlier frames per &ltslice|frame&gt</td>
    </tr>
    <tr>
        <td>FA_&ltmean|median&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">&ltAverage|Median&gt fractional anisotropy in brain mask</td>
    </tr>
    <tr>
        <td>fwhm_z</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Full width half max spatial smoothness in z-axis (inferior-superior)</td>
    </tr>
    <tr>
        <td>nbad_frame_slices</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of outlier frame-slices for dMRI</td>
    </tr>
    <tr>
        <td>nbad_frames</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of frames with outlier slices for dMRI</td>
    </tr>
    <tr>
        <td>nbad_slices</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of slices with outlier frames for dMRI</td>
    </tr>
    <tr>
        <td>fwhm_y</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Full width half max spatial smoothness in y-axis (anterior-posterior)</td>
    </tr>
    <tr>
        <td>qc_status</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Whether review is pending, complete, or has other status</td>
    </tr>
    <tr>
        <td>ngood_frames</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of frames without outlier slices for dMRI</td>
    </tr>
    <tr>
        <td>censor_thresh</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Threshold used for censoring outlier slices for dMRI</td>
    </tr>
    <tr>
        <td>nframes_b&ltN&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of b=&lt0|500|1000|2000|3000&gt frames</td>
    </tr>
    <tr>
        <td>nbad_frame_slices_b&ltN&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of outlier frame-slices for dMRI b=&lt0|500|1000|2000|3000&gt frames</td>
    </tr>
    <tr>
        <td>nbad_frames_b&ltN&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of frames with outlier slices for dMRI b=&lt0|500|1000|2000|3000&gt frames</td>
    </tr>
    <tr>
        <td>nbad_slices_b&ltN&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of slices with outlier frames for dMRI b=&lt0|500|1000|2000|3000&gt frames</td>
    </tr>
    <tr>
        <td>ngood_frames_b&ltN&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of frames without outlier slices for dMRI b=&lt0|500|1000|2000|3000&gt frames</td>
    </tr>
    <tr>
        <td>FWHMx_b&ltN&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Full width half max spatial smoothness in x-axis (left-right) for b=&lt0|500|1000|2000|3000&gt frames</td>
    </tr>
    <tr>
        <td>FWHMy_b&ltN&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Full width half max spatial smoothness in y-axis (anterior-posterior) for b=&lt0|500|1000|2000|3000&gt frames</td>
    </tr>
    <tr>
        <td>FWHMz_b&ltN&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Full width half max spatial smoothness in z-axis (inferior-superior) for b=&lt0|500|1000|2000|3000&gt frames</td>
    </tr>
    <tr>
        <td>tSNR_b&ltN&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Median temporal SNR in brain mask for b=&lt0|500|1000|2000|3000&gt frames</td>
    </tr>
    <tr>
        <td>DTerr_rel_b&ltN&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Median across brain voxels of DTI RMS residual error for b=&lt0|500|1000|2000|3000&gt frames relative to within-voxel RMS b=0 signal</td>
    </tr>
    <tr>
        <td>RSIerr_rel_b&N&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Median across brain voxels of RSI RMS residual error for b=&lt0|500|1000|2000|3000&gt frames relative to within-voxel RMS b=0 signal</td>
    </tr>
    <tr>
        <td>DTerr_rel</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Median across brain voxels of DTI RMS residual error for all frames relative to within-voxel RMS signal</td>
    </tr>
    <tr>
        <td>RSIerr_rel</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Median across brain voxels of RSI RMS residual error for all frames relative to within-voxel RMS signal</td>
    </tr>
    <tr>
        <td>NumberOfFilesMissing</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of DICOM files apparently missing (based on gaps in InstanceNumbers)</td>
    </tr>
    <tr>
        <td>Num&ltHead|Neck|Spine&gtCoilElem</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of &lthead|neck|spine&gt coil elements</td>
    </tr>
    <tr>
        <td>brain_nvox_max</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># of voxels within brain mask at maximum image intensity</td>
    </tr>
    <tr>
        <td>brain_fvox_max</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">Fraction of voxels within brain mask at maximum image intensity</td>
    </tr>
    <tr>
        <td>nonbrain_&ltmean|std|snr&gt</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;">&ltAverage|Standard deviation|Signal-to-noise ratio (mean/stdev)&gt image intensity outside brain mask</td>
    </tr>
    <tr>
        <td>NumberOfFilesOrig</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># DICOM files received (before excluding non-image, corrupt, or extra files)</td>
    </tr>
    <tr>
        <td>NumberOfFilesExtra</td>
        <td><i class="fa-solid fa-desktop"></i></td>
        <td style="word-wrap: break-word; white-space: normal;"># Extra DICOM files received (non-image, corrupt, or extra files)</td>
    </tr>
</tbody>
</table>
</div>

## Data Release Eligibility Criteria

After converting MRI data to BIDS format, both the NIfTI and JSON files undergo additional verification to ensure data integrity. Acquisition parameters can vary depending on the scanner vendor. For example, while the GE protocol acquires structural data at **0.8 mm isotropic resolution**, the current protocol/software version upsamples the data during reconstruction and DICOM creation, resulting in an **in-plane resolution of 0.5 × 0.5 × 0.8 mm³**. This will be adjusted in a future software upgrade. To account for such variations, most inclusion criteria are defined as acceptable **ranges** rather than fixed values. The specific modality-based inclusion criteria are extracted directly from the image JSON files and evaluated accordingly.

<p>
<div id="acq-param-table" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text">Acquisition Parameter Ranges for Data Release Eligibility</span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><i>NOTE: All images are additionally checked to confirm they were acquired using a head coil.</i></p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
  <thead>
    <tr>
      <th style="width: 100%; border-collapse: collapse; table-layout: fixed;">File</th>
      <th style="width: 100%; border-collapse: collapse; table-layout: fixed;">TR</th>   
      <th style="width: 100%; border-collapse: collapse; table-layout: fixed;">TE</th>        
      <th style="width: 100%; border-collapse: collapse; table-layout: fixed;">TI</th>    
      <th style="width: 100%; border-collapse: collapse; table-layout: fixed;">Slice Thickness</th>  
      <th style="width: 100%; border-collapse: collapse; table-layout: fixed;">Volume #</th>  
    </tr>
  </thead>
<tbody>
	<tr>
		<td>T1w</td>
		<td>2.3-2.41</td>
    <td>0.002-0.0035</td>
		<td>1.06-1.1</td>    
    <td>0.8</td>    
    <td>NA</td>    
	</tr>
	<tr>
		<td>T2w</td>
		<td>2.5-4.5</td>
    <td>0.09-0.15</td>
		<td>0.29-0.33</td>    
    <td>0.563-0.565</td>    
    <td>NA</td>
	</tr>  
	<tr>
		<td>MRS Localizer</td>
		<td>2.5-4.5</td>
    <td>0.09-0.15</td>
		<td>0.29-0.33</td>    
    <td>0.563-0.565</td>    
    <td>NA</td>
	</tr>   
	<tr>
		<td>Diffusion</td>
		<td>4.8</td>
    <td>0.0880-0.0980</td>
		<td>NA</td>    
    <td>1.7</td>    
    <td style="word-wrap: break-word; white-space: normal;">≥ 90 (AP + PA)</td>  
	</tr>  
	<tr>
		<td>EPI Fieldmap</td>
		<td>8.4-9.2</td>
    <td>0.064-0.0661</td>
		<td>2</td>    
    <td>0.563-0.565</td>    
    <td>NA</td>
	</tr>  
	<tr>
		<td>Functional</td>
		<td>1.725</td>
    <td>0.0369-0.0371</td>
		<td>NA</td>    
    <td>2</td>  
    <td>≥ 87 (~2.5 min)</td>   
	</tr>  
</tbody>
</table>
</div>
</p>

## BrainSwipes

Manual visual inspection remains the gold standard for identifying artifacts in structural and functional derivatives (e.g., from XCP-D) and diffusion derivatives (e.g., from QSIPrep). To streamline this process, derivative visual reports are integrated into [BrainSwipes](https://brainswipes.us/about), a gamified, crowdsourced QC platform built on the open-source [Swipes For Science](https://swipesforscience.org/) framework. BrainSwipes engages users in evaluating brain image quality through an intuitive interface designed for large-scale studies. After creating an account, users are guided through a brief [tutorial](https://brainswipes.us/tutorial-select) that teaches them how to assess derivative images and classify them as pass or fail.

<p>
<div id="swipes-procedures" class="table-banner" onclick="toggleCollapse(this)">
<span class="text-with-link">
  <span class="text">BrainSwipes QC Procedures</span>
	<a class="anchor-link" href="#swipes-procedures" title="Copy link">
  	<i class="fa-solid fa-link"></i>
  	</a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>
<p style="font-size: 1em; margin: 0 0 5px;"><b>Surface Delineation:</b></p>
For structural QA, swipers are presented with image slices in coronal, axial, and sagittal planes to assess the accuracy of T1w and T2w surface delineations in differentiating gray and white matter. Images are derived from XCP-D visual reports.
</p>
<p style="font-size: 1em; margin: 0 0 5px;"><b>Atlas Registration:</b></p>
In addition to surface delineation, structural QA also includes atlas registration quality, evaluated by overlaying delineations of the subject’s image onto the atlas, and vice versa. Swipes display nine T1w slices for visual inspection, with three slices per anatomical plane. Quality is assessed based on the alignment of the outer boundaries of the overlaid contours with those of the underlying image, ensuring minimal gaps or misalignments. Images are derived from XCP-D visual reports.
<p>
<p style="font-size: 1em; margin: 0 0 5px;"><b>Functional Registration:</b></p>
Functional registration is evaluated by overlaying outlines of functional images onto structural images and vice versa. Swipes display nine slices of the same functional image for visual inspection, with three slices per anatomical plane. Quality is assessed similarly to structural atlas registration, focusing on the alignment of the overlaid contours. Additional evaluation includes checking for artifacts such as signal dropout. Images are derived from XCP-D visual reports.
</p>
<p style="font-size: 1em; margin: 0 0 5px;"><b>Diffusion Direction Encoding (<i>to be included in future release</i>):</b></p>
Swipes display GIFs of full-resolution T2w images as a grayscale background, with the "Direction Encoded Color" (DEC) map overlaid. These GIFs sweep through a portion of the brain across the three anatomical planes. High-quality processed DWI images exhibit bands of color that closely follow the folds and contours of the grayscale background. These visuals are derived from the QSIPrep report.
<p>
<strong>Each visual report for a given modality is independently reviewed and rated as a pass or fail, which in the outputs are scored as values of 1 and 0 respectively. BrainSwipes generates a summary of these results that includes the average score as well as number of reviewers for each visual report of each modality.</strong>
</div>
</p>

<div class="img-with-text" style="width: 60%; margin: 0 auto; text-align: center;">
    <img src="../images/brainswipes.png" alt="Example quality assessment of surface delineation in BrainSwipes" style="width: 100%; height: auto;">
    <p><i>Example quality assessment of surface delineation on BrainSwipes platform (displaying brain in axial plane at level of basal ganglia/putamen).</i></p>
</div>

### BrainSwipes Results Provided in Data Release

<p>
<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text">
    BrainSwipes Quality Control (QC) Scoring
  </span>
</div>
<div class="notification-static-content">
<p>QC scores range from 0 to 1, where 0 indicates a "Fail" and 1 indicates a "Pass." Scores are averaged across reviewers. For example, an average QC score of 0.6 means that 60% of reviewers rated the image as a pass.</p>
</div>
</p>

BrainSwipes QC results are provided as <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> instrument data in the `rawdata/phenotype/` folder of the data release (see details [here](../../datacuration/phenotypes.md)), including `img_brainswipes_xcpd-T2w` and `img_brainswipes_xcpd-bold` instrument files. These files contain the BrainSwipes results reporting the average QC score and number of reviewers for each individual visual report. 

The results are also combined for each subject modality to report the overall average QC score and average number of reviewers across visual reports per run. In other words, a single average QC score is provided for each session-level T2w and session-level BOLD run. Below we provide a Python helper function to read a BrainSwipes TSV file into a Pandas DataFrame and filter out all subject runs with an average overall QC score of greater than or equal to a threshold specified by the user:

##### 🐍 Python Helper Function

```
import pandas as pd

def read_and_filter_tsv(file_path, threshold):
    """
    Reads an HBCD BrainSwipes TSV file into a DataFrame and keeps subject rows where 
	the overall average QC value is greater than or equal to the specified threshold.

    Parameters:
    - file_path (str): Path to the .tsv file
    - threshold (float): Threshold value for filtering

    Returns:
    - pd.DataFrame: Filtered DataFrame
    """
    df = pd.read_csv(file_path, sep='\t')

    fourth_col = df.columns[3]
    return df[df[fourth_col] >= threshold]

# Example usage:
# Filter to keep only subjects with an average structural QC of at least 0.6 (60% pass rate)
filtered_df = read_and_filter_tsv("img_brainswipes_xcpd_T2w.tsv", 0.6)
print(filtered_df.head())
```
## QC Summary Statistics

<div id="dwi-qc" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text-with-link">
  <span class="text">Automated QC for Processed Diffusion Data</span>
  <a class="anchor-link" href="#dwi-qc" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<p>The release currently includes BrainSwipes results for only structural and functional MRI. Diffusion results will be included in a later release. However, existing automated QC procedures for processed diffusion data are fairly robust compared to sMRI and fMRI. The automated QC metrics are provided within <code>SUBSES_space-ACPC_desc-image_qc.tsv</code> in the <a href="../../../datacuration/derivatives/#qsiprep-qsiprep">QSIPrep derivatives</a> - please see more information about automated QC on the <a href="https://qsiprep.readthedocs.io/en/latest/preprocessing.html#quality-control-data">QSIPrep website</a>.</p>
<p>Below are automated QC metric distributions for HBCD data from visits V02 and V03. Higher NDC (closer to 1) and CNR indicate better quality images. <strong>NDC can be used as a covariate in analyses to account for variation in QC.</strong></p>
<p><b>Left</b>: Neighboring DWI Correlation (NDC) calculated pre and post processing for each vendor on the combined AP/PA scans. Processed data is represented by a solid line, while raw data is dashed.</p>
<p><b>Right</b>: Contrast to Noise Ratio (CNR) per shell per vendor as calculated by Eddy. Distributions are likewise colored by vendor. As data included in these plots and in the beta release have already passed a preliminary QC check we do not have specific values recommended for exclusion. However, NDC and CNR are useful covariates to include when analyzing other derivatives.</p>
<img src="../images/ndc_cnr_comparison.svg" width="95%" height="auto" class="center">
</div>


<div id="fconn" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text-with-link">
  <span class="text">Functional Connectivity as Data Quality Improves</span>
  <a class="anchor-link" href="#fconn" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="notification-collapsible-content">
<p><b>Average Gordon Connectivity Matrices for V02 at Varying QC Thresholds</b><br>
Average functional connectivity matrices were computed using the Gordon parcellation from <a href="../../../datacuration/derivatives/#xcp-d-xcp_d">XCP-D derivatives</a> for V02 sessions with data inclusion based on various thresholds of BrainSwipes QC results (<code>img_brainswipes_xcpd-bold</code>; <a href="../qc/#brainswipes">see details</a>). Functional connectivity patterns remained consistent even when incorporating data with lower QC scores, suggesting robustness to mild quality variations.</p>
<p><strong>The following figures display connectivity matrices as data quality improves (Left -> Right) based on QC thresholds of 0.1, 0.5, and 0.9:</strong></p>
<img src="../images/fconn_qc.png" style="width: 100%;" class="center">
<br>
</div>




## References
<div class="references">
    <p>Dean III, D. C., Tisdall, M. D., Wisnowski, J. L., Feczko, E., Gagoski, B., Alexander, A. L., ... &amp; HBCD MRI Working Group. (2024). Quantifying brain development in the HEALthy Brain and Child Development (HBCD) Study: The magnetic resonance imaging and spectroscopy protocol. <em>Developmental Cognitive Neuroscience</em>, 70, 101452. <a href="https://doi.org/10.1016/j.dcn.2024.101452">https://doi.org/10.1016/j.dcn.2024.101452</a></p>
    <p>Gard, A. M., Hyde, L. W., Heeringa, S. G., West, B. T., & Mitchell, C. (2023). Why weight? Analytic approaches for large-scale population neuroscience data. Developmental Cognitive Neuroscience, 59, 101196. <a href="https://doi.org/10.1016/j.dcn.2023.101196">https://doi.org/10.1016/j.dcn.2023.101196</a></p>
    <p>Hagler, D. J., Jr, Ahmadi, M. E., Kuperman, J., Holland, D., McDonald, C. R., Halgren, E., &amp; Dale, A. M. (2009). Automated white-matter tractography using a probabilistic diffusion tensor atlas: Application to temporal lobe epilepsy. Human Brain Mapping, 30(5), 1535–1547. <a href="https://doi.org/10.1002/hbm.20619">https://doi.org/10.1002/hbm.20619</a></p>
    <p>Power, J. D., Barnes, K. A., Snyder, A. Z., Schlaggar, B. L., &amp; Petersen, S. E. (2012). Spurious but systematic correlations in functional connectivity MRI networks arise from subject motion. NeuroImage, 59(3), 2142–2154. <a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">https://doi.org/10.1016/j.neuroimage.2011.10.018</a></p>
    <p>Triantafyllou, C., Hoge, R. D., Krueger, G., Wiggins, C. J., Potthast, A., Wiggins, G. C., &amp; Wald, L. L. (2005). Comparison of physiological noise at 1.5 T, 3 T and 7 T and optimization of fMRI acquisition parameters. NeuroImage, 26(1), 243–250. <a href="https://doi.org/10.1016/j.neuroimage.2005.01.007">https://doi.org/10.1016/j.neuroimage.2005.01.007</a></p>
</div>
<br>
