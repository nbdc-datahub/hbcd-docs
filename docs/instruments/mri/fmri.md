
# Functional MRI

{{ alert_warning(instruments.fmri) }}
{{ data_warning(instruments.fmri) }}
{{ issues_banner() }}

---

## Overview & Acquisition

<!-- ##### Overview & Acquisition -->
{{ instrument_description(instruments.fmri) }}

## Processing & Derivatives

<div class="banner" style="margin-bottom: 1em;"> <span class="emoji"><i class="fa-solid fa-circle-info"></i><i class="fa fa-person-cane"></i></span> <span class="text">Full pipeline configuration details are available on the <a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0/tool_details.html">HBCD Processing site&nbsp;<i style="font-size: 5px;" class="fa-solid fa-up-right-from-square"></i></a></span> </div>

<p style="font-size: 2em; color: red;">ADD OVERVIEW TEXT</p>


### Infant fMRIPrep

<a href="https://nibabies.readthedocs.io/en/latest/">Infant-fMRIPrep</a> (also known as NiBabies) performs minimal structural and functional MRI processing. It is an adapted version of <em>fMRIPrep</em> optimized for infant data processing, using age-appropriate templates and surface reconstruction methods optimized for early development (<a href="https://doi.org/10.1101/2025.05.14.654069">Goncalves et al., 2025</a>). Pipeline outputs include visual quality assessment reports, preprocessed derivatives, and confounds used for denoising in subsequent processing steps.

<div id="nibabies" class="banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa-solid fa-diagram-project"></i></span>
<span class="text-with-link"><span class="text">Infant fMRIPrep Processing Overview</span>
<a class="anchor-link" href="#nibabies" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
<span class="arrow">▸</span></div>
<div class="collapsible-content">
<p><b>Anatomical Preprocessing</b><br>
T1w and T2w images are denoised, bias-corrected, and normalized to the MNI Infant template (0–4.5 yr), then to MNI152 for compatibility with adult datasets. <b><i>Surface reconstruction</i></b> is performed via one of the following methods:</p>
<table class="table-no-vertical-lines">
<tbody>
<tr>
<td><b>M-CRIB-S</b></td>
<td>T2w-based method for neonates (<a href="https://doi.org/10.1038/s41598-020-61326-2">Adamson et al., 2020</a>). Infant fMRIPrep runs a modified <code>MCRIBReconAll</code> workflow that uses the BIBSNet-derived brain segmentation. <i>Optimal age range per <a href="https://doi.org/10.1101/2025.05.14.654069">Goncalves et al., 2025</a>: ≤ 5 months</i></td>
</tr> <tr>
<td><b>Infant FreeSurfer</b></td>
<td>T1w-based method for infants 0-2 years old (<a href="https://doi.org/10.1016/j.neuroimage.2020.116946">Zöllei et al., 2020</a>). Infant fMRIPrep executes <code>infant_recon_all</code> with its default configuration. <i>Optimal age range per <a href="https://doi.org/10.1101/2025.05.14.654069">Goncalves et al., 2025</a>: ≥ 3 months</i></td>
</tr> </tbody>
</table>
<p><b>Functional Processing</b></p>
<ul>
  <li>Motion and distortion correction using fieldmap-based estimation.</li>
  <li>Alignment of functional to anatomical space via boundary-based registration.</li>
  <li>Confound estimation: framewise displacement (FD) and DVARS for motion, CompCor physiological noise regressors, global signals (mean CSF, white matter, and whole brain), and derived regressors (e.g. motion outlier flags for frames exceeding 0.5 mm FD or 1.5 standardized DVARS thresholds)</li>
  <li>Resampling of BOLD data to subject and fsLR-space surfaces, with grayordinates (91k) for surface-based analyses.</li>
</ul>
</div>

<div id="nibabies-derivs" class="banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
  <span class="text">Infant fMRIPrep Derivatives</span>
  <a class="anchor-link" href="#nibabies-derivs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p style="font-size: 1.1em; font-weight: 600;">Overview</p>
<ul>
<li>JSON files excluded for brevity from file trees below</li>
<li>See <a href="../../../datacuration/overview/#filetrees"><i class="fa fa-circle-info"></i> How To Read File Trees</a> for additional guidance</li>
<li>T1w-related files will only be present in the derivatives if a T1w was acquired</li>
</ul>
<pre class="folder-tree" style="font-size: 11px;">
hbcd/
└── derivatives/
    └── nibabies-<span class="var">{HASH}</span>/
        └── sub-[ID]/
            ├── figures/
            ├── ses-[V0X]/
            │   ├── anat/
            │   ├── fmap/
            │   ├── func/
            │   └── log/
            │
            └── sub-[ID]_ses-[V0X]_hash-<span class="var">{HASH}</span>.html

<span class="hashtag"># Label Values Legend</span>
<span class="var">HASH</span>: 0f306a2f , 2afa9081
</pre>
<p style="font-size: 1.1em; font-weight: 600;">Anatomical Folder Details</p>
<pre class="folder-tree" style="font-size: 11px;">
...
└── ses-[V0X]/
    └── anat/
        <span class="hashtag"># Primary volumetric outputs & segmentations</span>
        ├── *_desc-preproc_<span class="var">{T1w|T2w}</span>.nii.gz
        ├── *_space-MNI152NLin6Asym_res-2_desc-preproc_T2w.nii.gz
        ├── *_space-MNI152NLin6Asym_res-2_desc-brain_mask.nii.gz
        ├── *_space-T2w_desc-ribbon_mask.nii.gz
        ├── *_space-<span class="var">{STD_SPACE}</span>_dseg.nii.gz
        ├── *_space-T2w_desc-<span class="var">{aparcaseg|aseg}</span>_dseg.nii.gz
        ├── *_space-<span class="var">{STD_SPACE}</span>_label-<span class="var">{CSF|GM|WM}</span>_probseg.nii.gz
      
        <span class="hashtag"># Transforms</span>
        ├── *_from-<span class="var">{SPACE}</span>_to-T2w_mode-image_xfm.h5
        ├── *_from-T2w_to-<span class="var">{SPACE}</span>_mode-image_xfm.h5
      
        <span class="hashtag"># Surface & CIFTI outputs</span>
        ├── *_hemi-<span class="var">{L|R}</span>_desc-cortex_mask.label.gii
        ├── *_space-fsLR_den-91k_<span class="var">{METRIC}</span>.dscalar.nii 
        ├── *_hemi-<span class="var">{L|R}</span>_<span class="var">{METRIC}</span>.shape.gii
        ├── *_hemi-<span class="var">{L|R}</span>_<span class="var">{inflated|sphere}</span>.surf.gii
        ├── *_hemi-<span class="var">{L|R}</span>_<span class="var">{SURF}</span>.surf.gii
        ├── *_hemi-<span class="var">{L|R}</span>_space-dhcpAsym_den-32k_<span class="var">{SURF}</span>.surf.gii
        └── *_hemi-<span class="var">{L|R}</span>_space-<span class="var">{dhcpAsym|fsaverage}</span>_reg_sphere.surf.gii   
...
<span class="hashtag"># Label Values Legend</span>
File Prefixes (anat/, fmap/ files): sub-[ID]_ses-[V0X]_hash-{HASH}_run-[X]
<span class="var">METRIC</span>: curv , sulc , thickness 
<span class="var">SPACE</span>: fsnative , MNI152NLin6Asym , MNIInfant+1 , T1w
<span class="var">STD_SPACE</span>: MNI152NLin6Asym_res-2 , T2w
<span class="var">SURF</span>: midthickness , pial , white  
</pre>
<p style="font-size: 1.1em; font-weight: 600;">Fieldmap & Functional Folder Details</p>
<pre class="folder-tree" style="font-size: 11px;">
... 
└── ses-[V0X]/
    ├── fmap/
    │   └── *_fmapid-auto[X]_desc-<span class="var">{coeff|epi|preproc}</span>_fieldmap.nii.gz
    │
    └── func/
        <span class="hashtag"># BOLD & masks</span>
        ├── *_desc-<span class="var">{preproc_bold|brain_mask}</span>.nii.gz
        ├── *_space-<span class="var">{STD_SPACE}</span>_boldref.nii.gz
        ├── *_space-<span class="var">{STD_SPACE}</span>_desc-<span class="var">{preproc_bold|brain_mask}</span>.nii.gz

        <span class="hashtag"># Motion-corrected or coregistered outputs</span>
        ├── *_desc-<span class="var">{hmc|coreg}</span>_boldref.nii.gz
        ├── *_from-orig_to-boldref_mode-image_desc-hmc_xfm.txt
        ├── *_from-boldref_to-T2w_mode-image_desc-coreg_xfm.txt
        ├── *_from-boldref_to-auto*_mode-image_xfm.txt

        <span class="hashtag"># Surface & CIFTI outputs</span>
        ├── *_space-fsLR_den-91k_bold.dtseries.nii
        ├── *_hemi-<span class="var">{L|R}</span>_space-fsnative_bold.func.gii 

        <span class="hashtag"># Confounds</span>
        └── *_desc-confounds_timeseries.tsv 

<span class="hashtag"># Label Values Legend</span>
File Prefixes (func/): sub-[ID]_ses-[V0X]_hash-{HASH}_task-rest_dir-PA_run-[X]
<span class="var">STD_SPACE</span>: MNI152NLin6Asym_res-2 , T2w
</pre>
</div>


### XCP-D
<a href="https://xcp-d.readthedocs.io/en/latest/">XCP-D</a> performs functional MRI post-processing and noise regression from Infant-fMRIPrep derivatives, producing cleaned and parcellated data (<a href="#parc">see parcellation atlases</a>) ready for analysis.

<div id="xcpd" class="banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa-solid fa-diagram-project"></i></span>
<span class="text-with-link"><span class="text">XCP-D Processing Overview</span>
<a class="anchor-link" href="#xcpd" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
<span class="arrow">▸</span></div>
<div class="collapsible-content">
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
<li>Parcellated time series are extracted for <a href="#parc">each atlas</a> and pairwise functional connectivity is calculated as the Pearson correlation between regional time series.</li>
<li>Postprocessed derivatives are concatenated across runs.</li>
</ul>
</div>

<div id="xcpd-derivs" class="banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">XCP-D Derivatives</span>
  <a class="anchor-link" href="#xcpd-derivs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<pre style="font-size: 11px;" class="folder-tree">
<span class="hashtag"># JSON files excluded for brevity</span>
<span><a href="../../../datacuration/overview/#filetrees"><i class="fa fa-circle-info"></i> How To Read File Trees →</a></span>

hbcd/
└── derivatives/
    └── xcp_d-<span class="var">{HASH}</span>/
        └── sub-[ID]/
            └── ses-[V0X]/
                ├── anat/
                │   │ <span class="hashtag"># File Prefix: sub-[ID]_ses-[V0X]_hash-{HASH}_run-[X]</span>
                │   ├── *_space-MNI152NLin6Asym_desc-preproc_T2w.nii.gz    <span class="comment"># Preprocessed T2w in MNI standard space</span>
                │   ├── *_hemi-<span class="var">{L|R}</span>_space-fsLR_den-32k_<span class="var">{SURF}</span>.surf.gii    <span class="comment"># fsLR 32k cortical surfaces (L/R)</span>
                │   ├── *_space-fsLR_den-91k_<span class="var">{METRIC}</span>.dscalar.nii          <span class="comment"># Dense scalar maps (fsLR 91k grayordinates)</span>
                │   └── *_space-fsLR_seg-<span class="var">{PARC}</span>_stat-mean_desc-<span class="var">{METRIC}</span>_morph.tsv    <span class="comment"># Atlas-based summary statistics</span>
                │
                ├── func/
                │   │ <span class="hashtag"># Run-specific files ('run-[X]') are omitted for brevity if concatenated files are present</span>
                │   │ <span class="hashtag"># File Prefix: sub-[ID]_ses-[V0X]_hash-{HASH}_task-rest</span>
                │   │
                │   <span class="comment"># Primary denoised BOLD outputs in fsLR grayordinate space + confound files</span>
                │   ├── *_space-fsLR_den-91k_desc-<span class="var">{denoised|denoisedSmoothed}</span>_bold.dtseries.nii
                │   ├── *_<span class="var">{motion|outliers}</span>.tsv
                │   ├── *_dir-PA_run-[X]_design.tsv
                │
                │   <span class="comment"># Dense scalar maps</span>
                │   ├── *_dir-PA_run-[X]_space-fsLR_den-91k_stat-alff_desc-smooth_boldmap.dscalar.nii
                │   ├── *_dir-PA_run-[X]_space-fsLR_den-91k_stat-<span class="var">{alff|reho}</span>_boldmap.dscalar.nii
                │
                │   <span class="comment"># Parcellated outputs</span>
                │   ├── *_space-fsLR_seg-<span class="var">{PARC}</span>_den-91k_stat-mean_timeseries.ptseries.nii
                │   ├── *_space-fsLR_seg-<span class="var">{PARC}</span>_stat-mean_timeseries.tsv
                │   ├── *_space-fsLR_seg-<span class="var">{PARC}</span>_stat-pearsoncorrelation_relmat.tsv
                │   ├── *_dir-PA_run-[X]_space-fsLR_seg-<span class="var">{PARC}</span>_den-91k_stat-pearsoncorrelation_boldmap.pconn.nii
                │   ├── *_dir-PA_run-[X]_space-fsLR_seg-<span class="var">{PARC}</span>_den-91k_stat-coverage_boldmap.pscalar.nii
                │   ├── *_dir-PA_run-[X]_space-fsLR_seg-<span class="var">{PARC}</span>_stat-coverage_bold.tsv
                │   ├── *_dir-PA_run-[X]_space-fsLR_seg-<span class="var">{PARC}</span>_stat-<span class="var">{alff|reho}</span>_bold.tsv
                │
                │   <span class="comment"># Quality control metrics</span>
                │   ├── *_dir-PA_run-[X]_space-fsLR_den-91k_desc-linc_qc.tsv
                │   └── *_desc-abcc_qc.hdf5
                │
                ├── figures/*
                ├── sub-[ID]_ses-[V0X]_hash-<span class="var">{HASH}</span>_executive_summary.html
                └── sub-[ID].html

<span class="hashtag"># ── Label Legend ─────────────────────────────────────────────</span>
<span class="var">HASH</span>    : 0f306a2f+0ef9c88a , 2afa9081+0ef9c88a
<span class="var">METRIC</span>  : curv , sulc , thickness  
<span class="var">PARC</span>    : 4S-{156|256|...|1056}Parcels , Glasser , Gordon , MIDB , MyersLabonte , HCP (func/ only) , Tian  (func/ only)
<span class="var">SURF</span>    : midthickness , pial , white , inflated , vinflated
</div>


## Quality Control Summary Statistics

We evaluated the impact of data quality on functional connectivity. Average functional connectivity matrices were computed using the Gordon-parcellated time series available in the V02 XCP-D derivatives. Data were included based on varying thresholds of <a href="../qc/#brainswipes">BrainSwipes</a> QC scores. Functional connectivity patterns were not substantially altered with the inclusion of lower-quality data, indicating robustness to mild quality variation

**Connectivity matrices as data quality improves (left -> right) based on QC thresholds of 0.1, 0.5, and 0.9:**
<img src="../images/fconn_qc.png" style="width: 90%;" class="center">

---

{{ references(instruments.fmri) }}
