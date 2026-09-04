# Structural MRI

{{ alert_warning(instruments.smri) }}
{{ data_warning(instruments.smri) }}
{{ issues_banner() }}

## Overview & Acquisition

{{ instrument_description(instruments.smri) }}

## Processing & Derivatives

<p style="font-size: 2em; color: red;">ADD OVERVIEW TEXT</p>

<div id="file-selection" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
<span class="text">File Selection for Processing</span>
  <a class="anchor-link" href="#file-selection" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>For structural and functional MRI processing, file selection is based on raw data quality control metrics. Only scans with a passing overall QC score (<code>QC</code> = 1) and low motion (<code>QU_Motion</code> ≤ 2) are selected for processing. If multiple scans are present for a given modality (T1w/T2w), the scan with the highest QC metrics is used.</p>
<p>All processing streams utilized both the T1w and T2w if they were present. Processing was still executed with only a single modality present as well, with certain requirements depending on the surface reconstruction method utilized within Infant fMRIPrep (<a href="#m-crib-s-freesurfer">see details</a>):</p>
<ul>
<li>M-CRIB-S (T2w-based): requires T2w</li>
<li>Infant FreeSurfer (T1w-based): requires both T1w and T2w</li>
</ul>
</div>
<p></p>

### BIBSNet

BIBSNet is a deep learning model optimized for infant MRI brain tissue segmentation (<a href="https://doi.org/10.1101/2023.03.22.533696">Hendrickson et al. 2024</a>). The <a href="https://bibsnet.readthedocs.io/en/latest/">BIBSNet pipeline</a> generates native-space brain segmentations and brain masks (as well as <code>volumes.tsv</code> files with ROI volume statistics), which are fed into Infant fMRIPrep for use in anatomical preprocessing and surface reconstruction.

<div id="bibsnet-derivs" class="banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span><span class="text-with-link">
<span class="text">BIBSNet Derivatives</span><a class="anchor-link" href="#bibsnet-derivs" title="Copy link">
  <i class="fa-solid fa-link"></i></a></span><span class="arrow">▸</span></div>
<div class="collapsible-content">
<pre class="folder-tree">
hbcd/
└── derivatives/ 
    └── bibsnet/
        └── sub-[ID]/
            └── ses-[V0X]/
                └── anat/
                    ├── sub-[ID]_ses-[V0X]_space-<span class="var">{T1w|T2w}</span>_desc-aseg_dseg.nii.gz <span class="hashtag">(+JSON)</span>
                    ├── sub-[ID]_ses-[V0X]_space-<span class="var">{T1w|T2w}</span>_desc-aseg_volumes.tsv <span class="hashtag">(+JSON)</span>         
                    └── sub-[ID]_ses-[V0X]_space-<span class="var">{T1w|T2w}</span>_desc-aseg_brain-mask.nii.gz <span class="hashtag">(+JSON)</span>

<span><a href="../../../datacuration/overview/#filetrees"><i class="fa fa-circle-info"></i> How To Read File Trees →</a></span>
</pre>
</div>

### M-CRIB-S & FreeSurfer

M-CRIB-S & FreeSurfer are alternative surface reconstruction methods supported by Infant fMRIPrep optimized for different age ranges (see table below). The derivative folders provided in the release are generated from the [intermediate FreeSurfer-like folders](https://nibabies.readthedocs.io/en/latest/outputs.html#surface-reconstruction) produced by Infant fMRIPrep during surface reconstruction. When M-CRIB-S is used, Infant fMRIPrep still creates a FreeSurfer-structured folder containing the M-CRIB-S results mapped to the standard <a href="https://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllOutputFiles">recon-all</a> layout; these appear in the release under <code>freesurfer-0f306a2f/</code>.

<table class="table-no-vertical-lines">
<thead> <tr> <th>Method</th> <th>Hash ID</th> <th>Description</th> <th>Visits <i>(Age Range in Months)</i></th> </tr> </thead>
<tbody>
<tr>
<td>M-CRIB-S</td>
<td><a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0/tools/nibabies_25.2.0-0f306a2f.html">0f306a2f</a></td>
<td>T2w-based method for neonates</td>
<td>V02 <i>(0-1 m)</i></td>
</tr> <tr>
<td>Infant FreeSurfer</td>
<td><a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0/tools/nibabies_25.2.0-2afa9081.html">2afa9081</a></td> <td>T1w-based method for infants 0-2 years old</td>
<td>V02 <i>(0-1 m)</i>, V03 <i>(3-9 m)</i>, V04 <i>(9-15 m)</i></td>
</tr> </tbody>
</table>

<div id="fs" class="banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span><span class="text-with-link">
<span class="text">FreeSurfer Source Directories</span><a class="anchor-link" href="#fs" title="Copy link">
  <i class="fa-solid fa-link"></i></a></span><span class="arrow">▸</span></div>
<div class="collapsible-content">
<pre class="folder-tree">
hbcd/
└── derivatives/
    └── freesurfer-<span class="var">{HASH}</span>/
        └── sub-[ID]_ses-[V0X]/
            ├── label/
            │   ├── <span class="var">{lh|rh}</span>.<span class="var">{ATLAS}</span>.annot
            │   ├── <span class="var">{lh|rh}</span>.<span class="var">{ATLAS}</span>.auto.nomask.annot
            │   └── <span class="var">{lh|rh}</span>.cortex.label
            │
            ├── mri/
            │   ├── T2.mgz
            │   ├── <span class="var">{ATLAS}</span>+aseg.mgz
            │   ├── aseg*.mgz
            │   ├── <span class="var">{brain|brainmask}</span>.mgz
            │   ├── <span class="var">{lh|rh}</span>.ribbon.mgz
            │   ├── norm.mgz
            │   ├── orig.mgz
            │   └── ribbon.mgz
            │
            ├── stats/
            │   ├── aseg.stats
            │   ├── brainvol.stats
            │   ├── <span class="var">{lh|rh}</span>.<span class="var">{ATLAS}</span>.stats
            │   └── <span class="var">{lh|rh}</span>.curv.stats
            │
            ├── surf/
            │   ├── <span class="var">{lh|rh}</span>.{white,pial,midthickness}
            │   ├── <span class="var">{lh|rh}</span>.{inflated,sphere}*
            │   ├── <span class="var">{lh|rh}</span>.smoothwm*
            │   ├── <span class="var">{lh|rh}</span>.{area,area.mid,area.pial}
            │   └── <span class="var">{lh|rh}</span>.{curv,sulc,thickness,volume}
            │
            └── scripts/*

<span class="hashtag"># Label Legend</span>
<span class="var">HASH</span>: 0f306a2f | 2afa9081
<span class="var">HEM</span>: lh | rh
<span class="var">ATLAS</span>: aparc | aparc+DKTatlas
</pre>
</div>

<div id="mcribs" class="banner" onclick="toggleCollapse(this)" style="background-color: #f0dcfb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">M-CRIB-S Source Directories</span>
  <a class="anchor-link" href="#mcribs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<pre class="folder-tree">
hbcd/
└── derivatives/
    └── mcribs-0f306a2f/
        └── sub-[ID]_ses-V02/
            ├── RawT2/sub-[ID]_ses-V02.nii.gz
            ├── RawT2RadiologicalIsotropic/sub-[ID]_ses-V02.nii.gz_symlink_s3_object
            ├── SurfReconDeformable/
            │   └── sub-[ID]_ses-V02/
            │       ├── meshes/
            │       │   ├── <span class="var">{internal|pial|white|pial+internal|white+internal}</span>.vtp
            │       │   ├── pial-<span class="var">{lh|rh}</span>.vtp
            │       │   ├── pial-<span class="var">{lh|rh}</span>-reordered.vtp
            │       │   └── white-<span class="var">{lh|rh}</span>.<span class="var">{CortexMask.curv|Normals.surf|RegionId.curv|vtp}</span>
            │       ├── recon/
            │       │   ├── cortical-hull-dmap.nii.gz
            │       │   └── regions.nii.gz
            │       └── temp/
            │           ├── brain-mask.nii.gz
            │           ├── ventricles-dmap.nii.gz
            │           ├── t2w-image.nii.gz_symlink_s3_object
            │           ├── cerebrum-<span class="var">{lh|rh}</span>-dmap.nii.gz
            │           ├── cerebrum-<span class="var">{lh|rh}</span>-hull-[X].vtp
            │           ├── cerebrum-<span class="var">{lh|rh}</span>-iso.vtp
            │           ├── <span class="var">{STRUCT}</span>-mask-[X].nii.gz
            │           ├── <span class="var">{cerebrum-lh|cerebrum-rh|pial|white}</span>-[X].vtp
            │           ├── <span class="var">{cerebrum-lh|cerebrum-rh|pial|white}</span>-[X]-output_[X].vtp
            │           │
            │           └── <span class="var">{pial|white}</span>-foreground.nii.gz
            ├── TissueSeg/
            │   ├── sub-[ID]_ses-V02_all_labels.nii.gz
            │   ├── sub-[ID]_ses-V02_all_labels_manedit.nii.gz_symlink_s3_object
            │   ├── sub-[ID]_ses-V02_brain_mask.nii.gz
            │   └── sub-[ID]_ses-V02_t2w_restore.nii.gz_symlink_s3_object
            ├── TissueSegDrawEM/sub-[ID]_ses-V02/N4/sub-[ID]_ses-V02.nii.gz_symlink_s3_object
            ├── freesurfer/ <span class="hashtag"># M-CRIB-S–specific outputs</span>
            │   └── sub-[ID]_ses-V02/
            │       └── mri/
            │           └── <span class="var">{brain|orig}</span>.mgz_symlink_s3_object
            ├── logs/sub-[ID]_ses-V02.log
            └── command.txt
<span class="hashtag"># Label Values Legend</span>
<span class="var">STRUCT</span>: brain | cerebrum-{lh/rh} | corpus-callosum | cortex | {deep-gray|gray|white}-matter | ventricles 
</pre>

<h5>Restoring Symlink Files Present in M-CRIB-S Derivatives</h5>
<p>When downloaded, the symlink files present within the M-CRIB-S derivatives (<code>mcribs-0f306a2f/</code>), appended with <code>*_symlink_s3_object</code>, appear as text files that contain the S3 object path instead of the actual file content. If needed, you may restore these files as symlinks via the following terminal command, which restores all symlink files within your locally downloaded directory and renames them without <code>*_symlink_s3_object</code> to match the original sourcedata filenames:</p>

```
find . -type f -name "*_symlink_s3_object" -print | while read path ; do
  symval=$(cat "$path")
  symdir=$(dirname "$path")
  symbase=$(basename "$path" _symlink_s3_object)
  ln -s "$symval" "$symdir/$symbase" && rm -f "$path" || break
```
</div>


### QC Pipelines: MRIQC & BME-X

[MRIQC](https://mriqc.readthedocs.io/en/latest/about.html) extracts image quality metrics (IQMs) for each T1w/T2w and functional BOLD run and generates visual `.html` reports. The [BME-X](https://brain-mri-enhancement.readthedocs.io/) pipeline performs motion correction, resolution enhancement, denoising, and harmonization of MR images.

<div id="mriqc" class="banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span><span class="text-with-link">
<span class="text">MRIQC & BME-X Derivatives</span><a class="anchor-link" href="#mriqc" title="Copy link">  <i class="fa-solid fa-link"></i></a></span>
  <span class="arrow">▸</span></div>
<div class="collapsible-content">
<pre class="folder-tree">
hbcd/
└── derivatives/
    ├── mriqc/                            
    │   ├── sub-[ID]/
    │   │   └── ses-[V0X]/
    │   │       ├── anat/
    │   │       │   └── sub-[ID]_ses-[V0X]_run-[X]_<span class="var">{T1w|T2w}</span>.json
    │   │       └── func/
    │   │           └── sub-[ID]_ses-[V0X]_run-[X]_<span class="var">{T1w|T2w}</span>.json
    │   └── sub-[ID]_ses-[V0X]_run-[X]_<span class="var">{T1w|T2w}</span>.html
    │
    └── bme-x/                  
        └── sub-[ID]/
            └── ses-[V0X]/
                └── anat/
                    |__ sub-[ID]_ses-[V0X]_run-[X]_desc-<span class="var">{enhanced|preproc}</span>_<span class="var">{T1w|T2w}</span>.nii.gz <span class="hashtag">(+JSON)</span>
                    |__ sub-[ID]_ses-[V0X]_run-[X]_space-<span class="var">{T1w|T2w}</span>_desc-brain_mask.nii.gz <span class="hashtag">(+JSON)</span>
                    |__ sub-[ID]_ses-[V0X]_run-[X]_<span class="var">{T1w|T2w}</span>.nii.gz <span class="hashtag">(+JSON)</span>

<span><a href="../../../datacuration/overview/#filetrees"><i class="fa fa-circle-info"></i> How To Read File Trees →</a></span>
</pre>
</div>


---

{{ references(instruments.smri) }}




<!-- ### File selection for processing

For both structural and functional MRI processing, only scans with a passing overall raw data QC score (<code>QC</code> = 1) and low motion (<code>QU_Motion</code> ≤ 2) are selected for processing. If multiple scans are present for a given modality (T1w/T2w), the scan with the highest quality QC metric values is used. All processing streams utilized both the T1w and T2w if they were present, but processing was still executed with only a single modality present. There were however specific requirements depending on the surface reconstruction method utilized within Infant fMRIPrep ([see details](#m-crib-s-freesurfer)):

- M-CRIB-S (T2w-based): requires T2w
- Infant FreeSurfer (T1w-based): requires both T1w and T2w
 -->
