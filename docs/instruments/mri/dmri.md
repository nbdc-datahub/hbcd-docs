# Diffusion MRI (dMRI)

**Diffusion-Weighted Imaging (DWI)** measures the diffusion of water molecules in tissue and is used to model white matter microstructure and structural connectivity in the central nervous system.

## Acquisition

Full protocols, sequence installation, and operation instructions are available via <a href="https://hbcdsequences.readthedocs.io/">HBCD Study MRI Protocols</a>. In brief, the DWI protocol acquires roughly 140 diffusion-weighted echo planar images at four b-values (diffusion-weighting) between 0 and 3000 s/mm<sup>2</sup> (12-13 minutes total acquisition time). For raw image acquisition, a minimum of 60% of the diffusion-weighted volumes are required to be collected for the acquisition to be deemed successful.

## Processing & Derivatives

<div class="table-banner"> <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span> <span class="text"> Full details of HBCD diffusion MRI processing and methods are described in <a href="https://doi.org/10.1101/2025.11.10.687672">Cieslak et al. 2025</a>. </span> </div>
<p></p>

Diffusion MRI data are preprocessed using **[QSIPrep](https://qsiprep.readthedocs.io/)**, which performs motion and distortion correction, MP-PCA denoising, co-registration to T1w images, spatial normalization (ANTs), and tissue segmentation ([Cieslak et al. 2021](https://doi.org/10.1038/s41592-021-01185-5), [Cieslak et al. 2025](https://doi.org/10.1101/2025.11.10.687672)). Preprocessed outputs are then passed to **[QSIRecon](https://qsirecon.readthedocs.io/)**, which runs curated reconstruction workflows, including ODF/FOD reconstruction, tractography, Fixel estimation, and regional connectivity. 

<table class="table-no-vertical-lines"> 
<thead> <th>Pipeline</th> <th>Folder</th> <th>Description</th> </thead> 
<tbody> 
<tr> <td><b>QSIPrep</b></td> <td><code>qsiprep/</code></td> <td>Preprocessed diffusion data, transforms, QC metrics & reports</td> </tr> 
<tr> <td><b>QSIRecon</b></td> <td><code>qsirecon/</code></td> <td><a href="https://qsirecon.readthedocs.io/">QSIRecon</a> workflow logs and configuration files</td> </tr> 
<tr> <td><b>QSIRecon-DSIStudio</b></td> <td><code>qsirecon-DSIStudio/</code></td> <td><a href="https://dsi-studio.labsolver.org/">DSI Studio</a> DTI reconstruction & tractography</td> </tr>
<tr> <td><b>QSIRecon-DIPYDKI</b></td> <td><code>qsirecon-DIPYDKI/</code></td> <td><a href="https://dipy.org/">DIPY</a> Diffusion kurtosis (DKI) and tensor-derived maps</td> </tr> 
<tr> 
<td rowspan="2"><b>QSIRecon-TORTOISE</b></td>
<td><code>qsirecon-TORTOISE_model-MAPMRI/</code></td>
<td><a href="https://github.com/QMICodeBase/TORTOISEV4">TORTOISE</a> MAP-MRI and scalar maps</td> </tr> 
<tr>
<td><code>qsirecon-TORTOISE_model-tensor/</code></td>
<td><a href="https://github.com/QMICodeBase/TORTOISEV4">TORTOISE</a> Tensor fits and scalar maps</td> </tr> 
</tbody> </table> 

<p><a href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>

<div id="qsiprep" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>  <span class="text-with-link">
  <span class="text">QSIPrep Derivatives</span>  <a class="anchor-link" href="#qsiprep" title="Copy link">
  <i class="fa-solid fa-link"></i>  </a>  </span>  <span class="arrow">▸</span></div>
<div class="table-collapsible-content">
<pre class="folder-tree" style="font-size: 11px;">
hbcd/
└── derivatives/
    └── qsiprep/
        └── sub-{ID}/
            ├── log/
            └── ses-{V0X}/
                ├── anat/
                │   <span class="hashtag"># Transforms</span>
                │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>from-<span class="placeholder">&lt;ACPC_to-anat|anat_to-ACPC&gt;</span>_mode-image_xfm.mat
                │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>from-<span class="placeholder">&lt;ACPC_to-MNIInfant+1|MNIInfant+1_to-ACPC&gt;</span>_mode-image_xfm.h5
                │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>from-orig_to-anat_mode-image_xfm.txt
                │
                │   <span class="hashtag"># Structural outputs (ACPC space)</span>
                │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_desc-preproc_T2w.nii.gz <span class="hashtag">(+JSON)</span>
                │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_desc-<span class="placeholder">&lt;aseg_dseg|brain_mask&gt;</span>.nii.gz
                │   └── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_dseg.nii.gz
                │
                ├── dwi/
                │   <span class="hashtag"># QC & confounds</span>
                │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>desc-confounds_timeseries.tsv
                │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>desc-<span class="placeholder">&lt;image|pepolar&gt;</span>_qc.tsv
                │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_desc-slice_qc.json
                │
                │   <span class="hashtag"># Preprocessed data</span>
                │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_desc-preproc_dwi.nii.gz <span class="hashtag">(+JSON)</span>
                │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_desc-preproc_dwi.<span class="placeholder">&lt;bval|bvec|b|b_table.txt&gt;</span>
                │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_dwiref.nii.gz
                │
                │   <span class="hashtag"># Masks & maps</span>
                │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_desc-brain_mask.nii.gz
                │   └── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_model-eddy_stat-cnr_dwimap.nii.gz <span class="hashtag">(+JSON)</span>
                │
                ├── figures/
                └── <span class="muted">sub-{ID}_ses-{V0X}_</span>.html
</pre>
</div>

<div id="qsirecon" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span><span class="text-with-link">
  <span class="text">QSIRecon Derivatives</span><a class="anchor-link" href="#qsirecon" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><a href="https://qsirecon.readthedocs.io/">QSIRecon</a> outputs are organized into separate derivative folders by reconstruction workflow. 
The <code>qsirecon/</code> directory stores workflow metadata and logs. <i><b>Below:</b> Each folder corresponds to a reconstruction method; outputs are organized by session and modality (dwi/ + figures). For brevity, logs, figures, and JSON sidecars filenames are not shown.</i></p>
<pre class="folder-tree" style="font-size: 11px;">
hbcd/
└── derivatives/
    ├── qsirecon/
    │   └── <span class="muted">sub-{ID}/</span>
    │       └── log/*
    <!-- │           └── <span class="label">{YYYYMMDD-HHMMSS_UUID}</span>/
    │               ├── qsirecon.toml
    │               └── recon_spec.yaml -->
  <span class="hashtag">DSI Studio</span>
    ├── qsirecon-DSIStudio/
    │   └── <span class="muted">sub-{ID}/</span>
    │       └── <span class="muted">ses-{V0X}/</span>
    │           ├── dwi/
    │           │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_bundles-DSIStudio_<span class="placeholder">&lt;scalar|tdi&gt;</span>stats.tsv
    │           │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_model-gqi_bundle-<span class="placeholder">&lt;BUNDLE&gt;</span>_streamlines.tck.gz
    │           │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_model-gqi_bundlestats.csv
    │           │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_model-gqi_dwimap.fib.gz
    │           │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_model-gqi_dwimap.fib.gz.icbm152_adult.map.gz
    │           │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_model-gqi_param-<span class="placeholder">&lt;gfa|iso|qa&gt;</span>_dwimap.nii.gz
    │           │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-rdi_param-<span class="placeholder">&lt;rd1|rd2&gt;</span>_dwimap.nii.gz
    │           │   └── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-<span class="placeholder">&lt;DTI-PARAM&gt;</span>_dwimap.nii.gz
    │           ├── figures/*
    │           └── <span class="muted">sub-{ID}_ses-{V0X}_</span>.html

  <span class="hashtag">DIPY-DKI</span>
    ├── qsirecon-DIPYDKI/
    │   └── <span class="muted">sub-{ID}/</span>
    │       └── <span class="muted">ses-{V0X}/</span>
    │           ├── dwi/
    │           │   # DIPY DKI
    │           │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_bundles-DSIStudio_scalarstats.tsv
    │           │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-dki_param-<span class="placeholder">&lt;DKI-PARAM&gt;</span>_dwimap.nii.gz
    │           │   └── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-fa_dwimap.nii.gz
    │           ├── figures/*
    │           └── <span class="muted">sub-{ID}_ses-{V0X}_</span>.html
    
  <span class="hashtag">TORTOISE MAP-MRI</span>
    ├── qsirecon-TORTOISE_model-MAPMRI/
    │   └── <span class="muted">sub-{ID}/</span>
    │       └── <span class="muted">ses-{V0X}/</span>
    │           ├── dwi/
    │           │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_bundles-DSIStudio_scalarstats.tsv
    │           │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-mapmri_param-<span class="placeholder">&lt;MAPMRI&gt;</span>_dwimap.nii.gz
    │           │   └── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-<span class="placeholder">&lt;TENSOR&gt;</span>_dwimap.nii.gz
    │           ├── figures/*
    │           └── <span class="muted">sub-{ID}_ses-{V0X}_</span>.html
    
  <span class="hashtag">TORTOISE Tensor</span>
    └── qsirecon-TORTOISE_model-tensor/
        └── <span class="muted">sub-{ID}/</span>
            └── <span class="muted">ses-{V0X}/</span>
                └── dwi/
                    ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-ACPC_bundles-DSIStudio_scalarstats.tsv
                    └── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-MNIInfant+1_model-tensor_param-<span class="placeholder">&lt;TENSOR&gt;</span>_dwimap.nii.gz

<span class="hashtag"># Label Values Legend</span>
<span class="placeholder">DTI-PARAM</span>: ad, fa, ha, md, rd, txx, txy, txz, tyy, tyz, tzz
<span class="placeholder">DKI-PARAM</span>: ad, ak, kfa, md, mk, mkt, rd, rk
<span class="placeholder">MAPMRI</span>: ng, ngpar, ngperp, pa, path, rtap, rtop, rtpp
<span class="placeholder">TENSOR</span>: ad, am, fa, li, rd

<span class="hashtag"># DSI Studio &lt;BUNDLE&gt; groups:</span> → See <a href="#bundle">full DSIStudio bundle label list</a>
Association<span class="placeholder">&lt;LABEL&gt;</span>, Cerebellum<span class="placeholder">&lt;LABEL&gt;</span>, Commissure<span class="placeholder">&lt;LABEL&gt;</span>, ProjectionBasalGanglia<span class="placeholder">&lt;LABEL&gt;</span>, ProjectionBrainstem<span class="placeholder">&lt;LABEL&gt;</span>
</pre>  
</div>

<div id="bundle" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Label Values Legend Extended: DSIStudio <code>BUNDLE</code> Values</span>
  <a class="anchor-link" href="#bundle" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<tr><thead><th>&lt;BUNDLE&gt; Values</th><th>Nested Bundle &lt;LABEL&gt; Values</th></thead><tr>
<tbody>
<tr>
<td><strong style="color: #00a298ff;">Association&lt;LABEL&gt;</strong></td>
<td><div style="display: flex; flex-wrap: wrap; gap: 8px;"><span>Cingulum{L/R}</span><span>ExtremeCapsule{L/R}</span><span>FrontalAslantTract{L/R}</span><span>ParietalAslantTract{L/R}</span><span>HippocampusAlveus{L/R}</span><span>ArcuateFasciculus{L/R}</span><span>AssociationUncinateFasciculus{L/R}</span><span>InferiorFrontoOccipitalFasciculus{L/R}</span><span>InferiorLongitudinalFasciculus{L/R}</span><span>MiddleLongitudinalFasciculus{L/R}</span><span>SuperiorLongitudinalFasciculus{L/R}</span><span>VerticalOccipitalFasciculus{L/R}</span></div></td>
</tr>
<tr>
<td style="color: #00a298ff;"><strong>Cerebellum&lt;LABEL&gt;</strong></td>
<td><div style="display: flex; flex-wrap: wrap; gap: 8px;">
<span>Cerebellum{L/R}</span><span>InferiorCerebellarPeduncle{L/R}</span><span>MiddleCerebellarPeduncle</span><span>SuperiorCerebellarPeduncle</span><span>Vermis</span></div></td>
</tr>
<tr>
<td><strong style="color: #00a298ff;">Commissure&lt;LABEL&gt;</strong></td>
<td><div style="display: flex; flex-wrap: wrap; gap: 8px;"><span>AnteriorCommissure</span><span>CorpusCallosum</span></div></td>
</tr>
<tr>
<td><strong style="color: #00a298ff;">ProjectionBasalGanglia&lt;LABEL&gt;</strong></td>
<td><div style="display: flex; flex-wrap: wrap; gap: 8px;"><span>AcousticRadiation{L/R}</span><span>OpticRadiation{L/R}</span><span>ThalamicRadiation{L/R}</span><span>AnsaLenticularis{L/R}</span><span>FasciculusLenticularis{L/R}</span><span>AnsaSubthalamic{L/R}</span><span>FasciculusSubthalamicus{L/R}</span><span>CorticostriatalTract{L/R}</span><span>Fornix{L/R}</span></div></td>
</tr>
<tr>
<td><strong style="color: #00a298ff;">ProjectionBrainstem&lt;LABEL&gt;</strong></td>
<td><div style="display: flex; flex-wrap: wrap; gap: 8px;"><span>CorticobulbarTract{L/R}</span><span>CorticopontineTract{L/R}</span><span>CorticospinalTract{L/R}</span><span>ReticularTract{L/R}</span><span>DentatorubrothalamicTract{lr/rl}</span><span>NonDecussatingDentatorubrothalamicTract{L/R}</span><span>MedialForebrainBundle{L/R}</span><span>MedialLemniscus{L/R}</span></div></td>
</tr>
</tbody>
</table>
</div>

## dMRI Derivatives Quick Start Guide

The diffusion encoding provided via the multiple QSIRecon derivative folders enable the estimation of multiple diffusion MRI models to create the derived data, including:

#### Diffusion Tensor Imaging (DTI)        
DSI Studio models diffusion with a 3D Gaussian distribution of water displacements. Key outputs include fractional anisotropy (FA), i.e. anisotropic diffusion (typically higher in white matter bundles with dense, parallel fibers) and mean diffusivity (MD), i.e. directionally averaged apparent diffusion coefficient (inversely related to cellular membrane density) (<a href="https://doi.org/10.1016/S0006-3495(94)80775-1">Basser 1994</a>).     
<i class="fas fa-folder-tree header-icon"></i>**Derivatives**: <a href="#qsirecon">qsirecon-DSIStudio/</a>   

#### Diffusion Kurtosis Imaging (DKI)
DKI extends DTI to capture non-Gaussian diffusion. The main metric is mean kurtosis (MK), which is more sensitive to complex or restricted diffusion and often higher in dense white matter (<a href="https://doi.org/10.1002/mrm.20508">Jensen 2005</a>).      
<i class="fas fa-folder-tree header-icon"></i>**Derivatives**: <a href="#qsirecon">qsirecon-DIPYDKI/</a>                  

#### Mean Apparent Propagator MRI (MAP-MRI)
MAP-MRI Extends DTI by estimating the full spatial probability distribution (propagator) of water diffusion without assuming Gaussian distribution. This enables quantification of non-Gaussian diffusion and more accurate measures of directionality and anisotropy (<a href="https://doi.org/10.1016/j.neuroimage.2013.04.016">Özarslan 2013</a>).     
<i class="fas fa-folder-tree header-icon"></i>**Derivatives**: <a href="#qsirecon">qsirecon-TORTOISE_model-MAPMRI/</a>                  

<div id="mapmri-metrics" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-atom"></i></span>
  <span class="text-with-link">
  <span class="text">MAP-MRI Metrics</span>
  <a class="anchor-link" href="#mapmri-metrics" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead>  <tr>    <th>Metric</th>    <th>Description</th>  </tr></thead>
<tbody>
<tr><td>Propagator Anisotropy (PA)</td>
  <td style="word-wrap: break-word; white-space: normal;">Quantifies anisotropy by computing the dissimilarity of the full MAP-MRI propagator from its fully isotropic counterpart. More accurate than FA.</td>
</tr>
<tr><td>Non-Gaussianity (NG)</td>
  <td style="word-wrap: break-word; white-space: normal;">Quantifies deviation from Gaussian diffusion. <strong>NG</strong> measures overall deviation, <strong>NGpar</strong> along the primary diffusion axis (fiber direction in white matter), and <strong>NGperp</strong> perpendicular to it (often related to restriction).</td>
</tr>
<tr><td>Return To Origin Probability (RTOP)</td>
  <td style="word-wrap: break-word; white-space: normal;">Probability that a water molecule returns to its starting point. Low in unrestricted diffusion (large cells), high in restricted diffusion (small or impermeable cells). Inversely related to pore volume.</td>
</tr>
<tr><td>Return To Axis Probability (RTAP)</td>
 <td style="word-wrap: break-word; white-space: normal;">Probability that a water molecule returns to the principal diffusion axis (primary eigenvector).</td>
</tr>
<tr><td>Return To Plane Probability (RTPP)</td>
<td style="word-wrap: break-word; white-space: normal;">Reciprocal of mean cylinder length and inversely proportional to axial diffusivity; Related to diffusion taking place within coherently oriented cylinders.</td>
</tr>
</tbody>
</table>
</div>

<div id="model-param-details" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-atom"></i></span>
  <span class="text-with-link">
  <span class="text">QSIRecon Parametric Microstructure Maps Generated for HBCD</span>
  <a class="anchor-link" href="#model-param-details" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines" style="width: 100%; table-layout: fixed;">
<thead>
<tr>
<th>QSIRecon Workflow</th>
<th>Model (Shells)</th>
<th>Parameters</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<!-- DSI Studio -->
<tr>
<td rowspan="8"><b>DSI Studio</b></td>
<td rowspan="3"><b>gqi</b><br>(Full shells)</td>
<td>gfa</td><td>Generalized fractional anisotropy</td>
</tr>
<tr><td>iso</td><td>Isotropic diffusion component</td></tr>
<tr><td>qa</td><td>Quantitative anisotropy</td></tr>

<tr>
<td rowspan="5"><b>tensor</b><br>(Inner shells)</td>
<td>fa</td><td>Fractional anisotropy</td>
</tr>
<tr><td>ad / md / rd</td><td>Axial / Mean / Radial diffusivity</td></tr>
<tr><td>rd1 / rd2</td><td>Second and third eigenvalues (λ₂ / λ₃)</td></tr>
<tr><td>ha</td><td>Helix angle</td></tr>
<tr><td>txx / txy / txz / tyy / tyz / tzz</td><td>Diffusion tensor elements</td></tr>

<!-- DIPY DKI -->
<tr>
<td rowspan="4"><b>DIPY DKI</b></td>
<td rowspan="4"><b>dki</b><br>(Full shells)</td>
<td>ad / ak</td><td>Axial diffusivity / Axial kurtosis</td>
</tr>
<tr><td>fa / kfa</td><td>Fractional anisotropy / Kurtosis FA</td></tr>
<tr><td>md / mk / mkt</td><td>Mean diffusivity / Mean kurtosis / Mean kurtosis tensor</td></tr>
<tr><td>rd / rk</td><td>Radial diffusivity / Radial kurtosis</td></tr>

<!-- TORTOISE MAPMRI -->
<tr>
<td rowspan="7"><b>TORTOISE-<br>MAPMRI</b></td>
<td rowspan="4"><b>mapmri</b><br>(Full shells)</td>
<td>ng / ngpar / ngperp</td><td>Non-Gaussianity / Parallel NG / Perpendicular NG</td>
</tr>
<tr><td>fa / kfa</td><td>Fractional anisotropy / Kurtosis FA</td></tr>
<tr><td>pa / path</td><td>Propagator anisotropy / Thresholded PA</td></tr>
<tr><td>rtap / rtop / rtpp</td><td>Return-to-axis / origin / plane probability</td></tr>

<tr>
<td rowspan="3"><b>tensor</b><br>(Inner shells)</td>
<td>ad / rd</td><td>Axial / Radial diffusivity</td>
</tr>
<tr><td>am / fa</td><td>A0 (mean signal) / Fractional anisotropy</td></tr>
<tr><td>li</td><td>Lattice index</td></tr>

<!-- TORTOISE Tensor -->
<tr>
<td rowspan="5"><b>TORTOISE-<br>Tensor</b></td>
<td rowspan="5"><b>tensor</b><br>(Full shells)</td>
<td>ad / rd</td><td>Axial / Radial diffusivity</td>
</tr>
<tr><td>am / fa</td><td>A0 (mean signal) / Fractional anisotropy</td></tr>
<tr><td>li</td><td>Lattice index</td></tr>
</tbody>
</table>
</div>

## Quality Control Summary Statistics
<div id="dwi-qc" class="static-banner" style="border-left: 5px solid #199bd6;">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
    <span class="text">Automated QC for Processed Diffusion Data</span>
    <a class="anchor-link" href="#dwi-qc" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
</div>
<div class="table-static-content">
<p>Automated QC for processed diffusion data is fairly robust, with metrics provided in <code>sub-{ID}_ses-{V0X}_space-ACPC_desc-image_qc.tsv</code> within the QSIPrep derivatives (see <a href="https://qsiprep.readthedocs.io/en/latest/preprocessing.html#quality-control-data">QSIPrep documentation</a> for details). Below are distributions of automated QC metrics from HBCD visits V02 and V03. Higher Neighboring DWI Correlation (NDC; closer to 1) and Contrast-to-Noise Ratio (CNR) indicate better image quality. <strong>NDC can also be used as a covariate in analyses to account for QC variation.</strong></p>  
<p><strong>Left</strong>: NDC calculated pre- and post-processing for each vendor using combined AP/PA scans (solid = processed, dashed = raw).<br>  
<strong>Right</strong>: Shell-wise CNR per vendor, calculated by Eddy. Because all data shown passed preliminary QC, we do not provide exclusion threshold recommendations. However, NDC and CNR are useful covariates when analyzing other derivatives.</p>
<img src="../images/ndc_cnr_comparison.svg" width="95%" height="auto" class="center">
</div>

## References

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
    <p>Alexander AL, Lee JE, Lazar M, Field AS. (2007). Diffusion tensor imaging of the brain. <em>Neurotherapeutics</em>, 4(3):316-29. <a href="https://doi.org/10.1016/j.nurt.2007.05.011">10.1016/j.nurt.2007.05.011</a></p>
    <p>Basser PJ, Mattiello J, LeBihan D. (1994). MR diffusion tensor spectroscopy and imaging. <em>Biophys J.</em>, 66(1):259-67. <a href="https://doi.org/10.1016/S0006-3495(94)80775-1">10.1016/S0006-3495(94)80775-1</a></p>
    <p>Cieslak M, Cook PA, He X, Yeh FC, Dhollander T, Adebimpe A, Aguirre GK, Bassett DS, Betzel RF, Bourque J, Cabral LM, Davatzikos C, Detre JA, Earl E, Elliott MA, Fadnavis S, Fair DA, Foran W, Fotiadis P, Garyfallidis E, Giesbrecht B, Gur RC, Gur RE, Kelz MB, Keshavan A, Larsen BS, Luna B, Mackey AP, Milham MP, Oathes DJ, Perrone A, Pines AR, Roalf DR, Richie-Halford A, Rokem A, Sydnor VJ, Tapera TM, Tooley UA, Vettel JM, Yeatman JD, Grafton ST, Satterthwaite TD. (2021). QSIPrep: an integrative platform for preprocessing and reconstructing diffusion MRI data. <em>Nature Methods</em>, 18(7):775-778. <a href="https://doi.org/10.1038/s41592-021-01185-5">10.1038/s41592-021-01185-5</a></p>
    <p>Cieslak, M., Irfanoglu, M. O., Meisler, S. L., Salo, T., Raikes, A. C., Cook, P. A., Chung, A. W., Lee, E. G., Li, R., Li, X., Pecheva, D., Fair, D. A., Smyser, C. D., Harms, M. P., Landman, B. A., Wisnowski, J. L., Huang, H., Alexander, A. L., & Satterthwaite, T. D. (2025). Diffusion MRI processing in the HEALthy Brain and child development study: Innovations and applications. <em>In bioRxiv.</em> <a href="https://doi.org/10.1101/2025.11.10.687672">https://doi.org/10.1101/2025.11.10.687672</a></p>
    <p>Jensen, J. H., Helpern, J. A., Ramani, A., Lu, H., & Kaczynski, K. (2005). Diffusional kurtosis imaging: the quantification of non-gaussian water diffusion by means of magnetic resonance imaging. Magnetic Resonance in Medicine, 53(6), 1432–1440. <a href="https://doi.org/10.1002/mrm.20508">https://doi.org/10.1002/mrm.20508</a></p>
    <p>Özarslan E, Koay CG, Shepherd TM, Komlosh ME, İrfanoğlu MO, Pierpaoli C, Basser PJ. (2013). Mean apparent propagator (MAP) MRI: a novel diffusion imaging method for mapping tissue microstructure. <em>Neuroimage</em>, 78:16-32. <a href="https://doi.org/10.1016/j.neuroimage.2013.04.016">10.1016/j.neuroimage.2013.04.016</a></p>
</div>
</div>





<!-- <table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <tr>
    <th>Model</th>
    <th>Description</th>
    <th>Derivatives</th>
  </tr>
</thead>
<tbody>
<tr>
  <td><span class="tooltip">DTI<span class="tooltiptext">Diffusion Tensor Imaging</span></span></td>
  <td style="word-wrap: break-word; white-space: normal;">Models diffusion with a 3D Gaussian distribution of water displacements. Key outputs include Fractional Anisotropy (FA: anisotropic diffusion, typically higher in white matter bundles with dense, parallel fibers) and Mean Diffusivity (MD: the directionally averaged apparent diffusion coefficient, inversely related to cellular membrane density) (<a href="https://doi.org/10.1016/S0006-3495(94)80775-1">Basser 1994</a>).</td>
  <td><a href="#qsirecon-DSIStudio">qsirecon-<br>DSIStudio</a></td>
</tr>
<tr>
  <td><span class="tooltip">DKI<span class="tooltiptext">Diffusion Kurtosis Imaging</span></span></td>
  <td style="word-wrap: break-word; white-space: normal;">Extends DTI to capture non-Gaussian diffusion. Main metric: MK (mean kurtosis), which is more sensitive to complex or restricted diffusion and often higher in dense white matter (<a href="https://doi.org/10.1002/mrm.20508">Jensen 2005</a>).</td>
  <td><a href="#qsirecon-DIPYDKI">qsirecon-<br>DIPYDKI</a></td>
</tr>
<tr>
  <td><span class="tooltip">MAP-MRI<span class="tooltiptext">Mean Apparent Propagator MRI</span></span></td>
  <td style="word-wrap: break-word; white-space: normal;">Extends DTI by estimating the full spatial probability distribution (propagator) of water diffusion without assuming Gaussian distribution, enabling quantification of non-Gaussian diffusion and more accurate measures of directionality and anisotropy (<a href="https://doi.org/10.1016/j.neuroimage.2013.04.016">Özarslan 2013</a>). See <a href="#mapmri-metrics">MAP-MRI metrics</a>.</td>
  <td><a href="#qsirecon-TORTOISE">qsirecon-<br>TORTOISE_model-<br>MAPMRI</a></td>
</tr>
</tbody>
</table> -->
