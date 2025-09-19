# Magnetic Resonance Imaging & Spectroscopy

HBCD includes a suite of **magnetic resonance imaging (MRI)** and **spectroscopy (MRS)** data measures acquired as part of a comprehensive pediatric neuroimaging protocol, meticulously designed to overcome technical challenges of imaging early in life. MR data are acquired during visits V02, V03, V04, and V06 across all 27 Study recruitment sites. Please see [Quality Control Procedures](qc.md) for a detailed information on MR QC and the following sections for a summary of each modality:

<ul>
<li><a href="smri" target="_blank">Structural MRI (sMRI)</a></li>
<li><a href="fmri" target="_blank">Functional MRI (fMRI)</a></li>
<li><a href="dmri" target="_blank">Diffusion MRI (dMRI)</a></li>
<li><a href="qmri" target="_blank">Quantitative MRI (qMRI)</a></li>
<li><a href="mrs" target="_blank">Magnetic Resonance Spectroscopy (MRS)</a></li>
</ul>

## Release Data
MRI and MRS data in the release includes <span class="tooltip">tabulated data<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> (see table names listed [here](../index.md#mri)) and the following <span class="tooltip">file-based data<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span>:

- <i class="fa fa-hammer"></i><strong> Raw BIDS</strong> under subject- and session-specific folders - <a href="../../../datacuration/rawbids/#imaging">see details</a>
- <i class="fas fa-cog"></i><strong> Derivatives</strong> produced by various pipelines - <a href="../../../datacuration/derivatives">see details</a>

*HBCD data structure summary with only MRI & MRS data included:*
<pre class="folder-tree">
hbcd/
|__ rawdata/ 
|   |__ phenotype/     <span class="hashtag"># Tabulated Data</span>
|   |   |__ img_*
|   |
|   |__ sub-<span class="label">&lt;label&gt;</span>/   <span class="hashtag"># Raw BIDS (file-based data)</span>
|       |__ ses-<span class="label">&lt;label&gt;</span>/
|           |__ anat/
|           |__ dwi/
|           |__ fmap/
|           |__ func/
|           |__ mrs/
|
|__ derivatives/       <span class="hashtag"># Derivatives (file-based data)</span>
    |__ bibsnet/
    |__ freesurfer/
    |__ mcribs/
    |__ mriqc/
    |__ nibabies/
    |__ qmri_postproc/
    |__ qsiprep/
    |__ qsirecon/
    |__ qsirecon-*/
    |__ symri/
    |__ xcp_d/
</pre>


## MRI Protocols & Sequence Installation
For full MRI protocols for sequence installation and operation instructions, please visit <a href="https://hbcdsequences.readthedocs.io"><b>HBCD Study MRI Protocols</b></a>.