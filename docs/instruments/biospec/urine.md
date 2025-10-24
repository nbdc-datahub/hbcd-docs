# USDTL Urine Toxicology (Maternal)

<div class="info-block">
  <div class="info-row">
    <div class="info-label"><i class="fa fa-table"></i> Table Name:</div>
    <div class="info-value"><code>bio_bm_biosample_urine</code></div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-tape"></i> Construct:</div>
    <div class="info-value">Drug Panel, Toxins</div>
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
For all toxicology screens, continuous variables should be interpreted with caution based on the threshold limits of quantification (LOQs), or the cutoff concentration used to categorize metabolites as positive or negative. LOQs are provided in <a href="#urine-table1">Table 1. Urine Assay Thresholds for Analytes</a>.</p> 
<p><b>Urinary Concentration Corrections</b><br>
Urine concentrations vary by participant. Urinary concentration corrections can be made using creatinine results from sample validation or specific gravity. Creatinine values are provided for researchers who wish to adjust/correct for urinary concentration in continuous measures or apply different thresholds.</p>
<p><b>Large Gaps Between Collection and Analysis Dates</b><br> A substantial number of samples show unusually long intervals between collection and analysis (e.g., over 100–300 days, compared to the 30-day limit specified by internal SOPs). We are working to determine whether this reflects a data entry or site-level issue and will provide an update once more information is available.</p>
</div>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Respondent</b></td>
<td>Pregnant/postpartum person</td></tr>
<tr><td><b>Administration</b></td>
<td>Self-collected</td></tr>
<tr><td><b>Visits</b></td>
<td>V01</td></tr>
<tr><td><b>Completion Time</b></td>
<td>5 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td>Examine assay ranges and categorical versus continuous measures.</td></tr>
</tbody>
</table>

## Instrument Details

<img src="../images/Fig1_biospec_urine.png" width="70%" height="auto" class="center">

These data are the results of urine toxicology assays. **Screening** results for substances are determined to be positive or negative based on predefined thresholds (**[Table 1](#urine-table1)**), or invalid - see [Validation Procedures](#validation). **Confirmatory tests** are used to confirm the results of screening for any substance analyte (e.g. **Amphetamine (`c_amp_u`)**), which are grouped into different classes by analyte screening tests and analyte confirmatory tests (**[Table 2](#urine-table2)**).

<div id="urine-table1" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-table"></i></span>
  <span class="text-with-link">
  <span class="text">Table 1. Urine Assay Thresholds for Analytes</span>
  <a class="anchor-link" href="#urine-table1" title="Copy link">
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
        <th style="width: 20%;"><span class="tooltip tooltip-bottom">LOD<span class="tooltiptext">Limit of detection</span></span> (ng/mL)</th>
        <th style="width: 10%;"><span class="tooltip tooltip-bottom">LOQ<span class="tooltiptext">Limit of quantification</span></span> (ng/mL)</th>
        <th style="width: 10%;">Cutoff (ng/mL)</th>
        <th style="width: 40%;">Detection Window</th>
      </tr>
</thead>
<tbody>
    <tr>
        <td>Amphetamine</td>
        <td>50</td>
        <td>100</td>
        <td>250</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Methamphetamine</td>
        <td>50</td>
        <td>100</td>
        <td>250</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>MDA</td>
        <td>50</td>
        <td>100</td>
        <td>250</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>MDMA</td>
        <td>50</td>
        <td>100</td>
        <td>250</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>MDEA</td>
        <td>50</td>
        <td>100</td>
        <td>250</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Carboxy-delta-9-THC</td>
        <td>3</td>
        <td>7.5</td>
        <td>15</td>
        <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">2-5 days for casual use; 10-14 for chronic use</td>
    </tr>
    <tr>
        <td>Carboxy-delta-8-THC</td>
        <td>3</td>
        <td>7.5</td>
        <td>15</td>
        <td>No consensus</td>
    </tr>
    <tr>
        <td>Carboxy-cannabidiol</td>
        <td>10</td>
        <td>25</td>
        <td>50</td>
        <td>No consensus</td>
    </tr>
        <tr>
        <td><span class="tooltip tooltip-right">Cotinine<span class="tooltiptext" style="font-size: 0.9em;"> Based on DRI® Cotinine assay for the qualitative and semiquantitative determination of Cotinine</span></span></td>
        <td>34</td>
        <td>34</td>
        <td>500</td>
        <td>Up to 7 days</td>
    </tr>
    <tr>
        <td>Benzoylecgonine</td>
        <td>20</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>6-MAM</td>
        <td>2</td>
        <td>4</td>
        <td>10</td>
        <td>8 hours</td>
    </tr>
    <tr>
        <td>Codeine</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Hydrocodone</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Hydromorphone</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Morphine</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Oxycodone</td>
        <td>60</td>
        <td>120</td>
        <td>300</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Oxymorphone</td>
        <td>60</td>
        <td>120</td>
        <td>300</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Phencyclidine</td>
        <td>5</td>
        <td>12.5</td>
        <td>25</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Methadone</td>
        <td>60</td>
        <td>120</td>
        <td>300</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>EDDP</td>
        <td>60</td>
        <td>120</td>
        <td>300</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Amobarbital</td>
        <td>40</td>
        <td>100</td>
        <td>200</td>
        <td>2-4 days</td>
    </tr>
    <tr>
        <td>Butalbital</td>
        <td>40</td>
        <td>100</td>
        <td>200</td>
        <td>2-4 days</td>
    </tr>
    <tr>
        <td>Pentobarbital</td>
        <td>40</td>
        <td>100</td>
        <td>200</td>
        <td>1-2 days</td>
    </tr>
    <tr>
        <td>Phenobarbital</td>
        <td>40</td>
        <td>100</td>
        <td>200</td>
        <td>2 weeks</td>
    </tr>
    <tr>
        <td>Secobarbital</td>
        <td>40</td>
        <td>100</td>
        <td>200</td>
        <td>1-2 days</td>
    </tr>
    <tr>
        <td>&alpha;-Hydroxyalprazolam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>&alpha; -Hydroxytirazolam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>&alpha; -Hydroxymidazolam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>2-Hydroxyethylflurazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>7-Aminoflunitrazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>7-Aminoclonazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>7-Aminonitrazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>Lorazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>Nordiazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>Oxazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>Temazepam</td>
        <td>20</td>
        <td>40</td>
        <td>100</td>
        <td>1-4 days</td>
    </tr>
    <tr>
        <td>Norpropoxyphene</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Ketamine</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Norketamine</td>
        <td>10</td>
        <td>50</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Normeperidine</td>
        <td>40</td>
        <td>100</td>
        <td>200</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Tramadol</td>
        <td>40</td>
        <td>80</td>
        <td>200</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Buprenorphine</td>
        <td>1</td>
        <td>2</td>
        <td>5</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Norbuprenorphine</td>
        <td>1</td>
        <td>2</td>
        <td>5</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Ethyl glucuronide</td>
        <td>50</td>
        <td>100</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Ethyl sulfate</td>
        <td>12.5</td>
        <td>25</td>
        <td>25</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Zolpidem</td>
        <td>4</td>
        <td>8</td>
        <td>20</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Zolpidem Carboxylic Acid</td>
        <td>4</td>
        <td>8</td>
        <td>20</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Carisoprodol</td>
        <td>10</td>
        <td>20</td>
        <td>50</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Meprobamate</td>
        <td>10</td>
        <td>20</td>
        <td>50</td>
        <td>2-3 days</td>
    </tr>
    <tr>
    <td colspan="5"></td>
</tr>  
</tbody>
<thead>
      <tr>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Analyte</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">LOD (pg/mL)</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">LOQ (pg/mL)</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Cutoff (pg/mL)</th>
        <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Detection Window</th>
      </tr>
</thead>
    <tr>
        <td>Fentanyl</td>
        <td>40</td>
        <td>40</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Norfentanyl</td>
        <td>40</td>
        <td>40</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Alfentanil</td>
        <td>40</td>
        <td>40</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Sufentanil</td>
        <td>40</td>
        <td>40</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
    <tr>
        <td>Norsufentanil</td>
        <td>40</td>
        <td>40</td>
        <td>100</td>
        <td>2-3 days</td>
    </tr>
</table>
</div>

<div id="urine-table2" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-table"></i></span>
  <span class="text-with-link">
  <span class="text">Table 2. Mapping From Class to Screening Tests and Confirmatory Tests</span>
  <a class="anchor-link" href="#urine-table2" title="Copy link">
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
        <th style="width: 20%;">Screening Test</th>
        <th style="width: 60%;">Confirmatory Test (positive screen reflex)</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td colspan="1" rowspan="6">
            <div>stimulant (<code>c_any_stim_u</code>)</div>
        </td>
        <td colspan="1" rowspan="2">
            <div>amp (<code>s_amp_u</code>)</div>
        </td>
        <td>Amphetamine (<code>c_amp_u</code>)</td>
    </tr>
    <tr>
        <td>Methamphetamine (<code>c_meth_u</code>)</td>
    </tr>
    <tr>
        <td colspan="1" rowspan="3">
            <div>mdma (<code>s_mdma_u</code>)</div>
        </td>
        <td>MDM (<code>c_mdm_u</code>)</td>
    </tr>
    <tr>
        <td>MDA (<code>c_mda_u</code>)</td>
    </tr>
    <tr>
        <td>MDEA (<code>c_mdea_u</code>)</td>
    </tr>
    <tr>
        <td>coc (<code>s_coc_u</code>)</td>
        <td>Benzoylecgonine (<code>c_ben_u</code>)</td>
    </tr>
    <tr>
        <td colspan="1" rowspan="3">
            <div>cannabinoid (<code>c_any_cannabinoid_u</code>)</div>
        </td>
        <td colspan="1" rowspan="3">
            <div>thc (<code>s_thc_u</code>)</div>
        </td>
        <td>Carboxy-delta-9-THC (<code>c_delta-9-THC_u</code>)</td>
    </tr>
    <tr>
        <td>Carboxy-Cannabidiol (<code>c_cannabidiol_u</code>)</td>
    </tr>
    <tr>
        <td>Carboxy-delta-8-THC (<code>c_delta-8-THC_u</code>)</td>
    </tr>
    <tr>
        <td colspan="1" rowspan="5">
            <div>barbiturate (<code>c_any_barb_u</code>)</div>
        </td>
        <td colspan="1" rowspan="5">
            <div>bar (<code>s_bar_u</code>)</div>
        </td>
        <td>Amobarbital (<code>c_amobarb_u</code>)</td>
    </tr>
    <tr><td>Secobarbital (<code>c_secobarb_u</code>)</td></tr>
    <tr><td>Pentobarbital (<code>c_pentobarb_u</code>)</td></tr>
    <tr><td>Phenobarbital (<code>c_phenobarb_u</code>)</td></tr>
    <tr><td>Butalbital (<code>c_butalbital_u</code>)</td></tr>
    <tr>
        <td colspan="1" rowspan="11">
            <div>benzodiazepine (<code>c_any_benzo_u</code>)</div>
        </td>
        <td colspan="1" rowspan="11">
            <div>benz (<code>s_benz_u</code>)</div>
        </td>
        <td>Oxazepam (<code>c_oxaz_u</code>)</td>
    </tr>
    <tr><td>Nordiazepam (<code>c_nord_u</code>)</td></tr>
    <tr><td>Temazepam (<code>c_tema_u</code>)</td></tr>
    <tr><td>Hydroxymidazolam (<code>c_homi_u</code>)</td></tr>
    <tr><td>Alphahydroxyalprazolam (<code>c_aha_u</code>)</td></tr>
    <tr><td>2hydroxyethylflurazepam (<code>c_2hef_u</code>)</td></tr>
    <tr><td>7Aminoclonazepam (<code>c_7ac_u</code>)</td></tr>
    <tr><td>7Aminoflunitrazepam (<code>c_7af_u</code>)</td></tr>
    <tr><td>7Aminonitrazepam (<code>c_7an_u</code>)</td></tr>
    <tr><td>Alphahydroxytriazolam (<code>c_aht_u</code>)</td></tr>
    <tr><td>Lorazepam (<code>c_lor_u</code>)</td></tr>
    <tr>
        <td colspan="1" rowspan="19">
            <div>opioids (<code>c_any_opioid_u</code>)</div>
        </td>
        <td colspan="1" rowspan="5">
            <div>opi (<code>s_opi_u</code>)</div>
        </td>
        <td>Codeine (<code>c_cod_u</code>)</td></tr>
    <tr><td>Morphine (<code>c_mor_u</code>)</td></tr>
    <tr><td>MAM (<code>c_mam_u</code>)</td></tr>
    <tr><td>Hydrocodone (<code>c_hydroc_u</code>)</td></tr>
    <tr><td>Hydromorphone (<code>c_hydrom_u</code>)</td></tr>
    <tr>
        <td colspan="1" rowspan="2"><div>mtd (<code>s_mtd_u</code>)</div></td>
        <td>Methadone (<code>c_mtd_u</code>)</td></tr>
    <tr>
    <td>EDDP (<code>c_eddp_u</code>)</td></tr>
    <tr>
        <td>ppx (<code>s_ppx_u</code>)</td>
        <td>Norpropoxyphene (<code>c_nppx_u</code>)</td>
    </tr>
    <tr>
        <td colspan="1" rowspan="2">
            <div>oxyc (<code>s_oxyc_u</code>)</div>
        </td>
        <td>Oxycodone (<code>c_oxyc_u</code>)</td>
    </tr>
    <tr>
        <td>Oxymorphone (<code>c_oxym_u</code>)</td>
    </tr>
    <tr>
        <td>mep (<code>s_mep_u</code>)</td>
        <td>Normeperidine (<code>c_nmep_u</code>)</td>
    </tr>
    <tr>
        <td>tram (<code>s_tram_u</code>)</td>
        <td>Tramadol (<code>c_tram_u</code>)</td>
    </tr>
    <tr>
        <td colspan="1" rowspan="3"><div>fent (<code>s_fent_u</code>)</div></td>
        <td>Fentanyl (<code>c_fent_u</code>)</td>
    </tr>
    <tr>
        <td>Norfentanyl (<code>c_nfent_u</code>)</td></tr>
    <tr><td>Alfentanil (<code>c_afent_u</code>)</td></tr>
    <tr>
        <td colspan="1" rowspan="2"><div>suf (<code>s_suf_u</code>)</div></td>
        <td>Norsufentanil (<code>c_nsuf_u</code>)</td>
    </tr>
    <tr><td>Sufentanil (<code>c_suf_u</code>)</td></tr>
    <tr>
        <td colspan="1" rowspan="2">
            <div>bup (<code>s_bup_u</code>)</div>
        </td>
        <td>Buprenorphine (<code>c_bup_u</code>)</td></tr>
    <tr><td>Norbuprenorpine (<code>c_nbup_u</code>)</td></tr>
    <tr>
        <td colspan="1" rowspan="2">
            <div>muscle relaxant (<code>c_any_mscrlx_u</code>)</div>
        </td>
        <td colspan="1" rowspan="2">
            <div>crs (<code>s_crs_u</code>)</div>
        </td>
        <td>Carisoprodol (<code>c_crs_u</code>)</td>
    </tr>
    <tr><td>Meprobamate (<code>c_mepb_u</code>)</td></tr>
    <tr>
        <td colspan="1" rowspan="2"><div>ethanol (<code>c_ethanol_u</code>)</div></td>
        <td colspan="1" rowspan="2">
            <div>etgeia (<code>s_etgeia_u</code>)</div>
        </td>
        <td>EthylGluc-0100 (<code>c_ethglu_u</code>)</td>
    </tr>
    <tr><td>EthylSul-100 (<code>c_ethsyl_u</code>)</td></tr>
    <tr>
        <td colspan="1" rowspan="2">
            <div>sedative (<code>c_sedative_u</code>)</div>
        </td>
        <td colspan="1" rowspan="2">
            <div>zol (<code>s_zol_u</code>)</div>
        </td>
        <td>Zolpidem (<code>c_zol_u</code>)</td>
    </tr>
    <tr>
        <td>Zolpidem CA (<code>c_zolc_u</code>)</td>
    </tr>
    <tr>
        <td colspan="1" rowspan="3"><div>dissociative anesthetic (<code>c_disanesth_u</code>)</div></td>
        <td colspan="1" rowspan="2"><div>ket (<code>s_ket_u</code>)</div></td>
        <td>Ketamine (<code>c_ket_u</code>)</td>
    </tr>
    <tr><td>Norketamine (<code>c_nket_u</code>)</td></tr>
    <tr><td>pcp (<code>s_pcp_u</code>)</td>
    <td>Phencyclidine (<code>c_pcp_u</code>)</td></tr>
    <tr><td>nicotine (<code>c_nicotine_u</code>)</td>
        <td>&nbsp;</td>
        <td>Cotinine (<code>c_cot_u</code>)</td>
    </tr>
</tbody>
</table>
</div>

<div id="validation" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-clipboard-check"></i></span>
  <span class="text-with-link">
  <span class="text">Validation Procedures</span>
  <a class="anchor-link" href="#validation" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Assay results may be scored as invalid if specimens are identified as dilute, substituted, adulterated, or otherwise insufficient based on validation. Validation is based on creatinine, pH, and nitrite measurements. <b>Only specimens with low creatinine (< 20 mg/dL) are confirmed using specific gravity via a refractometer</b> (decision grid below), and the creatinine analysis is repeated to rule out issues with the first analysis (e.g. sample mix-ups, air bubble in a line on the instrument, etc.).</p>
<img src="../images/Table1_biospec_urine.png" width="70%" height="auto" class="center">
<br>
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
<li>If the confirmatory test for any substance analyte (e.g. Amphetamine (<code>c_amp_u</code>)) is positive based on predefined thresholds (<strong><a href="#urine-table1">Table 1</a></strong>), the class-level (<code>c_any_stim_u</code>) and sample-level (<code>c_any_specimen_u</code>) are also positive (value =1).</li>
<li>Otherwise, if the  substance analyte confirmatory tests are negative (e.g., <code>c_ethglu_u</code> and <code>c_ethsyl_u</code>, values = 0) then class-level (e.g., <code>c_etgeia_u</code>) are negative (value =0). If all classes are negative (value = 0), then sample-level (e.g., <code>c_any_specimen_u</code>) are negative (value = 0).</li>
<li>Finally, if any substance analyte confirmatory tests are invalid (value = 3) then that class-level, and sample-level values are also invalid (value = 3).</li>
</ul>
<p><b>Table 3. Screening Result Scoring</b></p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
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
<td><code>c_any_specimen_u</code></td>
<td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=invalid</td>
</tr>
<tr>
<td>Class</td>
<td style="word-wrap: break-word; white-space: normal;">Confirmatory results (presence of any analyte in class)</td>
<td><code>c_any_stim_u</code></td>
<td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=invalid</td>
</tr>
<tr>
<td rowspan="3">Analyte</td>
<td>Screening results</td>
<td><code>s_amp_u</code></td>
<td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=invalid</td>
</tr>
<tr>
<td>Confirmatory results</td>
<td><code>c_amp_u</code></td>
<td>concentration value</td>
</tr>
<tr>
<td>Confirmatory results - categorical</td>
<td><code>c_amp_u_cat</code>⁠<span class="blue-text">**</span></td>
<td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=invalid; <code>4</code>=screen negative</td>
</tr>
</tbody>
</table>
⁠<span class="blue-text">**</span><small>Note: the categorical confirmatory test variable for nicotine follows the convention: <code>c_nicotine_u</code>.</small>
<br>
</div>

## References

<div class="references">
    <p>Sullivan, E. L., Bogdan, R., Bakhireva, L., Levitt, P., Jones, J., Sheldon, M., Croff, J. M., Thomason, M., Lo, J. O., MacIntyre, L., Shrivastava, S., Cioffredi, L.-A., Edlow, A. G., Howell, B. R., Chaiyachati, B. H., Lashley-Simms, N., Molloy, K., Lam, C., Stoermann, A. M., … HBCD Biospecimens Workgroup. (2024). Biospecimens in the HEALthy Brain and Child Development (HBCD) study: Rationale and protocol. Developmental Cognitive Neuroscience, 70(101451), 101451. <a href="https://doi.org/10.1016/j.dcn.2024.101451">https://doi.org/10.1016/j.dcn.2024.101451</a></p>
</div>
<br>