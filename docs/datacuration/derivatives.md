
# Processed Derivatives

The `derivatives/` folder contains derivatives, which are file outputs from <a href="../../instruments/processing/" target="_blank">processing pipelines</a>. 

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    <span class="hashtag"># Structural & Functional MRI</span>             
    |__ mriqc/      
    |__ bibsnet/    
    |__ nibabies/   
    |__ freesurfer/ 
    |__ mcribs/     
    |__ xcp_d/      
    |               
    <span class="hashtag"># Quantitative MRI</span>    
    |__ symri/           
    |__ qmri_postproc/  
    | 
    <span class="hashtag"># Diffusion MRI</span>                                  
    |__ qsiprep/                         
    |__ qsirecon/                        
    |__ qsirecon-DIPYDKI/                
    |__ qsirecon-DSIStudio/               
    |__ qsirecon-NODDI/                  
    |__ qsirecon-TORTOISE_model-MAPMRI/  
    |__ qsirecon-TORTOISE_model-tensor/  
    |
    |__ osprey/       <span class="hashtag"># MRS</span>
    |__ made/         <span class="hashtag"># EEG</span>
    |__ hbcd_motion/  <span class="hashtag"># Biosensors Recordings</span>
</pre>

## Guide To File Tree Visuals

**The following formatting was employed to enhance readability of the file structure visuals:**

*   Some entities include a set of specific values, each of which is associated with a separate file: these values are either enclosed within `<>` as a list, separated by `|`, or listed in a **Label Values Legend**
*   For brevity, sidecar JSON files containing metadata for the corresponding data file may not be displayed, in which case files with corresponding JSONs are labeled with `(+JSON)` after the filename
*   Several pipelines produce an `.html` visual summary report intended to be used for quality assessment of processed outputs. These files, typically located at either the pipeline folder or session-level, source their images from a `figures/` folder found in the derivatives. For readability, the contents of the `figures/` folders are not listed

**Below we provide a brief summary of the derivatives included in the release. To see detailed documentation, visit the pipeline websites by clicking on the links provided.**

## Structural & Functional MRI

<pre class="folder-tree">
<span class="hashtag"># Structural & Functional MRI Pipeline Derivatives:</span>
hbcd/
|__ derivatives/ 
    |__ mriqc/
    |__ bibsnet/
    |__ nibabies/
    |__ freesurfer/ <span class="hashtag"># Derived from Infant fMRIPrep (nibabies/) sourcedata/ folder</span>
    |__ mcribs/     <span class="hashtag"># Derived from Infant fMRIPrep (nibabies/) sourcedata/ folder</span>
    |__ xcp_d/
</pre>

### MRIQC (`mriqc/`)
MRIQC extracts image quality metrics (IQMs) from structural (T1w and T2w) and functional MRI data and also generates visual `.html` reports.    
[<i class="fa-solid fa-book"></i> Go to pipeline documentation](https://mriqc.readthedocs.io/en/latest/about.html) 

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ mriqc/
        |__ sub-<span class="label">{ID}</span>/
        |   |__ ses-<span class="label">{V0X}</span>/
        |       |__ anat/
        |       |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_T1w.json
        |       |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_T2w.json
        |       |
        |       |__ func/
        |           |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_bold.json
        |        
        |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_T1w.html
        |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_T2w.html
        |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_bold.html
</pre>

### BIBSNet (`bibsnet/`)
BIBSNet outputs brain segmentations and masks in native T1w and T2w space as well as `volumes.tsv` files with ROI volume statistics.      
[<i class="fa-solid fa-book"></i> Go to pipeline documentation](https://bibsnet.readthedocs.io/en/latest/)

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ bibsnet/
        |__ sub-<span class="label">{ID}</span>/
            |__ ses-<span class="label">{V0X}</span>/
                |__ anat/
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_dseg.nii.gz <span class="hashtag">(+JSON)</span>
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes.tsv <span class="hashtag">(+JSON)</span>         
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;T1w|T2w&gt;</span>_desc-aseg_brain-mask.nii.gz <span class="hashtag">(+JSON)</span>
</pre>

### Infant-fMRIPrep (`nibabies/`)
Infant-fMRIPrep (also known as NiBabies) outputs from minimal structural and functional MRI processing include visual quality assessment reports, preprocessed derivatives, and confounds to be used for denoising in subsequent processing procedures.     
[<i class="fa-solid fa-book"></i> Go to pipeline documentation](https://nibabies.readthedocs.io/en/latest/outputs.html)

<p>
<div id="fyi-nibabies" class="table-banner">
    <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">NOTE: The current release includes Infant fMRIPrep (and consequently XCP-D) derivatives for V02 only.
	</span>
</div>
</p>

<pre class="folder-tree" style="font-size: 11px;">
hbcd/
|_ derivatives/ 
   |_ nibabies/
      |_ sub-<span class="label">{ID}</span>/
      |  |_ figures/
      |  |_ ses-<span class="label">{V0X}</span>/
      |     |_ log/
      |     |
      |     |_ anat/
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_desc-preproc_T2w.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_from-<span class="placeholder">&lt;MNI152NLin6Asym_res-2|MNIInfant+1&gt;</span>_to-T2w_mode-image_xfm.h5
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_from-T2w_to-<span class="placeholder">&lt;MNI152NLin6Asym_res-2|MNIInfant+1&gt;</span>_mode-image_xfm.h5
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_from-T2w_to-fsnative_mode-image_xfm.txt
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_from-fsnative_to-T2w_mode-image_xfm.txt
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_<span class="placeholder">&lt;curv|sulc|thickness&gt;</span>.shape.gii
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_<span class="placeholder">&lt;inflated|midthickness|pial|sphere|white&gt;</span>.surf.gii
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-dhcpAsym_den-32k_midthickness.surf.gii
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-dhcpAsym_den-32k_pial.surf.gii
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-dhcpAsym_den-32k_white.surf.gii
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-<span class="placeholder">&lt;dhcpAsym|fsaverage&gt;</span>_den-32k_sphere.surf.gii
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_desc-brain_mask.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_desc-preproc_T2w.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_dseg.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-<span class="placeholder">&lt;MNI152NLin6Asym_res-2|T2w&gt;</span>_label-<span class="placeholder">&lt;CSF|GM|WM&gt;</span>_probseg.nii.gz
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-T2w_desc-<span class="placeholder">&lt;aparcaseg|aseg&gt;</span>_dseg.nii.gz
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-T2w_dseg.nii.gz
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-T2w_desc-ribbon_mask.nii.gz <span class="hashtag">(+JSON)</span>
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_den-91k_<span class="placeholder">&lt;curv|sulc|thickness&gt;</span>.dscalar.nii <span class="hashtag">(+JSON)</span>
      |     |
      |     |_ fmap/
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_fmapid-auto00000<span class="label">{X}</span>_desc-coeff_fieldmap.nii.gz
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_fmapid-auto00000<span class="label">{X}</span>_desc-epi_fieldmap.nii.gz
      |     |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_fmapid-auto00000<span class="label">{X}</span>_desc-preproc_fieldmap.nii.gz <span class="hashtag">(+JSON)</span>
      |     |
      |     |_ func/ <span class="hashtag">(ALL +JSON)</span>
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_desc-brain_mask.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_desc-confounds_timeseries.tsv
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_desc-coreg_boldref.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_desc-hmc_boldref.nii.gz 
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_desc-preproc_bold.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_from-boldref_to-T2w_mode-image_desc-coreg_xfm.txt
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_from-boldref_to-auto00000_mode-image_xfm.txt
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_from-orig_to-boldref_mode-image_desc-hmc_xfm.txt
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsnative_bold.func.gii
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_boldref.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_desc-brain_mask.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_res-2_desc-preproc_bold.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-T2w_boldref.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-T2w_desc-brain_mask.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-T2w_desc-preproc_bold.nii.gz
      |        |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_bold.dtseries.nii
      |    
      |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.html
</pre>

### M-CRIB-S & FreeSurfer Source Directories

The `mcribs/` and `freesurfer/` derivatives folders are sourced from intermediate FreeSurfer-like folders generated by Infant-fMRIPrep during surface reconstruction - [see details](https://nibabies.readthedocs.io/en/latest/outputs.html#surface-reconstruction). Infant fMRIPrep supports three surface reconstruction methods, each optimized for a specific age range (see [Goncalves et al., 2025](https://doi.org/10.1101/2025.05.14.654069) for details):

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th>Surface Reconstruction Method</th>
      <th>Optimal Age Range</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
<tr>
    <td>M-CRIB-S</td>
    <td>≤ 5 months</td>
    <td style="word-wrap: break-word; white-space: normal;">Neonate method based on the Melbourne Children’s Regional Infant Brain atlases (<a href="https://doi.org/10.1038/s41598-020-61326-2">Adamson et al. 2020</a>)</td>
<tr>
<tr>
    <td>Infant FreeSurfer</td>
    <td>≥ 3 months</td>
    <td style="word-wrap: break-word; white-space: normal;">Modified version of FreeSurfer optimized for infants 0–2 years (<a href="https://doi.org/10.1016/j.neuroimage.2020.116946">Zöllei et al. 2020</a>)</td>
<tr>
<tr>
    <td>FreeSurfer</td>
    <td>≥ 10 months</td>
    <td style="word-wrap: break-word; white-space: normal;">Standard FreeSurfer, developed from adult data (<a href="https://doi.org/10.1006/nimg.1998.0395">Dale et al. 1998</a>)</td>
<tr>
</tbody>
</table>

The current HBCD release includes Infant-fMRIPrep derivatives for **visit V02 (0–1 months) using M-CRIB-S for surface reconstruction**. When M-CRIB-S is used, the `freesurfer/` folder is generated by mapping outputs from `mcribs/` to follow the structure of FreeSurfer’s [recon-all](https://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllOutputFiles) for compatibility. As a result, files in `freesurfer/` are identical to the corresponding source files in `mcribs/`.

<p>
<div id="fs" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">What is the difference between the FreeSurfer folders under M-CRIB-S vs. derivatives?</span>
    <a class="anchor-link" href="#fs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>The only difference between the M-CRIB-S FreeSurfer and derivatives FreeSurfer folder is that: 
<ul>
<li>M-CRIB-S FS: contains 2 symlink in place of regular files</li>
<li>Derivatives FS: includes 3 additional files, <code>scripts/mcribs.log</code> and <code>surf/<span class="placeholder">&lt;l|r&gt;</span>h.midthickness</code></li>
</ul>
</div>
</p>

#### FreeSurfer

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ freesurfer/
        |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>/
            |__ label/
            |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc+DKTatlas.annot
            |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc+DKTatlas.auto.nomask.annot
            |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc.annot
            |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc.auto.nomask.annot
            |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.cortex.label
            |
            |__ mri/
            |   |__ T2.mgz
            |   |__ aparc+<span class="placeholder">&lt;DKTatlas&gt;</span>+aseg.mgz
            |   |__ aseg.mgz
            |   |__ aseg.<span class="placeholder">&lt;internal|presurf|presurf.preunwmfix&gt;</span>.mgz
            |   |__ brain.mgz
            |   |__ brainmask.mgz
            |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.ribbon.mgz
            |   |__ norm.mgz
            |   |__ orig.mgz
            |   |__ ribbon.mgz
            |
            |__ scripts/
            |   |__ mcribs.log
            |
            |__ stats/
            |   |__aseg.stats
            |   |__brainvol.stats
            |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc+DKTatlas.stats
            |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.aparc.stats
            |   |__ <span class="placeholder">&lt;lh|rh&gt;</span>.curv.stats
            |
            |__ surf/
                |__ <span class="placeholder">&lt;lh|rh&gt;</span>.<span class="placeholder">&lt;area|area.mid|area.pial&gt;</span>
                |__ <span class="placeholder">&lt;lh|rh&gt;</span>.curv
                |__ <span class="placeholder">&lt;lh|rh&gt;</span>.inflated
                |__ <span class="placeholder">&lt;lh|rh&gt;</span>.inflated.<span class="placeholder">&lt;H|K&gt;</span>
                |__ <span class="placeholder">&lt;lh|rh&gt;</span>.midthickness
                |__ <span class="placeholder">&lt;lh|rh&gt;</span>.orig
                |__ <span class="placeholder">&lt;lh|rh&gt;</span>.pial
                |__ <span class="placeholder">&lt;lh|rh&gt;</span>.smoothwm
                |__ <span class="placeholder">&lt;lh|rh&gt;</span>.smoothwm.<span class="placeholder">&lt;BE|C|FI|H|K|K1|K2|S&gt;</span>.crv
                |__ <span class="placeholder">&lt;lh|rh&gt;</span>.smoothwm.<span class="placeholder">&lt;H|K&gt;</span>
                |__ <span class="placeholder">&lt;lh|rh&gt;</span>.sphere
                |__ <span class="placeholder">&lt;lh|rh&gt;</span>.sphere.<span class="placeholder">&lt;reg|reg2&gt;</span>
                |__ <span class="placeholder">&lt;lh|rh&gt;</span>.<span class="placeholder">&lt;sulc|thickness|volume|white&gt;</span>
</pre>

#### M-CRIB-S

<div id="symlinks" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-rotate-left"></i></span>
  <span class="text-with-link">
  <span class="text">Restoring Symlink Files</span>
  <a class="anchor-link" href="#symlinks" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>The M-CRIB-S folders contain four symlink files, which serve as references to data stored elsewhere. When these files are uploaded to the release bucket, they are renamed with the suffix <code>*_symlink_s3_object</code> to distinguish them from regular files. When downloaded, these symlink files appear as text files because they contain the S3 object path instead of the actual file content. To restore them as symlinks, run one of the following commands in the terminal:</p>
<p>Option 1: This command simply prints what commands to run to restore individual symlinks and does not change anything:</p>
<div class="copy-box">
  <div class="copy-text-container">
    <span id="specific-text-code">find . -type f -name "*_symlink_s3_object" -print | while read path ; do
  symval=$(cat "$path")
  symdir=$(dirname "$path")
  symbase=$(basename "$path" _symlink_s3_object)
  echo ln -s "$symval" "$symdir/$symbase" '&&' rm -f "$path"
done
    </span>
    <button class="copy-button">Copy</button>
  </div>
</div>
<p>Option 2: This restores all symlink files within the directory and renames them without <code>*_symlink_s3_object</code> to match the original sourcedata filenames:</p>
<div class="copy-box">
  <div class="copy-text-container">
    <span id="specific-text-code">find . -type f -name "*_symlink_s3_object" -print | while read path ; do
  symval=$(cat "$path")
  symdir=$(dirname "$path")
  symbase=$(basename "$path" _symlink_s3_object)
  ln -s "$symval" "$symdir/$symbase" && rm -f "$path" || break
done</span>
    <button class="copy-button">Copy</button>
  </div>
</div>
</div>

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ mcribs/
        |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>/
            |__ RawT2/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.nii.gz
            |
            |__ RawT2RadiologicalIsotropic/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.nii.gz_symlink_s3_object
            |
            |__ SurfReconDeformable/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>/
            |       |__ meshes/
            |       |   |__ <span class="placeholder">&lt;internal|pial+internal|pial|white+internal|white&gt;</span>.vtp
            |       |   |__ pial-<span class="placeholder">&lt;lh|rh&gt;</span>-reordered.vtp
            |       |   |__ pial-<span class="placeholder">&lt;lh|rh&gt;</span>.vtp
            |       |   |__ white-<span class="placeholder">&lt;lh|rh&gt;</span>.CortexMask.curv
            |       |   |__ white-<span class="placeholder">&lt;lh|rh&gt;</span>.Normals.surf
            |       |   |__ white-<span class="placeholder">&lt;lh|rh&gt;</span>.RegionId.curv
            |       |   |__ white-<span class="placeholder">&lt;lh|rh&gt;</span>.vtp
            |       |
            |       |__ recon/
            |       |   |__ cortical-hull-dmap.nii.gz
            |       |   |__ regions.nii.gz 
            |       |
            |       |__ temp/
            |           |__ <span class="placeholder">&lt;brain|cortex&gt;</span>-mask.nii.gz
            |           |__ cerebrum-<span class="placeholder">&lt;1|2|3&gt;</span>.vtp
            |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-<span class="placeholder">&lt;1|2|3&gt;</span>.vtp
            |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-2-output_<span class="placeholder">#</span>.vtp
            |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-dmap.nii.gz
            |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-hull-<span class="placeholder">#</span>.vtp
            |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-iso.vtp
            |           |__ cerebrum-<span class="placeholder">&lt;lh|rh&gt;</span>-mask.nii.gz
            |           |__ corpus-callosum-mask-<span class="placeholder">&lt;1|2|3&gt;</span>.nii.gz
            |           |__ deep-gray-matter-mask-<span class="placeholder">&lt;1|2&gt;</span>.nii.gz
            |           |__ gray-matter-mask-<span class="placeholder">&lt;1|2&gt;</span>.nii.gz
            |           |__ pial-<span class="placeholder">&lt;#|#-output_#&gt;</span>.vtp
            |           |__ pial-foreground.nii.gz
            |           |__ t2w-image.nii.gz_symlink_s3_object
            |           |__ ventricles-dmap.nii.gz
            |           |__ ventricles-mask-<span class="placeholder">&lt;1|2&gt;</span>.nii.gz
            |           |__ white-<span class="placeholder">&lt;#|#-output_#&gt;</span>.vtp
            |           |__ white-foreground.nii.gz
            |           |__ white-matter-mask-<span class="placeholder">&lt;1|2&gt;</span>.nii.gz
            |
            |__ TissueSeg/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_all_labels.nii.gz
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_all_labels_manedit.nii.gz_symlink_s3_object
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_brain_mask.nii.gz
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_t2w_restore.nii.gz_symlink_s3_object
            |
            |__ TissueSegDrawEM/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>/
            |       |__ N4/
            |           |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.nii.gz_symlink_s3_object
            |
            |__ freesurfer/ <span class="hashtag"># Only files unique to M-CRIB-S FreeSurfer subfolder displayed</span>
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>/
            |       |__ label/
            |       |__ mri/
            |       |   |__ brain.mgz_symlink_s3_object
            |       |   |__ orig.mgz_symlink_s3_object
            |       |__ stats/
            |       |__ surf/
            |
            |__ logs/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.log
            |
            |__ command.txt
</pre>


### XCP-D (`xcp_d/`)
XCP-D performs functional MRI post-processing and noise regression from Infant-fMRIPrep derivatives.      
[<i class="fa-solid fa-book"></i> Go to pipeline documentation](https://xcp-d.readthedocs.io/en/latest/)

<p>
<div id="fyi-nibabies" class="table-banner">
    <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">NOTE: The current release includes XCP-D derivatives for V02 only.
	</span>
</div>
</p>

<pre style="font-size: 10px;" class="folder-tree">
hbcd/
|_ derivatives/ 
   |_ xcp_d/
      |_ sub-<span class="label">{ID}</span>/
         |_ ses-<span class="label">{V0X}</span>/
         |  |_ anat/
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-MNI152NLin6Asym_desc-preproc_T2w.nii.gz
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-curv_morph.tsv
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-sulc_morph.tsv
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;APARC&gt;</span>_stat-mean_desc-thickness_morph.tsv
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span class="placeholder">&lt;inflated|vinflated&gt;</span>.surf.gii
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_hemi-<span class="placeholder">&lt;L|R&gt;</span>_space-fsLR_den-32k_<span class="placeholder">&lt;midthickness|pial|white&gt;</span>.surf.gii
         |  |  |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_space-fsLR_den-91k_<span class="placeholder">&lt;curv|sulc|thickness&gt;</span>.dscalar.nii
         |  |
         |  |_ func/ <span class="hashtag"># All func files have JSONs with exception of .hdf5 & *linc_qc.tsv</span>
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_desc-abcc_qc.hdf5 <span class="hashtag">(No JSON)</span>
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_<span class="placeholder">&lt;motion|outliers&gt;</span>.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_space-fsLR_den-91k_desc-denoised_bold.dtseries.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_den-91k_stat-mean_timeseries.ptseries.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-mean_timeseries.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-pearsoncorrelation_relmat.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_desc-abcc_qc.hdf5 <span class="hashtag">(No JSON)</span>
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_desc-linc_qc.tsv <span class="hashtag">(No JSON)</span>
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_<span class="placeholder">&lt;design|motion|outliers&gt;</span>.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_desc-denoised_bold.dtseries.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_stat-alff_boldmap.dscalar.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_stat-alff_desc-smooth_boldmap.dscalar.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_den-91k_stat-reho_boldmap.dscalar.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_den-91k_stat-coverage_boldmap.pscalar.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_den-91k_stat-mean_timeseries.ptseries.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_den-91k_stat-pearsoncorrelation_boldmap.pconn.nii
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-alff_bold.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-coverage_bold.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-mean_timeseries.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-pearsoncorrelation_relmat.tsv
         |     |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>-task-rest_dir-PA_run-<span class="label">{X}</span>_space-fsLR_seg-<span class="placeholder">&lt;PARC&gt;</span>_stat-reho_bold.tsv
         |  
         |_ figures/
         |_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_executive_summary.html
         |_ sub-<span class="label">{ID}</span>.html
</pre>


<div id="legend" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-tag"></i></span>
  <span class="text">Label Values Legend</span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<thead>
<tr>
    <th style="width: 10%;">BIDS Entity Label</th>
    <th style="width: 90%;">Values</th>
</tr>
</thead>
<tbody>
    <tr>
        <td><strong>&lt;APARC&gt;</strong> (anat/ parcellations)</td>
        <td>4S-&lt;1|2|3|4|5|6|7|8|9|10&gt;56Parcels, Glasser, Gordon, MIDB, MyersLabonte</td>
    </tr>
    <tr>
        <td><strong>&lt;PARC&gt;</strong> (func/ parcellations)</td>
        <td>4S-&lt;1|2|3|4|5|6|7|8|9|10&gt;56Parcels, Glasser, Gordon, MIDB, MyersLabonte, HCP, Tian</td>
    </tr>
</tbody>
</table>
</div>

## Quantitative MRI: SyMRI & qMRI Postproc

[SyMRI](https://syntheticmr.com/products/symri-neuro/), a proprietary software for quantitative MRI, is used to generate T1w and T2w images and derived relaxometry maps from [QALAS](https://pubmed.ncbi.nlm.nih.gov/25526880/) brain images. These outputs are then minimally preprocessed by [qMRI PostProc](https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html).

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

## Diffusion MRI

<pre class="folder-tree">
<span class="hashtag"># Diffusion MRI Pipeline Derivatives:</span>
hbcd/
|__ derivatives/ 
    |__ qsiprep/
    |__ qsirecon/
    |__ qsirecon-DIPYDKI/
    |__ qsirecon-DSIStudio/
    |__ qsirecon-NODDI/
    |__ qsirecon-TORTOISE_model-MAPMRI/
    |__ qsirecon-TORTOISE_model-tensor/
</pre>

### QSIPrep (`qsiprep/`) 
The QSIPrep pipeline is used for preprocessing the HBCD diffusion-weighted MRI (dMRI) data. Preprocessing includes head motion correction, susceptibility distortion correction, MP-PCA denoising, coregistration to T1w images, ANTS spatial normalization, and tissue segmentation. The QSIPrep derivatives are then passed to [QSIRecon](#qsirecon) for reconstruction.      
[<i class="fa-solid fa-book"></i> Go to pipeline documentation](https://qsiprep.readthedocs.io/)

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ qsiprep/
        |__ sub-<span class="label">{ID}</span>/
            |__ log/
            |__ ses-<span class="label">{V0X}</span>/
                |__ anat/
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_from-ACPC_to-anat_mode-image_xfm.mat        
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_from-ACPC_to-MNIInfant+1_mode-image_xfm.h5
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_from-anat_to-ACPC_mode-image_xfm.mat
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_from-MNIInfant+1_to-ACPC_mode-image_xfm.h5
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_from-orig_to-anat_mode-image_xfm.txt
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-aseg_dseg.nii.gz
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-brain_mask.nii.gz
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_T2w.json
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_T2w.nii.gz
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_dseg.nii.gz
                |
                |__ dwi/
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-confounds_timeseries.tsv
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-desc-pepolar_qc.tsv
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-brain_mask.nii.gz
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-image_qc.tsv
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_dwi.b
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_dwi.b_table.txt
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_dwi.bval
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_dwi.bvec
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-preproc_dwi.nii.gz <span class="hashtag">(+JSON)</span>
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_desc-slice_qc.json
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_dwiref.nii.gz
                |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-eddy_stat-cnr_dwimap.nii.gz <span class="hashtag">(+JSON)</span>
                |
                |__ figures/
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.html
</pre>

### QSIRecon 
QSIPrep derivatives are passed to QSIRecon for reconstruction, including ODF/FOD reconstruction, tractography, Fixel estimation, and regional connectivity. The data are processed using a variety of methods and models (e.g. [Dipy](https://dipy.org/), [MRTrix](https://www.mrtrix.org/), [DSI Studio](https://dsi-studio.labsolver.org/), etc).The [TORTOISE](https://github.com/QMICodeBase/TORTOISEV4) software calculates MAPMRI and Tensor fits and scalar maps.        
[<i class="fa-solid fa-book"></i> Go to pipeline documentation](https://qsirecon.readthedocs.io/)

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ qsirecon/
    |  |__ log/
    |
    |__ qsirecon-*/
        |__ sub-<span class="label">{ID}</span>/
            |__ ses-<span class="label">{V0X}</span>/
                |__ dwi/
                |__ figures/
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>.html    
</pre>  

<pre class="folder-tree" style="font-size: 11px;">
<span class="subses">qsirecon-DIPYDKI/</span>...dwi/
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-dki_param-<span class="placeholder">ad|ak|kfa|md|mk|mkt|rd|rk</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-dki_param-<span class="placeholder">ad|ak|kfa|md|mk|mkt|rd|rk</span>_dwimap.json
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-fa_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-fa_dwimap.json

<span class="subses">qsirecon-DSIStudio/</span>...dwi/
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_tdistats.tsv
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-Association<span class="placeholder">&lt;ASSOC&gt;</span><span class="placeholder">&lt;L|R&gt;</span>_streamlines.tck.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-Cerebellum<span class="placeholder">&lt;CEREB&gt;</span>_streamlines.tck.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-CommissureAnteriorCommissure_streamlines.tck.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-CommissureCorpusCallosum_streamlines.tck.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-ProjectionBasalGanglia<span class="placeholder">&lt;BG&gt;</span><span class="placeholder">&lt;L|R&gt;</span>_streamlines.tck.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundle-ProjectionBrainstem<span class="placeholder">&lt;BRAINSTEM&gt;</span>_streamlines.tck.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_bundlestats.csv
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_dwimap.fib.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_dwimap.fib.gz.icbm152_adult.map.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_param-<span class="placeholder">&lt;gfa|iso&gt;</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_param-qa_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_model-gqi_param-qa_dwimap.json
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-rdi_param-<span class="placeholder">&lt;rd1|rd2&gt;</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-<span class="placeholder">&lt;ad|fa|ha|md|rd&gt;</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-t<span class="placeholder">&lt;xx|xy|xz|yy|yz|zz&gt;</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-MNIInfant+1_model-gqi_param-<span class="placeholder">&lt;gfa|iso|qa&gt;</span>_dwimap.nii.gz

<span class="subses">qsirecon-TORTOISE_model-MAPMRI/</span>...dwi/
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-mapmri_param-<span class="placeholder">ng|ngpar|ngperp|pa|path|rtap|rtop|rtpp</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-mapmri_param-<span class="placeholder">ng|ngpar|ngperp|pa|path|rtap|rtop|rtpp</span>_dwimap.json
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-<span class="placeholder">&lt;TENSOR-PARAM&gt;</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-<span class="placeholder">&lt;ACPC|MNIInfant+1&gt;</span>_model-tensor_param-<span class="placeholder">&lt;TENSOR-PARAM&gt;</span>_dwimap.json

<span class="subses">qsirecon-TORTOISE_model-tensor/</span>...dwi/
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-ACPC_bundles-DSIStudio_scalarstats.tsv
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-MNIInfant+1_model-tensor_param-<span class="placeholder">ad|am|fa|li|rd</span>_dwimap.nii.gz
|_ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-MNIInfant+1_model-tensor_param-<span class="placeholder">ad|am|fa|li|rd</span>_dwimap.json
</pre>

<div id="legend" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-tag"></i></span>
  <span class="text">Label Values Legend (<i>DSI Studio</i>)</span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<thead>
<tr>
    <th style="width: 10%;">BIDS Entity Label</th>
    <th style="width: 90%;">Values</th>
</tr>
</thead>
<tbody>
  <tr>
      <td><strong>&lt;ASSOC&gt;</strong></td>
      <td style="word-wrap: break-word; white-space: normal;">ArcuateFasciculus, Cingulum, ExtremeCapsule, FrontalAslantTract, HippocampusAlveus, InferiorFrontoOccipitalFasciculus, InferiorLongitudinalFasciculus, MiddleLongitudinalFasciculus, ParietalAslantTract, SuperiorLongitudinalFasciculus, AssociationUncinateFasciculus, VerticalOccipitalFasciculus</td>
  </tr>
  <tr>
      <td><strong>&lt;CEREB&gt;</strong></td>
      <td style="word-wrap: break-word; white-space: normal;">Cerebellum(L/R), InferiorCerebellarPeduncle (L/R), MiddleCerebellarPeduncle, SuperiorCerebellarPeduncle, Vermis</td>
  </tr>
  <tr>
      <td><strong>&lt;BG&gt;</strong></td>
      <td style="word-wrap: break-word; white-space: normal;">AcousticRadiation, AnsaLenticularis, AnsaSubthalamica, CorticostriatalTract, FasciculusLenticularis, FasciculusSubthalamicus, Fornix, OpticRadiation, ThalamicRadiation</td>
  </tr>
  <tr>
      <td><strong>&lt;BRAINSTEM&gt;</strong></td>
      <td style="word-wrap: break-word; white-space: normal;">CorticobulbarTract(L\R), CorticopontineTract(L/R), CorticospinalTract(L/R), DentatorubrothalamicTractrl, MedialForebrainBundle(L/R), MedialLemniscus(L/R), NonDecussatingDentatorubrothalamicTract(L/R), ReticularTract(L/R)</td>
  </tr>
</tbody>
</table>
</div>

## MR Spectroscopy: OSPREY-BIDS

OSPREY-BIDS is the BIDS extension to the OSPREY pipeline used to process HBCD magnetic resonance spectroscopy (MRS) data. Only the `HERCULES/` file tree is displayed below. The `unedited/` files generally follow similar naming conventions, with some exceptions (e.g., the BIDS field `acq-shortTE` is used instead of `acq-hercules`).      
[<i class="fa-solid fa-book"></i> Go to pipeline documentation](https://osprey-bids.readthedocs.io/)

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ osprey/
        |__ sub-<span class="label">{ID}</span>/
            |__ ses-<span class="label">{V0X}</span>/
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
                |   |   |__ sub-<span class="label">{ID}</span>-report.html
                |   |
                |   |__ SegMaps/
                |   |   |__ TissueFractions_Voxel_1.tsv <span class="hashtag">(+JSON)</span>
                |   |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-hercules_svs.nii_space-scanner_Voxel-1_label-CSF.nii.gz
                |   |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-hercules_svs.nii_space-scanner_Voxel-1_label-GM.nii.gz
                |   |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-hercules_svs.nii_space-scanner_Voxel-1_label-Tha.nii.gz
                |   |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-hercules_svs.nii_space-scanner_Voxel-1_label-WM.nii.gz
                |   |
                |   |__ VoxelMasks/
                |   |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-hercules_svs_space-scanner_mask.nii.gz
                |   |
                |   |__ LogFile.txt
                |   |__ QM_processed_spectra.tsv <span class="hashtag">(+JSON)</span>
                |   |__ SummaryMRSinMRS.md
                |   |__ subject_names_and_excluded.tsv <span class="hashtag">(+JSON)</span>
                |   |__ wrapper_settings.mat <span class="hashtag">(+JSON)</span>
                |
                |__ unedited/
</pre>

## EEG: HBCD-MADE
HBCD-MADE produces preprocessed EEG derivatives.      
[<i class="fa-solid fa-book"></i> Go to pipeline documentation](https://docs-hbcd-made.readthedocs.io/)

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ made/
        |__ sub-<span class="label">{ID}</span>/
            |__ ses-<span class="label">{V0X}</span>/
                |__ eeg/
                    |__ filtered_data/
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_desc-filtered_eeg.fdt
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_desc-filtered_eeg.set
                    |
                    |__ ica_data/
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_adjustReport.txt
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-mergedICA_eeg.fdt
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-mergedICA_eeg.set
                    | 
                    |__ merged_data/
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-merged_eeg.fdt
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-merged_eeg.json
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-merged_eeg.set
                    | 
                    |__ processed_data/
                    |   |__ sub-<span class="label">{ID}</span>_task-FACE_desc-<span class="placeholder">&lt;FACE-JPG&gt;</span>.jpg
                    |   |__ sub-<span class="label">{ID}</span>_task-MMN_desc-<span class="placeholder">&lt;MMN-JPG&gt;</span>.jpg
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-RS_powerSummaryStats.csv
                    |   |__ sub-<span class="label">{ID}</span>_task-VEP_<span class="placeholder">&lt;desc-oz_ERP|topo&gt;</span>.jpg
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-<span class="placeholder">&lt;FACE|MMN|VEP&gt;</span>_acq-eeg_ERP.mat
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_desc-filteredprocessed_eeg.fdt
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_desc-filteredprocessed_eeg.set
                    | 
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-eeg_preprocessingReport.csv
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_MADEspecification.json
</pre>

<div id="legend" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-tag"></i></span>
  <span class="text">Label Values Legend</span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<thead>
<tr>
    <th style="width: 10%;">BIDS Entity Label</th>
    <th style="width: 90%;">Values</th>
</tr>
</thead>
<tbody>
    <tr>
        <td><strong>&lt;FACE-JPG&gt;</strong></td>
        <td>Oz_diffERP, diffInvVsUpr_topo, diffObjVsUp2_topo, inverted_topo, object_topo, oz_ERP, upright_topo, upright2_topo</td>
    </tr>
    <tr>
        <td><strong>&lt;MMN-JPG&gt;</strong></td>
        <td>deviant_topo, diffDevVsSta_topo, diffDevVsPre_topo, preDeviant_topo, standard_topo, t7t8_diffERP, t7t8_ERP</td>
    </tr>
</tbody>
</table>
</div>

## Biosensors: HBCD-Motion
The HBCD-Motion pipeline is used to process the HBCD Axivity Ax6 sensor recordings of infant leg movements across 72 continuous hours.      
[<i class="fa-solid fa-book"></i> Go to pipeline documentation](https://hbcd-motion-postproc.readthedocs.io/)

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ hbcd_motion/
        |__ sub-<span class="label">{ID}</span>/
            |__ ses-<span class="label">{V0X}</span>/
                |__ motion/
                    |__ Kinematics/
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-kinematics_recording-20_motion.json
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-kinematics_recording-25_motion.json
                    |
                    |__ PA/
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-accelerationPA_BOUTS.tsv
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-accelerationPA_LOG.txt
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-accelerationPA_RAW.tsv
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-accelerationPA_SUMMARY.json
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-jerkPA_BOUTS.tsv
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-jerkPA_LOG.txt
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-jerkPA_RAW.tsv
                    |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-jerkPA_SUMMARY.json
                    |
                    |__ PARAMETERS.json
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_leg-<span class="placeholder">&lt;left|right&gt;</span>_desc-calibrated_recording-20_motion.tsv
</pre>

<br>