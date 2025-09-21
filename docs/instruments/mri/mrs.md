# Magnetic Resonance Spectroscopy (MRS)

<p>
<div id="fyi" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">Please see <a href="../#mri-protocols-sequence-installation">MRI Protocols</a> and <a href="../qc">MR Quality Control Procedures</a> for additional details.</span>
</div>
</p>

Magnetic Resonance Spectroscopy (MRS) provides measures of biochemicals involved in neuronal metabolism, neurotransmission, and oxidative stress. These measures enable researchers to interrogate biochemical mechanisms underlying the structural, functional, and behavioral trajectories. HBCD is the first study of this magnitude to include MRS in a comprehensive pediatric neuroimaging protocol through the development of Integrated Short-TE and Hadamard Multi-Sequence, or ISTHMUS ([Hui et al., 2024](https://doi.org/10.1016/j.jneumeth.2024.110206)).

## MRS Protocol

The MRS acquisition protocol was optimized to maximize signal-to-noise across multiple low-concentration metabolites while maintaining an acquisition time (TA) under 9 minutes. The MRS acquisition centers on a single voxel Point-RESolved Spectroscopy (PRESS) ([Bottomley, 1987](https://doi.org/10.1111/j.1749-6632.1987.tb32915.x)) localization (30×23×23 mm^3) in the bilateral thalamus, with SVS localizer acquisitions to define the ROI. The ISTHMUS sequence incorporates a short TE (35 ms) unedited block at the beginning of the sequence for optimal measurement of high concentration metabolites, including N-acetylasparte, followed by an advanced Hadamard encoded spectral editing scheme ([Oeltzschner et al., 2019](https://doi.org/10.1016/j.neuroimage.2018.10.002)) to derive reliable and reproducible measures of the low-concentration metabolites. 

The primary metabolites measured for HBCD include: 

- **N-acetylaspartate (NAA)**: a marker of neuronal mitochondrial metabolism
- **Glutamate** and **γ-aminobutyric acid (GABA)**: the principal excitatory and inhibitory neurotransmitters
- **Glutathione (GSH)**: the most abundant antioxidant involved in protection against reactive oxygen species in the human brain

Additional metabolites measured include NAA, lactate, ascorbate, creatine, myo-inositol, glutamine, and total choline ([Oeltzschner et al., 2019](https://doi.org/10.1016/j.neuroimage.2018.10.002)).

## Innovations

One limitation to the incorporation of MRS into human connectome studies is proper control for scanner drift. Because MRS relies on the frequency of the measured signals, uncorrected frequency drift during data acquisition is very detrimental to data quality, as it changes the contribution of coedited signals as well as editing efficiency ([Harris et al., 2014](https://doi.org/10.1002/mrm.25009)). To mitigate drift, an innovative approach was taken to incorporate interleaved water referencing ([Edden et al., 2016](https://doi.org/10.1002/jmri.25304)) for real-time frequency correction, implemented on the Philips platform at the outset of HBCD, and in Y3 for Siemens and GE.

## Release Data

### Raw BIDS

<div id="bids-mrs" class="table-banner" onclick="toggleCollapse(this)">
  <img src="../../../images/BIDS-logo.png" style="width: 3%;" alt="BIDS-logo">
  <span class="text-with-link">
  <span>BIDS Conversion Procedures: MRS</span>
  <a class="anchor-link" href="#bids-mrs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>For MRS, vendor-specific raw data formats (Siemens <code>.dat</code>; Philips data/list; GE P-file) were converted to BIDS using a wrapper (<a href="https://github.com/DCAN-Labs/hbcd_mrs_to_nii_conversion">hbcd_mrs_to_nii_conversion</a>) for <a href="https://github.com/wtclarke/spec2nii">spec2nii v0.7.0</a>.</p>
</div>

MRS files include metabolite and water reference (`*_<svs|ref>.nii.gz`) data aqcuired via short-echo-time (TE = 35 ms) and HERCULES (spectral-edited, TE = 80 ms) (`acq-<shortTE|hercules>`). The JSON sidecar files include the dimensions of the NIfTI-MRS data array, holding different coil elements in dimension 5 and different transients in dimension 6.
<pre class="folder-tree">
mrs/
|__ sub-<span class="label">&lt;ID&gt;</span>_ses-<span class="label">&lt;V0X&gt;</span>_acq-shortTE_run-<span class="label">&lt;X&gt;</span>_svs.nii.gz
|__ sub-<span class="label">&lt;ID&gt;</span>_ses-<span class="label">&lt;V0X&gt;</span>_acq-shortTE_run-<span class="label">&lt;X&gt;</span>_svs.json
|__ sub-<span class="label">&lt;ID&gt;</span>_ses-<span class="label">&lt;V0X&gt;</span>_acq-shortTE_run-<span class="label">&lt;X&gt;</span>_ref.nii.gz
|__ sub-<span class="label">&lt;ID&gt;</span>_ses-<span class="label">&lt;V0X&gt;</span>_acq-shortTE_run-<span class="label">&lt;X&gt;</span>_ref.json
|__ sub-<span class="label">&lt;ID&gt;</span>_ses-<span class="label">&lt;V0X&gt;</span>_acq-hercules_run-<span class="label">&lt;X&gt;</span>_svs.nii.gz
|__ sub-<span class="label">&lt;ID&gt;</span>_ses-<span class="label">&lt;V0X&gt;</span>_acq-hercules_run-<span class="label">&lt;X&gt;</span>_svs.json
|__ sub-<span class="label">&lt;ID&gt;</span>_ses-<span class="label">&lt;V0X&gt;</span>_acq-hercules_run-<span class="label">&lt;X&gt;</span>_ref.nii.gz
|__ sub-<span class="label">&lt;ID&gt;</span>_ses-<span class="label">&lt;V0X&gt;</span>_acq-hercules_run-<span class="label">&lt;X&gt;</span>_ref.json
</pre>

### Derivatives: OSPREY-BIDS

For HBCD MRS data processing has been carried out using a customized automated pipeline, adapted from OSPREY ([Oeltzschner et al., 2020](https://doi.org/10.1016/j.jneumeth.2020.108827); [Zöllner et al., 2023](https://doi.org/10.1007/s10916-023-01969-6)). The derivatives include quality control metrics and metabolite estimates as a ratio to creatine and water, with and without tissue correction. For further details, please see the [OSPREY-BIDS documentation site](https://osprey-bids.readthedocs.io/en/latest/index.html) as well as the [Processing Pipelines](../processing/index.md) section, which contains an overview of pipelines used for HBCD data processing and links to relevant documentation.

Only the `HERCULES/` file tree is displayed below. The `unedited/` files generally follow similar naming conventions, with some exceptions (e.g., the BIDS field `acq-shortTE` is used instead of `acq-hercules`).

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ osprey/
        |__ sub-<span class="label">&lt;ID&gt;</span>/
            |__ ses-<span class="label">&lt;V0X&gt;</span>/
                |__ HERCULES/
                |   |__ PreOspreyLocalizerReg/
                |   |   |__ figures/
                |   |   |__ <span class="placeholder">&lt;aal|c1|c2|c3&gt;</span>reference_seg_aligned_to_localizer.nii.gz
                |   |   |__ reference_<span class="placeholder">&lt;img|seg&gt;</span>_aligned_to_localizer.nii.gz
                |   |   |__ registration_summary.json
                |   |   |__ transform_mat.npy
                |   |   |__ readme.txt
                |   |
                |   |__ QuantifyResults/ <span class="hashtag">(ALL +JSON)</span>
                |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1.tsv
                |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_AlphaCorrWaterScaled_Voxel_1_Basis_1.tsv
                |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_CSFWaterScaled_Voxel_1_Basis_1.tsv 
                |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_TissCorrWaterScaled_Voxel_1_Basis_1.tsv
                |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_amplMets_Voxel_1_Basis_1.tsv
                |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_rawWaterScaled_Voxel_1_Basis_1.tsv
                |   |   |__ <span class="placeholder">&lt;diff1|diff2|sum&gt;</span>_tCr_Voxel_1_Basis_1.tsv
                |   |
                |   |__ Reports/
                |   |   |__ reportFigures/
                |   |   |__ sub-<span class="label">&lt;ID&gt;</span>-report.html
                |   |
                |   |__ SegMaps/
                |   |   |__ TissueFractions_Voxel_1.tsv <span class="hashtag">(+JSON)</span>
                |   |   |__ <span class="subses">SUBSES</span>_acq-hercules_svs.nii_space-scanner_Voxel-1_label-CSF.nii.gz
                |   |   |__ <span class="subses">SUBSES</span>_acq-hercules_svs.nii_space-scanner_Voxel-1_label-GM.nii.gz
                |   |   |__ <span class="subses">SUBSES</span>_acq-hercules_svs.nii_space-scanner_Voxel-1_label-Tha.nii.gz
                |   |   |__ <span class="subses">SUBSES</span>_acq-hercules_svs.nii_space-scanner_Voxel-1_label-WM.nii.gz
                |   |
                |   |__ VoxelMasks/
                |   |   |__ <span class="subses">SUBSES</span>_acq-hercules_svs_space-scanner_mask.nii.gz
                |   |
                |   |__ LogFile.txt
                |   |__ QM_processed_spectra.tsv <span class="hashtag">(+JSON)</span>
                |   |__ SummaryMRSinMRS.md
                |   |__ subject_names_and_excluded.tsv <span class="hashtag">(+JSON)</span>
                |   |__ wrapper_settings.mat <span class="hashtag">(+JSON)</span>
                |
                |__ unedited/
</pre>

## References
<div class="references">
    <p>Bottomley, P. A. (1987). Spatial localization in NMR spectroscopy in vivo. <em>Annals of the New York Academy of Sciences</em>, 508(1), 333–348. <a href="https://doi.org/10.1111/j.1749-6632.1987.tb32915.x">https://doi.org/10.1111/j.1749-6632.1987.tb32915.x</a></p>
    <p>Edden, R. A. E., Oeltzschner, G., Harris, A. D., Puts, N. A. J., Chan, K. L., Boer, V. O., Schär, M., & Barker, P. B. (2016). Prospective frequency correction for macromolecule-suppressed GABA editing at 3T. <em>Journal of Magnetic Resonance Imaging</em>, 44(6), 1474–1482.. <a href="https://doi.org/10.1002/jmri.25304">https://doi.org/10.1002/jmri.25304</a></p>
    <p>Harris, A. D., Glaubitz, B., Near, J., John Evans, C., Puts, N. A. J., Schmidt-Wilcke, T., Tegenthoff, M., Barker, P. B., & Edden, R. A. E. (2014). Impact of frequency drift on gamma-aminobutyric acid-edited MR spectroscopy. <em>Magnetic Resonance in Medicine</em>, 72(4), 941–948. <a href="https://doi.org/10.1002/mrm.25009">https://doi.org/10.1002/mrm.25009</a></p>
    <p>Hui, S. C. N., Murali-Manohar, S., Zöllner, H. J., Hupfeld, K. E., Davies-Jenkins, C. W., Gudmundson, A. T., Song, Y., Yedavalli, V., Wisnowski, J. L., Gagoski, B., Oeltzschner, G., & Edden, R. A. E. (2024). Integrated Short-TE and Hadamard-edited Multi-Sequence (ISTHMUS) for advanced MRS. <em>Journal of Neuroscience Methods</em>, 409(110206), 110206. <a href="https://doi.org/10.1016/j.jneumeth.2024.110206">https://doi.org/10.1016/j.jneumeth.2024.110206</a></p>
    <p>Oeltzschner, G., Saleh, M. G., Rimbault, D., Mikkelsen, M., Chan, K. L., Puts, N. A. J., & Edden, R. A. E. (2019). Advanced Hadamard-encoded editing of seven low-concentration brain metabolites: Principles of HERCULES. <em>NeuroImage</em>, 185, 181–190. <a href="https://doi.org/10.1016/j.neuroimage.2018.10.002">https://doi.org/10.1016/j.neuroimage.2018.10.002</a></p>
    <p>Oeltzschner, G., Zöllner, H. J., Hui, S. C. N., Mikkelsen, M., Saleh, M. G., Tapper, S., & Edden, R. A. E. (2020). Osprey: Open-source processing, reconstruction & estimation of magnetic resonance spectroscopy data. Journal of Neuroscience Methods, 343(108827), 108827. <a href="https://doi.org/10.1016/j.jneumeth.2020.108827">https://doi.org/10.1016/j.jneumeth.2020.108827</a></p>
    <p>Träber, F., Block, W., Lamerichs, R., Gieseke, J., & Schild, H. H. (2004). 1H metabolite relaxation times at 3.0 tesla: Measurements of T1 and T2 values in normal brain and determination of regional differences in transverse relaxation. <em>Journal of Magnetic Resonance Imaging</em>, 19(5), 537–545. <a href="https://doi.org/10.1002/jmri.20053">https://doi.org/10.1002/jmri.20053</a></p>
    <p>Zöllner, H. J., Davies-Jenkins, C. W., Lee, E. G., Hendrickson, T. J., Clarke, W. T., Edden, R. A. E., Wisnowski, J. L., Gudmundson, A. T., & Oeltzschner, G. (2023). Continuous automated analysis workflow for MRS studies. Journal of Medical Systems, 47(1), 69. <a href="https://doi.org/10.1007/s10916-023-01969-6">https://doi.org/10.1007/s10916-023-01969-6</a></p>
</div>
<br>



 
