# Quantitative MRI (qMRI)


## Data Processing

### Relaxation (T1/T2) & Proton Density (PD) Maps 

For the HBCD study, the MRI working group adopted 3D-QALAS ([Kvernby et al. 2014](https://doi.org/10.1186/s12968-014-0102-0)), a time-efficient 3D method that combines interleaved Look-Locker acquisition with a T2-preparation pulse. This approach simultaneously estimates longitudinal (T1) and transverse (T2) relaxation times, as well as proton density (PD) maps, from a single scan, and has been validated across major MRI vendors ([Fujita et al. 2019](https://doi.org/10.1016/j.mri.2019.08.031)).

Conventional neuroimaging typically relies on qualitative relaxation time-weighted images, e.g, T1w and T2w images, which reflect relative differences in relaxation times, but are strongly influenced by sequence parameters, participant positioning, and scanner hardware. These dependencies complicate biological interpretation and hinder quantitative comparisons across participants, sessions, and sites. The issue is particularly acute in pediatric neuroimaging, where rapid changes in free water distribution, iron, and myelination alter image contrast as a function of age. By directly measuring relaxation properties, quantitative MRI overcomes many of these limitations and provides more reliable markers of brain tissue microstructure ([Deoni 2010](https://doi.org/10.1097/RMR.0b013e31821e56d8); [Does 2018](https://doi.org/10.1016/j.neuroimage.2017.12.087)).

### Synthetic T1w/T2w Images

Using 3D-QALAS data with the Synthetic MRI (SyMRI) toolbox, we also generate synthetic T1w (Sy-T1w) and T2w (Sy-T2w) volumes. These are created by substituting quantitative estimates of T1 and T2 relaxation times back into the MR signal equation (Bloch equations) for each sequence. This enables flexible generation of different contrasts without acquiring separate scans.



