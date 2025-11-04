# Structural & Functional MRI Processing

Structural and functional MRI data is processed via a sequence of BIDS App pipelines, so we describe the sequence here.

**BIBSNet**: generates brain segmentations and brain masks

**Infant fMRIPrep**: Brain segmentations and masks are fed into Infant fMRIPrep, which produces minimal structural and functional MRI processing including visual quality assessment reports, preprocessed derivatives, and confounds to be used for denoising in subsequent processing procedures.

**XCP-D**: Infant fMRIPrep outputs are fed into XCP-D, which performs functional MRI post-processing and noise regression.

## Infant fMRIPrep
Infant fMRIPrep adapts the fMRIPrep pipeline for infant MRI data, incorporating age-appropriate templates and processing steps optimized for developing brains.

### B0 Inhomogeneity Correction
Fieldmap estimation is performed using paired EPI images to correct for B0 inhomogeneity. The resulting fieldmap is applied to all BOLD runs for distortion correction.

### Anatomical Preprocessing
T1w and/or T2w images are denoised and corrected for intensity inhomogeneity.
A pre-computed brain mask is provided as input and used throughout all anatomical and functional processing.

Surface reconstruction is performed via 2 methods:

#### (1) M-CRIB-S
The modified `MCRIBReconAll` workflow uses the T2w reference image and a pre-computed anatomical segmentation from BIBSNet.
Images are normalized first to an age-specific MNI Infant template (0-4.5yr), then to the standard MNI152 space via nonlinear registration for compatibility with adult analyses.

#### (2) Infant FreeSurfer
ADD TEXT - Surface reconstruction using the Infant FreeSurfer pipeline ???????

### Functional Data Preprocessing
For each BOLD run, Infant fMRIPrep performs the following steps:

 - **Motion correction**: A reference volume is generated, and head motion parameters are estimated prior to filtering.
 - **Distortion correction**: The estimated fieldmap is aligned to the EPI reference and applied to correct distortions.
 - **Coregistration**: The functional reference is aligned to the T2w anatomical image using boundary-based registration for accurate mapping between spaces.

#### Confound Estimation
Several confound time series are calculated for each run for quality assessment and later noise modeling:

 - Motion metrics: Framewise displacement (FD) and DVARS
 - Global signals: Mean signal from CSF, white matter, and whole brain
 - CompCor components: Physiological noise regressors from aCompCor and tCompCor methods
 - Derived regressors: Temporal derivatives, quadratic terms, and motion outlier flags (for frames exceeding 0.5 mm FD or 1.5 standardized DVARS thresholds)

#### Surface and Grayordinate Outputs
BOLD data are resampled to both subject-specific (native) and symmetric (fsLR) surface spaces.
A “goodvoxels” mask is applied during volume-to-surface sampling in fsLR space to exclude unstable regions (voxels whose time-series with a locally high coefficient of variation before surface sampling) before surface projection.
Finally, grayordinates files (91k) are generated using the highest-resolution `fsaverage` as intermediate standardized surface space for use in surface-based analyses compatible with tools such as the Human Connectome Workbench.

## XCP-D
**XCP-D** is used to post-process the outputs of Infant-fMRIPrep, generating cleaned, denoised, and parcellated datasets ready for analysis.

**Both anatomical and functional data are parcellated using a set of standard atlases - see[Parcellations](../mri/index.md#parc) under *MRI Derivatives: Quickstart Guide*.**

### Anatomical data
Native-space T2w images are transformed into standard **MNI152NLin6Asym** space at 1 mm³ resolution.
**fsLR-space** morphometric surfaces are copied from the preprocessing derivatives provided by Infant-fMRIPrep to the XCP-D derivatives.
HCP-style midthickness, inflated, and very-inflated surfaces are generated from the white-matter and pial surface meshes and mapped to fsLR space.      
These surfaces and associated metrics are included in the XCP-D derivatives for downstream analysis.

### Functional data
For each BOLD run, XCP-D performs a series of cleanup and quality-control steps:

#### Preprocessing and Denoising
- The first four volumes (dummy scans) are removed.
- **Motion correction:** Framewise displacement (FD) is calculated per Power et al. (2014); volumes with FD > 0.3 mm are flagged as high-motion outliers.
- **Nuisance regression:** 36 confound regressors (motion, tissue, and global signals plus derivatives) are regressed out following the 36P strategy.
- **Despiking and filtering:** Data are despiked, temporally filtered (0.01–0.08 Hz), and smoothed (6 mm FWHM) to retain low-frequency neural signals while reducing noise.
- **Censoring:** High-motion volumes are interpolated and later censored to minimize motion artifacts.

#### Functional Metrics
Several functional measures are computed from the cleaned time series:

- **ALFF (Amplitude of Low-Frequency Fluctuations):** Quantifies spontaneous low-frequency signal amplitude across voxels.
- **ReHo (Regional Homogeneity):** Measures local synchronization of neural activity within surface and subcortical regions.

#### Connectivity Analysis
Parcellated time series are extracted for each atlas, described [here](../mri/index.md#parc), and pairwise functional connectivity is calculated as the Pearson correlation between regional time series.
For participants with multiple runs, postprocessed derivatives are concatenated across runs and directions.

## References

Andersson, Jesper L. R., Stefan Skare, and John Ashburner. 2003. “How to Correct Susceptibility Distortions in Spin-Echo Echo-Planar Images: Application to Diffusion Tensor Imaging.” NeuroImage 20 (2): 870–88. https://doi.org/10.1016/S1053-8119(03)00336-7.
