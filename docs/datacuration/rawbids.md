# Raw BIDS

The `rawdata/` folder includes raw <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> magnetic resonance imaging (MRI), spectroscopy (MRS), electroencephalography (EEG), and motion/accelerometry (i.e. [wearable sensor](../instruments/sensors/wearsensors.md) recordings for leg motion) data, converted to BIDS and organized under subject and session-specific directories for processing through BIDS App pipelines ([see details](../instruments/processing/index.md)). *Note that the folder and file counts may vary across subjects and sessions, which is expected in a large-scale infant MRI study.*

<pre class="folder-tree">
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

## Participant-, Session-, & Scan-Level Data
Participant-, session-, and scan-level data are stored in standardized `.tsv` files, accompanied by a `.json` sidecar file that defines the columns and describes the data fields, located in the `rawdata/` directory and its subdirectories:

- **Participant-level**: Stored in `rawdata/participants.tsv`, this file includes basic demographic and participant information (e.g., sex).
- **Session-level**: Stored in `sub-<label>_sessions.tsv` within each subject folder, this file includes session information such as collection site, the participant’s age at each session, and head size.
- **Scan-level**:  Each session folder includes a `sub-<label>_ses-<label>_scans.tsv` file with per-scan information including participant age at scan as well as all raw data QC scores (see [HBCD MR Quality Control Procedures](../instruments/mri/qc.md#location-of-raw-data-qc-results-in-data-release)).

### Fields Reporting Age

See description of fields reporting age under Age Variable Definitions > <a href="../../instruments/agevariables/#raw-file-based-data" target="_blank">Raw File-Based Data</a>.

## Imaging

<div id="bids-imaging" class="table-banner" onclick="toggleCollapse(this)">
  <img src="../images/BIDS-logo.png" style="width: 3%;" alt="BIDS-logo">
  <span class="text-with-link">
  <span>BIDS Conversion Procedures: Imaging</span>
  <a class="anchor-link" href="#bids-imaging" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>To convert imaging data to BIDS standard formatting, the DICOM image files are processed through an <a href="https://github.com/rordenlab/dcm2niix/tree/c5caaa9f858b704b61d3ff4a7989282922dd712e">HBCD-customized version</a> of the <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a> tool.</p>

<p><b>Hardcoded Fields for Philips &amp; GE</b><br>
In some cases, <code>dcm2niix</code> conversion led to missing or incorrectly configured NIfTI/JSON metadata. To address these issues, the headers for the file types listed below were hard-coded after conversion. These hard-coded values are also documented in the <code>HardCodedValues</code> field of the corresponding JSON sidecar file.
<ul>
<strong><u>Philips</u></strong>
<li>DWI: <code>PhaseEncodingDirection</code>, <code>TotalReadoutTime</code>, & <code>SliceTiming</code> (<code>SmallDelta</code> & <code>LargeDelta</code> also added)</li>
<li>EPI: <code>PhaseEncodingDirection</code> & <code>TotalReadoutTime</code></li>
<li>BOLD: <code>PhaseEncodingDirection</code>, <code>TotalReadoutTime</code>, & <code>SliceTiming</code></li>
<br>
<strong><u>Philips & GE</u></strong>
<li>T1W: <code>RepetitionTime</code></li>
</ul>
</p>
<p><b>QALAS Post-Conversion Modifications</b><br>
Depending on the scanner manufacturer, <code>dcm2niix</code> conversion for QALAS produced either five 3D NIfTI files or a single 4D NIfTI file with five volumes (as well as missing JSON header information). To standardize the output, all <code>dcm2niix</code>-derived QALAS series were converted into five separate NIfTI files, each corresponding to a different inversion time (labeled using the <code>inv-&lt;label&gt;</code> BIDS entity). The associated JSON sidecar was then updated with the following:
<ol>
<li><code>T2Prep</code> field of <code>inv-0</code> QALAS file hard-coded to 0.10 (Siemens), 0.09 (GE), and 0.10 (Philips)</li>
<li><code>InversionTime</code> values (sec) for QALAS files hard-coded as follows for each manufacturer:</li>
</ol>
</p>
<table>
  <tr>
  <th width="100">QALAS file</th>
  <th width="100">Siemens</th>
  <th width="100">GE</th>
  <th>Philips</th>
  </tr>
  <tbody>
    <tr><td>inv-0</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>inv-1</td><td>0.1</td><td>0.119300</td><td>0.115000</td></tr>
    <tr><td>inv-2</td><td>1</td><td>1.0191834</td><td>1.010522</td></tr>
    <tr><td>inv-3</td><td>1.9</td><td>1.919068</td><td>1.906045</td></tr>
    <tr><td>inv-4</td><td>2.8</td><td>2.818952</td><td>2.801567</td></tr>
  </tbody>
</table>
</div>


## Modality-Level Descriptions

- [EEG](../instruments/eeg/index.md#raw-bids)
- [Motion](../instruments/sensors/wearsensors.md#raw-bids)
- [MRS](../instruments/mrs/index.md#raw-bids)






### Anatomical (anat/)
Anatomical files include T1- and T2-weighted MRI images, MRS localizer files (`acq-mrsLocAx` and `acq-mrsLocCor` indicate axial and coronal localizers, respectively), and Quantitative MRI QALAS files. 
<pre class="folder-tree">
anat/
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_T1w.nii.gz 
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_T1w.json
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_T2w.nii.gz
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_T2w.json
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-sub-<span class="placeholder">&lt;mrsLocAx|mrsLocCor&gt;</span>_run-<span class="label">{X}</span>_T2w.nii.gz 
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-sub-<span class="placeholder">&lt;mrsLocAx|mrsLocCor&gt;</span>_run-<span class="label">{X}</span>_T2w.json
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_inv-sub-<span class="placeholder">&lt;0|1|2|3|4&gt;</span>_QALAS.nii.gz
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_inv-sub-<span class="placeholder">&lt;0|1|2|3|4&gt;</span>_QALAS.json
</pre>
*NOTE: See information about hardcoded fields for Philips and GE T1ws and post-BIDS conversion modifications for QALAS [here](#bids-imaging).*

### Diffusion (dwi/)
Diffusion files include DWI runs (`*_dwi.nii.gz`) along with `bval` and `bvec` (magnitudes and orientations of the diffusion gradients for each volume, respectively), and single-band reference files (`*_sbref.nii.gz`). All images were acquired in both AP (`dir-AP`) and PA (`dir-PA`) phase encoding directions.
<pre class="folder-tree">
dwi/
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.bval
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.bvec
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.nii.gz
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.json
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_sbref.json
|__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_sbref.nii.gz
</pre>
*NOTE: See information about hardcoded fields for Philips and GE DWI data [here](#bids-imaging).*

### Functional (func/) and Fieldmaps (fmap/) 
Functional files include BOLD functional resting state images under `func/`. Each functional acquisition has an associated pair of EPI fieldmaps acquired to use for distortion correction under `fmap/`, with AP (`dir-AP`) and PA (`dir-PA`) phase encoding directions. 

**Siemens, GE, and Philips additionally include B1 fieldmaps**: For Siemens, `acq-<anat|fmap>` denotes the anatomical (like) image and scaled flip angle map whereas for GE and Philips, `acq-tr<1|2>` denotes the first and second TR image (see BIDS specification for quantitative MRI: [TB1TFL and TB1RFM](https://bids-specification.readthedocs.io/en/stable/appendices/qmri.html#tb1tfl-and-tb1rfm-specific-notes) and [TB1AFI](https://bids-specification.readthedocs.io/en/stable/appendices/qmri.html#tb1afi-specific-notes)):

<pre class="folder-tree">
|__ func/
|   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_bold.nii.gz
|   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_bold.json
|
|__ fmap/
    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-AP_run-<span class="label">{X}</span>_epi.nii.gz
    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-AP_run-<span class="label">{X}</span>_epi.json
    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-PA_run-<span class="label">{X}</span>_epi.nii.gz
    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-PA_run-<span class="label">{X}</span>_epi.json
	|
	| <span class="hashtag"># SIEMENS ONLY:</span>
    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-anat_run-<span class="label">{X}</span>_TB1TFL.nii.gz
    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-anat_run-<span class="label">{X}</span>_TB1TFL.json
    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-fmap_run-<span class="label">{X}</span>_TB1TFL.nii.gz
    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-fmap_run-<span class="label">{X}</span>_TB1TFL.json
	|
	| <span class="hashtag"># GE AND PHILIPS ONLY:</span>
    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-tr1_run-<span class="label">{X}</span>_TB1AFI.nii.gz 
    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-tr1_run-<span class="label">{X}</span>_TB1AFI.json 
    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-tr2_run-<span class="label">{X}</span>_TB1AFI.nii.gz
    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-tr2_run-<span class="label">{X}</span>_TB1AFI.json
</pre>
*NOTE: See information about hardcoded fields for Philips and GE BOLD data [here](#bids-imaging).*





<br>