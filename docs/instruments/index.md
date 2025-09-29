# Study Instruments
The current release includes data from **Visits 1, 2, and 3 (V01, V02, and V03)** for the majority of measures. In this section we provide a brief overview of each study instrument provided in the data release, including, where applicable, details of implementation and data collection, scoring procedures, quality control procedures, data and responsible use warnings, and references. Full study protocols are available on the [HBCD Study site](https://hbcdstudy.org/study-protocols/). See [Upcoming Updates](../changelog/pending.md) for details on what to expect in future releases.

<div class="table-banner">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text">All surveys used in the HBCD Study were translated to Spanish by <a href="https://burgtranslations.com/our-services/">BURG Translations</a></span>
</div>
<p></p>

<img src="https://hbcdstudy.org/wp-content/uploads/2025/03/HBCD_Timeline_March2025_Updated.png" width="90%" height="auto" class="center">

HBCD Study data includes both tabulated and file-based data - see <a href="../datacuration/overview" target="_blank">Data Structure Overview</a> for details. In summary:

- <a href="../datacuration/phenotypes" target="_blank"><b>Tabulated data</b></a> contain data across all participants in a standardized [tabulated format](../datacuration/phenotypes.md/#table-organization) for HBCD (***includes Behavior, Biospecimens/Toxicology, Demographics, data derived from MRI and other file-based data, etc.***).
- File-based data include <a href="../datacuration/file-based-data/#raw-bids" target="_blank"><b>raw</b></a> and <a href="../datacuration/file-based-data/#processed-derivatives" target="_blank"><b>processed derivative</b></a> data organized under subject/session-level folders and are in varied modality-specific formats (***includes MRI/MRS, EEG, and Wearable Sensors data***).

Expand the sections below to see a list of measures associated with each domain included in Release 1.0.

## Instruments by Domain

<div style="margin-bottom: 8px;" class="warning-banner">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text">Click <i>domain headers</i> (e.g., <i>Biospecimen & Omics</i>) to expand and view domain measures.</span>
</div>

<div style="margin-bottom: 20px;" class="warning-banner">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text">Click <i>instrument names</i> (e.g., <i>Nails</i>) to access detailed instrument documentation.</span>
</div>

<button id="toggle-all-btn" style="
  padding: 6px 12px;
  font-size: 1em;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
  background-color: #ffe10066;;
">
  Expand All Sections ↕️
</button>

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
      <th style="width: 5%;"></th>
      <th style="width: 30%;">Instrument</th>
      <th style="width: 30%;">Construct</th>
      <th style="width: 30%;"><span class="tooltip tooltip-left"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
    <td><a href="demo/basicdemo" target="_blank">Basic Demographics</a></td>
    <td>Demographics data derived from multiple sources</td>
    <td><code>sed_basic_demographics</code></td>
  </tr>
    <tr>
    <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
    <td><a href="demo/visitinfo" target="_blank">Visit Information</a></td>
    <td>Participant visit information</td>
    <td><code>par_visit_data</code></td>
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
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 1%;"></th>
      <th style="width: 30%;">Instrument</th>
      <th>Version</th>
      <th style="width: 50%;">Construct</th>
      <th style="width: 10%;"><span class="tooltip tooltip-bottom"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
    <td><a href="bcgi/ecpromis" target="_blank">ecPROMIS-Ch/CG Interaction</a></td>
    <td>&lt;1 year</td>
    <td>Child/Caregiver Relationship</td>
    <td><code>mh_cg_pms__cc__inf</code></td>
  </tr>
  <tr>
    <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
    <td style="word-wrap: break-word; white-space: normal;"><a href="bcgi/ibqr" target="_blank">BQ (VSF)+BI</a></td>
    <td>IBQ-R (VSF)+BI<br>(<i>Infant</i>)</td>
    <td style="word-wrap: break-word; white-space: normal;">Surgency/Extraversion, Negative Affectivity, Effortful Control, Behavioral Inhibition</td>
    <td><code>mh_cg_ibqr</code></td>
  </tr>
  <tr>
    <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
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
      <th style="width: 1%;"></th>
      <th style="width: 10%;">Instrument</th>
      <th>Version</th>
      <th style="width: 30%;">Construct</th>
      <th style="width: 30%;"><span class="tooltip tooltip-bottom"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
    <td style="text-align: left;"><a href="biospec/nails" target="_blank">Nails</a></td>
    <td style="text-align: left;">Maternal</td>
    <td style="text-align: left;">Drug, Environmental Exposure</td>
    <td style="text-align: left;"><code>bio_bm_biosample_nails_results</code><br><code>bio_bm_biosample_nails_type</code></td>
  </tr>
  <tr>
    <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
    <td style="text-align: left;"><a href="biospec/urine" target="_blank">Urine</a></td>
    <td style="text-align: left;">Maternal</td>
    <td style="text-align: left;">Drug Panel, Toxins</td>
    <td><code>bio_bm_biosample_urine</code></td>
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
       <th style="width: 1%;"></th>
      <th style="width: 10%;">Instrument</th>
      <th style="width: 10%;">Version</th>
      <th style="width: 30%;">Construct</th>
      <th style="width: 20%;"><span class="tooltip tooltip-bottom"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name</th>
    </tr>
  </thead>
  <tbody>
   <tr>
    <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="neurocog/mlds" target="_blank">MLDS</a></td>
      <td></td>
      <td>Multilingual Exposure</td>
      <td><code>ncl_ch_mlds</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="neurocog/spm2" target="_blank">SPM-2</a></td>
      <td>Infant</td>
      <td>Sensory Processing/Integration</td>
      <td><code>ncl_cg_spm2__inf</code></td>
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
      <th style="width: 10%;">Version</th>
      <th style="width: 25%;">Construct</th>
      <th style="width: 25%;"><span class="tooltip tooltip-bottom"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="physhealth/foodinsecurity" target="_blank">2-item Food Insecurity</a></td>
      <td></td>
      <td>Food Insecurity</td>
      <td><code>sed_cg_foodins</code></td>
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
      <td><a href="physhealth/growth" target="_blank">Height/Weight/Head Circumference</a></td>
      <td></td>
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
  <td><a href="pregexp/pex" target="_blank">Health V1-Health History</a></td>
  <td></td>
  <td>Pre-pregnancy and pregnancy health</td>
  <td><code>pex_bm_health_preg__healthhx</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex" target="_blank">Health V1-Exp & Vaccines</a></td>
  <td></td>
  <td>Vaccines in pregnancy</td>
  <td><code>pex_bm_health_preg__exp__vacc</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex" target="_blank">Health V1-Chronic Conditions</a></td>
  <td></td>
  <td>Chronic conditions/STIs in pregnancy</td>
  <td><code>pex_bm_health_preg__chroncond</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex" target="_blank">Health V1-Illness</a></td>
  <td></td>
  <td>Illness in pregnancy</td>
  <td><code>pex_bm_health_preg__illness</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex" target="_blank">Health V1-ER Admissions</a></td>
  <td></td>
  <td>ER visit or hospitalization in pregnancy</td>
  <td><code>pex_bm_health_preg__erhosp</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex" target="_blank">Health V1-Medications</a></td>
  <td></td>
  <td>Medications in pregnancy</td>
  <td><code>pex_bm_health_preg__meds</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex" target="_blank">Health V2-Pregnancy</a></td>
  <td></td>
  <td>Health updates up to delivery</td>
  <td><code>pex_bm_healthv2_preg</code></td>
</tr>
<tr class="section-health">
  <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td><a href="pregexp/pex" target="_blank">Health V2-Infancy</a></td>
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
  <td rowspan="3"><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
  <td rowspan="3"><a href="pregexp/su/assist" target="_blank">ASSIST</a></td>
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
      <th style="width: 30%;"><span class="tooltip tooltip-bottom"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="SED/bfy" target="_blank">BFY</a></td>
      <td></td>
      <td>Benefits/Services, Economic Stress</td>
      <td><code>sed_bm_bfy</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="SED/v01-demo/" target="_blank">HBCD Demographics</a></td>
      <td>V1</td>
      <td>Demographics (Adult Visit 1)</td>
      <td><code>sed_bm_demo</code></td>
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
      <td><a href="SED/safety" target="_blank">Neighborhood Safety</a></td>
      <td></td>
      <td>Neighborhood Safety</td>
      <td><code>sed_bm_nbhsaf</code></td>
    </tr> 
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="SED/paces" target="_blank">PACES</a></td>
      <td>&lt;18</td>
      <td>Protective Factors</td>
      <td><code>sed_bm_paces</code></td>
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
      <td><a href="SED/discr" target="_blank">Unfair Treatment</a></td>
      <td></td>
      <td>Experiences of Unfair Treatment</td>
      <td><code>sed_bm_phx__discr</code></td>
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
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th></th>
      <th style="width: 40%;">EEG Task</th>
      <th style="width: 60%;"><span class="tooltip tooltip-bottom"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name / <span class="tooltip tooltip-left"><i class="fa-solid fa-folder-open"></i><span class="tooltiptext">File-Based Data</span></span> Folder</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="eeg/mmn" target="_blank">Auditory Mismatch Negativity (MMN)</a></td>
      <td><code>eeg_made_task-MMN_acq-eeg_preprocessingReport</code><br><code>eeg_qc_task-MMN</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="eeg/faces" target="_blank">Faces (Face)</a></td>
      <td><code>eeg_made_task-FACE_acq-eeg_preprocessingReport</code><br><code>eeg_qc_task-FACE</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="eeg/videors" target="_blank">Video Resting State (RS)</a></td>
      <td><code>eeg_made_task-RS_acq-eeg_preprocessingReport</code><br><code>eeg_qc_task-RS</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
      <td><a href="eeg/vep" target="_blank">Visual Evoked Potential (VEP)</a></td>
      <td><code>eeg_made_task-VEP_acq-eeg_preprocessingReport</code><br><code>eeg_qc_task-VEP</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-folder-open"></i><span class="tooltiptext">File-Based Data</span></span></td>
      <td><a href="eeg/#rawbids" target="_blank">All Tasks - <strong><i>Raw BIDS</i></strong></a></td>
      <td><i>rawdata/sub-{ID}/ses-{V0X}/eeg/</i></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><i class="fa-solid fa-folder-open"></i><span class="tooltiptext">File-Based Data</span></span></td>
      <td><a href="eeg/#made" target="_blank">All Tasks - <strong><i>HBCD-MADE Derivatives</i></strong></a></td>
      <td><i>derivatives/made/</i></td>
    </tr>
  </tbody>
</table>
</div>

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
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px">
  <thead>
    <tr>
      <th style="width: 1%;"></th>
      <th style="width: 10%;"><a href="../datacuration/file-based-data/#raw-bids" target="_blank"><span class="tooltip tooltip-right"><i class="fa-solid fa-folder-open"></i><span class="tooltiptext">File-Based Data</span></span> Raw BIDS</a></th>
      <th style="width: 40%;"><span class="tooltip tooltip-right"><i class="fa-solid fa-folder-open"></i><span class="tooltiptext">File-Based Data</span></span> <a href="../datacuration/file-based-data/#processed-derivatives" target="_blank">Derivatives</a> [Source <a href="processing" target="_blank">Pipeline</a>]</th>
      <th style="width: 40%;"><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Tables Derived from Pipeline Derivatives</th>
    </tr>
  </thead>
    <tbody>
    <tr>
      <td rowspan="5"><span class="tooltip tooltip-right"><a href="mri/smri" target="_blank">sMRI</a><span class="tooltiptext">Structural MRI</span></span></td>
      <td rowspan="5"><i>anat/</i></td>
      <td><i>bibsnet/</i> [<a href="mri/smri/#bibsnet" target="_blank">BIBSNet</a>]</td>
      <td><code>img_bibsnet_space-<span class="blue-text">&lt;T1w|T2w&gt;</span>_desc-aseg_volumes</code></td>
    </tr>
    <tr>
      <td><i>mriqc/</i> [<a href="mri/smri/#mriqc" target="_blank">MRIQC</a>]</td>
      <td><code>img_mriqc_<span class="blue-text">&lt;T1w|T2w&gt;</span></code></td>
    </tr>
    <tr>
      <td><i>nibabies/</i> [<a href="mri/fmri/#nibabies" target="_blank">Infant-fMRIPrep</a>]</td>
      <td>None</td>
    </tr>
    <tr>
      <td><i>xcp_d/</i> [<a href="mri/fmri/#xcpd" target="_blank">XCP-D</a>]</td>
      <td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-curv_morph</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-sulc_morph</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-mean_desc-thickness_morph</code>
      </td>
    </tr>
    <tr>
      <td><i>NA</i> - <a href="mri/qc/#brainswipes" target="_blank">BrainSwipes</a> QC results</td>
      <td><code>img_brainswipes_xcpd-T2w</code></td>
    </tr>
    <tr>
      <td rowspan="4"><span class="tooltip tooltip-right"><a href="mri/fmri" target="_blank">fMRI</a><span class="tooltiptext">Functional MRI</span></span></td>
      <td rowspan="4"><i>func/</i></td>
      <td><i>mriqc/</i> [<a href="mri/fmri/#mriqc" target="_blank">MRIQC</a>]</td>
      <td><code>img_mriqc_bold</code></td>
    </tr>
    <tr>
      <td><i>nibabies/</i> [<a href="mri/fmri/#nibabies" target="_blank">Infant-fMRIPrep</a>]</td>
      <td>None</td>
    </tr>
    <tr>
      <td><i>xcp_d/</i> [<a href="mri/fmri/#xcpd" target="_blank">XCP-D</a>]</td>
      <td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-alff_bold</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-coverage_bold</code><br>
        <code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;PARC&gt;</span>_stat-reho_bold</code>
      </td>
    </tr>
    <tr>
      <td><i>NA</i> - <a href="mri/qc/#brainswipes" target="_blank">BrainSwipes</a> QC results</td>
      <td><code>img_brainswipes_xcpd-bold</code></td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><a href="mri/qmri" target="_blank">qMRI</a><span class="tooltiptext">Quantitative MRI</span></span></td>      <td><i>anat/</i></td>
      <td><i>qmri_postproc/</i> [<a href="mri/qmri/#derivatives" target="_blank">qMRI Postproc</a>]</td>
      <td>None</td>
    </tr>
    <tr>
      <td rowspan="6"><span class="tooltip tooltip-right"><a href="mri/dmri" target="_blank">dMRI</a><span class="tooltiptext">Diffusion MRI</span></span></td>
      <td rowspan="6"><i>dwi/</i></td>
      <td><i>qsiprep/</i> [<a href="mri/dmri/#qsiprep" target="_blank">QSIPrep</a>]</td>
      <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td>
    </tr>
    <tr>
      <td><i>qsirecon/</i> [<a href="mri/dmri/#qsirecon" target="_blank">QSIRecon</a>]</td>
      <td>None</td>
    </tr>
    <tr>
      <td><a href="mri/dmri/#qsirecon-DSIStudio" target="_blank"><i>qsirecon-DSIStudio/</i></a></td>
      <td>None</td>
    </tr>
    <tr>
      <td><a href="mri/dmri/#qsirecon-DIPYDKI" target="_blank"><i>qsirecon-DIPYDKI/</i></a></td>
      <td>None</td>
    </tr>
    <tr>
      <td><a href="mri/dmri/#qsirecon-TORTOISE" target="_blank"><i>qsirecon-TORTOISE_model-MAPMRI/</i></a></td>
      <td>None</td>
    </tr>
      <tr>
      <td><a href="mri/dmri/#qsirecon-TORTOISE" target="_blank"><i>qsirecon-TORTOISE_model-tensor/</i></a></td>
      <td>None</td>
    </tr>
    <tr>
      <td><span class="tooltip tooltip-right"><a href="mri/mrs" target="_blank">MRS</a><span class="tooltiptext">MR Spectroscopy</span></span></td>      <td><i>mrs/</i></td>
      <td><i>osprey/</i> [<a href="mri/mrs/#derivatives" target="_blank">OSPREY-BIDS</a>]</td>
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
      <strong>end</strong><br>
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
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 1%;">Sensor</th>
      <th style="width: 1%;"></th>
      <th style="width: 30%;">Data Type</th>
      <th style="width: 30%;">Construct</th>
      <th style="width: 30%;"><span class="tooltip tooltip-bottom"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span> Table Name / <span class="tooltip tooltip-left"><i class="fa-solid fa-folder-open"></i><span class="tooltiptext">File-Based Data</span></span> Folder</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td rowspan="3"><a href="sensors/wearsensors" target="_blank">Infant Leg Motion</a></td>
    <td><span class="tooltip tooltip-right"><i class="fa-solid fa-table"></i><span class="tooltiptext">Tabulated Data</span></span></td>
    <td><a href="sensors/questionnaire" target="_blank">Questionnaire 1/2/3</a></td>
    <td rowspan="3">Motor Development,<br>Regulation (Sleep/Wake)</td>
    <td><code>nt_ch_sens__qtn_<span class="blue-text">&lt;1|2|3&gt;</span></code></td>
  </tr>
  <tr>
    <td><span class="tooltip tooltip-right"><i class="fa-solid fa-folder-open"></i><span class="tooltiptext">File-Based Data</span></span></td>
    <td><a href="sensors/wearsensors/#rawbids" target="_blank">Raw BIDS</a></td>
    <td><i>rawdata/sub-{ID}/ses-{V0X}/motion/</i></td>
  </tr>
  <tr>
    <td><span class="tooltip tooltip-right"><i class="fa-solid fa-folder-open"></i><span class="tooltiptext">File-Based Data</span></span></td>
    <td><a href="sensors/wearsensors/#derivatives" target="_blank">Derivatives</a></td>
    <td><i>derivatives/hbcd-motion/</i></td>
  </tr>
  </tbody>
  </table>
</div>

<br>
