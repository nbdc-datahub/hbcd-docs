# Structural MRI (sMRI)

## Overview & Acquisition

HBCD protocols for structural MRI were informed by recent large-scale developmental neuroimaging studies including [ABCD](https://abcdstudy.org/), HCP Lifespan, and BCP ([Howell et al., 2019](https://pubmed.ncbi.nlm.nih.gov/29578031/)). These studies laid critical foundation for the development of well-validated, high-resolution protocols harmonized across all three major scanner vendors ([Casey et al., 2018](https://doi.org/10.1016/j.dcn.2018.03.001)). In addition, the findings emphasized the importance of T2w acquisition in infants due to suboptimal grey/white T1w contrast resulting from incomplete myelination ([Howell et al., 2019](https://doi.org/10.1016/j.neuroimage.2018.03.049), [Myers et al., 2023](https://doi.org/10.1016/j.neuroimage.2018.03.049)).

<div id="acq" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Acquisition Details</span>
  <a class="anchor-link" href="#acq" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Key features of the HBCD T1w and T2w structural imaging protocols include:</p>
<ul>
<li>0.8 mm isotropic resolution</li>
<li>Compressed SENSE reconstruction enabling high acceleration and shorter acquisition times (&lt;9 min total for T1w & T2w;)</li>
<li>Embedded navigators for motion tracking (<a href="https://doi.org/10.1002/mrm.22176">White et al., 2010</a>, <a href="https://doi.org/10.1016/j.neuroimage.2015.11.054">Tisdall et al., 2016</a>, <a href="https://doi.org/10.1371/journal.pone.0217145">Andersen et al., 2019</a>)</li>
<li>Harmonization approach similar to the <a href="https://nbdc-splash-beta.lassoinformatics.com/abcd-study">ABCD Study</a>:<ul>
<li>T1w: contrast-relevant parameters matched as closely as possible across vendors</li>
<li>T2w: vendor-specific parameters selected to achieve comparable contrast and SNR, accounting for differences in 3D T2w pulse sequence implementation</li></ul></li></ul>
</div>

## Processing & Derivatives
Structural MRI data is used in several processing pipelines. In addition to the derivatives listed below, sMRI is also critical to Infant fMRIPrep and XCP-D, which generate structural-specific derivatives within an <code>anat/</code> subfolder (including T1w/T2w images processed to correct for motion and distortions and surface reconstructions). These derivatives are described on the fMRI page.

### BIBSNet
BIBSNet is a deep learning model optimized for infant MRI brain tissue segmentation (<a href="https://doi.org/10.1101/2023.03.22.533696">Hendrickson et al. 2024</a>). The <a href="https://bibsnet.readthedocs.io/en/latest/">BIBSNet pipeline</a> generates native-space brain segmentations and brain masks (as well as <code>volumes.tsv</code> files with ROI volume statistics), which are fed into Infant fMRIPrep for use in anatomical preprocessing and surface reconstruction.

<div id="bibsnet-derivs" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">BIBSNet Derivatives</span>
  <a class="anchor-link" href="#bibsnet-derivs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><a href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>
<pre class="folder-tree">
hbcd/
└── derivatives/ 
    └── bibsnet/
        └── sub-<span class="label">{ID}</span>/
            └── ses-<span class="label">{V0X}</span>/
                └── anat/
                    ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_dseg.nii.gz <span class="hashtag">(+JSON)</span>
                    ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes.tsv <span class="hashtag">(+JSON)</span>         
                    └── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_brain-mask.nii.gz <span class="hashtag">(+JSON)</span>
</pre>
</div>


### MRIQC & BME-X

[MRIQC](https://mriqc.readthedocs.io/en/latest/about.html) extracts image quality metrics (IQMs) for each T1w/T2w and generates visual <code>.html</code> reports. The [BME-X](https://brain-mri-enhancement.readthedocs.io/) pipeline performs motion correction, resolution enhancement, denoising, and harmonization of MR images.

<div id="mriqc" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span><span class="text-with-link">
<span class="text">MRIQC & BME-X Derivatives</span><a class="anchor-link" href="#mriqc" title="Copy link">  <i class="fa-solid fa-link"></i></a></span>
  <span class="arrow">▸</span></div>
<div class="table-collapsible-content">
<pre class="folder-tree">
hbcd/
└── derivatives/
    ├── mriqc/                            
    │   ├── sub-<span class="label">{ID}</span>/
    │   │   └── ses-<span class="label">{V0X}</span>/
    │   │       ├── anat/
    │   │       │   └── <span class="muted">sub-{ID}_ses-{V0X}_run-{x}</span>_<span class="placeholder">&lt;T1w|T2w&gt;</span>.json
    │   │       └── func/
    │   │           └── <span class="muted">sub-{ID}_ses-{V0X}_run-{x}</span>_<span class="placeholder">&lt;T1w|T2w&gt;</span>.json
    │   └── <span class="muted">sub-{ID}_ses-{V0X}_run-{x}</span>_<span class="placeholder">&lt;T1w|T2w&gt;</span>.html
    │
    └── bme-x/                  
        └── sub-<span class="label">{ID}</span>/
            └── ses-<span class="label">{V0X}</span>/
                └── anat/
                    |__ <span class="muted">sub-{ID}_ses-{V0X}_run-{X}_</span>desc-<span class="placeholder">&lt;enhanced|preproc&gt;</span>_<span class="placeholder">&lt;T1w|T2w&gt;</span>.nii.gz <span class="hashtag">(+JSON)</span>
                    |__ <span class="muted">sub-{ID}_ses-{V0X}_run-{X}_</span>space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-brain_mask.nii.gz <span class="hashtag">(+JSON)</span>
                    |__ <span class="muted">sub-{ID}_ses-{V0X}_run-{X}_</span><span class="placeholder">&lt;T1w|T2w&gt;</span>.nii.gz <span class="hashtag">(+JSON)</span>
</pre>
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
  <p>Andersen, M., Björkman-Burtscher, I. M., Marsman, A., Petersen, E. T., & Boer, V. O. (2019). Improvement in diagnostic quality of structural and angiographic MRI of the brain using motion correction with interleaved, volumetric navigators.
    <em>PLoS One</em>, 14(5), e0217145. <a href="https://doi.org/10.1371/journal.pone.0217145">https://doi.org/10.1371/journal.pone.0217145</a></p>
    <p>Casey, B. J., Cannonier, T., Conley, M. I., Cohen, A. O., Barch, D. M., Heitzeg, M. M., Soules, M. E., Teslovich, T., Dellarco, D. V., Garavan, H., Orr, C. A., Wager, T. D., Banich, M. T., Speer, N. K., Sutherland, M. T., Riedel, M. C., Dick, A. S., Bjork, J. M., Thomas, K. M., … ABCD Imaging Acquisition Workgroup. (2018). The Adolescent Brain Cognitive Development (ABCD) study: Imaging acquisition across 21 sites. <em>Developmental Cognitive Neuroscience</em>, 32, 43–54. <a href="https://doi.org/10.1016/j.dcn.2018.03.001">https://doi.org/10.1016/j.dcn.2018.03.001</a></p>
    <p>Hendrickson, T. J., Reiners, P., Moore, L. A., Lundquist, J. T., Fayzullobekova, B., Perrone, A. J., Lee, E. G., Moser, J., Day, T. K. M., Alexopoulos, D., Styner, M., Kardan, O., Chamberlain, T. A., Mummaneni, A., Caldas, H. A., Bower, B., Stoyell, S., Martin, T., Sung, S., … Feczko, E. (2024). BIBSNet: A deep learning Baby image brain segmentation network for MRI scans. <em>In bioRxivorg</em>. <a href="https://doi.org/10.1101/2023.03.22.533696">https://doi.org/10.1101/2023.03.22.533696</a></p>
    <p>Howell, B. R., Styner, M. A., Gao, W., Yap, P.-T., Wang, L., Baluyot, K., Yacoub, E., Chen, G., Potts, T., Salzwedel, A., Li, G., Gilmore, J. H., Piven, J., Smith, J. K., Shen, D., Ugurbil, K., Zhu, H., Lin, W., & Elison, J. T. (2019). The UNC/UMN Baby Connectome Project (BCP): An overview of the study design and protocol development. <em>NeuroImage</em>, 185, 891–905. <a href="https://doi.org/10.1016/j.neuroimage.2018.03.049">https://doi.org/10.1016/j.neuroimage.2018.03.049</a></p>
    <p>Myers, M. J., Labonte, A. K., Gordon, E. M., Laumann, T. O., Tu, J. C., Wheelock, M. D., Nielsen, A. N., Schwarzlose, R., Camacho, M. C., Warner, B. B., Raghuraman, N., Luby, J. L., Barch, D. M., Fair, D. A., Petersen, S. E., Rogers, C. E., Smyser, C. D., & Sylvester, C. M. (2023). Functional parcellation of the neonatal brain. In <em>bioRxivorg</em>. <a href="https://doi.org/10.1101/2023.11.10.566629">https://doi.org/10.1101/2023.11.10.566629</a></p>
    <p>Tisdall, M. D., Reuter, M., Qureshi, A., Buckner, R. L., Fischl, B., & van der Kouwe, A. J. W. (2016). Prospective motion correction with volumetric navigators (vNavs) reduces the bias and variance in brain morphometry induced by subject motion. <em>Neuroimage</em>, 127, 11-22. <a href="https://doi.org/10.1016/j.neuroimage.2015.11.054">https://doi.org/10.1016/j.neuroimage.2015.11.054</a></p>
    <p>White, N., Roddey, C., Shankaranarayanan, A., Han, E., Rettmann, D., Santos, J., Kuperman, J., & Dale, A. (2010). PROMO: Real-time prospective motion correction in MRI using image-based tracking. <em>Magnetic Resonance in Medicine</em>, 63(1), 91–105. <a href="https://doi.org/10.1002/mrm.22176">https://doi.org/10.1002/mrm.22176</a></p>
</div>
</div>