<style>
.compact-table-no-vertical-lines th {
  white-space: nowrap !important;
}
.compact-table-no-vertical-lines td:nth-child(2) {
  white-space: nowrap !important;
}
</style>

<div id="pipelines" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
<i class="fa-solid fa-diagram-project"></i>
</span>
<span class="text-with-link">
    <span class="text">HBCD Processing Pipelines & Relevant Links to Documentation</span>
    <a class="anchor-link" href="#scoring" title="Copy link">
        <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow rotate">▸</span>
</div>
<div class="collapsible-content open">

<table class="compact-table-no-vertical-lines" width="100%">
<thead>
<tr>
  <th>Pipeline</th>
  <th>Derivative Folder</th>
  <th>Description</th>
  <th>Pipeline site</th>
  <th>NMIND Evaluation</th>
</tr>
</thead>
<tbody>

<tr class="table-group-row">
  <td colspan="5">Structural &amp; Functional MRI</td>
</tr>

<tr>
  <td><a href="https://mriqc.readthedocs.io/en/latest/">MRIQC</a></td>
  <td><code>mriqc/</code></td>
  <td>Extracts image quality metrics from raw MRI data</td>
  <td><a href="../../instruments/mri/smri/#qc-pipelines-mriqc-bme-x" aria-label="View HBCD file documentation for MRIQC" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/mriqc/" aria-label="View MRIQC NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://brain-mri-enhancement.readthedocs.io/">BME-X</a></td>
  <td><code>bme_x/</code></td>
  <td>Enhances structural T1w/T2w image quality</td>
  <td><a href="../../instruments/mri/smri/#qc-pipelines-mriqc-bme-x" aria-label="View HBCD file documentation for BME-X" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/bmex/" aria-label="View BME-X NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://bibsnet.readthedocs.io/en/latest/">BIBSNet</a></td>
  <td><code>bibsnet/</code></td>
  <td>Uses deep learning for brain segmentation</td>
  <td><a href="../../instruments/mri/smri/#bibsnet" aria-label="View HBCD file documentation for BIBSNet" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/bibsnet/" aria-label="View BIBSNet NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://nibabies.readthedocs.io/en/latest/">Infant-fMRIPrep</a></td>
  <td><code>nibabies/</code></td>
  <td>Preprocesses structural and functional MRI data</td>
  <td><a href="../../instruments/mri/fmri/#nibabies-derivs" aria-label="View HBCD file documentation for Infant-fMRIPrep" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/nibabies/" aria-label="View Infant-fMRIPrep NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://doi.org/10.1016/j.neuroimage.2020.116946">FreeSurfer</a></td>
  <td><code>freesurfer/</code></td>
  <td>Reconstructs cortical surfaces using the Infant FreeSurfer workflow run in Infant fMRIPrep</td>
  <td><a href="../../instruments/mri/smri/#fs" aria-label="View HBCD file documentation for FreeSurfer" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td>—</td>
</tr>
<tr>
  <td><a href="https://doi.org/10.1038/s41598-020-61326-2">M-CRIB-S</a></td>
  <td><code>mcribs/</code></td>
  <td>Reconstructs neonatal cortical surfaces using the M-CRIB-S workflow run in Infant fMRIPrep</td>
  <td><a href="../../instruments/mri/smri/#mcribs" aria-label="View HBCD file documentation for M-CRIB-S" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td>—</td>
</tr>
<tr>
  <td><a href="https://xcp-d.readthedocs.io/en/latest/">XCP-D</a></td>
  <td><code>xcp_d/</code></td>
  <td>Performs functional MRI post-processing and nuisance regression</td>
  <td><a href="../../instruments/mri/fmri/#xcpd-derivs" aria-label="View HBCD file documentation for XCP-D" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/xcpd/" aria-label="View XCP-D NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://pennlinc.github.io/ModelArray/">ModelArrayIO</a></td>
  <td><code>xcp_d-*-ModelArrayIO/</code></td>
  <td>Aggregates cohort-level HDF5 arrays</td>
  <td><a href="../../instruments/mri/fmri/#modelarrayio" aria-label="View HBCD file documentation for ModelArrayIO (fMRI)" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/" aria-label="Browse NMIND proceedings for ModelArrayIO (fMRI)" title="Browse NMIND proceedings"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="5">Quantitative MRI</td>
</tr>
<tr>
  <td><a href="https://syntheticmr.com/products/symri-neuro/">SyMRI</a></td>
  <td><code>symri/</code></td>
  <td>Generates synthetic MRI contrasts and quantitative tissue maps</td>
  <td><a href="../../instruments/mri/qmri/#processing-derivatives" aria-label="View HBCD file documentation for SyMRI" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td>—</td>
</tr>
<tr>
  <td><a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/">qMRI Postproc</a></td>
  <td><code>qmri_postproc/</code></td>
  <td>Performs minimal post-processing of SyMRI images</td>
  <td><a href="../../instruments/mri/qmri/#processing-derivatives" aria-label="View HBCD file documentation for qMRI Postproc" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/hbcd_qmri_postproc/" aria-label="View qMRI Postproc NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="5">Diffusion MRI</td>
</tr>
<tr>
  <td><a href="https://qsiprep.readthedocs.io/en/latest/">QSIPrep</a></td>
  <td><code>qsiprep/</code></td>
  <td>Preprocesses diffusion MRI (dMRI) data</td>
  <td><a href="../../instruments/mri/dmri/#qsiprep" aria-label="View HBCD file documentation for QSIPrep" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/qsiprep/" aria-label="View QSIPrep NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://qsirecon.readthedocs.io/en/latest/">QSIRecon</a></td>
  <td><code>qsirecon-*/</code></td>
  <td>Runs post-processing reconstruction workflows</td>
  <td><a href="../../instruments/mri/dmri/#qsirecon" aria-label="View HBCD file documentation for QSIRecon" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/qsirecon/" aria-label="View QSIRecon NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://pennlinc.github.io/ModelArray/">ModelArrayIO</a></td>
  <td><code>qsirecon-ModelArrayIO/</code></td>
  <td>Aggregates cohort-level HDF5 arrays</td>
  <td><a href="../../instruments/mri/dmri/#modelarrayio" aria-label="View HBCD file documentation for ModelArrayIO (dMRI)" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/" aria-label="Browse NMIND proceedings for ModelArrayIO (dMRI)" title="Browse NMIND proceedings"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="5">MR Spectroscopy</td>
</tr>
<tr>
  <td><a href="https://osprey-bids.readthedocs.io/en/latest/">OSPREY-BIDS</a></td>
  <td><code>osprey/</code></td>
  <td>Processes MRS data</td>
  <td><a href="../../instruments/mri/mrs/#derivatives" aria-label="View HBCD file documentation for OSPREY-BIDS" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/osprey_bids/" aria-label="View OSPREY-BIDS NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="5">EEG</td>
</tr>
<tr>
  <td><a href="https://docs-hbcd-made.readthedocs.io/en/latest/">HBCD-MADE</a></td>
  <td><code>made/</code></td>
  <td>Processes EEG data (adapted for HBCD)</td>
  <td><a href="../../instruments/eeg/hbcd-made/#hbcd-made-derivatives" aria-label="View HBCD file documentation for HBCD-MADE" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/hbcdmade/" aria-label="View HBCD-MADE NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="5">Wearable Sensors</td>
</tr>
<tr>
  <td><a href="https://hbcd-motion-postproc.readthedocs.io/en/latest/">HBCD-Motion</a></td>
  <td><code>motion/</code></td>
  <td>Processes leg movement data from wearable sensors</td>
  <td><a href="../../instruments/sensors/wearsensors/#derivatives" aria-label="View HBCD file documentation for HBCD-Motion" title="View HBCD file documentation"><i class="fa-solid fa-folder-tree" aria-hidden="true"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/hbcd_motion_postproc/" aria-label="View HBCD-Motion NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>

</tbody>
</table>

</div>