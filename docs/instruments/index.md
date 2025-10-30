# Study Instruments
In this section we provide a brief overview of each study instrument provided in the data release, including, where applicable, details of implementation and data collection, scoring procedures, quality control procedures, data and responsible use warnings, and references. Full study protocols are available on the [HBCD Study site](https://hbcdstudy.org/study-protocols/). See [Pending Updates](../changelog/pending.md) for details on what to expect in future releases.

<div class="table-banner">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text">All surveys used in the HBCD Study were translated to Spanish by <a href="https://burgtranslations.com/our-services/">BURG Translations</a></span>
</div>
<p></p>

<img src="https://hbcdstudy.org/wp-content/uploads/2025/03/HBCD_Timeline_March2025_Updated.png" width="90%" height="auto" class="center">

HBCD Study data includes both tabulated and file-based data - see <a href="../datacuration/overview" target="_blank">Data Structure Overview</a> for details. In summary:

- <a href="../datacuration/phenotypes" target="_blank">Tabulated data</a> contain data across all participants organized according to a standardized tabulated format for HBCD (*includes Behavior, Biospecimens/Toxicology, Demographics, data derived from MRI and other file-based data, etc.*).
- File-based data are in varied, modality-specific formats. This includes <a href="../datacuration/file-based-data/#raw-bids" target="_blank">raw BIDS data</a> and <a href="../datacuration/file-based-data/#derivatives" target="_blank">processed derivatives</a> organized under subject/session-level folders (*MRI/MRS, EEG, and Wearable Sensors*) as well as <a href="../datacuration/file-based-data/#concatenated-data" target="_blank">concatenated data</a> aggregated across participants for certain modalities (*including Genomics*).

Expand the sections below to see a list of measures associated with each domain included in the latest release data.

## Instruments by Domain

Expand the sections below to see a list of measures associated with each domain included in the latest release data.

<img src="../images/inst-ex.png" width="90%" height="auto" class="center">

--------------

<button id="toggle-all-btn" style="
  padding: 2px 14px;
  font-size: 1em;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
">
  Expand All Sections ↕️
</button>

### Demographics & Administrative

<div id="demo" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-id-card"></i></span>
  <span class="text-with-link">
  <span class="text">Demographics</span>
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
      <th style="width: 30%;">Instrument</th>
      <th style="width: 30%;">Construct</th>
      <th style="width: 30%;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="demo/basicdemo" target="_blank">Basic Demographics</a></td>
    <td>Demographics data derived from multiple sources</td>
    <td><code>sed_basic_demographics</code></td>
  </tr>
    <tr>
    <td><a href="demo/visitinfo" target="_blank">Visit Information</a></td>
    <td>Participant visit information</td>
    <td><code>par_visit_data</code></td>
  </tr>
</tbody>
</table>
</div>

<div id="admin" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-clipboard"></i></span>
  <span class="text-with-link">
  <span class="text">Administrative</span>
  <a class="anchor-link" href="#admin" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 40%;">Instrument</th>
      <th style="width: 40%;">Construct</th>
      <th style="width: 30%;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="admin/study-navigators" target="_blank">Study Navigator Contact Form</a></td>
    <td>Study Navigation</td>
    <td><code>TBD</code></td>
  </tr>
  </tbody>
  </table>
</div>

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
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <tr>
    <th>Instrument</th>
    <th>Version</th>
    <th>Construct</th>
    <th>Table Name</th>
  </tr>
</thead>
  <tbody>
  <tr>
    <td><a href="bcgi/chaos" target="_blank">CHAOS</a></td>
    <td></td>
    <td>Family Organization</td>
    <td><code>mh_cg_chaos</code></td>
  </tr>
  <tr>
    <td rowspan="2" style="word-wrap: break-word; white-space: normal;">
      <a href="bcgi/ecpromis" target="_blank">ecPROMIS Child-Caregiver Relationship</a></td>
    <td>&lt;1 year</td>
    <td>Child-Caregiver Interaction</td>
    <td><code>mh_cg_pms__cc__inf</code></td>
  </tr>
  <tr>
    <td>1-5 years</td>
    <td>Child-Caregiver Interaction</td>
    <td><code>mh_cg_pms__cc__1to5</code></td>
  </tr>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
      <a href="bcgi/ecpromis-pr" target="_blank">ecPROMIS Peer Relationships</a></td>
    <td></td>
    <td>Peer Relationships</td>
    <td><code>mh_cg_pms__peer</code></td>
  </tr>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;">
      <a href="bcgi/ecpromis-selfreg" target="_blank">ecPROMIS Self-Regulation</a></td>
    <td></td>
    <td>Self-Regulation and Flexibility</td>
    <td><code>mh_cg_pms__selfreg</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/fad" target="_blank">FAD (GF6+)</a></td>
    <td></td>
    <td style="word-wrap: break-word; white-space: normal;">Global Functioning of Family Unit</td>
    <td><code>mh_cg_fad</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/home21" target="_blank">HOME-21</a></td>
    <td>Infant-Toddler</td>
    <td>Child’s Home Environment</td>
    <td><code>sed_cg_home_ec</code></td>
  </tr>
  <tr>
    <td rowspan="2"><a href="bcgi/ibqr" target="_blank">IBQR-R (VSF)+BI / ECBQ-R (VSF)+BI</a></td>
    <td>Infant (<i>I</i>)</td>
    <td rowspan="2">
      Surgency/Extraversion,<br>
      Negative Affectivity,<br>
      Effortful Control,<br>
      Behavioral Inhibition (<i>BI</i>)</td>
    <td><code>mh_cg_ibqr</code></td>
  </tr>
  <tr>
    <td>Early Childhood (<i>EC</i>)</td>
    <td><code>mh_cg_ecbq</code></td>
  </tr>
  <tr>
    <td rowspan="2"><a href="bcgi/maps-tl" target="_blank">MAPS-TL</a></td>
    <td>Infancy (< 1 year)</td>
    <td rowspan="2">Irritability</td>
    <td><code>mh_cg_mapdb__inf</code></td>
  </tr>
  <tr>
    <td>Toddlerhood & Preschool</td>
    <td><code>mh_cg_mapstl__tod</code></td>
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
<p style="font-size: 0.9em; color: #555;">
<i style="color: teal;" class="fas fa-layer-group"></i>&nbsp;= Concatenated (File-Based) Data &nbsp;&nbsp;
<i style="color: teal;" class="fa-solid fa-table"></i>&nbsp;= Tabulated Data
</p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<th></th>
<th>Instrument</th>
<th>Version</th>
<th>Construct</th>
<th><i style="color: teal;" class="fa-solid fa-table"></i>&nbsp; Table / <i style="color: teal;" class="fas fa-layer-group"></i>&nbsp; Folder Name</th>
</thead>
<tbody>
<tr>
    <td style="text-align: center;"><i style="color: teal;" class="fas fa-layer-group"></i></td>
    <td><a href="biospec/illumina-gda-gwas" target="_blank">Illumina GDA GWAS</a></td>
    <td>Maternal & Child</td>
    <td>GWAS, EWAS, Transcriptome</td>
    <td><i>concatenated/genetics/</i>  <a href="biospec/illumina-gda-gwas/#concat" target="_blank"><i class="fa-solid fa-up-right-from-square"></i></a></td>
</tr>
<tr>
    <td style="text-align: center;"><i style="color: teal;" class="fa-solid fa-table"></i></td>
    <td><a href="biospec/nails" target="_blank">Maternal Nails</a></td>
    <td>Maternal</td>
    <td>Drug, Environmental Exposure</td>
    <td><code>bio_bm_biosample_nails_<span class="blue-text">&lt;results|type&gt;</span></code></td>
</tr>
<tr>
    <td style="text-align: center;"><i style="color: teal;" class="fa-solid fa-table"></i></td>
    <td><a href="biospec/urine" target="_blank">Maternal Urine</a></td>
    <td>Maternal</td>
    <td>Drug Panel, Toxins</td>
    <td><code>bio_bm_biosample_urine</code></td>
</tr>
</tbody>
</table>
</div>

<div id="neurocog" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-puzzle-piece"></i></span>
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
       <th style="width: 1%;"></th>
      <th style="width: 10%;">Instrument</th>
      <th style="width: 20%;">Version</th>
      <th style="width: 30%;">Construct</th>
      <th style="width: 10%;"><span class="tooltip tooltip-bottom"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="neurocog/macarthur-bates" target="_blank">MacArthur-Bates CDI-I</a></td>
      <td>Infant Form</td>
      <td>Language Development in Child</td>
      <td><code>nc_ch_cdiws</code><br><code>nc_ch_cdiwg</code></td>
    </tr>
   <tr>
    <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="neurocog/mlds" target="_blank">MLDS</a></td>
      <td></td>
      <td>Multilingual exposure</td>
      <td><code>ncl_ch_mlds</code></td>
    </tr>
    <tr>
      <td rowspan="2"><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td rowspan="2"><a href="neurocog/spm2" target="_blank">SPM-2</a></td>
      <td>Infant</td>
      <td>Sensory Processing/Integration</td>
      <td><code>ncl_cg_spm2__inf</code></td>
    </tr>
    <tr>
      <td>Toddler</td>
      <td>Sensory Processing/Integration</td>
      <td><code>ncl_cg_spm2__tod</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="neurocog/vineland" target="_blank">Vineland</a></td>
      <td></td>
      <td>Adaptive Behavior</td>
      <td><code>nc_cg_vabs</code></td>
    </tr>
  </tbody>
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
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 1%;"></th>
      <th style="width: 25%;">Instrument</th>
      <th>Version</th>
      <th style="width: 25%;">Construct</th>
      <th style="width: 25%;"><span class="tooltip tooltip-bottom"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="physhealth/foodinsecurity" target="_blank">2-item Food Insecurity</a></td>
      <td></td>
      <td>Food insecurity</td>
      <td><code>sed_cg_foodins</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="physhealth/bisq-sf" target="_blank">Brief Infant Sleep Questionnaire</a></td>
      <td></td>
      <td>Sleep</td>
      <td><code>ph_cg_bisq</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="physhealth/bf" target="_blank">Breast Feeding History</a></td>
      <td></td>
      <td>Nutrition</td>
      <td><code>ph_cg_phx__bfh</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="physhealth/ecpromis-pags" target="_blank">ecPROMIS- Physical Activity/Greenspace</a></td>
      <td>Early Childhood</td>
      <td>Physical Activity</td>
      <td><code>ph_cg_pms__pags</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="physhealth/ecpromis-sleep" target="_blank">ecPROMIS- Sleep</a></td>
      <td>Early Childhood</td>
      <td>Sleep</td>
      <td><code>ph_cg_pms__sleep</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="physhealth/growth" target="_blank">Height/Weight/Head Circumference</a></td>
      <td></td>
      <td>Growth</td>
      <td><code>ph_ch_anthro</code></td>
    </tr> 
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="physhealth/medical-history" target="_blank">Medical History</a></td>
      <td></td>
      <td>Medical History</td>
      <td><code>ph_cg_ecls__medhist</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="physhealth/nutrition" target="_blank">Nutrition Questionnaire</a></td>
      <td>Infant</td>
      <td>Nutrition</td>
      <td><code>ph_cg_inq</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="physhealth/screenq" target="_blank">ScreenQ</a></td>
      <td></td>
      <td>Media Use</td>
      <td><code>ph_cg_screenq</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="physhealth/vision" target="_blank">Vision Screener</a></td>
      <td></td>
      <td>Vision</td>
      <td><code>ph_ch_vs</code></td>
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
  <th style="width: 1%;"></th>
  <th style="width: 5%;">Instrument</th>
  <th style="width: 1%;">Ver</th>
  <th style="width: 20%;">Construct</th>
  <th style="width: 10%;"><span class="tooltip tooltip-bottom"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name</th>
</tr>
</thead>
<tbody>
<!-- Pregnancy & Infant Health -->
<tr class="section-health">
  <td colspan="5" class="subsection-header">
    <i style="color: #3e3e3e;" class="fa-solid fa-baby"></i> <strong>&nbsp;&nbsp;Pregnancy & Infant Health</strong>
  </td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex/" target="_blank">Health V1-Health History</a></td>
  <td></td>
  <td>Pre-pregnancy and pregnancy health</td>
  <td><code>pex_bm_health_preg__healthhx</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex/" target="_blank">Health V1-Exp & Vaccines</a></td>
  <td></td>
  <td>Vaccines in pregnancy</td>
  <td><code>pex_bm_health_preg__exp__vacc</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex/" target="_blank">Health V1-Chronic Conditions</a></td>
  <td></td>
  <td>Chronic conditions/STIs in pregnancy</td>
  <td><code>pex_bm_health_preg__chroncond</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex/" target="_blank">Health V1-Illness</a></td>
  <td></td>
  <td>Illness in pregnancy</td>
  <td><code>pex_bm_health_preg__illness</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex/" target="_blank">Health V1-ER Admissions</a></td>
  <td></td>
  <td>ER visit or hospitalization in pregnancy</td>
  <td><code>pex_bm_health_preg__erhosp</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex/" target="_blank">Health V1-Medications</a></td>
  <td></td>
  <td>Medications in pregnancy</td>
  <td><code>pex_bm_health_preg__meds</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex/" target="_blank">Health V2-Pregnancy</a></td>
  <td></td>
  <td>Health updates up to delivery</td>
  <td><code>pex_bm_healthv2_preg</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex/" target="_blank">Health V2-Infancy</a></td>
  <td></td>
  <td>Delivery and birth outcomes</td>
  <td><code>pex_bm_healthv2_inf</code></td>
</tr>
<!-- Mental Health -->
<tr class="section-mh">
  <td colspan="5" class="subsection-header">
    <i style="color: #3e3e3e;" class="fas fa-brain"></i> <strong style="color: #3e3e3e;">&nbsp;&nbsp;Mental Health</strong>
  </td>
</tr>
<tr class="section-mh">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/mh/fam-mh" target="_blank">FAM MH</a></td>
  <td></td>
  <td>Personal and Family Mental Health</td>
  <td><code>pex_bm_psych</code></td>
</tr>
<tr class="section-mh">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/mh/apa12" target="_blank">APA 1/2</a></td>
  <td></td>
  <td>Mental Health</td>
  <td><code>pex_bm_apa</code></td>
</tr>
<tr class="section-mh">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/mh/ptsd" target="_blank">DSM5 Acute Stress or PTSD</a></td>
  <td></td>
  <td>PTSD/Acute Stress Symptom Severity</td>
  <td><code>pex_bm_str__ptsd</code></td>
</tr>
<tr class="section-mh">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/mh/epds" target="_blank">EPDS</a></td>
  <td></td>
  <td>Postnatal Depression</td>
  <td><code>pex_bm_epds</code></td>
</tr>
<!-- Substance Use -->
<tr class="section-su">
  <td colspan="5" class="subsection-header">
    <i style="color: #3e3e3e;" class="fa-solid fa-prescription-bottle"></i> <strong style="color: #3e3e3e;">&nbsp;&nbsp;Substance Use</strong>
  </td>
</tr>
<tr class="section-su">
  <td rowspan="4"><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td rowspan="4"><a href="pregexp/su/assist" target="_blank">ASSIST</a></td>
  <td>V1</td>
  <td>SU Before and During Pregnancy</td>
  <td><code>pex_bm_assistv1</code></td>
</tr>
<tr class="section-su">
  <td>V2</td>
  <td>SU, Pregnancy End & Postnatal</td>
  <td><code>pex_bm_assistv2</code></td>
</tr>
<tr class="section-su">
  <td>V3</td>
  <td>SU After Pregnancy (3 mo anchors)</td>
  <td><code>pex_bm_assistv3</code></td>
</tr>
<tr class="section-su">
  <td>V4</td>
  <td>SU After Pregnancy (12 mo anchors)</td>
  <td><code>pex_bm_assistv4</code></td>
</tr>
<tr class="section-su">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/su/su-patterns" target="_blank">Substance Use Patterns</a></td>
  <td></td>
  <td>Substance Use in Pregnancy</td>
  <td><code>pex_bm_subst</code></td>
</tr>
<tr class="section-su">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/su/tlfb" target="_blank">TLFB</a></td>
  <td></td>
  <td>SU Before and During Pregnancy</td>
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
      <th style="width: 1%;"></th>
      <th style="width: 15%;">Instrument</th>
      <th>Version</th>
      <th style="width: 60%;">Construct</th>
      <th style="width: 30%;"><span class="tooltip tooltip-bottom"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name / <span class="tooltip tooltip-bottom"><i class="fas fa-layer-group"></i><span class="tooltiptext">Concatenated Data</span></span> Folder</th>
    </tr>
  </thead>
  <tbody>
      <tr>
      <td rowspan="2"><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td rowspan="2"><a href="SED/aces" target="_blank">ACEs</a></td>
      <td></td>
      <td>Adverse Childhood Experiences (Caregiver)</td>
      <td><code>sed_cg_ace</code></td>
    </tr>  
    <tr>
      <td>Pediatric</td>
      <td>Adverse Childhood Experiences (Child)</td>
      <td><code>sed_cg_pedaces</code></td>
    </tr>  
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="SED/bfy" target="_blank">BFY</a></td>
      <td></td>
      <td>Benefits/Services/Economic Stress</td>
      <td><code>sed_bm_bfy</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="SED/cab" target="_blank">CABr-SF</a></td>
      <td></td>
      <td>Intimate Partner Violence</td>
      <td><code>sed_cg_cabr_sf</code></td>
    </tr>
    <tr>
      <td rowspan="3"><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td rowspan="3"><a href="SED/demo-cg" target="_blank">Demographics Adult</a></td>
      <td>V1</td>
      <td>Demographics (Adult Visit 1)</td>
      <td><code>sed_bm_demo</code></td>
    </tr> 
    <tr>
      <td>V4</td>
      <td>Demographics (Birth Parent Visit 4)</td>
      <td>ADD<code></code></td>
    </tr> 
    <tr>
      <td>V6</td>
      <td>Demographics (Adult Visit 6)</td>
      <td>ADD<code></code></td>
    </tr> 
    <tr>
      <td rowspan="2"><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td rowspan="2"><a href="SED/demo-ch" target="_blank">Demographics Child</a></td>
      <td>V4</td>
      <td>Demographics (Child Visit 4)</td>
      <td><code>sed_bm_demo_child</code></td>
    </tr> 
    <tr>
      <td>V6</td>
      <td>Demographics (Child Visit 6)</td>
      <td>ADD<code></code></td>
    </tr> 
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="SED/ehits" target="_blank">eHITS</a></td>
      <td></td>
      <td>Intimate Partner Violence</td>
      <td><code>sed_bm_ehits</code></td>
    </tr>  
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="SED/current-employment" target="_blank">Employment</a></td>
      <td></td>
      <td>Current Employment</td>
      <td><code>sed_cg_employ</code></td>
    </tr>  
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td style="word-wrap: break-word; white-space: normal;"><a href="SED/household-chemical-exposures" target="_blank">Household Chemical Exposures</a></td>
      <td></td>
      <td>Household Chemical Exposures</td>
      <td><code>sed_cg_hce</code></td>
    </tr>   
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="SED/lead-exposures" target="_blank">Lead Exposures</a></td>
      <td></td>
      <td>Lead Exposures</td>
      <td><code>sed_cg_leadexp</code></td>
    </tr> 
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="SED/safety" target="_blank">Neighborhood Safety</a></td>
      <td></td>
      <td>Neighborhood Safety</td>
      <td><code>sed_bm_nbhsaf</code></td>
    </tr> 
    <tr>
      <td rowspan="2"><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td rowspan="2"><a href="SED/paces" target="_blank">PACES</a></td>
      <td>Current</td>
      <td>Protective Factors</td>
      <td><code>sed_bm_paces</code></td>
    </tr>
     <tr>
      <td>&lt;18</td>
      <td>Protective Factors</td>
      <td><code>sed_cg_paces</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="SED/promis" target="_blank">PROMIS</a></td>
      <td></td>
      <td>Perceived Stress/Social Support</td>
      <td><code>sed_bm_strsup</code></td>
    </tr>      
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="SED/second-hand-smoke-exposure" target="_blank">Second Hand Smoke</a></td>
      <td></td>
      <td>Second Hand Smoke Exposure</td>
      <td><code>sed_cg_shs</code></td>
    </tr>    
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="SED/discr" target="_blank">Unfair Treatment</a></td>
      <td></td>
      <td>Experiences of Unfair Treatment</td>
      <td><code>sed_bm_phx__discr</code></td>
    </tr>  
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="SED/vi" target="_blank">Vancouver Index</a></td>
      <td></td>
      <td>Acculturation</td>
      <td><code>sed_cg_via</code></td>
    </tr>      
  </tbody>
  </table>
</div>

### Brain Activity & Biosensors

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
<p>The following <b>EEG tasks</b> were acquired for the HBCD Study - see <a href="eeg/" target="_blank">Overview & EEG Protocols</a> for more information.</p>
<div class="two-column-list">
  <div class="column">
    <ul>
      <li><b>Auditory Mismatch Negativity Task (<a href="eeg/mmn" target="_blank">MMN</a>)</b></li>
      <li><b>Faces Task (<a href="eeg/faces" target="_blank">FACE</a>)</b></li>
    </ul>
  </div>
  <div class="column">
    <ul>
      <li><b>Video Resting State Task (<a href="eeg/videors" target="_blank">RS</a>)</b></li>
      <li><b>Visual Evoked Potential Task (<a href="eeg/vep" target="_blank">VEP</a>)</b></li>
    </ul>
  </div>
</div>
<p><i style="color: teal;" class="fas fa-folder-open"></i> <b>FILE-BASED DATA</b>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; margin-bottom: 0; padding-bottom: 0;">
<tfoot>
<tr>
  <td colspan="4" style="word-wrap: break-word; white-space: normal; border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
    <sup><b>1</b></sup> Whenever possible, pipeline derivatives are also provided in the HBCD tabulated format to match other instruments - <a href="../datacuration/overview/#warning" target="_blank">see details</a>
  </td>
</tr>
</tfoot>
<thead>
<tr>
  <th>EEG Task</th>
  <th>Raw BIDS</th>
  <th>Pipeline Derivatives</th>
  <th style="text-align: center;">Tabulated Derivatives<sup><b>1</b></sup></th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="eeg/tasks/" target="_blank">ALL</td>
  <td><code>eeg/</code> <a href="eeg/#rawbids" target="_blank"><i class="fa-solid fa-up-right-from-square"></i></a></td>
  <td><a href="eeg/#made" target="_blank">HBCD-MADE</a></td>
  <td style="text-align: center;"><i style="color: green;" class="fa-solid fa-check"></i></td>
</tr>
</tbody>
</table>
<p><i style="color: teal;" class="fa-solid fa-table"></i> <b>TABULATED DATA</b></p>
<p style="font-size: 0.9em; color: #555;">
<i style="color: teal;" class="fa-solid fa-diagram-project"></i>&nbsp;= HBCD-MADE pipeline derivatives in HBCD tabulated format (<i><a href="../datacuration/overview/#warning" target="_blank">see details</a></i>)
</p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
<th>Table</th>
<th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="eeg/qc" target="_blank">Quality Control Metrics</a> (capping quality, StimTracker artifact, etc.)</td>
  <td><code>eeg_qc_task-<span class="blue-text">&lt;MMN|FACE|RS|VEP&gt;</span></code></td>
</tr>
<tr>
  <td><i style="color: teal;" class="fa-solid fa-diagram-project"></i> HBCD-MADE Preprocessing Report</td>
  <td><code>eeg_made_task-<span class="blue-text">&lt;MMN|FACE|RS|VEP&gt;</span>_acq-eeg_preprocessingReport</code></td>
</tr>
<tr>
  <td><i style="color: teal;" class="fa-solid fa-diagram-project"></i> HBCD-MADE ERP Summary Stats</td>
  <td><code>eeg_made_task-<span class="blue-text">&lt;MMN|FACE|VEP&gt;</span>_acq-eeg_ERPSummaryStats</code></td>
</tr>
</tbody>
</table>
</div>

<div id="mri" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-brain"></i></span>
  <span class="text-with-link">
    <span class="text">MRI & MRS</span>
    <a class="anchor-link" href="#mri" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><i style="color: teal;" class="fas fa-folder-open"></i> <b>FILE-BASED DATA</b></p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tfoot>
<tr>
  <td colspan="4" style="word-wrap: break-word; white-space: normal; border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
    <sup><b>1</b></sup> Whenever possible, pipeline derivatives are also provided in the HBCD tabulated format to match other instruments - <a href="../datacuration/overview/#warning" target="_blank">see details</a>
  </td>
</tr>
</tfoot>
<thead>
<tr>
  <th>Modality</th>
  <th>Raw BIDS</th>
  <th>Pipeline Derivatives</th>
  <th>Tabulated Derivatives<sup><b>1</b></sup></th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="4"><a href="mri/smri" target="_blank">Structural</a> &<br><a href="mri/fmri" target="_blank">Functional</a> MRI</td>
  <td rowspan="4"><code>anat/</code><br><code>fmap/</code><br><code>func/</code></td>
  <td>MRIQC (<a href="../../instruments/mri/smri/#mriqc" target="_blank">sMRI</a> & <a href="../../instruments/mri/fmri/#mriqc" target="_blank">fMRI</a>)</td>
  <td style="text-align: center;"><i style="color: green;" class="fa-solid fa-check"></i></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/smri/#bibsnet" target="_blank">BIBSNet</a></td>
  <td style="text-align: center;"><i style="color: green;" class="fa-solid fa-check"></i></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#nibabies" target="_blank">Infant fMRIPrep</a> & <a href="../../instruments/mri/fmri/#fs-mcribs" target="_blank">FreeSurfer & M-CRIB-S</a></td>
  <td style="text-align: center;"><i style="color: red;" class="fa-solid fa-xmark"></i></td>
</tr>
<tr>
  <td><a href="../../instruments/mri/fmri/#xcpd" target="_blank">XCP-D</a></td>
  <td style="text-align: center;"><i style="color: green;" class="fa-solid fa-check"></i></td>
</tr>
<tr>
  <td><a href="mri/qmri" target="_blank">Quantitative MRI</a></td>
  <td><code>anat/</code></td>
  <td><a href="../../instruments/mri/qmri/#derivatives" target="_blank">SyMRI</a> & <a href="../../instruments/mri/qmri/#derivatives" target="_blank">qMRI PostProc</a></td>
  <td style="text-align: center;"><i style="color: red;" class="fa-solid fa-xmark"></i></td>
</tr>
<tr>
  <td rowspan="2"><a href="mri/dmri" target="_blank">Diffusion MRI</a></td>
  <td rowspan="2"><code>dwi/</code></td>
  <td><a href="../../instruments/mri/dmri/#qsiprep" target="_blank">QSIPrep</a></td>
  <td style="text-align: center;"><i style="color: green;" class="fa-solid fa-check"></i></td>
</tr>
<tr>
<td><a href="mri/dmri/#qsirecon" target="_blank">QSIRecon</a> (<a href="../../instruments/mri/dmri/#qsirecon-DSIStudio" target="_blank">DSI Studio</a>/
  <a href="../../instruments/mri/dmri/#qsirecon-DIPYDKI" target="_blank">DIPY DKI</a>/
  <a href="../../instruments/mri/dmri/#qsirecon-TORTOISE" target="_blank">TORTOISE MAP-MRI & Tensor</a>)</td>
  <td style="text-align: center;"><i style="color: red;" class="fa-solid fa-xmark"></i></td>
</tr>
<tr>
  <td><a href="mri/mrs" target="_blank">MR Spectroscopy</a></td>
  <td><code>mrs/</code></td>
  <td><a href="../../instruments/mri/mrs/#derivatives" target="_blank">OSPREY-BIDS</a></td>
  <td style="text-align: center;"><i style="color: green;" class="fa-solid fa-check"></i></td>
</tr>
</tbody>
</table>
<p><i style="color: teal;" class="fa-solid fa-table"></i> <b>TABULATED DATA</b></p>
<p style="font-size: 0.9em; color: #555;">
<i style="color: teal;" class="fa-solid fa-diagram-project"></i>&nbsp;= Pipeline derivatives in tabulated format
</p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
<th>Instrument / <i style="color: teal;" class="fa-solid fa-diagram-project"></i> Modality</th>
<th>Construct / <i style="color: teal;" class="fa-solid fa-diagram-project"></i> Pipeline</th>
<th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="mri/questionnaire" target="_blank">Pre-Scan Questionnaire</a></td>
  <td>Sleeping Scan Prep</td>
  <td><code>img_ra_prep</code></td>
</tr>
<tr>
  <td><a href="mri/qc/#brainswipes" target="_blank">BrainSwipes</a></td>
  <td>Manual QC</td>
  <td><code>img_brainswipes_xcpd-bold</code></td>
</tr>
<tr>
  <td rowspan="3"><i style="color: teal;" class="fa-solid fa-diagram-project"></i>&nbsp; sMRI & fMRI</td>
  <td>MRIQC</td>
  <td><code>img_mriqc_<span class="blue-text">&lt;T1w|T2w&gt;</span></code><br><code>img_mriqc_bold</code></td>
</tr>
<tr>
  <td>BIBSNet</td>
  <td><code>img_bibsnet_space-<span class="blue-text">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes</code></td>
</tr>
<tr>
  <td>XCP-D</td>
  <td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-curv_morph</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-sulc_morph</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-thickness_morph</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-alff_bold</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-coverage_bold</code><br>
    <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-reho_bold</code>
  </td>
</tr>
<tr>
  <td><i style="color: teal;" class="fa-solid fa-diagram-project"></i>&nbsp; dMRI</td>
  <td>QSIPrep</td>
  <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td>
</tr>
<tr>
  <td><i style="color: teal;" class="fa-solid fa-diagram-project"></i>&nbsp; MRS</td>
  <td>OSPREY-BIDS</td>
  <td>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_AlphaCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_CSFWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_TissCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_rawWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_amplMets_Voxel_1_Basis_1</code><br>
    <code>img_osprey_<span class="blue-text">&lt;Q&gt;</span>_tCr_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_qm_processed_spectra</code><br>
    <code>img_osprey_unedited_qm_processed_spectra</code>
    </td>
</tr>
<tr>
  <td colspan="4">
    <strong>Label Values Legend</strong><br>
    <b style="color: #0077cc;">&lt;PARC&gt;</b> (parcellations): 4S-{1-10}56Parcels, Glasser, Gordon, MIDB, MyersLabonte, HCP, Tian (HCP & Tian functional only)<br>
    <b style="color: #0077cc;">&lt;Q&gt;</b> (quantification method): HERCULES_diff1, HERCULES_diff2, HERCULES_sum, unedited_A
  </td>
</tr>
</tbody>
</table>
</div>

<div id="sensors" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-microchip"></i></span>
  <span class="text-with-link">
  <span class="text">Novel Technologies & Wearable Sensors</span>
  <a class="anchor-link" href="#sensors" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><i style="color: teal;" class="fas fa-folder-open"></i> <b>FILE-BASED DATA</b></p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; margin-bottom: 0; padding-bottom: 0;">
<tfoot>
<tr>
  <td colspan="4" style="word-wrap: break-word; white-space: normal; border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
    <sup><b>1</b></sup> Whenever possible, pipeline derivatives are also provided in the HBCD tabulated format to match other instruments - <a href="../datacuration/overview/#warning" target="_blank">see details</a>
  </td>
</tr>
</tfoot>
<thead>
<tr>
  <th>Sensor</th>
  <th>Raw BIDS</th>
  <th>Pipeline Derivatives</th>
  <th style="text-align: center;">Tabulated Derivatives<sup><b>1</b></sup></th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="sensors/wearsensors/" target="_blank">Infant Leg Motion</td>
  <td><code>motion/</code> <a href="sensors/wearsensors/#rawbids" target="_blank"><i class="fa-solid fa-up-right-from-square"></i></a></td>
  <td><a href="sensors/wearsensors/#derivatives" target="_blank">HBCD-Motion</a></td>
  <td style="text-align: center;"><i style="color: red;" class="fa-solid fa-xmark"></i></td>
</tr>
</tbody>
</table>
<p style="margin-top: 0; padding-top: 0;"><i style="color: teal;" class="fa-solid fa-table"></i> <b>TABULATED DATA</b></p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
<th>Instrument</th>
<th>Construct</th>
<th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="sensors/questionnaire" target="_blank">Infant Sensor Questionnaire 1</a></td>
  <td>Day 1 - Motor Development, Regulation (Sleep/Wake)</td>
  <td><code>nt_ch_sens__qtn_<span class="blue-text">1</span></code></td>
</tr>
<tr>
  <td><a href="sensors/questionnaire" target="_blank">Infant Sensor Questionnaire 2</a></td>
  <td>Day 2 - Motor Development, Regulation (Sleep/Wake)</td>
  <td><code>nt_ch_sens__qtn_<span class="blue-text">2</span></code></td>
</tr>
  <td><a href="sensors/questionnaire" target="_blank">Infant Sensor Questionnaire 3</a></td>
  <td>Day 3 - Motor Development, Regulation (Sleep/Wake)</td>
  <td><code>nt_ch_sens__qtn_<span class="blue-text">3</span></code></td>
</tr>
</tbody>
</table>
</div>

