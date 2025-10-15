# Overview & MR Protocols

HBCD includes a suite of **magnetic resonance imaging (MRI)** and **spectroscopy (MRS)** data measures acquired as part of a comprehensive pediatric neuroimaging protocol, meticulously designed to overcome technical challenges of imaging early in life. MR data are acquired during visits V02, V03, V04, and V06 across all 27 Study recruitment sites. MR modalities include the following - click to be directed to modality documentation pages:

<ul>
<li><a href="smri" target="_blank">Structural MRI (sMRI)</a></li>
<li><a href="fmri" target="_blank">Functional MRI (fMRI)</a></li>
<li><a href="dmri" target="_blank">Diffusion MRI (dMRI)</a></li>
<li><a href="qmri" target="_blank">Quantitative MRI (qMRI)</a></li>
<li><a href="mrs" target="_blank">Magnetic Resonance Spectroscopy (MRS)</a></li>
</ul>

## Release Data

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">This data has known issues - <a href="../../changelog/knownissues/#mr-runid" target="_blank">see details</a>.</span>
</div>
<p></p>

MRI and MRS release data include both **file-based** (raw and processed data files in modality-specific formats) and **tabulated** (instrument and derived data in a standardized table format) data.      
<i>See the <a href="../../datacuration/overview" target="_blank">Data Structure Overview</a> for a full explanation of these data types.</i>

- <i class="fa fa-hammer"></i> <a href="../../datacuration/file-based-data/#raw-bids" target="_blank">Raw BIDS</a> under subject- and session-specific <code>rawdata/</code> folders
- <i class="fas fa-cog"></i> <a href="../../datacuration/file-based-data/#derivatives" target="_blank">Derivatives</a> processed through MRI & MRS pipelines (see <a href="../processing" target="_blank">Processing Pipelines</a>)
- <i class="fas fa-table"></i> <a href="../../datacuration/phenotypes" target="_blank">Tabulated</a> data tables derived from pipeline derivatives - see full list of tables <a href="../#mri" target="_blank">here</a>

<pre class="folder-tree" style="font-size: 11px;">
hbcd/
|__ rawdata/ 
|   |__ phenotype/   <span class="hashtag"># Tabulated Data</span> 
|   |   |__ img_*   
|   |
|   |__ sub-<span class="label">{ID}</span>/    <span class="hashtag"># Raw BIDS (file-based data)</span>
|       |__ ses-<span class="label">{V0X}</span>/ 
|           |__ anat/
|           |__ dwi/
|           |__ fmap/
|           |__ func/
|           |__ mrs/
|
|__ derivatives/     <span class="hashtag"># Derivatives (file-based data)</span> 
    |__ bibsnet/
    |__ freesurfer/
    |__ mcribs/
    |__ mriqc/
    |__ nibabies/
    |__ qmri_postproc/
    |__ qsiprep/
    |__ qsirecon/
    |__ qsirecon-*/
    |__ symri/
    |__ xcp_d/
</pre>

## MRI Derivatives: Quick Start Guide

Below is a summary of key MRI derivatives used for **structural morphology** and resting-state functional MRI (rsfMRI) **functional connectivity** analyses. Key derivatives are produced by the **XCP-D** pipeline, which builds on BIBSNet and Infant-fMRIPrep outputs to produce fully preprocessed, denoised, and quality-assessed data. The full list of available XCP-D outputs are documented [here](../mri/fmri.md#xcpd). **Click to expand** sections below for details.

<div id="struc" class="table-banner" onclick="toggleCollapse(this)">
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
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>anat/*_space-fsLR_den-91k_<span style="color: teal;">&lt;curv|sulc|thickness&gt;</span>.dscalar.nii</code></i><br>
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
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>anat/*_space-fsLR_seg-<span style="color: teal;">&lt;PARC&gt;</span>_stat-mean_desc-<span style="color: teal;">&lt;curv|sulc|thickness&gt;</span>_morph.tsv</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Region-based (ROI-level) analyses such as group comparisons or developmental modeling.</p>
<p class="details">
Tabulated summaries of cortical metrics (curvature, sulcal depth, thickness) within anatomical regions defined by 
<a href="#parc">parcellation atlases</a>. These files provide regional averages for statistical modeling or visualization.
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Midthickness, Pial, and White Matter Surfaces</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>anat/*_hemi-<span style="color: teal;">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span style="color: teal;">&lt;midthickness|pial|white&gt;</span>.surf.gii</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Visualizing cortical anatomy or mapping functional data to anatomical space.</p>
<p class="details">
3D surface models representing the midthickness, gray–white matter boundary, and pial surfaces for each hemisphere.  
Useful for rendering structural data, computing surface-based metrics, or visualizing functional overlays.
</p>
</div>

<div id="fc" class="table-banner" onclick="toggleCollapse(this)">
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
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>func/*_task-rest_space-fsLR_den-91k_desc-<span style="color: teal;">&lt;denoised|denoisedSmoothed&gt;</span>_bold.dtseries.nii</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Voxelwise or seed-based FC analyses, timeseries analysis via sliding windows or markov chains, etc.</p>
<p class="details">
CIFTI dense time series containing fully preprocessed, temporally filtered, and nuisance-regressed BOLD data.
These files combine the left and right surfaces, aligned to the standard fsLR surface template, with the subcortical volume annotated by subcortical structure.
Each greyordinate (~96k total) represents a vertex or voxel with pre-processed resting-state functional MRI time-series.
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Parcellated Timeseries</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>func/*_task-rest_space-fsLR_seg-<span style="color: teal;">&lt;PARC&gt;</span>_stat-mean_timeseries.tsv</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> ROI-to-ROI connectivity or network analyses using mean BOLD signals per region.</p>
<p class="details">
Tabulated mean BOLD time series for each region in the 
<a href="#parc">parcellation atlases</a>.  
Also available as CIFTI <code>.ptseries.nii</code> files, where columns = regions and rows = timepoints.
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Connectivity Matrices</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>func/*_task-rest_space-fsLR_seg-<span style="color: teal;">&lt;PARC&gt;</span>_stat-pearsoncorrelation_relmat.tsv</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-star"></i> <b>Recommended for:</b> Quick inspection, validation, or as input to network and graph analyses.</p>
<p class="details">
Tab-delimited matrices of pairwise Pearson correlations between atlas regions, computed from parcellated time series using all available low-motion data (motion censored with a framewise displacement threshold of 0.3 mm). These matrices form the foundation for ROI-to-ROI connectivity analyses.
</p>
<p style="font-size: 1.1em; font-weight:bold; padding-bottom: 2px; padding-top: 12px; border-bottom: 1px solid #6b6b6b66;">Motion Detection and Confound Files</p>
<p class="recommended">
<i style="font-size: 0.9em;" class="fa-solid fa-folder-open"></i> <b>File:</b> <code>func/*_task-rest_dir-PA_run-{X}_<span style="color: teal;">&lt;design|motion|outliers&gt;</span>.tsv</code></i><br>
<i style="font-size: 0.9em;" class="fa-solid fa-triangle-exclamation"></i> <b>Required for:</b> Motion assessment and filtering low-quality data prior to group analyses.</p>
<p class="details">
Includes framewise displacement values and nuisance regressor design files.  
Design files contain one column per regressor (e.g., motion parameters, high-motion outlier volume indicators).  
See the <a href="https://xcp-d.readthedocs.io/en/latest/outputs.html#other-outputs-include-quality-control-framewise-displacement-and-confounds-files" target="_blank">XCP-D documentation</a> for details.
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

<div id="parc" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-book-atlas"></i></span>
  <span class="text-with-link">
  <span class="text">Parcellations</span>
  <a class="anchor-link" href="#parc" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><i>See <a href="https://xcp-d.readthedocs.io/en/latest/outputs.html#parcellations-and-atlases">Parcellations & Atlases</a> in the XCP-D documentation for more details.</i></p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Atlas</th>
  <th>Description</th>
  <th>Recommended Use</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Glasser</td>
  <td style="word-wrap: break-word; white-space: normal;">Population-level multimodal anatomical atlas (<a href="https://doi.org/10.1016/j.neuroimage.2013.04.127">Glasser et al., 2013</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Population-level structure and surface-based morphology.</td>
</tr>
<tr>
  <td>Gordon</td>
  <td style="word-wrap: break-word; white-space: normal;">333-ROI template from rs-fMRI boundary detection for 120 young adults with 14 minutes of data collected on average  (<a href="https://doi.org/10.1093/cercor/bhu239">Gordon et al., 2016</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Functional network mapping and group-level FC analyses.</td>
</tr>
<tr>
  <td>HCP</td>
  <td style="word-wrap: break-word; white-space: normal;">360-ROI atlas parcellated from combining task, rest, and diffusion MRI data of 210 young adults   (<a href="https://doi.org/10.1038/nature18933">Glasser et al., 2016</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Cross-modal structural-functional alignment.</td>
</tr>
<tr>
  <td>MIDB</td>
  <td style="word-wrap: break-word; white-space: normal;">Precision atlas derived from ABCD data, 75% probability threshold (<a href="https://doi.org/10.1038/s41593-024-01596-5">Hermosillo et al., 2024</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Individualized functional network mapping.</td>
</tr>
<tr>
  <td>Myers Labonte</td>
  <td style="word-wrap: break-word; white-space: normal;">Infant probabilistic atlas, 50% probability threshold (<a href="https://doi.org/10.1101/2023.11.10.566629">Meyers et al., 2023</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Infant individualized functional network mapping.</td>
</tr>
<tr>
  <td>Tian</td>
  <td style="word-wrap: break-word; white-space: normal;">Subcortical parcellation atlas (<a href="https://doi.org/10.1038/s41593-020-00711-6">Tian et al., 2020</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Subcortical connectivity analyses.</td>
</tr>
<tr>
  <td><span class="tooltip tooltip-right">4S<span class="tooltiptext">Schaefer Supplemented with Subcortical Structures</span></span> Atlas</td>
  <td style="word-wrap: break-word; white-space: normal;">Integrated multimodal atlas combining cortical, subcortical, and cerebellar structures (<a href="https://github.com/PennLINC/AtlasPack">AtlasPack</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Cross-modality alignment across XCP-D, QSIPrep, and ASLPrep outputs.</td>
</tr>
</tbody>
</table>
</div>
<p></p>

<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text">
    Additional Resources
  </span>
</div>
<div class="notification-static-content">
<p> 
<a href="../../../datacuration/file-based-data/#derivatives" target="_blank"><i style="font-size: 0.9em;" class="fa-solid fa-up-right-from-square"></i> HBCD Derivatives</a>: List of MRI pipeline derivatives with links to documentation<br>
<a href="fmri/#xcpd" target="_blank"><i style="font-size: 0.9em;" class="fa-solid fa-up-right-from-square"></i> fMRI Release Data (XCP-D)</a>: Overview of XCP-D derivatives included in the HBCD release<br>
<a href="https://hbcd-cbrain-processing.readthedocs.io/latest/tools/xcp_d.html"><i style="font-size: 0.9em;" class="fa-solid fa-up-right-from-square"></i> HBCD Processing Documentation (XCP-D)</a>: Pipeline parameters and configurations used for HBCD processing<br>
<a href="https://xcp-d.readthedocs.io/en/latest/outputs.html#outputs-of-xcp-d"><i style="font-size: 0.9em;" class="fa-solid fa-up-right-from-square"></i> Official XCP-D Documentation</a>: Comprehensive documentation of all XCP-D outputs
</p>
</div>

## MRI & MRS Protocols

See <a href="https://hbcdsequences.readthedocs.io"><b>HBCD Study MRI Protocols</b></a> for full MRI protocols, sequence installation, and operation instructions.


<br>