<div id="pipelines" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-diagram-project"></i></span>
  <span class="text-with-link">
    <span class="text">HBCD Processing Pipelines & Relevant Links to Documentation</span>
    <a class="anchor-link" href="#pipelines" title="Copy link" aria-label="Link to this section">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow rotate">▸</span>
</div>

<div class="collapsible-content open">

  <div class="table-legend">
    <span class="legend-item">
      <i class="fa-solid fa-folder-tree legend-icon"></i>
      HBCD documentation &amp; file tree
    </span>
    <span class="legend-item">
      <i class="fa-solid fa-shield legend-icon"></i>
      NMIND evaluation
    </span>
  </div>

  <table class="compact-table-no-vertical-lines">
    <thead>
      <tr>
        <th>Modality</th>
        <th>Pipeline</th>
        <th>Derivative Folder</th>
        <th>Description</th>
        <th>Links</th>
      </tr>
    </thead>
    <tbody>
  <!-- MRI QC pipelines-->
      <tr>
        <td>Quality Control</td>
        <td><a href="https://mriqc.readthedocs.io/en/latest/">MRIQC</a></td>
        <td><code>mriqc/</code></td>
        <td>Extracts image-quality metrics from raw MRI data.</td>
        <td>
          <a href="../../instruments/mri/smri/#qc-pipelines-mriqc-bme-x"
             title="HBCD documentation and file tree for MRIQC"
             aria-label="HBCD documentation and file tree for MRIQC">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <a href="https://www.nmind.org/proceedings/mriqc/"
             title="NMIND evaluation of MRIQC"
             aria-label="NMIND evaluation of MRIQC">
            <i class="fa-solid fa-shield"></i>
          </a>
        </td>
      </tr>
      <!-- Structural MRI -->
      <tr>
        <td rowspan="3">Structural MRI</td>
        <td><a href="https://brain-mri-enhancement.readthedocs.io/">BME-X</a></td>
        <td><code>bme-x/</code></td>
        <td>Enhances brain MRI image quality.</td>
        <td>
          <a href="../../instruments/mri/smri/#qc-pipelines-mriqc-bme-x"
             title="HBCD documentation and file tree for BME-X"
             aria-label="HBCD documentation and file tree for BME-X">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <a href="https://www.nmind.org/proceedings/bmex/"
             title="NMIND evaluation of BME-X"
             aria-label="NMIND evaluation of BME-X">
            <i class="fa-solid fa-shield"></i>
          </a>
        </td>
      </tr>
      <tr>
        <td><a href="https://bibsnet.readthedocs.io/en/latest/">BIBSNet</a></td>
        <td><code>bibsnet/</code></td>
        <td>Performs automated brain extraction and tissue segmentation for infant MRI.</td>
        <td>
          <a href="../../instruments/mri/smri/#bibsnet"
             title="HBCD documentation and file tree for BIBSNet"
             aria-label="HBCD documentation and file tree for BIBSNet">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <a href="https://www.nmind.org/proceedings/bibsnet/"
             title="NMIND evaluation of BIBSNet"
             aria-label="NMIND evaluation of BIBSNet">
            <i class="fa-solid fa-shield"></i>
          </a>
        </td>
      </tr>
      <tr>
        <td><a href="https://doi.org/10.1016/j.neuroimage.2020.116946">FreeSurfer</a></td>
        <td><code>freesurfer/</code></td>
        <td>Provides structural MRI processing, including cortical reconstruction, segmentation, and anatomical measurements.</td>
        <td>
          <a href="../../instruments/mri/smri/#fs"
             title="HBCD documentation and file tree for FreeSurfer"
             aria-label="HBCD documentation and file tree for FreeSurfer">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <span aria-label="No NMIND evaluation listed" title="No NMIND evaluation listed">—</span>
        </td>
      </tr>
      <tr>
        <td><a href="https://doi.org/10.1038/s41598-020-61326-2">M-CRIB-S</a></td>
        <td><code>mcribs/</code></td>
        <td>Provides neonatal brain segmentation and cortical surface reconstruction.</td>
        <td>
          <a href="../../instruments/mri/smri/#mcribs"
             title="HBCD documentation and file tree for M-CRIB-S"
             aria-label="HBCD documentation and file tree for M-CRIB-S">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <span aria-label="No NMIND evaluation listed" title="No NMIND evaluation listed">—</span>
        </td>
      </tr>
      <!-- Functional MRI -->
      <tr>
        <td rowspan="3">Structural/Functional MRI</td>
        <td><a href="https://nibabies.readthedocs.io/en/latest/">Infant-fMRIPrep (NiBabies)</a></td>
        <td><code>nibabies/</code></td>
        <td>Preprocesses infant structural and functional MRI data using an age-appropriate workflow.</td>
        <td>
          <a href="../../instruments/mri/fmri/#nibabies-derivs"
             title="HBCD documentation and file tree for Infant-fMRIPrep"
             aria-label="HBCD documentation and file tree for Infant-fMRIPrep">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <a href="https://www.nmind.org/proceedings/nibabies/"
             title="NMIND evaluation of Infant-fMRIPrep"
             aria-label="NMIND evaluation of Infant-fMRIPrep">
            <i class="fa-solid fa-shield"></i>
          </a>
        </td>
      </tr>
      <tr>
        <td><a href="https://xcp-d.readthedocs.io/en/latest/">XCP-D</a></td>
        <td><code>xcp_d/</code></td>
        <td>Performs postprocessing of functional MRI data, including denoising and generation of functional connectivity measures.</td>
        <td>
          <a href="../../instruments/mri/fmri/#xcpd-derivs"
             title="HBCD documentation and file tree for XCP-D"
             aria-label="HBCD documentation and file tree for XCP-D">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <a href="https://www.nmind.org/proceedings/xcpd/"
             title="NMIND evaluation of XCP-D"
             aria-label="NMIND evaluation of XCP-D">
            <i class="fa-solid fa-shield"></i>
          </a>
        </td>
      </tr>
      <tr>
        <td><a href="https://pennlinc.github.io/ModelArray/">ModelArrayIO</a></td>
        <td><code>modelarrayio/</code></td>
        <td>Converts imaging-derived data into ModelArray format for efficient storage and downstream analysis.</td>
        <td>
          <a href="../../instruments/mri/fmri/#modelarrayio"
             title="HBCD documentation and file tree for ModelArrayIO"
             aria-label="HBCD documentation and file tree for ModelArrayIO">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <a href="https://www.nmind.org/proceedings/"
             title="NMIND proceedings"
             aria-label="NMIND proceedings">
            <i class="fa-solid fa-shield"></i>
          </a>
        </td>
      </tr>
      <!-- Quantitative MRI -->
      <tr>
        <td rowspan="2">Quantitative MRI</td>
        <td><a href="https://syntheticmr.com/products/symri-neuro/">SyMRI</a></td>
        <td><code>symri/</code></td>
        <td>Estimates quantitative tissue parameters and generates synthetic MRI contrasts from multi-contrast MRI acquisitions.</td>
        <td>
          <a href="../../instruments/mri/qmri/#processing-derivatives"
             title="HBCD documentation and file tree for SyMRI"
             aria-label="HBCD documentation and file tree for SyMRI">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <span aria-label="No NMIND evaluation listed" title="No NMIND evaluation listed">—</span>
        </td>
      </tr>
      <tr>
        <td><a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/">qMRI Postproc</a></td>
        <td><code>qmri_postproc/</code></td>
        <td>Processes and organizes quantitative MRI outputs for downstream analysis.</td>
        <td>
          <a href="../../instruments/mri/qmri/#processing-derivatives"
             title="HBCD documentation and file tree for qMRI Postproc"
             aria-label="HBCD documentation and file tree for qMRI Postproc">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <a href="https://www.nmind.org/proceedings/hbcd_qmri_postproc/"
             title="NMIND evaluation of qMRI Postproc"
             aria-label="NMIND evaluation of qMRI Postproc">
            <i class="fa-solid fa-shield"></i>
          </a>
        </td>
      </tr>
      <!-- Diffusion MRI -->
      <tr>
        <td rowspan="3">Diffusion MRI</td>
        <td><a href="https://qsiprep.readthedocs.io/en/latest/">QSIPrep</a></td>
        <td><code>qsiprep/</code></td>
        <td>Preprocesses diffusion MRI data, including motion and distortion correction and preparation for reconstruction.</td>
        <td>
          <a href="../../instruments/mri/dmri/#qsiprep"
             title="HBCD documentation and file tree for QSIPrep"
             aria-label="HBCD documentation and file tree for QSIPrep">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <a href="https://www.nmind.org/proceedings/qsiprep/"
             title="NMIND evaluation of QSIPrep"
             aria-label="NMIND evaluation of QSIPrep">
            <i class="fa-solid fa-shield"></i>
          </a>
        </td>
      </tr>
      <tr>
        <td><a href="https://qsirecon.readthedocs.io/en/latest/">QSIRecon</a></td>
        <td><code>qsirecon/</code></td>
        <td>Reconstructs diffusion MRI data and generates microstructural and tractography-related outputs.</td>
        <td>
          <a href="../../instruments/mri/dmri/#qsirecon"
             title="HBCD documentation and file tree for QSIRecon"
             aria-label="HBCD documentation and file tree for QSIRecon">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <a href="https://www.nmind.org/proceedings/qsirecon/"
             title="NMIND evaluation of QSIRecon"
             aria-label="NMIND evaluation of QSIRecon">
            <i class="fa-solid fa-shield"></i>
          </a>
        </td>
      </tr>
      <tr>
        <td><a href="https://pennlinc.github.io/ModelArray/">ModelArrayIO</a></td>
        <td><code>modelarrayio/</code></td>
        <td>Converts diffusion MRI-derived data into ModelArray format for efficient storage and downstream analysis.</td>
        <td>
          <a href="../../instruments/mri/dmri/#modelarrayio"
             title="HBCD documentation and file tree for ModelArrayIO"
             aria-label="HBCD documentation and file tree for ModelArrayIO">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <a href="https://www.nmind.org/proceedings/"
             title="NMIND proceedings"
             aria-label="NMIND proceedings">
            <i class="fa-solid fa-shield"></i>
          </a>
        </td>
      </tr>

      <!-- Magnetic Resonance Spectroscopy -->
      <tr>
        <td>Magnetic Resonance Spectroscopy</td>
        <td><a href="https://osprey-bids.readthedocs.io/en/latest/">OSPREY-BIDS</a></td>
        <td><code>osprey/</code></td>
        <td>Processes magnetic resonance spectroscopy data using OSPREY-compatible BIDS inputs and outputs.</td>
        <td>
          <a href="../../instruments/mri/mrs/#derivatives"
             title="HBCD documentation and file tree for OSPREY-BIDS"
             aria-label="HBCD documentation and file tree for OSPREY-BIDS">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <a href="https://www.nmind.org/proceedings/osprey_bids/"
             title="NMIND evaluation of OSPREY-BIDS"
             aria-label="NMIND evaluation of OSPREY-BIDS">
            <i class="fa-solid fa-shield"></i>
          </a>
        </td>
      </tr>

      <!-- EEG -->
      <tr>
        <td>EEG</td>
        <td><a href="https://docs-hbcd-made.readthedocs.io/en/latest/">HBCD-MADE</a></td>
        <td><code>hbcd-made/</code></td>
        <td>Processes EEG data through the HBCD-MADE workflow, including preprocessing and quality-control outputs.</td>
        <td>
          <a href="../../instruments/eeg/hbcd-made/#hbcd-made-derivatives"
             title="HBCD documentation and file tree for HBCD-MADE"
             aria-label="HBCD documentation and file tree for HBCD-MADE">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <a href="https://www.nmind.org/proceedings/hbcdmade/"
             title="NMIND evaluation of HBCD-MADE"
             aria-label="NMIND evaluation of HBCD-MADE">
            <i class="fa-solid fa-shield"></i>
          </a>
        </td>
      </tr>

      <!-- Wearable Sensors -->
      <tr>
        <td>Wearable Sensors</td>
        <td><a href="https://hbcd-motion-postproc.readthedocs.io/en/latest/">HBCD-Motion</a></td>
        <td><code>hbcd-motion/</code></td>
        <td>Processes wearable-sensor motion data and generates derived measures for downstream analysis.</td>
        <td>
          <a href="../../instruments/sensors/wearsensors/#derivatives"
             title="HBCD documentation and file tree for HBCD-Motion"
             aria-label="HBCD documentation and file tree for HBCD-Motion">
            <i class="fa-solid fa-folder-tree"></i>
          </a>
          <a href="https://www.nmind.org/proceedings/hbcd_motion_postproc/"
             title="NMIND evaluation of HBCD-Motion"
             aria-label="NMIND evaluation of HBCD-Motion">
            <i class="fa-solid fa-shield"></i>
          </a>
        </td>
      </tr>
    </tbody>
  </table>
</div>












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

<div class="table-legend">
  <span class="legend-item">
    <i class="fa-solid fa-link legend-icon"></i>
    Official documentation
  </span>
  <span class="legend-item">
    <i class="fa-solid fa-folder-tree legend-icon"></i>
   HBCD Docs documentation & file tree
  </span>
  <span class="legend-item">
    <i class="fa-solid fa-shield legend-icon"></i>
   NMIND Evaluation
  </span>
</div>
<table class="compact-table-no-vertical-lines" width="100%">
<thead>
<tr>
  <th>Modality</th>
  <th>Pipeline</th>
  <th>Derivative Folder</th>
  <th>Description</th>
  <th>Documentation Links</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Structural & Functional MRI</td>
  <td><a href="https://mriqc.readthedocs.io/en/latest/">MRIQC</a></td>
  <td><code>mriqc/</code></td>
  <td>Extracts image quality metrics from raw MRI data</td>
  <td>
    <a href="https://www.nmind.org/proceedings/mriqc/" 
      label="Official pipeline documentation for MRIQC" 
      title="Official pipeline documentation for MRIQC">
      <i class="fa-solid fa-link"></i></a>
     <a href="../../instruments/mri/smri/#qc-pipelines-mriqc-bme-x"
     label="View HBCD documentation for MRIQC"
     title="View HBCD documentation for HBCD">
     <i class="fa-solid fa-folder-tree"></i></a>
    <a href="../../instruments/mri/smri/#qc-pipelines-mriqc-bme-x"
    label="NMIND Evaluation" 
    title="NMIND Evaluation">
    <i class="fa-solid fa-shield"></i></a>
  </td>
</tr>
</tbody>
</table>

</div>