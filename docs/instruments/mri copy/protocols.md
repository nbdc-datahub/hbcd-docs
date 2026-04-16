# HBCD Study MRI Protocols
<!-- <meta http-equiv="refresh" content="0; url=https://hbcdsequences.readthedocs.io"> -->

On this page we provide a high-level summary of HBCD Study MRI protocols and acquisition parameters as described in <a href="https://doi.org/10.1016/j.dcn.2024.101452">Dean et al. 2024</a>. **See the external [HBCD Study MRI Protocols](https://hbcdsequences.readthedocs.io) documentation for full protocols, sequence installation, and operation instructions.**

## Structural MRI (sMRI)


<div id="smri" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-brain"></i></span>
  <span class="text-with-link">
    <span class="text">Acquisition Details</span>
    <a class="anchor-link" href="#smri" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Key features of the HBCD T1w and T2w structural imaging protocols include:</p>
<ul>
<li>0.8 mm isotropic resolution</li>
<li>Compressed SENSE reconstruction enabling high acceleration and shorter acquisition times (&lt;9 minutes total for T1w and T2w; see vendor-specific pages for details)</li>
<li>Embedded navigators for motion tracking during structural imaging (<a href="https://doi.org/10.1002/mrm.22176">White et al., 2010</a>, <a href="https://doi.org/10.1016/j.neuroimage.2015.11.054">Tisdall et al., 2016</a>, <a href="https://doi.org/10.1371/journal.pone.0217145">Andersen et al., 2019</a>). </li>
<li>Harmonization approach similar to the <a href="https://nbdc-splash-beta.lassoinformatics.com/abcd-study">ABCD Study</a>:<ul>
<li>T1w: contrast-relevant parameters matched as closely as possible across vendors</li>
<li>T2w: vendor-specific parameters selected to achieve comparable contrast and SNR, accounting for differences in 3D T2w pulse sequence implementation</li>
</ul>
</li>
</ul>
</div>

HBCD protocols for structural MRI were informed by recent large-scale developmental neuroimaging studies including [ABCD](https://abcdstudy.org/), HCP Lifespan, and BCP ([Howell et al., 2019](https://pubmed.ncbi.nlm.nih.gov/29578031/)). These studies laid critical foundation for the development of well-validated, high-resolution protocols harmonized across all three major scanner vendors ([Casey et al., 2018](https://doi.org/10.1016/j.dcn.2018.03.001)). In addition, the findings emphasized the importance of T2w acquisition in infants due to suboptimal grey/white T1w contrast resulting from incomplete myelination ([Howell et al., 2019](https://doi.org/10.1016/j.neuroimage.2018.03.049), [Myers et al., 2023](https://doi.org/10.1016/j.neuroimage.2018.03.049)).

## Quantitative MRI (qMRI)

<div id="qmri-warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</i></span>
  <a class="anchor-link" href="#qmri-warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Note that different sites may apply varying criteria for identifying motion-degraded QALAS and B1+ mapping scans. For 3D-QALAS, the SyMRI toolbox does <strong>not</strong> incorporate externally acquired B1+ field maps when estimating quantitative T1, T2, and proton density (PD) values.</p>
<p>Additionally, estimated quantitative T1 values show variability across MRI vendors and participant age. Current estimates do not align well with values reported in the literature, likely due to assumptions made in the modeling procedures. Work is ongoing to address these issues. As a result, quantitative T1 values (and by extension, PD values) will not be included initial release data.</p> 
</div>

<div id="qmri" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-brain"></i></span>
  <span class="text-with-link">
    <span class="text">Acquisition Details</span>
    <a class="anchor-link" href="#qmri" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><b>QALAS</b><br>
QALAS is a multi-contrast MRI sequence that produces five brain volumes using turbo-flash readouts with varying T1 and T2 weightings (acquisition time ~5 min for Siemens and ~4 min for GE/Philips). These volumes are combined to estimate T1, T2, and proton density (PD) maps. The sequence starts with a T2-preparation pulse, which adds T2 weighting to the first volume. An inversion pulse follows, imparting T1 weighting to the next four volumes.</p>
<p style="margin-bottom: 0;"><b>QALAS Pulse Sequence Diagram</b> (<i><a href="https://onlinelibrary.wiley.com/doi/10.1002/mrm.29939">Fujita et al., 2024</a> Figure. 1</i>)</p>
<img src="../images/qalas_Fig1.png" style="max-width:90%; height:auto;">
<br>
<p><b>B1+ Fieldmap</b><br>
The HBCD protocol includes a short B1+ field map acquisition (~30–45 seconds across all scanner types) to calibrate flip angle measurements, which can vary spatially due to B1+ field inhomogeneity. This calibration is required for accurate T1, T2, and PD estimation. Because the transmit B1+ field varies smoothly across space, coarse spatial resolution is sufficient, enabling rapid acquisition. Vendor-specific implementations in the HBCD protocol include Actual Flip Angle Imaging (AFI) (<a href="https://doi.org/10.1002/mrm.21120">Yarnykh 2007</a>) for GE and Philips, and a pre-saturation turbo-FLASH readout for Siemens.</p>
</div>

Conventional neuroimaging relies on qualitative relaxation-weighted images (e.g., T1w, T2w), which reflect relative differences in tissue properties, but are strongly influenced by sequence parameters, participant positioning, and scanner hardware. These dependencies limit biological interpretability and hinder comparisons across participants, sessions, and sites. The challenge is especially pronounced in pediatric imaging, where rapid age-related changes in free water distribution, iron, and myelination dynamically alter image contrast.

**Quantitative MRI (qMRI)** addresses these limitations by directly measuring relaxation properties, providing more reliable markers of brain tissue microstructure ([Deoni 2010](https://doi.org/10.1097/RMR.0b013e31821e56d8); [Does 2018](https://doi.org/10.1016/j.neuroimage.2017.12.087)). The HBCD Study acquires 3D-QALAS, a time-efficient 3D sequence that combines interleaved Look-Locker acquisition with a T2-preparation pulse ([Kvernby et al. 2014](https://doi.org/10.1186/s12968-014-0102-0)). This approach enables simultaneous estimation of T1/T2 relaxation times and proton density (PD) maps from a single scan and has been validated across major MRI vendors ([Fujita et al. 2019](https://doi.org/10.1016/j.mri.2019.08.031)).

<!-- derivs: 
- Relaxation (T1/T2) & Proton Density (PD) Maps 
- Synthetic T1w/T2w Images -->

<div id="qmri-derivs" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">qMRI Processing & Derivatives (SyMRI/qMRI PostProc Pipelines)</span>
  <a class="anchor-link" href="#qmri-derivs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Quantitative MRI data was processed through the Synthetic MRI (<a href="https://syntheticmr.com/products/symri-neuro/">SyMRI</a>) toolbox and <a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html">qMRI PostProc</a>. SyMRI is proprietary software for quantitative MRI that generates synthetic T1w/T2w images and derived relaxometry maps from 3D-QALAS brain images. Synthetic T1w/T2w volumes are created by substituting quantitative estimates of T1 and T2 relaxation times back into the MR signal equation (Bloch equations) for each sequence. This enables flexible generation of different contrasts without acquiring separate scans. These outputs are then minimally preprocessed by qMRI PostProc.</p>
<p><a href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>
<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ symri/  <span class="hashtag"># SyMRI Derivatives</span>
    |   |__ sub-<span class="label">{ID}</span>/
    |       |__ ses-<span class="label">{V0X}</span>/
    |           |__ anat/
    |               |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-QALAS_T1w.nii.gz <span class="hashtag">(+JSON)</span>
    |               |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-QALAS_T2map.nii.gz <span class="hashtag">(+JSON)</span>
    |               |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-QALAS_T2w.nii.gz <span class="hashtag">(+JSON)</span>
    |               |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-QALAS_desc-SymriContainer.log
    | 
    |__ qmri_postproc/ <span class="hashtag"># qMRI Post-Proc Derivatives</span>
        |__ sub-<span class="label">{ID}</span>/
            |__ ses-<span class="label">{V0X}</span>/
                |__ anat/  
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-AsegROIs_scalarstats.tsv <span class="hashtag">(+JSON)</span>
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-BilateralAsegROIs_scalarstats.tsv <span class="hashtag">(+JSON)</span>
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-RegistrationQCAid.png <span class="hashtag">(+JSON)</span>
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-QALAS_desc-aseg_dseg.nii.gz
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-T2w_desc-QALAS_T2map.nii.gz <span class="hashtag">(+JSON)</span>
</pre>
</div>



## Functional MRI (fMRI)

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
<p>Head motion is a serious issue in neuroimaging, especially for resting state fMRI, as it creates brain-wide artifactual effects such as inflated short-distance connectivity and attenuated long-distance connectivity (<a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">Power et al. 2012</a>). Researchers employ a variety of strategies to mitigate head motion during acquisition and processing (<a href="https://doi.org/10.1016/j.neuroimage.2013.08.048">Power et al. 2014</a>; <a href="https://doi.org/10.1016/j.neuroimage.2014.10.044">2015</a>; <a href="https://doi.org/10.1016/j.neuroimage.2012.08.052">Satterthwaite et al. 2013</a>; <a href="https://doi.org/10.1093/cercor/bhw253">Siegel et al. 2017</a>; <a href="https://doi.org/10.1016/j.neuroimage.2020.116866">Gratton et al. 2020</a>). This includes motion censoring (discarding individual frames that are proximal to motion events within a run) and/or excluding entire runs due to high motion. These strategies may lead to the exclusion of some participants from further analysis due to lack of sufficient data.</p>
<p>Levels of head motion differ according to demographic factors such as sex, race/ethnicity, and SES (<a href="https://doi.org/10.1007/s11682-022-00665-2">Cosgrove et al., 2022</a>). Therefore, mitigation strategies for head motion introduce questions around fairness and differential exclusions across demographic groups. In addition, motion censoring causes sessions to vary by the amount of data remaining. Such variability may continue to inflate findings especially in the presence of conditions that may correlate with the motion artifact like autism or ADHD (<a href="https://doi.org/10.1093/cercor/bhw403">Eggebrecht, 2017</a>). The amount of data remaining influences the variation in the connectivity calculations by affecting the degrees of freedom. Therefore, even after motion censoring, issues concerning fairness may persist when examining factors that might be affected by motion like sex, race/ethnicity, SES, and BMI (<a href="https://doi.org/10.1007/s11682-022-00665-2">Cosgrove et al., 2022</a>). One strategy that avoids this confound is to strictly control the degrees of freedom, where functional connectivity measures are calculated with the exact same amount of data. Researchers should assess whether control of artifactual effects of head motion effects can be achieved by alternative means that mitigate this impact. Examples of such strategies could include data augmentation approaches such as sampling from other datasets, data processing strategies like the include use of ICA-based denoising (<a href="https://doi.org/10.1016/j.neuroimage.2015.02.064">Pruim et al., 2015a</a>; <a href="https://doi.org/10.1016/j.neuroimage.2015.02.063">2015b</a>), use of bootstrap aggregation (<a href="https://doi.org/10.1101/2024.06.22.600221">Ramduny et al., 2024</a>), or the creation of “pseudo-rest” by removing task signals from the task data (<a href="https://doi.org/10.1016/j.neuroimage.2006.11.051">Fair et al. 2007</a>), or post-hoc approaches like propensity weighting.</p> 
<p>Researchers interested in examining brain-behavior associations or multivariate predictions should follow strategies such as those in <a href="https://doi.org/10.1093/cercor/bhw403">Eggebrecht 2017</a> to: 1) assess how missing data impacts dependent, independent variables and covariates, 2) examine the association between the degrees of freedom and non-FC variables, 3) use trimmed FC measures when needed to mitigate artifacts due to data quality.</p>
</div>

<div id="fmri-warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</span>
  <a class="anchor-link" href="#fmri-warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p><b>Overview & Prevalence</b><br>
A subset of Philips fMRI scans is affected by a <b>signal intensity clipping artifact</b>. Due to a scaling error during real-time reconstruction, raw pixel intensities &gt;4095 are capped, producing hyperintense regions that can obscure gray/white matter signal. This artifact can significantly distort BOLD registration and subsequent derived measures such as functional connectivity estimates.
This issue was identified during pilot data collection and patched at most sites prior to the main study. However, there are residual cases at the sites VAN and CCH, where the patch was implemented later (Oct 2024). Overall, ~20% of scans from VAN and CCH show some degree of clipping and ~6% are classified as severe enough to fail manual visual raw data QC.</p>
<p><b>How to Identify Affected Scans</b><br>
Clipping severity can be estimated from QC metrics available in the <a href="../../../datacuration/file-based-data/#participant-session-scan-level-data"><code>scans.tsv</code> file</a>, including (1) the ratio of median to maximum image intensity and (2) the fraction of voxels at maximum intensity within the brain mask:</p> 
<table class="table-no-vertical-lines">
<tr><th>Clipping Severity</th>
<th>Criteria</th></tr> <tr>
<td><b>Severe</b></td> <td>(<code>brain_median</code>/<code>brain_max</code>) &gt; 0.8 <b>AND</b> <code>brain_fvox_max</code> &gt; 0.001</td> </tr>
<tr><td><b>Potential</b></td> <td>(<code>brain_median</code>/<code>brain_max</code>) &gt; 0.5 <b>AND</b> <code>brain_fvox_max</code> &gt; 0.001</td> </tr> 
</table>
<p><b>Recommended Usage</b><br>
Updates to real-time reconstruction are in development to recover affected data. In the meantime, users should practice caution when performing sensitive analyses and consider including clipping metrics as covariates in analysis. Note that scans with severe clipping fail raw data QC, so are automatically excluded from downstream pipeline processing.</p>
</div>

<div id="fmri-acq" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-brain"></i></span>
  <span class="text-with-link">
    <span class="text">Acquisition Details</span>
    <a class="anchor-link" href="#fmri-acq" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<br>
<ul>
<li>Resting-state (rs-fMRI) data is acquired at 2 mm isotropic resolution with a repetition time (TR) of 1725 ms and multiband (MB) factor of 4</li>
 <li>A minimum of 2 runs are collected (during sleep for infants &lt;30 months old), each lasting 7.5 minutes</li>
<li><a href="https://firmm.readthedocs.io/" target="_blank"><b>FIRMM</b></a> is used to monitor head motion in real time, quantified by framewise displacement (FD)</li>
<li>Additional runs are acquired as needed to obtain at least <b>7.5 minutes of low-motion data</b> (FD &lt; 0.3 mm)</li>
<li>Each run includes forward and reverse phase-encoding spin-echo EPI images for distortion correction</li>
</ul>
</div>
<p></p>

fMRI measures functional brain activity using the blood oxygen level–dependent (BOLD) signal (see [Acquisition Details](#fmri-acq)). In the HBCD Study, at least **7.5 minutes of low-motion** resting-state fMRI (rs-fMRI) data (FD < 0.3 mm) are acquired per session across runs. Head motion is monitored in real time using [FIRMM](https://firmm.readthedocs.io/), which estimates the amount of usable low-motion data during acquisition (<a href="https://doi.org/10.1016/j.neuroimage.2017.08.025">Dosenbach et al., 2017</a>).

<div id="fconn" class="static-banner" style="border-left: 5px solid #199bd6;">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
    <span class="text">QC Report: Impact of Data Quality on Functional Connectivity</span>
    <a class="anchor-link" href="#fconn" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
</div>
<div class="table-static-content">
<p>Average functional connectivity matrices were computed using the Gordon-parcellated time series available in the V02 XCP-D derivatives. Data were included based on varying thresholds of <a href="../qc/#brainswipes">BrainSwipes</a> QC scores. Functional connectivity patterns were not substantially altered with the inclusion of lower-quality data, indicating robustness to mild quality variation.</p>
<p><strong>Connectivity matrices as data quality improves (left -> right) based on QC thresholds of 0.1, 0.5, and 0.9:</strong></p>
<img src="../images/fconn_qc.png" style="width: 90%;" class="center">
<br>
</div>
<p></p>







## Diffusion MRI
The DWI protocol provides diffusion-weighted images that may be used to estimate multiple models of diffusion behavior in the central nervous system. The protocol acquires roughly 140 diffusion-weighted echo planar images at four b-values (diffusion-weighting) between 0 and 3000 s/mm<sup>2</sup> (12-13 minutes total acquisition time). For raw image acquisition, a minimum of 60% of the diffusion-weighted volumes are required to be collected for the acquisition to be deemed successful.

## Magnetic Resonance Spectroscopy (MRS)
The MRS acquisition protocol was optimized to maximize signal-to-noise across multiple low-concentration metabolites while maintaining an acquisition time (TA) under 9 minutes. The MRS acquisition centers on a single voxel Point-RESolved Spectroscopy (PRESS) ([Bottomley, 1987](https://doi.org/10.1111/j.1749-6632.1987.tb32915.x)) localization (30×23×23 mm^3) in the bilateral thalamus, with SVS localizer acquisitions to define the ROI. The ISTHMUS sequence incorporates a short TE (35 ms) unedited block at the beginning of the sequence for optimal measurement of high concentration metabolites, including N-acetylasparte, followed by an advanced Hadamard encoded spectral editing scheme (HERCULES, TE = 80 ms) to derive reliable and reproducible measures of the low-concentration metabolites ([Oeltzschner et al., 2019](https://doi.org/10.1016/j.neuroimage.2018.10.002)).