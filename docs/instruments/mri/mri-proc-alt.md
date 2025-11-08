
# Original/more detailed Nibabies & XCP-D proc descriptions

## Nibabies processing
<p>Infant fMRIPrep adapts the fMRIPrep pipeline for infant MRI data, incorporating age-appropriate templates and processing steps optimized for developing brains.</p>
<p><b>B0 Inhomogeneity Correction</b><br>
Fieldmap estimation is performed using paired EPI images to correct for B0 inhomogeneity. The resulting fieldmap is applied to all BOLD runs for distortion correction.</p>
<p><b>Anatomical Preprocessing</b><br>
T1w and/or T2w images are denoised and corrected for intensity inhomogeneity. Surface reconstruction is performed via <b>M-CRIB-S</b> and <b>Infant FreeSurfer</b>.<br>
<b>M-CRIB-S</b>: a modified <code>MCRIBReconAll</code> workflow that uses the T2w reference image and the pre-computed anatomical segmentation from BIBSNet.<br>
<b>Infant FreeSurfer</b>: runs <code>infant_recon_all</code> using the T1w reference image.<br>
For both, images are normalized first to an age-specific MNI Infant template (0-4.5yr), then to the standard MNI152 space via nonlinear registration for compatibility with adult analyses.</p>
<p><b>Functional Preprocessing</b><br>
For each BOLD run, Infant fMRIPrep performs the following steps:</p>
<ul>
<li><strong>Motion correction</strong>: A reference volume is generated, and head motion parameters are estimated prior to filtering.</li>
<li><strong>Distortion correction</strong>: The estimated fieldmap is aligned to the EPI reference and applied to correct distortions.</li>
<li><strong>Coregistration</strong>: The functional reference is aligned to the T2w anatomical image using boundary-based registration for accurate mapping between spaces.</li>
</ul>
<p><b>Confound Estimation</b><br>
Several confound time series are calculated for each run for quality assessment and later noise modeling:</p>
<ul>
<li>Motion metrics: Framewise displacement (FD) and DVARS</li>
<li>Global signals: Mean signal from CSF, white matter, and whole brain</li>
<li>CompCor components: Physiological noise regressors from aCompCor and tCompCor methods</li>
<li>Derived regressors: Temporal derivatives, quadratic terms, and motion outlier flags (for frames exceeding 0.5 mm FD or 1.5 standardized DVARS thresholds)</li>
</ul>
<p><b>Surface and Grayordinate Outputs</b><br>
BOLD data are resampled to both subject-specific (native) and symmetric (fsLR) surface spaces.
A “goodvoxels” mask is applied during volume-to-surface sampling in fsLR space to exclude unstable regions (voxels whose time-series with a locally high coefficient of variation before surface sampling) before surface projection.
Finally, grayordinates files (91k) are generated using the highest-resolution <code>fsaverage</code> as intermediate standardized surface space for use in surface-based analyses compatible with tools such as the Human Connectome Workbench.</p>
</div>

## XCP-D processing

<p><strong>XCP-D</strong> is used to post-process the outputs of Infant-fMRIPrep, generating cleaned, denoised, and parcellated datasets ready for analysis. The workflow utilizes a set of standard atlases for parcellation - see <a href="../mri/#parc">Parcellations</a> under <em>MRI Derivatives: Quickstart Guide</em>.</p>
<p><b>ANATOMICAL PROCESSING</b><br>
Native-space T2w images are transformed into standard <strong>MNI152NLin6Asym</strong> space at 1 mm³ resolution.
<strong>fsLR-space</strong> morphometric surfaces are copied from the preprocessing derivatives provided by Infant-fMRIPrep to the XCP-D derivatives.
HCP-style midthickness, inflated, and very-inflated surfaces are generated from the white-matter and pial surface meshes and mapped to fsLR space. These surfaces and associated metrics are included in the XCP-D derivatives for downstream analysis.</p>
<p><b>FUNCTIONAL PROCESSING</b><br>
For each BOLD run, XCP-D performs a series of cleanup and quality-control steps.</p>
<ul>
<b>Preprocessing and Denoising</b>
<li>The first four volumes (dummy scans) are removed.</li>
<li><strong>Motion correction:</strong> Framewise displacement (FD) is calculated per Power et al. (2014); volumes with FD &gt; 0.3 mm are flagged as high-motion outliers.</li>
<li><strong>Nuisance regression:</strong> 36 confound regressors (motion, tissue, and global signals plus derivatives) are regressed out following the 36P strategy.</li>
<li><strong>Despiking and filtering:</strong> Data are despiked, temporally filtered (0.01–0.08 Hz), and smoothed (6 mm FWHM) to retain low-frequency neural signals while reducing noise.</li>
<li><strong>Censoring:</strong> High-motion volumes are interpolated and later censored to minimize motion artifacts.</li>
</ul>
<ul>
<b>Functional Metrics computed from the cleaned time series</b>
<li><strong>ALFF (Amplitude of Low-Frequency Fluctuations):</strong> Quantifies spontaneous low-frequency signal amplitude across voxels.</li>
<li><strong>ReHo (Regional Homogeneity):</strong> Measures local synchronization of neural activity within surface and subcortical regions.</li>
</ul>
<p><b>Connectivity Analysis</b><br>
Parcellated time series are extracted for each atlas, described <a href="../mri/index.md#parc">here</a>, and pairwise functional connectivity is calculated as the Pearson correlation between regional time series. For participants with multiple runs, postprocessed derivatives are concatenated across runs and directions.</p>


