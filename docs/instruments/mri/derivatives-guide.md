# Guide to Structural & Functional MRI Derivatives

Below we highlight key information to introduce you to the structural and functional pipeline derivatives.

## Multistep Processing Workflow

HBCD structural and functional MRI data are processed through a sequence of BIDS App pipelines. At a high level, **BIBSNet** generates brain tissue segmentations and masks for T1w/T2w images. These are fed into **Infant-fMRIPrep** to generate confound files and motion-corrected data (in MNI space, registered to age-specific volumetric atlases) as well as fs_LR32k surface space. Outputs are then fed into **XCP-D** to run nuisance regression/denoising, parcellate the fMRI data, and compute summary measures.

<style> .pipeline-step { transition: all 0.25s ease; } 
.pipeline-step:hover { transform: translateY(-3px); box-shadow: 0 4px 10px rgba(100, 100, 255, 0.2); } 
</style>
<div style="display: flex; align-items: center; justify-content: center; gap: 16px; flex-wrap: wrap; font-size: 0.95em;"> <div style="text-align: center;"> <a href="https://bibsnet.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #a9bffcff; border-radius: 12px; background-color: #dde6fe; color: #222;"> <strong>BIBSNet</strong><br> <small>Brain segmentations & masks</small> </div> </a> </div> <span style="font-size: 20px;"><i class="fa-solid fa-arrow-right"></i></span> <div style="text-align: center;"> <a href="https://nibabies.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #a89df9ff; border-radius: 12px; background-color: #dcd8fb; color: #222;"> <strong>Infant-fMRIPrep</strong><br> <strong>(Includes M-CRIB-S/Infant FreeSurfer)</strong><br><small>Surface reconstruction, preprocessing & confounds</small> </div> </a> </div> <span style="font-size: 20px;"><i class="fa-solid fa-arrow-right"></i></span> <div style="text-align: center;"> <a href="https://xcp-d.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #d794fcff; border-radius: 12px; background-color: #f0dcfb; color: #222;"> <strong>XCP-D</strong><br> <small>Post-processing & denoising</small> </div> </a> </div> </div>


## Hashes

Infant fMRIPrep and XCP-D derivative folder/filenames include unique hash IDs to indicate distinct processing parameters used for a given pipeline. In the case of HBCD data, the hash IDs correspond to which surface reconstruction method was used for processing within Infant fMRIPrep.

Downstream XCP-D derivatives include a second hash ID (`0ef9c88a`) indicating the XCP-D processing configuration. This value is identical for all HBCD data because the XCP-D parameters were fixed. Below we summarize the processing workflows and resulting derivative folder names. 
<p align="center">
  <img src="../images/proc-hashes.png" alt="Detailed MRI Processing Workflow">
</p>


## Derivatives Highlight

Below is a summary of key MRI derivatives used for structural morphology and resting-state functional MRI (rsfMRI) functional connectivity analyses. Key derivatives, produced by the [XCP-D](https://xcp-d.readthedocs.io/en/latest/) pipeline, include volumetric and surface-based time series for each participant. The data release also includes dense and parcellated time series with at least 2.5 minutes of low-motion data (FD>0.3), functional connectivity matrices, regional homogeneity values, and amplitude of low-frequency fluctuation values. 


<div id="struc" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-cubes"></i></span>
  <span class="text-with-link">
  <span class="text">Structural Morphology: Key Derivatives for Analysis</span>
  <a class="anchor-link" href="#struc" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; border-bottom: 1px solid #6b6b6b66;">Curvature, Sulcal Depth, & Cortical Thickness</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>anat/*_space-fsLR_den-91k_<span style="color: teal;">{curv|sulc|thickness}</span>.dscalar.nii</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Vertex-wise cortical morphology analyses (e.g., folding, curvature, thickness comparisons).</p>
<p class="details">
These CIFTI scalar files contain surface-based structural metrics derived from reconstructed L/R cortical surfaces, aligned to the fsLR template (~64k vertices per hemisphere).  
<ul style="margin-top: 0; font-size: 0.9em;">
<li><b>Curvature</b>: Characterizes cortical folding and morphology; often used as a covariate in morphometric analyses.</li>
<li><b>Sulcal depth</b>: Complements curvature to describe cortical shape and folding complexity.</li>
<li><b>Cortical thickness</b>: Distance between pial and white matter surfaces (mm); typically averaged within ROIs or compared across participants to study development, aging, or group effects.</li>
</ul>
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; border-bottom: 1px solid #6b6b6b66;">Parcellated Structural Measures</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>anat/*_space-fsLR_seg-<span style="color: teal;">{PARC}</span>_stat-mean_desc-<span style="color: teal;">{curv|sulc|thickness}</span>_morph.tsv</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Region-based (ROI-level) analyses such as group comparisons or developmental modeling.</p>
<p class="details">
Tabulated summaries of cortical metrics (curvature, sulcal depth, thickness) within anatomical regions defined by 
<a href="#parc">parcellation atlases</a>. These files provide regional averages for statistical modeling or visualization.
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Midthickness, Pial, and White Matter Surfaces</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>anat/*_hemi-<span style="color: teal;">{L|R}</span>_space-fsLR_den-32k_<span style="color: teal;">{midthickness|pial|white}</span>.surf.gii</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Visualizing cortical anatomy or mapping functional data to anatomical space.</p>
<p class="details">
3D surface models representing the midthickness, gray–white matter boundary, and pial surfaces for each hemisphere.  
Useful for rendering structural data, computing surface-based metrics, or visualizing functional overlays.
</p>
</div>

<div id="fc" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-globe"></i></span>
  <span class="text-with-link">
  <span class="text">Functional Connectivity: Key Derivatives for Analysis</span>
  <a class="anchor-link" href="#fc" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px;  padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Dense Timeseries</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>func/*_task-rest_space-fsLR_den-91k_desc-<span style="color: teal;">{denoised|denoisedSmoothed}</span>_bold.dtseries.nii</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Voxelwise or seed-based FC analyses, timeseries analysis via sliding windows or markov chains, etc.</p>
<p class="details">
CIFTI dense time series containing fully preprocessed, temporally filtered, and nuisance-regressed BOLD data.
These files combine the left and right surfaces, aligned to the standard fsLR surface template, with the subcortical volume annotated by subcortical structure.
Each greyordinate (~96k total) represents a vertex or voxel with pre-processed resting-state functional MRI time-series.
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Parcellated Timeseries</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>func/*_task-rest_space-fsLR_seg-<span style="color: teal;">{PARC}</span>_stat-mean_timeseries.tsv</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> ROI-to-ROI connectivity or network analyses using mean BOLD signals per region.</p>
<p class="details">
Tabulated mean BOLD time series for each region in the 
<a href="#parc">parcellation atlases</a>.  
Also available as CIFTI <code>.ptseries.nii</code> files, where columns = regions and rows = timepoints.
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Connectivity Matrices</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>func/*_task-rest_space-fsLR_seg-<span style="color: teal;">{PARC}</span>_stat-pearsoncorrelation_relmat.tsv</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Quick inspection, validation, or as input to network and graph analyses.</p>
<p class="details">
Tab-delimited matrices of pairwise Pearson correlations between atlas regions, computed from parcellated time series using all available low-motion data (motion censored with a framewise displacement threshold of 0.3 mm). These matrices form the foundation for ROI-to-ROI connectivity analyses.
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Motion Detection and Confound Files</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>func/*_task-rest_dir-PA_run-{X}_<span style="color: teal;">{design|motion|outliers}</span>.tsv</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-triangle-exclamation"></i> <b>Required for:</b> Motion assessment and filtering low-quality data prior to group analyses.</p>
<p class="details">
Includes framewise displacement values and nuisance regressor design files.  
Design files contain one column per regressor (e.g., motion parameters, high-motion outlier volume indicators).  
See the <a href="https://xcp-d.readthedocs.io/en/latest/outputs.html#other-outputs-include-quality-control-framewise-displacement-and-confounds-files">XCP-D documentation</a> for details.
</p>
</div>
<style>
.filename {
  background-color: #f8f9fa;
  border: 1px solid #e1e4e8;
  border-radius: 6px;
  padding: 6px 10px;
  font-family: monospace;
  font-size: 0.95em;
  margin-bottom: 6px;
  overflow-x: auto;
}
.recommended {
  background-color: #eef6ff;
  padding: 6px 10px;
  font-size: 0.9em;
  border-radius: 4px;
  margin: 4px 0 10px;
}
.details {
  margin-top: 0;
  font-size: 0.95em;
  color: #333;
}
</style>

<div id="parc" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-book-atlas"></i></span>
  <span class="text-with-link">
  <span class="text">Parcellations</span>
  <a class="anchor-link" href="#parc" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><i>See <a href="https://xcp-d.readthedocs.io/en/latest/outputs.html#parcellations-and-atlases">Parcellations & Atlases</a> in the XCP-D documentation for more details.</i></p>


<style>
    .compact-table-clean {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
}

.compact-table-clean th {
  text-align: left;
  font-weight: 600;
  padding: 0.6em 0.5em;
  border-bottom: 2px solid #e5e7eb;
}

.compact-table-clean td {
  padding: 0.65em 0.5em;
  vertical-align: top;
  word-break: break-word;
}

.compact-table-clean tr:not(:last-child) td {
  border-bottom: 1px solid #f0f0f0;
}

.compact-table-clean code {
  font-weight: 600;
  font-size: 0.95em;
}

.atlas-type {
  font-weight: 600;
}

.atlas-details {
  color: #6b7280;
  font-size: 0.85em;
  display: block;
  margin-top: 0.15em;
}

.atlas-use {
  display: inline-block;
  margin-top: 0.35em;
  font-size: 0.8em;
  color: #0f766e;
  background: #eef6f6;
  padding: 2px 6px;
  border-radius: 6px;
}
</style>
<table class="compact-table-clean">
<thead>
<tr>
  <th>Atlas</th>
  <th>Description</th>
</tr>
</thead>
<tbody>

<tr>
  <td><code>Glasser</code></td>
  <td>
    <span class="atlas-type">Multimodal anatomical atlas (population-level)</span>
    <span class="atlas-details">
      Derived from multimodal MRI data (<a href="https://doi.org/10.1038/nature18933">Glasser et al., 2016</a>)
    </span>
    <span class="atlas-use">Surface-based morphology, population-level structure</span>
  </td>
</tr>
<tr>
  <td><code>Gordon</code></td>
  <td>
    <span class="atlas-type">Functional atlas (333 ROIs)</span>
    <span class="atlas-details">
      rs-fMRI boundary detection (120 young adults, ~14 min per subject;
      <a href="https://doi.org/10.1093/cercor/bhu239">Gordon et al., 2016</a>)
    </span>
    <span class="atlas-use">Functional network mapping, group-level FC analyses</span>
  </td>
</tr>
<tr>
  <td><code>HCP</code></td>
  <td>
    <span class="atlas-type">Multimodal cortical atlas (360 ROIs)</span>
    <span class="atlas-details">
      Combined task, resting-state, and diffusion MRI (210 young adults;
      <a href="https://doi.org/10.1016/j.neuroimage.2013.04.127">Glasser et al., 2013</a>)
    </span>
    <span class="atlas-use">Cross-modal structural–functional alignment</span>
  </td>
</tr>
<tr>
  <td><code>MIDB</code></td>
  <td>
    <span class="atlas-type">Precision functional atlas (individualized)</span>
    <span class="atlas-details">
      Derived from ABCD data using a 75% probability threshold
      (<a href="https://doi.org/10.1038/s41593-024-01596-5">Hermosillo et al., 2024</a>)
    </span>
    <span class="atlas-use">Individualized functional network mapping</span>
  </td>
</tr>
<tr>
  <td><code>Myers-Labonte</code></td>
  <td>
    <span class="atlas-type">Infant probabilistic functional atlas</span>
    <span class="atlas-details">
      50% probability threshold; infant population
      (<a href="https://doi.org/10.1101/2023.11.10.566629">Myers et al., 2023</a>)
    </span>
    <span class="atlas-use">Infant functional network mapping</span>
  </td>
</tr>
<tr>
  <td><code>Tian</code></td>
  <td>
    <span class="atlas-type">Subcortical parcellation atlas</span>
    <span class="atlas-details">
      High-resolution subcortical segmentation
      (<a href="https://doi.org/10.1038/s41593-020-00711-6">Tian et al., 2020</a>)
    </span>
    <span class="atlas-use">Subcortical connectivity analyses</span>
  </td>
</tr>
<tr>
  <td><code>4S{X}56Parcels</code></td>
  <td>
    <span class="atlas-type">Multimodal atlas (multi-resolution)</span>
    <span class="atlas-details">
      Schaefer cortical parcellations (100–1000 parcels) supplemented with subcortical and cerebellar regions
      (<a href="https://github.com/PennLINC/AtlasPack">AtlasPack</a>)
    </span>
    <span class="atlas-use">Cross-modality alignment across XCP-D, QSIPrep, and ASLPrep</span>
  </td>
</tr>
</tbody>
</table>
</div>

## Postprocessing Outputs

Copy documentation we wrote for ABCD - https://docs.abcdstudy.org/latest/documentation/imaging/abcc_postproc.html


### ModelArray

<span class="subtle">Mass-univariate statistical modeling for large neuroimaging datasets</span>

Release data include [ModelArrayIO](https://modelarrayio.readthedocs.io/en/latest/) outputs (HDF/CSV) for efficient voxel-wise statistical modeling with the ModelArray R package. The release includes ModelArray ouputs for XCP-D, including connectivity, ALFF, ReHo, and morphometrics.