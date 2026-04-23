# HBCD MR Quality Control Procedures

<!-- SUMMARY TABLE
 MR data undergoes both **raw** and **processed** data quality control assessments, as summarized below.
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<thead>
<tr>
    <th>QC Type</th>
    <th>Specific Data Performed On</th>
    <th>Location of Output QC Metrics in Data Release</th>
</tr>
</thead>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Raw MR Data QC, including automated and manual</td>
    <td style="word-wrap: break-word; white-space: normal;">Raw DICOMs, after protocol compliance & completeness checks (<a href="../../qc/#compliance">see details</a>) and prior to BIDS conversion</td>
    <td style="word-wrap: break-word; white-space: normal;">Session-level Scans TSV files - <a href="../../qc/#scanstsv">see details</a> - includes both automated and manual QC metrics</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Raw BIDS QC via MRIQC Pipeline</td>
    <td style="word-wrap: break-word; white-space: normal;">MRIQC generates image quality metrics (IQM) for raw anatomical and functional data (only outputs for the scans selected for full structural and functional processing are included in the release)</td>
    <td style="word-wrap: break-word; white-space: normal;">MRIQC Pipeline Derivatives - <a href="../../qc/#scanstsv">see details</a>. NOTE that the MRIQC outputs are not used to inform HBCD processing workflows, but are instead simple made available in the release for users convenience.</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Processed Data: Pipeline-Specific Reports</td>
    <td style="word-wrap: break-word; white-space: normal;">Several pipelines generate visual reports and automated metrics for users to assess the quality of processed outputs (ADD MORE INFO)</td>
    <td style="word-wrap: break-word; white-space: normal;">Available in pipeline derivatives (ADD MORE INFO)</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Processed Data: BrainSwipes</td>
    <td style="word-wrap: break-word; white-space: normal;">Structural and functional visual reports derived from XCP-D derivative outputs - <a href="../../brainswipes/">see details</a></td>
    <td style="word-wrap: break-word; white-space: normal;">Available as tabulated derivatives, with most up-to-date results provided between releases in the HBCD Private Release Notes - <a href="../../brainswipes/#location-of-brainswipes-qc-results">see details</a></td>
</tr>
</tbody>
</table> -->

## Raw MR Data QC

Raw MRI QC combines **automated** and **manual** checks to evaluate unprocessed data and identify acquisition errors, image artifacts, or corrupted files before downstream processing. Automated QC is applied to all data. Due to the large data volume and time-intensive nature of manual inspection, manual visual review is only performed for series that fail automated QC. Although automated tools detect most quality issues, some artifacts may be missed if misclassified or not assessed as part of automated QC.

### <i class="fa-solid fa-location-dot header-icon"></i> Location in Release Data

Raw data QC metrics are provided in the session-level <a href="../../../datacuration/file-based-data/#participant-session-scan-level-data" target="_blank">scans TSV Files</a>. QC metrics included in the scans TSV file are summarized <a href="../tables/scans-tsv.html" target="_blank">here</a>.

### <i class="fa fa-desktop header-icon"></i> Automated QC

Automated QC begins immediately after data upload with protocol compliance and completeness checks ([expand infobox for details](#compliance)). Data that fail are flagged for review and excluded from release until resolved. For compliant data, automated QC metrics are then calculated (see table below).

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
<p><strong>Protocol compliance</strong> is performed by extracting imaging parameters from DICOM headers to confirm that key parameters (e.g., voxel size, TR, orientation) match the expected protocol for each scanner. Out-of-compliance series are flagged for review and sites are contacted if corrective action is needed.</p>
<p><strong>Completeness checks</strong> verify that all expected series are present in each imaging session. Missing data usually indicate an aborted scan or incomplete data transfer. Series included in a valid session include: <strong>T1w &amp; T2w</strong> structural scans; <strong>2 resting state functional runs</strong> (each accompanied by fieldmaps acquired in AP and PA phase encoding directions); <strong>diffusion scans (acquired both AP and PA)</strong>; quantitative <strong>QALAS and B1 maps</strong>; and an <strong>MRS scan and SVS localizer</strong>. </p>
</div>

<div id="auto-qc" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
<span class="text">Automated QC Metrics</span>
  <a class="anchor-link" href="#auto-qc" title="Copy link">
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
    <th>Automated QC Metrics</th>
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

### <i class="fa-solid fa-eye header-icon"></i> Manual Review

Data are flagged for manual review based on automated QC results using multivariate prediction and Bayesian classifiers, so only a subset undergoes both automated and manual review. When a series is flagged, trained technicians perform visual review and rate artifact severity on a **0–3 scale**: *none* (**0**), *mild* (**1**), *moderate* (**2**), or *severe* (**3**). Series rated **3** (*severe*) are automatically assigned an overall QC score of **0** (*Fail*) and excluded from downstream processing. For all others, final selection is informed by manual ratings, reviewer notes, and automated QC metrics.

<div id="man-qc" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
<span class="text">Manual QC Metrics</span>
  <a class="anchor-link" href="#man-qc" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead><tr>    <th>Modality</th>    <th>Manual QC Procedures & Scoring</th></tr></thead>
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
</div>

## BrainSwipes

<!-- PATCH: REMOVE FOLLOWIGN DATA WARNING-->
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
<p>The following groups are missing all or a large portion of BrainSwipes QC results in the release data:
<ul>
<li>V02 sessions processed with T1-based surface reconstruction (<a href="../mri-proc/#m-crib-s-freesurfer" target="_blank">Infant FreeSurfer method</a>) within Infant fMRIPrep: ~70% of the visual reports across sessions are missing BrainSwipes QC scores. <i>Note, however, that for separate reasons we advise against using this data for analyses - see <a href="../mri-proc/#warning" target="_blank">Data Warning</a></i>.</li>
<li>V02 sessions with only a T2w anatomical image present (that passes raw data QC), and no T1w: missing ALL BrainSwipes QC results in the release data.</li>
</ul>
<p><b>Completed tabulated data can be found in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a> accessible to DUC-authorized users.</b></p>  
<p><a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/brainswipes_2026-01-26.zip"><i class="fa-solid fa-download"></i> &nbsp; Download Completed BrainSwipes Results</a></p>
</div>
<p></p>



<div style="display: flex; align-items: center; gap: 30px;">
<div style="flex: 1;">
<!-- <p>Processed structural and functional MRI data are quality-controlled via manual review of <a href="../mri-proc/#xcp-d">XCP-D</a> visual reports. Manual inspection remains the gold standard for QC, but is highly resource-intensive.</p> -->
<p>QC is performed on processed structural and functional MRI data via manual review of <a href="../mri-proc/#xcp-d">XCP-D</a> visual reports. Though manual inspection remains the gold standard for QC, it is highly resource-intensive. Manual visual review was therefore performed using <a href="https://brainswipes.us/about/">BrainSwipes</a>, a gamified crowdsourcing platform where users classify images as Pass or Fail by swiping right or left after completing a brief visual QC tutorial.</p>
<p>BrainSwipes QC results were also used to inform processed data exclusion (see <a href="../exclusion-criteria/#processed-data-exclusion-criteria" target="_blank">Processed Data Exclusion Criteria</a> for details).</p>
</div>
  <div style="flex: 1; text-align: center;">
    <img src="../images/brainswipes.png" style="max-width:100%; height:auto; display:block; margin:0 auto;">
    <p style="font-size: 0.8em; margin-top: 5px; line-height: 1.1; max-width:80%; margin-left:auto; margin-right:auto; text-align:justify;">
      <i>Example quality assessment of surface delineation on BrainSwipes platform (displaying brain in axial plane at level of basal ganglia/putamen).</i>
    </p>
  </div>
</div>

<div id="swipes-procedures" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-brain"></i></span>
<span class="text-with-link">
  <span class="text">Detailed BrainSwipes QC Procedures</span>
    <a class="anchor-link" href="#swipes-procedures" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><b>Surface Delineation</b><br>
For structural QA, swipers are presented with image slices in coronal, axial, and sagittal planes to assess the accuracy of T1w and T2w surface delineations in differentiating gray and white matter. Images are derived from XCP-D visual reports.</p>
<p><b>Atlas Registration</b><br>
In addition to surface delineation, structural QA also includes atlas registration quality, evaluated by overlaying delineations of the subject’s image onto the atlas, and vice versa. Swipes display nine T1w slices for visual inspection, with three slices per anatomical plane. Quality is assessed based on the alignment of the outer boundaries of the overlaid contours with those of the underlying image, ensuring minimal gaps or misalignments. Images are derived from XCP-D visual reports.</p>
<p><b>Functional Registration</b><br>
Functional registration is evaluated by overlaying outlines of functional images onto structural images and vice versa. Swipes display nine slices of the same functional image for visual inspection, with three slices per anatomical plane. Quality is assessed similarly to structural atlas registration, focusing on the alignment of the overlaid contours. Additional evaluation includes checking for artifacts such as signal dropout. Images are derived from XCP-D visual reports.</p>
</div>

### <i class="fa-solid fa-location-dot header-icon"></i> Location in Release Data
BrainSwipes QC results for processed data are provided as <a href="../../#mri-tab">tabulated data</a> (`img_brainswipes_xcpd_*`). BrainSwipes presents users with a series of visual reports, generated by XCP-D, to assess the quality of structural and functional processing. Each report is independently rated as **Pass (1)** or **Fail (0)**. The BrainSwipes data include:

 - The mean QC score and number of reviewers **for each individual visual report**
 - The mean QC score and average number of reviewers **across all visual reports** 

---

<div id="ref" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-book-open"></i></span>
  <span class="text-with-link">
  <span class="text">References</span>
  <a class="anchor-link" href="#ref" title="Copy link">
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