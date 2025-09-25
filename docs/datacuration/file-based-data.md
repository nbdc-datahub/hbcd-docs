# File-Based Data: Raw BIDS & Processed Derivatives

## Raw BIDS

The `rawdata/` folder includes raw <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> MR Imaging, MR Spectroscopy, EEG, and [wearable sensor](../instruments/sensors/wearsensors.md) recordings. The raw data has been converted to BIDS format, organized under subject and session-specific directories for processing through BIDS App pipelines ([see details](../instruments/processing/index.md)). 

<pre class="folder-tree" style="font-size: 11px;">
hbcd/
|__ rawdata/ 
    |__ sub-<span class="label">{ID}</span>/
    |   |__ sub-<span class="label">{ID}</span>_sessions.tsv
    |   |__ sub-<span class="label">{ID}</span>_sessions.json
    |   |__ ses-<span class="label">{V0X}</span>/
    |       |__ anat/
    |       |__ dwi/
    |       |__ eeg/
    |       |__ fmap/
    |       |__ func/
    |       |__ motion/
    |       |__ mrs/
    |       |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_scans.tsv
    |       |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_scans.json
    |
    |__ dataset_description.json
    |__ participants.tsv
    |__ participants.json 
</pre>
<p></p>

### Fields Reporting Age

See description of fields reporting age under Age Variable Definitions > <a href="../../instruments/agevariables/#raw-file-based-data" target="_blank">Raw File-Based Data</a>.

### Participant-, Session-, & Scan-Level Data
Participant-, session-, and scan-level data are stored in the following `.tsv` files, accompanied by `.json` sidecar files containing metadata:

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead>
<tr>
  <th>Level</th>
  <th>File Name</th>
  <th style="width: 60%;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Participant</td>
  <td><code>participants.tsv</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Basic demographic and participant information (e.g., sex)</td>
</tr>
<tr>
  <td>Session</td>
  <td><code>sub-&lt;ID&gt;_sessions.tsv</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Session information (e.g., collection site, participant’s age at each session, head size)</td>
</tr>
<tr>
  <td>Scan</td>
  <td><code>sub-&lt;ID&gt;_ses-&lt;V0X&gt;_scans.tsv</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Per-scan information (age at scan and raw data QC scores - see <a href="../../../instruments/mri/qc/#location-of-raw-data-qc-results-in-data-release" target="_blank">HBCD MR Quality Control Procedures</a>)</td>
</tr>
</tbody>
</table>

### Modality-Specific Data
<i>Expand the section below for links to detailed descriptions of each raw BIDS folder and its contents.</i>

<div id="rawbids-links" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-link"></i></span>
  <span class="text-with-link">
<span class="text">Links to Detailed Folder Descriptions</span>
  <a class="anchor-link" href="#rawbids-links" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Raw BIDS Folder</th>
  <th>Relevant Modalities With Link to Documentation</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="2"><code>anat/</code></td>
  <td><a href="../../instruments/mri/smri/#rawbids" target="_blank">Structural MRI</a></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/qmri/#rawbids" target="_blank">Quantitative MRI</a></td>
</tr>
<tr>
  <td><code>func/</code> & <code>fmap/</code></td>
  <td><a href="../../instruments/mri/fmri/#rawbids" target="_blank">Functional MRI</a></td>
</tr>
<tr>
  <td><code>dwi/</code></td>
  <td><a href="../../instruments/mri/dmri/#rawbids" target="_blank">Diffusion MRI</a></td>
</tr>
<tr>
  <td><code>mrs/</code></td>
  <td><a href="../../instruments/mri/mrs/#rawbids" target="_blank">MR Spectroscopy</a></td>
</tr>
<tr>
  <td><code>eeg/</code></td>
  <td><a href="../../instruments/eeg/#rawbids" target="_blank">EEG</a></td>
</tr>
<tr>
  <td><code>motion/</code></td>
  <td><a href="../../instruments/sensors/wearsensors/#rawbids" target="_blank">Wearable Sensors</a></td>
</tr>
</tbody>
</table>
</div>

## Processed Derivatives

The `derivatives/` folder contains derivatives, which are file outputs from <a href="../../instruments/processing/" target="_blank">processing pipelines</a>. 

<pre class="folder-tree" style="font-size: 11px;">
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
<p></p>

### Links to Pipeline Derivatives

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Modalities</th>
  <th>Derivatives Folder</th>
  <th>Pipeline Name & Link to Derivatives Documentation</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="5">Structural & Functional MRI</td>
  <td><code>mriqc/</code></td>
  <td>MRIQC - <a href="../../instruments/mri/smri/#mriqc" target="_blank">sMRI</a> & <a href="../../instruments/mri/fmri/#mriqc" target="_blank">fMRI</a></td>
</tr>
<tr>
  <td><code>bibsnet/</code></td>
  <td><a href="../../instruments/mri/smri/#bibsnet" target="_blank">BIBSNet</a></td>
</tr>
<tr>
  <td><code>nibabies/</code></td>
  <td><a href="../../instruments/mri/fmri/#nibabies" target="_blank">Infant fMRIPrep (or Nibabies)</a></td>
</tr>
<tr>
  <td><code>freesurfer/</code> & <code>mcribs/</code></td>
  <td><a href="../../instruments/mri/fmri/#fs-mcribs" target="_blank">FreeSurfer & M-CRIB-S</a></td>
</tr>
<tr>
  <td><code>xcp_d/</code></td>
  <td><a href="../../instruments/mri/fmri/#xcpd" target="_blank">XCP-D</a></td>
</tr>
<tr>
  <td rowspan="2">Quantitative MRI</td>
  <td><code>symri/</code></td>
  <td><a href="../../instruments/mri/qmri/#derivatives" target="_blank">SyMRI</a></td>
</tr>
<tr>
  <td><code>qmri_postproc/</code></td>
  <td><a href="../../instruments/mri/qmri/#derivatives" target="_blank">qMRI PostProc</a></td>
</tr>
<tr>
  <td rowspan="6">Diffusion MRI</td>
  <td><code>qsiprep/</code></td>
  <td><a href="../../instruments/mri/dmri/#qsiprep" target="_blank">QSIPrep</a></td>
</tr>
<tr>
  <td><code>qsirecon/</code></td>
  <td><a href="../../instruments/mri/dmri/#qsirecon" target="_blank">QSIRecon</a></td>
</tr>
<tr>
  <td><code>qsirecon-DSIStudio/</code></td>
  <td><a href="../../instruments/mri/dmri/#qsirecon-DSIStudio" target="_blank">QSIRecon-DSI Studio</a></td>
</tr>
<tr>
  <td><code>qsirecon-DIPYDKI/</code></td>
  <td><a href="../../instruments/mri/dmri/#qsirecon-DIPYDKI" target="_blank">QSIRecon-DIPY DKI</a></td>
</tr>
<tr>
  <td><code>qsirecon-TORTOISE_model-MAPMRI/</code></td>
  <td><a href="../../instruments/mri/dmri/#qsirecon-TORTOISE" target="_blank">QSIRecon-TORTOISE MAP-MRI</a></td>
</tr>
<tr>
  <td><code>qsirecon-TORTOISE_model-tensor/</code></td>
  <td><a href="../../instruments/mri/dmri/#qsirecon-TORTOISE" target="_blank">QSIRecon-TORTOISE Tensor</a></td>
</tr>
<tr>
  <td>MR Spectroscopy</td>
  <td><code>osprey/</code></td>
  <td><a href="../../instruments/mri/mrs/#derivatives" target="_blank">OSPREY-BIDS</a></td>
</tr>
<tr>
  <td>EEG</td>
  <td><code>made/</code></td>
  <td><a href="../../instruments/eeg/#made" target="_blank">HBCD-MADE</a></td>
</tr>
<tr>
  <td>Wearable Sensors</td>
  <td><code>motion/</code></td>
  <td><a href="../../instruments/sensors/wearsensors/#derivatives" target="_blank">HBCD-Motion</a></td>
</tr>
</tbody>
</table>

<br>