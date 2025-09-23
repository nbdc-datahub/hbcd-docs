# Diffusion MRI (dMRI)

<div class="table-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">See <a href="..">Overview</a> for MR protocols and <a href="../qc">MR Quality Control Procedures</a> for additional details.</span>
</div>
<p></p>

## Release Data

Diffusion data in the release includes <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> and <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> data - see [Data Structure Overview](../../datacuration/overview.md) for details on these different data types.

#### <i class="fa fa-hammer"></i> Raw BIDS

<div id="rawbids" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">Raw BIDS Files (<code>dwi/</code>)</span>
  <a class="anchor-link" href="#rawbids" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<div style="display: flex; align-items: center;">
  <img src="../../../images/BIDS-logo.png" style="width: 40px; margin-right: 10px;" alt="BIDS-logo">
  <p style="margin: 0;">
  <strong><i>BIDS Conversion</i></strong>: DICOM images are converted using an <a href="https://github.com/rordenlab/dcm2niix/tree/c5caaa9f858b704b61d3ff4a7989282922dd712e">HBCD-customized</a> version of <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a>. 
  Because <code>dcm2niix</code> sometimes omits or misconfigures NIfTI/JSON metadata, key fields for Philips data are hard-coded to ensure consistency across vendors. 
  These include <code>PhaseEncodingDirection</code>, <code>TotalReadoutTime</code>, <code>SliceTiming</code>, and the addition of <code>SmallDelta</code> and <code>LargeDelta</code> for Philips DWI data. All hard-coded values are also recorded in the <code>HardCodedValues</code> field of each JSON sidecar. 
  </p>
</div>
<p>Raw diffusion files include DWI runs (<code>*_dwi.nii.gz</code>), magnitude and orientation of the diffusion gradients for each volume (<code>bval</code> and <code>bvec</code>, respectively), and single-band reference files (<code>*_sbref.nii.gz</code>). All images were acquired in both AP (<code>dir-AP</code>) and PA (<code>dir-PA</code>) phase encoding directions.</p>
<pre class="folder-tree">
dwi/
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.bval
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.bvec
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.nii.gz
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.json
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_sbref.json
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_sbref.nii.gz
</pre>
</div>

------------------------------------

#### <i class="fas fa-cog"></i> Derivatives processed through the QSIPrep and QSIRecon

<div id="qsiprep" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
  <span class="text">QSIPrep (<code>qsiprep/</code>)</span>
  <a class="anchor-link" href="#qsiprep" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>The QSIPrep pipeline is used for preprocessing the HBCD diffusion-weighted MRI (dMRI) data. Preprocessing includes head motion correction, susceptibility distortion correction, MP-PCA denoising, coregistration to T1w images, ANTS spatial normalization, and tissue segmentation. The QSIPrep derivatives are then passed to <a href="#qsirecon">QSIRecon</a> for reconstruction.<br><a href="https://qsiprep.readthedocs.io/"><i class="fa-solid fa-book"></i> Go to pipeline documentation</a></p>
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
</div>

<div id="qsirecon" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
  <span class="text">QSIRecon (<code>qsirecon/</code>)</span>
  <a class="anchor-link" href="#qsirecon" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>QSIPrep derivatives are passed to QSIRecon for reconstruction, including ODF/FOD reconstruction, tractography, Fixel estimation, and regional connectivity. The data are processed using a variety of methods and models (e.g. <a href="https://dipy.org/">Dipy</a>, <a href="https://www.mrtrix.org/">MRTrix</a>, <a href="https://dsi-studio.labsolver.org/">DSI Studio</a>, etc). The contents of each QSIRecon derivative folder are described in individual sections below.<br><a href="https://qsirecon.readthedocs.io/"><i class="fa-solid fa-book"></i> Go to pipeline documentation</a></p>
<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ qsirecon/
    |   |__ log/
    |
    |__ qsirecon-*/
        |__ sub-<span class="label">{ID}</span>/
        |__ ses-<span class="label">{V0X}</span>/
            |__ dwi/
            |__ figures/
            |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.html    
</pre>
</div>

<div id="qsirecon-dsistudio" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
  <span class="text">QSIRecon-DSI Studio (<code>qsirecon-DSIStudio/</code>)</span>
  <a class="anchor-link" href="#qsirecon-dsistudio" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Diffusion Tensor Imaging (DTI) Maps include Fractional Anisotropy (FA) and Mean Diffusivity (MD), commonly used measures that represent the DWI signal using a 3D multivariate normal (Gaussian) distribution of water diffusion displacements. The FA of the diffusion tensor represents the degree of anisotropic diffusion. In neural tissues, FA is increased in white matter bundles with dense, parallel fiber orientations. The MD corresponds the directionally-averaged apparent diffusion coefficient of water in the tissue and is inversely related to the density of cellular membranes.</p>
<pre class="folder-tree" style="font-size: 11px;">
hbcd/
|_ derivatives/ 
   |_ qsirecon-DSIStudio/
      |_ sub-<span class="label">{ID}</span>/
         |_ ses-<span class="label">{V0X}</span>/
            |_ dwi/
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_tdistats.tsv
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-Association<span class="placeholder">&lt;ASSOC&gt;</span><span class="placeholder">&lt;L|R&gt;</span>_streamlines.tck.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-Cerebellum<span class="placeholder">&lt;CEREB&gt;</span>_streamlines.tck.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-CommissureAnteriorCommissure_streamlines.tck.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-CommissureCorpusCallosum_streamlines.tck.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-ProjectionBasalGanglia<span class="placeholder">&lt;BG&gt;</span><span class="placeholder">&lt;L|R&gt;</span>_streamlines.tck.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-ProjectionBrainstem<span class="placeholder">&lt;BRAINSTEM&gt;</span>_streamlines.tck.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundlestats.csv
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_dwimap.fib.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_dwimap.fib.gz.icbm152_adult.map.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_param-<span class="placeholder">&lt;gfa|iso&gt;</span>_dwimap.nii.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_param-qa_dwimap.nii.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_param-qa_dwimap.json
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-rdi_param-<span class="placeholder">&lt;rd1|rd2&gt;</span>_dwimap.nii.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-<span class="placeholder">&lt;ad|fa|ha|md|rd&gt;</span>_dwimap.nii.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-t<span class="placeholder">&lt;xx|xy|xz|yy|yz|zz&gt;</span>_dwimap.nii.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-MNIInfant+1_model-gqi_param-<span class="placeholder">&lt;gfa|iso|qa&gt;</span>_dwimap.nii.gz
            |
            |_ figures/
            |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.html
</pre>
<div id="legend" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dde6fe31;">
  <span class="emoji"><i class="fa-solid fa-tag"></i></span>
  <span class="text" style="font-size: 14px;">Label Values Legend</span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; font-size: 13px;">
  <thead>
    <tr>
      <th style="width: 15%; text-align: left;">BIDS Entity</th>
      <th style="width: 85%; text-align: left;">Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>&lt;ASSOC&gt;</strong></td>
      <td>
        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
          <span>ArcuateFasciculus</span>
          <span>Cingulum</span>
          <span>ExtremeCapsule</span>
          <span>FrontalAslantTract</span>
          <span>HippocampusAlveus</span>
          <span>InferiorFrontoOccipitalFasciculus</span>
          <span>&lt;Inferior|Middle|Superior&gt;LongitudinalFasciculus</span>
          <span>ParietalAslantTract</span>
          <span>AssociationUncinateFasciculus</span>
          <span>VerticalOccipitalFasciculus</span>
        </div>
      </td>
    </tr>
    <tr>
      <td><strong>&lt;CEREB&gt;</strong></td>
      <td>
        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
          <span>Cerebellum (L/R)</span>
          <span>InferiorCerebellarPeduncle (L/R)</span>
          <span>MiddleCerebellarPeduncle</span>
          <span>SuperiorCerebellarPeduncle</span>
          <span>Vermis</span>
        </div>
      </td>
    </tr>
    <tr>
      <td><strong>&lt;BG&gt;</strong></td>
      <td>
        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
          <span>AcousticRadiation</span>
          <span>AnsaLenticularis</span>
          <span>AnsaSubthalamica</span>
          <span>CorticostriatalTract</span>
          <span>FasciculusLenticularis</span>
          <span>FasciculusSubthalamicus</span>
          <span>Fornix</span>
          <span>OpticRadiation</span>
          <span>ThalamicRadiation</span>
        </div>
      </td>
    </tr>
    <tr>
      <td><strong>&lt;BRAINSTEM&gt;</strong></td>
      <td>
        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
          <span>CorticobulbarTract (L/R)</span>
          <span>CorticopontineTract (L/R)</span>
          <span>CorticospinalTract (L/R)</span>
          <span>DentatorubrothalamicTractrl</span>
          <span>MedialForebrainBundle (L/R)</span>
          <span>MedialLemniscus (L/R)</span>
          <span>NonDecussatingDentatorubrothalamicTract (L/R)</span>
          <span>ReticularTract (L/R)</span>
        </div>
      </td>
    </tr>
  </tbody>
</table>
</div>
</div>

<div id="qsirecon-DIPY" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
  <span class="text">QSIRecon- DIPY DKI (<code>qsirecon-DIPYDKI</code>)</span>
  <a class="anchor-link" href="#qsirecon-DIPY" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Diffusion Kurtosis Imaging (DKI) Maps, including <span class="tooltip">MK<span class="tooltiptext">Mean Kurtosis</span></span>, provide commonly used measures that expand the DTI signal model to estimate non-Gaussian diffusion kurtosis behavior in the brain. DKI maps may be used to better represent more complex diffusion-weighted signals phenomena that may be associated with more restricted diffusion. The MK is the directionally averaged kurtosis measure, which is increased in regions of dense white matter.</p>
<pre class="folder-tree" style="font-size: 11px;">
hbcd/
|_ derivatives/ 
   |_ qsirecon-DIPYDKI/
      |_ sub-<span class="label">{ID}</span>/
         |_ ses-<span class="label">{V0X}</span>/
            |_ dwi/
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-dki_param-<span class="placeholder">ad|ak|kfa|md|mk|mkt|rd|rk</span>_dwimap.nii.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-dki_param-<span class="placeholder">ad|ak|kfa|md|mk|mkt|rd|rk</span>_dwimap.json
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-fa_dwimap.nii.gz
            |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-fa_dwimap.json
            |
            |_ figures/
            |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.html
</pre>
</div>

<div id="qsirecon-TORTOISE-MAPMRI" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
  <span class="text">QSIRecon-TORTOISE Model MAP-MRI (<code>qsirecon-TORTOISE_model-MAPMRI/</code>)</span>
  <a class="anchor-link" href="#qsirecon-TORTOISE-MAPMRI" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>The <a href="https://github.com/QMICodeBase/TORTOISEV4">TORTOISE</a> software computes MAP-MRI and tensor fits along with derived scalar maps. 
Mean Apparent Propagator MRI (MAP-MRI) extends DTI by estimating a full spatial probability distribution (propagator) of water diffusion. In essence, MAP-MRI describes a probability distribution function of where a water molecule could travel to within a specified amount of time. Unlike DTI, MAP-MRI makes no assumptions about the diffusion profile, enabling quantification of non-Gaussian diffusion and providing more accurate measures of directionality and anisotropy (<a href="https://doi.org/10.1016/j.neuroimage.2013.04.016">Özarslan et al., 2013</a>). 
Key MAP-MRI metrics include:</p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <tr>
    <th>Metric</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
<tr>
  <td><span class="tooltip">PA<span class="tooltiptext">Propagator Anisotropy</span></span></td>
  <td style="word-wrap: break-word; white-space: normal;">More accurate than FA, PA quantifies anisotropy by computing the dissimilarity of the full MAP-MRI propagator from its fully isotropic counterpart.</td>
</tr>
<tr>
  <td><span class="tooltip">NG<span class="tooltiptext">Non-Gaussianity</span></span></td>
  <td style="word-wrap: break-word; white-space: normal;">The NG index quantifies deviation from Gaussian diffusion. <strong>NG</strong> measures overall deviation, <strong>NGpar</strong> along the primary diffusion axis (fiber direction in white matter), and <strong>NGperp</strong> perpendicular to it (often related to restriction).</td>
</tr>
<tr>
  <td><span class="tooltip">RTOP<span class="tooltiptext">Return To Origin Probability</span></span></td>
  <td style="word-wrap: break-word; white-space: normal;">Probability that a water molecule returns to its starting point. Low in unrestricted diffusion (large cells), high in restricted diffusion (small or impermeable cells). Inversely related to pore volume.</td>
</tr>
<tr>
  <td><span class="tooltip">RTAP<span class="tooltiptext">Return To Axis Probability</span></span></td>
  <td style="word-wrap: break-word; white-space: normal;">Probability that a water molecule returns to the principal diffusion axis (primary eigenvector).</td>
</tr>
<tr>
  <td><span class="tooltip">RTPP<span class="tooltiptext">Return To Plane Probability</span></span></td>
  <td style="word-wrap: break-word; white-space: normal;">Reciprocal of mean cylinder length and inversely proportional to axial diffusivity; Related to diffusion taking place within coherently oriented cylinders.</td>
</tr>
</tbody>
</table>
<pre class="folder-tree" style="font-size: 11px;">
hbcd/
|_ derivatives/ 
   |_ qsirecon-TORTOISE_model-MAPMRI/
      |_ sub-<span class="label">{ID}</span>/
         |_ ses-<span class="label">{V0X}</span>/
            |_ dwi/
            | |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
            | |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-mapmri_param-<span class="placeholder">&lt;MAPMRI&gt;</span>_dwimap.nii.gz <span class="hashtag">(+JSON)</span>
            | |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-<span class="placeholder">&lt;TENSOR&gt;</span>_dwimap.nii.gz <span class="hashtag">(+JSON)</span>
            |
            |_ figures/
            |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.html

<span class="hashtag"># Label Values Legend</span>
<span class="placeholder">&lt;MAPMRI&gt;</span>: ng, ngpar, ngperp, pa, path, rtap, rtop, rtpp
<span class="placeholder">&lt;TENSOR&gt;</span>: ad, am, fa, li, rd
</pre>
</div>

<div id="qsirecon-TORTOISE-tensor" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
  <span class="text">QSIRecon-TORTOISE Model Tensor (<code>qsirecon-TORTOISE_model-tensor/</code>)</span>
  <a class="anchor-link" href="#qsirecon-TORTOISE-tensor" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>In addition to MAPMRI, the <a href="https://github.com/QMICodeBase/TORTOISEV4">TORTOISE</a> software also calculates Tensor fits and scalar maps:</p>
<pre class="folder-tree" style="font-size: 11px;">
hbcd/
|_ derivatives/ 
   |_ qsirecon-TORTOISE_model-tensor/
      |_ sub-<span class="label">{ID}</span>/
         |_ ses-<span class="label">{V0X}</span>/
            |_ dwi/
               |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
               |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-MNIInfant+1_model-tensor_param-<span class="placeholder">ad|am|fa|li|rd</span>_dwimap.nii.gz
               |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-MNIInfant+1_model-tensor_param-<span class="placeholder">ad|am|fa|li|rd</span>_dwimap.json
</pre>
</div>

------------------------------------

#### <i class="fas fa-table"></i> Tabulated Data

Includes the `img_qsiprep_space-ACPC_desc-image_qc` data table, derived from the QSIPrep pipeline file `sub-{ID}_ses-{V0X}_space-ACPC_desc-image_qc.tsv`.


## Details

Diffusion-Weighted Imaging (DWI) refers to the raw image data acquired during scanning, provided in BIDS format as outlined in the [raw BIDS file tree above](#rawbids). The DWI protocol provides diffusion-weighted images that may be used to estimate multiple models of diffusion behavior in the central nervous system. The protocol acquires roughly 140 diffusion-weighted echo planar images at four b-values (diffusion-weighting) between 0 and 3000 s/mm^2 (12-13 minutes total acquisition time). For raw image acquisition, a minimum of 60% of the diffusion-weighted volumes are required to be collected for the acquisition to be deemed successful.

The diffusion-weighted images are processed with denoising and Gibbs artifact reduction, and corrected for eddy current distortion, head motion and echo planar susceptibility distortion ([Cieslak et al. 2021](https://doi.org/10.1038/s41592-021-01185-5)). The diffusion encoding enables the estimation of multiple diffusion MRI models to create the derived data, including:

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <tr>
    <th>Model</th>
    <th>Pipeline Derivatives (+Link to documentation)</th>
    <th>Reference</th>
  </tr>
</thead>
<tbody>
<tr>
  <td><span class="tooltip tooltip-right">DTI<span class="tooltiptext">Diffusion Tensor Imaging</span></span></td>
  <td><a href="#qsirecon-dsistudio">QSIRecon-DSI Studio</a> (<code>qsirecon-DSIStudio/</code>)</td>
  <td><a href="https://doi.org/10.1016/S0006-3495(94)80775-1">Basser et al. 1994</a></td>
</tr>
<tr>
  <td><span class="tooltip tooltip-right">DKI<span class="tooltiptext">Diffusion Kurtosis Imaging</span></span></td>
  <td><a href="#qsirecon-DIPY">QSIRecon- DIPY DKI</a> (<code>qsirecon-DIPYDKI/</code>)</td>
  <td><a href="https://doi.org/10.1002/mrm.20508">Jensen et al., 2005</a></td>
</tr>
<tr>
  <td><span class="tooltip tooltip-right">MAP-MRI<span class="tooltiptext">Mean Apparent Propagator</span></span></td>
  <td><a href="#qsirecon-TORTOISE-MAPMRI">QSIRecon-TORTOISE Model MAP-MRI</a> (<code>qsirecon-TORTOISE_model-MAPMRI/</code>)</td>
  <td><a href="https://doi.org/10.1016/j.neuroimage.2013.04.016">Özarslan et al. 2013</a></td>
</tr>
</tbody>
</table>

## References
<div class="references">
    <p>Alexander AL, Lee JE, Lazar M, Field AS. (2007). Diffusion tensor imaging of the brain. <em>Neurotherapeutics</em>, 4(3):316-29. <a href="https://doi.org/10.1016/j.nurt.2007.05.011">10.1016/j.nurt.2007.05.011</a></p>
    <p>Basser PJ, Mattiello J, LeBihan D. (1994). MR diffusion tensor spectroscopy and imaging. <em>Biophys J.</em>, 66(1):259-67. <a href="https://doi.org/10.1016/S0006-3495(94)80775-1">10.1016/S0006-3495(94)80775-1</a></p>
    <p>Cieslak M, Cook PA, He X, Yeh FC, Dhollander T, Adebimpe A, Aguirre GK, Bassett DS, Betzel RF, Bourque J, Cabral LM, Davatzikos C, Detre JA, Earl E, Elliott MA, Fadnavis S, Fair DA, Foran W, Fotiadis P, Garyfallidis E, Giesbrecht B, Gur RC, Gur RE, Kelz MB, Keshavan A, Larsen BS, Luna B, Mackey AP, Milham MP, Oathes DJ, Perrone A, Pines AR, Roalf DR, Richie-Halford A, Rokem A, Sydnor VJ, Tapera TM, Tooley UA, Vettel JM, Yeatman JD, Grafton ST, Satterthwaite TD. (2021). QSIPrep: an integrative platform for preprocessing and reconstructing diffusion MRI data. <em>Nature Methods</em>, 18(7):775-778. <a href="https://doi.org/10.1038/s41592-021-01185-5">10.1038/s41592-021-01185-5</a></p>
    <p>Jensen, J. H., Helpern, J. A., Ramani, A., Lu, H., & Kaczynski, K. (2005). Diffusional kurtosis imaging: the quantification of non-gaussian water diffusion by means of magnetic resonance imaging. Magnetic Resonance in Medicine, 53(6), 1432–1440. <a href="https://doi.org/10.1002/mrm.20508">https://doi.org/10.1002/mrm.20508</a></p>
    <p>Özarslan E, Koay CG, Shepherd TM, Komlosh ME, İrfanoğlu MO, Pierpaoli C, Basser PJ. (2013). Mean apparent propagator (MAP) MRI: a novel diffusion imaging method for mapping tissue microstructure. <em>Neuroimage</em>, 78:16-32. <a href="https://doi.org/10.1016/j.neuroimage.2013.04.016">10.1016/j.neuroimage.2013.04.016</a></p>
</div>
<br>

