# Structural MRI

{{ alert_warning(instruments.smri) }}
{{ data_warning(instruments.smri) }}
{{ issues_banner() }}

## Overview & Acquisition

{{ instrument_description(instruments.smri) }}

## Processing & Derivatives

<p style="font-size: 2em; color: red;">ADD OVERVIEW TEXT</p>


### BIBSNet

BIBSNet is a deep learning model optimized for infant MRI brain tissue segmentation (<a href="https://doi.org/10.1101/2023.03.22.533696">Hendrickson et al. 2024</a>). The <a href="https://bibsnet.readthedocs.io/en/latest/">BIBSNet pipeline</a> generates native-space brain segmentations and brain masks (as well as <code>volumes.tsv</code> files with ROI volume statistics), which are fed into Infant fMRIPrep for use in anatomical preprocessing and surface reconstruction.

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

---

{{ references(instruments.smri) }}