<p style="color: red;">LUCI ADMIN NOTES: original drafts of nibabies and xcp-d proc descriptions <a href="../mri-proc-alt/">here</a> - info below is more simplified</p>

# Structural & Functional MRI Processing

HBCD MRI data are processed through a standardized sequence of BIDS App pipelines. Each pipeline builds on the derivatives from the previous step:

<style> .pipeline-step { transition: all 0.25s ease; } .pipeline-step:hover { transform: translateY(-3px); box-shadow: 0 4px 10px rgba(100, 100, 255, 0.2); } </style> <div style="display: flex; align-items: center; justify-content: center; gap: 16px; flex-wrap: wrap; font-size: 0.95em;"> <div style="text-align: center;"> <a href="https://bibsnet.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #a9bffcff; border-radius: 12px; background-color: #dde6fe; color: #222;"> <strong>BIBSNet</strong><br> <small>Segmentation & masks</small> </div> </a> </div> <span style="font-size: 20px;"><i class="fa-solid fa-arrow-right"></i></span> <div style="text-align: center;"> <a href="https://nibabies.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #a89df9ff; border-radius: 12px; background-color: #dcd8fb; color: #222;"> <strong>Infant-fMRIPrep</strong><br> <small><i>Surface reconstruction, preprocessing & confounds</i></small> </div> </a> </div> <span style="font-size: 20px;"><i class="fa-solid fa-arrow-right"></i></span> <div style="text-align: center;"> <a href="https://xcp-d.readthedocs.io/en/latest/" style="text-decoration: none;"> <div class="pipeline-step" style="padding: 12px 20px; border: 2px solid #d794fcff; border-radius: 12px; background-color: #f0dcfb; color: #222;"> <strong>XCP-D</strong><br> <small>Post-processing & denoising</small> </div> </a> </div> </div>

## BIBSNet

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

## Infant fMRIPrep

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

### Surface Reconstruction Methods
Unique hash IDs in the Infant fMRIPrep and XCP-D derivative folder and filenames are used to distinguish processing methods. These correspond to dual Infant fMRIPrep surface reconstruction methods (hash ID `0f306a2f` vs. `2afa9081`), followed by XCP-D processing (hash ID `0ef9c88a`). Full details are available on the HBCD Processing site (see [here](https://hbcd-cbrain-processing.readthedocs.io/release_2.0_dev2/tool_details.html)).

<table class="compact-table-no-vertical-lines">
<b>Surface Reconstruction Methods</b>
<thead> <tr> <th>Method</th> <th>Hash ID</th> <th>Description</th> </tr> </thead>
<tbody>
<tr>
<td>M-CRIB-S</td>
<td><a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0_dev2/tools/nibabies_25.2.0-0f306a2f.html">0f306a2f</a></td>
<td>T2w-based method optimized for neonates (<a href="https://doi.org/10.1038/s41598-020-61326-2">Adamson et al., 2020</a>). <i>Optimal ages<b>*</b>: ≤ 5 months</i>.</td>
</tr> <tr>
<td>Infant FreeSurfer</td>
<td><a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0_dev2/tools/nibabies_25.2.0-2afa9081.html">2afa9081</a></td> <td>T1w-based, optimized for infants 0-2 years old (<a href="https://doi.org/10.1016/j.neuroimage.2020.116946">Zöllei et al., 2020</a>). <i>Optimal ages<b>*</b>: ≥ 3 months</i></td>
</tr> </tbody>
<tfoot>
<tr>
  <td colspan="3" style="word-wrap: break-word; white-space: normal; border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
    <b>*</b> Optimal age ranges based on <a href="https://doi.org/10.1101/2025.05.14.654069">Goncalves et al., 2025</a>.
  </td>
</tr>
</tfoot>
</table>

## XCP-D

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

## References
<div class="references">
<p>Adamson, C. L., Alexander, B., Ball, G., Beare, R., Cheong, J. L. Y., Spittle, A. J., Doyle, L. W., Anderson, P. J., Seal, M. L., & Thompson, D. K. (2020). Parcellation of the neonatal cortex using Surface-based Melbourne Children’s Regional Infant Brain atlases (M-CRIB-S). <em>Scientific Reports</em>, 10(1), 4359. <a href="https://doi.org/10.1038/s41598-020-61326-2">https://doi.org/10.1038/s41598-020-61326-2</a></p>
<p>Goncalves, M., Moser, J., Madison, T. J., McCollum, R., Lundquist, J. T., Fayzullobekova, B., Hadera, L., Pham, H. H. N., Moore, L. A., Houghton, A., Conan, G., Styner, M. A., Alexopoulos, D., Smyser, C. D., Stoyell, S. M., Koirala, S., Nelson, S. M., Weldon, K. B., Lee, E., … Fair, D. A. (2025). FMRIPrep Lifespan: Extending A robust pipeline for functional MRI preprocessing to developmental neuroimaging. <em>In bioRxivorg.</em> <a href="https://doi.org/10.1101/2025.05.14.654069">https://doi.org/10.1101/2025.05.14.654069</a></p>
<p>Hendrickson, T. J., Reiners, P., Moore, L. A., Lundquist, J. T., Fayzullobekova, B., Perrone, A. J., Lee, E. G., Moser, J., Day, T. K. M., Alexopoulos, D., Styner, M., Kardan, O., Chamberlain, T. A., Mummaneni, A., Caldas, H. A., Bower, B., Stoyell, S., Martin, T., Sung, S., … Feczko, E. (2024). BIBSNet: A deep learning Baby image brain segmentation network for MRI scans. <em>In bioRxivorg</em>. <a href="https://doi.org/10.1101/2023.03.22.533696">https://doi.org/10.1101/2023.03.22.533696</a></p>
<p>Zöllei, L., Iglesias, J. E., Ou, Y., Grant, P. E., & Fischl, B. (2020). Infant FreeSurfer: An automated segmentation and surface extraction pipeline for T1-weighted neuroimaging data of infants 0-2 years. <em>NeuroImage</em>, 218(116946), 116946. <a href="https://doi.org/10.1016/j.neuroimage.2020.116946">https://doi.org/10.1016/j.neuroimage.2020.116946</a></p>
</div>
 


 




<br><br>
<br><br>

