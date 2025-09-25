
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

MRI and MRS release data include both **file-based** (raw and processed data files in modality-specific formats) and **tabulated** (instrument and derived data in a standardized table format) data.      
<i>See the <a href="../../datacuration/overview" target="_blank">Data Structure Overview</a> for a full explanation of these data types.</i>

- <i class="fa fa-hammer"></i> <a href="../../datacuration/file-based-data/#raw-bids" target="_blank">Raw BIDS</a> under subject- and session-specific <code>rawdata/</code> folders
- <i class="fas fa-cog"></i> <a href="../../datacuration/file-based-data/#processed-derivatives" target="_blank">Derivatives</a> processed through MRI & MRS pipelines (see <a href="../processing" target="_blank">Processing Pipelines</a>)
- <i class="fas fa-table"></i> <a href="../../datacuration/phenotypes" target="_blank">Tabulated</a> data tables derived from pipeline derivatives - see full list of tables <a href="../#mri" target="_blank">here</a>

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