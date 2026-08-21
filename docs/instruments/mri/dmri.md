# Diffusion MRI (dMRI)

{{ alert_warning(instruments.dmri) }}
{{ data_warning(instruments.dmri) }}
{{ issues_banner() }}

---

<!-- ##### Overview & Acquisition -->
{{ instrument_description(instruments.dmri) }}

##### Diffusion Pulse Sequence Timings
{{ csv_table("diffusion_pulse_sequence_timing.csv") }}

## Processing 

{{ suppx(instruments.dmri, "1") }}

<!-- HARDCODED IMAGE -->

<table class="compact-table-no-vertical-lines"> 
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


## Derivatives

### QSIPrep

<pre class="folder-tree">hbcd/
└── derivatives/
    └── qsiprep/
        └── sub-[ID]/
            ├── log/
            └── ses-[V0X]/
                ├── anat/
                │   <span class="hashtag"># Transforms</span>
                │   ├── *_from-<span class="var">{ACPC_to-anat|anat_to-ACPC}</span>_mode-image_xfm.mat
                │   ├── *_from-<span class="var">{ACPC_to-MNIInfant+1|MNIInfant+1_to-ACPC}</span>_mode-image_xfm.h5
                │   ├── *_from-orig_to-anat_mode-image_xfm.txt
                │
                │   <span class="hashtag"># Structural outputs (ACPC space)</span>
                │   ├── *_space-ACPC_desc-preproc_T2w.nii.gz <span class="hashtag">(+JSON)</span>
                │   ├── *_space-ACPC_desc-<span class="var">{aseg_dseg|brain_mask}</span>.nii.gz
                │   └── *_space-ACPC_dseg.nii.gz
                │
                ├── dwi/
                │   <span class="hashtag"># QC & confounds</span>
                │   ├── *_desc-confounds_timeseries.tsv
                │   ├── *_desc-<span class="var">{image|pepolar}</span>_qc.tsv
                │   ├── *_space-ACPC_desc-slice_qc.json
                │
                │   <span class="hashtag"># Preprocessed data</span>
                │   ├── *_space-ACPC_desc-preproc_dwi.nii.gz <span class="hashtag">(+JSON)</span>
                │   ├── *_space-ACPC_desc-preproc_dwi.<span class="var">{bval|bvec|b|b_table.txt}</span>
                │   ├── *_space-ACPC_dwiref.nii.gz
                │
                │   <span class="hashtag"># Masks & maps</span>
                │   ├── *_space-ACPC_desc-brain_mask.nii.gz
                │   └── *_space-ACPC_model-eddy_stat-cnr_dwimap.nii.gz <span class="hashtag">(+JSON)</span>
                │
                ├── figures/
                └── sub-[ID]_ses-[V0X].html
<a href="../../../datacuration/overview/#filetrees"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a>
</pre>


### QSIRecon Details

##### Diffusion Tensor Imaging (DTI)        
DSI Studio models diffusion with a 3D Gaussian distribution of water displacements. Key outputs include fractional anisotropy (FA), i.e. anisotropic diffusion (typically higher in white matter bundles with dense, parallel fibers) and mean diffusivity (MD), i.e. directionally averaged apparent diffusion coefficient (inversely related to cellular membrane density) (<a href="https://doi.org/10.1016/S0006-3495(94)80775-1">Basser 1994</a>).
<pre class="folder-tree">
hbcd/
└── derivatives/
    ├── qsirecon-DSIStudio/
    │   └── sub-[ID]/
    │       └── ses-[V0X]/
    │           ├── dwi/
    │           │   ├── *_space-ACPC_bundles-DSIStudio_<span class="var">{scalar|tdi}</span>stats.tsv
    │           │   ├── *_space-ACPC_model-gqi_bundle-<span class="var">{BUNDLE}</span>_streamlines.tck.gz
    │           │   ├── *_space-ACPC_model-gqi_bundlestats.csv
    │           │   ├── *_space-ACPC_model-gqi_dwimap.fib.gz
    │           │   ├── *_space-ACPC_model-gqi_dwimap.fib.gz.icbm152_adult.map.gz
    │           │   ├── *_space-ACPC_model-gqi_param-<span class="var">{gfa|iso|qa}</span>_dwimap.nii.gz
    │           │   ├── *_space-<span class="var">{ACPC|MNIInfant+1}</span>_model-rdi_param-<span class="var">{rd1|rd2}</span>_dwimap.nii.gz
    │           │   └── *_space-<span class="var">{ACPC|MNIInfant+1}</span>_model-tensor_param-<span class="var">{DTI-PARAM}</span>_dwimap.nii.gz
    │           ├── figures/*
    │           └── sub-[ID]_ses-[V0X].html

<span class="var">DTI-PARAM</span>: ad, fa, ha, md, rd, txx, txy, txz, tyy, tyz, tzz
<span class="var">BUNDLE</span>: <a href="../dmri.html">see full list</a>
</pre>

##### Diffusion Kurtosis Imaging (DKI)
DKI extends DTI to capture non-Gaussian diffusion. The main metric is mean kurtosis (MK), which is more sensitive to complex or restricted diffusion and often higher in dense white matter (<a href="https://doi.org/10.1002/mrm.20508">Jensen 2005</a>).
<pre class="folder-tree">
    ├── qsirecon-DIPYDKI/
    │   └── sub-[ID]/
    │       └── ses-[V0X]/
    │           ├── dwi/
    │           │   # DIPY DKI
    │           │   ├── *_space-ACPC_bundles-DSIStudio_scalarstats.tsv
    │           │   ├── *_space-<span class="var">{ACPC|MNIInfant+1}</span>_model-dki_param-<span class="var">{DKI-PARAM}</span>_dwimap.nii.gz
    │           │   └── *_space-<span class="var">{ACPC|MNIInfant+1}</span>_model-tensor_param-fa_dwimap.nii.gz
    │           ├── figures/*
    │           └── sub-[ID]_ses-[V0X].html

<span class="var">DKI-PARAM</span>: ad, ak, kfa, md, mk, mkt, rd, rk
</pre>

##### Mean Apparent Propagator MRI (MAP-MRI)
MAP-MRI Extends DTI by estimating the full spatial probability distribution (propagator) of water diffusion without assuming Gaussian distribution. This enables quantification of non-Gaussian diffusion and more accurate measures of directionality and anisotropy (<a href="https://doi.org/10.1016/j.neuroimage.2013.04.016">Özarslan 2013</a>).
<pre class="folder-tree">
    ├── qsirecon-TORTOISE_model-MAPMRI/
    │   └── sub-[ID]/
    │       └── ses-[V0X]/
    │           ├── dwi/
    │           │   ├── *_space-ACPC_bundles-DSIStudio_scalarstats.tsv
    │           │   ├── *_space-<span class="var">{ACPC|MNIInfant+1}</span>_model-mapmri_param-<span class="var">{MAPMRI}</span>_dwimap.nii.gz
    │           │   └── *_space-<span class="var">{ACPC|MNIInfant+1}</span>_model-tensor_param-<span class="var">{TENSOR}</span>_dwimap.nii.gz
    │           ├── figures/*
    │           └── sub-[ID]_ses-[V0X].html

<span class="var">MAPMRI</span>: ng, ngpar, ngperp, pa, path, rtap, rtop, rtpp
</pre>

<table class="compact-table-no-vertical-lines">
<thead>  <tr>    <th>Metric</th>    <th>Description</th>  </tr></thead>
<tbody>
<tr><td>Propagator Anisotropy (PA)</td>
  <td>Quantifies anisotropy by computing the dissimilarity of the full MAP-MRI propagator from its fully isotropic counterpart. More accurate than FA.</td>
</tr>
<tr><td>Non-Gaussianity (NG)</td>
  <td>Quantifies deviation from Gaussian diffusion. <strong>NG</strong> measures overall deviation, <strong>NGpar</strong> along the primary diffusion axis (fiber direction in white matter), and <strong>NGperp</strong> perpendicular to it (often related to restriction).</td>
</tr>
<tr><td>Return To Origin Probability (RTOP)</td>
  <td>Probability that a water molecule returns to its starting point. Low in unrestricted diffusion (large cells), high in restricted diffusion (small or impermeable cells). Inversely related to pore volume.</td>
</tr>
<tr><td>Return To Axis Probability (RTAP)</td>
 <td>Probability that a water molecule returns to the principal diffusion axis (primary eigenvector).</td>
</tr>
<tr><td>Return To Plane Probability (RTPP)</td>
<td>Reciprocal of mean cylinder length and inversely proportional to axial diffusivity; Related to diffusion taking place within coherently oriented cylinders.</td>
</tr>
</tbody>
</table>

##### QSIRecon-TORTOISE Tensor

<pre class="folder-tree">
    └── qsirecon-TORTOISE_model-tensor/
        └── sub-[ID]/
            └── ses-[V0X]/
                └── dwi/
                    ├── *_space-ACPC_bundles-DSIStudio_scalarstats.tsv
                    └── *_space-MNIInfant+1_model-tensor_param-<span class="var">{TENSOR}</span>_dwimap.nii.g

<span class="var">TENSOR</span>: ad, am, fa, li, rd
</pre>


<div id="model-param-details" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-atom"></i></span>
  <span class="text-with-link">
  <span class="text">QSIRecon Parametric Microstructure Maps Generated for HBCD</span>
  <a class="anchor-link" href="#model-param-details" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="compact-table-no-vertical-lines">
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

---

## Quality Control Summary Statistics

{{ qc(instruments.dmri) }}

<img src="../images/ndc_cnr_comparison.svg" width="95%" height="auto" class="center">

---

{{ references(instruments.dmri) }}








<!-- Automated QC for processed diffusion data is fairly robust, with metrics provided in <code>sub-[ID]_ses-[V0X]_space-ACPC_desc-image_qc.tsv</code> within the QSIPrep derivatives (see <a href="https://qsiprep.readthedocs.io/en/latest/preprocessing.html#quality-control-data">QSIPrep documentation</a> for details). Below are distributions of automated QC metrics from HBCD visits V02 and V03. Higher Neighboring DWI Correlation (NDC; closer to 1) and Contrast-to-Noise Ratio (CNR) indicate better image quality. NDC can also be used as a covariate in analyses to account for QC variation. 
<p><strong>Left</strong>: NDC calculated pre- and post-processing for each vendor using combined AP/PA scans<br>  
<strong>Right</strong>: Shell-wise CNR calculated by Eddy. We do not provide exclusion threshold recommendations because all data passed preliminary QC. However, NDC and CNR are useful covariates when analyzing other derivatives.</p> -->
