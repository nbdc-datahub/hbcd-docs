# HBCD MR Quality Control Procedures


## Raw MR Data QC

<div class="warning-banner">
  <span class="emoji"><i class="fa-solid fa-location-dot"></i></span>
  <span class="text">Location in Release Data: 
  Raw data QC metrics (<a href="../tables/scans-tsv.html" target="_blank">see list</a>) are provided in the <a href="../../../datacuration/file-based-data/#participant-session-scan-level-data" target="_blank">scans TSV Files</a>.</span>
</div>
<p></p>

Raw MRI QC combines **automated** and **manual** checks to evaluate unprocessed data and identify acquisition errors, image artifacts, or corrupted files before downstream processing. Automated QC is applied to all data. Due to the large data volume and time-intensive nature of manual inspection, manual visual review is only performed for series that fail automated QC. Although automated tools detect most quality issues, some artifacts may be missed if misclassified or not assessed as part of automated QC.

<!-- ### <i class="fa-solid fa-location-dot header-icon"></i> Location in Release Data

Raw data QC metrics are provided in the session-level <a href="../../../datacuration/file-based-data/#participant-session-scan-level-data" target="_blank">scans TSV Files</a>. QC metrics included in the scans TSV file are summarized <a href="../tables/scans-tsv.html" target="_blank">here</a>. -->

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
<div class="collapsible-content">
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
<td>
    • Estimate head motion with average <span class="tooltip">FD<span class="tooltiptext">framewise displacement</span></span> and data (sec) at FD thresholds of 0.2/0.3/0.4 mm (<a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">Power et al., 2012</a>)<br>
    • Detect line artifacts and FOV cutoff<br>
    • Compute spatial smoothness (FWHM) and temporal SNR (tSNR) after motion correction (<a href="https://doi.org/10.1016/j.neuroimage.2005.01.007">Triantafyllou et al., 2005</a>)
</td>
</tr>
<tr>
    <td>dMRI</td>
    <td>
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
    <td>
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

<div class="warning-banner">
  <span class="emoji"><i class="fa-solid fa-location-dot"></i></span>
  <span class="text">Location in Release Data: 
  BrainSwipes data are provided as <a href="../../#mri">tabulated data</a> (<code>img_brainswipes_xcpd_*</code>).</span>
</div>
<p></p>

<div style="display: flex; align-items: center; gap: 20px;">
<div style="flex: 1;"> <p><a href="https://brainswipes.us/about/">BrainSwipes</a> is a gamified crowdsourcing platform used to perform manual QC of processed MRI data. Reviewers assess images from <a href="../fmri/#xcp-d">XCP-D</a> visual reports, displaying a series of brain images in coronal, axial, and sagittal planes, and classify each report as <strong>Pass (1)</strong> or <strong>Fail (0)</strong>.</p> <p>The released data include:</p>
<ul> 
<li><strong>Report-level QC metrics</strong>: mean QC score and number of reviewers for each visual report</li>
<li><strong>Subject-level QC metrics</strong>: mean QC score and average number of reviewers across all reports for a participant</li> 
</ul> 
<p>BrainSwipes QC results were also used to inform <a href="../#processed-derivatives">processed-data exclusions</a>.</p>
</div>
  <div style="flex: 1;">
  <figure>
    <img src="../images/brainswipes.png" alt="BrainSwipes example">
    <figcaption class="figure-caption">
      Example BrainSwipes assessment of cortical surface delineation. Reviewers swipe right/left to classify images as Pass/Fail after completing a brief QC tutorial.
    </figcaption>
  </figure>
  </div> 
</div> 

<table class="table-no-vertical-lines">
<thead>
<tr>
  <th width="25%">QC Assessment</th>
  <th width="75%">What is Evaluated</th>
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

## QC Summary Statistics

Post-processing QC analyses are performed for certain MR modalities to provide in tandem with release data. These results are included on the modality README pages - see the following **Quality Control Summary Statistics** for: 

- [Functional MRI](fmri.md#quality-control-summary-statistics) - generated from BrainSwipes QC and XCP-D connectivity matrices
- [Diffusion MRI](dmri.md#quality-control-summary-statistics) - summary statistics for automated QC metrics included in QSIPrep pipeline derivatives

Note that many of the processing pipelines provide QC metrics in their derivative outputs, including quantitative metrics, brain visualizations/visual reports, and summary figures.
In some cases these are directly leveraged for data release QC procedures, such as [BrainSwipes](#brainswipes) where the images used for visual QC are sourced directly from the XCP-D HTML reports. In other cases, the QC results are provided as-is to users without additional analysis, e.g. summary reports generated by [Infant fMRIPrep](fmri.md#nibabies-derivs). The [MRIQC](smri.md#mriqc) pipeline is unique in that the outputs are strictly QC metrics, run on raw BIDS data to extract image quality metrics from structural and functional MRI. Review the documentation pages for each modality for details.

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
<div class="table-collapsible-content">
<div class="references">
    <p>Dean III, D. C., Tisdall, M. D., Wisnowski, J. L., Feczko, E., Gagoski, B., Alexander, A. L., ... &amp; HBCD MRI Working Group. (2024). Quantifying brain development in the HEALthy Brain and Child Development (HBCD) Study: The magnetic resonance imaging and spectroscopy protocol. <em>Developmental Cognitive Neuroscience</em>, 70, 101452. <a href="https://doi.org/10.1016/j.dcn.2024.101452">https://doi.org/10.1016/j.dcn.2024.101452</a></p>
    <p>Gard, A. M., Hyde, L. W., Heeringa, S. G., West, B. T., & Mitchell, C. (2023). Why weight? Analytic approaches for large-scale population neuroscience data. Developmental Cognitive Neuroscience, 59, 101196. <a href="https://doi.org/10.1016/j.dcn.2023.101196">https://doi.org/10.1016/j.dcn.2023.101196</a></p>
    <p>Hagler, D. J., Jr, Ahmadi, M. E., Kuperman, J., Holland, D., McDonald, C. R., Halgren, E., &amp; Dale, A. M. (2009). Automated white-matter tractography using a probabilistic diffusion tensor atlas: Application to temporal lobe epilepsy. Human Brain Mapping, 30(5), 1535–1547. <a href="https://doi.org/10.1002/hbm.20619">https://doi.org/10.1002/hbm.20619</a></p>
    <p>Power, J. D., Barnes, K. A., Snyder, A. Z., Schlaggar, B. L., &amp; Petersen, S. E. (2012). Spurious but systematic correlations in functional connectivity MRI networks arise from subject motion. NeuroImage, 59(3), 2142–2154. <a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">https://doi.org/10.1016/j.neuroimage.2011.10.018</a></p>
    <p>Triantafyllou, C., Hoge, R. D., Krueger, G., Wiggins, C. J., Potthast, A., Wiggins, G. C., &amp; Wald, L. L. (2005). Comparison of physiological noise at 1.5 T, 3 T and 7 T and optimization of fMRI acquisition parameters. NeuroImage, 26(1), 243–250. <a href="https://doi.org/10.1016/j.neuroimage.2005.01.007">https://doi.org/10.1016/j.neuroimage.2005.01.007</a></p>
</div>
</div>