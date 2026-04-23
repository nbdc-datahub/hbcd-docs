# HBCD Processing Pipelines

## HBCD Pipelines

The HBCD processing pipelines are a collection of modular tools used to process HBCD Study data, including magnetic resonance imaging/spectroscopy (**MRI/MRS**), electroencephalography (**EEG**), and **biosensor data**. See [Derivatives](../../datacuration/file-based-data.md#links-to-pipeline-derivatives) documentation for details on processed outputs.


The table below also includes links to the <a href="https://www.nmind.org/proceedings/"><i class="fa fa-shield"></i> NMIND Evaluated Tools</a> page for each pipeline - see <a href="standards/">Processing & Derivative Standards</a> for details.


<table class="compact-table-no-vertical-lines">
<thead><tr><th>Processing Pipeline</th><th>NMIND</th><th>Pipeline Description</th></tr></thead>
<tbody>
<!-- s/f/MRI -->
<tr><td colspan="3" style="font-weight: bold; padding-top: 10px;">Structural & Functional MRI</td></tr>
<tr>
<td><a href="https://mriqc.readthedocs.io/en/latest/">MRIQC</a></td>
<td style="text-align: center;"><a href="https://www.nmind.org/proceedings/mriqc/"><i class="fa fa-shield"></i></a></td>
<td>Extracts image quality metrics from structural and functional MRI data</td>
</tr>
<tr>
<td><a href="https://brain-mri-enhancement.readthedocs.io/">BME-X</a></td>
<td style="text-align: center;"><a href="https://www.nmind.org/proceedings/bmex/"><i class="fa fa-shield"></i></a></td>
<td>Structural pipeline for T1w/T2w image quality enhancement</td>
</tr>
<tr>
<td><a href="https://bibsnet.readthedocs.io/en/latest/">BIBSNet</a></td>
<td style="text-align: center;"><a href="https://www.nmind.org/proceedings/bibsnet/"><i class="fa fa-shield"></i></a></td>
<td>Deep learning model for brain segmentation</td>
</tr>
<tr>
<td><a href="https://nibabies.readthedocs.io/en/latest/">infant-fMRIPrep</a></td>
<td style="text-align: center;"><a href="https://www.nmind.org/proceedings/nibabies/"><i class="fa fa-shield"></i></a></td>
<td>Structural and functional MRI preprocessing pipeline</td>
</tr>
<tr>
<td><a href="https://xcp-d.readthedocs.io/en/latest/">XCP-D</a></td>
<td style="text-align: center;"><a href="https://www.nmind.org/proceedings/xcpd/"><i class="fa fa-shield"></i></a></td>
<td>Functional MRI post-processing and noise regression pipeline</td>
</tr>
<!-- qMRI -->
<tr><td colspan="3" style="font-weight: bold; padding-top: 10px;">Quantitative MRI</td></tr>
<tr>
<td><a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html">qMRI Postproc</a></td>
<td style="text-align: center;"><a href="https://www.nmind.org/proceedings/hbcd_qmri_postproc/"><i class="fa fa-shield"></i></a></td>
<td>Minimal post-processing for SyMRI synthetic images</td>
</tr>
<!-- dMRI -->
<tr><td colspan="3" style="font-weight: bold; padding-top: 10px;">Diffusion MRI</td></tr>
<tr>
<td><a href="https://qsiprep.readthedocs.io/en/latest/">QSIPrep</a></td>
<td style="text-align: center;"><a href="https://www.nmind.org/proceedings/qsiprep/"><i class="fa fa-shield"></i></a></td>
<td>dMRI data preprocessing pipeline</td>
</tr>
<tr>
<td><a href="https://qsirecon.readthedocs.io/en/latest/">QSIRecon</a></td>
<td style="text-align: center;"><a href="https://www.nmind.org/proceedings/qsirecon/"><i class="fa fa-shield"></i></a></td>
<td>dMRI post-processing workflows for reconstruction of preprocessed q-space images </td>
</tr>
<!-- MRS -->
<tr>
  <td colspan="3" style="font-weight: bold; padding-top: 10px;">MRS</td>
</tr>
<tr>
<td><a href="https://osprey-bids.readthedocs.io/en/latest/index.html">OSPREY-BIDS</a></td>
<td style="text-align: center;"><a href="https://www.nmind.org/proceedings/osprey_bids/"><i class="fa fa-shield"></i></a></td>
<td>MRS data processing pipeline</td>
</tr>
<!-- EEG -->
<tr>
  <td colspan="3" style="font-weight: bold; padding-top: 10px;">EEG</td>
</tr>
<tr>
<td><a href="https://docs-hbcd-made.readthedocs.io/en/latest/">HBCD-MADE</a></td>
<td style="text-align: center;"><a href="https://www.nmind.org/proceedings/hbcdmade/"><i class="fa fa-shield"></i></a></td>
<td>Maryland Analysis of Developmental EEG (MADE) pipeline adapted for HBCD</td>
</tr>
<!-- Biosensors -->
<tr>
  <td colspan="3" style="font-weight: bold; padding-top: 10px;">Biosensors</td>
</tr>
<tr>
<td><a href="https://hbcd-motion-postproc.readthedocs.io/en/latest/">HBCD-Motion</a></td>
<td style="text-align: center;"><a href="https://www.nmind.org/proceedings/hbcd_motion_postproc/"><i class="fa fa-shield"></i></a></td>
<td>Leg movement sensor data processing</td>
</tr>
</tbody>
</table>

## Pipeline Configuration

The full details on how each pipeline was executed and configured is available in the complete <a href="https://hbcd-cbrain-processing.readthedocs.io/release_2.0/">HBCD Processing</a> documentation. All pipeline-specific parameters and data criteria are detailed under [Tool Names](https://hbcd-cbrain-processing.readthedocs.io/release_2.0/tool_details.html#tool-names), including **processing settings**, **pipeline outputs**, **file selection for processing**, **QC selection information**, and more.


<!-- 
A general overview of file selection procedures specifically for **structural and functional MRI data** is additionally provided in the [MRI Processing & Derivatives Guide](../mri/mri-proc.md#file-selection-for-processing).
 -->

<!-- ## Pipeline Standards & Design

### Running an HBCD Processing Pipeline
To process HBCD study data using one of these pipelines, follow the installation and usage instructions on the specific pipeline's documentation page (links below).

**Choosing a Container System:**            
**Singularity/Apptainer** → Recommended for university-affiliated HPC clusters, where users lack administrative privileges.         
**Docker** → Preferred for personal computers due to its ease of installation (may require extra setup for HPC use).

All processing containers are available on [Docker Hub](https://hub.docker.com/). -->


