# Known Issues

The following issues have been identified in the current HBCD data release. **We are actively working to address them and expect most fixes to be implemented in Release 2.0 unless otherwise noted.** This page will be updated as new issues are discovered.  

If you have questions or would like to report an issue, please submit a ticket through the [Lasso Help Center](https://nbdc.lassoinformatics.com/issue-tracker).

## General

<div id="instr-metadata" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">Instruction Metadata — Read Carefully</span>
  <span class="badge">Fix: TBD</span>
  <a class="anchor-link" href="#instr-metadata" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>

  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>Instruction text in the form's metadata is extracted programmatically from the most recent instruction field in the REDCap Data Dictionary for each form, based on field order. <b>As a result:</b></p>
<ul style="margin-top: 0.2em; margin-bottom: 0.2em;">
  <li>If an instruction spans multiple fields, only the <b>last portion</b> will be captured.</li>
  <li>Some fields may display text intended for a <b>previous section</b>.</li>
</ul>
<p style="margin-top: 0; padding-top: 0;">Manual curation of instruction metadata is planned for future releases. For the most accurate information, always refer to the original form.</p>
</div>

## <a href="../../instruments/#demo" target="_blank"><i class="fas fa-id-card"></i></a> Demographics

### Basic Demographics (`sed_basic_demographics`)

<div id="mother-race" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">Mother Race (<code>screen_mother_race</code>): Erroneous Inclusion of Response Option 2</span>
  <span class="badge">Fix: 2.0</span>
  <a class="anchor-link" href="#mother-race" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>Erroneous inclusion of two levels for Hawaiian race (2 = <i>Hawaiian</i>; 7 = <i>Native Hawaiian or Other Pacific Islander</i>). The 2 = <i>Hawaiian</i> code was not a valid response option and can be ignored; no participants selected it.</p>
</div>

<div id="child-acs-1" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">Child Multi-Race & -Ethnicity (<code>child_ethnoracial_acs_by_multi_*</code>): Duplicate Coding</span>
  <span class="badge">Fix: 2.0</span>
  <a class="anchor-link" href="#child-acs-1" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>Child Multi-Race (<code>child_ethnoracial_acs_by_multi_race</code>) and Multi-Ethnicity (<code>child_ethnoracial_acs_by_multi_ethnicity</code>) variables have the same data and levels. Child Multi-Race to be removed to resolve duplication.</p>
</div>

<div id="child-acs-2" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">Child Multi-Race & -Ethnicity (<code>child_ethnoracial_acs_by_multi_*</code>): V01 Values to be Removed</span>
  <span class="badge">Fix: 2.0</span>
  <a class="anchor-link" href="#child-acs-2" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>Child Multi-Race & Ethnicity (<code>child_ethnoracial_acs_by_multi_&lt;race|ethnicity&gt;</code>) V01 data will be removed and in the meantime, we do not recommend using V01 data for this variable in analyses.</p>
</div>

### Visit Information (`par_visit_data`)

<div id="visit1" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">Withdrawal Date (<code>participant_withdrawal_date</code>): Value of <code>12/26/1999</code> if No Withdrawal</span>
  <span class="badge">Fix: 2.0</span>
  <a class="anchor-link" href="#visit1" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>Participants who did <b>not</b> withdraw from the study (<code>participant_withdrawal</code> = “no”) are assigned a sentinel withdrawal date (<code>participant_withdrawal_date</code>) of <code>12/26/1999</code>. This date simply indicates <b>no withdrawal</b> and can be ignored. It will be removed in a future release for clarity. Participants who <b>did</b> withdraw (“yes”) have valid withdrawal dates and are unaffected.</p>
</div>

<div id="visit-su2" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">Biospec Substance Use Flags (<code>su_flag_bio_*</code>): Erroneous Inclusion for Visit 2</span>
  <span class="badge">Fix: 2.0</span>
  <a class="anchor-link" href="#visit-su2" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>Substance use flags derived from USDTL urine toxicology results (<a href="../../instruments/demo/visitinfo/#substance-use-flags">see details</a>) are erroneously included for Visit 2. Urine samples are not collected at Visit 2, and these values are duplicates of Visit 1 data. They will be removed in the next release and can be safely ignored.</p>
</div>

<div id="visit-su3" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">TLFB Substance Use Flags (<code>su_flag_tlfb_*</code>): Incorrect Values for Participants Missing V02</span>
  <span class="badge">Fix: 2.0</span>
  <a class="anchor-link" href="#visit-su3" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>The TLFB substance use flags (<a href="../../instruments/demo/visitinfo/#substance-use-flags">see details</a>) for participants who do not have a Visit 2 have an incorrect value of 'no' instead of 'null.' These values will be corrected to 'null.'</p>
</div>


## <a href="../../instruments/#biospec" target="_blank"><i class="fa fa-vial"></i></a> Biospecimen & Omics

<div id="cot-u" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">Urine Toxicology - Cotinine (<code>bio_c_cot_u</code>): Missing Values Incorrectly Set to 0</span>
  <span class="badge">Fix: 2.0</span>
  <a class="anchor-link" href="#cot-u" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>In the Urine toxicology results (<code>bio_bm_biosample_urine</code>), all negative values for urinary cotinine (<code>bio_c_cot_u</code>) were previously set to <code>0</code>, as negative values are not biologically plausible. During this correction, <b>missing values</b> were inadvertently also set to <code>0</code> (N = 18). These values will be restored to missing in a future release. In the meantime, users can identify affected records by checking <code>bio_c_nicotine_u</code> for values of <code>3</code> (<code>--invalid</code>).</p>
</div>

## <a href="../../instruments/#neurocog" target="_blank"><i class="fa fa-brain"></i></a> Neurocognition & Language

<div id="spm2-1" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">SPM2 (<code>ncl_cg_spm2__inf</code>): Age Fields Missing</span>
  <span class="badge">Fix: 2.0</span>
  <a class="anchor-link" href="#spm2-1" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>Age fields are not currently included for the SPM-2. Until added in a future release, users can refer to corresponding age variables in related datasets for the same time point.</p>
</div>

<div id="spm2-2" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">SPM2 (<code>ncl_cg_spm2__inf</code>): Status Scores Missing</span>
  <span class="badge">Fix: 2.0</span>
  <a class="anchor-link" href="#spm2-2" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>T-scores are now provided (see <a href="../../changelog/releasenotes/#r1.1ngl">1.1 Resolved Known Issues</a>), but <b>STATUS SCORE</b> is still missing for all but one subscale. To be provided in the next release.</p>
</div>

## <a href="../../instruments/#pex" target="_blank"><i class="fa-solid fa-baby"></i></a> Pregnancy & Exposure, Including Substance Use

<div id="pex" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">Pregnancy & Infant Health (<code>pex_bm_health*</code>): ICD Codes Inconsistently Provided</span>
  <span class="badge">Fix: 2.1</span>
  <a class="anchor-link" href="#pex" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>In cases where ICD codes are provided, corresponding names/labels are sometimes missing. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a>.</p>
</div>

<div id="apa" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">APA 1/2 (<code>pex_bm_apa_anger_*</code>): Anger Subscores Missing</span>
  <span class="badge">Fix: 2.0</span>
  <a class="anchor-link" href="#apa" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>T-scores and total scores are missing in the APA 1/2 for only the Anger subscale.</p>
</div>

<div id="tlfb" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">TLFB (<code>pex_ch_tlfb</code>): Missing Age Fields</span>
  <span class="badge">Fix: 2.0</span>
  <a class="anchor-link" href="#tlfb" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>TLFB age variable fields (<code>gestational_age</code>, <code>adjusted_age</code>, and <code>candidate_age</code>) were removed for R1.1 due to incorrect values. Until added in a future release, users can refer to corresponding age variables in related datasets for the same time point.</p>
</div>
    
## <a href="../../instruments/#socenvdet" target="_blank"><i class="fas fa-city"></i></a> Social & Environmental Determinants

<div id="discr" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">PhenX+ Discrimination (<code>sed_bm_phx__discr.006</code>): Blank Cells</span>
  <span class="badge">Fix: 2.0</span>
  <a class="anchor-link" href="#discr" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>For the PhenX+ Discrimination survey, the <code>sed_bm_phx__discr.006</code> multi-select question:<br>
<i>"What do you think is the main reason for these experiences? If more than one main reason, check all that apply."</i><br>
is blank for some participants. This will be corrected in R2.0.</p>
</div>

## <a href="../../instruments/#mri" target="_blank"><i class="fa fa-magnet"></i></a> Imaging Data

<div id="mr-runid" class="issues-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text-with-link">
  <span class="text">MR Data: Incorrect Run ID Order</span>
  <span class="badge">Fix: TBD</span>
  <a class="anchor-link" href="#mr-runid" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="issues-collapsible-content">
<p>For HBCD imaging data with multiple runs, the <code>run-{X}</code> field may not reflect chronological acquisition order.  
This affects both <b>raw BIDS and derivatives</b> as well as <b>derivative files converted to HBCD tabulated data</b> (<a href="../../datacuration/overview" target="_blank">see file type details</a>). Despite this, data remain internally consistent — e.g., run IDs match between raw and processed datasets.</p>
</div>

<br>

