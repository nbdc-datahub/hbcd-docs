# Structural & Functional MRI

<p style="color: red;">The information below describes general as well as data acquisition details for structural and functional MRI data. Details of processing and pipeline derivative outputs are described under [Processed Derivatives](mri-proc.md).</p>

## Structural MRI (sMRI)

HBCD protocols for structural MRI were informed by recent large-scale developmental neuroimaging studies including [ABCD](https://abcdstudy.org/), HCP Lifespan, and BCP ([Howell et al., 2019](https://pubmed.ncbi.nlm.nih.gov/29578031/)). These studies laid critical foundation for the development of well-validated, high-resolution protocols harmonized across all three major scanner vendors ([Casey et al., 2018](https://doi.org/10.1016/j.dcn.2018.03.001)). In addition, the findings emphasized the importance of T2w acquisition in infants due to suboptimal grey/white T1w contrast resulting from incomplete myelination ([Howell et al., 2019](https://doi.org/10.1016/j.neuroimage.2018.03.049), [Myers et al., 2023](https://doi.org/10.1016/j.neuroimage.2018.03.049)).

## Quantitative MRI (qMRI)

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

### Relaxation (T1/T2) & Proton Density (PD) Maps 

For the HBCD study, the MRI working group adopted 3D-QALAS ([Kvernby et al. 2014](https://doi.org/10.1186/s12968-014-0102-0)), a time-efficient 3D method that combines interleaved Look-Locker acquisition with a T2-preparation pulse. This approach simultaneously estimates longitudinal (T1) and transverse (T2) relaxation times, as well as proton density (PD) maps, from a single scan, and has been validated across major MRI vendors ([Fujita et al. 2019](https://doi.org/10.1016/j.mri.2019.08.031)).

Conventional neuroimaging typically relies on qualitative relaxation time-weighted images, e.g, T1w and T2w images, which reflect relative differences in relaxation times, but are strongly influenced by sequence parameters, participant positioning, and scanner hardware. These dependencies complicate biological interpretation and hinder quantitative comparisons across participants, sessions, and sites. The issue is particularly acute in pediatric neuroimaging, where rapid changes in free water distribution, iron, and myelination alter image contrast as a function of age. By directly measuring relaxation properties, quantitative MRI overcomes many of these limitations and provides more reliable markers of brain tissue microstructure ([Deoni 2010](https://doi.org/10.1097/RMR.0b013e31821e56d8); [Does 2018](https://doi.org/10.1016/j.neuroimage.2017.12.087)).

### Synthetic T1w/T2w Images

Using 3D-QALAS data with the Synthetic MRI (SyMRI) toolbox, we also generate synthetic T1w (Sy-T1w) and T2w (Sy-T2w) volumes. These are created by substituting quantitative estimates of T1 and T2 relaxation times back into the MR signal equation (Bloch equations) for each sequence. This enables flexible generation of different contrasts without acquiring separate scans.


<div id="qmri-derivs" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">qMRI Processing & Derivatives (SyMRI/qMRI PostProc</span>
  <a class="anchor-link" href="#qmri-derivs" title="Copy link">
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

## Functional MRI (fMRI)

<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Responsible Use Warning</i></span>
  <a class="anchor-link" href="#alert" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p>Head motion is a serious issue for neuroimaging, and especially for resting state fMRI. It creates brain-wide artifactual effects including elevated short-distance connectivity and attenuated long-distance connectivity (<a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">Power et al. 2012</a>). In order to guard against artifactual effects due to head motion, researchers typically implement a variety of strategies that operate at multiple points of the data collection and processing pipeline, with guidance regularly evolving over time (<a href="https://doi.org/10.1016/j.neuroimage.2013.08.048">Power et al. 2014</a>; <a href="https://doi.org/10.1016/j.neuroimage.2014.10.044">2015</a>; <a href="https://doi.org/10.1016/j.neuroimage.2012.08.052">Satterthwaite et al. 2013</a>; <a href="https://doi.org/10.1093/cercor/bhw253">Siegel et al. 2017</a>; <a href="https://doi.org/10.1016/j.neuroimage.2020.116866">Gratton et al. 2020</a>). Some of these strategies include discarding entire runs of data that exceed certain motion thresholds and discarding individual functional imaging frames that are proximal to motion events (i.e., “motion censoring”). These strategies in particular typically lead to the exclusion of some participants from further analysis for lack of sufficient data.</p> <p>Levels of head motion differ according to demographic factors such as sex, race/ethnicity, and SES (<a href="https://doi.org/10.1007/s11682-022-00665-2">Cosgrove et al., 2022</a>). Therefore, strategies to deal with head motion may introduce questions of fairness and may lead to differential exclusions across demographic groups. In addition, motion censoring causes sessions to vary by the amount of data remaining. Such variability may continue to inflate findings especially in the presence of conditions that may correlate with the motion artifact like autism or ADHD (<a href="https://doi.org/10.1093/cercor/bhw403">Eggebrecht, 2017</a>). The amount of data remaining influences the variation in the connectivity calculations by affecting the degrees of freedom. Therefore, even after motion censoring, issues concerning fairness may persist when examining factors that might be affected by motion like sex, race/ethnicity, SES, and BMI (<a href="https://doi.org/10.1007/s11682-022-00665-2">Cosgrove et al., 2022</a>). One strategy that avoids this confound is to strictly control the degrees of freedom, where functional connectivity measures are calculated with the exact same amount of data. Researchers should assess whether control of artifactual effects of head motion effects can be achieved by alternative means that mitigate this impact. Examples of such strategies could include data augmentation approaches such as sampling from other datasets, data processing strategies like the include use of ICA-based denoising (<a href="https://doi.org/10.1016/j.neuroimage.2015.02.064">Pruim et al., 2015a</a>; <a href="https://doi.org/10.1016/j.neuroimage.2015.02.063">2015b</a>), use of bootstrap aggregation (<a href="https://doi.org/10.1101/2024.06.22.600221">Ramduny et al., 2024</a>), or the creation of “pseudo-rest” by removing task signals from the task data (<a href="https://doi.org/10.1016/j.neuroimage.2006.11.051">Fair et al. 2007</a>), or post-hoc approaches like propensity weighting.</p> 
<p>Researchers interested in examining brain-behavior associations or multivariate predictions should follow strategies such as those in <a href="https://doi.org/10.1093/cercor/bhw403">Eggebrecht 2017</a> to: 1) assess how missing data impacts dependent, independent variables and covariates, 2) examine the association between the degrees of freedom and non-FC variables, 3) use trimmed FC measures when needed to mitigate artifacts due to data quality.</p>
</div>

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p><b>Philips signal intensity clipping - Overview</b><br>
A subset of Philips fMRI scans is affected by a signal intensity clipping issue. Due to a scaling error during real-time reconstruction, raw pixel intensity values above 4095 are capped, resulting in hyperintense regions that obscure gray/white matter signal. This artifact can significantly impact BOLD registration and derived measures such as ROI-to-ROI correlations.</p>
<p><b>Detection and Prevalence</b><br>
The artifact was initially detected during HBCD pilot scanning through manual quality control (QC) and addressed with a protocol patch applied at most Philips sites prior to the start of the HBCD main study. However, the patch was implemented later (October 2024) at sites VAN and CCH, leading to residual cases at these locations. Severe cases typically fail manual QC (QC=0), while less severe cases often pass (QC=1), as they may not be visually apparent. Overall, ~20% of scans from VAN and CCH show some degree of clipping, with ~6% classified as severe enough to fail QC. Updates to real-time reconstruction are in development to recover affected data. In the meantime, only scans that pass QC, including those with mild clipping, are included in the release.</p>
<p><b>How to Identify Affected Scans</b><br>
Clipping severity can be estimated using the ratio of median to maximum image intensity and the fraction of voxels at maximum intensity within the brain mask (both available in the <a href="../../../datacuration/file-based-data/#participant-session-scan-level-data"><code>scans.tsv</code> file</a>):</p> 
<ul>
<li><i>Severe clipping</i>: (brain_median / brain_max) > 0.8 AND brain_fvox_max > 0.001</li> 
<li><i>Potential clipping</i>: (brain_median / brain_max) > 0.5 AND brain_fvox_max > 0.001</li> 
</ul>
</div>
<p></p>

fMRI measures functional brain activity based on the blood oxygen level–dependent (BOLD) signal. Resting-state (rs-fMRI) data is acquired at 2mm isotropic resolution with a repetition time (TR) of 1725 ms and multi-band (MB) factor of 4. A minimum of 2 runs are acquired (during sleep for infants <30 months old), each lasting 7.5 minutes. [FIRMM](https://firmm.readthedocs.io/) ([Dosenbach et al., 2017](https://doi.org/10.1016/j.neuroimage.2017.08.025)) is used to monitor head motion in real time and additional runs are acquired as needed to obtain at least 7.5 minutes of low-motion data (FD < 0.3 mm) across runs.

### Quality Control Summary Statistics

<div id="fconn" class="static-banner" style="border-left: 5px solid #199bd6;">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
    <span class="text">Functional Connectivity as Data Quality Improves</span>
    <a class="anchor-link" href="#fconn" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
</div>
<div class="table-static-content">
<p>Average functional connectivity matrices were computed using the Gordon parcellation from <a href="../mri-proc/#xcp-d">XCP-D derivatives</a> for V02 sessions with data inclusion based on various thresholds of BrainSwipes QC results (<code>img_brainswipes_xcpd-bold</code>; <a href="../qc/#brainswipes">see details</a>). Functional connectivity patterns remained consistent even when incorporating data with lower QC scores, suggesting robustness to mild quality variations.</p>
<p><strong>Connectivity matrices as data quality improves (Left -> Right) based on QC thresholds of 0.1, 0.5, and 0.9:</strong></p>
<img src="../images/fconn_qc.png" style="width: 90%;" class="center">
<br>
</div>
<p></p>

## Derivatives


## MRI Derivatives Quick Start Guide

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning: Avoid Use of V02 Derivatives Processed Via Infant FreeSurfer Workflow</span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p><b>Summary</b><br>
Data acquired at visit V02 (from neonates/0-1 months old) was processed through Infant fMRIPrep via two separate surface reconstruction workflows - Infant FreeSurfer and M-CRIB-S (see <a href="#m-crib-s-freesurfer">M-CRIB-S & FreeSurfer Surface Reconstruction Methods</a> above). Though Infant FreeSurfer outputs are included in the release, preliminary reviews and QC results made it clear that M-CRIB-S produced much higher quality outputs compared to Infant FreeSurfer at the neonatal age range. <b>We therefore strongly recommend using V02 data processed with M-CRIB-S instead for all analyses with V02 data.</b>. The following section outlines the reasoning for this.</p>

<p><b>Neonatal Data Processing</b><br>
</b> Expert visual review as well as preliminary BrainSwipes QC results indicate that V02 data processed with Infant FreeSurfer generally yield lower quality surface reconstructions. Reasons for this include:</p> 
<ul>
<li>T2w images are generally higher contrast in neonates and infants, which improves segmentation and surface reconstruction quality</li>
<li>M-CRIB-S leverages T2w images for surface reconstruction, whereas Infant FreeSurfer relies solely on T1w images, which are often lower contrast at these ages. <a href="https://doi.org/10.1101/2025.05.14.654069">Goncalves et al., 2025</a> similarly reports that M-CRIB-S is optimal for neonates (optimal age range ≤ 5 month old) vs infant Freesurfer (optimal ages ≥ 3 months).</li>
<li>Not all sessions include a T1w. For HBCD, T2w images were prioritized over T1w during acquisition for visit V02, which were acquired at the end of the session if time permitted.</li>
</ul>

<p><b>BrainSwipes QC Results</b><br>
Approximately 30% of the visual reports produced across subject sessions were assigned QC scores based on BrainSwipes review. As early results indicated high rates of QC failure, we chose not to complete manual review of the remaining data. Based on the 30% of the sessions reviewed, a total of ~50% of the session derivatives for this group were removed across pipeline derivative outputs due to unusually high QC failures based on BrainSwipes results. Due to the expected high rates of failure for this group, structural and functional data flagged by BrainSwipes results underwent very minimal additional expert review. Instead, sessions were in large part excluded based on the BrainSwipes QC results alone. See <a href="../exclusion-criteria/#processed-data-exclusion-criteria">Processed Data Exclusion Criteria</a> for details.</p>

<p><b>Implications for Corresponding V02 Data Processed via M-CRIB-S Workflow</b><br>
<i>Note that poor quality T1w images can also negatively impact data processed via the M-CRIB-S workflow</i> (despite its reliance on the T2w and brain segmentation). BIBSNet derives the brain segmentation based on both the T1w and T2w if both are available, so if the T1w data quality is poor, this may result in lower quality segmentations (particularly when the poor T1w quality results in poor T2w-to-T1w registration of the data fed into the BIBSNet model for segmentation).</p> 
</div>

Below is a summary of key MRI derivatives used for **structural morphology** and **resting-state functional MRI (rsfMRI) functional connectivity** analyses. Key derivatives, produced by the **XCP-D** pipeline, include volumetric and surface-based time series for each participant. The data release also includes dense and parcellated time series with at least 2.5 minutes of low-motion data (FD>0.3), functional connectivity matrices, regional homogeneity values, and amplitude of low-frequency fluctuation values. 

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

<style>
    .compact-table-clean {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
}

.compact-table-clean th {
  text-align: left;
  font-weight: 600;
  padding: 0.6em 0.5em;
  border-bottom: 2px solid #e5e7eb;
}

.compact-table-clean td {
  padding: 0.65em 0.5em;
  vertical-align: top;
  word-break: break-word;
}

.compact-table-clean tr:not(:last-child) td {
  border-bottom: 1px solid #f0f0f0;
}

.compact-table-clean code {
  font-weight: 600;
  font-size: 0.95em;
}

.atlas-type {
  font-weight: 600;
}

.atlas-details {
  color: #6b7280;
  font-size: 0.85em;
  display: block;
  margin-top: 0.15em;
}

.atlas-use {
  display: inline-block;
  margin-top: 0.35em;
  font-size: 0.8em;
  color: #0f766e;
  background: #eef6f6;
  padding: 2px 6px;
  border-radius: 6px;
}
</style>
<table class="compact-table-clean">
<thead>
<tr>
  <th style="width: 22%;">Atlas</th>
  <th>Description</th>
</tr>
</thead>
<tbody>

<tr>
  <td><code>Glasser</code></td>
  <td>
    <span class="atlas-type">Multimodal anatomical atlas (population-level)</span>
    <span class="atlas-details">
      Derived from multimodal MRI data (<a href="https://doi.org/10.1038/nature18933">Glasser et al., 2016</a>)
    </span>
    <span class="atlas-use">Surface-based morphology, population-level structure</span>
  </td>
</tr>
<tr>
  <td><code>Gordon</code></td>
  <td>
    <span class="atlas-type">Functional atlas (333 ROIs)</span>
    <span class="atlas-details">
      rs-fMRI boundary detection (120 young adults, ~14 min per subject;
      <a href="https://doi.org/10.1093/cercor/bhu239">Gordon et al., 2016</a>)
    </span>
    <span class="atlas-use">Functional network mapping, group-level FC analyses</span>
  </td>
</tr>
<tr>
  <td><code>HCP</code></td>
  <td>
    <span class="atlas-type">Multimodal cortical atlas (360 ROIs)</span>
    <span class="atlas-details">
      Combined task, resting-state, and diffusion MRI (210 young adults;
      <a href="https://doi.org/10.1016/j.neuroimage.2013.04.127">Glasser et al., 2013</a>)
    </span>
    <span class="atlas-use">Cross-modal structural–functional alignment</span>
  </td>
</tr>
<tr>
  <td><code>MIDB</code></td>
  <td>
    <span class="atlas-type">Precision functional atlas (individualized)</span>
    <span class="atlas-details">
      Derived from ABCD data using a 75% probability threshold
      (<a href="https://doi.org/10.1038/s41593-024-01596-5">Hermosillo et al., 2024</a>)
    </span>
    <span class="atlas-use">Individualized functional network mapping</span>
  </td>
</tr>
<tr>
  <td><code>Myers-Labonte</code></td>
  <td>
    <span class="atlas-type">Infant probabilistic functional atlas</span>
    <span class="atlas-details">
      50% probability threshold; infant population
      (<a href="https://doi.org/10.1101/2023.11.10.566629">Myers et al., 2023</a>)
    </span>
    <span class="atlas-use">Infant functional network mapping</span>
  </td>
</tr>
<tr>
  <td><code>Tian</code></td>
  <td>
    <span class="atlas-type">Subcortical parcellation atlas</span>
    <span class="atlas-details">
      High-resolution subcortical segmentation
      (<a href="https://doi.org/10.1038/s41593-020-00711-6">Tian et al., 2020</a>)
    </span>
    <span class="atlas-use">Subcortical connectivity analyses</span>
  </td>
</tr>
<tr>
  <td><code>4S{1-10}56Parcels</code></td>
  <td>
    <span class="atlas-type">Multimodal atlas (multi-resolution)</span>
    <span class="atlas-details">
      Schaefer cortical parcellations (100–1000 parcels) supplemented with subcortical and cerebellar regions
      (<a href="https://github.com/PennLINC/AtlasPack">AtlasPack</a>)
    </span>
    <span class="atlas-use">Cross-modality alignment across XCP-D, QSIPrep, and ASLPrep</span>
  </td>
</tr>
</tbody>
</table>
</div>


<div id="fmri-ref" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-book-open"></i></span>
  <span class="text-with-link">
  <span class="text">References</span>
  <a class="anchor-link" href="#fmri-ref" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<div class="references">
<p>STRUCTURAL MRI</p>
  <p>Andersen, M., Björkman-Burtscher, I. M., Marsman, A., Petersen, E. T., & Boer, V. O. (2019). Improvement in diagnostic quality of structural and angiographic MRI of the brain using motion correction with interleaved, volumetric navigators.
    <em>PLoS One</em>, 14(5), e0217145. <a href="https://doi.org/10.1371/journal.pone.0217145">https://doi.org/10.1371/journal.pone.0217145</a></p>
    <p>Casey, B. J., Cannonier, T., Conley, M. I., Cohen, A. O., Barch, D. M., Heitzeg, M. M., Soules, M. E., Teslovich, T., Dellarco, D. V., Garavan, H., Orr, C. A., Wager, T. D., Banich, M. T., Speer, N. K., Sutherland, M. T., Riedel, M. C., Dick, A. S., Bjork, J. M., Thomas, K. M., … ABCD Imaging Acquisition Workgroup. (2018). The Adolescent Brain Cognitive Development (ABCD) study: Imaging acquisition across 21 sites. <em>Developmental Cognitive Neuroscience</em>, 32, 43–54. <a href="https://doi.org/10.1016/j.dcn.2018.03.001">https://doi.org/10.1016/j.dcn.2018.03.001</a></p>
    <p>Howell, B. R., Styner, M. A., Gao, W., Yap, P.-T., Wang, L., Baluyot, K., Yacoub, E., Chen, G., Potts, T., Salzwedel, A., Li, G., Gilmore, J. H., Piven, J., Smith, J. K., Shen, D., Ugurbil, K., Zhu, H., Lin, W., & Elison, J. T. (2019). The UNC/UMN Baby Connectome Project (BCP): An overview of the study design and protocol development. <em>NeuroImage</em>, 185, 891–905. <a href="https://doi.org/10.1016/j.neuroimage.2018.03.049">https://doi.org/10.1016/j.neuroimage.2018.03.049</a></p>
    <p>Myers, M. J., Labonte, A. K., Gordon, E. M., Laumann, T. O., Tu, J. C., Wheelock, M. D., Nielsen, A. N., Schwarzlose, R., Camacho, M. C., Warner, B. B., Raghuraman, N., Luby, J. L., Barch, D. M., Fair, D. A., Petersen, S. E., Rogers, C. E., Smyser, C. D., & Sylvester, C. M. (2023). Functional parcellation of the neonatal brain. In <em>bioRxivorg</em>. <a href="https://doi.org/10.1101/2023.11.10.566629">https://doi.org/10.1101/2023.11.10.566629</a></p>
    <p>Tisdall, M. D., Reuter, M., Qureshi, A., Buckner, R. L., Fischl, B., & van der Kouwe, A. J. W. (2016). Prospective motion correction with volumetric navigators (vNavs) reduces the bias and variance in brain morphometry induced by subject motion. <em>Neuroimage</em>, 127, 11-22. <a href="https://doi.org/10.1016/j.neuroimage.2015.11.054">https://doi.org/10.1016/j.neuroimage.2015.11.054</a></p>
    <p>White, N., Roddey, C., Shankaranarayanan, A., Han, E., Rettmann, D., Santos, J., Kuperman, J., & Dale, A. (2010). PROMO: Real-time prospective motion correction in MRI using image-based tracking. <em>Magnetic Resonance in Medicine</em>, 63(1), 91–105. <a href="https://doi.org/10.1002/mrm.22176">https://doi.org/10.1002/mrm.22176</a></p>
    <br>
    <p>QUANTITATIVE MRI</p>
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
<br>
<p>FUNCTIONAL MRI</p>
<p>Cosgrove KT, McDermott TJ, White EJ, Mosconi MW, Thompson WK, Paulus MP, Cardenas-Iniguez C, Aupperle RL. Limits to the generalizability of resting-state functional magnetic resonance imaging studies of youth: An examination of ABCD Study® baseline data. <i>Brain Imaging Behav</i> 16, 1919-1925, 2022. <a href="https://doi.org/10.1007/s11682-022-00665-2" target="_blank">doi: 10.1007/s11682-022-00665-2</a></p>
  <p>Dean III, D. C., Tisdall, M. D., Wisnowski, J. L., Feczko, E., Gagoski, B., Alexander, A. L., ... &amp; HBCD MRI Working Group. (2024). Quantifying brain development in the HEALthy Brain and Child Development (HBCD) Study: The magnetic resonance imaging and spectroscopy protocol. <em>Developmental Cognitive Neuroscience</em>, 70, 101452. <a href="https://doi.org/10.1016/j.dcn.2024.101452">10.1016/j.dcn.2024.101452</a></p>
  <p>Dosenbach, N. U. F., Koller, J. M., Earl, E. A., Miranda-Dominguez, O., Klein, R. L., Van, A. N., Snyder, A. Z., Nagel, B. J., Nigg, J. T., Nguyen, A. L., Wesevich, V., Greene, D. J., & Fair, D. A. (2017). Real-time motion analytics during brain MRI improve data quality and reduce costs. <em>NeuroImage</em>, 161, 80-93. <a href="https://doi.org/10.1016/j.neuroimage.2017.08.025">https://doi.org/10.1016/j.neuroimage.2017.08.025</a></p>
  <p>Eggebrecht, A. T., Elison, J. T., Feczko, E., Todorov, A., Wolff, J. J., Kandala, S., Adams, C. M., Snyder, A. Z., Lewis, J. D., Estes, A. M., Zwaigenbaum, L., Botteron, K. N., McKinstry, R. C., Constantino, J. N., Evans, A., Hazlett, H. C., Dager, S., Paterson, S. J., Schultz, R. T., … Pruett, J. R., Jr. (2017). Joint attention and brain functional connectivity in infants and toddlers. <i>Cerebral Cortex (New York, N.Y.: 1991)</i>, 27(3), 1709–1720. <a href="https://doi.org/10.1093/cercor/bhw403" target="_blank">doi: 10.1093/cercor/bhw403</a></p>
  <p>Fair, D. A., Schlaggar, B. L., Cohen, A. L., Miezin, F. M., Dosenbach, N. U. F., Wenger, K. K., Fox, M. D., Snyder, A. Z., Raichle, M. E., & Petersen, S. E. (2007). A method for using blocked and event-related fMRI data to study “resting state” functional connectivity. <i>NeuroImage</i>, 35(1), 396–405. <a href="https://doi.org/10.1016/j.neuroimage.2006.11.051" target="_blank">doi: 10.1016/j.neuroimage.2006.11.051</a></p>
  <p>Gratton, C., Dworetsky, A., Coalson, R. S., Adeyemo, B., Laumann, T. O., Wig, G. S., Kong, T. S., Gratton, G., Fabiani, M., Barch, D. M., Tranel, D., Miranda-Dominguez, O., Fair, D. A., Dosenbach, N. U. F., Snyder, A. Z., Perlmutter, J. S., Petersen, S. E., & Campbell, M. C. (2020). Removal of high frequency contamination from motion estimates in single-band fMRI saves data without biasing functional connectivity. <i>NeuroImage</i>, 217(116866), 116866. <a href="https://doi.org/10.1016/j.neuroimage.2020.116866" target="_blank">doi: 10.1016/j.neuroimage.2020.116866</a></p>
  <p>Power, J. D., Barnes, K. A., Snyder, A. Z., Schlaggar, B. L., & Petersen, S. E. (2012). Spurious but systematic correlations in functional connectivity MRI networks arise from subject motion. <i>NeuroImage</i>, 59(3), 2142–2154. <a href="https://doi.org/10.1016/j.neuroimage.2011.10.018" target="_blank">doi: 10.1016/j.neuroimage.2011.10.018</a></p>
  <p>Power, J. D., Mitra, A., Laumann, T. O., Snyder, A. Z., Schlaggar, B. L., & Petersen, S. E. (2014). Methods to detect, characterize, and remove motion artifact in resting state fMRI. <i>NeuroImage</i>, 84, 320–341. <a href="https://doi.org/10.1016/j.neuroimage.2013.08.048" target="_blank">doi: 10.1016/j.neuroimage.2013.08.048</a></p>
  <p>Power, J. D., Schlaggar, B. L., & Petersen, S. E. (2015). Recent progress and outstanding issues in motion correction in resting state fMRI. <i>NeuroImage</i>, 105, 536–551. <a href="https://doi.org/10.1016/j.neuroimage.2014.10.044" target="_blank">doi: 10.1016/j.neuroimage.2014.10.044</a></p>
  <p>Pruim RHR, Mennes M, van Rooij D, Llera A, Buitelaar JK, Beckmann CF. ICA-AROMA: A robust ICA-based strategy for removing motion artifacts from fMRI data. <i>Neuroimage</i> 112, 267-277, 2015a. <a href="https://doi.org/10.1016/j.neuroimage.2015.02.064" target="_blank">doi: 10.1016/j.neuroimage.2015.02.064</a></p>
  <p>Pruim RHR, Mennes M, Buitelaar JK, Beckmann CF. Evaluation of ICA-AROMA and alternative strategies for motion artifact removal in resting state fMRI. <i>Neuroimage</i> 112, 278-287, 2015b. <a href="https://doi.org/10.1016/j.neuroimage.2015.02.063" target="_blank">doi: 10.1016/j.neuroimage.2015.02.063</a></p>
  <p>Ramduny, J., Uddin, L. Q., Vanderwal, T., Feczko, E., Fair, D. A., Kelly, C., & Baskin-Sommers, A. (2024). Increasing the representation of minoritized youth for inclusive and reproducible brain-behavior associations. <i>bioRxiv</i>. <a href="https://doi.org/10.1101/2024.06.22.600221" target="_blank">doi: 10.1101/2024.06.22.600221</a></p>
  <p>Satterthwaite TD, Elliott MA, Gerraty RT, Ruparel K, Loughead J, Calkins ME, Eickhoff SB, Hakonarson H, Gur RC, Gur RE, Wolf DH. An improved framework for confound regression and filtering for control of motion artifact in the preprocessing of resting-state functional connectivity data. <i>Neuroimage</i> 64, 240-256, 2013. <a href="https://doi.org/10.1016/j.neuroimage.2012.08.052" target="_blank">doi: 10.1016/j.neuroimage.2012.08.052</a></p>
  <p>Siegel JS, Mitra A, Laumann TO, Seitzman BA, Raichle M, Corbetta M, Snyder AZ. Data Quality Influences Observed Links Between Functional Connectivity and Behavior. <i>Cereb Cortex</i> 27, 4492-4502, 2017. <a href="https://doi.org/10.1093/cercor/bhw253" target="_blank">doi: 10.1093/cercor/bhw253</a></p>
</div>
</div>