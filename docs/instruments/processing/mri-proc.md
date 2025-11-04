# Structural & Functional MRI Processing

Structural and functional MRI data is processed via a sequence of BIDS App pipelines, so we describe the sequence here.

**BIBSNet**: generates brain segmentations and brain masks

**Infant fMRIPrep**: Brain segmentations and masks are fed into Infant fMRIPrep, which produces minimal structural and functional MRI processing including visual quality assessment reports, preprocessed derivatives, and confounds to be used for denoising in subsequent processing procedures.

**XCP-D**: Infant fMRIPrep outputs are fed into XCP-D, which performs functional MRI post-processing and noise regression.

## Infant fMRIPrep

### Preprocessing of B0 inhomogeneity mappings
A B0-nonuniformity map (or fieldmap) is estimated based on two (or more) echo-planar imaging (EPI) references with topup (Andersson, Skare, and Ashburner (2003); FSL None).

### Anatomical data preprocessing
Anatomical images (T1w and/or T2w) are denoised and corrected for intensity non-uniformity (INU). **A pre-computed brain mask is provided as input and used throughout the workflow.**

Surface reconstruction is performed via 2 methods:

#### (1) M-CRIB-S
A modified MCRIBReconAll (M-CRIB-S, Adamson et al. 2020) workflow is run using the reference T2w and a pre-computed anatomical segmentation. Volume-based spatial normalization to one standard space (MNIInfant:cohort-1) was performed through nonlinear registration with antsRegistration, using brain-extracted versions of both T1w reference and the T1w template. 

Age-specific MNI Infant Atlases 0-4.5yr [Fonov et al. (2009), RRID:SCR_008796; TemplateFlow ID: MNIInfant:cohort-1] are selected for spatial normalization and accessed with TemplateFlow (24.2.2, Ciric et al. 2022). Volume-based spatial normalization to one standard space (MNI152NLin6Asym) is performed by concatenating two registrations with antsRegistration. First, the anatomical reference is registered to the Infant MNI templates (Fonov et al. (2009)). Separately, the Infant MNI templates are registered to one standard space, with the saved transform to template stored for reuse and accessed with TemplateFlow (24.2.2, Ciric et al. 2022): FSL’s MNI ICBM 152 non-linear 6th Generation Asymmetric Average Brain Stereotaxic Registration Model [Evans et al. (2012), RRID:SCR_002823; TemplateFlow ID: MNI152NLin6Asym].

#### (2) Infant FreeSurfer
ADD TEXT

### Functional Data Preprocessing
For each BOLD run, the following preprocessing is performed:

A reference volume is generated for use in head motion correction. Head-motion parameters with respect to the BOLD reference (transformation matrices, and six corresponding rotation and translation parameters) are estimated before any spatiotemporal filtering using `mcflirt` (FSL , Jenkinson et al. 2002).

The estimated fieldmap is aligned with rigid-registration to the target EPI (echo-planar imaging) reference run, the field coefficients are mapped on to the reference EPI using the transform, and the BOLD reference is co-registered to the anatomical reference (boundary-based registration with six degrees of freedom) (Greve and Fischl 2009). The aligned T2w image is used for initial co-registration.

Several confounding time-series are calculated based on the preprocessed BOLD, including: framewise displacement (FD), DVARS and three region-wise global signals. FD was computed using two formulations following Power (absolute sum of relative motions, Power et al. (2014)) and Jenkinson (relative root mean square displacement between affines, Jenkinson et al. (2002)). FD and DVARS are calculated for each functional run. The three global signals are extracted within the CSF, the WM, and the whole-brain masks. Additionally, a set of physiological regressors are extracted to allow for component-based noise correction (CompCor, Behzadi et al. 2007). Principal components are estimated after high-pass filtering the preprocessed BOLD time-series (using a discrete cosine filter with 128s cut-off) for the two CompCor variants: temporal (tCompCor) and anatomical (aCompCor). tCompCor components are then calculated from the top 2% variable voxels within the brain mask. For aCompCor, three probabilistic masks (CSF, WM and combined CSF+WM) are generated in anatomical space. The implementation differs from that of Behzadi et al. in that instead of eroding the masks by 2 pixels on BOLD space, a mask of pixels that likely contain a volume fraction of GM is subtracted from the aCompCor masks. This mask is obtained by dilating a GM mask extracted from the FreeSurfer’s aseg segmentation, and it ensures components are not extracted from voxels containing a minimal fraction of GM. Finally, these masks are resampled into BOLD space and binarized by thresholding at 0.99 (as in the original implementation).

Components are also calculated separately within the WM and CSF masks. For each CompCor decomposition, the k components with the largest singular values are retained, such that the retained components’ time series are sufficient to explain 50 percent of variance across the nuisance mask (CSF, WM, combined, or temporal). The remaining components are dropped from consideration. The head-motion estimates calculated in the correction step were also placed within the corresponding confounds file. The confound time series derived from head motion estimates and global signals are expanded with the inclusion of temporal derivatives and quadratic terms for each (Satterthwaite et al. 2013). Frames that exceeded a threshold of 0.5 mm FD or 1.5 standardized DVARS are annotated as motion outliers. Additional nuisance timeseries are calculated by means of principal components analysis of the signal found within a thin band (crown) of voxels around the edge of the brain (Patriat, Reynolds, and Birn 2017). The BOLD time-series are resampled onto fsnative. The BOLD time-series are resampled onto the left/right-symmetric template “fsLR” using the Connectome Workbench (Glasser et al. 2013). 

A “goodvoxels” mask is applied during volume-to-surface sampling in fsLR space, excluding voxels whose time-series have a locally high coefficient of variation. Grayordinates files (Glasser et al. 2013) containing 91k samples are also generated using the highest-resolution fsaverage as intermediate standardized surface space. All resamplings can be performed with a single interpolation step by composing all the pertinent transformations (i.e. head-motion transform matrices, susceptibility distortion correction when available, and co-registrations to anatomical and output spaces). Gridded (volumetric) resamplings are performed using nitransforms, configured with cubic B-spline interpolation. Non-gridded (surface) resamplings are performed using mri_vol2surf (FreeSurfer).

## References

Andersson, Jesper L. R., Stefan Skare, and John Ashburner. 2003. “How to Correct Susceptibility Distortions in Spin-Echo Echo-Planar Images: Application to Diffusion Tensor Imaging.” NeuroImage 20 (2): 870–88. https://doi.org/10.1016/S1053-8119(03)00336-7.




