# Study Instruments
The current release includes data from **Visits 1, 2, and 3 (V01, V02, and V03)** for the majority of measures. In this section we provide a brief overview of each study instrument provided in the data release, including, where applicable, details of implementation and data collection, scoring procedures, quality control procedures, known issues, and references. Full study protocols are available on the [HBCD Study site](https://hbcdstudy.org/study-protocols/). See [Upcoming Updates](../changelog/pending.md) for details on what to expect in future releases.

<p>
<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text">All surveys used in the HBCD Study were translated to Spanish by <a href="https://burgtranslations.com/our-services/">BURG Translations</a></span>
</div>
</p>

<img src="https://hbcdstudy.org/wp-content/uploads/2025/03/HBCD_Timeline_March2025_Updated.png" width="90%" height="auto" class="center">

HBCD Study data includes both tabulated and file-based data - see <a href="../datacuration/overview" target="_blank">Data Structure Overview</a> for details. In summary:

- <a href="../datacuration/phenotypes" target="_blank"><b>Tabulated data</b></a> contain data across all participants in a standardized [tabulated format](../datacuration/phenotypes.md/#table-organization) for HBCD. This includes data for behavior, demographics, toxicology, data derived from MRI and other file-based data, etc.
- File-based data include <a href="../datacuration/rawbids" target="_blank"><b>raw</b></a> and <a href="../datacuration/derivatives" target="_blank"><b>processed derivative</b></a> data for MRI/MRS and EEG, and wearable sensors. The files are organized under subject/session-level folders and are in varied modality-specific formats.

Expand the sections below to see a list of measures associated with each domain included in Release 1.0.

## Instruments by Domain

<div class="warning-static-banner">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text">Click <i>domain headers</i> (e.g., <i>Biospecimen & Omics</i>) to expand and view domain measures.<br>
  Click <i>instrument names</i> (e.g., <i>Nails</i>) to access detailed instrument documentation.</span>
</div>
<br>
<button id="toggle-all-btn" style="
  padding: 6px 12px;
  font-size: 1em;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
  background-color: #ffe10042;
">
  Expand All Sections ↕️
</button>

### Behavior, Biology, & Environment

<div id="bcgi" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-people-arrows"></i></span>
  <span class="text-with-link">
  <span class="text">Behavior & Caregiver-Child Interaction</span>
  <a class="anchor-link" href="#bcgi" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 20%;">Instrument</th>
      <th>Version</th>
      <th style="width: 50%;">Construct</th>
      <th style="width: 10%;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="bcgi/ecpromis" target="_blank">ecPROMIS-Ch/CG Interaction</a></td>
    <td>&lt;1 year</td>
    <td>Child/Caregiver Relationship</td>
    <td><code>mh_cg_pms__cc__inf</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/ibqr" target="_blank">BQ (VSF)+BI</a></td>
    <td>IBQ-R (VSF)+BI (<i>Infant</i>)</td>
    <td style="word-wrap: break-word; white-space: normal;">Surgency/Extraversion, Negative Affectivity, Effortful Control, Behavioral Inhibition</td>
    <td><code>mh_cg_ibqr</code></td>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="bcgi/maps-tl" target="_blank">MAPS-TL</a></td>
    <td>Infancy (< 1 year)</td>
    <td>Irritability</td>
    <td><code>mh_cg_mapdb__inf</code></td>
  </tr>
  </tbody>
  </table>
</div>

<div id="biospec" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-vial"></i></span>
  <span class="text-with-link">
  <span class="text">Biospecimen & Omics</span>
  <a class="anchor-link" href="#biospec" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 10%;">Instrument</th>
      <th>Version</th>
      <th style="width: 40%;">Construct</th>
      <th style="width: 20%;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td style="text-align: left;"><a href="biospec/nails" target="_blank">Nails</a></td>
    <td style="text-align: left;">Maternal</td>
    <td style="text-align: left;">Drug, Environmental Exposure</td>
    <td style="text-align: left;"><code>bio_bm_biosample_nails_results</code><br><code>bio_bm_biosample_nails_type</code></td>
  </tr>
  <tr>
      <td style="text-align: left;"><a href="biospec/urine" target="_blank">Urine</a></td>
      <td style="text-align: left;">Maternal</td>
      <td style="text-align: left;">Drug Panel, Toxins</td>
      <td style="text-align: left;"><code>bio_bm_biosample_urine</code></td>
  </tr>
  </tbody>
  </table>
</div>

<div id="neurocog" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-brain"></i></span>
  <span class="text-with-link">
  <span class="text">Neurocognition & Language</span>
  <a class="anchor-link" href="#neurocog" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 10%;">Instrument</th>
      <th style="width: 10%;">Version</th>
      <th style="width: 40%;">Construct</th>
      <th style="width: 10%;">Table Name</th>
    </tr>
  </thead>
  <tbody>
   <tr>
      <td><a href="neurocog/mlds" target="_blank">MLDS</a></td>
      <td></td>
      <td>Multilingual exposure</td>
      <td><code>ncl_ch_mlds</code></td>
    </tr>
    <tr>
      <td><a href="neurocog/spm2" target="_blank">SPM-2</a></td>
      <td>Infant/Toddler</td>
      <td>Sensory processing</td>
      <td><code>ncl_cg_spm2__inf</code></td>
    </tr>
  </tbody>
  </table>
</div>

<div id="sensors" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-microchip"></i></span>
  <span class="text-with-link">
  <span class="text">Novel Technologies & Wearable Sensors <span class="hint">(Primarily file-based data)</span></span>
  <a class="anchor-link" href="#sensors" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><b>Tabulated Data</b></p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 30%;">Instrument</th>
      <th style="width: 30%;">Construct</th>
      <th style="width: 30%;">Table Names</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="sensors/questionnaire" target="_blank">Infant Sensor Questionnaire 1/2/3</a></td>
    <td>Motor behavior, physical activity, sleep</td>
    <td><code>nt_ch_sens__qtn_<span class="blue-text">&lt;1|2|3&gt;</span></code></td>
  </tr>
  </tbody>
  </table>
<p><span class="tooltip tooltip-right"><b>File-Based Data</b><span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> <b>From Wearable Sensors</b></p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th>Sensor</th>
      <th>Description</th>
      <th><i class="fas fa-hammer"></i> Raw Data</th>
      <th><i class="fas fa-cog"></i> Derivatives</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="sensors/wearsensors" target="_blank">Infant Leg Sensors</a></td>
    <td>Motion/accelerometry data collected from wearable infant leg sensors</td>
    <td><a href="../datacuration/rawbids/#motion"><code>motion/</code></a></td>
    <td><a href="../datacuration/derivatives/#hbcd-motion-hbcd_motion">HBCD-Motion</a></td>
  </tr>
  </tbody>
  </thead>
</table>
</div>

<div id="physhealth" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-heart-pulse"></i></span>
  <span class="text-with-link">
  <span class="text">Physical Health</span>
  <a class="anchor-link" href="#physhealth" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th style="width: 30%;">Instrument</th>
      <th style="width: 30%;">Construct</th>
      <th style="width: 30%;">Table Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="physhealth/bf" target="_blank">Breast Feeding History</a></td>
      <td>Nutrition</td>
      <td><code>ph_cg_phx__bfh</code></td>
    </tr>
    <tr>
      <td><a href="physhealth/foodinsecurity" target="_blank">2-item Food Insecurity</a></td>
      <td>Food insecurity</td>
      <td><code>sed_cg_foodins</code></td>
    </tr>
    <tr>
      <td><a href="physhealth/growth" target="_blank">Height/Weight/Head Circumference</a></td>
      <td>Growth</td>
      <td><code>ph_ch_anthro</code></td>
  </tr> 
  </tbody>
  </table>
</div>

<div id="pex" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-baby"></i></span>
  <span class="text-with-link">
  <span class="text">Pregnancy & Exposure, Including Substance Use</span>
  <a class="anchor-link" href="#pex" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
<thead>
<tr>
    <th style="width: 5%;">Instrument</th>
    <th style="width: 5%;">Version</th>
    <th style="width: 30%;">Construct</th>
    <th style="width: 10%;">Table Name</th>
</tr>
</thead>
<tbody>
<!-- Pregnancy & Infant Health -->
<tr class="section-health">
  <td colspan="4" class="subsection-header">
    <i style="color: #3e3e3e;" class="fa-solid fa-baby"></i> <strong>&nbsp;&nbsp;Pregnancy & Infant Health</strong>
  </td>
</tr>
<tr class="section-health">
    <td><a href="pregexp/preghealth/healthhx" target="_blank">Health V1-Health History</a></td>
    <td></td>
    <td>Pre-pregnancy and pregnancy health</td>
    <td><code>pex_bm_health_preg__healthhx</code></td>
</tr>
<tr class="section-health">
    <td><a href="pregexp/preghealth/vacc" target="_blank">Health V1-Exposures & Vaccines</a></td>
    <td></td>
    <td>Vaccines in pregnancy</td>
    <td><code>pex_bm_health_preg__exp__vacc</code></td>
</tr>
<tr class="section-health">
    <td><a href="pregexp/preghealth/chronconditions" target="_blank">Health V1-Chronic Conditions</a></td>
    <td></td>
    <td>Chronic conditions/STIs in pregnancy</td>
    <td><code>pex_bm_health_preg__chroncond</code></td>
</tr>
<tr class="section-health">
    <td><a href="pregexp/preghealth/illness" target="_blank">Health V1-Illness</a></td>
    <td></td>
    <td>Illness in pregnancy</td>
    <td><code>pex_bm_health_preg__illness</code></td>
</tr>
<tr class="section-health">
    <td><a href="pregexp/preghealth/er-hosp" target="_blank">Health V1-ER Admissions</a></td>
    <td></td>
    <td>ER visit or hospitalization in pregnancy</td>
    <td><code>pex_bm_health_preg__erhosp</code></td>
</tr>
<tr class="section-health">
    <td><a href="pregexp/preghealth/medications" target="_blank">Health V1-Medications</a></td>
    <td></td>
    <td>Medications in pregnancy</td>
    <td><code>pex_bm_health_preg__meds</code></td>
</tr>
<tr class="section-health">
    <td><a href="pregexp/preghealth/end-preg" target="_blank">Health V2-Pregnancy</a></td>
    <td></td>
    <td>Health updates up to delivery</td>
    <td><code>pex_bm_healthv2_preg</code></td>
</tr>
<tr class="section-health">
    <td><a href="pregexp/preghealth/infanthealth" target="_blank">Health V2-Infancy</a></td>
    <td></td>
    <td>Delivery and birth outcomes</td>
    <td><code>pex_bm_healthv2_inf</code></td>
</tr>
<!-- Mental Health -->
<tr class="section-mh">
  <td colspan="4" class="subsection-header">
    <i style="color: #3e3e3e;" class="fas fa-brain"></i> <strong style="color: #3e3e3e;">&nbsp;&nbsp;Mental Health</strong>
  </td>
</tr>
<tr class="section-mh">
    <td><a href="pregexp/mh/fam-mh" target="_blank">FAM MH</a></td>
    <td></td>
    <td>Personal and family mental health</td>
    <td><code>pex_bm_psych</code></td>
</tr>
<tr class="section-mh">
    <td><a href="pregexp/mh/apa12" target="_blank">APA 1/2</a></td>
    <td></td>
    <td>Mental Health</td>
    <td><code>pex_bm_apa</code></td>
</tr>
<tr class="section-mh">
    <td><a href="pregexp/mh/ptsd" target="_blank">DSM5 Acute Stress or PTSD</a></td>
    <td></td>
    <td>PTSD/acute stress symptom severity</td>
    <td><code>pex_bm_str__ptsd</code></td>
</tr>
<tr class="section-mh">
    <td><a href="pregexp/mh/epds" target="_blank">EPDS</a></td>
    <td></td>
    <td>Postnatal depression</td>
    <td><code>pex_bm_epds</code></td>
</tr>
<!-- Substance Use -->
<tr class="section-su">
  <td colspan="4" class="subsection-header">
    <i style="color: #3e3e3e;" class="fa-solid fa-prescription-bottle"></i> <strong style="color: #3e3e3e;">&nbsp;&nbsp;Substance Use</strong>
  </td>
</tr>
<tr class="section-su">
  <td rowspan="3"><a href="pregexp/su/assist" target="_blank">ASSIST</a></td>
  <td>V1.0</td>
  <td>Substance use before and during pregnancy</td>
  <td><code>pex_bm_assistv1</code></td>
</tr>
<tr class="section-su">
  <td>V2.0</td>
  <td>Substance use, pregnancy end and postnatal</td>
  <td><code>pex_bm_assistv2</code></td>
</tr>
<tr class="section-su">
  <td>V3.0</td>
  <td>Substance use post-pregnancy</td>
  <td><code>pex_bm_assistv3</code></td>
</tr>
<tr class="section-su">
  <td><a href="pregexp/su/tlfb" target="_blank">TLFB</a></td>
  <td></td>
  <td>Substance use before and during pregnancy</td>
  <td><code>pex_ch_tlfb</code></td>
</tr>
</tbody>
</table>
</div>

<div id="socenvdet" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-city"></i></span>
  <span class="text-with-link">
  <span class="text">Social & Environmental Determinants</span>
  <a class="anchor-link" href="#socenvdet" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th>Instrument</th>
      <th>Version</th>
      <th style="width: 60%;">Construct</th>
      <th>Table Name</th>
    </tr>
  </thead>
  <tbody> 
    <tr>
      <td><a href="SED/bfy" target="_blank">BFY</a></td>
      <td></td>
      <td>Benefits/Services/Economic Stress</td>
      <td><code>sed_bm_bfy</code></td>
    </tr>
    <tr>
      <td><a href="SED/v01-demo" target="_blank">HBCD Demographics</a></td>
      <td>V1</td>
      <td>Demographics (Adult Visit 1)</td>
      <td><code>sed_bm_demo</code></td>
    </tr>  
    <tr>
      <td><a href="SED/ehits" target="_blank">eHITS</a></td>
      <td></td>
      <td>Intimate Partner Violence</td>
      <td><code>sed_bm_ehits</code></td>
    </tr>    
    <tr>
      <td><a href="SED/safety" target="_blank">Neighborhood Safety</a></td>
      <td></td>
      <td>Neighborhood Safety</td>
      <td><code>sed_bm_nbhsaf</code></td>
    </tr> 
    <tr>
      <td><a href="SED/paces" target="_blank">PACES</a></td>
      <td></td>
      <td>Protective Factors</td>
      <td><code>sed_bm_paces</code></td>
    </tr>
    <tr>
      <td><a href="SED/promis" target="_blank">PROMIS</a></td>
      <td></td>
      <td>Perceived Stress/Social Support</td>
      <td><code>sed_bm_strsup</code></td>
    </tr>      
    <tr>
      <td><a href="SED/discr" target="_blank">Unfair Treatment</a></td>
      <td></td>
      <td>Experiences of Unfair Treatment</td>
      <td><code>sed_bm_phx__discr</code></td>
    </tr>           
  </tbody>
  </table>
  </div>

### Brain Activity - MRI & EEG

<div id="mri" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-magnet"></i></span>
  <span class="text-with-link">
    <span class="text">MRI & MRS</span>
    <a class="anchor-link" href="#mri" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
  <p><strong><span class="emoji"><i class="fa-regular fa-lightbulb"></i></span> Also see 
    <a href="mri">Overview & MRI Protocols</a> and 
    <a href="mri/qc"> HBCD MR Quality Control Procedures</a></strong>
  </p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <!-- First header row -->
    <tr>
      <th style="width: 15%;" rowspan="2">Name</th>
      <th style="width: 20%; text-align: center;" colspan="2"><span class="tooltip tooltip-right">File-Based Data<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span></th>
      <th style="width: 60%;" rowspan="2">Table Name(s)</th>
    </tr>
    <!-- Second header row -->
    <tr>
      <th style="width: 20%;">
        <i class="fas fa-hammer"></i> Raw Data
      </th>
      <th style="width: 20%;">
        <i class="fas fa-cog"></i> Derivatives
      </th>
    </tr>
  </thead>
    <tbody>
    <!-- sMRI -->
    <tr>
    <td><span class="tooltip tooltip-right"><a href="mri/smri" target="_blank">sMRI</a><span class="tooltiptext">Structural MRI</span></span></td>
    <td><a href="../datacuration/rawbids/#anatomical-anat" target="_blank"><code>anat/</code></a></td>
    <td>
        • <a href="../datacuration/derivatives/#bibsnet-bibsnet" target="_blank">BIBSNet</a><br>
        • <a href="../datacuration/derivatives/#mriqc-mriqc" target="_blank">MRIQC</a><br>
        • <a href="../datacuration/derivatives/#infant-fmriprep-nibabies" target="_blank">Infant-fMRIPrep</a><br>
        • <a href="../datacuration/derivatives/#xcp-d-xcp_d" target="_blank">XCP-D</a>
    </td>
    <td><code>img_brainswipes_xcpd-T2w</code><br>
        <code>img_mriqc_<span class="blue-text">&lt;T1w|T2w&gt;</span></code><br>
        <code>img_bibsnet_space-<span class="blue-text">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-A&gt;</span>_stat-mean_desc-curv_morph</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-A&gt;</span>_stat-mean_desc-sulc_morph</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-A&gt;</span>_stat-mean_desc-thickness_morph</code>
    </td>
    </tr>
    <!-- fMRI -->
    <tr>
    <td><span class="tooltip tooltip-right"><a href="mri/fmri" target="_blank">fMRI</a>
    <span class="tooltiptext">Functional MRI</span>
    </span>
    </td>
    <td>
        • <a href="../datacuration/rawbids/#functional-func-and-fieldmaps-fmap" target="_blank"><code>func/</code></a><br>
        • <a href="../datacuration/rawbids/#functional-func-and-fieldmaps-fmap" target="_blank"><code>fmap/</code></a>
    </td>
    <td>
        • <a href="../datacuration/derivatives/#infant-fmriprep-nibabies" target="_blank">Infant-fMRIPrep</a><br>
        • <a href="../datacuration/derivatives/#xcp-d-xcp_d" target="_blank">XCP-D</a>
    </td>
    <td><code>img_brainswipes_xcpd-bold</code><br>
        <code>img_mriqc_bold</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-F&gt;</span>_stat-alff_bold</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-F&gt;</span>_stat-coverage_bold</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-F&gt;</span>_stat-reho_bold</code>
    </td></tr>
    <!-- dMRI -->
    <tr>
    <td>
        <a href="mri/dmri" target="_blank">dMRI</a>
    </td>
    <td><a href="../datacuration/rawbids/#diffusion-dwi" target="_blank"><code>dwi/</code></a></td>
    <td>
        • <a href="../datacuration/derivatives/#qsiprep-qsiprep" target="_blank">QSIPrep</a><br>
        • <a href="../datacuration/derivatives/#qsirecon" target="_blank">QSIRecon</a>
    </td>
    <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td>
    </tr>
    <!-- qMRI -->
    <tr>
    <td>
        <a href="mri/qmri" target="_blank">qMRI</a>
    </td>
    <td><code>anat/</code></td>
    <td>
        • <a href="../datacuration/derivatives/#symri-symri" target="_blank">SyMRI</a><br>
        • <a href="../datacuration/derivatives/#qmri-postproc-qmri_postproc" target="_blank">qMRI Postproc</a>
    </td>
    <td>N/A</td>
    </tr>
    <!-- MRS -->
    <tr>
    <td><a href="mri/mrs" target="_blank">MRS</a></td>
    <td><code>mrs/</code></td>
    <td><a href="../datacuration/derivatives/#osprey-bids-osprey" target="_blank">OSPREY-BIDS</a></td>
    <td>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code><br>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_AlphaCorrWaterScaled_Voxel_1_Basis_1</code><br>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_CSFWaterScaled_Voxel_1_Basis_1</code><br>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_TissCorrWaterScaled_Voxel_1_Basis_1</code><br>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_rawWaterScaled_Voxel_1_Basis_1</code><br>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_amplMets_Voxel_1_Basis_1</code><br>
        <code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_tCr_Voxel_1_Basis_1</code><br>
        <code>img_osprey_HERCULES_qm_processed_spectra</code><br>
        <code>img_osprey_unedited_qm_processed_spectra</code>
    </td>
    </tr>
</tbody>
</table>
<details open>
<summary>Label Values Legend</summary>
<p style="margin-bottom: 0; padding-bottom: 0; font-size: smaller;">
  <b style="color: #0077cc;">SEG-A</b>: 4S{1-10}00Parcels, Glasser, Gordon, MIDB, MyersLabonte<br>
  <b style="color: #0077cc;">SEG-F</b>: 4S{1-10}00Parcels, Glasser, Gordon, MIDB, MyersLabonte, HCP, Tian<br>
  <b style="color: #0077cc;">PROC</b>: HERCULES_diff1, HERCULES_diff2, HERCULES_sum, unedited_A
</p>
</details>
</div>

<div id="eeg" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-bolt"></i></span>
  <span class="text-with-link">
  <span class="text">EEG</span>
  <a class="anchor-link" href="#eeg" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong><span class="emoji"><i class="fa-regular fa-lightbulb"></i></span> Also see <a href="eeg">Overview & Quality Control</a></strong></p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <!-- First header row -->
    <tr>
      <th style="width: 30%;" rowspan="2">Task</th>
      <th style="width: 40%; text-align: center;" colspan="2">
        <span class="tooltip tooltip-right">
          File-Based Data
          <span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span>
        </span>
      </th>
      <th style="width: 40%;" rowspan="2">Table Names</th>
    </tr>
    <!-- Second header row -->
    <tr>
      <th style="width: 10%;">
        <i class="fas fa-hammer"></i> Raw BIDS
      </th>
      <th style="width: 10%;">
        <i class="fas fa-cog"></i> Derivatives
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="eeg/mmn" target="_blank">Auditory Mismatch Negativity (MMN)</a></td>
      <td><a href="../datacuration/rawbids/#eeg" target="_blank"><code>eeg/</code></a></td>
      <td><a href="../datacuration/derivatives/#hbcd-made-made" target="_blank">HBCD-MADE</a></td>
      <td><code>eeg_made_task-MMN_acq-eeg_preprocessingReport</code><br><code>eeg_qc_task-MMN</code></td>
    </tr>
    <tr>
      <td><a href="eeg/faces" target="_blank">Faces (Face)</a></td>
      <td><a href="../datacuration/rawbids/#eeg" target="_blank"><code>eeg/</code></a></td>
      <td><a href="../datacuration/derivatives/#hbcd-made-made" target="_blank">HBCD-MADE</a></td>
      <td><code>eeg_made_task-FACE_acq-eeg_preprocessingReport</code><br><code>eeg_qc_task-FACE</code></td>
    </tr>
    <tr>
      <td><a href="eeg/videors" target="_blank">Video Resting State (RS)</a></td>
      <td><a href="../datacuration/rawbids/#eeg" target="_blank"><code>eeg/</code></a></td>
      <td><a href="../datacuration/derivatives/#hbcd-made-made" target="_blank">HBCD-MADE</a></td>
      <td><code>eeg_made_task-RS_acq-eeg_preprocessingReport</code><br><code>eeg_qc_task-RS</code></td>
    </tr>
    <tr>
      <td><a href="eeg/vep" target="_blank">Visual Evoked Potential (VEP)</a></td>
      <td><a href="../datacuration/rawbids/#eeg" target="_blank"><code>eeg/</code></a></td>
      <td><a href="../datacuration/derivatives/#hbcd-made-made" target="_blank">HBCD-MADE</a></td>
      <td><code>eeg_made_task-VEP_acq-eeg_preprocessingReport</code><br>
          <code>eeg_qc_task-VEP</code></td>
    </tr>
  </tbody>
</table>
  </div>

### Demographics & Visit Information

<div id="demo" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-id-card"></i></span>
  <span class="text-with-link">
  <span class="text">Basic Demographics & Visit Info</span>
  <a class="anchor-link" href="#demo" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 20%;">Instrument</th>
      <th>Version <span class="tooltip tooltip-right"><i class="fa-solid fa-circle-info"></i><span class="tooltiptext">if more than one version is included in the release</span></span></th>
      <th style="width: 30%;">Construct</th>
      <th style="width: 30%;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="demo/basicdemo" target="_blank">Basic Demographics</a></td>
    <td><i>NA</i></td>
    <td>Demographics data derived from multiple sources</td>
    <td><code>sed_basic_demographics</code></td>
  </tr>
    <tr>
    <td><a href="demo/visitinfo" target="_blank">Visit Level Data</a></td>
    <td><i>NA</i></td>
    <td>Participant visit information</td>
    <td><code>par_visit_data</code></td>
  </tr>
  </tbody>
  </table>
</div>

<br>
