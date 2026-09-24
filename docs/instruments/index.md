<style>
.blue-text {
  color: #2563eb;
}

.compact-table-no-vertical-lines {
  width: 100%;
  table-layout: fixed;
  border-collapse: collapse;
}
/* Consistent column widths across every section */
.compact-table-no-vertical-lines th:nth-child(1),
.compact-table-no-vertical-lines td:nth-child(1) {
  width: 30%;
}
.compact-table-no-vertical-lines th:nth-child(2),
.compact-table-no-vertical-lines td:nth-child(2) {
  width: 35%;
}
.compact-table-no-vertical-lines th:nth-child(3),
.compact-table-no-vertical-lines td:nth-child(3) {
  width: 35%;
}

/* Wider Table Name column for sections with long/multiple codes (EEG, Imaging) */
.compact-table-no-vertical-lines.wide-name-col th:nth-child(1),
.compact-table-no-vertical-lines.wide-name-col td:nth-child(1) {
  width: 22%;
}
.compact-table-no-vertical-lines.wide-name-col th:nth-child(2),
.compact-table-no-vertical-lines.wide-name-col td:nth-child(2) {
  width: 23%;
}
.compact-table-no-vertical-lines.wide-name-col th:nth-child(3),
.compact-table-no-vertical-lines.wide-name-col td:nth-child(3) {
  width: 55%;
}

/* INSTRUMENTS FILTER */
.archive-controls {
  margin: 1.5rem 0 1rem;
  padding: 1rem 1.1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: #f8f9fa;
}

.archive-controls-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  align-items: center;
}

.archive-search {
  flex: 1 1 280px;
  min-width: 220px;
}

.archive-controls input,
.archive-controls select,
.archive-controls button {
  box-sizing: border-box;
  height: 38px;
  border: 1px solid #cfd4da;
  border-radius: 5px;
  background: white;
  padding: 0 0.75rem;
  font: inherit;
  font-size: 0.9rem;
}

.archive-controls input:focus,
.archive-controls select:focus,
.archive-controls button:focus {
  outline: 2px solid rgba(25, 155, 214, 0.25);
  border-color: #199bd6;
}

.archive-controls button {
  cursor: pointer;
  font-weight: 600;
}

.archive-controls button:hover {
  background: #f1f3f5;
}

.archive-status {
  margin-top: 0.65rem;
  font-size: 0.85rem;
  color: #666;
}

.archive-empty {
  display: none;
  padding: 2rem 1rem;
  text-align: center;
  color: #777;
  font-size: 0.95rem;
}

@media (max-width: 700px) {
  .archive-controls-row {
    align-items: stretch;
  }

  .archive-controls input,
  .archive-controls select,
  .archive-controls button {
    width: 100%;
  }

  .archive-search {
    flex-basis: 100%;
  }
}
</style>

# Study Measures

This page lists all instruments included in the current release, organized by domain. Each instrument links to a separate README page containing instrument documentation, including, where applicable, details of implementation and data collection, quality control procedures, data and responsible use warnings, scoring procedures, and references. Study protocols are also available on the [HBCD Study site](https://hbcdstudy.org/study-protocols/). 

<div class="archive-controls" aria-label="Instrument filters">
  <div class="archive-controls-row">
    <input
      id="instr-search"
      class="archive-search"
      type="search"
      placeholder="Search instrument, construct, or table name..."
      aria-label="Search instruments"
    >
    <select id="instr-domain" aria-label="Filter by domain">
      <option value="">All domains</option>
    </select>
    <button id="instr-reset" type="button">Clear filters</button>
  </div>
  <div id="instr-status" class="archive-status" aria-live="polite"></div>
</div>
<div id="instr-empty" class="archive-empty">No matching instruments found.</div>

### <i class="fa fa-clipboard-list header-icon"></i> Administrative

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Instrument</th>
<th>Construct</th>
<th>Table / Folder Name</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="admin/study-navigators">Study Navigator Contact Form</a></td>
<td>Recruitment/Retention</td>
<td><i>concatenated/study_navigator/</i></td>
</tr>
</tbody>
</table>

### <i class="fa fa-people-arrows header-icon"></i> Behavior & Caregiver-Child Interaction
<table class="compact-table-no-vertical-lines">
<thead>
  <tr>
    <th>Instrument</th>
    <th>Construct</th>
    <th>Table Name</th>
  </tr>
</thead>
  <tbody>
  <tr>
    <td><a href="bcgi/chaos">CHAOS</a></td>
    <td>Family Organization</td>
    <td><code>mh_cg_chaos</code></td>
  </tr>
  <tr>
    <td>
      <a href="bcgi/ecpromis">ecPROMIS Caregiver-Child</a> <span class="subtle">(&lt;1/1-5 yrs)</span>
      </td>
    <td>Caregiver-Child Interactions</td>
    <td><code>mh_cg_pms__cc__inf</code> / <code>mh_cg_pms__cc__1to5</code> </td>
  </tr>
  <tr>
    <td><a href="bcgi/ecpromis-pr">ecPROMIS Peer</a></td>
    <td>Peer Relationships</td>
    <td><code>mh_cg_pms__peer</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/ecpromis-selfreg">ecPROMIS Self-Regulation</a></td>
    <td>Self-Regulation and Flexibility</td>
    <td><code>mh_cg_pms__selfreg</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/erica">ERICA</a></td>
    <td>Emotional Regulation</td>
    <td><code>mh_cg_erica</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/fad">FAD (GF6+)</a></td>
    <td>Global Functioning of Family Unit</td>
    <td><code>mh_cg_fad</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/ibqr">IBQ-R (VSF)+BI</a></td>
    <td rowspan="2">
      Surgency/Extraversion,
      Negative Affectivity,
      Effortful Control,
      Behavioral Inhibition
      </td>
    <td><code>mh_cg_ibqr</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/ibqr">ECBQ (VSF)+BI</a></td>
    <td><code>mh_cg_ecbq</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/maps-tl">MAPS-TL</a> <span class="subtle">(Infant/Toddler)</span>
    </td>
    <td>Irritability</td>
    <td><code>mh_cg_mapdb__inf</code> / <code>mh_cg_mapstl__tod</code></td>
  </tr>
  </tbody>
  </table>


### <i class="fa fa-vial header-icon"></i> Biospecimen & Omics
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Instrument</th>
<th>Construct</th>
<th>Table / Folder Name</th>
</tr>
</thead>
<tbody>
<tr>
    <td><a href="biospec/illumina-gda-gwas">Illumina GDA GWAS</a></td>
    <td>GWAS, EWAS, Transcriptome</td>
    <td><i>concatenated/genetics/</i></td>
</tr>
<tr>
    <td><a href="biospec/nails">Maternal Nails</a></td>
    <td>Drug, Environmental Exposure</td>
    <td><code>bio_bm_biosample_nails_<span class="blue-text">{results|type}</span></code></td>
</tr>
<tr>
    <td><a href="biospec/urine">Maternal Urine</a></td>
    <td>Drug Panel, Toxins</td>
    <td><code>bio_bm_biosample_urine_results</code></td>
</tr>
<tr>
    <td><a href="biospec/olink">Olink Explore</a></td>
    <td>Maternal Inflammation</td>
    <td><i>concatenated/proteins/</i></td>
</tr>
</tbody>
</table>

### <i class="fa-solid fa-file-waveform header-icon"></i> EEG
The EEG datasets include task data from Auditory Mismatch Negativity (MMN), Faces (FACE), Visual Evoked Potential (VEP), and Video Resting State (RS). File-based EEG data include raw BIDS and HBCD-MADE pipeline derivatives; see <a href="eeg/release-data/">Release Data</a> for details. Tabular EEG data includes tabulated pipeline derivatives, acquisition forms, and quality-control metrics:
<table class="compact-table-no-vertical-lines wide-name-col">
<thead>
<tr>
<th>Table</th>
<th>Construct</th>
<th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="2">HBCD-MADE tabulated derivatives</td>
  <td>Processing Reports</td>
  <td><code>eeg_made_task-<span class="blue-text">{FACE|MMN|RS|VEP}</span>_acq-eeg_preprocessingReport</code></td>
</tr>
<tr>
  <td>Summary Statistics</td>
  <td><code>eeg_made_task-<span class="blue-text">{FACE|MMN|VEP}</span>FACE_ERPSummaryStats</code></td>
</tr>
<tr>
  <td>EEG Acquisition Checklists</td>
  <td>Acquisition Prep</td>
  <td><code>eeg_ch_<span class="blue-text">{chkl|chkl_1|chkl_2}</span></code></td>
</tr>
<tr>
  <td><a href="eeg/qc">Quality Control Metrics</a></td>
  <td>Quality Control</td>
  <td><code>eeg_qc_task-<span class="blue-text">{FACE|MMN|RS|VEP}</span></code>
  </td>
</tr>
</tbody>
</table>


### <i class="fa fa-brain header-icon"></i> Imaging
Imaging includes Magnetic Resonance Imaging (structural, functional, quantitative, and diffusion MRI) as well as MR Spectroscopy (MRS) datasets. File-based data include raw BIDS and pipeline derivatives; see [Release Data](mri/release-data.md) for details. Tabular Imaging includes tabulated pipeline derivatives, questionnaire/form data, and quality-control metrics:

<div class="table-legend">
  <span class="legend-item">
    <i class="fa-solid fa-diagram-project legend-icon"></i>
    Tabulated pipeline derivatives
  </span>
</div>

<table class="compact-table-no-vertical-lines wide-name-col"> 
<thead>
<tr>
  <th>Table</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<a href="mri/smri/#bibsnet">BIBSNet</a><i class="fa-solid fa-diagram-project simple-icon" title="Tabulated pipeline derivative"></i></td>
  <td>Brain ROI Volumes</td>
  <td><code>img_bibsnet_space-<span class="blue-text">{T1w|T2w}</span>_desc-aseg_volumes</code></td>
</tr>
<tr>
  <td><a href="mri/qc/#brainswipes">BrainSwipes</a></td>
  <td>Manual QC</td>
  <td><code>img_brainswipes_xcpd_hash-<span class="blue-text">{HASH}</span>_<span class="blue-text">{T1w/T2w|bold}</span></code><br>
    <!-- <code>img_brainswipes_xcpd_hash-d902942d+7a4c379b_<span class="blue-text">{T2w|bold}</span></code><br>
    <code>img_brainswipes_xcpd_hash-364caa63+7a4c379b_<span class="blue-text">{T1w|bold}</span></code> -->
  </td>
</tr>
<tr>
  <td><a href="mri/smri/#mriqc">MRIQC</a><i class="fa-solid fa-diagram-project simple-icon" title="Tabulated pipeline derivative"></i></td>
  <td>Raw BIDS QC Metrics</td>
  <td><code>img_mriqc_<span class="blue-text">{T1w|T2w|bold}</span></code></td>
</tr>
<tr>
  <td><a href="mri/mri-forms/#mri-scan-session-data-summary-forms">MRI Summary Forms</a></td>
  <td>Pre/Post-Scan Checklists</td>
  <td><code>mri_ra_chkl_scan</code> / <code>mri_ra_chkl_data</code></td>
</tr>
<tr>
  <td><a href="mri/mrs/#derivatives">OSPREY-BIDS</a><i class="fa-solid fa-diagram-project simple-icon" title="Tabulated pipeline derivative"></i></td>
  <td>Metabolites</td>
  <td>
    <code>img_osprey_<span class="blue-text">{HERCULES|unedited}</span>_*</code>
    <a href="mri/tables/osprey.html">→ View full file list</a>
  </td>
</tr>
<tr>
  <td><a href="mri/mri-forms/#pre-scan-questionnaire">Pre-Scan Questionnaire</a></td>
  <td>Infant Sleep Environment</td>
  <td><code>mri_ra_prep</code></td>
</tr>
<tr>
  <td><a href="mri/dmri/#qsiprep">QSIPrep</a><i class="fa-solid fa-diagram-project simple-icon" title="Tabulated pipeline derivative"></i></td>
  <td>QSIPrep QC Metrics</td>
  <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td> 
</tr>
<tr> 
  <td><a href="mri/fmri/#xcp-d">XCP-D</a><i class="fa-solid fa-diagram-project simple-icon" title="Tabulated pipeline derivative"></i></td>
  <td>Morph/fMRI metrics</td>
  <td>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-*</code> <a href="mri/tables/xcpd.html">→ View full file list</a>
  </td>
</tr>
</tbody>
</table>

### <i class="fa-solid fa-puzzle-piece header-icon"></i> Neurocognition & Language

<div class="table-legend">
  <span class="legend-item">
    <i class="fa-solid fa-language legend-icon"></i>
    Spanish version available
  </span>
</div>

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
  <th>Instrument</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="neurocog/bayley-4">Bayley-4 Scales</a></td>
  <td>Child Development (Cognitive, Language, Motor)</td>
  <td><code>ncl_ch_bayley</code></td>
</tr>
<tr>
  <td><a href="neurocog/mbcdi">MacArthur-Bates CDI-I</a><i class="fa-solid fa-language table-icon"></i>
</td>
  <td>Language Development (Words & Gestures)</td>
  <td><code>ncl_ch_cdiwgen</code> / <code>ncl_ch_cdiwges</code></td>
</tr>
<tr>
  <td><a href="neurocog/mlds">MLDS</a></td>
  <td>Multilingual Exposure</td>
  <td><code>ncl_ch_mlds</code></td>
</tr>
<tr>
  <td><a href="neurocog/spm2">SPM-2</a> <span class="subtle">(Infant/Toddler)</span>
  </td>
  <td>Sensory Processing/Integration</td>
  <td><code>ncl_cg_spm2__inf</code> / <code>ncl_cg_spm2__tod</code></td>
</tr>
<tr>
  <td><a href="neurocog/vineland">Vineland</a></td>
  <td>Adaptive Behavior</td>
  <td><code>ncl_cg_vabs</code></td>
</tr>
</tbody>
</table>



### <i class="fa fa-microchip header-icon"></i> Novel Technologies & Wearable Sensors
Wearable sensor data includes raw BIDS and processed <a href="sensors/wearsensors/#derivatives">HBCD-Motion</a> pipeline derivatives - see [Release Data](sensors/wearsensors.md#release-data) for details. Tabulated data includes questionnaires and sensor checklists:

<table class="compact-table-no-vertical-lines"> 
<thead>
<tr>
<th>Instrument</th>
<th>Construct</th>
<th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="sensors/questionnaire">Infant Sensor Questionnaires</a></td>
<td>Motor Development, Regulation (Sleep/Wake)</td>
<td><code>nt_ch_sens__qtn_<span class="blue-text">{1|2|3}</span></code></td>
</tr>
<tr>
<td>Biosensor Receipt / Setup</td>
<td>Administrative</td>
<td><code>nt_ch_sens_rcpt</code> / <code>nt_ch_sens_setup</code></td>
</tr>
</tbody>
</table>

### <i class="fas fa-id-card header-icon"></i> Participant Derived
<table class="compact-table-no-vertical-lines" style="width: 100%;">
<thead>
<tr>
<th>Instrument</th>
<th>Construct</th>
<th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="demo/dynamic/">Dynamic Participant Information</a></td>
  <td>Dynamic derived participant information</td>
  <td><code>par_gd_dyn</code></td>
</tr>
<tr>
  <td><a href="demo/static/">Static Participant Information</a></td>
  <td>Static derived participant information</td>
  <td><code>par_gd_stc</code></td>
</tr>
</tbody>
</table>

### <i class="fa fa-heart-pulse header-icon"></i> Physical Health
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
  <th>Instrument</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="physhealth/growth">Anthropometrics</a></td>
  <td>Growth</td>
  <td><code>ph_ch_anthro</code></td>
</tr> 
<tr>
  <td><a href="physhealth/bf">Breast Feeding History</a></td>
  <td>Nutrition</td>
  <td><code>ph_cg_phx__bfh</code></td>
</tr>
<tr>
  <td><a href="physhealth/bisq-sf">Brief Infant Sleep Questionnaire</a></td>
  <td>Sleep</td>
  <td><code>ph_cg_bisq</code></td>
</tr>
<tr>
  <td><a href="physhealth/ecpromis-pags">ecPROMIS Physical Activity</a></td>
  <td>Physical Activity / Greenspace</td>
  <td><code>ph_cg_pms__pags</code></td>
</tr> 
<tr>
  <td><a href="physhealth/ecpromis-sleep">ecPROMIS Sleep</a></td>
  <td>Sleep</td>
  <td><code>ph_cg_pms__sleep</code></td>
</tr>
<tr>
  <td><a href="physhealth/medical-history">Medical History</a></td>
  <td>Medical History</td>
  <td><code>ph_cg_ecls__medhist</code></td>
</tr>
<tr>
  <td><a href="physhealth/nutrition">Nutrition Questionnaire</a></td>
  <td>Nutrition</td>
  <td><code>ph_cg_inq</code></td>
</tr>
<tr>
  <td><a href="physhealth/screenq">ScreenQ</a></td>
  <td>Media Use</td>
  <td><code>ph_cg_screenq</code></td>
</tr>
<tr>
  <td><a href="physhealth/vision">Vision Screener</a></td>
  <td>Vision</td>
  <td><code>ph_ch_vs</code></td>
</tr>
</tbody>
</table>

### <i class="fa-solid fa-baby header-icon"></i> Pregnancy & Exposure, Including Substance Use
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
  <th>Instrument</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<!-- Pregnancy & Infant Health -->
<tr class="table-group-row">
  <td colspan="3"> [ Pregnancy & Infant Health ]</td>
</tr>
<tr>
  <td><a href="pregexp/pex/">Health V1-Health History</a></td>
  <td>Pre-pregnancy and pregnancy health</td>
  <td><code>pex_bm_health_preg__healthhx</code></td>
</tr>
<tr>
  <td><a href="pregexp/pex/">Health V1-Exp & Vaccines</a></td>
  <td>Vaccines in pregnancy</td>
  <td><code>pex_bm_health_preg__exp__vacc</code></td>
</tr>
<tr>
  <td><a href="pregexp/pex/">Health V1-Chronic Conditions</a></td>
  <td>Chronic conditions/STIs in pregnancy</td>
  <td><code>pex_bm_health_preg__chroncond</code></td>
</tr>
<tr>
  <td><a href="pregexp/pex/">Health V1-Illness</a></td>
  <td>Illness in pregnancy</td>
  <td><code>pex_bm_health_preg__illness</code></td>
</tr>
<tr>
  <td><a href="pregexp/pex/">Health V1-ER Admissions</a></td>
  <td>ER visit or hospitalization in pregnancy</td>
  <td><code>pex_bm_health_preg__erhosp</code></td>
</tr>
<tr>
  <td><a href="pregexp/pex/">Health V1-Medications</a></td>
  <td>Medications in pregnancy</td>
  <td><code>pex_bm_health_preg__meds</code></td>
</tr>
<tr>
  <td><a href="pregexp/pex/">Health V2-Pregnancy</a></td>
  <td>Health updates up to delivery</td>
  <td><code>pex_bm_healthv2_preg</code></td>
</tr>
<tr>
  <td><a href="pregexp/pex/">Health V2-Infancy</a></td>
  <td>Delivery and birth outcomes</td>
  <td><code>pex_bm_healthv2_inf</code></td>
</tr>

<!-- MENTAL HEALTH -->
<tr class="table-group-row">
  <td colspan="3">[ Mental Health ]</td>
</tr>
<tr>
  <td><a href="pregexp/mh/fam-mh">FAM MH</a></td>
  <td>Personal and Family Mental Health</td>
  <td><code>pex_bm_psych</code></td>
</tr>
<tr>
  <td><a href="pregexp/mh/apa12">APA 1/2</a></td>
  <td>Mental Health</td>
  <td><code>pex_bm_apa</code></td>
</tr>
<tr>
  <td><a href="pregexp/mh/ptsd">DSM5 Acute Stress or PTSD</a></td>
  <td>PTSD/Acute Stress Symptom Severity</td>
  <td><code>pex_bm_str__ptsd</code></td>
</tr>
<tr>
  <td><a href="pregexp/mh/epds">EPDS</a></td>
  <td>Postnatal Depression</td>
  <td><code>pex_bm_epds</code></td>
</tr>

<!-- Substance Use -->
<tr class="table-group-row">
  <td colspan="3"> [ Substance Use ] </td>
</tr>
<tr class="section-su">
  <td><a href="pregexp/su/assist">ASSIST V1/2/3/4</a></td>
  <td>Substance Use Pre-, During, and Post-Pregnancy</td>
  <td><code>pex_bm_assistv<span class="blue-text">{1|2|3|4}</span></code></td>
</tr>
<tr class="section-su">
  <td><a href="pregexp/su/su-patterns">Substance Use Patterns</a></td>
  <td>Substance Use in Pregnancy</td>
  <td><code>pex_bm_subst</code></td>
</tr>
<tr class="section-su">
  <td><a href="pregexp/su/tlfb">TLFB</a></td>
  <td>Substance Use Before and During Pregnancy</td>
  <td><code>pex_ch_tlfb</code></td>
</tr>
</tbody>
</table>

### <i class="fas fa-city header-icon"></i> Social & Environmental Determinants
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
  <th>Instrument</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="SED/aces">ACES</a>  <span class="subtle">(Adult/Pediatric)</td>
  <td>Adverse Childhood Experiences</td>
  <td><code>sed_cg_ace</code> / <code>sed_cg_pedaces</code></span>
  </td>
</tr>  
<tr>
  <td><a href="SED/bfy">Baby's First Years (BFY)</a></td>
  <td>Benefits/Services/Economic Stress</td>
  <td><code>sed_bm_bfy</code></td>
</tr>
<tr>
  <td><a href="SED/cab">Composite Abuse Scale (CABr-SF)</a></td>
  <td>Intimate Partner Violence</td>
  <td><code>sed_cg_cabr_sf</code></td>
</tr>
<tr>
  <td><a href="SED/current-employment">Current Employment</a></td>
  <td>Current Employment</td>
  <td><code>sed_cg_employ</code></td>
</tr>  
<tr>
  <td><a href="SED/demo-cg">Demographics</a></td>
  <td>Adult Demographics</td>
  <td><code>sed_bm_demo</code></td>
</tr> 
<tr>
  <td><a href="SED/demo-ch">Child Demographics</a></td>
  <td>Child Demographics</td>
  <td><code>sed_bm_demo_child</code></td>
</tr> 
<tr>
  <td><a href="SED/ehits">eHITS</a></td>
  <td>Intimate Partner Violence</td>
  <td><code>sed_bm_ehits</code></td>
</tr>  
<tr>
  <td><a href="SED/foodinsecurity">Food Insecurity</a></td>
  <td>Food insecurity</td>
  <td><code>sed_cg_foodins</code></td>
</tr>
<tr>
  <td><a href="SED/geocoded-linkage">Geocoded Linkage</a></td>
  <td>Neighborhood Measures</td>
  <td><i>concatenated/geocoding/</i></td>
</tr>  
<tr>
  <td><a href="SED/home21">HOME-21</a></td>
  <td>Child’s Home Environment</td>
  <td><code>sed_cg_home_it</code></td>
</tr>
<tr>
  <td><a href="SED/household-chemical-exposures">Household Chemical Exposures</a></td>
  <td>Household Chemical Exposures</td>
  <td><code>sed_cg_hce</code></td>
</tr>   
<tr>
  <td><a href="SED/lead-exposures">Lead Exposures</a></td>
  <td>Lead Exposures</td>
  <td><code>sed_cg_leadexp</code></td>
</tr> 
<tr>
  <td><a href="SED/safety">Neighborhood Safety</a></td>
  <td>Neighborhood Safety</td>
  <td><code>sed_bm_nbhsaf</code></td>
</tr> 
<tr>
  <td><a href="SED/paces">PACEs</a></td>
  <td>Protective Factors</td>
  <td><code>sed_bm_paces</code> / <code>sed_cg_paces</code><br>
  </td>
</tr>
<tr>
  <td><a href="SED/promis">PROMIS</a></td>
  <td>Perceived Stress/Social Support</td>
  <td><code>sed_bm_strsup</code></td>
</tr>      
<tr>
  <td><a href="SED/second-hand-smoke-exposure">Second Hand Smoke</a></td>
  <td>Second Hand Smoke Exposure</td>
  <td><code>sed_cg_shs</code></td>
</tr>    
<tr>
  <td><a href="SED/transitions-in-care">Transitions in Care Screener</a></td>
  <td>Recruitment/Retention</td>
  <td><code>sed_cg_tic_screener</code></td>
</tr>
<tr>
  <td><a href="SED/discr">Unfair Treatment</a></td>
  <td>Experiences of Unfair Treatment</td>
  <td><code>sed_bm_phx__discr</code></td>
</tr>  
<tr>
  <td><a href="SED/vi">Vancouver Index (VIA)</a></td>
  <td>Acculturation</td>
  <td><code>sed_cg_via</code></td>
</tr>      
</tbody>
</table>






<script>
document.addEventListener("DOMContentLoaded", function () {
  const container = document.querySelector(".wy-nav-content") || document.body;

  const searchInput = document.getElementById("instr-search");
  const domainSelect = document.getElementById("instr-domain");
  const resetButton = document.getElementById("instr-reset");
  const status = document.getElementById("instr-status");
  const emptyMessage = document.getElementById("instr-empty");

  if (!searchInput) return;

  function normalize(value) {
    return value.toLowerCase().replace(/\s+/g, " ").trim();
  }

  function cleanHeadingText(heading) {
    const clone = heading.cloneNode(true);
    clone.querySelectorAll(".headerlink, i").forEach(el => el.remove());
    return clone.textContent.replace(/ /g, " ").replace(/\s+/g, " ").trim();
  }

  // Walk the page in document order, pairing each h3 domain heading with the
  // table that follows it.
  const flow = Array.from(
    container.querySelectorAll("h3, table.compact-table-no-vertical-lines")
  );

  const sections = [];

  flow.forEach((el, i) => {
    if (el.tagName !== "H3") return;

    let j = i + 1;
    while (j < flow.length && flow[j].tagName === "H3") j++;
    const table = j < flow.length && flow[j].tagName === "TABLE" ? flow[j] : null;
    if (!table) return;

    // The ReadTheDocs theme's own JS wraps every <table> in a
    // ".wy-table-responsive" div at runtime, so the table itself is not
    // necessarily a direct sibling of the heading. Walk up from the table to
    // whichever ancestor-or-self IS that sibling, so hiding it doesn't leave
    // the wrapper's own margin behind. Doing this lazily (not once at setup)
    // means it stays correct however late that wrapping happens.
    function outerTableContainer() {
      let node = table;
      while (node.parentElement && node.parentElement !== el.parentElement) {
        node = node.parentElement;
      }
      return node;
    }

    // Collect any intro text/notes between the heading and its table so they
    // hide/show together with the section.
    const extras = [];
    let node = el.nextElementSibling;
    while (node && !node.contains(table)) {
      extras.push(node);
      node = node.nextElementSibling;
    }

    sections.push({
      heading: el,
      table,
      outerTableContainer,
      extras,
      domain: cleanHeadingText(el),
    });
  });

  sections.forEach(section => {
    domainSelect.add(new Option(section.domain, section.domain));
  });

  // Group table rows so that rowspan blocks and "table-group-row" sub-headers
  // stay intact and are shown/hidden as a unit rather than row-by-row.
  function buildRowGroups(table) {
    const rows = Array.from(table.querySelectorAll("tbody > tr"));
    const groups = [];
    let i = 0;
    while (i < rows.length) {
      const row = rows[i];
      if (row.classList.contains("table-group-row")) {
        groups.push({ type: "header", rows: [row] });
        i++;
        continue;
      }
      let span = 1;
      row.querySelectorAll("td[rowspan]").forEach(td => {
        const n = parseInt(td.getAttribute("rowspan"), 10);
        if (!Number.isNaN(n) && n > span) span = n;
      });
      groups.push({ type: "data", rows: rows.slice(i, i + span) });
      i += span;
    }
    return groups;
  }

  function filterTable(table, search) {
    const groups = buildRowGroups(table);
    let visibleCount = 0;
    let pendingHeader = null;
    let headerHasVisible = false;

    function flushHeader() {
      if (pendingHeader) {
        pendingHeader.rows.forEach(r => (r.style.display = headerHasVisible ? "" : "none"));
      }
    }

    groups.forEach(group => {
      if (group.type === "header") {
        flushHeader();
        pendingHeader = group;
        headerHasVisible = false;
        return;
      }

      const text = normalize(group.rows.map(r => r.textContent).join(" "));
      const show = !search || text.includes(search);
      group.rows.forEach(r => (r.style.display = show ? "" : "none"));
      if (show) {
        visibleCount += group.rows.length;
        headerHasVisible = true;
      }
    });

    flushHeader();
    return visibleCount;
  }

  function applyFilters() {
    const search = normalize(searchInput.value);
    const domain = domainSelect.value;

    let totalVisible = 0;
    let domainsVisible = 0;

    sections.forEach(section => {
      const container = section.outerTableContainer();

      if (domain && section.domain !== domain) {
        section.heading.style.display = "none";
        container.style.display = "none";
        section.extras.forEach(el => (el.style.display = "none"));
        return;
      }

      const sectionMatchesSearch = !search || normalize(section.domain).includes(search);

      const visible = filterTable(section.table, sectionMatchesSearch ? "" : search);
      const showSection = visible > 0;

      section.heading.style.display = showSection ? "" : "none";
      container.style.display = showSection ? "" : "none";
      section.extras.forEach(el => (el.style.display = showSection ? "" : "none"));

      if (showSection) domainsVisible++;
      totalVisible += visible;
    });

    status.textContent =
      `Showing ${totalVisible} instrument${totalVisible === 1 ? "" : "s"} across ${domainsVisible} domain${domainsVisible === 1 ? "" : "s"}.`;
    emptyMessage.style.display = totalVisible === 0 ? "block" : "none";
  }

  [searchInput, domainSelect].forEach(control => {
    control.addEventListener("input", applyFilters);
    control.addEventListener("change", applyFilters);
  });

  resetButton.addEventListener("click", function () {
    searchInput.value = "";
    domainSelect.value = "";
    applyFilters();
  });

  applyFilters();
});
</script>