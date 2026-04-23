# Quantitative MRI (qMRI)

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</i></span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Note that different sites may apply varying criteria for identifying motion-degraded QALAS and B1+ mapping scans. For 3D-QALAS, the SyMRI toolbox does <strong>not</strong> incorporate externally acquired B1+ field maps when estimating quantitative T1, T2, and proton density (PD) values.</p>
<p>Additionally, estimated quantitative T1 values show variability across MRI vendors and participant age. Current estimates do not align well with values reported in the literature, likely due to assumptions made in the modeling procedures. Work is ongoing to address these issues. As a result, quantitative T1 values (and by extension, PD values) will not be included initial release data.</p> 
</div>

## Overview & Acquisition

Conventional neuroimaging relies on qualitative relaxation-weighted images (e.g., T1w, T2w), which reflect relative differences in tissue properties, but are strongly influenced by sequence parameters, participant positioning, and scanner hardware. These dependencies limit biological interpretability and hinder comparisons across participants, sessions, and sites. The challenge is especially pronounced in pediatric imaging, where rapid age-related changes in free water distribution, iron, and myelination dynamically alter image contrast.

**Quantitative MRI (qMRI)** addresses these limitations by directly measuring relaxation properties, providing more reliable markers of brain tissue microstructure ([Deoni 2010](https://doi.org/10.1097/RMR.0b013e31821e56d8); [Does 2018](https://doi.org/10.1016/j.neuroimage.2017.12.087)). The HBCD Study acquires 3D-QALAS, a time-efficient 3D sequence that combines interleaved Look-Locker acquisition with a T2-preparation pulse ([Kvernby et al. 2014](https://doi.org/10.1186/s12968-014-0102-0)). This approach enables simultaneous estimation of T1/T2 relaxation times and proton density (PD) maps from a single scan and has been validated across major MRI vendors ([Fujita et al. 2019](https://doi.org/10.1016/j.mri.2019.08.031)).

<div id="acq" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa-solid fa-circle-info"></i></span><span class="text-with-link">
<span class="text">Acquisition Details</span><a class="anchor-link" href="#acq" title="Copy link">
<i class="fa-solid fa-link"></i></a></span><span class="arrow">▸</span>
</div><div class="collapsible-content">
<p><b>QALAS</b><br>
QALAS is a multi-contrast MRI sequence that produces five brain volumes using turbo-flash readouts with varying T1 and T2 weightings (acquisition time ~5 min for Siemens and ~4 min for GE/Philips). These volumes are combined to estimate T1, T2, and proton density (PD) maps. The sequence starts with a T2-preparation pulse, which adds T2 weighting to the first volume. An inversion pulse follows, imparting T1 weighting to the next four volumes.</p>
**QALAS Pulse Sequence Diagram** (<i><a href="https://onlinelibrary.wiley.com/doi/10.1002/mrm.29939">Fujita et al., 2024</a> Figure. 1</i>)
<img src="../images/qalas_Fig1.png" style="max-width:90%; height:auto;">
<p><b>B1+ Fieldmaps</b><br>
The HBCD protocol includes a short B1+ field map acquisition (~30–45 seconds across all scanner types) to calibrate flip angle measurements, which can vary spatially due to B1+ field inhomogeneity. This calibration is required for accurate T1, T2, and PD estimation. Because the transmit B1+ field varies smoothly across space, coarse spatial resolution is sufficient, enabling rapid acquisition. Vendor-specific implementations in the HBCD protocol include Actual Flip Angle Imaging (AFI) for GE and Philips, and a pre-saturation turbo-FLASH readout for Siemens (<a href="https://doi.org/10.1002/mrm.21120">Yarnykh 2007</a>).</p>
</div>

## Processing & Derivatives
qMRI data are processed via <a href="https://syntheticmr.com/products/symri-neuro/">SyMRI</a> followed by minimal post-processing through <a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html">qMRI PostProc</a>. SyMRI derives synthetic T1w/T2w images and quantitative relaxometry maps from 3D-QALAS acquisitions by reintroducing estimated T1/T2 relaxation times into the MR signal equation (Bloch equations).

<div id="qmri-derivs" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">SyMRI & qMRI PostProc Derivatives</span>
  <a class="anchor-link" href="#qmri-derivs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<pre class="folder-tree">
hbcd/
└── derivatives/
    │
  <span class="hashtag">SyMRI</span>
    ├── symri/ 
    │   └── sub-<span class="label">{ID}</span>/
    │       └── ses-<span class="label">{V0X}</span>/
    │           └── anat/
    │               ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>acq-QALAS_T1w.nii.gz      <span class="hashtag">(+JSON)</span>
    │               ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>acq-QALAS_T2w.nii.gz      <span class="hashtag">(+JSON)</span>
    │               ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>acq-QALAS_T2map.nii.gz    <span class="hashtag">(+JSON)</span>
    │               └── <span class="muted">sub-{ID}_ses-{V0X}_</span>acq-QALAS_desc-SymriContainer.log
    │
  <span class="hashtag">qMRI PostProc</span>
    └── qmri_postproc/
        └── sub-<span class="label">{ID}</span>/
            └── ses-<span class="label">{V0X}</span>/
                └── anat/
                    ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>desc-AsegROIs_scalarstats.tsv            <span class="hashtag">(+JSON)</span>
                    ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>desc-BilateralAsegROIs_scalarstats.tsv   <span class="hashtag">(+JSON)</span>
                    ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>desc-RegistrationQCAid.png               <span class="hashtag">(+JSON)</span>
                    ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-T2w_desc-QALAS_T2map.nii.gz        <span class="hashtag">(+JSON)</span>
                    └── <span class="muted">sub-{ID}_ses-{V0X}_</span>space-QALAS_desc-aseg_dseg.nii.gz

<span><a style="color: white;" href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: white;" class="fa fa-circle-info"></i> How To Read File Trees →</a></span>
</pre>
</div>
<p></p>

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
<p>Dean III, D. C., Tisdall, M. D., Wisnowski, J. L., Feczko, E., Gagoski, B., Alexander, A. L., ... &amp; HBCD MRI Working Group. (2024). Quantifying brain development in the HEALthy Brain and Child Development (HBCD) Study: The magnetic resonance imaging and spectroscopy protocol. <em>Developmental Cognitive Neuroscience</em>, 70, 101452. <a href="https://doi.org/10.1016/j.dcn.2024.101452">https://doi.org/10.1016/j.dcn.2024.101452</a></p>
<p>Deoni, S. C. L. (2010). Quantitative relaxometry of the brain. <i>Topics in Magnetic Resonance Imaging: TMRI</i>, 21(2), 101–113. <a href="https://doi.org/10.1097/RMR.0b013e31821e56d8">https://doi.org/10.1097/RMR.0b013e31821e56d8</a></p>
<p>Deoni, S. C. L., Rutt, B. K., & Peters, T. M. (2006). Synthetic T1-weighted brain image generation with incorporated coil intensity correction using DESPOT1. <i>Magnetic Resonance Imaging</i>, 24(9), 1241–1248. <a href="https://doi.org/10.1016/j.mri.2006.03.015">https://doi.org/10.1016/j.mri.2006.03.015</a></p>
<p>Does, M. D. (2018). Inferring brain tissue composition and microstructure via MR relaxometry. <i>NeuroImage</i>, 182, 136–148. <a href="https://doi.org/10.1016/j.neuroimage.2017.12.087">https://doi.org/10.1016/j.neuroimage.2017.12.087</a></p>
<p>Fautz H-P, Vogel M, Gross P, Kerr A, Zhu Y. B1 mapping of coil arrays for parallel transmission. <i>Proceedings of the 16th Annual Meeting of ISMRM</i>, Toronto, Canada. Vol. 1247. 2008.</p>
<p>Fujita, S., Gagoski, B., Hwang, K.-P., Hagiwara, A., Warntjes, M., Fukunaga, I., Uchida, W., Saito, Y., Sekine, T., Tachibana, R., Muroi, T., Akatsu, T., Kasahara, A., Sato, R., Ueyama, T., Andica, C., Kamagata, K., Amemiya, S., Takao, H., … Aoki, S. (2024). Cross-vendor multiparametric mapping of the human brain using 3D-QALAS: A multicenter and multivendor study. <i>Magnetic Resonance in Medicine</i>, 91(5), 1863–1875. <a href="https://doi.org/10.1002/mrm.29939" target="_blank">https://doi.org/10.1002/mrm.29939</a></p>
<p>Fujita, S., Hagiwara, A., Hori, M., Warntjes, M., Kamagata, K., Fukunaga, I., Andica, C., Maekawa, T., Irie, R., Takemura, M. Y., Kumamaru, K. K., Wada, A., Suzuki, M., Ozaki, Y., Abe, O., &amp; Aoki, S. (2019). Three-dimensional high-resolution simultaneous quantitative mapping of the whole brain with 3D-QALAS: An accuracy and repeatability study. <i>Magnetic Resonance Imaging</i>, 63, 235–243. <a href="https://doi.org/10.1016/j.mri.2019.08.031">https://doi.org/10.1016/j.mri.2019.08.031</a></p>
<p>Gonçalves, F. G., Serai, S. D., & Zuccoli, G. (2018). Synthetic brain MRI. <i>Topics in Magnetic Resonance Imaging: TMRI</i>, 27(6), 387–393. <a href="https://doi.org/10.1097/rmr.0000000000000189">https://doi.org/10.1097/rmr.0000000000000189</a></p>
<p>Ji, S., Yang, D., Lee, J., Choi, S. H., Kim, H., & Kang, K. M. (2022). Synthetic MRI: Technologies and applications in neuroradiology. <i>Journal of Magnetic Resonance Imaging</i>, 55(4), 1013–1025. <a href="https://doi.org/10.1002/jmri.27440">https://doi.org/10.1002/jmri.27440</a></p>
<p>Kvernby, S., Warntjes, M. J. B., Haraldsson, H., Carlhäll, C.-J., Engvall, J., & Ebbers, T. (2014). Simultaneous three-dimensional myocardial T1 and T2 mapping in one breath hold with 3D-QALAS. <i>Journal of Cardiovascular Magnetic Resonance: Official Journal of the Society for Cardiovascular Magnetic Resonance</i>, 16(1), 102. <a href="https://doi.org/10.1186/s12968-014-0102-0" target="_blank">https://doi.org/10.1186/s12968-014-0102-0</a></p>
<p>Yarnykh, V. L. (2007). Actual flip-angle imaging in the pulsed steady state: a method for rapid three-dimensional mapping of the transmitted radiofrequency field. <i>Magnetic Resonance in Medicine</i>, 57(1), 192–200. <a href="https://doi.org/10.1002/mrm.21120" target="_blank">https://doi.org/10.1002/mrm.21120</a></p>
</div>
</div>
