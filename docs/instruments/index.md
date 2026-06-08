<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
</style>

# Study Instruments

In this section we provide a brief overview of each study instrument provided in the data release, organized below by domain. Instrument documentat pages include, where applicable, details of implementation and data collection, scoring procedures, quality control procedures, data and responsible use warnings, and references. Study protocols are also available on the [HBCD Study site](https://hbcdstudy.org/study-protocols/). Note that HBCD Study data includes both tabulated and file-based data - see <a href="../datacuration/overview" target="_blank">Data Structure Overview</a> for details.

*Expand the sections below to see a list of measures associated with each domain included in the latest release data.*

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

## Behavior, Biology, & Environment

<div id="adm" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-clipboard-list"></i></span>
  <span class="text-with-link">
    <span class="text">Administrative</span>
    <a class="anchor-link" href="#adm" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<div class="table-legend">
  <span class="legend-item">
    <i class="fas fa-layer-group legend-icon"></i>
    Concatenated data <a href="/datacuration/file-based-data/#concatenated-data" target="_blank"><i>(see details)</i></a>
  </span>
</div>
<table class="table-no-vertical-lines index">
<thead>
<th>Instrument</th>
<th>Construct</th>
<th>File Name</th>
</thead>
<tbody>
<tr>
<td><a href="admin/study-navigators" target="_blank">Study Navigator Contact Form</a> <i class="fas fa-layer-group table-icon"></i></td>
<td>Recruitment/Retention</td>
<td><i>study_navigator/Study Navigator Export - Release 2.0.csv</i></td>
</tr>
</tbody>
</table>
</div>

<div id="demo" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-id-card"></i></span>
  <span class="text-with-link">
    <span class="text">Demographics</span>
    <a class="anchor-link" href="#demo" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="table-no-vertical-lines index">
  <thead>
    <tr>
      <th>Instrument</th>
      <th>Construct</th>
      <th>Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="demo/basicdemo/" target="_blank">Basic Demographics</a></td>
    <td>Demographics data derived from multiple sources</td>
    <td><code>sed_basic_demographics</code></td>
  </tr>
    <tr>
    <td><a href="demo/visitinfo/" target="_blank">Visit Level Data</a></td>
    <td>Participant visit information</td>
    <td><code>par_visit_data</code></td>
  </tr>
</tbody>
</table>
</div>

---

<div id="mh" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-people-arrows"></i></span>
  <span class="text-with-link">
    <span class="text">Behavior & Caregiver-Child Interaction</span>
    <a class="anchor-link" href="#mh" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="table-no-vertical-lines index">
<thead>
  <tr>
    <th>Instrument</th>
    <th>Construct</th>
    <th>Table Name</th>
  </tr>
</thead>
  <tbody>
  <tr>
    <td><a href="bcgi/chaos" target="_blank">CHAOS</a></td>
    <td>Family Organization</td>
    <td><code>mh_cg_chaos</code></td>
  </tr>
  <tr>
    <td>
      <a href="bcgi/ecpromis" target="_blank">ecPROMIS Caregiver-Child</a> 
      <!-- <div class="subtle">(&lt;1 / 1-5 years versions)</div> -->
      </td>
    <td>Caregiver-Child Interactions</td>
    <td><code>mh_cg_pms__cc__inf</code> <span class="subtle">(&lt;1 year)</span><br>
    <code>mh_cg_pms__cc__1to5</code> <span class="subtle">(1-5 years)</span></td>
  </tr>
  <tr>
    <td><a href="bcgi/ecpromis-pr" target="_blank">ecPROMIS Peer</a></td>
    <td>Peer Relationships</td>
    <td><code>mh_cg_pms__peer</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/ecpromis-selfreg" target="_blank">ecPROMIS Self-Regulation</a></td>
    <td>Self-Regulation and Flexibility</td>
    <td><code>mh_cg_pms__selfreg</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/erica" target="_blank">ERICA</a></td>
    <td>Emotional Regulation</td>
    <td><code>mh_cg_erica</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/fad" target="_blank">FAD (GF6+)</a></td>
    <td>Global Functioning of Family Unit</td>
    <td><code>mh_cg_fad</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/ibqr" target="_blank">IBQ-R (VSF)+BI</a></td>
    <td rowspan="2">
      Surgency/Extraversion,
      Negative Affectivity,<br>
      Effortful Control, 
      Behavioral Inhibition
      </td>
    <td><code>mh_cg_ibqr</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/ibqr" target="_blank">ECBQ (VSF)+BI</a></td>
    <td><code>mh_cg_ecbq</code></td>
  </tr>
  <tr>
    <td><a href="bcgi/maps-tl" target="_blank">MAPS-TL</a>
    <!-- <div class="subtle">(Infant / Toddler versions)</div> -->
    </td>
    <td>Irritability</td>
    <td>
    <code>mh_cg_mapdb__inf</code> <span class="subtle">(Infant)</span><br>
    <code>mh_cg_mapstl__tod</code> <span class="subtle">(Toddler)</span>
    </td>
  </tr>
  </tbody>
  </table>
</div>

<!-- BIOSPEC -->
<div id="biospec" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-vial"></i></span>
  <span class="text-with-link">
  <span class="text">Biospecimen & Omics</span>
  <a class="anchor-link" href="#biospec" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<div class="table-legend">
  <span class="legend-item">
    <i class="fas fa-layer-group legend-icon"></i>
    Concatenated data <a href="/datacuration/file-based-data/#concatenated-data" target="_blank"><i>(see details)</i></a>
  </span>
</div>
<table class="table-no-vertical-lines index">
<thead>
<th>Instrument</th>
<th>Construct</th>
<th>Table / Folder Name</th>
</thead>
<tbody>
<tr>
    <td><a href="biospec/illumina-gda-gwas" target="_blank">Illumina GDA GWAS</a><i class="fas fa-layer-group table-icon"></i></td>
    <td>GWAS, EWAS, Transcriptome</td>
    <td><i>concatenated/genetics/</i></td>
</tr>
<tr>
    <td><a href="biospec/nails" target="_blank">Maternal Nails</a></td>
    <td>Drug, Environmental Exposure</td>
    <td><code>bio_bm_biosample_nails_results</code><br>
    <code>bio_bm_biosample_nails_type</code></td>
</tr>
<tr>
    <td><a href="biospec/urine" target="_blank">Maternal Urine</a></td>
    <td>Drug Panel, Toxins</td>
    <td><code>bio_bm_biosample_urine_results</code></td>
</tr>
<tr>
    <td><a href="biospec/olink" target="_blank">Olink Explore</a> <i class="fas fa-layer-group table-icon"></i></td>
    <td>Maternal Inflammation</td>
    <td><i>concatenated/proteins/</i></td>
</tr>
</tbody>
</table>
</div>

<!-- NCL -->
<div id="ncl" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-puzzle-piece"></i></span>
  <span class="text-with-link">
  <span class="text">Neurocognition & Language</span>
  <a class="anchor-link" href="#ncl" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="table-no-vertical-lines">
<thead>
<tr>
  <th>Instrument</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="neurocog/bayley-4" target="_blank">Bayley-4 Scales</a></td>
  <td>Child Development (Cognitive, Language, and Motor)</td>
  <td><code>ncl_ch_bayley</code></td>
</tr>
<tr>
  <td><a href="neurocog/macarthur-bates" target="_blank">MacArthur-Bates CDI-I</a>
</td>
  <td>Language Development (Words & Gestures)</td>
  <td><code>ncl_ch_cdiwgen</code> <span class="subtle">(English version)</span>
  <br>
  <code>ncl_ch_cdiwges</code> <span class="subtle">(Spanish version)</span>  
  </td>
</tr>
<tr>
  <td><a href="neurocog/mlds" target="_blank">MLDS</a></td>
  <td>Multilingual Exposure</td>
  <td><code>ncl_ch_mlds</code></td>
</tr>
<tr>
  <td><a href="neurocog/spm2" target="_blank">Sensory Processing Measure-2</a>
  </td>
  <td>Sensory Processing/Integration</td>
  <td><code>ncl_cg_spm2__inf</code> <span class="subtle">(Infant version)</span>
  <br><code>ncl_cg_spm2__tod</code> <span class="subtle">(Toddler version)</span></td>
</tr>
<tr>
  <td><a href="neurocog/vineland" target="_blank">Vineland Adaptive Behavior</a></td>
  <td>Adaptive Behavior</td>
  <td><code>ncl_cg_vabs</code></td>
</tr>
</tbody>
</table>
</div>

<!-- PHYSICAL HEALTH -->
<div id="ph" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-heart-pulse"></i></span>
  <span class="text-with-link">
  <span class="text">Physical Health</span>
  <a class="anchor-link" href="#ph" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="table-no-vertical-lines index">
<thead>
<tr>
  <th>Instrument</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="physhealth/bisq-sf" target="_blank">Brief Infant Sleep Questionnaire</a></td>
  <td>Sleep</td>
  <td><code>ph_cg_bisq</code></td>
</tr>
<tr>
  <td><a href="physhealth/bf" target="_blank">Breast Feeding History</a></td>
  <td>Nutrition</td>
  <td><code>ph_cg_phx__bfh</code></td>
</tr>
<tr>
  <td><a href="physhealth/ecpromis-pags" target="_blank">ecPROMIS Physical Activity/Greenspace</a></td>
  <!-- <td>Early Childhood</td> -->
  <td>Physical Activity</td>
  <td><code>ph_cg_pms__pags</code></td>
</tr>
<tr>
  <td><a href="physhealth/ecpromis-sleep" target="_blank">ecPROMIS Sleep</a></td>
  <!-- <td>Early Childhood</td> -->
  <td>Sleep</td>
  <td><code>ph_cg_pms__sleep</code></td>
</tr>
<tr>
  <td><a href="physhealth/growth" target="_blank">Height/Weight/Head Circumference</a></td>
  <td>Growth</td>
  <td><code>ph_ch_anthro</code></td>
</tr> 
<tr>
  <td><a href="physhealth/medical-history" target="_blank">Medical History</a></td>
  <td>Medical History</td>
  <td><code>ph_cg_ecls__medhist</code></td>
</tr>
<tr>
  <td><a href="physhealth/nutrition" target="_blank">Nutrition Questionnaire</a></td>
  <!-- <td>Infant</td> -->
  <td>Nutrition</td>
  <td><code>ph_cg_inq</code></td>
</tr>
<tr>
  <td><a href="physhealth/screenq" target="_blank">ScreenQ</a></td>
  <td>Media Use</td>
  <td><code>ph_cg_screenq</code></td>
</tr>
<tr>
  <td><a href="physhealth/vision" target="_blank">Vision Screener</a></td>
  <td>Vision</td>
  <td><code>ph_ch_vs</code></td>
</tr>
</tbody>
</table>
</div>

<!-- PEX -->
<div id="pex" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-baby"></i></span>
  <span class="text-with-link">
  <span class="text">Pregnancy & Exposure, Including Substance Use</span>
  <a class="anchor-link" href="#pex" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<!-- Pregnancy & Infant Health -->
<span class="table-title"><i class="fa-solid fa-baby header-icon"></i> Pregnancy & Infant Health</span>
<table class="table-no-vertical-lines index">
<thead>
<tr>
  <th>Instrument</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<!-- <tr class="table-group-row">
  <td colspan="3"><i style="color: white;" class="fa-solid fa-baby table-icon-left"></i> Pregnancy & Infant Health</td>
</tr> -->
<tr class="section-health">
  <td><a href="pregexp/pex/" target="_blank">Health V1-Health History</a></td>
  <td>Pre-pregnancy and pregnancy health</td>
  <td><code>pex_bm_health_preg__healthhx</code></td>
</tr>
<tr class="section-health">
  <td><a href="pregexp/pex/" target="_blank">Health V1-Exp & Vaccines</a></td>
  <td>Vaccines in pregnancy</td>
  <td><code>pex_bm_health_preg__exp__vacc</code></td>
</tr>
<tr class="section-health">
  <td><a href="pregexp/pex/" target="_blank">Health V1-Chronic Conditions</a></td>
  <td>Chronic conditions/STIs in pregnancy</td>
  <td><code>pex_bm_health_preg__chroncond</code></td>
</tr>
<tr class="section-health">
  <td><a href="pregexp/pex/" target="_blank">Health V1-Illness</a></td>
  <td>Illness in pregnancy</td>
  <td><code>pex_bm_health_preg__illness</code></td>
</tr>
<tr class="section-health">
  <td><a href="pregexp/pex/" target="_blank">Health V1-ER Admissions</a></td>
  <td>ER visit or hospitalization in pregnancy</td>
  <td><code>pex_bm_health_preg__erhosp</code></td>
</tr>
<tr class="section-health">
  <td><a href="pregexp/pex/" target="_blank">Health V1-Medications</a></td>
  <td>Medications in pregnancy</td>
  <td><code>pex_bm_health_preg__meds</code></td>
</tr>
<tr class="section-health">
  <td><a href="pregexp/pex/" target="_blank">Health V2-Pregnancy</a></td>
  <td>Health updates up to delivery</td>
  <td><code>pex_bm_healthv2_preg</code></td>
</tr>
<tr class="section-health">
  <td><a href="pregexp/pex/" target="_blank">Health V2-Infancy</a></td>
  <td>Delivery and birth outcomes</td>
  <td><code>pex_bm_healthv2_inf</code></td>
</tr>
</tbody>
</table>





<!-- MENTAL HEALTH -->
<span class="table-title"><i class="fas fa-brain header-icon"></i> Mental Health</span>
<table class="table-no-vertical-lines index">
<thead>
<tr>
  <th>Instrument</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<!-- <tr class="table-group-row">
  <td colspan="3"><i style="color: white;" class="fas fa-brain table-icon-left"></i> Mental Health</td>
</tr> -->
<tr class="section-mh">
  <td><a href="pregexp/mh/fam-mh" target="_blank">FAM MH</a></td>
  <td>Personal and Family Mental Health</td>
  <td><code>pex_bm_psych</code></td>
</tr>
<tr class="section-mh">
  <td><a href="pregexp/mh/apa12" target="_blank">APA 1/2</a></td>
  <td>Mental Health</td>
  <td><code>pex_bm_apa</code></td>
</tr>
<tr class="section-mh">
  <td><a href="pregexp/mh/ptsd" target="_blank">DSM5 Acute Stress or PTSD</a></td>
  <td>PTSD/Acute Stress Symptom Severity</td>
  <td><code>pex_bm_str__ptsd</code></td>
</tr>
<tr class="section-mh">
  <td><a href="pregexp/mh/epds" target="_blank">EPDS</a></td>
  <td>Postnatal Depression</td>
  <td><code>pex_bm_epds</code></td>
</tr>
</tbody>
</table>
<!-- Substance Use -->
<span class="table-title"><i class="fa-solid fa-prescription-bottle header-icon"></i> Substance Use</span>
<table class="table-no-vertical-lines index">
<thead>
<tr>
  <th>Instrument</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<!-- <tr class="table-group-row">
  <td colspan="3"><i style="color: white;" class="fa-solid fa-prescription-bottle table-icon-left"></i> Substance Use</td>
</tr> -->
<tr class="section-su">
  <td><a href="pregexp/su/assist" target="_blank">ASSIST V1/2/3/4</a></td>
  <td>Substance Use Pre-, During, and Post-Pregnancy</td>
  <td><code>pex_bm_assistv<span class="blue-text">{1|2|3|4}</span></code></td>
</tr>
<tr class="section-su">
  <td><a href="pregexp/su/su-patterns" target="_blank">Substance Use Patterns</a></td>
  <td>Substance Use in Pregnancy</td>
  <td><code>pex_bm_subst</code></td>
</tr>
<tr class="section-su">
  <td><a href="pregexp/su/tlfb" target="_blank">TLFB</a></td>
  <td>Substance Use Before and During Pregnancy</td>
  <td><code>pex_ch_tlfb</code></td>
</tr>
</tbody>
</table>
</div>



<!-- SOC & ENV DETERMINANTS -->
<div id="sed" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-city"></i></span>
  <span class="text-with-link">
  <span class="text">Social & Environmental Determinants</span>
  <a class="anchor-link" href="#sed" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">

<div class="table-legend">
  <span class="legend-item">
    <i class="fas fa-layer-group legend-icon"></i>
    Concatenated data <a href="/datacuration/file-based-data/#concatenated-data" target="_blank"><i>(see details)</i></a>
  </span>
</div>

<table class="table-no-vertical-lines index">
<thead>
<tr>
  <th>Instrument</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="SED/aces" target="_blank">ACES</a></td>
  <td>Adverse Childhood Experiences</td>
  <td><code>sed_cg_ace</code> <br>
  <code>sed_cg_pedaces</code> <span class="subtle">(Pediatric ACES)</span>
  </td>
</tr>  
<tr>
  <td><a href="SED/bfy" target="_blank">Baby's First Years (BFY)</a></td>
  <td>Benefits/Services/Economic Stress</td>
  <td><code>sed_bm_bfy</code></td>
</tr>
<tr>
  <td><a href="SED/cab" target="_blank">Composite Abuse Scale (CABr-SF)</a></td>
  <td>Intimate Partner Violence</td>
  <td><code>sed_cg_cabr_sf</code></td>
</tr>
<tr>
  <td><a href="SED/current-employment" target="_blank">Current Employment</a></td>
  <td>Current Employment</td>
  <td><code>sed_cg_employ</code></td>
</tr>  
<tr>
  <td><a href="SED/demo-cg" target="_blank">Demographics</a></td>
  <td>Adult Demographics</td>
  <td><code>sed_bm_demo</code></td>
</tr> 
<tr>
  <td><a href="SED/demo-ch" target="_blank">Child Demographics</a></td>
  <td>Child Demographics</td>
  <td><code>sed_bm_demo_child</code></td>
</tr> 
<tr>
  <td><a href="SED/ehits" target="_blank">eHITS</a></td>
  <td>Intimate Partner Violence</td>
  <td><code>sed_bm_ehits</code></td>
</tr>  
<tr>
  <td><a href="SED/foodinsecurity" target="_blank">Food Insecurity</a></td>
  <td>Food insecurity</td>
  <td><code>sed_cg_foodins</code></td>
</tr>
<tr>
  <td><a href="SED/geocoded-linkage" target="_blank">Geocoded Linkage</a> <i class="fas fa-layer-group table-icon"></i></td>
  <td>Neighborhood Measures</td>
  <td><i>geocoded_linkage/</i></td>
</tr>  
<tr>
  <td><a href="SED/home21" target="_blank">HOME-21</a></td>
  <td>Child’s Home Environment</td>
  <td><code>sed_cg_home_it</code></td>
</tr>
<tr>
  <td><a href="SED/household-chemical-exposures" target="_blank">Household Chemical Exposures</a></td>
  <td>Household Chemical Exposures</td>
  <td><code>sed_cg_hce</code></td>
</tr>   
<tr>
  <td><a href="SED/lead-exposures" target="_blank">Lead Exposures</a></td>
  <td>Lead Exposures</td>
  <td><code>sed_cg_leadexp</code></td>
</tr> 
<tr>
  <td><a href="SED/safety" target="_blank">Neighborhood Safety</a></td>
  <td>Neighborhood Safety</td>
  <td><code>sed_bm_nbhsaf</code></td>
</tr> 
<tr>
  <td><a href="SED/paces" target="_blank">PACEs</a></td>
  <td>Protective Factors</td>
  <td><code>sed_bm_paces</code> <span class="subtle">(Current)</span><br>
      <code>sed_cg_paces</code> <span class="subtle">(Retrospective &lt;18)</span><br>
  </td>
</tr>
<tr>
  <td><a href="SED/promis" target="_blank">PROMIS</a></td>
  <td>Perceived Stress/Social Support</td>
  <td><code>sed_bm_strsup</code></td>
</tr>      
<tr>
  <td><a href="SED/second-hand-smoke-exposure" target="_blank">Second Hand Smoke</a></td>
  <td>Second Hand Smoke Exposure</td>
  <td><code>sed_cg_shs</code></td>
</tr>    
<tr>
  <td><a href="SED/transitions-in-care" target="_blank">Transitions in Care Screener</a></td>
  <td>Recruitment/Retention</td>
  <td><code>sed_cg_tic_screener</code></td>
</tr>
<tr>
  <td><a href="SED/discr" target="_blank">Unfair Treatment</a></td>
  <td>Experiences of Unfair Treatment</td>
  <td><code>sed_bm_phx__discr</code></td>
</tr>  
<tr>
  <td><a href="SED/vi" target="_blank">Vancouver Index (VIA)</a></td>
  <td>Acculturation</td>
  <td><code>sed_cg_via</code></td>
</tr>      
</tbody>
</table>
</div>

## Brain Activity & Biosensors

<div id="eeg" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-file-waveform"></i></span>
  <span class="text-with-link">
  <span class="text">EEG & Tabular EEG</span>
  <a class="anchor-link" href="#eeg" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>See the <a href="eeg/#overview-eeg-protocols">Overview page</a> for protocols, quality control procedures, etc. and <a href="eeg/tasks/">HBCD EEG Tasks</a> for task protocols/documentation. EEG tasks include Auditory Mismatch Negativity (<a href="eeg/tasks/#auditory-mismatch-negativity-task" target="_blank">MMN</a>), Faces (<a href="eeg/tasks/#faces-task" target="_blank">FACE</a>), Visual Evoked Potential (<a href="eeg/tasks/#visual-evoked-potential-task" target="_blank">VEP</a>), and Video Resting State (<a href="eeg/tasks/#video-resting-state-task" target="_blank">RS</a>).</p>

<h4><i class="fa-solid fa-folder-open header-icon"></i> EEG</h4>
<p>The <b>EEG</b> domain includes raw and processed file-based data:</p>
<ul>
<li><b>Raw BIDS</b>: <code>eeg/</code> participant session subfolders within <code>rawbids/</code> - <a href="eeg/#rawbids" target="_blank">see details</a></li>
<li><b>Processed</b>: <a href="eeg/#made" target="_blank">HBCD-MADE pipeline</a> derivatives under <code>derivatives/made/</code></li>
</ul>

<h4><i class="fa-solid fa-table header-icon"></i> Tabular EEG</h4>
<table class="table-no-vertical-lines index">
<thead>
<tr>
<th>Table</th>
<th>Table Name</th>
</tr>
</thead>
<tr>
  <td>EEG Acquisition Checklist & Checklist Reattempt 1/2</td>
  <td><code>eeg_ch_chkl</code><br>
  <code>eeg_ch_chkl_1</code><br>
  <code>eeg_ch_chkl_2</code></td>
</tr>
<tr>
  <td><a href="eeg/qc" target="_blank">Quality Control Metrics</a></td>
  <td><code>eeg_qc_task-<span class="blue-text">FACE</span></code><br>
      <code>eeg_qc_task-<span class="blue-text">MMN</span></code><br>
      <code>eeg_qc_task-<span class="blue-text">RS</span></code><br>
      <code>eeg_qc_task-<span class="blue-text">VEP</span></code>
  </td>
</tr>
<tr>
  <td>Tabular HBCD-MADE derivatives<br>
  <i>(See <a href="../datacuration/overview/#tabulated-pipeline-derivatives" target="_blank"><i>Tabulated Pipeline Derivatives</a> for details)</i></td>
  <td><code>eeg_made_task-<span class="blue-text">{FACE|MMN|RS|VEP}</span>_acq-eeg_preprocessingReport</code><br>
    <code>eeg_made_task-<span class="blue-text">{FACE|MMN|VEP}</span>FACE_ERPSummaryStats</code>
</td>
</tr>
</tbody>
</table>
</div>

<div id="mri" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-brain"></i></span>
  <span class="text-with-link">
    <span class="text">Imaging</span>
    <a class="anchor-link" href="#mri" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
    <th>Modality</th>
    <th>Raw BIDS <i>(<a href="mri/rawbids/" target="_blank">Documentation</a>)</i></th>
    <th>Pipeline Derivatives <i>(see <a href="../datacuration/file-based-data/#links-to-pipeline-derivatives" target="_blank">Links to Pipeline Derivatives</a>)</i></th>
</tr>
</thead>
<tbody>
<tr>
  <td>Structural MRI (<a href="mri/smri" target="_blank">sMRI</a>)</td>
  <td><code>anat/</code></td>
  <td>
    MRIQC • BIBSNet</td>
</tr>
<tr>
  <td>Functional MRI (<a href="mri/fmri" target="_blank">fMRI</a>)</td>
  <td><code>func/</code>, <code>fmap/</code></td>
  <td>
    MRIQC • Infant fMRIPrep + FreeSurfer / M-CRIB-S • XCP-D</td>
</tr>
<tr>
    <td>Quantitative MRI (<a href="mri/qmri" target="_blank">qMRI</a>)</td>
    <td><code>anat/</code>, <code>fmap/</code></td>
    <td>SyMRI & qMRI PostProc</td>
</tr>
<tr>
    <td>Diffusion MRI (<a href="mri/dmri" target="_blank">dMRI</a>)</td>
    <td><code>dwi/</code></td>
    <td>
      QSIPrep & QSIRecon (DSI Studio, DIPY DKI, TORTOISE)</td>
</tr>
<tr>
  <td>MR Spectroscopy (<a href="mri/mrs" target="_blank">MRS</a>)</td>
  <td><code>mrs/</code></td>
  <td>OSPREY-BIDS</td>
</tr>
</tbody>
</table>
</div>

<div id="mri-tab" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-brain"></i></span>
  <span class="text-with-link">
    <span class="text">Tabular Imaging</span>
    <a class="anchor-link" href="#mri-tab" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">

<div class="table-legend">
  <span class="legend-item">
    <i class="fa-solid fa-diagram-project legend-icon"></i>
   Tabulated pipeline derivatives (<a href="../datacuration/overview/#tabulated-pipeline-derivatives" target="_blank"><i>see details</i></a>)
  </span>
</div>
<table class="table-no-vertical-lines">
<thead>
<tr>
<th>Table</th>
<th>Construct</th>
<th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="mri/mri-forms/#mri-scan-session-data-summary-forms" target="_blank">MRI Data Summary Form</a></td>
<td>Pre-/Post-MRI Tech Checklist 2</td>
<td><code>mri_ra_chkl_data</code></td>
</tr>
<tr>
<td><a href="mri/mri-forms/#mri-scan-session-data-summary-forms" target="_blank">MRI Scan Session Summary Form</a></td>
<td>Pre-/Post-MRI Tech Checklist 1</td>
<td><code>mri_ra_chkl_scan</code></td>
</tr>
<tr>
<td><a href="mri/prescan-questionnaire" target="_blank">Pre/Post Scan Prep</a></td>
<td>Infant Sleep</td>
<td><code>mri_ra_prep</code></td>
</tr>
<tr>
<td><a href="mri/qc#brainswipes" target="_blank">BrainSwipes</a></td>
<td>Manual QC</td>
<td>
<code>img_brainswipes_xcpd_hash-0f306a2f+0ef9c88a_T2w</code><br>
<code>img_brainswipes_xcpd_hash-0f306a2f+0ef9c88a_bold</code><br>
<code>img_brainswipes_xcpd_hash-2afa9081+0ef9c88a_T1w</code><br>
<code>img_brainswipes_xcpd_hash-2afa9081+0ef9c88a_bold</code><br>
</td>
</tr>
<tr>
<td>MRIQC</td><td><i class="fa-solid fa-diagram-project header-icon"></i></td>
<td><code>img_mriqc_T1w</code><br><code>img_mriqc_T2w</code><br><code>img_mriqc_bold</code></td>
</tr>
<tr>
<td>BIBSNet</td><td><i class="fa-solid fa-diagram-project header-icon"></i></td>
<td><code>img_bibsnet_space-T1w_desc-aseg_volumes</code><br><code>img_bibsnet_space-T2w_desc-aseg_volumes</code></td>
</tr>
<tr>
  <td>XCP-D</td>
  <td><i class="fa-solid fa-diagram-project header-icon"></i></td>
  <td>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-mean_desc-curv_morph</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-mean_desc-sulc_morph</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-mean_desc-thickness_morph</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-alff_bold</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-coverage_bold</code><br>
    <code>img_xcpd_hash-<span class="blue-text">{HASH}</span>_space-fsLR_seg-<span class="blue-text">{PARC}</span>_stat-reho_bold</code>
  <br><br>
  <code><span class="blue-text">{HASH}</span></code>  values: <code>0f306a2f+0ef9c88a</code>; <code>2afa9081+0ef9c88a</code><br>
  <code><span class="blue-text">{PARC}</span></code>  values: <code>Glasser</code>, <code>Gordon</code>, etc - <a href="mri/fmri/#parc" target="_blank">see full atlas list →</a></code><br><br>
  <a href="mri/tables/xcpd.html" target="_blank">See full file list →</a></td>
</tr>
<tr>
  <td>QSIPrep</td>
  <td><i class="fa-solid fa-diagram-project header-icon"></i></td>
  <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td>
</tr>
<tr>
<td>OSPREY-BIDS</td>
<td><i class="fa-solid fa-diagram-project header-icon"></i></td>
<td>
<code><span class="blue-text"># HERCULES diff1, diff2, and sum files</span></code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_AlphaCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_CSFWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_TissCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_rawWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_amplMets_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_diff<span class="blue-text">{1|2|sum}</span>_tCr_Voxel_1_Basis_1</code><br>
    <code>img_osprey_HERCULES_qm_processed_spectra</code><br><br>
    <code><span class="blue-text"># Unedited files</span></code><br>
    <code>img_osprey_unedited_A_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_AlphaCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_CSFWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_TissCorrWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_rawWaterScaled_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_amplMets_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_A_tCr_Voxel_1_Basis_1</code><br>
    <code>img_osprey_unedited_qm_processed_spectra</code><br><br>
    <a href="mri/tables/osprey.html" target="_blank">See full file list →</a>
    </td>
</tr>
</tbody>
</table>
</div>

<div id="sensors" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-microchip"></i></span>
  <span class="text-with-link">
  <span class="text">Novel Technologies & Wearable Sensors</span>
  <a class="anchor-link" href="#sensors" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><i class="fa-solid fa-folder-open header-icon"></i> File-based data</p>
<ul>
<li>Raw BIDS stored under subject- and session-specific <a href="sensors/wearsensors/#rawbids" target="_blank"><code>motion/</code></a> folders</li>
<li>Processed derivatives output by the <a href="sensors/wearsensors/#derivatives" target="_blank">HBCD-Motion</a> pipeline</li>
</ul>

<p><i class="fa-solid fa-table header-icon"></i> Tabulated Data</p>
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
<td><a href="sensors/questionnaire" target="_blank">Infant Sensor Questionnaire 1/2/3</a></td>
<td>Motor Development, Regulation (Sleep/Wake) <i>(Day 1/2/3)</i></td>
<td><code>nt_ch_sens__qtn_<span class="blue-text">{1|2|3}</span></code></td>
</tr>
<tr>
<td><a href="sensors/wearsensors" target="_blank">Biosensor Receipt</a></td>
<td>Administrative</td>
<td><code>nt_ch_sens_rcpt</code></td>
</tr>
<tr>
<td><a href="sensors/wearsensors" target="_blank">Biosensor Setup</a></td>
<td>Administrative</td>
<td><code>nt_ch_sens_setup</code></td>
</tr>
</tbody>
</table>
</div>







