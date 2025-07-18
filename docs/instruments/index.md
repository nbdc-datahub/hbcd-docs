# Study Instruments
The current release includes data from **Visits 1, 2, and 3 (V01, V02, and V03)** for the majority of measures. In this section we provide a brief overview of each study instrument *for those provided in the current release*, including, where applicable, details of implementation and data collection, scoring procedures, quality control procedures, known issues, and references. See [Upcoming Updates](../changelog/pending.md) for details on what to expect in future releases.

<p>
<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">
    Visit numbers are labeled as Visit X or V0X in the release notes (e.g., V01 = Visit 1). 
  </span>
</div>
</p>

<img src="https://hbcdstudy.org/wp-content/uploads/2025/03/HBCD_Timeline_March2025_Updated.png" width="80%" height="auto" class="center">

HBCD Study data includes both **tabulated data** and **file-based data** (see [overview of data structure](../datacuration/overview.md)):

- **Tabulated data** are in table format and include behavior, demographics, visit data, toxicology results, and tabulated data associated with brain imaging and other file-based data ([see details](../datacuration/phenotypes.md)). 
- **File-based data** are in BIDS format and include both <span><i class="fas fa-hammer"></i> <b>Raw BIDS</b></span> ([details](../datacuration/rawbids.md)) and processed <span><i class="fas fa-cog"></i> <b>Derivatives</b></span> ([details](../datacuration/derivatives.md)) for MRI, MRS, EEG, and motion/accelerometry. 

Expand each section below to see a list of study instruments associated with each domain included in Release 1.0, including the table names for **tabulated data** and links to information for associated **file-based data** where relevant.

### Demographics & Visit Information
<div id="demo" class="table-banner" onclick="toggleCollapse(this)">
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
      <th style="width: 20%; text-align: center;">Name of Instrument</th>
      <th style="width: 20%; text-align: center;">Acronym</th>
      <th style="width: 40%; text-align: center;">Construct</th>
      <th style="width: 20%; text-align: center;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="demo/basicdemo" target="_blank">Basic Demographics</a></td>
    <td style="word-wrap: break-word; white-space: normal;">Demographics</td>
    <td style="word-wrap: break-word; white-space: normal;">Demographics data derived from multiple sources</td>
    <td style="word-wrap: break-word; white-space: normal;"><code>sed_basic_demographics</code></td>
  </tr>
    <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="demo/visitinfo" target="_blank">Visit Information</a></td>
    <td style="word-wrap: break-word; white-space: normal;">Visit Information</td>
    <td style="word-wrap: break-word; white-space: normal;">Participant visit information</td>
    <td style="word-wrap: break-word; white-space: normal;"><code>par_visit_data</code></td>
  </tr>
  </tbody>
  </table>
</div>

### Behavior, Biology, & Environment
<div id="bcgi" class="table-banner" onclick="toggleCollapse(this)">
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
      <th style="width: 50%; text-align: center;">Name of Instrument</th>
      <th style="width: 20%; text-align: center;">Acronym</th>
      <th style="width: 40%; text-align: center;">Construct</th>
      <th style="width: 20%; text-align: center;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="bcgi/ecpromis" target="_blank">Early Childhood Patient-Reported Outcome Measurement Information System Child/Caregiver Relationship Scale</a></td>
    <td style="word-wrap: break-word; white-space: normal;">ecPROMIS</td>
    <td style="word-wrap: break-word; white-space: normal;">Relationships</td>
    <td><code>mh_cg_pms__cc__inf</code></td>
  </tr>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="bcgi/ibqr" target="_blank">Infant Behavior Questionnaire &ndash; Revised Very Short Form + Behavior Inhibition</a></td>
    <td style="word-wrap: break-word; white-space: normal;">IBQ-R (VSF)+BI</td>
    <td style="word-wrap: break-word; white-space: normal;">Temperamental Surgency/Extraversion, Negative Affectivity, Effortful Control, and Behavioral Inhibition</td>
    <td><code>mh_cg_ibqr</code></td>
  </tr>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="bcgi/maps-tl" target="_blank">Multidimensional Assessment Profiles - Temper Loss scale</a></td>
    <td style="word-wrap: break-word; white-space: normal;">MAPS-TL</td>
    <td style="word-wrap: break-word; white-space: normal;">Irritability</td>
    <td><code>mh_cg_mapdb__inf</code></td>
  </tr>
  </tbody>
  </table>
</div>


<div id="biospec" class="table-banner" onclick="toggleCollapse(this)">
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
      <th style="width: 20%; text-align: center;">Name of Instrument</th>
      <th style="width: 20%; text-align: center;">Acronym</th>
      <th style="width: 40%; text-align: center;">Construct</th>
      <th style="width: 20%; text-align: center;">Table Name</th>
    </tr>
  </thead>
  <tbody>
      <tr>
      <td style="text-align: left;"><a href="biospec/nails" target="_blank">Nails Toxicology Screen</a></td>
      <td style="text-align: left;">Nails</td>
      <td style="text-align: left;">Toxicology Screen</td>
      <td style="text-align: left;"><code>bio_bm_biosample_nails</code></td>
    </tr>
    <tr>
        <td style="text-align: left;"><a href="biospec/urine" target="_blank">Urine Toxicology Screen</a></td>
        <td style="text-align: left;">Urine</td>
        <td style="text-align: left;">Toxicology Screen</td>
        <td style="text-align: left;"><code>bio_bm_biosample_urine</code></td>
    </tr>
  </tbody>
  </table>
</div>

<div id="neurocog" class="table-banner" onclick="toggleCollapse(this)">
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
      <th style="width: 50%; text-align: center;">Name of Instrument</th>
      <th style="width: 10%; text-align: center;">Acronym</th>
      <th style="width: 30%; text-align: center;">Construct</th>
      <th style="width: 10%; text-align: center;">Table Name</th>
    </tr>
  </thead>
  <tbody>
   <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="neurocog/mlds" target="_blank">Multilingual Language Development Screener</a></td>
      <td style="word-wrap: break-word; white-space: normal;">MLDS</td>
      <td style="word-wrap: break-word; white-space: normal;">Multilingual exposure</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>ncl_ch_mlds</code></td>
    </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="neurocog/spm2" target="_blank">Sensory Processing Measure – Infant/Toddler</a></td>
      <td style="word-wrap: break-word; white-space: normal;">SPM-2</td>
      <td style="word-wrap: break-word; white-space: normal;">Sensory processing</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>ncl_cg_spm2__inf</code></td>
    </tr>
  </tbody>
  </table>
</div>

<div id="sensors" class="table-banner" onclick="toggleCollapse(this)">
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
      <th style="width: 10%; text-align: center;">Name of Instrument</th>
      <th style="width: 20%; text-align: center;">Acronym</th>
      <th style="width: 20%; text-align: center;">Construct</th>
      <th style="width: 10%; text-align: center;">Table Name</th>
      <th style="width: 40%; text-align: center;">File-Based Data<br>
          <i class="fas fa-hammer"></i> &nbsp;<i>Raw BIDS</i><br>
          <i class="fas fa-cog"></i> &nbsp;<i>Derivatives</i></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="sensors/wearsensors" target="_blank">Wearable Sensors</a></td>
      <td style="word-wrap: break-word; white-space: normal;">Channel setup</td>
      <td style="word-wrap: break-word; white-space: normal;">N/A</td>
      <td style="word-wrap: break-word; white-space: normal;">N/A</td>
      <td style="word-wrap: break-word; white-space: normal;">
      <i class="fa fa-hammer"></i> &nbsp;<a href="../datacuration/rawbids/#motion"><code>motion/</code></a><br>
      <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#hbcd-motion-hbcd_motion">HBCD-Motion</a>
      </td>
    </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="sensors/questionnaire" target="_blank">Infant Sensor Questionnaire</a></td>
      <td style="word-wrap: break-word; white-space: normal;">N/A</td>
      <td style="word-wrap: break-word; white-space: normal;">Motor behavior, physical activity, sleep</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>nt_ch_sens__qtn_1</code><br>
          <code>nt_ch_sens__qtn_2</code><br>
          <code>nt_ch_sens__qtn_3</code></td>
      <td style="word-wrap: break-word; white-space: normal;">NA</td>
    </tr>
  </tbody>
  </table>
</div>

<div id="physhealth" class="table-banner" onclick="toggleCollapse(this)">
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
      <th style="width: 40%; text-align: center;">Name of Instrument</th>
      <th style="width: 20%; text-align: center;">Acronym</th>
      <th style="width: 30%; text-align: center;">Construct</th>
      <th style="width: 10%; text-align: center;">Table Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="physhealth/bf" target="_blank">Breast Feeding History</a></td>
      <td style="word-wrap: break-word; white-space: normal;">PHENX BF</td>
      <td style="word-wrap: break-word; white-space: normal;">Nutrition</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>ph_cg_phx__bfh</code></td>
    </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="physhealth/foodinsecurity" target="_blank">2-item Food Insecurity</a></td>
      <td style="word-wrap: break-word; white-space: normal;">USDA short form</td>
      <td style="word-wrap: break-word; white-space: normal;">Food insecurity</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>sed_cg_foodins</code></td>
    </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="physhealth/growth" target="_blank">Height/Weight/Head Circumference</a></td>
      <td style="word-wrap: break-word; white-space: normal;">Growth</td>
      <td style="word-wrap: break-word; white-space: normal;">Growth</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>ph_ch_anthro</code></td>
  </tr> 
  </tbody>
  </table>
</div>



<div id="pregexp" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Pregnancy & Exposure, Including Substance Use</span>
  <a class="anchor-link" href="#pregexp" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<br>
<p style="margin-bottom: 5px; font-size: 1.2em; text-align: center;">&nbsp; <strong>Pregnancy & Infant Health</strong></p>

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 30%; text-align: center;">Name of Instrument</th>
      <th style="width: 20%; text-align: center;">Acronym</th>
      <th style="width: 30%; text-align: center;">Construct</th>
      <th style="width: 10%; text-align: center;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/preghealth/healthhx" target="_blank">Pregnancy Health</a></td>
      <td style="word-wrap: break-word; white-space: normal;">Healthhx</td>
      <td style="word-wrap: break-word; white-space: normal;">Pre-pregnancy and pregnancy health</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_health_preg__healthhx</code></td>
    </tr>          
    <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/preghealth/vacc" target="_blank">Pregnancy Health-Exposures and Vaccines</a></td>
    <td style="word-wrap: break-word; white-space: normal;">Vacc</td>
    <td style="word-wrap: break-word; white-space: normal;">Vaccines in pregnancy</td>
    <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_health_preg__exp__vacc</code></td>
  </tr>    
  <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/preghealth/chronconditions" target="_blank">Pregnancy Health-Chronic Conditions</a></td>
    <td style="word-wrap: break-word; white-space: normal;">Exp I chroncond</td>
    <td style="word-wrap: break-word; white-space: normal;">Chronic conditions and sexually transmitted infections in pregnancy</td>
    <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_health_preg__chroncond</code></td>
  </tr>  
  <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/preghealth/illness" target="_blank">Pregnancy Health-Illness</a></td>
    <td style="word-wrap: break-word; white-space: normal;">Exp I illness</td>
    <td style="word-wrap: break-word; white-space: normal;">Illness in pregnancy</td>
    <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_health_preg__illness</code></td>
  </tr>     
  <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/preghealth/er-hosp" target="_blank">Pregnancy Health-ER/Hospitalizations</a></td>
    <td style="word-wrap: break-word; white-space: normal;">Exp I ERhosp</td>
    <td style="word-wrap: break-word; white-space: normal;">ER visit or hospitalization in pregnancy</td>
    <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_health_preg__erhosp</code></td>
  </tr>  
  <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/preghealth/medications" target="_blank">Pregnancy Health-Medications</a></td>
    <td style="word-wrap: break-word; white-space: normal;">Exp I Meds</td>
    <td style="word-wrap: break-word; white-space: normal;">Prescription and over the counter medications in pregnancy</td>
    <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_health_preg__meds</code></td>
  </tr>  
  <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/preghealth/end-preg" target="_blank">Pregnancy Health-V2 (End of Pregnancy)</a></td>
    <td style="word-wrap: break-word; white-space: normal;">Healthv2 Preg</td>
    <td style="word-wrap: break-word; white-space: normal;">Updates information between enrollment and delivery</td>
    <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_healthv2_preg</code></td>
  </tr>     
  <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/preghealth/infanthealth" target="_blank">Infant health- V2</a></td>
    <td style="word-wrap: break-word; white-space: normal;">Healthv2 Inf</td>
    <td style="word-wrap: break-word; white-space: normal;">Delivery and birth outcomes</td>
    <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_healthv2_inf</code></td>
  </tr>    
</tbody>
</table>

<p style="margin-bottom: 5px; font-size: 1.2em; text-align: center;">&nbsp; <strong>Mental Health</strong></p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 30%; text-align: center;">Name of Instrument</th>
      <th style="width: 10%; text-align: center;">Acronym</th>
      <th style="width: 30%; text-align: center;">Construct</th>
      <th style="width: 10%; text-align: center;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/mh/fam-mh" target="_blank">Personal and family psychiatric history</a></td>
      <td style="word-wrap: break-word; white-space: normal;">FAM MH</td>
      <td style="word-wrap: break-word; white-space: normal;">Personal and family mental health</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_psych</code></td>
    </tr>            
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/mh/apa12" target="_blank">DSM-5 Self-Rated Level 1 and Level 2 (version 8a) Cross-Cutting Symptom Measure—Adult</a></td>
      <td style="word-wrap: break-word; white-space: normal;">APA 1/2</td>
      <td style="word-wrap: break-word; white-space: normal;">Mental Health</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_apa</code></td>
    </tr>  
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/mh/ptsd" target="_blank">National Stressful Events Survey- PTSD Short Scale/Acute Stress Disorder</a></td>
      <td style="word-wrap: break-word; white-space: normal;">NSESSS—PTSD/Acute Stress Disorder</td>
      <td style="word-wrap: break-word; white-space: normal;">PTSD/acute stress disorder symptom severity</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_str__ptsd</code></td>
    </tr>      
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/mh/epds" target="_blank">Edinburgh Postnatal Depression Scale</a></td>
      <td style="word-wrap: break-word; white-space: normal;">EPDS</td>
      <td style="word-wrap: break-word; white-space: normal;">Postnatal depression</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_epds</code></td>
    </tr>      
  </tbody>
  </table>

<p style="margin-bottom: 5px; font-size: 1.2em; text-align: center;">&nbsp; <strong>Substance Use</strong></p>

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 30%; text-align: center;">Name of Instrument</th>
      <th style="width: 10%; text-align: center;">Acronym</th>
      <th style="width: 30%; text-align: center;">Construct</th>
      <th style="width: 10%; text-align: center;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/su/assist" target="_blank">Alcohol, Smoking and Substance Involvement Screening Test V1.0</a></td>
    <td>Assist V1</td>
    <td style="word-wrap: break-word; white-space: normal;">Substance use and problematic use before and during pregnancy</td>
    <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_assistv1</code></td>
  </tr>    
  <tr>
    <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/su/assist" target="_blank">Alcohol, Smoking and Substance Involvement Screening Test V2.0</a></td>
    <td style="word-wrap: break-word; white-space: normal;">Assist V2</td>
    <td style="word-wrap: break-word; white-space: normal;">Substance use during end of pregnancy ( between V1 and delivery) and postnatal (weeks 0-4, between delivery and V2)</td>
    <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_assistv2</code></td>
  </tr>    
  <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/su/assist" target="_blank">Alcohol, Smoking and Substance Involvement Screening Test V3.0</a></td>
      <td style="word-wrap: break-word; white-space: normal;">Assist V3</td>
      <td style="word-wrap: break-word; white-space: normal;">Substance use after pregnancy</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_assistv3</code></td>
  </tr>   
  <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="pregexp/su/tlfb" target="_blank">Timeline Follow Back</a></td>
      <td style="word-wrap: break-word; white-space: normal;">TLFB</td>
      <td style="word-wrap: break-word; white-space: normal;">Substance use before and during pregnancy</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>pex_ch_tlfb</code></td>
  </tr>   
  </tbody>
  </table>
</div>


<div id="socenvdet" class="table-banner" onclick="toggleCollapse(this)">
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
      <th style="width: 30%; text-align: center;">Name of Instrument</th>
      <th style="width: 20%; text-align: center;">Acronym</th>
      <th style="width: 30%; text-align: center;">Construct</th>
      <th style="width: 10%; text-align: center;">Table Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="SED/bfy" target="_blank">Baby’s First Years – Benefits/Services/Economic Stress</a></td>
      <td style="word-wrap: break-word; white-space: normal;">BFY</td>
      <td style="word-wrap: break-word; white-space: normal;">Benefits/Services/Economic Stress</td>
      <td style="word-wrap: break-word; white-space: normal;"><code>sed_bm_bfy</code></td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;"><a href="SED/discr" target="_blank">Experiences of Unfair Treatment</a></td>
        <td style="word-wrap: break-word; white-space: normal;">PhenX+ Discrimination</td>
        <td style="word-wrap: break-word; white-space: normal;">Experiences of Unfair Treatment</td>
        <td style="word-wrap: break-word; white-space: normal;"><code>sed_bm_phx__discr</code></td>
    </tr>   
    <tr>
          <td style="word-wrap: break-word; white-space: normal;"><a href="SED/ehits" target="_blank">Extended – Hurt, Insult, Threaten, Scream</a></td>
          <td style="word-wrap: break-word; white-space: normal;">eHITS</td>
          <td style="word-wrap: break-word; white-space: normal;">Intimate Partner Violence</td>
          <td style="word-wrap: break-word; white-space: normal;"><code>sed_bm_ehits</code></td>
      </tr>  
      <tr>
          <td style="word-wrap: break-word; white-space: normal;"><a href="SED/v01-demo" target="_blank">HBCD Demographics V01</a></td>
          <td style="word-wrap: break-word; white-space: normal;">Demographics</td>
          <td style="word-wrap: break-word; white-space: normal;">Basic social characteristics related to the birthing parent, the other biological parent, and their household</td>
          <td style="word-wrap: break-word; white-space: normal;"><code>sed_bm_demo</code></td>
      </tr>     
      <tr>
          <td style="word-wrap: break-word; white-space: normal;"><a href="SED/promis" target="_blank">Patient-Reported Outcome Measurement Information System</a></td>
          <td style="word-wrap: break-word; white-space: normal;">PROMIS</td>
          <td style="word-wrap: break-word; white-space: normal;">Perceived Stress/Social Support</td>
          <td style="word-wrap: break-word; white-space: normal;"><code>sed_bm_strsup</code></td>
      </tr> 
      <tr>
          <td style="word-wrap: break-word; white-space: normal;"><a href="SED/safety" target="_blank">PhenX+ Toolkit Neighborhood Safety</a></td>
          <td style="word-wrap: break-word; white-space: normal;">Neighborhood Safety</td>
          <td style="word-wrap: break-word; white-space: normal;">Neighborhood Safety</td>
          <td style="word-wrap: break-word; white-space: normal;"><code>sed_bm_nbhsaf</code></td>
      </tr>          
      <tr>
          <td style="word-wrap: break-word; white-space: normal;"><a href="SED/paces" target="_blank">Protective and Compensatory Experience</a></td>
          <td style="word-wrap: break-word; white-space: normal;">PACES</td>
          <td style="word-wrap: break-word; white-space: normal;">Protective Factors</td>
          <td style="word-wrap: break-word; white-space: normal;"><code>sed_bm_paces</code></td>
      </tr>      
  </tbody>
  </table>
  </div>

### Brain Activity - MRI & EEG

<div id="mri" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">MRI & MRS</span>
  <a class="anchor-link" href="#mri" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong><span class="emoji"><i class="fa-regular fa-lightbulb"></i></span> Also see <a href="mri">Overview & MRI Protocols</a> and <a href="mri/qc"> HBCD MR Quality Control Procedures</a></strong></p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
  <thead>
    <tr>
      <th style="width: 10%; text-align: center;">Name</th>
      <th style="width: 30%; text-align: center;">File-Based Data<br>
      <i class="fas fa-hammer"></i> &nbsp;<i>Raw BIDS</i><br>
      <i class="fas fa-cog"></i> &nbsp;<i>Derivatives</i></th>
      <th style="width: 60%; text-align: center;">Table Name(s)</th>
    </tr>
  </thead>
  <tbody>
<!-- sMRI -->
    <tr>
      <td rowspan="6"><span class="tooltip tooltip-right">
          <a href="mri/smri" target="_blank">sMRI</a>
          <span class="tooltiptext">Structural MRI</span>
          </span>
      </td>
      <td rowspan="6" style="word-wrap: break-word; white-space: normal;">
      <i class="fas fa-hammer"></i> &nbsp;<a href="../datacuration/rawbids/#anatomical-anat"><code>anat/</code></a><br>
      <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#bibsnet-bibsnet">BIBSNet</a><br>
      <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#mriqc-mriqc">MRIQC</a><br>
      <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#xcp-d-xcp_d">XCP-D</a>
      </td>
      <td><code>img_brainswipes_xcpd-T2w</td>
    </tr>
    <tr><td><code>img_mriqc_&lt;T1w|T2w&gt;</code></td></tr>
    <tr><td><code>img_bibsnet_space-&lt;T1w|T2w&gt;_desc-aseg_volumes</code></td></tr>
    <tr><td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-A&gt;</span>_stat-mean_desc-curv_morph</code></td></tr>
    <tr><td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-A&gt;</span>_stat-mean_desc-sulc_morph</code></td></tr>
    <tr><td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-A&gt;</span>_stat-mean_desc-thickness_morph</code></td></tr>
<!-- fMRI -->
    <tr>
      <td rowspan="5"><span class="tooltip tooltip-right">
        <a href="mri/fmri" target="_blank">fMRI</a>
        <span class="tooltiptext">Functional MRI</span>
        </span>
      </td>
      <td rowspan="5" style="word-wrap: break-word; white-space: normal;">
      <i class="fas fa-hammer"></i> &nbsp;<a href="../datacuration/rawbids/#functional-func-and-fieldmaps-fmap"><code>func/</code></a><br>
      <i class="fas fa-hammer"></i> &nbsp;<a href="../datacuration/rawbids/#functional-func-and-fieldmaps-fmap"><code>fmap/</code></a><br>
      <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#infant-fmriprep-nibabies">Infant-fMRIPrep</a><br>
      <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#xcp-d-xcp_d">XCP-D</a>
      </td>
      <td><code>img_brainswipes_xcpd-bold</td>
    </tr>
    <tr><td><code>img_mriqc_bold</td></tr>
    <tr><td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-F&gt;</span>_stat-alff_bold</code></td></tr>
    <tr><td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-F&gt;</span>_stat-coverage_bold</code></td></tr>
    <tr><td><code>img_xcpd_space-fsLR_seg-<span class="blue-text">&lt;SEG-F&gt;</span>_stat-reho_bold</code></td></tr>
<!-- dMRI -->
    <tr>
    <td><span class="tooltip tooltip-right">
        <a href="mri/dmri" target="_blank">dMRI</a>
        <span class="tooltiptext">Diffusion MRI</span>
        </span>
    </td>
      <td style="word-wrap: break-word; white-space: normal;">
      <i class="fas fa-hammer"></i> &nbsp;<a href="../datacuration/rawbids/#diffusion-dwi"><code>dwi/</code></a><br>
      <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#qsiprep-qsiprep">QSIPrep</a><br>
      <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#qsirecon">QSIRecon</a>
      </td>
      <td><code>img_qsiprep_space-ACPC_desc-image_qc</code></td>
    </tr>
    <!-- qMRI -->
    <tr>
    <td><span class="tooltip tooltip-right">
        <a href="mri/qmri" target="_blank">qMRI</a>
        <span class="tooltiptext">Quantitative MRI</span>
        </span>
    </td>
      <td style="word-wrap: break-word; white-space: normal;">
      <i class="fa fa-hammer"></i> &nbsp;<a href="../datacuration/rawbids/#diffusion-dwi"><code>anat/</code></a><br>
      <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#symri-symri">SyMRI</a><br>
      <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#qmri-postproc-qmri_postproc">qMRI Postproc</a>
      </td>
      <td>N/A</td>
    </tr>
    <!-- MRS -->
    <tr>
      <td rowspan="9">
      <span class="tooltip tooltip-right">
        <a href="mri/mrs" target="_blank">MRS</a>
        <span class="tooltiptext">Magnetic Resonance Spectroscopy</span>
      </span>
      </td>
      <td rowspan="9" style="word-wrap: break-word; white-space: normal;">
        <i class="fas fa-hammer"></i> &nbsp;<a href="../datacuration/rawbids/#mr-spectroscopy-mrs"><code>mrs/</code></a><br>
        <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#osprey-bids-osprey">OSPREY-BIDS</a>
      </td>
      <td><code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_AlphaCorrWaterScaledGroupNormed_Voxel_1_Basis_1</code></td>
    </tr>
    <tr><td><code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_AlphaCorrWaterScaled_Voxel_1_Basis_1</code></td></tr>
    <tr><td><code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_CSFWaterScaled_Voxel_1_Basis_1</code></td></tr>
    <tr><td><code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_TissCorrWaterScaled_Voxel_1_Basis_1</code></td></tr>
    <tr><td><code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_rawWaterScaled_Voxel_1_Basis_1</code></td></tr>
    <tr><td><code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_amplMets_Voxel_1_Basis_1</code></td></tr>
    <tr><td><code>img_osprey_<span class="blue-text">&lt;PROC&gt;</span>_tCr_Voxel_1_Basis_1</code></td></tr>
    <tr><td><code>img_osprey_HERCULES_qm_processed_spectra</code></td></tr>
    <tr><td><code>img_osprey_unedited_qm_processed_spectra</code></td></tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="3" style="word-wrap: break-word; white-space: normal; padding: 10px;">
          <li><b class="blue-text">&lt;SEG-A&gt;</b> label values: 4S&lt;1-10&gt;Parcels, Glasser, Gordon, MIDB, MyersLabonte</li>
          <li><b class="blue-text">&lt;SEG-F&gt;</b> label values: 4S&lt;1-10&gt;Parcels, Glasser, Gordon, MIDB, MyersLabonte, HCP, Tian</li>
          <li><b class="blue-text">&lt;PROC&gt;</b> label values: HERCULES_&lt;diff1|diff2|sum&gt;, unedited_A</li>
      </td>
    </tr>
  </tfoot>
</table>
</div>


<div id="eeg" class="table-banner" onclick="toggleCollapse(this)">
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
    <tr>
      <th style="width: 25%; text-align: center;">Task</th>
      <th style="width: 25%; text-align: center;">File-Based Data<br>
        <i class="fas fa-hammer"></i> &nbsp;<i>Raw BIDS</i><br>
        <i class="fas fa-cog"></i> &nbsp;<i>Derivatives</i></th>
      <th style="width: 60%; text-align: center;">Table Name</th>
    </tr>
  </thead>
  <tbody>
      <tr>
        <td rowspan="2" style="word-wrap: break-word; white-space: normal;"><a href="eeg/mmn" target="_blank">Auditory Mismatch Negativity (MMN)</a></td>
        <td rowspan="2" style="word-wrap: break-word; white-space: normal;">
          <i class="fas fa-hammer"></i> &nbsp;<a href="../datacuration/rawbids/#eeg"><code>eeg/</code></a><br>
          <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#hbcd-made-made">HBCD-MADE</a>
        </td>
        <td><code>eeg_made_task-MMN_acq-eeg_preprocessingReport</code></td>
      </tr>
      <tr>
        <td><code>eeg_qc_task-MMN</code></td>
      </tr>
      <tr>
        <td rowspan="2" style="word-wrap: break-word; white-space: normal;"><a href="eeg/faces" target="_blank">Faces (Face)</a></td>
          <td rowspan="2" style="word-wrap: break-word; white-space: normal;">
          <i class="fas fa-hammer"></i> &nbsp;<a href="../datacuration/rawbids/#eeg"><code>eeg/</code></a><br>
          <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#hbcd-made-made">HBCD-MADE</a>
        </td>
        <td><code>eeg_made_task-FACE_acq-eeg_preprocessingReport</code></td>
      </tr>
      <tr>
        <td><code>eeg_qc_task-FACE</code></td>
      </tr>
      <tr>
        <td rowspan="2" style="word-wrap: break-word; white-space: normal;"><a href="eeg/videors" target="_blank">Video Resting State (RS)</a></td>
          <td rowspan="2" style="word-wrap: break-word; white-space: normal;">
          <i class="fas fa-hammer"></i> &nbsp;<a href="../datacuration/rawbids/#eeg"><code>eeg/</code></a><br>
          <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#hbcd-made-made">HBCD-MADE</a>
        </td>
        <td><code>eeg_made_task-RS_acq-eeg_preprocessingReport</code></td>
      </tr>
      <tr>
        <td><code>eeg_qc_task-RS</code></td>
      </tr>
      <tr>
        <td rowspan="2" style="word-wrap: break-word; white-space: normal;"><a href="eeg/vep" target="_blank">Visual Evoked Potential (VEP)</a></td>
          <td rowspan="2" style="word-wrap: break-word; white-space: normal;">
          <i class="fas fa-hammer"></i> &nbsp;<a href="../datacuration/rawbids/#eeg"><code>eeg/</code></a><br>
          <i class="fas fa-cog"></i> &nbsp;<a href="../datacuration/derivatives/#hbcd-made-made">HBCD-MADE</a>
        </td>
        <td><code>eeg_made_task-VEP_acq-eeg_preprocessingReport</code></td>
      </tr>
      <tr>
        <td><code>eeg_qc_task-VEP</code></td>
      </tr>
    </tbody>
  </table>
  </div>



  <p>
<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">
    Additional Resources
  </span>
</div>
<div class="notification-static-content">
<p><b>Explore HBCD Study Data before Obtaining Data Access</b><br> 
Users can explore the HBCD Study data dictionary via <a href="https://hbcd.deapscience.com/#/my-datasets/create-dataset">DEAP's data dictionary & ontology browser</a> or <a href="https://nbdc-datashare.lassoinformatics.com">Lasso's Query Tool</a> before obtaining a data use certification (DUC). To create custom datasets and download data, users need an active DUC - <a href="../../access/download">see details</a>.</p>
<p><b>Study Protocols</b><br> 
Full study protocols are available on the <a href="https://hbcdstudy.org/study-protocols/">HBCD Study site</a>.</p> 
</div>
</p>