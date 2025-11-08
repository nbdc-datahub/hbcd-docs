# HBCD MR Quality Control Procedures

## Raw MR Data QC

Raw MR QC includes **automated** and **manual** checks to evaluate unprocessed MRI data. Raw data QC is performed to detect acquisition errors, image artifacts, or corrupted files early so that problematic scans are excluded from [downstream processing](../processing/index.md#file-selection-for-processing).

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

#### <i class="fa fa-desktop"></i> Automated QC

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

#### <i class="fa-solid fa-eye"></i> Manual Review

Automated metrics flag series for manual review using multivariate prediction and Bayesian classifiers. Trained technicians then score artifact severity on a **0–3 scale** (0 = none, 1 = mild, 2 = moderate, 3 = severe). Series with **severe artifacts (score = 3) are rejected** (QC = 0) and excluded from processing. Data are selected from the remaining series based on manual ratings, notes, and automated scores.

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

## BrainSwipes

Manual visual inspection remains the gold standard for detecting artifacts in structural, functional (e.g., XCP-D), and diffusion (e.g., QSIPrep) derivatives. To support this, derivative visual reports are integrated into [BrainSwipes](https://brainswipes.us/about), a gamified, crowdsourced QC platform built on the open-source [Swipes For Science](https://swipesforscience.org/) framework. BrainSwipes provides an intuitive interface for large-scale studies, guiding users through a short [tutorial](https://brainswipes.us/tutorial-select) before they evaluate images and classify them as pass or fail.

<p>
<div id="swipes-procedures" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-brain"></i></span>
<span class="text-with-link">
  <span class="text">BrainSwipes QC Procedures</span>
	<a class="anchor-link" href="#swipes-procedures" title="Copy link">
  	<i class="fa-solid fa-link"></i>
  	</a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<br>
<div class="img-with-text" style="width: 60%; margin: 0 auto; text-align: center;">
    <img src="../images/brainswipes.png" alt="Example quality assessment of surface delineation in BrainSwipes" style="width: 100%; height: auto;">
    <p><i>Example quality assessment of surface delineation on BrainSwipes platform (displaying brain in axial plane at level of basal ganglia/putamen).</i></p>
</div>
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

**BrainSwipes QC results are provided as [tabulated](../index.md#mri) data**: <code>img_brainswipes_xcpd_hash-<span class="blue-text">&lt;HASH&gt;</span>_<span class="blue-text">&lt;T1w|T2w&gt;</span></code> and <code>img_brainswipes_xcpd_hash-<span class="blue-text">&lt;HASH&gt;</span>_bold</code> (where <code><span class="blue-text">&lt;HASH&gt;</span></code> ID corresponds to the method used for surface reconstruction - see [Dual Surface Reconstruction Methods](mri-proc.md#dual-surface-reconstruction-methods)).
QC scores range from 0 (Fail) to 1 (Pass), averaged across reviewers. For example, a score of 0.6 indicates that 60% of reviewers rated the image as a pass. The data includes overall average QC scores and average number of reviewers for each session-level T2w and BOLD run (summarizing across all visual reports for a given run) as well as the average QC and number of reviewers for each visual report. A Python helper function is provided below to load a BrainSwipes TSV file into a Pandas DataFrame and filter runs with average QC scores above a user-specified threshold:

<div id="python-helper-function" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-brands fa-python"></i></span>
  <span class="text-with-link">
  <span class="text">Python Helper Function</span>
  <a class="anchor-link" href="#python-helper-function" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<pre class="helper-code"><code>
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
</code></pre>
</div>

## QC Summary Statistics

<div id="fconn" class="static-banner" style="border-left: 5px solid #199bd6;">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
    <span class="text">Functional Connectivity as Data Quality Improves</span>
    <a class="anchor-link" href="#fconn" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
</div>
<div class="table-static-content">
<p>Average functional connectivity matrices were computed using the Gordon parcellation from <a href="../fmri/#xcpd">XCP-D derivatives</a> for V02 sessions with data inclusion based on various thresholds of BrainSwipes QC results (<code>img_brainswipes_xcpd-bold</code>; <a href="../qc/#brainswipes">see details</a>). Functional connectivity patterns remained consistent even when incorporating data with lower QC scores, suggesting robustness to mild quality variations.</p>
<p><strong>Connectivity matrices as data quality improves (Left -> Right) based on QC thresholds of 0.1, 0.5, and 0.9:</strong></p>
<img src="../images/fconn_qc.png" style="width: 90%;" class="center">
<br>
</div>
<p></p>

<div id="dwi-qc" class="static-banner" style="border-left: 5px solid #199bd6;">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
    <span class="text">Automated QC for Processed Diffusion Data</span>
    <a class="anchor-link" href="#dwi-qc" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
</div>
<div class="table-static-content">
<p>The current release includes BrainSwipes results for structural and functional MRI only; diffusion results will be added in a future release. However, automated QC for processed diffusion data is fairly robust, with metrics provided in <code>sub-{ID}_ses-{V0X}_space-ACPC_desc-image_qc.tsv</code> within the <a href="../dmri/#qsiprep">QSIPrep derivatives</a>. See the <a href="https://qsiprep.readthedocs.io/en/latest/preprocessing.html#quality-control-data">QSIPrep documentation</a> for details.</p>  
<p>Below are distributions of automated QC metrics from HBCD visits V02 and V03. Higher Neighboring DWI Correlation (NDC; closer to 1) and Contrast-to-Noise Ratio (CNR) indicate better image quality. <strong>NDC can also be used as a covariate in analyses to account for QC variation.</strong></p>  
<p><strong>Left</strong>: NDC calculated pre- and post-processing for each vendor using combined AP/PA scans (solid = processed, dashed = raw).<br>  
<strong>Right</strong>: Shell-wise CNR per vendor, calculated by Eddy. Because all data shown passed preliminary QC, we do not provide exclusion threshold recommendations. However, NDC and CNR are useful covariates when analyzing other derivatives.</p>
<img src="../images/ndc_cnr_comparison.svg" width="95%" height="auto" class="center">
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