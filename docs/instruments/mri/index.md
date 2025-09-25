
# Magnetic Resonance Imaging & Spectroscopy

<div class="table-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">See <a href="https://hbcdsequences.readthedocs.io"><b>HBCD Study MRI Protocols</b></a> for full MRI protocols, sequence installation, and operation instructions.</span>
</div>
<p></p>

HBCD includes a suite of **magnetic resonance imaging (MRI)** and **spectroscopy (MRS)** data measures acquired as part of a comprehensive pediatric neuroimaging protocol, meticulously designed to overcome technical challenges of imaging early in life. MR data are acquired during visits V02, V03, V04, and V06 across all 27 Study recruitment sites. MRI modalities include **structural**, **functional**, **diffusion**, and **quantitative MRI** - select a modality in the left-hand table of contents to be directed to detailed measure descriptions.

## Release Data

MRI and MRS release data include both **file-based** (raw and processed data files in modality-specific formats) and **tabulated** (instrument and derived data in a standardized table format) data.      
<i>See the <a href="../../datacuration/overview" target="_blank">Data Structure Overview</a> for a full explanation of these data types.</i>

- <i class="fa fa-hammer"></i> <a href="../../datacuration/file-based-data/#raw-bids" target="_blank">Raw BIDS</a> under subject- and session-specific <code>rawdata/</code> folders
- <i class="fas fa-cog"></i> <a href="../../datacuration/file-based-data/#processed-derivatives" target="_blank">Derivatives</a> processed through MRI & MRS pipelines (see <a href="../processing" target="_blank">Processing Pipelines</a>)
- <i class="fas fa-table"></i> <a href="../../datacuration/phenotypes" target="_blank">Tabulated</a> data tables derived from pipeline derivatives - see full list of tables <a href="../#mri" target="_blank">here</a>

<pre class="folder-tree" style="font-size: 11px;">
hbcd/
|__ rawdata/ 
|   |__ phenotype/   <span class="hashtag"># Tabulated Data</span> 
|   |   |__ img_*   
|   |
|   |__ sub-<span class="label">{ID}</span>/    <span class="hashtag"># Raw BIDS (file-based data)</span>
|       |__ ses-<span class="label">{V0X}</span>/ 
|           |__ anat/
|           |__ dwi/
|           |__ fmap/
|           |__ func/
|           |__ mrs/
|
|__ derivatives/     <span class="hashtag"># Derivatives (file-based data)</span> 
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

## Quality Control 
See [HBCD MR Quality Control Procedures](qc.md) for a detailed information on MR QC.