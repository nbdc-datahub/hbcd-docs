<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
.blue-text {
  color: #2563eb;
}
</style>

# Study Instruments

This page lists all instruments included in the current release, organized by domain. Each instrument links to a separate README page containing instrument documentation, including, where applicable, details of implementation and data collection, quality control procedures, data and responsible use warnings, scoring procedures, and references. Study protocols are also available on the [HBCD Study site](https://hbcdstudy.org/study-protocols/). 

---

## Behavior, Biology, & Environment

<div class="infobox">
  <strong>The following domains provide most of the tabulated data and ALL concatenated data included in the release.</strong>
  <p>For the small number of concatenated datasets, the folder name is provided in the summary tables below in place of table names. 
    See <a href="../datacuration/overview/">Data Structure Overview</a> for an overview of release data types.</p>
</div>


###### <i class="fa fa-clipboard-list header-icon"></i> Administrative &nbsp;/ &nbsp; <i class="fas fa-id-card header-icon"></i> Demographics

<table class="compact-table-no-vertical-lines" style="width: 100%;">
<thead>
<th>Domain</th>
<th>Instrument</th>
<th>Construct</th>
<th>Table / Folder Name</th>
</thead>
<tbody>
<tr>
<td style="color: #6b7280;"><b>ADMINISTRATIVE</b></td>
<td><a href="admin/study-navigators">Study Navigator Contact Form</a></td>
<td>Recruitment/Retention</td>
<td><i>concatenated/study_navigator/</i></td>
</tr>
<tr>
  <td style="color: #6b7280;" rowspan="2"><b>DEMOGRAPHICS</b></td>
  <td><a href="demo/basicdemo/">Basic Demographics</a></td>
  <td>Derived Demographics</td>
  <td><code>sed_basic_demographics</code></td>
</tr>
  <tr>
  <td><a href="demo/visitinfo/">Visit Level Data</a></td>
  <td>Participant visit information</td>
  <td><code>par_visit_data</code></td>
</tr>
</tbody>
</table>


###### <i class="fa fa-people-arrows header-icon"></i> Behavior & Caregiver-Child Interaction
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
      <a href="bcgi/ecpromis">ecPROMIS Caregiver-Child</a> 
      </td>
    <td>Caregiver-Child Interactions</td>
    <td><code>mh_cg_pms__cc__inf</code> <span class="subtle">(&lt;1 year)</span> /
    <code>mh_cg_pms__cc__1to5</code> <span class="subtle">(1-5 years)</span></td>
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
      Surgency/Extraversion,<br>
      Negative Affectivity,<br>
      Effortful Control,<br>
      Behavioral Inhibition
      </td>
    <td><code>mh_cg_ibqr</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/ibqr">ECBQ (VSF)+BI</a></td>
    <td><code>mh_cg_ecbq</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/maps-tl">MAPS-TL</a>
    </td>
    <td>Irritability</td>
    <td>
    <code>mh_cg_mapdb__inf</code> <span class="subtle">(Infant)</span> /
    <code>mh_cg_mapstl__tod</code> <span class="subtle">(Toddler)</span>
    </td>
  </tr>
  </tbody>
  </table>


###### <i class="fa fa-vial header-icon"></i> Biospecimen & Omics
<table class="compact-table-no-vertical-lines">
<thead>
<th>Instrument</th>
<th>Construct</th>
<th>Table / Folder Name</th>
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
    <td><code>bio_bm_biosample_nails_results</code> / <code>bio_bm_biosample_nails_type</code></td>
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

###### <i class="fa-solid fa-puzzle-piece header-icon"></i> Neurocognition & Language
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
  <td>Child Development (Cognitive, Language, and Motor)</td>
  <td><code>ncl_ch_bayley</code></td>
</tr>
<tr>
  <td><a href="neurocog/macarthur-bates">MacArthur-Bates CDI-I</a>
</td>
  <td>Language Development (Words & Gestures)</td>
  <td><code>ncl_ch_cdiwgen</code> <span class="subtle">(English)</span> /
  <code>ncl_ch_cdiwges</code> <span class="subtle">(Spanish)</span>  
  </td>
</tr>
<tr>
  <td><a href="neurocog/mlds">MLDS</a></td>
  <td>Multilingual Exposure</td>
  <td><code>ncl_ch_mlds</code></td>
</tr>
<tr>
  <td><a href="neurocog/spm2">SPM-2</a>
  </td>
  <td>Sensory Processing/Integration</td>
  <td><code>ncl_cg_spm2__inf</code> <span class="subtle">(Infant)</span> / <code>ncl_cg_spm2__tod</code> <span class="subtle">(Toddler)</span></td>
</tr>
<tr>
  <td><a href="neurocog/vineland">Vineland</a></td>
  <td>Adaptive Behavior</td>
  <td><code>ncl_cg_vabs</code></td>
</tr>
</tbody>
</table>

###### <i class="fa fa-heart-pulse header-icon"></i> Physical Health
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
  <td><a href="physhealth/ecpromis-pags">ecPROMIS Physical Activity/Greenspace</a></td>
  <td>Physical Activity</td>
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

###### <i class="fa-solid fa-baby header-icon"></i> Pregnancy & Exposure, Including Substance Use
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



###### <i class="fas fa-city header-icon"></i> Social & Environmental Determinants
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
  <td><a href="SED/aces">ACES</a></td>
  <td>Adverse Childhood Experiences</td>
  <td><code>sed_cg_ace</code> / <code>sed_cg_pedaces</code> <span class="subtle">(Pediatric ACES)</span>
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
  <td><code>sed_bm_paces</code> <span class="subtle">(Current)</span> / <code>sed_cg_paces</code> <span class="subtle">(Retrospective &lt;18)</span><br>
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

## Brain Activity & Biosensors

<div class="infobox">
  <strong>The following domains are the source of ALL file-based raw BIDS and processed derivatives in the release.</strong>
  <p>Associated tabulated data include tabulated pipeline derivatives (<a href="../datacuration/overview/#tabulated-pipeline-derivatives">see details</a>), participant questionnaires, and session/acquisition forms filled out by technicians. See <a href="../datacuration/overview/">Data Structure Overview</a> for an overview of release data types.</p>
</div>

###### <i class="fa-solid fa-file-waveform header-icon"></i> EEG / Tabular EEG
<p></p>
The EEG datasets include task data from Auditory Mismatch Negativity (MMN), Faces (FACE), Visual Evoked Potential (VEP), and Video Resting State (RS). File-based EEG data include raw BIDS and HBCD-MADE pipeline derivatives; see <a href="eeg/release-data/">Release Data</a> for details. Tabular EEG data includes tabulated pipeline derivatives, acquisition forms, and quality-control metrics:
<table class="compact-table-no-vertical-lines">
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
  <td><code>eeg_ch_chkl</code>, 
  <code>eeg_ch_chkl_1</code>,
  <code>eeg_ch_chkl_2</code></td>
</tr>
<tr>
  <td><a href="eeg/qc">Quality Control Metrics</a></td>
  <td>Quality Control</td>
  <td><code>eeg_qc_task-<span class="blue-text">{FACE|MMN|RS|VEP}</span></code>
  </td>
</tr>
</tbody>
</table>

###### <i class="fa fa-brain header-icon"></i> Imaging / Tabular Imaging
<p></p>
Imaging includes Magnetic Resonance Imaging (structural, functional, quantitative, and diffusion MRI) as well as MR Spectroscopy (MRS) datasets. File-based data include raw BIDS and pipeline derivatives; see [Release Data](mri/release-data.md) for details. Tabular Imaging includes tabulated pipeline derivatives (<i class="fa-solid fa-gear simple-icon"></i>), questionnaire/form data, and quality-control metrics:
<table class="compact-table-no-vertical-lines"> 
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
<a href="mri/sfmri-processing/#bibsnet">BIBSNet</a><i class="fa-solid fa-gear simple-icon" title="Tabulated pipeline derivative"></i></td>
  <td>Brain ROI Volumes</td>
  <td><code>img_bibsnet_space-<span class="blue-text">{T1w|T2w}</span>_desc-aseg_volumes</code></td>
</tr>
<tr>
  <td><a href="mri/qc/#brainswipes">BrainSwipes</a></td>
  <td>Manual QC</td>
  <td>
    <code>img_brainswipes_xcpd_hash-0f306a2f+0ef9c88a_<span class="blue-text">{T2w|bold}</span></code><br>
    <code>img_brainswipes_xcpd_hash-2afa9081+0ef9c88a_<span class="blue-text">{T1w|bold}</span></code>
  </td>
</tr>
<tr>
  <td><a href="mri/sfmri-processing/#mriqc">MRIQC</a><i class="fa-solid fa-gear simple-icon" title="Tabulated pipeline derivative"></i></td>
  <td>Raw BIDS QC Metrics</td>
  <td><code>img_mriqc_<span class="blue-text">{T1w|T2w|bold}</span></code></td>
</tr>
<tr>
  <td><a href="mri/mri-forms/#mri-scan-session-data-summary-forms">MRI Summary Forms</a></td>
  <td>Pre/Post-Scan Checklists</td>
  <td><code>mri_ra_chkl_scan</code> / <code>mri_ra_chkl_data</code></td>
</tr>
<tr>
  <td><a href="mri/mrs/#derivatives">OSPREY-BIDS</a><i class="fa-solid fa-gear simple-icon" title="Tabulated pipeline derivative"></i></td>
  <td>Metabolites</td>
  <td>
    <code>img_osprey_<span class="blue-text">{HERCULES|unedited}</span>_*</code>
    <a href="mri/tables/osprey.html">→ View full file list &amp; details</a>
  </td>
</tr>
<tr>
  <td><a href="mri/mri-forms/#pre-scan-questionnaire">Pre-Scan Questionnaire</a></td>
  <td>Infant Sleep Environment</td>
  <td><code>mri_ra_prep</code></td>
</tr>
<tr>
  <td><a href="mri/dmri/#qsiprep">QSIPrep</a><i class="fa-solid fa-gear simple-icon" title="Tabulated pipeline derivative"></i></td>
  <td>QSIPrep QC Metrics</td>
  <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td> 
</tr>
<tr> 
  <td><a href="mri/sfmri-processing/#xcp-d">XCP-D</a><i class="fa-solid fa-gear simple-icon" title="Tabulated pipeline derivative"></i></td>
  <td>Morph/fMRI metrics</td>
  <td>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-mean_desc-<span class="blue-text">{METRIC}</span>_morph</code>
    <br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-<span class="blue-text">{alff|coverage|reho}</span>_bold</code>
    <br>
    &nbsp;&nbsp;<a href="mri/tables/xcpd.html">→ View full file list &amp; details</a>
  </td>
</tr>
</tbody>
</table>

###### <i class="fa fa-microchip header-icon"></i> Novel Technologies & Wearable Sensors
<p></p>
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
<td><a href="sensors/questionnaire">Infant Sensor Questionnaire 1/2/3</a></td>
<td>Motor Development, Regulation (Sleep/Wake) <i>(Day 1/2/3)</i></td>
<td><code>nt_ch_sens__qtn_<span class="blue-text">{1|2|3}</span></code></td>
</tr>
<tr>
<td>Biosensor Receipt / Setup</td>
<td>Administrative</td>
<td><code>nt_ch_sens_rcpt</code> / <code>nt_ch_sens_setup</code></td>
</tr>
</tbody>
</table>











<!-- ##### Data types included in this section

The following study domains are the **source of all file-based raw BIDS and processed derivatives** (see full list of processing pipelines <a href="../standards/processing/">here</a>) data provided in the release. There are also some tabulated data, including <a href="../datacuration/overview/#tabulated-pipeline-derivatives">tabulated pipeline derivatives</a>, participant questionnaires, and session/acquisition forms filled out by technicians. See <a href="../datacuration/overview/">Data Structure Overview</a> for an overview of different data types.
 -->