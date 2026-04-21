# Processing & Derivative Data Standards

<img src="../nmind.png" alt="NMIND" width="70%" height="auto" class="center">

HBCD pipeline developers, Workgroups, and community contributors who wish to integrate tools into the HBCD release environment are expected to follow all guidelines described below, including adherence to [NMIND](https://www.nmind.org/about) standards for reproducible neuroimaging ([Kiar et al. 2023](https://www.nature.com/articles/s41562-023-01647-0)) as well as additional HBCD-specific requirements.

Software are peer-reviewed via submission of the [NMIND Coding Standards Checklist](https://www.nmind.org/standards-checklist/), which evaluates code against community-driven scientific software standards across three main categories (documentation, infrastructure, and testability). The software is reviewed by a third party, who reviews the accuracy of the submitted checklist and provides other suggested updates, reported to the developers via the [proceedings repository](https://github.com/nmind/proceedings). Reviewed tools are assigned badge ratings and published to [Evaluated Tools](https://www.nmind.org/proceedings/). At a minimum, tools must meet Bronze-level standards. 

## Derivative Data Standards
<span class="badge-hbcd"><i class="fa-solid fa-triangle-exclamation"></i> HBCD-Specific Requirement</span>

All software standards also apply to derivative data standards for HBCD Study data. In practice, this means software must comply with the data standards in order for its processed outputs to be eligible for inclusion in a release. Therefore, in addition to the requirements outlined below, all pipelines must be containerized following [BIDS-App guidelines](https://bids-apps.neuroimaging.io/) and produce derivatives compatible with current release data.

## Documentation Standards
#### NMIND Documentation Checklist (Bronze Badge)
<input type="checkbox"> Landing page provides a link to documentation and brief description of what program does<br>
<input type="checkbox"> Documentation is up to date with version of software (*see [Obtaining a DOI](#obtaining-a-doi) for details*)<br>
<input type="checkbox"> Typical intended usage is described<br>
<input type="checkbox"> An example of its usage is shown<br>
<input type="checkbox"> Document functions intended for users (i.e., public function docstring/help coverage ≥ 10%)<br>
<input type="checkbox"> Reasonable description of required inputs (i.e., "NIfTI of brain mask in MNI" vs. "An image file")<br>
<input type="checkbox"> Description of output(s)<br>
<input type="checkbox"> User installation instructions available<br>
<input type="checkbox"> Dependencies listed *(Note: this is largely inapplicable to HBCD pipelines as they are required to be containerized - [see details](#derivative-data-standards))*

#### Dedicated Pipeline Documentation Website  
<span class="badge-hbcd"><i class="fa-solid fa-triangle-exclamation"></i> HBCD-specific requirement</span>

In addition to the checklist above, HBCD pipelines must maintain living documentation via a dedicated website. This provides a current, easily navigable resource beyond static publications or a GitHub README. We recommend hosting documentation with [Read the Docs](https://docs.readthedocs.com/platform/stable/) or [GitHub Pages](https://pages.github.com/). See the [fMRIPrep documentation](https://fmriprep.org/en/stable/) for guidance on organization of level of detail. Include clear guidance on how to cite the documentation (<a href="https://fmriprep.org/en/stable/#citation">example</a>).

## Infrastructure Standards
#### NMIND Infrastructure Checklist (Bronze Badge)
<input type="checkbox"> Code is open source<br>
<input type="checkbox"> Package is under version control (*see [Version Control](#version-control) for details*)<br>
<input type="checkbox"> Readme is present<br>
<input type="checkbox"> License is present (*see [Licensing Tips](#licensing) for details*)<br>
<input type="checkbox"> Issues tracking is enabled (i.e., either through GitHub or external site)<br>
<input type="checkbox"> Digital Object Identifier (DOI) points to latest version (*see [How to Obtain a DOI](#doi) for details*)<br>
<input type="checkbox"> All documented installation instructions can be successfully followed<br>

<div id="doi" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-circle-info"></i></span>
<span class="text-with-link">
<span class="text">How to Obtain a DOI</span>
<a class="anchor-link" href="#doi" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
<span class="arrow">▸</span></div>
<div class="collapsible-content">
<p>HBCD software must include a DOI for publication that points to the latest software version. Developers can obtain a DOI by self-publishing on <a href="https://cdnis-brain.readthedocs.io/zenodo/">Zenodo</a>, which generates a top-level DOI as well as a per-version DOI attached to each release. Note that this should be done even if you have published a scientific article about your tool so that the software version can be properly cited.</p>
<p>A Zenodo DOI badge should also be included on the landing page of your pipeline documentation website. This will additionally fulfill the Documentation checklist item <em>&quot;Documentation is up to date with version of software</em>.&quot; See an example of Zenodo badge and associated Zenodo publication on the <a href="https://nibabies.readthedocs.io/en/latest/">Nibabies webpage</a>.</p>
</div>

<div id="licensing" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-circle-info"></i></span>
<span class="text-with-link">
<span class="text">Licensing Tips</span>
<a class="anchor-link" href="#licensing" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
<span class="arrow">▸</span></div>
<div class="collapsible-content">
<p>HBCD processing pipelines are largely open source. Common permissive license options include <a href="https://github.com/DCAN-Labs/hbcd-docs/community/license/new?branch=main&amp;filename=LICENSE&amp;template=apache-2.0">Apache-2.0 License 2.0</a>, <a href="https://github.com/DCAN-Labs/hbcd-docs/community/license/new?branch=main&amp;filename=LICENSE&amp;template=mit">MIT License</a>, and the <a href="https://github.com/DCAN-Labs/hbcd-docs/community/license/new?branch=main&amp;filename=LICENSE&amp;template=bsd-3-clause">BSD-3-Clause license</a>. Visit GitHub&#39;s documentation on <a href="https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository">Licensing a Repository</a> and <a href="https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository">Adding a License To a Repository</a> for more information. </p>
</div>

<div id="version-control" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-circle-info"></i></span>
<span class="text-with-link">
<span class="text">Version Control</span>
<a class="anchor-link" href="#version-control" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
<span class="arrow">▸</span></div>
<div class="collapsible-content">
<p>Version control is maintained via GitHub. Tag releases for significant or cumulative updates, and include a changelog summarizing changes from the previous version. Establish a standard release cycle and criteria for special releases (e.g., urgent bug fixes). Pipeline documentation should define long-term support versions, deprecation plans, and timelines.</p>
</div>

## Testing Ability Standards

#### NMIND Testing Checklist (Bronze Badge)
<input type="checkbox"> Provide/generate/point to test data (*Only applicable if non-HBCD data can be shared as a representative data sample*)<br>
<input type="checkbox"> Provide instructions for users to run tests and evaluate for correct behavior

## Current HBCD Pipeline & Utility Evaluations
A full list of tools evaluated through the [NMIND Coding Standards Checklist](https://www.nmind.org/standards-checklist/) can be found on their webpage under [Evaluated Tools](https://www.nmind.org/proceedings/). Below are the badge rating details for pipelines integrated into the HBCD release environment:

- [MRIQC](https://www.nmind.org/proceedings/mriqc/)
- [BME-X](https://www.nmind.org/proceedings/bmex/)
- [BIBSNet](https://www.nmind.org/proceedings/bibsnet/)
- [infant-fMRIPrep](https://www.nmind.org/proceedings/nibabies/) (as well as base software [fMRIPrep](https://www.nmind.org/proceedings/fmriprep/))
- [XCP-D](https://www.nmind.org/proceedings/xcpd/)
- [QSIPrep](https://www.nmind.org/proceedings/qsiprep/) 
- [QSIRecon](https://www.nmind.org/proceedings/qsirecon/)
- [qMRI Postproc](https://www.nmind.org/proceedings/hbcd_qmri_postproc/)
- [HBCD-MADE](https://www.nmind.org/proceedings/hbcdmade/)
- [OSPREY-BIDS](https://www.nmind.org/proceedings/osprey_bids/) (as well as base software [OSPREY](https://www.nmind.org/proceedings/osprey/))
- [HBCD-Motion](https://www.nmind.org/proceedings/hbcd_motion_postproc/)





<!-- <div id="study-design-logic-child-centric-data-structure" class="notification-banner static-banner">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Application of Software Standards to Derivate Data</span>
  <a class="anchor-link" href="#study-design-logic-child-centric-data-structure" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
</div>
<div class="notification-static-content">
<p>Note that all software standards also apply to derivative data standards for HBCD Study data. In practice, this means software must comply with the data standards in order for its outputs to be eligible for inclusion in a release.</p>
</div>
<p></p> -->