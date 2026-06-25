<style>
.wy-nav-content {
    width: 85% !important;
    max-width: 85% !important;
    flex-grow: 1 !important;
}
.compact-table-no-vertical-lines th:nth-child(4),
.compact-table-no-vertical-lines th:nth-child(5),
.compact-table-no-vertical-lines td:nth-child(4),
.compact-table-no-vertical-lines td:nth-child(5) {
    text-align: center;
}
</style>

# HBCD Processing Pipelines

<div id="config" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Processing Configuration Details</span>
  <a class="anchor-link" href="#config" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Processing details for each pipeline are provided within the modality-specific documentation under <a href="../../instruments/">Study Instruments</a>, e.g., structural/functional MRI processing is described <a href="../../instruments/mri/fmri/#processing-derivatives">here</a>. Full technical details on how each pipeline was executed and configured is available in the <a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0/">HBCD Processing</a> documentation, with pipeline-specific parameters detailed under <a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0/tool_details.html#tool-names">Tool Names</a> (e.g., <b>File Selection For Processing</b> and <b>Quality Control Selection Information</b> documentation).
</div>
<p></p>

The HBCD processing pipelines are a collection of modular tools used to process HBCD Study data, including magnetic resonance imaging/spectroscopy (MRI/MRS), electroencephalography (EEG), and biosensor data. Pipeline outputs are provided within the data release as file-based <a href="../../datacuration/file-based-data/#derivatives" target="_blank">derivatives</a>. All community pipelines used for HBCD data processing must follow HBCD [Processing & Derivative Data Standards](standards.md). The table below includes links to the <a href="https://www.nmind.org/proceedings/">NMIND Evaluated Tools</a> page for each pipeline.

<div class="table-title">HBCD Processing Pipelines & Relevant Links to Documentation</div>
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
  <th>Pipeline</th>
  <th>Derivatives</th>
  <th>Description</th>
  <th>File Tree</th>
  <th>NMIND</th>
</tr>
</thead>
<tbody>
<tr class="table-group-row">
  <td colspan="5">Structural & Functional MRI</td>
</tr>
<tr>
  <td><a href="https://mriqc.readthedocs.io/en/latest/">MRIQC</a></td>
  <td><code>mriqc/</code></td>
  <td>Extracts image quality metrics from raw MRI data</td>
<td>
  <a href="../../instruments/mri/smri/#mriqc" target="_blank"><i class="fa-solid fa-folder-tree header icon"></i>
  </a>
</td>
  <td><a href="https://www.nmind.org/proceedings/mriqc/"><i class="fa fa-shield"></i></a></td>
</tr>
<tr>
  <td><a href="https://brain-mri-enhancement.readthedocs.io/">BME-X</a></td>
  <td><code>bme_x/</code></td>
  <td>Structural pipeline for T1w/T2w image quality enhancement</td>
  <td><a href="../../instruments/mri/smri/#mriqc" target="_blank">
  <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/bmex/"><i class="fa fa-shield"></i></a></td>
</tr>
<tr>
  <td><a href="https://bibsnet.readthedocs.io/en/latest/">BIBSNet</a></td>
  <td><code>bibsnet/</code></td>
  <td>Deep learning model for brain segmentation</td>
  <td><a href="../../instruments/mri/smri/#bibsnet-derivs" target="_blank">
    <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/bibsnet/"><i class="fa fa-shield"></i></a></td>
</tr>
<tr>
  <td><a href="https://nibabies.readthedocs.io/en/latest/">Infant-fMRIPrep</a></td>
  <td><code>nibabies/</code></td>
  <td>Structural and functional MRI preprocessing pipeline</td>
  <td><a href="../../instruments/mri/fmri/#nibabies-derivs" target="_blank">
    <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/nibabies/">
  <i class="fa fa-shield"></i></a></td>
</tr>
<tr>
  <td><a href="https://doi.org/10.1016/j.neuroimage.2020.116946">FreeSurfer</a></td>
  <td><code>freesurfer/</code></td>
  <td>Infant FreeSurfer surface reconstruction workflow run in fMRIPrep</td>
  <td>
    <a href="../../instruments/mri/fmri/#fs" target="_blank">
    <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td>—</td>
</tr>
<tr>
  <td><a href="https://doi.org/10.1038/s41598-020-61326-2">M-CRIB-S</a></td>
  <td><code>mcribs/</code></td>
  <td>Neonatal surface reconstruction workflow run in fMRIPrep</td>
  <td>
    <a href="../../instruments/mri/fmri/#mcribs" target="_blank">
    <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td>—</td>
</tr>
<tr>
  <td><a href="https://xcp-d.readthedocs.io/en/latest/">XCP-D</a></td>
  <td><code>xcp_d/</code></td>
  <td>Functional MRI post-processing and noise regression pipeline</td>
  <td><a href="../../instruments/mri/fmri/#xcpd-derivs" target="_blank">
      <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/xcpd/">
  <i class="fa fa-shield"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="5">Quantitative MRI</td>
</tr>
<tr>
  <td><a href="https://syntheticmr.com/products/symri-neuro/">SyMRI</a></td>
  <td><code>symri/</code></td>
  <td>Synthetic image generation</td>
  <td>
   <a href="../../instruments/mri/qmri/#qmri-derivs" target="_blank">
    <i class="fa-solid fa-folder-tree header icon"></i></a></td>
    <td>--</td>
</tr>
<tr>
  <td><a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html">qMRI Postproc</a></td>
  <td><code>qmri_postproc/</code></td>
  <td>Minimal post-processing of SyMRI images</td>
  <td><a href="../../instruments/mri/qmri/#qmri-derivs" target="_blank">
    <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/hbcd_qmri_postproc/"><i class="fa fa-shield"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="5">Diffusion MRI</td>
</tr>
<tr>
  <td><a href="https://qsiprep.readthedocs.io/en/latest/">QSIPrep</a></td>
  <td><code>qsiprep/</code></td>
  <td>dMRI data preprocessing pipeline</td>
  <td><a href="../../instruments/mri/dmri/#qsiprep" target="_blank">
  <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/qsiprep/"><i class="fa fa-shield"></i></a></td>
</tr>
<tr>
  <td><a href="https://qsirecon.readthedocs.io/en/latest/">QSIRecon</a></td>
  <td><code>qsirecon-<span class="tooltip">{RECON}<span class="tooltiptext">Workflows include DSIStudio, DIPYDKI, and TORTOISE_model-{MAPMRI|tensor}</span></span>/</code></td>
  <td>dMRI post-processing reconstruction workflows</td>
  <td><a href="../../instruments/mri/dmri/#qsirecon" target="_blank">
    <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/qsirecon/"><i class="fa fa-shield"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="5">MR Spectroscopy</td>
</tr>
<tr>
  <td><a href="https://osprey-bids.readthedocs.io/en/latest/index.html">OSPREY-BIDS</a></td>
  <td><code>osprey/</code></td>
  <td>MRS data processing pipeline</td>
  <td><a href="../../instruments/mri/mrs/#derivatives" target="_blank"><i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/osprey_bids/"><i class="fa fa-shield"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="5">EEG</td>
</tr>
<tr>
  <td><a href="https://docs-hbcd-made.readthedocs.io/en/latest/">HBCD-MADE</a></td>
  <td><code>made/</code></td>
  <td>EEG MADE pipeline adapted for HBCD</td>
  <td><a href="../../instruments/eeg/#made" target="_blank">
    <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/hbcdmade/"><i class="fa fa-shield"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="5">Wearable Sensors</td>
</tr>
<tr>
  <td><a href="https://hbcd-motion-postproc.readthedocs.io/en/latest/">HBCD-Motion</a></td>
  <td><code>motion/</code></td>
  <td>Leg movement sensor data processing</td>
  <td><a href="../../instruments/sensors/wearsensors/#derivatives" target="_blank">
  <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/hbcd_motion_postproc/"><i class="fa fa-shield"></i></a></td>
</tr>
</tbody>
</table>


