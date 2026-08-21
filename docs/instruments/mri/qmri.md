# Quantitative MRI (qMRI)

{{ alert_warning(instruments.qmri) }}
{{ data_warning(instruments.qmri) }}

---

{{ instrument_description(instruments.qmri) }}

<!-- ## Acquisition  -->

{{ suppx(instruments.qmri, "1") }}

<!-- ## Processing & Derivatives -->
{{ suppx(instruments.qmri, "2") }}

<span><a href="../../../datacuration/overview/#filetrees"><i class="fa fa-circle-info"></i> How To Read File Trees</a></span>
<pre class="folder-tree">
hbcd/
└── derivatives/
    <span class="hashtag"># SyMRI</span>
    ├── symri/ 
    │   └── sub-[ID]/
    │       └── ses-[V0X]/
    │           └── anat/
    │               ├── sub-[ID]_ses-[V0X]_acq-QALAS_{T1w|T2w}.nii.gz
    │               ├── sub-[ID]_ses-[V0X]_acq-QALAS_T2map.nii.gz
    │               └── sub-[ID]_ses-[V0X]_acq-QALAS_desc-SymriContainer.log
    │
    <span class="hashtag"># qMRI PostProc</span>
    └── qmri_postproc/
        └── sub-[ID]/
            └── ses-[V0X]/
                └── anat/
                    ├── sub-[ID]_ses-[V0X]_desc-AsegROIs_scalarstats.tsv
                    ├── sub-[ID]_ses-[V0X]_desc-BilateralAsegROIs_scalarstats.tsv
                    ├── sub-[ID]_ses-[V0X]_desc-RegistrationQCAid.png   
                    ├── sub-[ID]_ses-[V0X]_space-T2w_desc-QALAS_T2map.nii.gz
                    └── sub-[ID]_ses-[V0X]_space-QALAS_desc-aseg_dseg.nii.gz
</pre>

---

{{ references(instruments.qmri) }}




<!-- 
qMRI data are processed via <a href="https://syntheticmr.com/products/symri-neuro/">SyMRI</a> followed by minimal post-processing through <a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html">qMRI PostProc</a>. SyMRI derives synthetic T1w/T2w images and quantitative relaxometry maps from 3D-QALAS acquisitions by reintroducing estimated T1/T2 relaxation times into the MR signal equation (Bloch equations). -->

<!-- <div id="qmri-derivs" class="banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">SyMRI & qMRI PostProc Derivatives</span>
  <a class="anchor-link" href="#qmri-derivs" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<span><a href="../../../datacuration/overview/#filetrees"><i class="fa fa-circle-info"></i> How To Read File Trees →</a></span>
</div> -->
