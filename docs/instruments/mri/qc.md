# HBCD MR Quality Control Procedures

## Raw MR Data QC

Raw MRI QC combines **automated** and **manual** checks to evaluate unprocessed data and identify acquisition errors, image artifacts, or corrupted files before downstream processing. Automated QC is applied to all data. Due to the large data volume and time-intensive nature of manual inspection, manual visual review is only performed for series that fail automated QC. Although automated tools detect most quality issues, some artifacts may be missed if misclassified or not assessed as part of automated QC. Raw MR QC metrics are provided in the raw BIDS `scans.tsv` files in the release ([see details](../../datacuration/file-based-data.md#participant-session-scan-level-data)).

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
</div>

### Automated QC

Data that pass [protocol adherence and completeness checks](#compliance) move to the next stage of automated QC. Automated QC metrics are calculated for modalities as follows:

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