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
<p>Note that different sites may apply varying criteria for identifying motion-degraded QALAS and B1⁺ mapping scans. For 3D-QALAS, the SyMRI toolbox does <strong>not</strong> incorporate externally acquired B1⁺ field maps when estimating quantitative T1, T2, and proton density (PD) values.</p>
<p>Additionally, estimated quantitative T1 values show variability across MRI vendors and participant age. Current estimates do not align well with values reported in the literature, likely due to assumptions made in the modeling procedures. Work is ongoing to address these issues. As a result, quantitative T1 values (and by extension, PD values) will not be included in the initial data release.</p> 
</div>

## Data Processing

### Relaxation (T1/T2) & Proton Density (PD) Maps 

For the HBCD study, the MRI working group adopted 3D-QALAS ([Kvernby et al. 2014](https://doi.org/10.1186/s12968-014-0102-0)), a time-efficient 3D method that combines interleaved Look-Locker acquisition with a T2-preparation pulse. This approach simultaneously estimates longitudinal (T1) and transverse (T2) relaxation times, as well as proton density (PD) maps, from a single scan, and has been validated across major MRI vendors ([Fujita et al. 2019](https://doi.org/10.1016/j.mri.2019.08.031)).

Conventional neuroimaging typically relies on qualitative relaxation time-weighted images, e.g, T1w and T2w images, which reflect relative differences in relaxation times, but are strongly influenced by sequence parameters, participant positioning, and scanner hardware. These dependencies complicate biological interpretation and hinder quantitative comparisons across participants, sessions, and sites. The issue is particularly acute in pediatric neuroimaging, where rapid changes in free water distribution, iron, and myelination alter image contrast as a function of age. By directly measuring relaxation properties, quantitative MRI overcomes many of these limitations and provides more reliable markers of brain tissue microstructure ([Deoni 2010](https://doi.org/10.1097/RMR.0b013e31821e56d8); [Does 2018](https://doi.org/10.1016/j.neuroimage.2017.12.087)).

### Synthetic T1w/T2w Images

Using 3D-QALAS data with the Synthetic MRI (SyMRI) toolbox, we also generate synthetic T1w (Sy-T1w) and T2w (Sy-T2w) volumes. These are created by substituting quantitative estimates of T1 and T2 relaxation times back into the MR signal equation (Bloch equations) for each sequence. This enables flexible generation of different contrasts without acquiring separate scans.

<div id="derivatives" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">SyMRI (<code>symri/</code>) & qMRI PostProc (<code>qmri_postproc/</code>) Derivatives</span>
  <a class="anchor-link" href="#derivatives" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Quantitative MRI data was processed through two pipelines, SyMRI and qMRI PostProc. <a href="https://syntheticmr.com/products/symri-neuro/">SyMRI</a>, a proprietary software for quantitative MRI, is used to generate T1w and T2w images and derived relaxometry maps from <a href="https://pubmed.ncbi.nlm.nih.gov/25526880/">QALAS</a> brain images. These outputs are then minimally preprocessed by <a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html">qMRI PostProc</a>.</p>
<p><a href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>
<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ symri/  <span class="hashtag"># SyMRI Derivatives</span>
    |   |__ sub-<span class="label">{ID}</span>/
    |       |__ ses-<span class="label">{V0X}</span>/
    |           |__ anat/
    |               |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-QALAS_T1w.nii.gz <span class="hashtag">(+JSON)</span>
    |               |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-QALAS_T2map.nii.gz <span class="hashtag">(+JSON)</span>
    |               |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-QALAS_T2w.nii.gz <span class="hashtag">(+JSON)</span>
    |               |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-QALAS_desc-SymriContainer.log
    | 
    |__ qmri_postproc/ <span class="hashtag"># qMRI Post-Proc Derivatives</span>
        |__ sub-<span class="label">{ID}</span>/
            |__ ses-<span class="label">{V0X}</span>/
                |__ anat/  
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-AsegROIs_scalarstats.tsv <span class="hashtag">(+JSON)</span>
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-BilateralAsegROIs_scalarstats.tsv <span class="hashtag">(+JSON)</span>
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-RegistrationQCAid.png <span class="hashtag">(+JSON)</span>
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-QALAS_desc-aseg_dseg.nii.gz
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-T2w_desc-QALAS_T2map.nii.gz <span class="hashtag">(+JSON)</span>
</pre>
</div>

## References
<div class="references">
<p>Deoni, S. C. L. (2010). Quantitative relaxometry of the brain. <i>Topics in Magnetic Resonance Imaging: TMRI</i>, 21(2), 101–113. <a href="https://doi.org/10.1097/RMR.0b013e31821e56d8">https://doi.org/10.1097/RMR.0b013e31821e56d8</a></p>

<p>Deoni, S. C. L., Rutt, B. K., & Peters, T. M. (2006). Synthetic T1-weighted brain image generation with incorporated coil intensity correction using DESPOT1. <i>Magnetic Resonance Imaging</i>, 24(9), 1241–1248. <a href="https://doi.org/10.1016/j.mri.2006.03.015">https://doi.org/10.1016/j.mri.2006.03.015</a></p>

<p>Does, M. D. (2018). Inferring brain tissue composition and microstructure via MR relaxometry. <i>NeuroImage</i>, 182, 136–148. <a href="https://doi.org/10.1016/j.neuroimage.2017.12.087">https://doi.org/10.1016/j.neuroimage.2017.12.087</a></p>

<p>Fujita, S., Gagoski, B., Hwang, K.-P., Hagiwara, A., Warntjes, M., Fukunaga, I., Uchida, W., Saito, Y., Sekine, T., Tachibana, R., Muroi, T., Akatsu, T., Kasahara, A., Sato, R., Ueyama, T., Andica, C., Kamagata, K., Amemiya, S., Takao, H., … Aoki, S. (2024). Cross-vendor multiparametric mapping of the human brain using 3D-QALAS: A multicenter and multivendor study. <i>Magnetic Resonance in Medicine</i>, 91(5), 1863–1875. <a href="https://doi.org/10.1002/mrm.29939" target="_blank">https://doi.org/10.1002/mrm.29939</a></p>

<p>Fujita, S., Hagiwara, A., Hori, M., Warntjes, M., Kamagata, K., Fukunaga, I., Andica, C., Maekawa, T., Irie, R., Takemura, M. Y., Kumamaru, K. K., Wada, A., Suzuki, M., Ozaki, Y., Abe, O., &amp; Aoki, S. (2019). Three-dimensional high-resolution simultaneous quantitative mapping of the whole brain with 3D-QALAS: An accuracy and repeatability study. <i>Magnetic Resonance Imaging</i>, 63, 235–243. <a href="https://doi.org/10.1016/j.mri.2019.08.031">https://doi.org/10.1016/j.mri.2019.08.031</a></p>

<p>Kvernby, S., Warntjes, M. J. B., Haraldsson, H., Carlhäll, C.-J., Engvall, J., & Ebbers, T. (2014). Simultaneous three-dimensional myocardial T1 and T2 mapping in one breath hold with 3D-QALAS. <i>Journal of Cardiovascular Magnetic Resonance: Official Journal of the Society for Cardiovascular Magnetic Resonance</i>, 16(1), 102. <a href="https://doi.org/10.1186/s12968-014-0102-0" target="_blank">https://doi.org/10.1186/s12968-014-0102-0</a></p>
</div>