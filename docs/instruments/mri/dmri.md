# Diffusion MRI (dMRI)

<p>
<div id="fyi" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">Please see <a href="../#mri-protocols-sequence-installation">MRI Protocols</a> and <a href="../qc">MR Quality Control Procedures</a> for additional details.</span>
</div>
</p>

## Diffusion-Weighted Acquisitions
Diffusion-Weighted Imaging (DWI) refers to the raw image data acquired during scanning. The DWI protocol provides diffusion-weighted images that may be used to estimate multiple models of diffusion behavior in the central nervous system. The protocol acquires roughly 140 diffusion-weighted echo planar images at four b-values (diffusion-weighting) between 0 and 3000 s/mm^2 (12-13 minutes total acquisition time). For raw image acquisition, a minimum of 60% of the diffusion-weighted volumes are required to be collected for the acquisition to be deemed successful. 

The diffusion-weighted images are processed with denoising and Gibbs artifact reduction, and corrected for eddy current distortion, head motion and echo planar susceptibility distortion ([Cieslak et al. 2021](https://doi.org/10.1038/s41592-021-01185-5)). The diffusion encoding enables the estimation of multiple diffusion MRI models including diffusion tensor imaging (DTI) (Basser et al. 1994), diffusion kurtosis imaging (DKI) ([Jensen et al., 2005](https://doi.org/10.1002/mrm.20508)), and mean apparent propagator (MAP) ([Özarslan et al. 2013](https://doi.org/10.1016/j.neuroimage.2013.04.016)). Each of these is described in greater detail below.

## Derived Images
### Diffusion Tensor Imaging (DTI) Maps
DTI maps, including **fractional anisotropy (FA)** and **mean diffusivity (MD)**, are commonly used measures that represent the DWI signal using a 3D multivariate normal (Gaussian) distribution of water diffusion displacements. The FA of the diffusion tensor represents the degree of anisotropic diffusion. In neural tissues, FA is increased in white matter bundles with dense, parallel fiber orientations. The MD corresponds the directionally-averaged apparent diffusion coefficient of water in the tissue and is inversely related to the density of cellular membranes. 

### Diffusion Kurtosis Imaging (DKI) Maps
DKI maps, including mean kurtosis (MK), provide commonly used measures that expand the DTI signal model to estimate non-Gaussian diffusion kurtosis behavior in the brain. DKI maps may be used to better represent more complex diffusion-weighted signals phenomena that may be associated with more restricted diffusion. The mean kurtosis (MK) is the directionally averaged kurtosis measure, which is increased in regions of dense white matter.  

### Mean Apparent Propagator (MAP-MRI)
The Mean Apparent Propagator (MAP-MRI) extends DTI to generate a true and proper propagator, i.e. a spatial probability distribution function that indicates the likelihood a water molecule will end up at a given position for a specified diffusion time. Because of its non-parametric nature and lack of any assumptions on this distribution, MAP-MRI can quantify the non-Gaussian character of the diffusion process, therefore, more accurately characterizes diffusion directionality and anisotropy (please refer to [Özarslan et al. 2013](https://doi.org/10.1016/j.neuroimage.2013.04.016) for details). MAP-MRI includes the following metrics:

<p style="font-size: 1.1em; margin: 0 0 5px;"><u>Propagator Anisotropy (PA)</u></p>
**PA** computed with MAP-MRI provides a more accurate metric of anisotropy compared to FA (described above) by relating the entire three-dimensional apparent propagator to a measure of anisotropy. This is accomplished by computing the dissimilarity of a MAP-MRI propagator from its fully isotropic counterpart.  

<p style="font-size: 1.1em; margin: 0 0 5px;"><u>Non-Gaussianity (NG)</u></p>
MAP-MRI propagators are described as a summation of basis functions, where the first term is the diffusion tensor. The additional terms describe how the diffusion process deviates from pure Gaussian. The **NG** index provides a normalized magnitude of these terms. NG measures the overall 3D deviation from a tensor, whereas **NGpar** describes the non-Gaussianity along the primary axis of the diffusion (fiber direction in white matter), and **NGperp** defines it along the perpendicular cross-section (more related to restriction).

<p style="font-size: 1.1em; margin: 0 0 5px;"><u>Return To Origin/Axis Probability (RTOP & RTAP)</u></p>
As described above, MAP-MRI, in essence, describes a probability distribution function of where a water molecule could travel to within a specified amount of time. **RTOP** measures the probability that the water molecule would return to its original location. For a large cell with no barriers, this probability would be quite low, whereas for a very small cell with impermeable cell membranes, this probably would be significantly larger as the molecule does not have freedom to move farther. Therefore, RTOP is inversely proportional to pore volume. The mean diffusivity metric from the DTI model is known to be directly proportional to the pore volume, therefore, RTOP is a measure of (inverse) diffusivity for more complex diffusion profiles. 

Similar to RTOP, **RTAP** describes the probability of the water molecule to return to the axis of principal diffusion direction (primary eigenvector) and RTPP is equal to the reciprocal of the mean length of the cylinders, therefore inversely proportional to axial diffusivity, for diffusion taking place within coherently oriented cylinders.

## Release Data

Diffusion data in the release includes <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> and <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> data:

- <i class="fa fa-hammer"></i> <a href="../../../datacuration/file-based-data/#raw-bids" target="_blank">Raw BIDS</a> under subject- and session-specific <code>dwi/</code> folders
- <i class="fas fa-cog"></i> <a href="../../../datacuration/file-based-data/#processed-derivatives" target="_blank">Derivatives</a> processed through the QSIPrep and QSIRecon pipelines under <code>qsiprep/</code> and <code>qsirecon*/</code>
- <i class="fas fa-table"></i> <a href="../../../datacuration/phenotypes" target="_blank">Tabulated</a> `img_qsiprep_space-ACPC_desc-image_qc` data table derived from the QSIPrep pipeline file `sub-{ID}_ses-{V0X}_space-ACPC_desc-image_qc.tsv`

### Raw BIDS

<div id="bids-conversion" class="table-banner" onclick="toggleCollapse(this)">
  <img src="../../../images/BIDS-logo.png" style="width: 3%;" alt="BIDS-logo">
  <span class="text-with-link">
  <span>BIDS Conversion Procedures</span>
  <a class="anchor-link" href="#bids-conversion" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>To convert imaging data to BIDS standard formatting, the DICOM image files are processed through an <a href="https://github.com/rordenlab/dcm2niix/tree/c5caaa9f858b704b61d3ff4a7989282922dd712e">HBCD-customized version</a> of the <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a> tool.</p>
<p><b>Hardcoded Fields for Philips</b><br>
In some cases, <code>dcm2niix</code> conversion led to missing or incorrectly configured NIfTI/JSON metadata. To address these issues, certain headers were hard-coded after conversion. These hard-coded values are also documented in the <code>HardCodedValues</code> field of the corresponding JSON sidecar file. The following fields were hard-coded for Philips DWI data:</p>
<ul>
  <li><code>PhaseEncodingDirection</code></li>
  <li><code>TotalReadoutTime</code></li>
  <li><code>SliceTiming</code></li>
  <li>Addition of fields <code>SmallDelta</code> & <code>LargeDelta</code></li>
</ul>
</div>

Diffusion files include DWI runs (`*_dwi.nii.gz`) along with `bval` and `bvec` (magnitudes and orientations of the diffusion gradients for each volume, respectively), and single-band reference files (`*_sbref.nii.gz`). All images were acquired in both AP (`dir-AP`) and PA (`dir-PA`) phase encoding directions.
<pre class="folder-tree">
dwi/
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.bval
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.bvec
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.nii.gz
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.json
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_sbref.json
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_sbref.nii.gz
</pre>

### Derivatives

Diffusion MRI data was processed through [QSIPrep](#qsiprep-qsiprep) and [QSIRecon](#qsirecon) pipelines, with the following folders included in the release:

<pre class="folder-tree">
<span class="hashtag"># Diffusion MRI Pipeline Derivatives:</span>
hbcd/
|__ derivatives/ 
    |__ qsiprep/
    |__ qsirecon/
    |__ qsirecon-DIPYDKI/
    |__ qsirecon-DSIStudio/
    |__ qsirecon-NODDI/
    |__ qsirecon-TORTOISE_model-MAPMRI/
    |__ qsirecon-TORTOISE_model-tensor/
</pre>

#### QSIPrep (`qsiprep/`) 
The QSIPrep pipeline is used for preprocessing the HBCD diffusion-weighted MRI (dMRI) data. Preprocessing includes head motion correction, susceptibility distortion correction, MP-PCA denoising, coregistration to T1w images, ANTS spatial normalization, and tissue segmentation. The QSIPrep derivatives are then passed to [QSIRecon](#qsirecon) for reconstruction.      
[<i class="fa-solid fa-book"></i> Go to pipeline documentation](https://qsiprep.readthedocs.io/)

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ qsiprep/
        |__ sub-<span class="label">{ID}</span>/
            |__ log/
            |__ ses-<span class="label">{V0X}</span>/
                |__ anat/
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_from-ACPC_to-anat_mode-image_xfm.mat        
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_from-ACPC_to-MNIInfant+1_mode-image_xfm.h5
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_from-anat_to-ACPC_mode-image_xfm.mat
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_from-MNIInfant+1_to-ACPC_mode-image_xfm.h5
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_from-orig_to-anat_mode-image_xfm.txt
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-aseg_dseg.nii.gz
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-brain_mask.nii.gz
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_T2w.json
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_T2w.nii.gz
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_dseg.nii.gz
                |
                |__ dwi/
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-confounds_timeseries.tsv
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-desc-pepolar_qc.tsv
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-brain_mask.nii.gz
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-image_qc.tsv
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_dwi.b
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_dwi.b_table.txt
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_dwi.bval
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_dwi.bvec
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_dwi.nii.gz <span class="hashtag">(+JSON)</span>
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-slice_qc.json
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_dwiref.nii.gz
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-eddy_stat-cnr_dwimap.nii.gz <span class="hashtag">(+JSON)</span>
                |
                |__ figures/
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.html
</pre>

#### QSIRecon 
QSIPrep derivatives are passed to QSIRecon for reconstruction, including ODF/FOD reconstruction, tractography, Fixel estimation, and regional connectivity. The data are processed using a variety of methods and models (e.g. [Dipy](https://dipy.org/), [MRTrix](https://www.mrtrix.org/), [DSI Studio](https://dsi-studio.labsolver.org/), etc).The [TORTOISE](https://github.com/QMICodeBase/TORTOISEV4) software calculates MAPMRI and Tensor fits and scalar maps.        
[<i class="fa-solid fa-book"></i> Go to pipeline documentation](https://qsirecon.readthedocs.io/)

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ qsirecon/
    |  |__ log/
    |
    |__ qsirecon-*/
        |__ sub-<span class="label">{ID}</span>/
            |__ ses-<span class="label">{V0X}</span>/
                |__ dwi/
                |__ figures/
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.html    
</pre>  

<pre class="folder-tree" style="font-size: 11px;">
<span class="subses">qsirecon-DIPYDKI/</span>...dwi/
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-dki_param-<span class="placeholder">ad|ak|kfa|md|mk|mkt|rd|rk</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-dki_param-<span class="placeholder">ad|ak|kfa|md|mk|mkt|rd|rk</span>_dwimap.json
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-fa_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-fa_dwimap.json

<span class="subses">qsirecon-DSIStudio/</span>...dwi/
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_tdistats.tsv
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-Association<span class="placeholder">&lt;ASSOC&gt;</span><span class="placeholder">&lt;L|R&gt;</span>_streamlines.tck.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-Cerebellum<span class="placeholder">&lt;CEREB&gt;</span>_streamlines.tck.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-CommissureAnteriorCommissure_streamlines.tck.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-CommissureCorpusCallosum_streamlines.tck.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-ProjectionBasalGanglia<span class="placeholder">&lt;BG&gt;</span><span class="placeholder">&lt;L|R&gt;</span>_streamlines.tck.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-ProjectionBrainstem<span class="placeholder">&lt;BRAINSTEM&gt;</span>_streamlines.tck.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundlestats.csv
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_dwimap.fib.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_dwimap.fib.gz.icbm152_adult.map.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_param-<span class="placeholder">&lt;gfa|iso&gt;</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_param-qa_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_param-qa_dwimap.json
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-rdi_param-<span class="placeholder">&lt;rd1|rd2&gt;</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-<span class="placeholder">&lt;ad|fa|ha|md|rd&gt;</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-t<span class="placeholder">&lt;xx|xy|xz|yy|yz|zz&gt;</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-MNIInfant+1_model-gqi_param-<span class="placeholder">&lt;gfa|iso|qa&gt;</span>_dwimap.nii.gz

<span class="subses">qsirecon-TORTOISE_model-MAPMRI/</span>...dwi/
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-mapmri_param-<span class="placeholder">ng|ngpar|ngperp|pa|path|rtap|rtop|rtpp</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-mapmri_param-<span class="placeholder">ng|ngpar|ngperp|pa|path|rtap|rtop|rtpp</span>_dwimap.json
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-<span class="placeholder">&lt;TENSOR-PARAM&gt;</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-<span class="placeholder">&lt;TENSOR-PARAM&gt;</span>_dwimap.json

<span class="subses">qsirecon-TORTOISE_model-tensor/</span>...dwi/
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-MNIInfant+1_model-tensor_param-<span class="placeholder">ad|am|fa|li|rd</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-MNIInfant+1_model-tensor_param-<span class="placeholder">ad|am|fa|li|rd</span>_dwimap.json
</pre>

<div id="legend" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-tag"></i></span>
  <span class="text">Label Values Legend (<i>DSI Studio</i>)</span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<thead>
<tr>
    <th style="width: 10%;">BIDS Entity Label</th>
    <th style="width: 90%;">Values</th>
</tr>
</thead>
<tbody>
  <tr>
      <td><strong>&lt;ASSOC&gt;</strong></td>
      <td style="word-wrap: break-word; white-space: normal;">ArcuateFasciculus, Cingulum, ExtremeCapsule, FrontalAslantTract, HippocampusAlveus, InferiorFrontoOccipitalFasciculus, InferiorLongitudinalFasciculus, MiddleLongitudinalFasciculus, ParietalAslantTract, SuperiorLongitudinalFasciculus, AssociationUncinateFasciculus, VerticalOccipitalFasciculus</td>
  </tr>
  <tr>
      <td><strong>&lt;CEREB&gt;</strong></td>
      <td style="word-wrap: break-word; white-space: normal;">Cerebellum(L/R), InferiorCerebellarPeduncle (L/R), MiddleCerebellarPeduncle, SuperiorCerebellarPeduncle, Vermis</td>
  </tr>
  <tr>
      <td><strong>&lt;BG&gt;</strong></td>
      <td style="word-wrap: break-word; white-space: normal;">AcousticRadiation, AnsaLenticularis, AnsaSubthalamica, CorticostriatalTract, FasciculusLenticularis, FasciculusSubthalamicus, Fornix, OpticRadiation, ThalamicRadiation</td>
  </tr>
  <tr>
      <td><strong>&lt;BRAINSTEM&gt;</strong></td>
      <td style="word-wrap: break-word; white-space: normal;">CorticobulbarTract(L\R), CorticopontineTract(L/R), CorticospinalTract(L/R), DentatorubrothalamicTractrl, MedialForebrainBundle(L/R), MedialLemniscus(L/R), NonDecussatingDentatorubrothalamicTract(L/R), ReticularTract(L/R)</td>
  </tr>
</tbody>
</table>
</div>

## References
<div class="references">
    <p>Alexander AL, Lee JE, Lazar M, Field AS. (2007). Diffusion tensor imaging of the brain. <em>Neurotherapeutics</em>, 4(3):316-29. <a href="https://doi.org/10.1016/j.nurt.2007.05.011">10.1016/j.nurt.2007.05.011</a></p>
    <p>Basser PJ, Mattiello J, LeBihan D. (1994). MR diffusion tensor spectroscopy and imaging. <em>Biophys J.</em>, 66(1):259-67. <a href="https://doi.org/10.1016/S0006-3495(94)80775-1">10.1016/S0006-3495(94)80775-1</a></p>
    <p>Cieslak M, Cook PA, He X, Yeh FC, Dhollander T, Adebimpe A, Aguirre GK, Bassett DS, Betzel RF, Bourque J, Cabral LM, Davatzikos C, Detre JA, Earl E, Elliott MA, Fadnavis S, Fair DA, Foran W, Fotiadis P, Garyfallidis E, Giesbrecht B, Gur RC, Gur RE, Kelz MB, Keshavan A, Larsen BS, Luna B, Mackey AP, Milham MP, Oathes DJ, Perrone A, Pines AR, Roalf DR, Richie-Halford A, Rokem A, Sydnor VJ, Tapera TM, Tooley UA, Vettel JM, Yeatman JD, Grafton ST, Satterthwaite TD. (2021). QSIPrep: an integrative platform for preprocessing and reconstructing diffusion MRI data. <em>Nature Methods</em>, 18(7):775-778. <a href="https://doi.org/10.1038/s41592-021-01185-5">10.1038/s41592-021-01185-5</a></p>
    <p>Jensen, J. H., Helpern, J. A., Ramani, A., Lu, H., & Kaczynski, K. (2005). Diffusional kurtosis imaging: the quantification of non-gaussian water diffusion by means of magnetic resonance imaging. Magnetic Resonance in Medicine, 53(6), 1432–1440. <a href="https://doi.org/10.1002/mrm.20508">https://doi.org/10.1002/mrm.20508</a></p>
    <p>Özarslan E, Koay CG, Shepherd TM, Komlosh ME, İrfanoğlu MO, Pierpaoli C, Basser PJ. (2013). Mean apparent propagator (MAP) MRI: a novel diffusion imaging method for mapping tissue microstructure. <em>Neuroimage</em>, 78:16-32. <a href="https://doi.org/10.1016/j.neuroimage.2013.04.016">10.1016/j.neuroimage.2013.04.016</a></p>
</div>
<br>

