# Magnetic Resonance Spectroscopy (MRS)

**Magnetic Resonance Spectroscopy (MRS)** measures biochemicals involved in neuronal metabolism, neurotransmission, and oxidative stress, enabling investigation of mechanisms underlying structural, functional, and behavioral development. HBCD is the first study of this scale to incorporate MRS into a comprehensive pediatric neuroimaging protocol, with data acquired via Integrated Short-TE and Hadamard Multi-Sequence (ISTHMUS) ([Hui et al., 2024](https://doi.org/10.1016/j.jneumeth.2024.110206); [Oeltzschner et al., 2019](https://doi.org/10.1016/j.neuroimage.2018.10.002)). Primary metabolites measured for HBCD include: 

- **N-acetylaspartate (NAA)**: marker of neuronal mitochondrial metabolism
- **Glutamate** and **γ-aminobutyric acid (GABA)**: principal excitatory and inhibitory neurotransmitters
- **Glutathione (GSH)**: major antioxidant protecting against reactive oxygen species
- Additional metabolites include lactate, ascorbate, creatine, myo-inositol, glutamine, and total choline 

## MRS Acquisition

Full protocols, sequence installation, and operation instructions are available via <a href="https://hbcdsequences.readthedocs.io/">HBCD Study MRI Protocols</a>. Of note, a key challenge in MRS is sensitivity to scanner frequency drift, which can degrade data quality by altering editing efficiency and signal contributions (<a href="https://doi.org/10.1002/mrm.25009">Harris et al., 2014</a>). To address this, HBCD incorporates interleaved water referencing for real-time frequency correction, initially implemented on Philips systems and later extended to Siemens and GE platforms
 (<a href="https://doi.org/10.1002/jmri.25304">Edden et al., 2016</a>).

## MRS Processing & Derivatives
HBCD MRS data are processed with [OSPREY-BIDS](https://osprey-bids.readthedocs.io/en/latest/index.html), a customized automated pipeline based on OSPREY ([Oeltzschner et al., 2020](https://doi.org/10.1016/j.jneumeth.2020.108827); [Zöllner et al., 2023](https://doi.org/10.1007/s10916-023-01969-6)). Full details regarding HBCD processing implementation (e.g., file selection for processing) are available in the external [HBCD Processing](https://hbcd-cbrain-processing.readthedocs.io/release_2.0/tools/osprey.html) documentation.

<div id="derivatives" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">OSPREY-BIDS Derivatives</span>
  <a class="anchor-link" href="#derivatives" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<pre class="folder-tree" style="font-size: 0.75em;">
<span><a style="color: white;" href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: white;" class="fa fa-circle-info"></i> How To Read File Trees →</a></span>

hbcd/
└── derivatives/
    └── osprey/
        └── sub-<span class="label">{ID}</span>/
            └── ses-<span class="label">{V0X}</span>/
                ├── HERCULES/
                │   ├── PreOspreyLocalizerReg/
                │   │   ├── <span class="placeholder">&lt;aal|c1|c2|c3&gt;</span>reference_seg_aligned_to_localizer.nii.gz
                │   │   ├── reference_<span class="placeholder">&lt;img|seg&gt;</span>_aligned_to_localizer.nii.gz
                │   │   ├── readme.txt
                │   │   ├── registration_summary.json
                │   │   └── transform_mat.npy
                │   │
                │   ├── QuantifyResults/
                │   │   ├── <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1.tsv
                │   │   ├── <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_<span class="placeholder">&lt;AlphaCorr|CSF|raw|TissCorr&gt;</span>WaterScaled_Voxel_1_Basis_1.tsv
                │   │   └── <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_<span class="placeholder">&lt;amplMets|tCr&gt;</span>_Voxel_1_Basis_1.tsv
                │   │
                │   ├── SegMaps/
                │   │   ├── <span class="muted">sub-{ID}_ses-{V0X}_</span>acq-hercules_svs.nii_space-scanner_Voxel-1_label-<span class="placeholder">&lt;ROI&gt;</span>.nii.gz
                │   │   └── TissueFractions_Voxel_1.tsv
                │   │
                │   ├── VoxelMasks/
                │   │   └── <span class="muted">sub-{ID}_ses-{V0X}_</span>acq-hercules_svs_space-scanner_mask.nii.gz
                │   │
                │   ├── LogFile.txt
                │   ├── QM_processed_spectra.tsv
                │   ├── subject_names_and_excluded.tsv 
                │   ├── SummaryMRSinMRS.md
                │   └── wrapper_settings.mat
                │
                └── unedited/
                <span class="hashtag"># Mirrors HERCULES/ structure - only unique filenames are displayed below</span>
                    ├── QuantifyResults/
                    │   ├── A_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1.tsv
                    │   ├── A_<span class="placeholder">&lt;AlphaCorr|CSF|raw|TissCorr&gt;</span>WaterScaled_Voxel_1_Basis_1.tsv
                    │   └── A_<span class="placeholder">&lt;amplMets|tCr&gt;</span>_Voxel_1_Basis_1.tsv
                    ├── SegMaps/
                    │   └── <span class="muted">sub-{ID}_ses-{V0X}_</span>acq-shortTE_svs.nii_space-scanner_Voxel-1_label-<span class="placeholder">&lt;ROI&gt;</span>.nii.gz
                    └── VoxelMasks/
                        └── <span class="muted">sub-{ID}_ses-{V0X}_</span>acq-shortTE_svs_space-scanner_mask.nii.gz

<span class="hashtag"># Label Values Legend</span>
<span class="placeholder">ROI</span>: CSF | GM | Tha | WM
</pre>
</div>

## Osprey MRS Output User Guide

The primary of outcome variables from MRS data processed through the Osprey pipeline are metabolite concentrations. The ISTHMUS acquisition generates four spectra, each modeled separately using linear combination modeling with inclusive basis sets (since most metabolites may contribute, at least minimally, to all spectra). Each spectrum provides optimal quantification for a different subset of metabolites as follows:

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead><tr><th>Spectrum</th><th>Best-Quantified Metabolites</th><th>Table Name<sup><b>1</b></sup></th></tr></thead>
<tbody>
<tr><td><b>Short-TE Unedited</b></td><td>tNAA, tCr, tCho, mI, Glx, Scyllo</d><td><code>img_osprey_unedited_A_TissCorrWaterScaled_Voxel_1_Basis_1</code></td>
</tr>
<tr><td><b>HERCULES Sum</b></td><td>NAA, Glu, Gln</td><td><code>img_osprey_HERCULES_sum_TissCorrWaterScaled_Voxel_1_Basis_1</code></td>
</tr>
<tr><td><b>HERCULES Diff1</b></td><td>GABA+</td><td><code>img_osprey_HERCULES_diff1_TissCorrWaterScaled_Voxel_1_Basis_1</code></td>
</tr>
<tr><td><b>HERCULES Diff2</b></td><td>GSH, Lac, NAAG, PE</td><td><code>img_osprey_HERCULES_diff2_TissCorrWaterScaled_Voxel_1_Basis_1</code></td>
</tr>
</tbody><tfoot>
<tr><td colspan="3" style="word-wrap: break-word; white-space: normal; border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
<sup><b>1</b></sup> Note: tables contain data summarized across participants from <a href="#derivatives">Osprey pipeline derivatives</a></td></tr>
</tfoot>
</table>

### Quantification Approaches
MRS values are quantified relative to internal reference signals. Optimal reference for HBCD data has not yet been established, so several quantification methods are provided (see [Harris et al., 2015](https://doi.org/10.1002/jmri.24903)):

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr><th>Method</th><th>Recommended Use</th></tr></thead>
<tbody>
<tr>
  <td>Tissue-Corrected Water-Scaled Concentrations <i class="fa-solid fa-star" style="color: gold;"></i></td>
  <td><b>Recommended default</b> (<code>TissCorrWaterScaled</code> TSV files)</td>
</tr>
<tr><td>Alpha-corrected variants</td><td>Use only for GABA+</td></tr>
<tr>
  <td>Metabolite-to-creatine ratios</td>
  <td style="word-wrap: break-word; white-space: normal;">Values are normalized to total creatine (tCr), which is relativel stable across lifespan, but only present in tissue and not CSF; use only for tissue</td>
</tr>
<tr><td>Unscaled model amplitudes</td><td>Do not use for analyses</td></tr>
<!-- <tr><td>Raw water-scaled concentrations</td><td></td></tr> -->
</tbody>
</table>

## References 

<div id="ref" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-book-open"></i></span>
  <span class="text-with-link">
  <span class="text">References <span class="hint">(Click to expand)</span></span>
  <a class="anchor-link" href="#ref" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<div class="references">
    <p>Bottomley, P. A. (1987). Spatial localization in NMR spectroscopy in vivo. <em>Annals of the New York Academy of Sciences</em>, 508(1), 333–348. <a href="https://doi.org/10.1111/j.1749-6632.1987.tb32915.x">https://doi.org/10.1111/j.1749-6632.1987.tb32915.x</a></p>
    <p>Edden, R. A. E., Oeltzschner, G., Harris, A. D., Puts, N. A. J., Chan, K. L., Boer, V. O., Schär, M., & Barker, P. B. (2016). Prospective frequency correction for macromolecule-suppressed GABA editing at 3T. <em>Journal of Magnetic Resonance Imaging</em>, 44(6), 1474–1482.. <a href="https://doi.org/10.1002/jmri.25304">https://doi.org/10.1002/jmri.25304</a></p>
    <p>Harris, A. D., Glaubitz, B., Near, J., John Evans, C., Puts, N. A. J., Schmidt-Wilcke, T., Tegenthoff, M., Barker, P. B., & Edden, R. A. E. (2014). Impact of frequency drift on gamma-aminobutyric acid-edited MR spectroscopy. <em>Magnetic Resonance in Medicine</em>, 72(4), 941–948. <a href="https://doi.org/10.1002/mrm.25009">https://doi.org/10.1002/mrm.25009</a></p>
     <p>Harris, A. D., Puts, N. A. J., & Edden, R. A. E. (2015). Tissue correction for GABA-edited MRS: Considerations of voxel composition, tissue segmentation, and tissue relaxations.<em>Journal of Magnetic Resonance Imaging</em>, 42(5), 1431–1440. <a href="https://doi.org/10.1002/jmri.24903">https://doi.org/10.1002/jmri.24903</a></p>
    <p>Hui, S. C. N., Murali-Manohar, S., Zöllner, H. J., Hupfeld, K. E., Davies-Jenkins, C. W., Gudmundson, A. T., Song, Y., Yedavalli, V., Wisnowski, J. L., Gagoski, B., Oeltzschner, G., & Edden, R. A. E. (2024). Integrated Short-TE and Hadamard-edited Multi-Sequence (ISTHMUS) for advanced MRS. <em>Journal of Neuroscience Methods</em>, 409(110206), 110206. <a href="https://doi.org/10.1016/j.jneumeth.2024.110206">https://doi.org/10.1016/j.jneumeth.2024.110206</a></p>
    <p>Oeltzschner, G., Saleh, M. G., Rimbault, D., Mikkelsen, M., Chan, K. L., Puts, N. A. J., & Edden, R. A. E. (2019). Advanced Hadamard-encoded editing of seven low-concentration brain metabolites: Principles of HERCULES. <em>NeuroImage</em>, 185, 181–190. <a href="https://doi.org/10.1016/j.neuroimage.2018.10.002">https://doi.org/10.1016/j.neuroimage.2018.10.002</a></p>
    <p>Oeltzschner, G., Zöllner, H. J., Hui, S. C. N., Mikkelsen, M., Saleh, M. G., Tapper, S., & Edden, R. A. E. (2020). Osprey: Open-source processing, reconstruction & estimation of magnetic resonance spectroscopy data. Journal of Neuroscience Methods, 343(108827), 108827. <a href="https://doi.org/10.1016/j.jneumeth.2020.108827">https://doi.org/10.1016/j.jneumeth.2020.108827</a></p>
    <p>Träber, F., Block, W., Lamerichs, R., Gieseke, J., & Schild, H. H. (2004). 1H metabolite relaxation times at 3.0 tesla: Measurements of T1 and T2 values in normal brain and determination of regional differences in transverse relaxation. <em>Journal of Magnetic Resonance Imaging</em>, 19(5), 537–545. <a href="https://doi.org/10.1002/jmri.20053">https://doi.org/10.1002/jmri.20053</a></p>
    <p>Zöllner, H. J., Davies-Jenkins, C. W., Lee, E. G., Hendrickson, T. J., Clarke, W. T., Edden, R. A. E., Wisnowski, J. L., Gudmundson, A. T., & Oeltzschner, G. (2023). Continuous automated analysis workflow for MRS studies. Journal of Medical Systems, 47(1), 69. <a href="https://doi.org/10.1007/s10916-023-01969-6">https://doi.org/10.1007/s10916-023-01969-6</a></p>
</div>
</div>


 