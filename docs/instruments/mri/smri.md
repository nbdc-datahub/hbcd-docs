# Structural MRI

{{ alert_warning(instruments.smri) }}
{{ data_warning(instruments.smri) }}
{{ issues_banner() }}

## Overview & Acquisition

{{ instrument_description(instruments.smri) }}

## File Selection for Processing

#### Scan eligibility and selection
When multiple eligible T1w or T2w scans are available, the scan with the best quality is selected for each modality. Scans must meet both of the following raw data quality control (QC) criteria (see {{ hbcd_processing_site }} for full configuration details):

 <table class="table-no-vertical-lines">
  <thead>
    <tr>
      <th>QC criterion</th>
      <th>Field</th>
      <th>Requirement</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Passing overall QC</td>
      <td><code>QC</code></td>
      <td>= 1</td>
    </tr>
    <tr>
      <td>Low motion</td>
      <td><code>QU_motion</code></td>
      <td>&lt; 2.01</td>
    </tr>
    <tr>
      <td>Automated motion QC score for sMRI</td>
      <td><code>aqc_motion</code></td>
      <td>&lt; 10000</td>
    </tr>
    <tr>
      <td>SNR ratio of image intensity within the brain mask</td>
      <td><code>brain_SNR</code></td>
      <td>&gt; -1000</td>
    </tr>
  </tbody>
</table>

#### Anatomical scan requirements
**Processing uses both T1w and T2w scans when both are available and meet the QC criteria.** Processing with a single anatomical modality is supported only when it meets the minimum requirements for the visit and surface reconstruction method used within Infant fMRIPrep ([see details](smri.md#m-crib-s-freesurfer)).

<table class="table-no-vertical-lines" width="100%"> 
<caption>Minimum anatomical scan requirements by visit and surface reconstruction method</caption>
<thead>
<tr>
<th>Surface reconstruction method</th>
<th>Derivatives hash ID</th>
<th>V02</th>
<th>V03</th>
<th>V04</th>
<th>V06</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>M-CRIB-S</strong> (T2w-based)</td>
<td><code>hash-d902942d</code></td>
<td>T2w</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td><strong>Infant FreeSurfer</strong> (T1w-based)</td>
<td><code>hash-364caa63</code></td>
<td>T1w and T2w</td>
<td>T1w and T2w</td>
<td>T1w</td>
<td>T1w</td>
</tr>
</tbody>
</table>
<!-- 
*Note that this only applies to the full processing workflow from BIBSNet to XCP-D. All sessions are processed through BIBSNet in spite of visit/age as long as at least one anatomical, T1w or T2w, is present. The restrictions above determine whether the data will continue through Infant fMRIPrep and XCP-D processing as well after BIBSNet.* -->

## Processing & Derivatives

<div class="banner" style="margin-bottom: 1em;"> <span class="emoji"><i class="fa-solid fa-circle-info"></i><i class="fa fa-person-cane"></i></span> <span class="text">See the {{ hbcd_processing_site }} for full pipeline configuration and processing details.</span> </div>

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

<span><a href="../../../help/resources/#how-to-read-file-trees"><i class="fa fa-circle-info"></i> How To Read File Trees →</a></span>
</pre>
</div>

### M-CRIB-S & FreeSurfer

M-CRIB-S & FreeSurfer are alternative surface reconstruction methods supported by Infant fMRIPrep optimized for different age ranges (see table below). The derivative folders provided in the release are generated from the [intermediate FreeSurfer-like folders](https://nibabies.readthedocs.io/en/latest/outputs.html#surface-reconstruction) produced by Infant fMRIPrep during surface reconstruction. When M-CRIB-S is used, Infant fMRIPrep still creates a FreeSurfer-structured folder containing the M-CRIB-S results mapped to the standard <a href="https://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllOutputFiles">recon-all</a> layout; these appear in the release under <code>freesurfer-d902942d/</code>.

<table class="table-no-vertical-lines">
<thead> <tr> <th>Method</th> <th>Hash ID</th> <th>Description</th> <th>Visits <i>(Age Range in Months)</i></th> </tr> </thead>
<tbody>
<tr>
<td>M-CRIB-S</td>
<td><a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0/tools/nibabies_25.2.0-d902942d.html">d902942d</a></td>
<td>T2w-based method for neonates</td>
<td>V02 <i>(0-1 m)</i></td>
</tr> <tr>
<td>Infant FreeSurfer</td>
<td><a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0/tools/nibabies_25.2.0-364caa63.html">364caa63</a></td> <td>T1w-based method for infants 0-2 years old</td>
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
<span class="var">HASH</span>: d902942d | 364caa63
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
    └── mcribs-d902942d/
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
<p>When downloaded, the symlink files present within the M-CRIB-S derivatives (<code>mcribs-d902942d/</code>), appended with <code>*_symlink_s3_object</code>, appear as text files that contain the S3 object path instead of the actual file content. If needed, you may restore these files as symlinks via the following terminal command, which restores all symlink files within your locally downloaded directory and renames them without <code>*_symlink_s3_object</code> to match the original sourcedata filenames:</p>

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

<span><a href="../../../help/resources/#how-to-read-file-trees"><i class="fa fa-circle-info"></i> How To Read File Trees →</a></span>
</pre>
</div>


---

{{ references(instruments.smri) }}




<!-- ### File selection for processing

For both structural and functional MRI processing, only scans with a passing overall raw data QC score (<code>QC</code> = 1) and low motion (<code>QU_Motion</code> ≤ 2) are selected for processing. If multiple scans are present for a given modality (T1w/T2w), the scan with the highest quality QC metric values is used. All processing streams utilized both the T1w and T2w if they were present, but processing was still executed with only a single modality present. There were however specific requirements depending on the surface reconstruction method utilized within Infant fMRIPrep ([see details](#m-crib-s-freesurfer)):

- M-CRIB-S (T2w-based): requires T2w
- Infant FreeSurfer (T1w-based): requires both T1w and T2w
 -->
