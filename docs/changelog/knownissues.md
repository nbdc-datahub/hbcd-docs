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

## <a href="../../instruments/#mri" target="_blank"><i class="fa fa-brain"></i></a> Imaging Data

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