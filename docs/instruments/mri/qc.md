# HBCD MR Quality Control Procedures

## Raw MR Data QC

Raw MRI QC combines **automated** and **manual** checks to evaluate unprocessed data and identify acquisition errors, image artifacts, or corrupted files before downstream processing. Automated QC is applied to all data. Due to the large data volume and time-intensive nature of manual inspection, manual visual review is only performed for series that fail automated QC. Although automated tools detect most quality issues, some artifacts may be missed if misclassified or not assessed as part of automated QC. Raw MR QC metrics are provided in the raw BIDS `scans.tsv` files in the release.

<div id="scans-tsv" class="banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-circle-check"></i></span>
<span class="text-with-link">
<span class="text">QC Metrics Included in SCANS TSV Files</span>
<a class="anchor-link" href="#scans-tsv" title="Copy link"><i class="fa-solid fa-link"></i></a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead><tr><th>Field</th><th>Description</th></tr></thead>
<tbody>
<tr class="table-group-row"><td colspan="2">[ Summary QC Metric ]</td></tr>
<tr><td><code>QC</code></td><td>Overall QC score: 1 (pass) or 0 (fail). If manual QC is not required, this equals <code>auto_qc_score</code></td></tr>

<tr class="table-group-row"><td colspan="2">[ Manual QC Metrics ]</td></tr>
<tr><td><code>notes</code></td><td>Optional notes from manual QC review</td></tr>
<tr><td><code>nrev</code></td><td>Number of manual QC reviewers</td></tr>
<tr><td><code>QU_cutoff</code></td><td>Qualitative manual QC score for FOV cutoff artifacts (dMRI, fMRI, and field maps)</td></tr>
<tr><td><code>QU_line</code></td><td>Qualitative manual QC score for line artifacts (dMRI, fMRI, and field maps)</td></tr>
<tr><td><code>QU_motion</code></td><td>Qualitative manual QC score for motion (sMRI and qMRI)</td></tr>
<tr><td><code>QU_sus</code></td><td>Qualitative manual QC score for susceptibility artifacts (dMRI, fMRI, and field maps)</td></tr>

<tr class="table-group-row"><td colspan="2">[ Automated QC Metrics ]</td></tr>
<tr><td><code>AdditionalInfo</code></td><td>Notes on classification and protocol compliance</td></tr>
<tr><td><code>aqc_motion</code></td><td>Automated motion QC score for sMRI</td></tr>
<tr><td><code>auto_qc_notes</code></td><td>Reason for automated QC failure</td></tr>
<tr><td><code>auto_qc_score</code></td><td>Automated QC score: 1 (pass) or 0 (fail)</td></tr>
<tr><td><code>b0_mean</code></td><td>Mean b=0 image intensity within the brain mask</td></tr>
<tr><td><code>b0_{median|std}</code></td><td>Median or standard deviation of b=0 image intensity within the brain mask</td></tr>
<tr><td><code>bad_philips_exam_card_values</code></td><td>Whether the QALAS exam card used for acquisition contained incorrect values</td></tr>
<tr><td><code>brain_entropy</code></td><td>Entropy of voxel intensities within the brain mask</td></tr>
<tr><td><code>brain_{mean|std|SNR}</code></td><td>Mean, standard deviation, or SNR of image intensity within the brain mask</td></tr>
<tr><td><code>brain_{min|max|median}</code></td><td>Minimum, maximum, or median image intensity within the brain mask</td></tr>
<tr><td><code>brain_{n|f}vox_max</code></td><td>Number or fraction of voxels within the brain mask at maximum image intensity</td></tr>
<tr><td><code>brain_tSNR_{mean|median|std}</code></td><td>Mean, median, or standard deviation of temporal SNR within the brain mask</td></tr>
<tr><td><code>brainvol</code></td><td>Volume of the brain mask (mm<sup>3</sup>)</td></tr>
<tr><td><code>censor_thresh</code></td><td>Threshold used to censor outlier slices (dMRI)</td></tr>
<tr><td><code>Completed</code></td><td>Whether the series contains the expected number of files</td></tr>
<tr><td><code>cutoff</code></td><td>Sum of the dorsal and ventral cutoff scores</td></tr>
<tr><td><code>{dorsal|ventral}_cutoff</code></td><td>Dorsal or ventral cutoff score</td></tr>
<tr><td><code>{DT|RSI}err_rel</code></td><td>Median DTI or RSI RMS error across all frames and voxels, relative to the within-voxel RMS signal</td></tr>
<tr><td><code>{DT|RSI}err_rel_b{X}</code></td><td>Median DTI or RSI RMS error across voxels for b-value <code>X</code>, relative to the within-voxel RMS b=0 signal (<code>X</code> = <code>0–3000</code>)</td></tr>
<tr><td><code>DTerr_{mean|median|std}</code></td><td>Mean, median, or standard deviation across frames of RMS residual error relative to RMS signal within brain voxels</td></tr>
<tr><td><code>FA_{mean|median}</code></td><td>Mean or median fractional anisotropy within the brain mask</td></tr>
<tr><td><code>FA_std</code></td><td>Standard deviation of fractional anisotropy within the brain mask</td></tr>
<tr><td><code>fwhm_x</code></td><td>Full width at half maximum spatial smoothness along the x-axis (left–right)</td></tr>
<tr><td><code>fwhm_y</code></td><td>Full width at half maximum spatial smoothness along the y-axis (anterior–posterior)</td></tr>
<tr><td><code>fwhm_z</code></td><td>Full width at half maximum spatial smoothness along the z-axis (inferior–superior)</td></tr>
<tr><td><code>FWHM{x|y|z}_b{X}</code></td><td>FWHM spatial smoothness along the x-, y-, or z-axis (L–R, A–P, or I–S) for b-value <code>X</code> (<code>X</code> = <code>0–3000</code>)</td></tr>
<tr><td><code>HBCD_compliant</code></td><td>Whether the series passes the minimal protocol compliance check</td></tr>
<tr><td><code>line_max_{score|count}</code></td><td>Maximum line artifact score or count across frames</td></tr>
<tr><td><code>line_mean_{score|count}</code></td><td>Mean line artifact score or count across frames</td></tr>
<tr><td><code>line_nframes</code></td><td>Number of frames with line artifacts</td></tr>
<tr><td><code>loris_qc_status</code></td><td>Pass/fail value mapped from the UCSD QC JSON file</td></tr>
<tr><td><code>loris_selected</code></td><td>Whether the file is selected for further processing</td></tr>
<tr><td><code>max_{dx|dy|dz|rx|ry|rz}</code></td><td>Maximum absolute x-, y-, or z-axis translation (<code>d</code>) or rotation (<code>r</code>) (mm)</td></tr>
<tr><td><code>max_nbad_frames_per_frame</code></td><td>Maximum number of outlier frames identified for any frame</td></tr>
<tr><td><code>max_nbad_frames_per_slice</code></td><td>Maximum number of outlier frames identified for any slice</td></tr>
<tr><td><code>MD_{mean|median}</code></td><td>Mean or median mean diffusivity within the brain mask</td></tr>
<tr><td><code>MD_std</code></td><td>Standard deviation of mean diffusivity within the brain mask</td></tr>
<tr><td><code>mean_{motion|trans|rot}</code></td><td>Mean framewise displacement, translation, or rotation (mm)</td></tr>
<tr><td><code>nbad_{frames|slices}</code></td><td>Number of frames or slices containing outlier slices or frames (dMRI)</td></tr>
<tr><td><code>nbad_{frames|slices}_b{X}</code></td><td>Number of frames or slices containing outlier slices or frames for b-value <code>X</code> (dMRI; <code>X</code> = <code>0–3000</code>)</td></tr>
<tr><td><code>nbad_frame_slices</code></td><td>Number of outlier frame–slice combinations (dMRI)</td></tr>
<tr><td><code>nbad_frame_slices_b{X}</code></td><td>Number of outlier frame–slice combinations for b-value <code>X</code> (dMRI; <code>X</code> = <code>0–3000</code>)</td></tr>
<tr><td><code>nframes_b{X}</code></td><td>Number of frames for b-value <code>X</code> (<code>X</code> = <code>0–3000</code>)</td></tr>
<tr><td><code>ngood_frames</code></td><td>Number of frames without outlier slices (dMRI)</td></tr>
<tr><td><code>ngood_frames_b{X}</code></td><td>Number of frames without outlier slices for b-value <code>X</code> (dMRI; <code>X</code> = <code>0–3000</code>)</td></tr>
<tr><td><code>nonbrain_{mean|std|snr}</code></td><td>Mean, standard deviation, or SNR of image intensity outside the brain mask</td></tr>
<tr><td><code>nreps</code></td><td>Number of repetitions or frames</td></tr>
<tr><td><code>NumberOfFiles</code></td><td>Number of DICOM files</td></tr>
<tr><td><code>NumberOfFilesExtra</code></td><td>Number of extra DICOM files received, including non-image, corrupt, or duplicate files</td></tr>
<tr><td><code>NumberOfFilesMissing</code></td><td>Number of DICOM files apparently missing based on gaps in <code>InstanceNumber</code> values</td></tr>
<tr><td><code>NumberOfFilesOrig</code></td><td>Number of DICOM files received before excluding non-image, corrupt, or extra files</td></tr>
<tr><td><code>NumberOfFilesValid</code></td><td>Number of valid DICOM files after excluding non-image, corrupt, or extra files, but before excluding files from the final partial frame</td></tr>
<tr><td><code>Num{Head|Neck|Spine}CoilElem</code></td><td>Number of head, neck, or spine coil elements</td></tr>
<tr><td><code>part_of_a_pair</code></td><td>Whether the DWI file is part of a pair</td></tr>
<tr><td><code>qc_selection</code></td><td>Whether the series is selected for manual QC</td></tr>
<tr><td><code>qc_status</code></td><td>Manual QC review status, such as pending or complete</td></tr>
<tr><td><code>revdisp</code></td><td>Whether manual QC reviewers disagreed</td></tr>
<tr><td><code>subthresh_{02|03|04}</code></td><td>Number of seconds with framewise displacement below 0.2, 0.3, or 0.4 mm</td></tr>
<tr><td><code>tSNR_b{X}</code></td><td>Median temporal SNR within the brain mask for b-value <code>X</code> (<code>X</code> = <code>0–3000</code>)</td></tr>
</tbody>
</table>
</div>

### Protocol Adherence & Completeness Checks
Acquired imaging data are automatically uploaded to central servers, where they undergo automated protocol compliance and completeness checks. Data that fail are flagged for review and excluded from release until the issues are resolved.
 
 - **Protocol compliance** is performed by extracting imaging parameters from DICOM headers to confirm that key parameters (e.g., voxel size, TR, orientation) match the expected scanner protocol. Out-of-compliance series are flagged for review, with site followup as necessary.
 - **Completeness checks** verify that all expected series are present in each imaging session. Missing data may be caused by aborted scans, incomplete sessions, and/or incomplete data transfer. Valid sessions are expected to include: T1w & T2w, 2 resting state functional runs (each accompanied by fieldmaps acquired in AP/PA phase encoding directions), diffusion scans (acquired AP/PA), quantitative QALAS and B1 maps, and MRS scan and SVS localizer.

### Automated QC
<!-- 
<div id="compliance" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
<span class="text">Protocol Compliance & Completeness Checks</span>
  <a class="anchor-link" href="#compliance" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Acquired imaging data are automatically uploaded to central servers, where they undergo automated protocol compliance and completeness checks. Data that fail are flagged for review and excluded from release until the issues are resolved.</p>
<p><b>Protocol compliance</b> is performed by extracting imaging parameters from DICOM headers to confirm that key parameters (e.g., voxel size, TR, orientation) match the expected scanner protocol. Out-of-compliance series are flagged for review, with site followup as necessary.</p>
<p><b>Completeness checks</b> verify that all expected series are present in each imaging session. Missing data may be caused by aborted scans, incomplete sessions, and/or incomplete data transfer. Valid sessions are expected to include: T1w & T2w, 2 resting state functional runs (each accompanied by fieldmaps acquired in AP/PA phase encoding directions), diffusion scans (acquired AP/PA), quantitative QALAS and B1 maps, and MRS scan and SVS localizer. </p>
</div> -->

Data that pass protocol adherence and completeness checks move to the next stage of automated QC, calculated for modalities as follows:

<table class="compact-table-no-vertical-lines readme-intro">
  <thead>
    <tr>
      <th>Modality</th>
      <th>Automated QC Metrics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>sMRI &amp; qMRI</td>
      <td>
        <ul>
          <li>Estimate motion artifacts using a deep learning model</li>
          <li>Compute signal-to-noise ratio (SNR)</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>fMRI</td>
      <td>
        <ul>
          <li>
            Estimate head motion with average framewise displacement and data (sec) at FD thresholds of 0.2/0.3/0.4 mm
            (<a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">Power et al., 2012</a>)
          </li>
          <li>Detect line artifacts and FOV cutoff</li>
          <li>
            Compute spatial smoothness (FWHM) and temporal SNR (tSNR) after motion correction
            (<a href="https://doi.org/10.1016/j.neuroimage.2005.01.007">Triantafyllou et al., 2005</a>)
          </li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>dMRI</td>
      <td>
        <ul>
          <li>Estimate head motion (framewise displacement, FD)</li>
          <li>
            Refine motion estimates via registration to tensor-synthesized images
            (<a href="https://doi.org/10.1002/hbm.20619">Hagler et al., 2009</a>)
          </li>
          <li>
            Identify dark slices (caused by abrupt head movements) using RMS difference
            between raw and tensor-fitted data
          </li>
          <li>Calculate total slices and frames with motion artifacts</li>
          <li>Detect line artifacts and field-of-view (FOV) cutoff</li>
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

### Manual Review

Data are flagged for manual review based on automated QC results using multivariate prediction and Bayesian classifiers, so only a subset undergoes both automated and manual review. When a series is flagged, trained technicians perform visual review and rate artifact severity on a **0–3 scale**: *none* (**0**), *mild* (**1**), *moderate* (**2**), or *severe* (**3**). Series rated **3** (*severe*) are automatically assigned an overall QC score of **0** (*Fail*) and excluded from downstream processing. For all others, final selection is informed by manual ratings, reviewer notes, and automated QC metrics.

<table class="compact-table-no-vertical-lines readme-intro">
<thead>
  <tr>    
  <th>Modality</th>    
  <th>Manual QC Procedures & Scoring</th>
  </tr>
</thead>
<tbody>
<tr>
<td>sMRI</td>
<td>
  <ul>
  <li>Motion artifacts (ripples, blurring), scored 0–3</li>
  <li>Document additional issues (e.g., intensity inhomogeneity, ghosting</li>
  </ul>
</td>
</tr>
<tr>
<td>qMRI</td>
<td>
  <ul>
  <li>Same artifact scoring (0–3)</li>
  <li>Inspect derived data (parametric maps, ROI analysis, quantitative checks for 3D-QALAS)</li>
  </ul>
</td>
</tr>
<tr>
    <td>dMRI, fMRI, fmaps</td>
    <td>
    <ul>
    <li>Score susceptibility artifacts, FOV cutoff, and horizontal line artifacts (present in sagittal view)</li>
    <li>Note susceptibility artifacts, including signal dropout (common in posterior occipital cortex of infant fMRI data acquired in PA phase encoding direction), signal bunching, and warping</li>
    </ul>
    </td>
</tr> 
<tr>
    <td>MRS</td>
    <td><ul><li>Visual inspection and overall QC only of SVS localizer (used to define spectroscopy ROI)</li></ul></td>
</tr>
</tbody>
</table>


## BrainSwipes

<div style="display: flex; align-items: center; gap: 20px;">
<div style="flex: 1;"> <p><a href="https://brainswipes.us/about/">BrainSwipes</a> is a gamified crowdsourcing platform used to perform manual QC of processed MRI data. Reviewers assess images from <a href="../fmri/#xcp-d">XCP-D</a> visual reports, displaying a series of brain images in coronal, axial, and sagittal planes, and classify each report as <strong>Pass (1)</strong> or <strong>Fail (0)</strong>.</p> <p>BrainSwipes results are included in the Tabular Imaging domain:</p>
<ul> 
<li><strong>Report-level QC metrics</strong>: mean QC score and number of reviewers for each visual report</li>
<li><strong>Subject-level QC metrics</strong>: mean QC score and average number of reviewers across all reports for a participant</li> 
</ul> 

</div>
  <div style="flex: 1;">
  <figure>
    <img src="../images/brainswipes.png" alt="BrainSwipes example">
  </figure>
  </div> 
</div> 

<table class="table-no-vertical-lines readme-intro">
<thead>
<tr>
  <th>QC Assessment</th>
  <th>What is Evaluated</th>
</tr>
</thead>
<tbody>
<tr>
  <td><strong>Surface Delineation</strong></td>
  <td>Accuracy of cortical surface placement and gray/white matter boundaries</td>
</tr>
<tr>
  <td><strong>Atlas Registration</strong></td>
  <td>Alignment between the participant's anatomical image and the reference atlas</td>
</tr>
<tr>
  <td><strong>Functional Registration</strong></td>
  <td>Alignment between functional and structural images and detection of major artifacts such as signal dropout</td>
</tr>
</tbody>
</table>

---

## Where to find QC data in release

MR quality control (QC) is performed at multiple stages of data processing. The release includes the following QC metrics, reports, and manual review results, displayed below in roughly chronological order (from raw data QC to group-level analyses provided in the release documentation):

<table class="compact-table-no-vertical-lines readme-intro">
  <thead>
    <tr>
      <th>QC Source</th>
      <th>Stage</th>
      <th>Description</th>
      <th>Release Data</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Raw MR QC</strong></td>
      <td>Raw DICOM</td>
      <td>
        Automated and manual QC metrics, including compliance/completeness checks
      </td>
      <td><code>scans.tsv</code> files</td>
    </tr>
    <tr>
      <td><strong>MRIQC</strong></td>
      <td>Raw BIDS</td>
      <td>Automated image quality metrics</td>
      <td>MRIQC derivatives</td>
    </tr>
    <tr>
      <td><strong>Pipeline QC Reports</strong></td>
      <td>Processing</td>
      <td>Pipeline-generated visual reports and automated metrics</td>
      <td>Derivatives</td>
    </tr>
    <tr>
      <td><strong>BrainSwipes</strong></td>
      <td>Post-processing</td>
      <td>
        Manual review results for structural and functional XCP-D QC reports
      </td>
      <td>Tabular Imaging</td>
    </tr>
    <tr>
      <td><strong>Release QC Summaries</strong></td>
      <td>Group analysis</td>
      <td>
        Group-level analyses/QC summaries provided in documentation, e.g.,
        <a href="../fmri/#quality-control-summary-statistics">fMRI</a> and <a href="../dmri/#quality-control-summary-statistics">dMRI</a> 
        QC Summary Statistics
      </td>
      <td>Release documentation</td>
    </tr>
  </tbody>
</table>

---

<div id="references" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fa-solid fa-book-open"></i>
</span>
<span class="text-with-link">
    <span class="text">References</span>
    <a class="anchor-link" href="#references" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<div class="references">
    <p>Dean III, D. C., Tisdall, M. D., Wisnowski, J. L., Feczko, E., Gagoski, B., Alexander, A. L., ... &amp; HBCD MRI Working Group. (2024). Quantifying brain development in the HEALthy Brain and Child Development (HBCD) Study: The magnetic resonance imaging and spectroscopy protocol. <em>Developmental Cognitive Neuroscience</em>, 70, 101452. <a href="https://doi.org/10.1016/j.dcn.2024.101452">https://doi.org/10.1016/j.dcn.2024.101452</a></p>
    <p>Gard, A. M., Hyde, L. W., Heeringa, S. G., West, B. T., & Mitchell, C. (2023). Why weight? Analytic approaches for large-scale population neuroscience data. Developmental Cognitive Neuroscience, 59, 101196. <a href="https://doi.org/10.1016/j.dcn.2023.101196">https://doi.org/10.1016/j.dcn.2023.101196</a></p>
    <p>Hagler, D. J., Jr, Ahmadi, M. E., Kuperman, J., Holland, D., McDonald, C. R., Halgren, E., &amp; Dale, A. M. (2009). Automated white-matter tractography using a probabilistic diffusion tensor atlas: Application to temporal lobe epilepsy. Human Brain Mapping, 30(5), 1535–1547. <a href="https://doi.org/10.1002/hbm.20619">https://doi.org/10.1002/hbm.20619</a></p>
    <p>Power, J. D., Barnes, K. A., Snyder, A. Z., Schlaggar, B. L., &amp; Petersen, S. E. (2012). Spurious but systematic correlations in functional connectivity MRI networks arise from subject motion. NeuroImage, 59(3), 2142–2154. <a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">https://doi.org/10.1016/j.neuroimage.2011.10.018</a></p>
    <p>Triantafyllou, C., Hoge, R. D., Krueger, G., Wiggins, C. J., Potthast, A., Wiggins, G. C., &amp; Wald, L. L. (2005). Comparison of physiological noise at 1.5 T, 3 T and 7 T and optimization of fMRI acquisition parameters. NeuroImage, 26(1), 243–250. <a href="https://doi.org/10.1016/j.neuroimage.2005.01.007">https://doi.org/10.1016/j.neuroimage.2005.01.007</a></p>
</div>
</div>




<!-- Key results from internal post-processing QC analyses or QC summary reports are provided in the MR README pages under **Quality Control Summary Statistics**, e.g. [Functional MRI](fmri.md#quality-control-summary-statistics) and [Diffusion MRI](dmri.md#quality-control-summary-statistics). Note that many of the processing pipelines provide QC metrics in their derivative outputs, including quantitative metrics, brain visualizations/visual reports, and summary figures. -->


<!-- ## QC Summary Statistics

Key results from internal post-processing QC analyses or QC summary reports are provided in the MR README pages under **Quality Control Summary Statistics**, e.g. [Functional MRI](fmri.md#quality-control-summary-statistics) and [Diffusion MRI](dmri.md#quality-control-summary-statistics). Note that many of the processing pipelines provide QC metrics in their derivative outputs, including quantitative metrics, brain visualizations/visual reports, and summary figures. -->