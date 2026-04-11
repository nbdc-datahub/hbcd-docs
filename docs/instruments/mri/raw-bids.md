# MR Raw BIDS

<p>
<div class="table-banner">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
<span class="text">See <a href="../../../datacuration/file-based-data/#raw-bids" target="_blank">File-Based Data</a> for a general introduction to the Brain Imaging Data Structure (BIDS).</span>
</div>
</p>

## BIDS Conversion Procedures

For **MRI**, DICOM images are converted using an <a href="https://github.com/rordenlab/dcm2niix/tree/c5caaa9f858b704b61d3ff4a7989282922dd712e">HBCD-customized</a> version of <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a>, with post-conversion modifications required for certain scan types to maintain consistency across vendors - see <a href="#bids-conversion-mri">MRI Hardcoded Fields & Post-Conversion Modifications</a> below for details.

<div id="bids-conversion-mri" class="table-banner" onclick="toggleCollapse(this)">
  <img src="../images/BIDS-logo.png" style="width: 3%;" alt="BIDS-logo">
  <span class="text-with-link">
  <span class="text">MRI Hardcoded Fields & Post-Conversion Modifications</span>
  <a class="anchor-link" href="#bids-conversion-mri" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><strong>Hardcoded Fields</strong><br>
Key fields for Philips (<i>and GE for T1w scans</i>) are hard-coded to ensure consistency across vendors, as NIfTI/JSON metadata can be omitted or misconfigured during conversion. Hardcoded fields for different modalities/scan types are outlined in the following table and also documented in the JSON sidecars under <code>HardCodedValues</code>. <strong>All of the following were modified for Philips only with the exception of T1w scans, modified for both Philips and GE.</strong></p>
<table class="compact-table-no-vertical-lines" style="width:100%; border-collapse:collapse; table-layout:fixed; text-align:center;">
  <thead>
    <tr>
      <th>Modality</th>
      <th><code>PhaseEncodingDirection</code></th>
      <th><code>TotalReadoutTime</code></th>
      <th><code>SliceTiming</code></th>
      <th><code>&lt;Small|Large&gt;Delta</code></th>
      <th><code>RepetitionTime</code></th>
    </tr>
  </thead>
  <tbody>
    <tr><td>DWI</td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td></td></tr>
    <tr><td>EPI</td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td></td><td></td><td></td></tr>
    <tr><td>BOLD</td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td></td><td></td></tr>
    <tr><td>T1w <i>(both Philips & GE)</i></td><td></td><td></td><td></td><td></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td></tr>
  </tbody>
</table>
<p><strong>QALAS</strong><br>
QALAS conversion yielded either five 3D NIfTI files or one 4D file with five volumes and missing JSON headers. To standardize outputs, all series were split into five NIfTI files, each labeled by inversion time (<code>inv-{X}</code>). The JSON sidecars were updated as follows: <code>T2Prep</code> for QALAS file <code>inv-0</code> is set to 0.10 for Siemens/Philips and 0.09  for GE. <code>InversionTime</code> (s) is hard-coded per manufacturer as follows:</p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; font-size: 90%;">
    <tr>
      <th></th><th>inv-0</th><th>inv-1</th><th>inv-2</th><th>inv-3</th><th>inv-4</th>
    </tr>
    <tr><th>Siemens</th><td>0</td><td>0.1</td><td>1</td><td>1.9</td><td>2.8</td></tr>
    <tr><th>GE</th><td>0</td><td>0.1193</td><td>1.0192</td><td>1.9191</td><td>2.8190</td></tr>
    <tr><th>Philips</th><td>0</td><td>0.115</td><td>1.0105</td><td>1.9060</td><td>2.8016</td></tr>
  </table>
</div>

For **MRS**, vendor-specific raw data formats (Siemens <code>.dat</code>; Philips data/list; GE P-file) were converted to BIDS using a wrapper (<a href="https://github.com/DCAN-Labs/hbcd_mrs_to_nii_conversion">hbcd_mrs_to_nii_conversion</a>) for <a href="https://github.com/wtclarke/spec2nii">spec2nii v0.7.0</a>.

## Anatomical Files (`anat/`)

The `anat/` subfolder contains the following raw data files, all accompanied by sidecar JSON files containing metadata:
<table class="table-no-vertical-lines">
<thead>
    <th>Modality</th>
    <th>Included Files</th>
</thead>
<tbody>
<tr><td>Structural MRI</td> 
<td>T1- and T2-weighted MRI images</td>
</tr>
<tr><td>Quantitative MRI</td>
<td>Five QALAS sequences (<code>inv-*</code>) and axial (<code>aqc-mrsLocAx</code>) + coronal (<code>aqc-mrsLocCor</code>) localizer files</td>
</tr>
</tbody></table>

<p style="margin-bottom: 0; padding-bottom: 0;"><a href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>
<pre class="folder-tree">
hbcd/
|__ rawdata/ 
    |__ sub-<span class="label">{ID}</span>/
        |__ ses-<span class="label">{V0X}</span>/
            |__ anat/ <span class="hashtag"># All files accompanied by sidecar JSONs</span>
            <span class="hashtag"># Structural MRI</span>
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_T1w.nii.gz
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_T2w.nii.gz
            <span class="hashtag"># Quantitative MRI</span>
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-mrsLocAx_run-<span class="label">{X}</span>_T2w.nii.gz
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-mrsLocCor_run-<span class="label">{X}</span>_T2w.nii.gz
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_run-<span class="label">{X}</span>_inv-<span class="placeholder">&lt;0|1|2|3|4&gt;</span>_QALAS.nii.gz
</pre>

## Functional Files (`func/`) & Fieldmaps (`fmap/`)

The `func/` and `fmap/` subfolders contain the following files, all accompanied by sidecar JSONs with metadata:

<table class="table-no-vertical-lines">
<thead>
    <th>Modality</th>
    <th>Included Files</th>
</thead>
<tbody>
<tr><td>Functional MRI</td> 
<td style="word-wrap: break-word; white-space: normal;">Functional BOLD runs in <code>func/</code>, each associated with a pair of EPI fieldmaps in <code>fmap/</code> acquired in AP and PA (<code>dir-&lt;AP|PA&gt;</code>) phase encoding directions (used for distortion correction)</td>
</tr>
<tr><td>Quantitative MRI</td>
<td style="word-wrap: break-word; white-space: normal;">B1+ fieldmaps acquired for flip angle calibration. Note that acquisition methods and associated <a href="https://bids-specification.readthedocs.io/en/stable/appendices/qmri.html">BIDS specifications</a> vary by vendor - see <a href="../qmri/#b1-fieldmap" target="_blank">qMRI README</a> for details.</td>
</tr>
</tbody></table>

<p style="margin-bottom: 0; padding-bottom: 0;"><a href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>
<pre class="folder-tree">
hbcd/
|__ rawdata/ 
    |__ sub-<span class="label">{ID}</span>/
        |__ ses-<span class="label">{V0X}</span>/ <span class="hashtag"># All files accompanied by sidecar JSONs</span>
            |__ func/
            |   |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_task-rest_dir-PA_run-<span class="label">{X}</span>_bold.nii.gz 
            |
            |__ fmap/
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_epi.nii.gz
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-<span class="placeholder">&lt;anat|fmap&gt;</span>_run-<span class="label">{X}</span>_TB1TFL.nii.gz <span class="hashtag"># B1 fmap (Siemens only)</span>
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-<span class="placeholder">&lt;tr1|tr2&gt;</span>_run-<span class="label">{X}</span>_TB1AFI.nii.gz   <span class="hashtag"># B1 fmap (GE & Philips only)</span>
</pre>

## Diffusion (`dwi/`)

Raw diffusion files include DWI runs (`*_dwi.nii.gz`), magnitude (`bval`) and orientation (<code>bvec</code>) of the diffusion gradients for each volume, and single-band reference files (<code>*_sbref.nii.gz</code>), all acquired in AP and PA phase encoding directions (<code>dir-&lt;AP|PA&gt;</code>).

<p style="margin-bottom: 0; padding-bottom: 0;"><a href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>
<pre class="folder-tree">
hbcd/
|__ rawdata/ 
    |__ sub-<span class="label">{ID}</span>/
        |__ ses-<span class="label">{V0X}</span>/
            |__ dwi/
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.bval
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.bvec
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_dwi.nii.gz <span class="hashtag">(+JSON)</span>
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-<span class="label">{X}</span>_sbref.nii.gz <span class="hashtag">(+JSON)</span>
</pre>


## MRS (`mrs/`)

MRS files include metabolite (`*_svs.nii.gz`) and water reference (<code>*_ref.nii.gz</code>) data acquired via short-echo-time (TE = 35 ms; <code>acq-shortTE</code>) and HERCULES (spectral-edited, TE = 80 ms; <code>acq-hercules</code>). The JSON sidecar files include the dimensions of the NIfTI-MRS data array, holding different coil elements in dimension 5 and different transients in dimension 6.

<p><a href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>
<pre class="folder-tree">
hbcd/
|__ rawdata/ 
    |__ sub-<span class="label">{ID}</span>/
        |__ ses-<span class="label">{V0X}</span>/
            |__ mrs/  <span class="hashtag"># All files accompanied by sidecar JSONs</span>
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-shortTE_run-<span class="label">{X}</span>_svs.nii.gz 
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-shortTE_run-<span class="label">{X}</span>_ref.nii.gz 
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-hercules_run-<span class="label">{X}</span>_svs.nii.gz
                |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-hercules_run-<span class="label">{X}</span>_ref.nii.gz
</pre>