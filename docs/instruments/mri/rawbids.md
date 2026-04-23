
# Raw MR BIDS

Each participant/session folder within `rawdata/` contains raw imaging data organized into modality-specific subfolders (e.g., `anat/`, `func/`, `dwi/`), with filenames encoding acquisition details (task, direction, run, etc.). See <a href="../../../datacuration/file-based-data/#raw-bids" target="_blank">File-Based Data</a> for a general introduction to BIDS.

<div id="bids-conversion" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span><span class="text-with-link"><span class="text">BIDS Conversion Procedures</span>
  <a class="anchor-link" href="#bids-conversion" title="Copy link"><i class="fa-solid fa-link"></i></a></span><span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>For MRI, DICOM images are converted using an HBCD-customized version of <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a>. For MRS, vendor-specific formats (Siemens <code>.dat</code>, Philips data/list, GE P-file) are converted using <a href="https://github.com/DCAN-Labs/hbcd_mrs_to_nii_conversion">spec2nii v0.7.0</a>.</p>
<p>Additional post-processing is performed for MRI to ensure consistency across vendors. This includes converting QALAS to five 3D NIfTI files (labeled by inversion time) and hardcoding missing or inconsistent metadata fields for various modalities as follows:</p>
<table class="compact-table-no-vertical-lines">
  <thead>
    <tr>
      <th>Field</th>
      <th>DWI <span style="font-weight:normal;">(Philips)</span></th>
      <th>EPI <span style="font-weight:normal;">(Philips)</span></th>
      <th>BOLD <span style="font-weight:normal;">(Philips)</span></th>
      <th>T1w <span style="font-weight:normal;">(Philips & GE)</span></th>
      <th>QALAS <span style="font-weight:normal;">(Philips, Siemens, GE)</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>PhaseEncodingDirection</code></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td></td> <td></td>
    </tr>
    <tr>
      <td><code>TotalReadoutTime</code></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td></td> <td></td>
    </tr>
    <tr><td><code>SliceTiming</code></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td></td> <td></td></tr>
    <tr><td><code>&lt;Small|Large&gt;Delta</code></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td></td> <td></td><td></td><td></td></tr>
    <tr><td><code>RepetitionTime</code></td> <td></td> <td></td> <td></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td><td></td>    </tr>
      <tr>      <td><code>T2Prep</code></td><td></td> <td></td> <td></td> <td></td> <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>      <tr><td><code>InversionTime</code></td><td></td><td></td><td></td><td></td><td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>    </tr>
  </tbody>
</table>
</div>
<p></p>

<table class="table-no-vertical-lines">
<thead><tr><th>Folder</th><th>Modality</th><th>Key Files</th></tr></thead>
<tbody>
<tr><td rowspan="3"><code>anat/</code></td><td>sMRI</td><td>T1w, T2w</td></tr>
<tr><td>qMRI</td><td>QALAS (<code>inv-0</code> → <code>inv-4</code>) files</td></tr>
<tr><td>MRS</td><td>Localizers (<code>aqc-mrsLocAx</code>, <code>aqc-mrsLocCor</code>)</td></tr>
<tr><td><code>func/</code></td><td>fMRI</td><td>Resting-state BOLD runs</td></tr>
<tr><td rowspan="2"><code>fmap/</code></td><td>fMRI</td>
<td>EPI fieldmap pairs acquired in AP/PA directions for each <code>func/</code> BOLD run</td></tr>
<tr><td>qMRI</td><td>B1+ fieldmaps</td></tr>
<tr><td><code>dwi/</code></td><td>dMRI</td><td>DWI; gradient magnitude/direction (<code>.bval</code>/<code>.bvec</code>); single-band reference images (<code>*_sbref.nii.gz</code>)</li></ul></td></tr>
<tr><td><code>mrs/</code></td><td>MRS</td>
<td style="word-wrap: break-word; white-space: normal;">Metabolite spectra and water reference scans (<code>{svs|ref}.nii.gz</code>), each acquired via short echo time and HERCULES edited spectra (<code>acq-{shortTE|hercules}</code>)</td>
</tr></tbody></table>

#### Raw BIDS Folder Structure

<pre class="folder-tree">
<span><a style="color: white;" href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: white;" class="fa fa-circle-info"></i> How To Read File Trees →</a></span>
<span class="hashtag"># All NIfTI files include sidecar JSON metadata ({FILENAME}.json)</span>
hbcd/
└── rawdata/
    └── sub-{ID}/
        └── ses-{V0X}/
            ├── anat/
            │   ├── *_<span class="placeholder">&lt;T1w|T2w&gt;</span>.nii.gz                      <span class="hashtag"># Structural MRI</span>
            │   ├── *_inv-<span class="placeholder">&lt;0-4&gt;</span>_QALAS.nii.gz                <span class="hashtag"># Quantitative MRI (QALAS)</span>
            │   └── *_acq-mrsLoc<span class="placeholder">&lt;Ax|Cor&gt;</span>_run-{X}_T2w.nii.gz <span class="hashtag"># MRS localizers</span>
            │
            ├── func/
            │   └── *_task-rest_dir-PA_run-{X}_bold.nii.gz  <span class="hashtag"># Resting-state fMRI</span>
            │
            ├── fmap/
            │   ├── *_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-{X}_epi.nii.gz        <span class="hashtag"># fMRI fieldmaps</span>
            │   ├── *_acq-<span class="placeholder">&lt;anat|famp&gt;</span>_run-{X}_TB1TFL.nii.gz <span class="hashtag"># qMRI Siemens B1+ fieldmaps</span>
            │   └── *_acq-<span class="placeholder">&lt;tr1|tr2&gt;</span>_run-{X}_TB1AFI.nii.gz   <span class="hashtag"># qMRI GE/Philips B1+ fieldmaps</span>
            │
            ├── dwi/
            │   ├── *_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-{X}_dwi.nii.gz        <span class="hashtag"># Diffusion MRI</span>
            │   ├── *_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-{X}_dwi.bval
            │   ├── *_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-{X}_dwi.bvec
            │   └── *_dir-<span class="placeholder">&lt;AP|PA&gt;</span>_run-{X}_sbref.nii.gz
            │
            └── mrs/
                ├── *_acq-<span class="placeholder">&lt;shortTE|hercules&gt;</span>_run-{X}_svs.nii.gz <span class="hashtag"># Spectroscopy (SVS)</span>
                └── *_acq-<span class="placeholder">&lt;shortTE|hercules&gt;</span>_run-{X}_ref.nii.gz <span class="hashtag"># Reference scans</span>
</pre>
