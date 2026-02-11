# MR Exclusion Criteria

## Raw Data Exclusion Criteria

Acquisition parameters vary by scanner vendor, so inclusion criteria are typically defined as acceptable <b>ranges</b> rather than fixed values. Following BIDS conversion, modality-specific criteria are extracted from BIDS sidecar JSON files and evaluated accordingly. All images are additionally checked to confirm they were acquired using a head coil. **Aside from acquisition parameter criteria, all raw data regardless of raw data QC scores are included in the release data.**

<p style="margin-bottom: 0;"><i><b>Acquisition Parameter Ranges for Data Release Eligibility</b></i></p>
<table class="compact-table-no-vertical-lines">
  <thead>
    <tr>
      <th>Scan Type</th>
      <th>Repetition Time (TR)</th>   
      <th>Echo Time (TE)</th>        
      <th>Inversion Time (TI)</th>    
      <th>Slice Thickness</th>  
      <th>Number of Volumes</th>  
    </tr>
  </thead>
<tbody>
<tr>
  <td>T1w</td>
  <td>2.3 - 2.41</td>
    <td>0.002 - 0.0035</td>
  <td>1.06 - 1.1</td>    
    <td>0.8</td>    
    <td>NA</td>    
  </tr>
  <tr>
    <td>T2w</td>
    <td>2.5 - 4.5</td>
    <td>0.09 - 0.15</td>
    <td>0.29 - 0.33</td>    
    <td>0.563 - 0.565</td>    
    <td>NA</td>
  </tr>  
  <tr>
    <td>MRS Localizer</td>
    <td>2.5 - 4.5</td>
    <td>0.09 - 0.15</td>
    <td>0.29 - 0.33</td>    
    <td>0.563 - 0.565</td>    
    <td>NA</td>
  </tr>   
  <tr>
    <td>Diffusion</td>
    <td>4.8</td>
    <td>0.0880 - 0.0980</td>
    <td>NA</td>    
    <td>1.7</td>    
    <td>≥ 90 (AP + PA)</td>  
  </tr>  
  <tr>
    <td>EPI Fieldmap</td>
    <td>8.4 - 9.2</td>
    <td>0.064 - 0.0661</td>
    <td>2</td>    
    <td>0.563 - 0.565</td>    
    <td>NA</td>
  </tr>  
  <tr>
    <td>Functional</td>
    <td>1.725</td>
    <td>0.0369 - 0.0371</td>
    <td>NA</td>    
    <td>2</td>  
    <td>≥ 87 (~2.5 min)</td>   
  </tr>  
</tbody>
</table>

## Processed Data Exclusion Criteria

Structural and functional MRI derivatives were evaluated using **BrainSwipes**, a web-based QC tool that collects QC ratings through visual inspection of standardized reports (<a href="../brainswipes/" target="_blank">see MRI QC Procedures > BrainSwipes</a>). Any structural or functional dataset with an average BrainSwipes score below **0.5** was flagged for additional expert manual review (<a href="#manual-review">expand section below for details</a>).

<div id="manual-review" class="table-banner" onclick="toggleCollapse(this)"> <span class="emoji"><i class="fa fa-circle-check"></i></span> <span class="text-with-link"> <span class="text">Details: Expert Manual Review of Flagged Data</span> <a class="anchor-link" href="#manual-review" title="Copy link"> <i class="fa-solid fa-link"></i> </a> </span> <span class="arrow">▸</span> </div> 
<div class="collapsible-content"> <p>Flagged data underwent additional review to identify sessions with severe quality issues that should be excluded from the release. These severe issues primarily reflected underlying data quality problems rather than processing errors and were flagged for secondary <a href="../qc/">raw MR data QC</a>.</p>
<ul> Manual review was performed on:
<li>a subset of data flagged for structural QC failures, and</li> <li><em>all</em> data flagged for functional-only QC failures.</li> </ul>
<p>This process was applied to all datasets except V02 sessions reconstructed using the <strong>Infant FreeSurfer (hash-2afa9081)</strong> workflow, which consistently produced poor-quality outputs. For this group, sessions were removed based on BrainSwipes QC scores alone without additional review. We advise against using this data for analysis (<a href="../mri-proc/#warning">see Data Warning</a>).</p>
<p><strong>Structural QC.</strong> Structural BrainSwipes ratings were generally reliable and indicated low failure rates (0–3%). Only a subset of structurally flagged data required additional review to confirm removal.</p>
<p><strong>Functional QC.</strong> Functional ratings exhibited higher apparent failure rates, likely because raters applied stricter, adult-oriented QC criteria. Therefore, all sessions with only functional QC failures were manually reviewed to determine which represented true severe issues for removal.</p>
</div>
<p></p>

Session data with confirmed severe **structural issues** were removed across the pipeline derivatives indicated below. This includes Osprey and qMRI-PostProc pipelines for MRS and qMRI as these depend on BIBSNet outputs. Sessions without structural issues flagged for **functional issues** (at least one severely failing BOLD run) were only removed from Infant fMRIPrep and XCP-D derivatives. 

<table class="table-no-vertical-lines">
  <thead>
    <tr>
      <th>QC Type</th>
      <th><a href="mri-proc.md#bibsnet">BIBSNet</a></th>
      <th><a href="mri-proc.md#infant-fmriprep">Infant fMRIPrep</a></th>
      <th><a href="mri-proc.md#m-crib-s-freesurfer-surface-reconstruction-methods">M-CRIB-S / FreeSurfer</a></th>
      <th><a href="mri-proc.md#xcp-d">XCP-D</a></th>
      <th><a href="mrs.md#derivatives">Osprey</a></th>
      <th><a href="qmri.md#derivatives">qMRI-PostProc</a></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Structural</strong></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
    </tr>
    <tr>
      <td><strong>Functional</strong></td>
      <td></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td></td>
      <td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

See the [2.0 Release Notes](../../changelog/releasenotes.md#20-new-brain-imaging-derivatives-exclusions) for a summary of sessions excluded from the release. 

### Caveat: Sessions Missing XCP-D Outputs
BrainSwipes QC relies on visual reports generated by **XCP-D**, the final stage of structural and functional MRI processing (<a href="../mri-proc/#structural-functional-mri-processing-overview" target="_blank">see overview</a>). **If a session fails during XCP-D or at any earlier stage, BrainSwipes QC results are not available and therefore not reviewed for exclusion due to severe data quality issues.** Therefore, if you are analyzing derivatives from earlier stages (e.g., BIBSNet or Infant fMRIPrep), we recommend checking for missing XCP-D derivatives, as this may indicate underlying data quality issues.
