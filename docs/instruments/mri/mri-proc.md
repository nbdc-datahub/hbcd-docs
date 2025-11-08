# MRI Processing & Derivatives Guide

Below we describe the processing streams for structural and functional MRI, which are more involved and include multiple pipelines. For a high-level overview of processing across modalities, see <a href="../../processing/">HBCD Processing Pipelines</a>.

## Structural and Functional MRI Processing

HBCD **structural and functional MRI** data are processed through a standardized sequence of BIDS App pipelines. Each pipeline builds on the derivatives from the previous step, as outlined below. Visit the external [HBCD Processing](https://hbcd-cbrain-processing.readthedocs.io/latest/tool_details.html#tool-names) website for full details on parameters and configurations used for each pipeline.

<style> .pipeline-step { transition: all 0.25s ease; } .pipeline-step:hover { transform: translateY(-3px); box-shadow: 0 4px 10px rgba(100, 100, 255, 0.2); } </style> <div style="display: flex; align-items: center; justify-content: center; gap: 16px; flex-wrap: wrap; font-size: 0.95em;"> <div style="text-align: center;"> <a href="https://bibsnet.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #a9bffcff; border-radius: 12px; background-color: #dde6fe; color: #222;"> <strong>BIBSNet</strong><br> <small>Segmentation & masks</small> </div> </a> </div> <span style="font-size: 20px;"><i class="fa-solid fa-arrow-right"></i></span> <div style="text-align: center;"> <a href="https://nibabies.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #a89df9ff; border-radius: 12px; background-color: #dcd8fb; color: #222;"> <strong>Infant-fMRIPrep</strong><br> <small><i>Surface reconstruction, preprocessing & confounds</i></small> </div> </a> </div> <span style="font-size: 20px;"><i class="fa-solid fa-arrow-right"></i></span> <div style="text-align: center;"> <a href="https://xcp-d.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #d794fcff; border-radius: 12px; background-color: #f0dcfb; color: #222;"> <strong>XCP-D</strong><br> <small>Post-processing & denoising</small> </div> </a> </div> </div>

In brief, BIBSNet performs preprocessing on structural T1w/T2w images to generate brain tissue segmentations and masks. These are fed into Infant-fMRIPrep, which produces minimally pre-processed outputs including confound files (with motion parameters, average signals for ROIs like CSF, etc.) and motion-corrected data in age-specific MNI volumetric atlas as well as fs_LR32k surface space. From these outputs, the XCP-D pipeline runs nuisance regression/denoising, parcellates the fMRI data, and computes summary measures.

*Click to expand the following sections for further processing details:*

<div id="bibsnet-proc" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa-solid fa-diagram-project"></i></span>
<span class="text-with-link">
<span class="text">BIBSNet Processing Overview</span>
<a class="anchor-link" href="#bibsnet-proc" title="Copy link">
<i class="fa-solid fa-link"></i></a></span>
<span class="arrow">▸</span></div>
<div class="table-collapsible-content">
<p>BIBSNet is a deep learning model optimized for infant MRI brain tissue segmentation (<a href="https://doi.org/10.1101/2023.03.22.533696">Hendrickson et al. 2024</a>). The <a href="https://bibsnet.readthedocs.io/en/latest/">BIBSNet pipeline</a> generates native-space brain segmentations and brain masks (as well as ROI volume statistics), which are fed into Infant fMRIPrep for use in anatomical preprocessing and surface reconstruction.</p>
</div>

<div id="nibabies" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa-solid fa-diagram-project"></i></span>
<span class="text-with-link"><span class="text">Infant fMRIPrep Processing Overview</span>
<a class="anchor-link" href="#nibabies" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
<span class="arrow">▸</span></div>
<div class="table-collapsible-content">
<p>
  <a href="https://nibabies.readthedocs.io/en/latest/">Infant-fMRIPrep</a> adapts 
  <em>fMRIPrep</em> for infant data using age-appropriate templates and two surface 
  reconstruction methods optimized for early development.
</p>
<p><b>Anatomical Processing</b><br>
  T1w and T2w images are denoised, bias-corrected, and normalized to the MNI Infant 
  template (0–4.5 yr), then to MNI152 for compatibility with adult datasets. Surface 
  reconstruction is performed via:
</p>
<ul>
  <li><b>M-CRIB-S</b>: T2w-based method with modified <code>MCRIBReconAll</code> workflow. Uses pre-computed anatomical segmentation from BIBSNet.</li>
  <li><b>Infant FreeSurfer</b>: T1w-based method that runs <code>infant_recon_all</code>.</li>
</ul>
<p><b>Functional Processing</b></p>
<ul>
  <li>Motion and distortion correction using fieldmap-based estimation.</li>
  <li>Alignment of functional to anatomical space via boundary-based registration.</li>
  <li>Confound estimation: framewise displacement (FD) and DVARS for motion, CompCor physiological noise regressors, global signals (mean CSF, white matter, and whole brain), and derived regressors (e.g. motion outlier flags for frames exceeding 0.5 mm FD or 1.5 standardized DVARS thresholds)</li>
  <li>Resampling of BOLD data to subject and fsLR-space surfaces, with grayordinates (91k) for surface-based analyses.</li>
</ul>
</div>

<div id="xcpd" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa-solid fa-diagram-project"></i></span>
<span class="text-with-link"><span class="text">XCP-D Processing Overview</span>
<a class="anchor-link" href="#xcpd" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
<span class="arrow">▸</span></div>
<div class="table-collapsible-content">
<p><a href="https://xcp-d.readthedocs.io/en/latest/">XCP-D</a> is used for post-processing of Infant fMRIPrep outputs, producing cleaned and parcellated data ready for analysis. Atlases used for parcellation are described under <a href="../../mri/#parc">MRI Derivatives: Quickstart Guide</a>.</p>
<p><b>Anatomical Processing</b><br>
Native-space T2w images are transformed into standard MNI152NLin6Asym space (1 mm³ resolution).
Morphometric surfaces (fsLR-space) from Infant fMRIPrep are copied to the XCP-D derivatives. HCP-style midthickness, inflated, and very-inflated surfaces are generated from the white-matter and pial surface meshes and mapped to fsLR space.</p> 
<p><b>Functional Processing</b><br>
For each BOLD run, XCP-D performs a series of cleanup and quality-control steps:</p>
<ul>
<li>First 4 volumes (dummy scans) are removed.</li>
<li>Motion correction: Framewise displacement (FD) is calculated per Power et al. (2014); volumes with FD &gt; 0.3 mm flagged as high-motion outliers.</li>
<li>Nuisance regression: 36 confound regressors (motion, tissue, and global signals plus derivatives) regressed out following the 36P strategy.</li>
<li>Despiking and filtering: Data despiked, temporally filtered (0.01–0.08 Hz), and smoothed (6 mm FWHM).</li>
<li>Censoring: High-motion volumes are interpolated and later censored to minimize motion artifacts.</li>
<li>Amplitude of Low-Frequency Fluctuations (ALFF) and Regional Homogeneity (ReHo) metrics computed from cleaned data.</li> 
<li>Parcellated time series are extracted for <a href="../mri/index.md#parc">each atlas</a> and pairwise functional connectivity is calculated as the Pearson correlation between regional time series.</li>
<li>Postprocessed derivatives are concatenated across runs.</li>
</ul>
</div>

## Dual Surface Reconstruction Methods
Unique hash IDs in the Infant fMRIPrep and XCP-D derivative folder and filenames are used to distinguish processing methods. These correspond to dual Infant fMRIPrep surface reconstruction methods (hash ID `0f306a2f` vs. `2afa9081`), followed by XCP-D processing (hash ID `0ef9c88a`). Full details are available on the HBCD Processing site (see [here](https://hbcd-cbrain-processing.readthedocs.io/release_2.0_dev2/tool_details.html)).

<table class="compact-table-no-vertical-lines">
<b>Surface Reconstruction Methods</b>
<thead> <tr> <th>Method</th> <th>Hash ID</th> <th>Description</th> </tr> </thead>
<tbody>
<tr>
<td>M-CRIB-S</td>
<td><a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0_dev2/tools/nibabies_25.2.0-0f306a2f.html">0f306a2f</a></td>
<td>T2w-based method optimized for neonates (<a href="https://doi.org/10.1038/s41598-020-61326-2">Adamson et al., 2020</a>). <i>Optimal ages: ≤ 5 months<b>*</b></i>.</td>
</tr> <tr>
<td>Infant FreeSurfer</td>
<td><a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0_dev2/tools/nibabies_25.2.0-2afa9081.html">2afa9081</a></td> <td>T1w-based, optimized for infants 0-2 years old (<a href="https://doi.org/10.1016/j.neuroimage.2020.116946">Zöllei et al., 2020</a>). <i>Optimal ages: ≥ 3 months<b>*</b></i></td>
</tr> </tbody>
<tfoot>
<tr>
  <td colspan="3" style="word-wrap: break-word; white-space: normal; border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
    <b>*</b> Optimal age ranges based on <a href="https://doi.org/10.1101/2025.05.14.654069">Goncalves et al., 2025</a>.
  </td>
</tr>
</tfoot>
</table>

## MRI Derivatives Quick Start Guide

Below is a summary of key MRI derivatives used for **structural morphology** and **resting-state functional MRI (rsfMRI) functional connectivity** analyses. Key derivatives are produced by the **XCP-D** pipeline, which builds on BIBSNet and Infant-fMRIPrep outputs to produce fully preprocessed, denoised, and quality-assessed data. See <a href="../fmri/#xcpd" target="_blank">XCP-D derivatives included in the HBCD release</a>.

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
  <td style="word-wrap: break-word; white-space: normal;">Population-level multimodal anatomical atlas (<a href="https://doi.org/10.1038/nature18933">Glasser et al., 2016</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Population-level structure and surface-based morphology.</td>
</tr>
<tr>
  <td>Gordon</td>
  <td style="word-wrap: break-word; white-space: normal;">333-ROI template from rs-fMRI boundary detection for 120 young adults with 14 minutes of data collected on average  (<a href="https://doi.org/10.1093/cercor/bhu239">Gordon et al., 2016</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Functional network mapping and group-level FC analyses.</td>
</tr>
<tr>
  <td>HCP</td>
  <td style="word-wrap: break-word; white-space: normal;">360-ROI atlas parcellated from combining task, rest, and diffusion MRI data of 210 young adults (<a href="https://doi.org/10.1016/j.neuroimage.2013.04.127">Glasser et al., 2013</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Cross-modal structural-functional alignment.</td>
</tr>
<tr>
  <td>MIDB</td>
  <td style="word-wrap: break-word; white-space: normal;">Precision atlas derived from ABCD data, 75% probability threshold (<a href="https://doi.org/10.1038/s41593-024-01596-5">Hermosillo et al., 2024</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Individualized functional network mapping.</td>
</tr>
<tr>
  <td>Myers-Labonte</td>
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
  <td style="word-wrap: break-word; white-space: normal;">Integrated multimodal atlas combining cortical (at ten resolutions, 100-1000 parcels), subcortical, and cerebellar structures (<a href="https://github.com/PennLINC/AtlasPack">AtlasPack</a>).</td>
  <td style="word-wrap: break-word; white-space: normal;">Cross-modality alignment across XCP-D, QSIPrep, and ASLPrep outputs.</td>
</tr>
</tbody>
</table>
</div>

## References
<div class="references">
<p>Adamson, C. L., Alexander, B., Ball, G., Beare, R., Cheong, J. L. Y., Spittle, A. J., Doyle, L. W., Anderson, P. J., Seal, M. L., & Thompson, D. K. (2020). Parcellation of the neonatal cortex using Surface-based Melbourne Children’s Regional Infant Brain atlases (M-CRIB-S). <em>Scientific Reports</em>, 10(1), 4359. <a href="https://doi.org/10.1038/s41598-020-61326-2">https://doi.org/10.1038/s41598-020-61326-2</a></p>
<p>Goncalves, M., Moser, J., Madison, T. J., McCollum, R., Lundquist, J. T., Fayzullobekova, B., Hadera, L., Pham, H. H. N., Moore, L. A., Houghton, A., Conan, G., Styner, M. A., Alexopoulos, D., Smyser, C. D., Stoyell, S. M., Koirala, S., Nelson, S. M., Weldon, K. B., Lee, E., … Fair, D. A. (2025). FMRIPrep Lifespan: Extending A robust pipeline for functional MRI preprocessing to developmental neuroimaging. <em>In bioRxivorg.</em> <a href="https://doi.org/10.1101/2025.05.14.654069">https://doi.org/10.1101/2025.05.14.654069</a></p>
<p>Hendrickson, T. J., Reiners, P., Moore, L. A., Lundquist, J. T., Fayzullobekova, B., Perrone, A. J., Lee, E. G., Moser, J., Day, T. K. M., Alexopoulos, D., Styner, M., Kardan, O., Chamberlain, T. A., Mummaneni, A., Caldas, H. A., Bower, B., Stoyell, S., Martin, T., Sung, S., … Feczko, E. (2024). BIBSNet: A deep learning Baby image brain segmentation network for MRI scans. <em>In bioRxivorg</em>. <a href="https://doi.org/10.1101/2023.03.22.533696">https://doi.org/10.1101/2023.03.22.533696</a></p>
<p>Zöllei, L., Iglesias, J. E., Ou, Y., Grant, P. E., & Fischl, B. (2020). Infant FreeSurfer: An automated segmentation and surface extraction pipeline for T1-weighted neuroimaging data of infants 0-2 years. <em>NeuroImage</em>, 218(116946), 116946. <a href="https://doi.org/10.1016/j.neuroimage.2020.116946">https://doi.org/10.1016/j.neuroimage.2020.116946</a></p>
</div>
 
