# BrainSwipes

Manual visual inspection remains the gold standard for detecting artifacts in structural, functional (e.g., XCP-D), and diffusion (e.g., QSIPrep) derivatives. To support this, derivative visual reports are integrated into [BrainSwipes](https://brainswipes.us/about), a gamified, crowdsourced QC platform built on the open-source [Swipes For Science](https://swipesforscience.org/) framework. BrainSwipes provides an intuitive interface for large-scale studies, guiding users through a short [tutorial](https://brainswipes.us/tutorial-select) before they evaluate images and classify them as pass or fail.

## QC Procedure Details
 <p>
<div id="swipes-procedures" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-brain"></i></span>
<span class="text-with-link">
  <span class="text">BrainSwipes QC Procedures</span>
    <a class="anchor-link" href="#swipes-procedures" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<br>
<div class="img-with-text" style="width: 60%; margin: 0 auto; text-align: center;">
    <img src="../images/brainswipes.png" alt="Example quality assessment of surface delineation in BrainSwipes" style="width: 100%; height: auto;">
    <p><i>Example quality assessment of surface delineation on BrainSwipes platform (displaying brain in axial plane at level of basal ganglia/putamen).</i></p>
</div>
<p>
<p style="font-size: 1em; margin: 0 0 5px;"><b>Surface Delineation:</b></p>
For structural QA, swipers are presented with image slices in coronal, axial, and sagittal planes to assess the accuracy of T1w and T2w surface delineations in differentiating gray and white matter. Images are derived from XCP-D visual reports.
</p>
<p style="font-size: 1em; margin: 0 0 5px;"><b>Atlas Registration:</b></p>
In addition to surface delineation, structural QA also includes atlas registration quality, evaluated by overlaying delineations of the subject’s image onto the atlas, and vice versa. Swipes display nine T1w slices for visual inspection, with three slices per anatomical plane. Quality is assessed based on the alignment of the outer boundaries of the overlaid contours with those of the underlying image, ensuring minimal gaps or misalignments. Images are derived from XCP-D visual reports.
<p>
<p style="font-size: 1em; margin: 0 0 5px;"><b>Functional Registration:</b></p>
Functional registration is evaluated by overlaying outlines of functional images onto structural images and vice versa. Swipes display nine slices of the same functional image for visual inspection, with three slices per anatomical plane. Quality is assessed similarly to structural atlas registration, focusing on the alignment of the overlaid contours. Additional evaluation includes checking for artifacts such as signal dropout. Images are derived from XCP-D visual reports.</p>
</div>
</p>

As described in the [procedure details](#swipes-procedures) above, structural and functional QC is performed based on a series of visual reports generated for processed outputs derived from the T1w/T2w and each BOLD run (one or more present per session). Each visual report is independently rated by reviewers as **Pass (1)** or **Fail (0)**. The BrainSwipes release data includes **(1)** the overall average QC score and average number of reviewers across visual reports for each modality as well as **(2)** the average QC score and number of reviewers for each visual report. 

**BrainSwipes QC results are used to exclude derivative outputs with severe data quality issues from the release - see <a href="../exclusion-criteria/#processed-data-exclusion-criteria" target="_blank">Processed Data Exclusion Criteria</a> for details.**



##  Location of BrainSwipes QC Results
### Release Data
BrainSwipes QC results are provided as <a href="../../#mri">tabulated data</a>, with unique hash identifiers indicating the surface-reconstruction method used in Infant fMRIPrep (see <a href="../mri-proc/#m-crib-s-freesurfer-surface-reconstruction-methods">M-CRIB-S & FreeSurfer Reconstruction Methods</a>):
<ul>
<li><code>img_brainswipes_xcpd_hash-0f306a2f+0ef9c88a_<span class="blue-text">&lt;T2w|bold&gt;</span></code> - <i>T2w-based surface reconstruction (M-CRIB-S)</i></li>
<li><code>img_brainswipes_xcpd_hash-2afa9081+0ef9c88a_<span class="blue-text">&lt;T1w|bold&gt;</span></code> - <i>T1w-based surface reconstruction (Infant FreeSurfer)</i></li>
</ul>

**Note that BrainSwipes QC scores should be available for all release data with the exception of visit V02 data processed using Infant FreeSurfer for surface reconstruction, which is not advised for use in analysis - see <a href="../mri-proc/#warning">Data Warning</a>.**

### Private Release Notes

BrainSwipes results will additionally be provided on a rolling basis between releases via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a> (*only accessible for DUC-authorized users*). This is done to provide users with the most up-to-date QC results to inform their anaylses. Files are provided in the same format as the release data, nested under folders named with the date that the results were provided.

**Maybe provide status?** eg no T2w-only sessions will have swipes, and vast majority of V02 processed via infant FS workflow are missing results as well 


  <a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/
nc_ch_bayley-supplemental.csv"><i class="fa-solid fa-download"></i> &nbsp; Download latest BrainSwipes Results</a> <i>(available to DUC-authorized users via the )</i>
