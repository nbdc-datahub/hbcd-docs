# Magnetic Resonance Spectroscopy (MRS)

{{ alert_warning(instruments.mrs) }}
{{ data_warning(instruments.mrs) }}
{{ issues_banner() }}

---

<!-- ##### Overview & Acquisition -->
{{ instrument_description(instruments.mrs) }}

<!-- ## MRS Processing & Derivatives -->
{{ suppx(instruments.mrs, "1") }}

<pre class="folder-tree">
<span><a href="../../../datacuration/overview/#filetrees"><i class="fa fa-circle-info"></i> How To Read File Trees →</a></span>
hbcd/
└── derivatives/
    └── osprey/
        └── sub-[ID]/
            └── ses-[V0X]/
                ├── HERCULES/
                │   ├── PreOspreyLocalizerReg/
                │   │   ├── <span class="var">{aal|c1|c2|c3}</span>reference_seg_aligned_to_localizer.nii.gz
                │   │   ├── reference_<span class="var">{img|seg}</span>_aligned_to_localizer.nii.gz
                │   │   ├── readme.txt
                │   │   ├── registration_summary.json
                │   │   └── transform_mat.npy
                │   │
                │   ├── QuantifyResults/
                │   │   ├── <span class="var">{diff1|diff2|sum}</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1.tsv
                │   │   ├── <span class="var">{diff1|diff2|sum}</span>_<span class="var">{AlphaCorr|CSF|raw|TissCorr}</span>WaterScaled_Voxel_1_Basis_1.tsv
                │   │   └── <span class="var">{diff1|diff2|sum}</span>_<span class="var">{amplMets|tCr}</span>_Voxel_1_Basis_1.tsv
                │   │
                │   ├── SegMaps/
                │   │   ├── *_acq-hercules_svs.nii_space-scanner_Voxel-1_label-<span class="var">{CSF|GM|Tha|WM}</span>.nii.gz
                │   │   └── TissueFractions_Voxel_1.tsv
                │   │
                │   ├── VoxelMasks/
                │   │   └── *_acq-hercules_svs_space-scanner_mask.nii.gz
                │   │
                │   ├── LogFile.txt
                │   ├── QM_processed_spectra.tsv
                │   ├── subject_names_and_excluded.tsv 
                │   ├── SummaryMRSinMRS.md
                │   └── wrapper_settings.mat
                │
                └── unedited/* <span class="hashtag"># Mirrors HERCULES/ folder structure</span>
</pre>

<!-- ## Osprey MRS Output User Guide -->
{{ suppx(instruments.mrs, "2") }}


<table class="compact-table-no-vertical-lines">
<thead><tr><th>Spectrum</th><th>Best-Quantified Metabolites</th><th>Table Name (in <a href="../../../datacuration/overview/#tabulated-pipeline-derivatives">tabulated pipeline derivatives</a>)
</th></tr></thead>
<tbody>
<tr><td><b>Short-TE Unedited</b></td><td>tNAA, tCr, tCho, mI, Glx, Scyllo</d><td><code>img_osprey_unedited_A_TissCorrWaterScaled_Voxel_1_Basis_1</code></td>
</tr>
<tr><td><b>HERCULES Sum</b></td><td>NAA, Glu, Gln</td><td><code>img_osprey_HERCULES_sum_TissCorrWaterScaled_Voxel_1_Basis_1</code></td>
</tr>
<tr><td><b>HERCULES Diff1</b></td><td>GABA+</td><td><code>img_osprey_HERCULES_diff1_TissCorrWaterScaled_Voxel_1_Basis_1</code></td>
</tr>
<tr><td><b>HERCULES Diff2</b></td><td>GSH, Lac, NAAG, PE</td><td><code>img_osprey_HERCULES_diff2_TissCorrWaterScaled_Voxel_1_Basis_1</code></td>
</tr>
</tbody>
</table>

<!-- ### Quantification Approaches -->
{{ suppx(instruments.mrs, "3") }}

---

{{ references(instruments.mrs) }}
