# Supplement: Detailed XCP-D Derivatives Guide
<!-- 
### AT A GLANCE
<ul>
<li><strong>Denoised BOLD timeseries</strong><br>Surface-based (fsLR 91k), in CIFTI format, generated per task and run</li>
<li><strong>Parcellated timeseries</strong><br>Atlas-based (Gordon, HCP, MIDB), in TSV and CIFTI formats</li>
<li><strong>Functional connectivity matrices</strong><br>Pearson correlation matrices for Gordon, HCP, and MIDB atlases, in TSV and CIFTI formats</li>
<li><strong>ALFF and ReHo maps</strong><br>Amplitude of low-frequency fluctuations (ALFF) and regional homogeneity (ReHo), in CIFTI format</li>
<li><strong>Anatomical surfaces</strong><br>fsLR 32k meshes and morphometry maps (curvature, sulcal depth, thickness)</li>
<li><strong>Quality control</strong><br>Motion parameters, outlier detection, ABCC QC metrics (HDF5), and visual reports</li>
</ul> -->

## Anatomical Derivatives
<pre class="folder-tree" style="font-size: 11px;">
...
└── ses-[V0X]/
    └── anat/
        ├── *_space-MNI152NLin6Asym_desc-preproc_T2w.nii.gz    <span class="comment"># Preprocessed T2w in MNI standard space</span>
        ├── *_hemi-<span class="var">{L|R}</span>_space-fsLR_den-32k_<span class="var">{SURF}</span>.surf.gii    <span class="comment"># fsLR 32k cortical surfaces (L/R)</span>
        ├── *_space-fsLR_den-91k_<span class="var">{METRIC}</span>.dscalar.nii          <span class="comment"># Dense scalar maps (fsLR 91k grayordinate space)</span>
        └── *_space-fsLR_seg-<span class="var">{PARC}</span>_stat-mean_desc-<span class="var">{METRIC}</span>_morph.tsv     <span class="comment"># Atlas-based summary statistics</span>           

<span class="hashtag"># Label Values Legend</span>
File Prefix: sub-[ID]_ses-[V0X]_hash-{HASH}_run-[X]
<span class="var">METRIC</span>     : curv , sulc , thickness  
<span class="var">PARC</span>       : 4S-{156|256|...|1056}Parcels , Glasser , Gordon , MIDB , MyersLabonte
<span class="var">SURF</span>       : midthickness , pial , white , inflated , vinflated
</pre>

## Functional Derivatives
<pre class="folder-tree" style="font-size: 11px;">
<span class="hashtag"># NOTE: Many outputs are provided both per-run and concatenated across runs.
# Run-specific files ('run-[X]') are omitted for brevity unless they only exist as run-specific files.</span>

...
    └── func/
        <span class="comment"># Primary denoised BOLD outputs in fsLR grayordinate space + confound files</span>
        ├── *_space-fsLR_den-91k_desc-<span class="var">{denoised|denoisedSmoothed}</span>_bold.dtseries.nii
        ├── *_<span class="var">{motion|outliers}</span>.tsv
        ├── *_dir-PA_run-[X]_design.tsv

        <span class="comment"># Dense scalar maps</span>
        ├── *_dir-PA_run-[X]_space-fsLR_den-91k_stat-alff_desc-smooth_boldmap.dscalar.nii
        ├── *_dir-PA_run-[X]_space-fsLR_den-91k_stat-<span class="var">{alff|reho}</span>_boldmap.dscalar.nii

        <span class="comment"># Parcellated outputs</span>
        ├── *_space-fsLR_seg-<span class="var">{PARC}</span>_den-91k_stat-mean_timeseries.ptseries.nii
        ├── *_space-fsLR_seg-<span class="var">{PARC}</span>_stat-mean_timeseries.tsv

        ├── *_space-fsLR_seg-<span class="var">{PARC}</span>_stat-pearsoncorrelation_relmat.tsv
        ├── *_dir-PA_run-[X]_space-fsLR_seg-<span class="var">{PARC}</span>_den-91k_stat-pearsoncorrelation_boldmap.pconn.nii

        ├── *_dir-PA_run-[X]_space-fsLR_seg-<span class="var">{PARC}</span>_den-91k_stat-coverage_boldmap.pscalar.nii
        ├── *_dir-PA_run-[X]_space-fsLR_seg-<span class="var">{PARC}</span>_stat-coverage_bold.tsv
        ├── *_dir-PA_run-[X]_space-fsLR_seg-<span class="var">{PARC}</span>_stat-<span class="var">{alff|reho}</span>_bold.tsv

        <span class="comment"># Quality control metrics</span>
        ├── *_dir-PA_run-[X]_space-fsLR_den-91k_desc-linc_qc.tsv
        └── *_desc-abcc_qc.hdf5

<span class="hashtag"># Label Values Legend</span>
File Prefix: sub-[ID]_ses-[V0X]_hash-{HASH}_task-rest
<span class="var">PARC</span>: 4S-{156|256|...|1056}Parcels , Glasser , Gordon , MIDB , MyersLabonte , HCP , Tian
</pre>


<!-- 

<pre class="folder-tree" style="font-size: 11px;">
hbcd/
└── derivatives/
    └── xcp_d-<span class="var">{HASH}</span>/
        └── sub-[ID]/
            ├── figures/
            ├── ses-[V0X]/
            │   ├── anat/
            │   ├── func/
            │   └── figures/
            │
            ├── sub-[ID]_ses-[V0X]_hash-<span class="var">{HASH}</span>_executive_summary.html
            └── sub-[ID].html

<span class="hashtag"># Label Values Legend</span>
<span class="var">HASH</span>: 0f306a2f+0ef9c88a , 2afa9081+0ef9c88a
</pre>


#### Dense Timeseries & Confounds
*Primary denoised BOLD outputs in fsLR grayordinate space (`.dtseries.nii`) accompanied by confound files (`motion.tsv`, `outliers.tsv`).*

- **Primary input for most analyses** 
- Includes nuisance regression, bandpass filtering, and motion censoring
- Provided with and without surface-based spatial smoothing
- Available as both per-run and concatenated outputs
- Accompanied by run-level nuisance regressors and motion metrics used during denoising, including:
    - Motion parameters and framewise displacement (`motion.tsv`)
    - Censored timepoints (`outliers.tsv`)
    - Nuisance regressor design matrices (`design.tsv`)

#### Dense Scalar Maps

*Voxel-wise (grayordinate-level) functional metrics derived from the denoised timeseries.*

```default
├── *_task-<TASK>_space-fsLR_den-91k_stat-alff_boldmap.dscalar.nii
├── *_task-<TASK>_space-fsLR_den-91k_stat-alff_desc-smooth_boldmap.dscalar.nii
├── *_task-<TASK>_space-fsLR_den-91k_stat-reho_boldmap.dscalar.nii
```

- **ALFF**: Amplitude of low-frequency fluctuations (unsmoothed and smoothed variants)
- **ReHo**: Regional Homogeneity, reflecting local BOLD synchrony across neighboring grayordinates


#### Quality Control Metrics

*Summary metrics for assessing data quality and inclusion.*

```default
├── *_task-<TASK>_space-fsLR_den-91k_desc-linc_qc.tsv
└── *_task-<TASK>_desc-abcc_qc.hdf5
```

- **LINC QC** (`.tsv`): Run-level metrics (e.g., retained frames, mean FD, DVARS)
- **ABCC QC** (`.hdf5`): Aggregated metrics across tasks, including motion summaries and atlas coverage, for downstream filtering and participant exclusion


### HTML QC Reports

The `.html` files provide subject-level visual summaries designed for rapid, systematic quality control (QC) review (source image files stored in `figures/`).

- **`sub-<LABEL>_ses-<LABEL>.html`**    
  - Standard XCP-D subject-level report, structured similarly to the fMRIPrep report
  - Includes registration figures, BOLD carpet plots, motion summaries, and connectivity outputs

- **`sub-<LABEL>_ses-<LABEL>_executive_summary.html`**
  - ABCC-specific executive summary report that provides a streamlined review of the most critical QC checkpoints
  - Includes anatomical normalization quality, per-task BOLD pre/post-processing summaries, and motion censoring profiles -->
