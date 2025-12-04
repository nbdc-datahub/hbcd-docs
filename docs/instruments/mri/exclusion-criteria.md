# MR Exclusion Criteria

## Raw Data Exclusion Criteria

Acquisition parameters vary by scanner vendor, so inclusion criteria are typically defined as acceptable <b>ranges</b> rather than fixed values. Following BIDS conversion, modality-specific criteria are extracted from BIDS sidecar JSON files and evaluated accordingly. All images are additionally checked to confirm they were acquired using a head coil.

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

Structural and functional MRI derivatives were evaluated using <strong>BrainSwipes</strong>, a web-based quality control tool that collects expert ratings on image quality via visual assessment of standardized reports <i>(see <a href="../qc/#brainswipes" target="_blank">MRI QC Procedures &gt; BrainSwipes</a> for details)</i>. Structural and functional data was flagged for additional review if the average QC score across visual reports was less than 0.5. 

Additional expert manual review was performed on flagged data to identify sessions with severe issues to exclude from the release. Severe issues noted were the result of underlying data quality issues as opposed to pipeline processing errors, and so were additionally flagged for secondary [raw MR data QC review](qc.md#raw-mr-data-qc). <span style="color: red;">[LUCI NOTE: EXPLAIN WHAT "SEVERE ISSUES" ACTUALLY MEANS HERE]</span>

<div id="manual-review" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
<span class="text">Details: Expert Manual Review of Flagged Data</span>
  <a class="anchor-link" href="#manual-review" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Additional manual review by experts was performed on a small subset of the data flagged with structural QC failures and all data flagged with only functional QC failures.</p>
<p><b>Structural QC</b>: Structural BrainSwipes QC results are fairly consistent and reliable and reported only 0-3% of failures, so only a subset of the data flagged for structural QC failures were followed up by additional expert review.</p>
<p><b>Functional QC</b>: Functional BrainSwipes QC results report an inflated rate of failures due, perhaps due to raters performing QC based on adult data QC standards, which are much more strict than for infant data. Therefore, all sessions with only functional failures reported were followed up with additional expert manual review to identify the severe failures.</p> <span style="color: red;">LUCI NOTE: not sure how to explain this in a way that would make sense to users. either way, should probably state inherent drawbacks of BrainSwipes and the results for users who may wish to use them for determining their own data exclusions</span>
<p><b>V02	Infant FreeSurfer (hash-2afa9081)</b>: was not manually reviewed because data is bad, and we expected that. so removed data based on BrainSwipes results alone - also mention data warning telling users not to use this data - <a href="../mri-proc/#warning">link</a></p>
</div>
<p></p>

#### Structural Data QC Failure
Session data with severe structural issues were removed across the following pipeline derivative folders: [BIBSNet](mri-proc.md#bibsnet), [Infant fMRIPrep](mri-proc.md#infant-fmriprep), [M-CRIB-S and FreeSurfer](mri-proc.md#m-crib-s-freesurfer-surface-reconstruction-methods), and [XCP-D](mri-proc.md#xcp-d).    
Sessions were also removed from [Osprey](mrs.md#derivatives) and [qMRI-PostProc](qmri.md#derivatives) derivatives (used for MRS and quantitative MRI processing, respectively) and these pipelines both utilize BIBSNet outputs. 

#### Functional Data QC Failure
BOLD runs with an average QC score less than 0.5 were flagged for additional expert manual review. For sessions with severe issues in one or more BOLD run, [Infant fMRIPrep](mri-proc.md#infant-fmriprep) and [XCP-D](mri-proc.md#xcp-d) derivatives for that session were excluded from the release.

#### Summary of Sessions Excluded From Release 
<table class="table-no-vertical-lines">
<tfoot>
<tr><td colspan="5"><b>*</b> Includes sessions with failed structural as well as functional QC<br>
<b>**</b> Includes sessions with no structural QC failures, but at least 1 BOLD run that failed QC
</td></tr>
</tfoot>
<thead>
<tr>
<th>Visit</th>
<th>Surface Reconstruction Workflow</th>
<th>% Structural QC Failure*</th>
<th>% Functional QC Failure**</th>
<th>Total</th>
</tr>
</thead>
<tbody>
<tr><td>V02</td><td>M-CRIB-S (hash-0f306a2f)</td><td>3%</td><td>16%</td><td>19%</td></tr>
<tr><td>V02</td><td>Infant FreeSurfer (hash-2afa9081)</td><td>19%</td><td>30%</td><td>49%</td></tr>
<tr><td>V03</td><td>Infant FreeSurfer (hash-2afa9081)</td><td>3%</td><td>3%</td><td>6%</td></tr>
<tr><td>V04</td><td>Infant FreeSurfer (hash-2afa9081)</td><td>0%</td><td>3%</td><td>3%</td></tr>
</tbody>
</table>

### Caveat: Sessions Missing XCP-D Outputs Due to Incomplete Processing
BrainSwipes QC is performed on visual reports generated by <strong>XCP-D</strong>, the final stage of structural and functional MRI processing (see <a href="../mri-proc/#structural-functional-mri-processing-overview" target="_blank">Structural & Functional MRI Processing Overview</a>). Session data that fails to process through XCP-D or at an earlier stages do not reach BrainSwipes and therefore will not have associated QC scores. Therefore, if you are using derivatives from earlier processing stages (e.g., BIBSNet or Infant fMRIPrep) for your analysis, we recommend taking note of data missing corresponding XCP-D derivatives and BrainSwipes QC scores, as this may indicate processing failures due to underlying data quality issues. 


#### DRAFTING

 - explain why V02 FS brainswipes scores are missing, why there was no manual review, and why we encourage users not to use this data 
 - Unscored Data: V02 Outputs Processed Via Infant FreeSurfer Workflow

BrainSwipes QC results should be present for most if not all participant data with XCP-D outputs with the key exception: **visit V02 processed using infant FreeSurfer for surface reconstruction.** V02 data (acquired from neonates/0-1 months old) was processed through 2 parallel surface reconstruction workflows, detailed under [M-CRIB-S & FreeSurfer Surface Reconstruction Methods](mri-proc.md#m-crib-s-freesurfer-surface-reconstruction-methods). Expert review and preliminary BrainSwipes QC results made it clear that M-CRIB-S produced much higher quality outputs compared to infant FreeSurfer at the neonatal age range (as it is T2w-based), so manual review via BrainSwipes was only performed on a subset of the data (&lt;20%). We further discourage the use of V02 data processed with FreeSurfer for surface reconstruction for analysis - see [Data Warning](mri-proc.md#warning).    



