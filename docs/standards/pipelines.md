<style>
.compact-table-no-vertical-lines th:nth-child(4),
.compact-table-no-vertical-lines th:nth-child(5),
.compact-table-no-vertical-lines td:nth-child(4),
.compact-table-no-vertical-lines td:nth-child(5) {
    text-align: center;
}
</style>

# Processing & Derivative Data Standards

<img src="../images/nmind.png" alt="NMIND" width="70%" height="auto" class="center">

**All community pipelines used for HBCD data processing must follow HBCD Processing and Derivative Data Standards**, including the completion of NMIND Checklists to adhere to NMIND standards for reproducible neuroimaging and HBCD-specific requirements.


## HBCD Processing Pipelines

The HBCD processing pipelines are a collection of modular tools used to process HBCD Study data, including magnetic resonance imaging/spectroscopy (MRI/MRS), electroencephalography (EEG), and biosensor data. Pipeline outputs are provided within the data release as file-based derivatives. The table below includes links to the <a href="https://www.nmind.org/proceedings/">NMIND Evaluated Tools</a> page for each pipeline.

**Full technical details on how each pipeline was executed and configured is available in the [HBCD Processing](https://hbcd-cbrain-processing.readthedocs.io/release_2.0/) documentation,** with pipeline-specific parameters detailed under **Tool Names** (e.g., 'File Selection For Processing' and 'Quality Control Selection Information').

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
<table class="compact-table-no-vertical-lines" with="100%">
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
  <a href="../../instruments/mri/smri/#mriqc"><i class="fa-solid fa-folder-tree header icon"></i>
  </a>
</td>
  <td><a href="https://www.nmind.org/proceedings/mriqc/"><i class="fa fa-shield"></i></a></td>
</tr>
<tr>
  <td><a href="https://brain-mri-enhancement.readthedocs.io/">BME-X</a></td>
  <td><code>bme_x/</code></td>
  <td>Structural pipeline for T1w/T2w image quality enhancement</td>
  <td><a href="../../instruments/mri/smri/#mriqc">
  <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/bmex/"><i class="fa fa-shield"></i></a></td>
</tr>
<tr>
  <td><a href="https://bibsnet.readthedocs.io/en/latest/">BIBSNet</a></td>
  <td><code>bibsnet/</code></td>
  <td>Deep learning model for brain segmentation</td>
  <td><a href="../../instruments/mri/smri/#bibsnet">
    <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/bibsnet/"><i class="fa fa-shield"></i></a></td>
</tr>
<tr>
  <td><a href="https://nibabies.readthedocs.io/en/latest/">Infant-fMRIPrep</a></td>
  <td><code>nibabies/</code></td>
  <td>Structural and functional MRI preprocessing pipeline</td>
  <td><a href="../../instruments/mri/fmri/#nibabies-derivs">
    <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/nibabies/">
  <i class="fa fa-shield"></i></a></td>
</tr>
<tr>
  <td><a href="https://doi.org/10.1016/j.neuroimage.2020.116946">FreeSurfer</a></td>
  <td><code>freesurfer/</code></td>
  <td>Infant FreeSurfer surface reconstruction workflow run in fMRIPrep</td>
  <td>
    <a href="../../instruments/mri/smri/#fs">
    <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td>—</td>
</tr>
<tr>
  <td><a href="https://doi.org/10.1038/s41598-020-61326-2">M-CRIB-S</a></td>
  <td><code>mcribs/</code></td>
  <td>Neonatal surface reconstruction workflow run in fMRIPrep</td>
  <td>
    <a href="../../instruments/mri/smri/#mcribs">
    <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td>—</td>
</tr>
<tr>
  <td><a href="https://xcp-d.readthedocs.io/en/latest/">XCP-D</a></td>
  <td><code>xcp_d/</code></td>
  <td>Functional MRI post-processing and noise regression pipeline</td>
  <td><a href="../../instruments/mri/fmri/#xcpd-derivs">
      <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/xcpd/">
  <i class="fa fa-shield"></i></a></td>
</tr>

<tr>
  <td><a href="https://pennlinc.github.io/ModelArray/">ModelArray</a></td>
  <td><code>modelarray/</code></td>
  <td>Aggregates cohort-level HDF5 arrays for efficient large-scale analyses</td>
  <td><a href="../../../instruments/mri/fmri/#modelarrayio">
      <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/">
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
   <a href="../../instruments/mri/qmri/#processing-derivatives">
    <i class="fa-solid fa-folder-tree header icon"></i></a></td>
    <td>--</td>
</tr>
<tr>
  <td><a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html">qMRI Postproc</a></td>
  <td><code>qmri_postproc/</code></td>
  <td>Minimal post-processing of SyMRI images</td>
  <td><a href="../../instruments/mri/qmri/#processing-derivatives">
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
  <td><a href="../../instruments/mri/dmri/#qsiprep">
  <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/qsiprep/"><i class="fa fa-shield"></i></a></td>
</tr>
<tr>
  <td><a href="https://qsirecon.readthedocs.io/en/latest/">QSIRecon</a></td>
  <td><code>qsirecon-*/</code></td>
  <td>dMRI post-processing reconstruction workflows</td>
  <td><a href="../../instruments/mri/dmri/#qsirecon">
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
  <td><a href="../../instruments/mri/mrs/#derivatives"><i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/osprey_bids/"><i class="fa fa-shield"></i></a></td>
</tr>

<tr class="table-group-row">
  <td colspan="5">EEG</td>
</tr>
<tr>
  <td><a href="https://docs-hbcd-made.readthedocs.io/en/latest/">HBCD-MADE</a></td>
  <td><code>made/</code></td>
  <td>EEG MADE pipeline adapted for HBCD</td>
  <td><a href="../../instruments/eeg/hbcd-made/#hbcd-made-derivatives">
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
  <td><a href="../../instruments/sensors/wearsensors/#derivatives">
  <i class="fa-solid fa-folder-tree header icon"></i></a></td>
  <td><a href="https://www.nmind.org/proceedings/hbcd_motion_postproc/"><i class="fa fa-shield"></i></a></td>
</tr>
</tbody>
</table>

</div>



## NMIND Checklists

<div class="banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">See NMIND checklist ratings under <a href="https://www.nmind.org/proceedings/">Evaluated Tools</a> (specific links provided in <a href="../#hbcd-pipelines">pipeline table</a>).</span>
</div>
<p></p>

The [NMIND](https://www.nmind.org/about) consortium is dedicated to the advancement of community standards and utilities in support of reproducible neuroimaging research ([Kiar et al. 2023](https://www.nature.com/articles/s41562-023-01647-0)). For HBCD, peer review of software is performed via submission of the [NMIND Coding Standards Checklist](https://www.nmind.org/standards-checklist/). Software is reviewed against community-driven scientific software standards across three main categories: documentation, infrastructure, and testability. Reviewed tools are assigned badge ratings and published to [Evaluated Tools](https://www.nmind.org/proceedings/). **At a minimum, HBCD pipelines must meet Bronze-level standards.** Pipelines are additionally published with DOIs to support reproducibility.  

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



