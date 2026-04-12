# HBCD Study MRI Protocols
<!-- <meta http-equiv="refresh" content="0; url=https://hbcdsequences.readthedocs.io"> -->

On this page we provide a high-level summary of HBCD Study MRI protocols and acquisition parameters as described in <a href="https://doi.org/10.1016/j.dcn.2024.101452">Dean et al. 2024</a>. **See the external [HBCD Study MRI Protocols](https://hbcdsequences.readthedocs.io) documentation for full protocols, sequence installation, and operation instructions.**

## Structural MRI
Key features of the HBCD T1w and T2w structural imaging protocols include:

 - 0.8 mm isotropic resolution
 - Compressed SENSE reconstruction enabling high acceleration and shorter acquisition times (<9 minutes total for T1w and T2w; see vendor-specific pages for details)
 - Embedded navigators for motion tracking during structural imaging ([White et al., 2010](https://doi.org/10.1002/mrm.22176), [Tisdall et al., 2016](https://doi.org/10.1016/j.neuroimage.2015.11.054), [Andersen et al., 2019](https://doi.org/10.1371/journal.pone.0217145)). 
 <!-- In the current release, scans were not prospectively motion-corrected, though this is planned for future releases. -->
 - Harmonization approach similar to the [ABCD Study](https://nbdc-splash-beta.lassoinformatics.com/abcd-study):
        - T1w: contrast-relevant parameters matched as closely as possible across vendors
        - T2w: vendor-specific parameters selected to achieve comparable contrast and SNR, accounting for differences in 3D T2w pulse sequence implementation

## Quantitative MRI
### QALAS
QALAS is a multi-contrast MRI sequence that produces five brain volumes using turbo-flash readouts with varying T1 and T2 weightings (acquisition time ~5 min for Siemens and ~4 min for GE/Philips). These volumes are combined to estimate T1, T2, and proton density (PD) maps. The sequence starts with a T2-preparation pulse, which adds T2 weighting to the first volume. An inversion pulse follows, imparting T1 weighting to the next four volumes.

<p style="margin-bottom: 0;"><b>QALAS Pulse Sequence Diagram</b> (<i><a href="https://onlinelibrary.wiley.com/doi/10.1002/mrm.29939">Fujita et al., 2024</a> Figure. 1</i>)</p>
<img src="../images/qalas_Fig1.png" style="max-width:90%; height:auto;">

### B1+ Fieldmap
The HBCD protocol includes a short B1+ field map acquisition (~30–45 seconds across all scanner types) to calibrate flip angle measurements, which can vary spatially due to B1+ field inhomogeneity. This calibration is required for accurate T1, T2, and PD estimation. Because the transmit B1+ field varies smoothly across space, coarse spatial resolution is sufficient, enabling rapid acquisition. Vendor-specific implementations in the HBCD protocol include Actual Flip Angle Imaging (AFI) ([Yarnykh 2007](https://doi.org/10.1002/mrm.21120)) for GE and Philips, and a pre-saturation turbo-FLASH readout for Siemens.

## Functional MRI
Resting-state (rs-fMRI) data is acquired at 2mm isotropic resolution with a repetition time (TR) of 1725 ms and multi-band (MB) factor of 4. A minimum of 2 runs are acquired (during sleep for infants <30 months old), each lasting 7.5 minutes. [FIRMM](https://firmm.readthedocs.io/) ([Dosenbach et al., 2017](https://doi.org/10.1016/j.neuroimage.2017.08.025)) is used to monitor head motion in real time, quantified by framewise displacement (FD). Additional runs are acquired as needed to obtain at least 7.5 minutes of low-motion data (FD < 0.3 mm) across runs. Each rs-fMRI run is preceded by acquisition of single-shot spin-echo (SE) EPI images with both forward and reverse phase-encoding directions, which are used for distortion correction.

<!-- <div style="display: flex; align-items: center; gap: 20px;">
  <div style="flex: 1;">
    <p>
      fMRI is a measure of functional activity based on the blood oxygen level dependent (BOLD). BOLD signal is measured at each voxel in 2mm isotropic space with a repetition time (TR) of 1725 ms and multi-band (MB) factor of 4. 
    </p>
    <p>
      A minimum of two resting state (rs) fMRI runs are acquired during sleep (for infants &lt;30 months old) lasting 
      7.5 minutes each (<b>Figure 1A</b>). <a href="https://firmm.readthedocs.io/">FIRMM software</a> 
      (Dosenbach et al. 2017) is used to monitor motion, as quantified by framewise displacement (FD), 
      in real time, and additional runs are acquired as needed to obtain a minimum total of 7.5 minutes of 
      low-motion (FD &lt;0.3 mm) data across runs (<b>Figure 1B</b>).
    </p>
    <p>
      Each rsfMRI run is additionally preceded by acquisition of single shot spin-echo (SE) EPI images with same 
      and reversed polarity phase encoding gradients with which to perform distortion correction (<b>Figure 1C</b>). 
      Additional details are available at <a href="https://doi.org/10.1016/j.dcn.2024.101452">Dean et al. 2024</a>.
    </p>
  </div>
  <div style="flex: 1; text-align: center;">
    <img src="../images/Deanetal2024_fMRI.jpg" style="max-width: 90%; height:auto;">
    <p style="font-size: 0.9em; margin-top: 5px;">
      <b>Figure 1.</b> HBCD fMRI Acquisition Protocol 
      (<i><a href="https://doi.org/10.1016/j.dcn.2024.101452">Dean et al., 2024</a></i>)
    </p>
  </div>
</div> -->

## Diffusion MRI
The DWI protocol provides diffusion-weighted images that may be used to estimate multiple models of diffusion behavior in the central nervous system. The protocol acquires roughly 140 diffusion-weighted echo planar images at four b-values (diffusion-weighting) between 0 and 3000 s/mm<sup>2</sup> (12-13 minutes total acquisition time). For raw image acquisition, a minimum of 60% of the diffusion-weighted volumes are required to be collected for the acquisition to be deemed successful.

## Magnetic Resonance Spectroscopy (MRS)
The MRS acquisition protocol was optimized to maximize signal-to-noise across multiple low-concentration metabolites while maintaining an acquisition time (TA) under 9 minutes. The MRS acquisition centers on a single voxel Point-RESolved Spectroscopy (PRESS) ([Bottomley, 1987](https://doi.org/10.1111/j.1749-6632.1987.tb32915.x)) localization (30×23×23 mm^3) in the bilateral thalamus, with SVS localizer acquisitions to define the ROI. The ISTHMUS sequence incorporates a short TE (35 ms) unedited block at the beginning of the sequence for optimal measurement of high concentration metabolites, including N-acetylasparte, followed by an advanced Hadamard encoded spectral editing scheme (HERCULES, TE = 80 ms) to derive reliable and reproducible measures of the low-concentration metabolites ([Oeltzschner et al., 2019](https://doi.org/10.1016/j.neuroimage.2018.10.002)).