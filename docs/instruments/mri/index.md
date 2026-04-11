# Overview

HBCD includes a suite of **magnetic resonance imaging (MRI)** and **spectroscopy (MRS)** data measures acquired as part of a comprehensive pediatric neuroimaging protocol, meticulously designed to overcome technical challenges of imaging early in life. MR data are acquired during visits V02, V03, V04, and V06 across all 27 Study recruitment sites. MR modalities include the following - click to be directed to modality documentation pages:

<ul>
<li><a href="smri" target="_blank">Structural MRI (sMRI)</a></li>
<li><a href="fmri" target="_blank">Functional MRI (fMRI)</a></li>
<li><a href="dmri" target="_blank">Diffusion MRI (dMRI)</a></li>
<li><a href="qmri" target="_blank">Quantitative MRI (qMRI)</a></li>
<li><a href="mrs" target="_blank">Magnetic Resonance Spectroscopy (MRS)</a></li>
</ul>

## HBCD Study MRI Protocols

See <a href="https://hbcdsequences.readthedocs.io"><b>HBCD Study MRI Protocols</b></a> for full MRI protocols, sequence installation, and operation instructions.

## Release Data

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">Please review the <a href="https://docs.hbcdstudy.org/latest/changelog/issues-updates/" target="_blank">Known Issues & Pending Updates</a> page for updates that may affect data use.</span>
</div>
<p></p>

MRI and MRS release data include the following - <i>see <a href="../../datacuration/overview" target="_blank">Data Structure Overview</a> for explanation of these data types</i>:

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b><i class="fas fa-hammer header-icon"></i> Raw BIDS</b></td>
<td>File-based data in modality-specific formats under subject- and session-specific <code>rawdata/</code> folders</td></tr>
<tr><td><b><i class="fas fa-cog header-icon"></i> Derivatives</b></td>
<td>File-based data in modality-specific formats processed through <a href="../processing" target="_blank">HBCD pipelines</a></td></tr>
<tr><td><b><i class="fas fa-table header-icon"></i> Tabulated Data</b></td>
<td style="word-wrap: break-word; white-space: normal;">Includes (1) questionnaires and (2) select derivative data compiled across participants in HBCD-tabulated format (see <a href="../#mri-tab" target="_blank">Tabulated Imaging</a>)</td></tr>
</tbody></table>

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