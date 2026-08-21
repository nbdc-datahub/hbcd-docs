# Magnetic Resonance Spectroscopy (MRS)

{{ alert_warning(instruments.mrs) }}
{{ data_warning(instruments.mrs) }}
{{ issues_banner() }}

---

<!-- ##### Overview & Acquisition -->
{{ instrument_description(instruments.mrs) }}

<!-- ## MRS Processing & Derivatives -->
{{ suppx(instruments.mrs, "1") }}

<div id="osprey" class="banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">OSPREY-BIDS</span>
  <a class="anchor-link" href="#osprey" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<span><a href="../../../datacuration/overview/#filetrees"><i class="fa fa-circle-info"></i> How To Read File Trees →</a></span>
<pre class="folder-tree">
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
</div>

<!-- ## Osprey MRS Output User Guide -->
{{ suppx(instruments.mrs, "2") }}


<table class="table-no-vertical-lines">
<thead><tr><th>Spectrum</th><th>Best-Quantified Metabolites</th><th>Table Name</th></tr></thead>
<tbody>
<tr><td>Short-TE Unedited</td><td>tNAA, tCr, tCho, mI, Glx, Scyllo</d><td><code>img_osprey_unedited_A_TissCorrWaterScaled_Voxel_1_Basis_1</code></td>
</tr>
<tr><td>HERCULES Sum</td><td>NAA, Glu, Gln</td><td><code>img_osprey_HERCULES_sum_TissCorrWaterScaled_Voxel_1_Basis_1</code></td>
</tr>
<tr><td>HERCULES Diff1</td><td>GABA+</td><td><code>img_osprey_HERCULES_diff1_TissCorrWaterScaled_Voxel_1_Basis_1</code></td>
</tr>
<tr><td>HERCULES Diff2</td><td>GSH, Lac, NAAG, PE</td><td><code>img_osprey_HERCULES_diff2_TissCorrWaterScaled_Voxel_1_Basis_1</code></td>
</tr>
</tbody>
</table>


<!-- ### Quantification Approaches -->
{{ suppx(instruments.mrs, "3") }}

---

{{ references(instruments.mrs) }}




<!-- ## Osprey MRS Output User Guide

The primary outcome variables from MRS data processed with the Osprey pipeline are metabolite concentrations. Osprey outputs are available as both **file-based derivatives** within individual participant directories and **tabulated derivatives** that combine pipeline outputs across participants for analysis (see full list of available tabulated outputs [here](tables/osprey.html)).

### Metabolite Quantification by Spectrum

The ISTHMUS acquisition generates four spectra, each modeled separately using linear combination modeling with an inclusive basis set. Although most metabolites may contribute at least minimally to multiple spectra, each spectrum is best suited for quantifying a particular subset of metabolites. -->
