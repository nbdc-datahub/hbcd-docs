# Processing & Derivative Data Standards

## HBCD Processing Pipelines

The HBCD processing pipelines are a collection of modular tools used to process HBCD Study data, including magnetic resonance imaging/spectroscopy (MRI/MRS), electroencephalography (EEG), and biosensor data. Pipeline outputs are provided within the data release as file-based derivatives. The table below includes links to the <a href="https://www.nmind.org/proceedings/">NMIND Evaluated Tools</a> page for each pipeline.

**Full technical details on how each pipeline was executed and configured is available in the [HBCD Processing](https://hbcd-cbrain-processing.readthedocs.io/release_2.0/) documentation,** with pipeline-specific parameters detailed under **Tool Names** (e.g., 'File Selection For Processing' and 'Quality Control Selection Information').

<style>
.compact-table-no-vertical-lines th {
  white-space: nowrap !important;
}
.compact-table-no-vertical-lines td:nth-child(2) {
  white-space: nowrap !important;
}
.compact-table-no-vertical-lines td:nth-child(4) {
    text-align: center;
}
</style>

<div id="pipelines" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
<i class="fa-solid fa-diagram-project"></i>
</span>
<span class="text-with-link">
    <span class="text">HBCD Processing Pipelines & Relevant Links to Documentation</span>
    <a class="anchor-link" href="#pipelines" title="Copy link">
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
  <th>HBCD Derivatives</th>
  <th>Pipeline Description</th>
  <th>NMIND</th>
</tr>
</thead>
<tbody>

<tr class="table-group-row">
  <td colspan="4">Structural &amp; Functional MRI</td>
</tr>

<tr>
  <td><a href="https://mriqc.readthedocs.io/en/latest/">MRIQC</a></td>
    <td><a href="../../instruments/mri/smri/#qc-pipelines-mriqc-bme-x" aria-label="View HBCD file documentation for MRIQC" title="View HBCD file documentation"><code>mriqc/</code></a></td>
  <td>Extracts image quality metrics from raw MRI data</td>
  <td><a href="https://www.nmind.org/proceedings/mriqc/" aria-label="View MRIQC NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://brain-mri-enhancement.readthedocs.io/">BME-X</a></td>
<td><a href="../../instruments/mri/smri/#qc-pipelines-mriqc-bme-x" aria-label="View HBCD file documentation for BME-X" title="View HBCD file documentation"><code>bme_x/</code></a></td>
  <td>Enhances structural T1w/T2w image quality</td>
  <td><a href="https://www.nmind.org/proceedings/bmex/" aria-label="View BME-X NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://bibsnet.readthedocs.io/en/latest/">BIBSNet</a></td>
    <td><a href="../../instruments/mri/smri/#bibsnet" aria-label="View HBCD file documentation for BIBSNet" title="View HBCD file documentation"><code>bibsnet/</code></a></td>
  <td>Performs automated tissue segmentation for infant MRI via deep learning model</td>
  <td><a href="https://www.nmind.org/proceedings/bibsnet/" aria-label="View BIBSNet NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://nibabies.readthedocs.io/en/latest/">Infant-fMRIPrep</a></td>
  <td>
    <code>nibabies-d902942d/</code>
    <br>
    <code>nibabies-d902942d/</code>
  </td>
    <td>Preprocesses structural and functional MRI data <a href="../../instruments/mri/fmri/#infant-fmriprep"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/nibabies/" aria-label="View Infant-fMRIPrep NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://doi.org/10.1016/j.neuroimage.2020.116946">FreeSurfer</a></td>
  <td><a href="../../instruments/mri/smri/#m-crib-s-freesurfer" aria-label="View HBCD file documentation for FreeSurfer" title="View HBCD file documentation"><code>freesurfer/</code></a></td>
  <td>Reconstructs cortical surfaces (workflow run in Infant fMRIPrep)</td>
  <td>—</td>
</tr>
<tr>
  <td><a href="https://doi.org/10.1038/s41598-020-61326-2">M-CRIB-S</a></td>
    <td><a href="../../instruments/mri/smri/#m-crib-s-freesurfer" aria-label="View HBCD file documentation for M-CRIB-S" title="View HBCD file documentation"><code>mcribs/</code></a></td>
  <td>Reconstructs neonatal cortical surfaces (workflow run in Infant fMRIPrep)</td>
  <td>—</td>
</tr>
<tr>
  <td><a href="https://xcp-d.readthedocs.io/en/latest/">XCP-D</a></td>
  <td><a href="../../instruments/mri/fmri/#xcp-d" aria-label="View HBCD file documentation for XCP-D" title="View HBCD file documentation"><code>xcp_d/</code></a></td>
  <td>Performs functional MRI post-processing (denoising, connectivity matrices, etc.)</td>
  <td><a href="https://www.nmind.org/proceedings/xcpd/" aria-label="View XCP-D NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://pennlinc.github.io/ModelArray/">ModelArrayIO</a></td>
  <td><a href="../../instruments/mri/fmri/#modelarrayio" aria-label="View HBCD file documentation for ModelArrayIO (fMRI)" title="View HBCD file documentation"><code>xcp_d-*-ModelArrayIO/</code></a></td>
  <td>Aggregates cohort-level HDF5 arrays from XCP-D</td>
  <td><a href="https://www.nmind.org/proceedings/" aria-label="Browse NMIND proceedings for ModelArrayIO (fMRI)" title="Browse NMIND proceedings"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="4">Quantitative MRI</td>
</tr>
<tr>
  <td><a href="https://syntheticmr.com/products/symri-neuro/">SyMRI</a></td>
  <td><a href="../../instruments/mri/qmri/#processing-derivatives" aria-label="View HBCD file documentation for SyMRI" title="View HBCD file documentation"><code>symri/</code></a></td>
  <td>Generates synthetic MRI contrasts and quantitative tissue maps</td>
  <td>—</td>
</tr>
<tr>
  <td><a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/">qMRI Postproc</a></td>
  <td><a href="../../instruments/mri/qmri/#processing-derivatives" aria-label="View HBCD file documentation for qMRI Postproc" title="View HBCD file documentation"><code>qmri_postproc/</code></a></td>
  <td>Performs minimal post-processing of SyMRI images</td>
  <td><a href="https://www.nmind.org/proceedings/hbcd_qmri_postproc/" aria-label="View qMRI Postproc NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="4">Diffusion MRI</td>
</tr>
<tr>
  <td><a href="https://qsiprep.readthedocs.io/en/latest/">QSIPrep</a></td>
  <td><a href="../../instruments/mri/dmri/#qsiprep" aria-label="View HBCD file documentation for QSIPrep" title="View HBCD file documentation"><code>qsiprep/</code></a></td>
  <td>Preprocesses dMRI data (e.g. motion and distortion correction)</td>
  <td><a href="https://www.nmind.org/proceedings/qsiprep/" aria-label="View QSIPrep NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://qsirecon.readthedocs.io/en/latest/">QSIRecon</a></td>
  <td><a href="../../instruments/mri/dmri/#qsirecon" aria-label="View HBCD file documentation for QSIRecon" title="View HBCD file documentation"><code>qsirecon-*/</code></a></td>
  <td>Runs post-processing reconstruction workflows</td>
  <td><a href="https://www.nmind.org/proceedings/qsirecon/" aria-label="View QSIRecon NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>
<tr>
  <td><a href="https://pennlinc.github.io/ModelArray/">ModelArrayIO</a></td>
  <td><a href="../../instruments/mri/dmri/#modelarrayio" aria-label="View HBCD file documentation for ModelArrayIO (dMRI)" title="View HBCD file documentation"><code>qsirecon-ModelArrayIO/</code></a></td>
  <td>Aggregates cohort-level HDF5 arrays</td>
  <td><a href="https://www.nmind.org/proceedings/" aria-label="Browse NMIND proceedings for ModelArrayIO (dMRI)" title="Browse NMIND proceedings"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="4">Magnetic Resonance Spectroscopy</td>
</tr>
<tr>
  <td><a href="https://osprey-bids.readthedocs.io/en/latest/">OSPREY-BIDS</a></td>
  <td><a href="../../instruments/mri/mrs/#mrs-processing-derivatives" aria-label="View HBCD file documentation for OSPREY-BIDS" title="View HBCD file documentation"><code>osprey/</code></a></td>
  <td>Processes MRS data using OSPREY-compatible BIDS inputs and outputs</td>
  <td><a href="https://www.nmind.org/proceedings/osprey_bids/" aria-label="View OSPREY-BIDS NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="4">EEG</td>
</tr>
<tr>
  <td><a href="https://docs-hbcd-made.readthedocs.io/en/latest/">HBCD-MADE</a></td>
  <td><a href="../../instruments/eeg/release-data/#hbcd-made-derivatives" aria-label="View HBCD file documentation for HBCD-MADE" title="View HBCD file documentation"><code>made/</code></a></td>
  <td>Processes EEG data using MADE-compatible BIDS inputs and outputs</td>
  <td><a href="https://www.nmind.org/proceedings/hbcdmade/" aria-label="View HBCD-MADE NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="4">Wearable Sensors</td>
</tr>
<tr>
  <td><a href="https://hbcd-motion-postproc.readthedocs.io/en/latest/">HBCD-Motion</a></td>
  <td><a href="../../instruments/sensors/wearsensors/#derivatives" aria-label="View HBCD file documentation for HBCD-Motion" title="View HBCD file documentation"><code>motion/</code></a></td>
  <td>Processes leg movement data from wearable sensor recordings</td>
  <td><a href="https://www.nmind.org/proceedings/hbcd_motion_postproc/" aria-label="View HBCD-Motion NMIND evaluation" title="View NMIND evaluation"><i class="fa-solid fa-shield" aria-hidden="true"></i></a></td>
</tr>

</tbody>
</table>

</div>

## NMIND Checklists

<img src="../images/nmind.png" alt="NMIND" width="70%" height="auto" class="center">

<div class="banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">See NMIND checklist ratings under <a href="https://www.nmind.org/proceedings/">Evaluated Tools</a> (specific links provided in <a href="../#hbcd-pipelines">pipeline table</a>).</span>
</div>
<p></p>

The [NMIND](https://www.nmind.org/about) consortium is dedicated to the advancement of community standards and utilities in support of reproducible neuroimaging research ([Kiar et al. 2023](https://www.nature.com/articles/s41562-023-01647-0)). **All community pipelines used for HBCD data processing must follow HBCD Processing and Derivative Data Standards**, including the completion of NMIND Checklists to adhere to NMIND standards for reproducible neuroimaging and HBCD-specific requirements. 

Peer review of software is performed via submission of the [NMIND Coding Standards Checklist](https://www.nmind.org/standards-checklist/). Software is reviewed against community-driven scientific software standards across three main categories: documentation, infrastructure, and testability. Reviewed tools are assigned badge ratings and published to [Evaluated Tools](https://www.nmind.org/proceedings/). **At a minimum, HBCD pipelines must meet Bronze-level standards.** Pipelines are additionally published with DOIs to support reproducibility.  

After submitting the NMIND Checklist, an issue is automatically generated in the [NMIND Proceedings GitHub repository](https://github.com/nmind/proceedings/issues), where the NMIND team triages to initiate third-party review. Feel free to review and comment on the issue created there for updates.

### NMIND Documentation Checklist 
<input type="checkbox"> Landing page provides a link to documentation and brief description of what program does<br>
<input type="checkbox"> Documentation is up to date with version of software (*see [Obtaining a DOI](#doi) for details*)<br>
<input type="checkbox"> Typical intended usage is described<br>
<input type="checkbox"> An example of its usage is shown<br>
<input type="checkbox"> Document functions intended for users (i.e., public function docstring/help coverage ≥ 10%)<br>
<input type="checkbox"> Reasonable description of required inputs (i.e., "NIfTI of brain mask in MNI" vs. "An image file")<br>
<input type="checkbox"> Description of output(s)<br>
<input type="checkbox"> User installation instructions available<br>
<input type="checkbox"> Dependencies listed *(Largely inapplicable as HBCD pipelines are required to be containerized - [see details](#bids-compliance-bids-apps))*

### NMIND Infrastructure Checklist
<input type="checkbox"> Code is open source<br>
<input type="checkbox"> Package is under version control (*see [Version Control](#version-control) for details*)<br>
<input type="checkbox"> Readme is present<br>
<input type="checkbox"> License is present (*see [Licensing Tips](#licensing) for details*)<br>
<input type="checkbox"> Issues tracking is enabled (i.e., either through GitHub or external site)<br>
<input type="checkbox"> Digital Object Identifier (DOI) points to latest version (*see [How to Obtain a DOI](#doi) for details*)<br>
<input type="checkbox"> All documented installation instructions can be successfully followed<br>

<div id="doi" class="banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-circle-info"></i></span>
<span class="text-with-link">
<span class="text">How to Obtain a DOI</span>
<a class="anchor-link" href="#doi" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
<span class="arrow">▸</span></div>
<div class="collapsible-content">
<p>HBCD software must include a DOI for publication that points to the latest software version. Developers can obtain a DOI by self-publishing on <a href="https://cdnis-brain.readthedocs.io/zenodo/">Zenodo</a>, which generates a top-level DOI as well as a per-version DOI attached to each release. Note that this should be done even if you have published a scientific article about your tool so that the software version can be properly cited.</p>
<p>A Zenodo DOI badge should also be included on the landing page of your pipeline documentation website. This will additionally fulfill the Documentation checklist item <em>&quot;Documentation is up to date with version of software</em>.&quot; See an example of Zenodo badge and associated Zenodo publication on the <a href="https://nibabies.readthedocs.io/en/latest/">Nibabies webpage</a>.</p>
</div>

<div id="licensing" class="banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-circle-info"></i></span>
<span class="text-with-link">
<span class="text">Licensing Tips</span>
<a class="anchor-link" href="#licensing" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
<span class="arrow">▸</span></div>
<div class="collapsible-content">
<p>HBCD processing pipelines are largely open source. Common permissive license options include <a href="https://github.com/DCAN-Labs/hbcd-docs/community/license/new?branch=main&amp;filename=LICENSE&amp;template=apache-2.0">Apache-2.0 License 2.0</a>, <a href="https://github.com/DCAN-Labs/hbcd-docs/community/license/new?branch=main&amp;filename=LICENSE&amp;template=mit">MIT License</a>, and the <a href="https://github.com/DCAN-Labs/hbcd-docs/community/license/new?branch=main&amp;filename=LICENSE&amp;template=bsd-3-clause">BSD-3-Clause license</a>. Visit GitHub&#39;s documentation on <a href="https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository">Licensing a Repository</a> and <a href="https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository">Adding a License To a Repository</a> for more information. </p>
</div>

<div id="version-control" class="banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-circle-info"></i></span>
<span class="text-with-link">
<span class="text">Version Control</span>
<a class="anchor-link" href="#version-control" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
<span class="arrow">▸</span></div>
<div class="collapsible-content">
<p>Version control is maintained via GitHub. Tag releases for significant or cumulative updates, and include a changelog summarizing changes from the previous version. Establish a standard release cycle and criteria for special releases (e.g., urgent bug fixes). Pipeline documentation should define long-term support versions, deprecation plans, and timelines.</p>
</div>

### NMIND Testing Ability Checklist
<input type="checkbox"> Provide/generate/point to test data (*Only applicable if non-HBCD data can be shared as a representative data sample*)<br>
<input type="checkbox"> Provide instructions for users to run tests and evaluate for correct behavior 

## HBCD-Specific Requirements

Additional requirements include compliance with HBCD Study derivative data standards and Brain Imaging Data Structure (BIDS). Pipelines must also be implemented as BIDS Apps ([Gorgolewski et al.,2017](https://doi.org/10.1371/journal.pcbi.1005209)), ensuring containerized, standardized processing.   

### Derivative Data Standards
All software standards also apply to derivative data standards for HBCD Study data. In practice, this means software must comply with the data standards in order for its processed outputs to be eligible for inclusion in a release. Therefore, in addition to the requirements outlined below, all pipelines must produce derivatives compatible with current release data.

### BIDS Compliance & BIDS Apps
BIDS is a community-driven standard for organizing neuroimaging and behavioral data to make datasets structured, shareable, and reproducible. BIDS Apps are containerized applications that intake and output BIDS-formatted data. 

Per the [BIDS-App guidelines](https://bids-apps.neuroimaging.io/), all HBCD pipelines must be containerized to run on any system supporting [Docker](https://docs.docker.com/get-started/get-docker/) or [Apptainer](https://apptainer.org/docs/user/main/quick_start.html) (Singularity). Containerization ensures that all software dependencies are included to guarantee consistent processing environments across systems. This is not only critical for reproducibility, but also makes data processing more straightforward and foolproof.

### Pipeline Documentation Websites
HBCD pipelines must maintain living documentation via a dedicated website. This provides a current, easily navigable resource beyond static publications or a GitHub README. We recommend hosting documentation with [Read the Docs](https://docs.readthedocs.com/platform/stable/) or [GitHub Pages](https://pages.github.com/). See the [fMRIPrep documentation](https://fmriprep.org/en/stable/) for guidance on organization of level of detail.



