# USDTL Nails Toxicology (Maternal)

<div class="info-block">
  <div class="info-row">
    <div class="info-label"><i class="fa fa-table"></i> Table Name:</div>
    <div class="info-value"><code>bio_bm_biosample_nails_results</code> (toxicology screen), <code>bio_bm_biosample_nails_type</code> (specimen type)</div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-tape"></i> Construct:</div>
    <div class="info-value">Drug, Environmental Exposure</div>
  </div>
</div>

---------------------------------------------

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</i></span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p><b>Continuous Variables</b><br>
For all toxicology screens, continuous variables should be interpreted with caution based on the threshold limits of quantification (LOQs), or the cutoff concentration used to categorize metabolites as positive or negative. LOQs are provided in <a href="#nails-table1">Table 1. Nail Assay Thresholds</a>.</p> 
<p><b>Updated Workflow</b><br>
As of July 1, 2024, the nail processing workflow was updated to optimize specimen use and allow confirmation testing for low sample quantities. Prior to this update, remnants of ELISA extract were not used for confirmation when specimens had insufficient sample.</p> 
<p><b>Large Gaps Between Collection and Analysis Dates</b><br> A substantial number of samples show unusually long intervals between collection and analysis (e.g., over 100–300 days, compared to the 30-day limit specified by internal SOPs). We are working to determine whether this reflects a data entry or site-level issue and will provide an update once more information is available.</p>
</div>

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">This data has known issues - <a href="../../../changelog/knownissues/#biospecimen-omics" target="_blank">see details</a>.</span>
</div>
<p></p>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Respondent</b></td>
<td>Pregnant/postpartum person</td></tr>
<tr><td><b>Administration</b></td>
<td>Self-collected under research team supervision, or collected by research team</td></tr>
<tr><td><b>Visits</b></td>
<td>V01, V02</td></tr>
<tr><td><b>Completion Time</b></td>
<td>5 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td>Examine assay ranges and categorical versus continuous measures.</td></tr>
</tbody>
</table>

## Instrument Details

For the USDTL assay, fingernail and toenail specimens are sorted by weight, and those weighing at least 20 mg undergo ELISA screening, followed by LCMSMS confirmation for presumptive positives, each requiring an additional 20 mg. If insufficient specimen remains for LCMSMS, the remnant ELISA extract is used for confirmation.  Please note that as of November 2025, USDTL no longer assayed sufentanil in the nail samples.

<img src="../images/Fig1_nails.png" width="70%" height="auto" class="center">

Based on the predefined threshold outlined in [Table 1](#nails-table1), a confirmatory test result for any substance analyte is determined to be positive, negative, or invalid (*QNS* i.e. *quantity not sufficient*). Substance analytes (e.g. **Amphetamine/`c_amp_n`**) are grouped into different classes by analyte screening tests and confirmatory tests (**[Table 2](#nails-table2)**). 

<div id="nails-table1" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-table"></i></span>
  <span class="text-with-link">
  <span class="text">Table 1. Nail Assay Thresholds</span>
  <a class="anchor-link" href="#nails-table1" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
    <tr>
    <th style="width: 30%;">Analyte</th>
    <th style="width: 20%;"><span class="tooltip tooltip-bottom">LOD
                <span class="tooltiptext">Limit of detection</span>
            </span> (pg/mL)</th>
    <th style="width: 10%;"><span class="tooltip tooltip-bottom">LOQ
                <span class="tooltiptext">Limit of quantification</span>
            </span> (pg/mL)</th>
    <th style="width: 10%;">Cutoff (pg/mL)</th>
    <th style="width: 40%;">Detection Window (months)</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>Amphetamine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Methamphetamine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>MDA</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>MDMA</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>MDEA</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Carboxy-delta-9-THC</td>
        <td>0.01</td>
        <td>0.02</td>
        <td>0.05</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Cocaine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Cocaethylene</td>
        <td>10</td>
        <td>20</td>
        <td>50</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Benzoylecgonine</td>
        <td>10</td>
        <td>20</td>
        <td>50</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Norcocaine</td>
        <td>10</td>
        <td>20</td>
        <td>50</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>6-MAM</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Codeine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Hydrocodone</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Hydromorphone</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Morphine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Norhydrocodone</td>
        <td>8</td>
        <td>16</td>
        <td>40</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Oxycodone</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Oxymorphone</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Noroxycodone</td>
        <td>8</td>
        <td>16</td>
        <td>40</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Methadone</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>EDDP</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Amobarbital</td>
        <td>80</td>
        <td>80</td>
        <td>200</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Butalbital</td>
        <td>80</td>
        <td>80</td>
        <td>200</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Pentobarbital</td>
        <td>80</td>
        <td>80</td>
        <td>200</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Phenobarbital</td>
        <td>80</td>
        <td>80</td>
        <td>200</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Secobarbital</td>
        <td>80</td>
        <td>80</td>
        <td>200</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Alprazolam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Diazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Midazolam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Nordiazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Oxazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Temazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Ketamine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Norketamine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Tramadol</td>
        <td>200</td>
        <td>400</td>
        <td>500</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Fentanyl</td>
        <td>2</td>
        <td>4</td>
        <td>10</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Norfentanyl</td>
        <td>2</td>
        <td>4</td>
        <td>10</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Alfentanil</td>
        <td>2</td>
        <td>4</td>
        <td>10</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Acetyl Fentanyl</td>
        <td>2</td>
        <td>4</td>
        <td>10</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Acetyl Norfentanyl</td>
        <td>2</td>
        <td>4</td>
        <td>10</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Sufentanil</td>
        <td>1</td>
        <td>2</td>
        <td>5</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Norsufentanil</td>
        <td>2</td>
        <td>2</td>
        <td>5</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Buprenorphine</td>
        <td>4</td>
        <td>8</td>
        <td>20</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Norbuprenorphine</td>
        <td>4</td>
        <td>8</td>
        <td>20</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Ethyl glucuronide</td>
        <td>4</td>
        <td>8</td>
        <td>20</td>
        <td>Finger 3; Toe no consensus</td>
    </tr>
    <tr>
        <td>Nicotine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
    <tr>
        <td>Cotinine</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>Finger 3-6; Toe 10-14</td>
    </tr>
</tbody>
</table>
</div>

<div id="nails-table2" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-table"></i></span>
  <span class="text-with-link">
  <span class="text">Table 2. Mapping from Class to Screening Tests and Confirmatory Tests for Nails</span>
  <a class="anchor-link" href="#nails-table2" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead>
<tr>
    <th style="width: 20%;">Class</th>
    <th style="width: 30%;">Screening Test</th>
    <th style="width: 50%;">Confirmatory Test</th>
</tr>
</thead>
<tbody>
<tr>
    <td colspan="1" rowspan="9">Stimulant (<code>c_any_stim_n</code>)</td>
    <td colspan="1" rowspan="5">amp/mamp (<code>s_amp_n, s_mamp_n</code>)</td>
    <td>Amphetamine (<code>c_amp_n</code>)</td>
</tr>
    <tr><td>Methamphetamine (<code>c_meth_n</code>)</td></tr>
    <tr><td>MDMA (<code>c_mdma_n</code>)</td></tr>
    <tr><td>MDA (<code>c_mda_n</code>)</td></tr>
    <tr><td>MDEA (<code>c_mdea_n</code>)</td></tr>
<tr>
    <td colspan="1" rowspan="4">coc (<code>s_coc_n</code>)</td>
    <td>Cocaine (<code>c_coc_n</code>)</td>
</tr>
    <tr><td>Cocaethylene (<code>c_cocae_n</code>)</td></tr>
    <tr><td>Benzoylecgonine (<code>c_ben_n</code>)</td></tr>
    <tr><td>Norcocaine (<code>c_ncoc_n</code>)</td></tr>
<tr>
    <td>Cannabinoid (<code>c_any_cannabinoid_n</code>)</td>
    <td>thc (<code>s_thc_n</code>)</td>
    <td style="word-wrap: break-word; white-space: normal;">Carboxy-delta-9-THC (<code>c_delta-9-THC_n</code>)</td>
</tr>
<tr>
    <td colspan="1" rowspan="5">Barbiturate (<code>c_any_barb_n</code>)</td>
    <td colspan="1" rowspan="5">bar (<code>s_bar_n</code>)</td>
    <td>Amobarbital (<code>c_amobarb_n</code>)</td>
</tr>
    <tr><td>Secobarbital (<code>c_secobarb_n</code>)</td></tr>
    <tr><td>Pentobarbital (<code>c_pentobarb_n</code>)</td></tr>
    <tr><td>Phenobarbital (<code>c_phenobarb_n</code>)</td></tr>
    <tr><td>Butalbital (<code>c_butalbital_n</code>)</td>
</tr> 
<tr>
    <td colspan="1" rowspan="6" style="word-wrap: break-word; white-space: normal;">Benzodiazepine (<code>c_any_benzo_n</code>)</td>
    <td colspan="1" rowspan="6">benz (<code>s_benz_n</code>)</td>
    <td>Diazepam (<code>c_diaz_n</code>)</td></tr>
    <tr><td>Oxazepam (<code>c_oxaz_n</code>)</td></tr>
    <tr><td>Nordiazepam (<code>c_nord_n</code>)</td></tr>
    <tr><td>Temazepam (<code>c_tema_n</code>)</td></tr>
    <tr><td>Midazolam (<code>c_mida_n</code>)</td></tr>
    <tr><td>Alprazolam (<code>c_alpa_n</code>)</td>
</tr>
<tr>
    <td colspan="1" rowspan="21">Opioids (<code>c_any_opioid_n</code>)</td>
    <td colspan="1" rowspan="6">opi (<code>s_opi_n</code>)</td>
    <td>Codeine (<code>c_cod_n</code>)</td></tr>
    <tr><td>Morphine (<code>c_mor_n</code>)</td></tr>
    <tr><td>MAM (<code>c_mam_n</code>)</td></tr>
    <tr><td>Hydrocodone (<code>c_hydroc_n</code>)</td></tr>
    <tr><td>Norhydrocodone (<code>c_norh_n</code>)</td></tr>
    <tr><td>Hydromorphone (<code>c_hydrom_n</code>)</td>
</tr>
<tr>
    <td colspan="1" rowspan="2">mtd (<code>s_mtd_n</code>)</td>
    <td>Methadone (<code>c_mtd_n</code>)</td></tr>
    <tr><td>EDDP (<code>c_eddp_n</code>)</td>
</tr>
<tr>
    <td colspan="1" rowspan="3">oxyc (<code>s_oxyc_n</code>)</td>
    <td>Oxycodone (<code>c_oxyc_n</code>)</td></tr>
    <tr><td>Noroxycodone (<code>c_noxyc_n</code>)</td></tr>
    <tr><td>Oxymorphone (<code>c_oxym_n</code>)</td>
</tr>
<tr>    
    <td>tram (<code>s_tram_n</code>)</td>
    <td>Tramadol (<code>c_tram_n</code>)</td>
</tr>
<tr>
    <td colspan="1" rowspan="4">fent (<code>s_fent_n</code>)</td>
    <td>Fentanyl (<code>c_fent_n</code>)</td></tr>
    <tr><td>Norfentanyl (<code>c_nfent_n</code>)</td></tr>
    <tr><td>Acetylfentanyl (<code>c_acfent_n</code>)</td></tr>
    <tr><td>ActlNorfentanyl (<code>c_acnfent_n</code>)</td>
</tr>
<tr>
    <td colspan="1" rowspan="3">suf (<code>s_suf_n</code>)</td>
    <td>Alfentanil (<code>c_afent_n</code>)</td></tr>
    <tr><td>Sufentanil (<code>c_suf_n</code>)</td></tr>
    <tr><td>Norsufentanil (<code>c_nsuf_n</code>)</td>
</tr>
<tr>
    <td colspan="1" rowspan="2">bup (<code>s_bup_n</code>)</td>
    <td>Buprenorphine (<code>c_bup_n</code>)</td></tr>
    <tr><td>Norbuprenorpine (<code>c_nbup_n</code>)</td>
</tr>
<tr>
    <td colspan="1" rowspan="2" style="word-wrap: break-word; white-space: normal;">dissociative anesthetic (<code>c_disanesth_n</code>)</td>
    <td colspan="1" rowspan="2">ket (<code>s_ket_n</code>)</td>
    <td>Ketamine (<code>c_ket_n</code>)</td>
    </tr><tr><td>Norketamine (<code>c_nket_n</code>)</td>
</tr>
<tr>
    <td colspan="1" rowspan="2">Nicotine (<code>c_nicotine_n</code>)</td>
    <td colspan="1" rowspan="2">cot (<code>s_cot_n</code>)</td>
    <td>Nicotine (<code>c_nic_n</code>)</td></tr>
    <tr><td>Cotinine (<code>c_cot_n</code>)</td>
</tr>
<tr>
    <td>Ethanol (<code>c_ethanol_n</code>)</td>
    <td>&nbsp;</td>
    <td>ethyl glucuronide (<code>c_etoh_n</code>)</td>
</tr>
</tbody>
</table> 
</div>

<div id="scoring" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-calculator"></i></span>
  <span class="text-with-link">
  <span class="text">Scoring Procedures</span>
  <a class="anchor-link" href="#scoring" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><b>Final results for each substance follows these rules</b>:</p>
<ul>
<li>If the confirmatory test for any substance analyte (e.g. Amphetamine (<code>c_amp_n</code>)) is positive based on predefined thresholds (<strong><a href="#nails-table1">Table 1</a></strong>), the class-level (<code>c_any_stim_n</code>) and sample-level (<code>c_any_specimen_n</code>) are also positive (value =1).</li>
<li>Otherwise, if the substance analyte confirmatory tests are negative, then class-level are negative (value =0). If all classes are negative (value = 0), then sample-level (<code>c_any_specimen_n</code>) are negative (value = 0).</li>
<li>Finally, if any substance analyte confirmatory tests are invalid (value = 3) then that class-level, and sample-level values are also invalid (value = 3)</li>
</ul>
<p><b>Table 3. Screening Result Scoring</b></p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px">
    <thead>
      <tr>
        <th style="width: 10%; text-align: center;">Level</th>
        <th style="width: 50%; text-align: center;">Result Type</th>
        <th style="width: 10%; text-align: center;">Example</th>
        <th style="width: 20%; text-align: center;">Options</th>
       </tr>
    </thead>
    <tbody>
<tr>
<td>Specimen</td>
<td style="word-wrap: break-word; white-space: normal;">Confirmatory results (presence of any analyte)</td>
<td><code>c_any_specimen_n</code></td>
<td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=invalid</td>
</tr>
<tr>
<td>Class</td>
<td style="word-wrap: break-word; white-space: normal;">Confirmatory results (presence of any analyte in class)</td>
<td><code>c_any_stim_n</code></td>
<td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=invalid</td>
</tr>
<tr>
<td colspan="1" rowspan="3">
<div>Analyte</div>
</td>
<td>Screening results</td>
<td><code>s_amp_n</code></td>
<td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=invalid</td>
</tr>
<tr>
<td>Confirmatory results</td>
<td><code>c_amp_n</code></td>
<td>concentration value; -999</td>
</tr>
<tr>
<td>Confirmatory results - categorical</td>
<td><span class="tooltip"><code>c_amp_n_cat</code><span class="tooltiptext" style="font-size: 0.9em;">Categorical confirmatory test variable for alcohol follows a different convention and is ‘c_ethanol_n’</span></span></td>
<td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=invalid; <code>4</code>=screen negative</td>
</tr>
</tbody>
</table>
</div>

## References

<div class="references">
    <p>Bandoli, G., Anunziata, F., Bogdan, R., Zilverstand, A., Chaiyachati, B. H., Gurka, K. K., Sullivan, E., Croff, J., & Bakhireva, L. N. (2024). Assessment of substance exposures in nail clipping samples: A systematic review. <i>Drug and Alcohol Dependence</i>, 254, 111038. <a href="https://doi.org/10.1016/j.drugalcdep.2023.111038" target="_blank">https://doi.org/10.1016/j.drugalcdep.2023.111038</a></p>
    <p>Sullivan, E. L., Bogdan, R., Bakhireva, L., Levitt, P., Jones, J., Sheldon, M., Croff, J. M., Thomason, M., Lo, J. O., MacIntyre, L., Shrivastava, S., Cioffredi, L.-A., Edlow, A. G., Howell, B. R., Chaiyachati, B. H., Lashley-Simms, N., Molloy, K., Lam, C., Stoermann, A. M., … HBCD Biospecimens Workgroup. (2024). Biospecimens in the HEALthy Brain and Child Development (HBCD) study: Rationale and protocol. Developmental Cognitive Neuroscience, 70(101451), 101451. <a href="https://doi.org/10.1016/j.dcn.2024.101451">https://doi.org/10.1016/j.dcn.2024.101451</a></p>
</div>