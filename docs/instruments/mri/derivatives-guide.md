# Guide to Structural & Functional MRI Derivatives

This guide helps you navigate HBCD structural and resting-state functional MRI (rsfMRI) derivatives, identify their processing configurations, and locate files for analysis. Outputs include cortical morphology measures, cortical surfaces, denoised BOLD time series, and functional connectivity matrices. The release also includes dense and parcellated time series with at least 2.5 minutes of low-motion data, using an FD threshold of 0.3 mm for motion censoring.


<!-- ## Usable Data Requirements
 Before analysis:

- Check the usable data duration and motion characteristics for each run.
- Confirm the processing configuration, parcellation, and smoothing variant selected for your analysis. -->

<!-- Key derivatives, produced by the [XCP-D](https://xcp-d.readthedocs.io/en/latest/) pipeline, include volumetric and surface-based time series for each participant.  -->

## At A Glance

<table class="compact-table-no-vertical-lines">
<thead>
<tr><th>Analysis</th><th>Derivative</th><th>File Format</th></tr>
</thead>
<tbody>
<tr><td>Compare cortical curvature, sulcal depth, or thickness at individual vertices</td><td><a href="#cortical-metrics">Cortical metrics</a></td><td><code>.dscalar.nii</code></td></tr>
<tr><td>Compare regional averages of cortical measures</td><td><a href="#parcellated-structural-measures">Parcellated structural measures</a></td><td><code>.tsv</code></td></tr>
<tr><td>Visualize cortical anatomy or display surface overlays</td><td><a href="#cortical-surfaces">Cortical surfaces</a></td><td><code>.surf.gii</code></td></tr>
<tr><td>Analyze BOLD signals at individual cortical vertices or subcortical voxels</td><td><a href="#dense-time-series">Dense time series</a></td><td><code>.dtseries.nii</code></td></tr>
<tr><td>Analyze regional BOLD signals or calculate ROI-to-ROI connectivity</td><td><a href="#parcellated-time-series">Parcellated time series</a></td><td><code>.tsv</code>, <code>.ptseries.nii</code></td></tr>
<tr><td>Use precomputed ROI-to-ROI correlations</td><td><a href="#connectivity-matrices">Connectivity matrices</a></td><td><code>.tsv</code></td></tr>
<tr><td>Assess motion, censoring, or nuisance regressors</td><td><a href="#motion-and-confound-files">Motion and confound files</a></td><td><code>.tsv</code></td></tr>
</tbody>
</table>

## Processing Workflow

HBCD structural and functional MRI data are processed through a sequence of BIDS App pipelines:

<style>
.mri-workflow {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 2rem;
  list-style: none !important;
  margin: 1.25rem 0 !important;
  padding: 0 !important;
}
.mri-workflow > .mri-workflow-step {
  position: relative;
  list-style: none !important;
  margin: 0 !important;
  padding: 1rem;
  border: 2px solid;
  border-radius: 12px;
  color: #222;
}
.mri-workflow-step-1 { background: #dde6fe; border-color: #a9bffc !important; }
.mri-workflow-step-2 { background: #dcd8fb; border-color: #a89df9 !important; }
.mri-workflow-step-3 { background: #f0dcfb; border-color: #d794fc !important; }
.mri-workflow-name {
  display: inline-block;
  color: #212658 !important;
  font-size: 1.05em;
  font-weight: 700;
  text-decoration: underline;
  text-underline-offset: 3px;
}
.mri-workflow-name:focus-visible { outline: 2px solid #212658; outline-offset: 4px; }
.mri-workflow-step p {
  margin: 0.65rem 0 0;
  font-size: 0.9em;
  line-height: 1.5;
}
.mri-workflow-step:not(:last-child)::after {
  content: "";
  position: absolute;
  top: 50%;
  right: -1.4rem;
  width: 0.65rem;
  height: 0.65rem;
  border-top: 2px solid #626782;
  border-right: 2px solid #626782;
  transform: translateY(-50%) rotate(45deg);
}
@media (max-width: 800px) {
  .mri-workflow { grid-template-columns: 1fr; }
  .mri-workflow-step:not(:last-child)::after {
    top: auto;
    bottom: -1.35rem;
    right: auto;
    left: 50%;
    transform: translateX(-50%) rotate(135deg);
  }
}
</style>

<ol class="mri-workflow" aria-label="MRI processing pipeline sequence">
  <li class="mri-workflow-step mri-workflow-step-1">
    <a href="https://bibsnet.readthedocs.io/en/latest/" class="mri-workflow-name">BIBSNet</a>
    <p>Generates brain tissue segmentations and masks from T1w/T2w images for downstream preprocessing.</p>
  </li>
  <li class="mri-workflow-step mri-workflow-step-2">
    <a href="https://nibabies.readthedocs.io/en/latest/" class="mri-workflow-name">Infant fMRIPrep</a>
    <p>Performs anatomical and functional preprocessing, including surface reconstruction with M-CRIB-S or Infant FreeSurfer, registration, motion correction, and confound estimation.</p>
  </li>
  <li class="mri-workflow-step mri-workflow-step-3">
    <a href="https://xcp-d.readthedocs.io/en/latest/" class="mri-workflow-name">XCP-D</a>
    <p>Performs functional post-processing and denoising, summarizes data within parcellations, and generates connectivity and other summary measures.</p>
  </li>
</ol>

## Configurations & Folder Names

**Derivative folder and file names include hash IDs that identify the processing configuration.** For Infant fMRIPrep, the hashes distinguish the surface reconstruction method. Downstream XCP-D derivatives also include a hash identifying the XCP-D configuration.

<table class="table-no-vertical-lines">
<thead><tr><th>Pipeline</th><th>Configuration</th><th>Hash ID</th></tr></thead>
<tbody>
<tr><td>Infant fMRIPrep</td><td>M-CRIB-S surface reconstruction</td><td><code>d902942d</code></td></tr>
<tr><td>Infant fMRIPrep</td><td>Infant FreeSurfer surface reconstruction</td><td><code>364caa63</code></td></tr>
<tr><td>XCP-D</td><td>Fixed XCP-D processing configuration</td><td><code>7a4c379b</code></td></tr>
</tbody>
</table>

Use the Infant fMRIPrep hash to distinguish derivatives generated with M-CRIB-S from those generated with Infant FreeSurfer. The XCP-D hash is shared across the configurations described here because the XCP-D parameters were fixed. The processing workflows and corresponding derivative folder names are as follows:

<!-- Source diagram: https://canva.link/pndtkg25cdfer95 -->
<figure>
  <img src="../images/proc-hashes.svg" alt="MRI processing workflows and derivative folder names for the M-CRIB-S and Infant FreeSurfer configurations" width="100%">
</figure>

<!-- ## Reading the File Patterns

The patterns below show paths relative to a participant/session derivative directory:

- `anat/` contains anatomical derivatives; `func/` contains functional derivatives.
- `*` represents the filename prefix, including participant/session identifiers and any additional entities.
- `{PARC}` represents a [parcellation identifier](#parc).
- Braces containing alternatives, such as `{curv|sulc|thickness}`, indicate separate files for each listed measure.
- `{L|R}` identifies the left or right hemisphere; `{X}` represents a run number. -->

## Structural MRI Derivatives
##### Cortical Metrics
CIFTI scalar files contain curvature, sulcal depth, and cortical thickness values derived from reconstructed cortical surfaces and aligned to fsLR space.   
**Recommended for:** Vertex-wise cortical morphology analyses.      
**File pattern:** `anat/*_space-fsLR_den-91k_{curv|sulc|thickness}.dscalar.nii`

<table class="table-no-vertical-lines">
<thead><tr><th>Measure</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>curv</code></td><td>Curvature: characterizes cortical folding and shape.</td></tr>
<tr><td><code>sulc</code></td><td>Sulcal depth: describes the depth of cortical folds.</td></tr>
<tr><td><code>thickness</code></td><td>Cortical thickness: distance between the white matter and pial surfaces, measured in millimeters.</td></tr>
</tbody>
</table>

##### Cortical Surfaces
GIFTI files provide midthickness, pial, and white matter surface models for each hemisphere in fsLR space.    
**Recommended for:** Visualizing cortical anatomy, displaying structural metrics, or overlaying functional data.      
**File pattern:** `anat/*_hemi-{L|R}_space-fsLR_den-32k_{midthickness|pial|white}.surf.gii`

##### Parcellated Structural Measures
TSV files contain regional averages of curvature, sulcal depth, and cortical thickness within regions defined by a [parcellation atlas](#parc).   
**Recommended for:** ROI-level group comparisons, developmental modeling, and other analyses of regional cortical morphology.     
**File pattern:** `anat/*_space-fsLR_seg-{PARC}_stat-mean_desc-{curv|sulc|thickness}_morph.tsv`

## Functional MRI Derivatives
The files below support analyses of denoised resting-state BOLD signals and functional connectivity. Review [motion and confound files](#motion-and-confound-files) before selecting runs for analysis.

##### Dense Time Series
CIFTI dense time series contain preprocessed, temporally filtered, and nuisance-regressed BOLD signals. Each grayordinate represents a cortical surface vertex or subcortical voxel. The files combine cortical data aligned to fsLR space with subcortical volumetric data. The `denoised` and `denoisedSmoothed` file labels distinguish denoised outputs from denoised outputs with spatial smoothing.      
**Recommended for:** Analyses of BOLD signals at individual grayordinates, including seed-based connectivity and time series analyses.    
**File pattern:** `func/*_task-rest_space-fsLR_den-91k_desc-{denoised|denoisedSmoothed}_bold.dtseries.nii`    

##### Parcellated Time Series
These files contain the mean BOLD signal within each region of a [parcellation atlas](#parc). Outputs are available as TSV tables and CIFTI parcellated time series (`.ptseries.nii`), where rows represent time points and columns represent regions.      
**Recommended for:** ROI-to-ROI connectivity and network analyses using regional BOLD signals.      
**TSV file pattern:** `func/*_task-rest_space-fsLR_seg-{PARC}_stat-mean_timeseries.tsv`

##### Connectivity Matrices
TSV matrices contain pairwise Pearson correlations between atlas regions, calculated from parcellated time series using available low-motion data. Motion censoring uses a framewise displacement (FD) threshold of 0.3 mm.   
**Recommended for:** ROI-to-ROI connectivity analyses, network and graph analyses, and inspection of regional correlation patterns.     
**File pattern:** `func/*_task-rest_space-fsLR_seg-{PARC}_stat-pearsoncorrelation_relmat.tsv`

##### Other Functional Summary Measures
The release also includes regional homogeneity (ReHo) and amplitude of low-frequency fluctuation (ALFF) values. See the [XCP-D output documentation](https://xcp-d.readthedocs.io/en/latest/outputs.html) for descriptions of these measures.

##### Motion and Confound Files
Review motion and confound files to assess run quality and understand nuisance regression and censoring before group analyses.    
**File pattern:** `func/*_task-rest_dir-PA_run-{X}_{design|motion|outliers}.tsv`    
These files document motion estimates, nuisance regressors, and outlier volumes. Design files contain the regressors used for denoising; motion and outlier files support assessment of motion and censoring. See the [XCP-D documentation on quality control, framewise displacement, and confound files](https://xcp-d.readthedocs.io/en/latest/outputs.html#other-outputs-include-quality-control-framewise-displacement-and-confounds-files) for details.



##  Parcellations & Atlases
Parcellations define the regions used to summarize structural measures and BOLD time series. Their identifiers appear in the `seg-{PARC}` portion of derivative filenames. The table below summarizes the atlases described in this guide. See the [XCP-D parcellations and atlases documentation](https://xcp-d.readthedocs.io/en/latest/outputs.html#parcellations-and-atlases) for additional details.

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

<style>
.compact-table-clean {
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
  font-size: 0.95em;
}
.compact-table-clean th {
  text-align: left;
  font-weight: 600;
  padding: 0.55em 0.5em;
  border-bottom: 2px solid #e5e7eb;
}
.compact-table-clean td {
  padding: 0.55em 0.5em;
  vertical-align: top;
  overflow-wrap: anywhere;
}
.compact-table-clean tbody tr:not(:last-child) td {
  border-bottom: 1px solid #f0f0f0;
}
.compact-table-clean .atlas-type {
  font-weight: 600;
}
.compact-table-clean .atlas-details {
  color: #555;
  font-size: 0.9em;
  display: block;
  margin-top: 0.15em;
}
.compact-table-clean .atlas-use {
  display: inline-block;
  margin-top: 0.35em;
  font-size: 0.85em;
  color: #0f766e;
  background: #eef6f6;
  padding: 2px 6px;
  border-radius: 6px;
}
</style>