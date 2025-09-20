# Magnetic Resonance Imaging & Spectroscopy

HBCD includes a suite of **magnetic resonance imaging (MRI)** and **spectroscopy (MRS)** data measures acquired as part of a comprehensive pediatric neuroimaging protocol, meticulously designed to overcome technical challenges of imaging early in life. MR data are acquired during visits V02, V03, V04, and V06 across all 27 Study recruitment sites. MR modalities include the following - click to be directed to modality documentation pages:

<ul>
<li><a href="smri" target="_blank">Structural MRI (sMRI)</a></li>
<li><a href="fmri" target="_blank">Functional MRI (fMRI)</a></li>
<li><a href="dmri" target="_blank">Diffusion MRI (dMRI)</a></li>
<li><a href="qmri" target="_blank">Quantitative MRI (qMRI)</a></li>
<li><a href="mrs" target="_blank">Magnetic Resonance Spectroscopy (MRS)</a></li>
</ul>

## Release Data

MRI and MRS data in the release includes <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> and <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> data:

- <i class="fa fa-hammer"></i> <a href="../../../datacuration/rawbids/#imaging" target="_blank">Raw BIDS</a> under subject- and session-specific <code>eeg/</code> folders (*file-based data*)
- <i class="fas fa-cog"></i> <a href="../../../datacuration/derivatives" target="_blank">Derivatives</a> processed through pipelines designed for <a href="../../../datacuration/derivatives/#structural-functional-mri" target="_blank">sMRI & fMRI</a>, <a href="../../../datacuration/derivatives/#diffusion-mri" target="_blank">dMRI</a>, and <a href="../../../datacuration/derivatives/#mr-spectroscopy-osprey-bids" target="_blank">MRS</a> (*file-based data*)
- <i class="fas fa-table"></i> <a href="../../../datacuration/phenotypes" target="_blank">Tabulated</a> data tables derived from pipeline derivatives - see full list of tables <a href="../#mri" target="_blank">here</a>

<pre class="folder-tree">
hbcd/
|__ rawdata/ 
|   |
| <span class="hashtag"># Tabulated Data</span>
|   |__ phenotype/     
|   |   |__ img_*
|   |
| <span class="hashtag"># Raw BIDS (file-based data)</span>
|   |__ sub-<span class="label">&lt;label&gt;</span>/
|       |__ ses-<span class="label">&lt;label&gt;</span>/
|           |__ anat/
|           |__ dwi/
|           |__ fmap/
|           |__ func/
|           |__ mrs/
| <span class="hashtag"># Derivatives (file-based data)</span>
|__ derivatives/       
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

## Quality Control 
See [HBCD MR Quality Control Procedures](qc.md) for a detailed information on MR QC.