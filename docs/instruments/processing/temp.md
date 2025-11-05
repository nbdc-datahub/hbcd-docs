# Structural & Functional MRI Processing

HBCD MRI data are processed through a standardized sequence of BIDS App pipelines. Each pipeline builds on the derivatives from the previous step:

<style> .pipeline-step { transition: all 0.25s ease; } .pipeline-step:hover { transform: translateY(-3px); box-shadow: 0 4px 10px rgba(100, 100, 255, 0.2); } </style> <div style="display: flex; align-items: center; justify-content: center; gap: 16px; flex-wrap: wrap; font-size: 0.95em;"> <div style="text-align: center;"> <a href="https://bibsnet.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #a9bffcff; border-radius: 12px; background-color: #dde6fe; color: #222;"> <strong>BIBSNet</strong><br> <small>Segmentation & masks</small> </div> </a> </div> <span style="font-size: 20px;"><i class="fa-solid fa-arrow-right"></i></span> <div style="text-align: center;"> <a href="https://nibabies.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #a89df9ff; border-radius: 12px; background-color: #dcd8fb; color: #222;"> <strong>Infant-fMRIPrep</strong><br> <small><i>Surface reconstruction, preprocessing & confounds</i></small> </div> </a> </div> <span style="font-size: 20px;"><i class="fa-solid fa-arrow-right"></i></span> <div style="text-align: center;"> <a href="https://xcp-d.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #d794fcff; border-radius: 12px; background-color: #f0dcfb; color: #222;"> <strong>XCP-D</strong><br> <small>Post-processing & denoising</small> </div> </a> </div> </div>


## Infant fMRIPrep

<div id="nibabies" class="table-banner" onclick="toggleCollapse(this)"> <span class="emoji"><i class="fa-solid fa-diagram-project"></i></span> <span class="text-with-link"> <span class="text">Infant fMRIPrep</span> <a class="anchor-link" href="#nibabies" title="Copy link"> <i class="fa-solid fa-link"></i> </a> </span> <span class="arrow">▸</span> </div> <div class="table-collapsible-content">
<p><b>Infant fMRIPrep</b> adapts <em>fMRIPrep</em> for infant data using age-appropriate templates and two surface reconstruction methods optimized for early development.</p>
<p><b>Anatomical Processing</b><br>
T1w and T2w images are denoised, bias-corrected, and normalized to the MNI Infant template (0–4.5 yr), then to MNI152 for compatibility with adult datasets. Surface reconstruction is performed via:
<ul>
<li><b>M-CRIB-S</b>: T2w-based method with modified <code>MCRIBReconAll</code> workflow. Uses pre-computed anatomical segmentation from BIBSNet.</li>
<li><b>Infant FreeSurfer</b>: T1w-based method that runs <code>infant_recon_all</code>.</li>
</ul>
</p>
<p><b>Functional Processing</b><br>
For each BOLD run: 
<ul>
<li>Motion and distortion correction using fieldmap-based estimation.</li>
<li>Alignment of functional to anatomical space via boundary-based registration.</li>
<li>Confound estimation: framewise displacement (FD) and DVARS for motion, CompCor physiological noise regressors, global signals (mean CSF, white matter, and whole brain), and derived regressors (e.g. motion outlier flags for frames exceeding 0.5 mm FD or 1.5 standardized DVARS thresholds)</li>
<li>Resampling of BOLD data to subject and fsLR-space surfaces, with grayordinates (91k) for surface-based analyses.</li>
</ul></p>
</div>





### Surface Reconstruction Methods

Unique hash IDs identify each processing configuration for traceability. These correspond to the dual Infant fMRIPrep methods used in HBCD data, followed by XCP-D processing (hash `0ef9c88a`). Full details are available on the HBCD Processing site.

<table class="compact-table-no-vertical-lines"> <b>Surface Reconstruction Methods</b> <thead> <tr> <th>Method</th> <th>Hash ID</th> <th>Description</th> </tr> </thead> <tbody> <tr> <td>M-CRIB-S</td> <td><a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0_dev2/tools/nibabies_25.2.0-0f306a2f.html">0f306a2f</a></td> <td>T2w-based, optimized for neonates ≤5 months (<a href="https://doi.org/10.1038/s41598-020-61326-2">Adamson et al., 2020</a>).</td> </tr> <tr> <td>Infant FreeSurfer</td> <td><a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0_dev2/tools/nibabies_25.2.0-2afa9081.html">2afa9081</a></td> <td>T1w-based, optimized for infants ≥3 months (<a href="https://doi.org/10.1016/j.neuroimage.2020.116946">Zöllei et al., 2020</a>).</td> </tr> </tbody> </table>

## XCP-D

<div id="xcpd" class="table-banner" onclick="toggleCollapse(this)"> <span class="emoji"><i class="fa-solid fa-diagram-project"></i></span> <span class="text-with-link"> <span class="text">XCP-D</span> <a class="anchor-link" href="#xcpd" title="Copy link"> <i class="fa-solid fa-link"></i> </a> </span> <span class="arrow">▸</span> </div> <div class="table-collapsible-content"> <p><b>XCP-D</b> refines Infant fMRIPrep outputs, producing cleaned and parcellated data ready for analysis. Atlases used for parcellation are listed under <a href="../mri/#parc">MRI Derivatives: Quickstart Guide</a>.</p> <p><b>Anatomical Processing</b><br> T2w images are transformed to MNI152NLin6Asym (1 mm³). Morphometric surfaces (fsLR-space) from Infant fMRIPrep are converted to HCP-style midthickness, inflated, and very-inflated surfaces.</p> <p><b>Functional Processing</b><br> <ul> <li>Remove first 4 volumes, apply motion correction (FD > 0.3 mm flagged).</li> <li>Regress 36 confounds (36P model), despike, bandpass filter (0.01–0.08 Hz), and smooth (6 mm FWHM).</li> <li>Interpolate and censor high-motion frames.</li> <li>Compute ALFF and ReHo metrics from cleaned data.</li> <li>Extract parcellated time series and compute pairwise functional connectivity.</li> </ul></p> </div>