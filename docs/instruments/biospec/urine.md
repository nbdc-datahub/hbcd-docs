# USDTL Urine Toxicology (Maternal)

<table class="table-no-vertical-lines" style="font-size: 1em;">
<tbody>
<tr><td><b>Table Name</b></td><td><code>bio_bm_biosample_urine_results</code></td></tr>
<tr><td><b>Construct</b></td><td>Drug Panel, Toxins</td></tr>
<tr><td><b>Study Visit(s)</b></td><td>V01</td></tr>
<tr><td><b>Administration</b></td><td>
<b>Respondent</b>: Pregnant/postpartum person<br>
<b>Method</b>: Self-collected (5 min estimated duration)
</td></tr>
<td><b>Quality Control</b></td><td>Examine assay ranges and categorical versus continuous measures</td></tr>
</tbody>
</table>

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
<p><b>USDTL Screening Updates</b><br>
As of May 19, 2025, USDTL transitioned the initial urine screening test for fentanyl and sufentanil from LDTD to ELISA. As of November 2025, urine samples were no longer assayed for sufentanil, and USDTL simplified its specimen validity assessment, replacing a multi-parameter algorithm (including pH and nitrite) with a single creatinine-based measure to evaluate urine hydration.</p>
<p><b>Continuous Variables</b><br>
Continuous variables should be interpreted with caution based on limits of quantification (LOQ), i.e. the minimum concentration at which metabolites can be reliably quantified. See <a href="#urine-table1">Urine Assay Thresholds for Analytes</a>.</p>
<p><b>Urinary Concentration Corrections</b><br>
Urinary concentration varies by participant. Researchers who wish to correct for urinary concentration in continuous measures, or apply different thresholds, can do so using creatinine or specific gravity results from sample validation.</p>
<p><b>Large Gaps Between Collection and Analysis Dates</b><br> A substantial number of samples show unusually long intervals between collection and analysis (e.g., over 100–300 days, compared to the 30-day limit specified by internal SOPs). We are working to determine whether this reflects a data entry or site-level issue and will provide an update once more information is available.</p>
</div>

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">Please review the <a href="https://docs.hbcdstudy.org/latest/changelog/issues-updates/" target="_blank">Known Issues & Pending Updates</a> page for updates that may affect data use.</span>
</div>

## Instrument Details

Urine toxicology assay results include:

- **Screening results**: initial screening results for substances (e.g. **Amphetamine/`s_amp_u`**), determined to be positive/negative based on [predefined thresholds](#urine-table1), or invalid based on [Validation Procedures](#validation)
- **Confirmatory results**: confirm positive screening results for a given substance analyte, e.g. **Amphetamine**, including continuous (`c_amp_u`) and categorical (`c_amp_u_cat`) results
- **Classification**: results are grouped into different classes based on analyte screening and confirmatory tests (**[Mapping From Class to Screening & Confirmatory Tests](#urine-table2)**)

<img src="../images/Fig1_biospec_urine.png" width="70%" height="auto" class="center">

<div id="urine-table1" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-table"></i></span><span class="text-with-link">
<span class="text">Urine Assay Thresholds for Analytes</span><a class="anchor-link" href="#urine-table1" title="Copy link">
<i class="fa-solid fa-link"></i></a></span><span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Analytes</th>
<th>Unit</th>
<th><span class="tooltip tooltip-right">LOD<span class="tooltiptext">Limit of detection</span></span></th>
<th><span class="tooltip tooltip-right">LOQ<span class="tooltiptext">Limit of quantification</span></span></th>
<th><span class="tooltip tooltip-right">Cutoff<span class="tooltiptext">Threshold used to classify results as positive or negative</span></span></th>
<th>Detection Window</th>
</tr>
</thead>
<tbody>
<tr><td>2-Hydroxyethylflurazepam</td><td>ng/mL</td><td>20</td><td>40</td><td>100</td><td>1–4 days</td></tr>
<tr><td>6-MAM</td><td>ng/mL</td><td>2</td><td>4</td><td>10</td><td>8 hours</td></tr>
<tr><td>7-Aminoflunitrazepam<br>7-Aminoclonazepam<br>7-Aminonitrazepam</td><td>ng/mL</td><td>20</td><td>40</td><td>100</td><td>1–4 days</td></tr>
<tr><td>&alpha;-Hydroxyalprazolam<br>&alpha;-Hydroxymidazolam<br>&alpha;-Hydroxytirazolam</td><td>ng/mL</td><td>20</td><td>40</td><td>100</td><td>1–4 days</td></tr>
<tr><td>Amphetamine<br>Methamphetamine</td><td>ng/mL</td><td>50</td><td>100</td><td>250</td><td>2–3 days</td></tr>
<tr><td>Amobarbital<br>Butalbital</td><td>ng/mL</td><td>40</td><td>100</td><td>200</td><td>2–4 days</td></tr>
<tr><td>Benzoylecgonine</td><td>ng/mL</td><td>20</td><td>50</td><td>100</td><td>2–3 days</td></tr>
<tr><td>Buprenorphine<br>Norbuprenorphine</td><td>ng/mL</td><td>1</td><td>2</td><td>5</td><td>2–3 days</td></tr>
<tr><td>Carboxy-delta-9-THC</td><td>ng/mL</td><td>3</td><td>7.5</td><td>15</td><td>2–5 days (casual); 10–14 days (chronic)</td></tr>
<tr><td>Carboxy-delta-8-THC</td><td>ng/mL</td><td>3</td><td>7.5</td><td>15</td><td>No consensus</td></tr>
<tr><td>Carboxy-cannabidiol</td><td>ng/mL</td><td>10</td><td>25</td><td>50</td><td>No consensus</td></tr>
<tr><td>Carisoprodol</td><td>ng/mL</td><td>10</td><td>20</td><td>50</td><td>2–3 days</td></tr>
<tr><td>Codeine<br>Hydrocodone</td><td>ng/mL</td><td>10</td><td>50</td><td>100</td><td>2–3 days</td></tr>
<tr><td><span class="tooltip tooltip-right">Cotinine<span class="tooltiptext" style="font-size: 0.9em;">Based on DRI® Cotinine assay (qualitative/semiquantitative)</span></span></td><td>ng/mL</td><td>34</td><td>34</td><td>500</td><td>Up to 7 days</td></tr>
<tr><td>EDDP</td><td>ng/mL</td><td>60</td><td>120</td><td>300</td><td>2–3 days</td></tr>
<tr><td>Ethyl glucuronide</td><td>ng/mL</td><td>50</td><td>100</td><td>100</td><td>2–3 days</td></tr>
<tr><td>Ethyl sulfate</td><td>ng/mL</td><td>12.5</td><td>25</td><td>25</td><td>2–3 days</td></tr>
<tr><td>Fentanyl<br>Norfentanyl<br>Alfentanil<br>Sufentanil</td><td>pg/mL</td><td>40</td><td>40</td><td>100</td><td>2–3 days</td></tr>
<tr><td>Hydromorphone<br>Morphine</td><td>ng/mL</td><td>10</td><td>50</td><td>100</td><td>2–3 days</td></tr>
<tr><td>Ketamine<br>Norketamine</td><td>ng/mL</td><td>10</td><td>50</td><td>100</td><td>2–3 days</td></tr>
<tr><td>Lorazepam<br>Nordiazepam<br>Oxazepam<br>Temazepam</td><td>ng/mL</td><td>20</td><td>40</td><td>100</td><td>1–4 days</td></tr>
<tr><td>MDA<br>MDMA<br>MDEA</td><td>ng/mL</td><td>50</td><td>100</td><td>250</td><td>2–3 days</td></tr>
<tr><td>Meprobamate</td><td>ng/mL</td><td>10</td><td>20</td><td>50</td><td>2–3 days</td></tr>
<tr><td>Methadone</td><td>ng/mL</td><td>60</td><td>120</td><td>300</td><td>2–3 days</td></tr>
<tr><td>Normeperidine</td><td>ng/mL</td><td>40</td><td>100</td><td>200</td><td>2–3 days</td></tr>
<tr><td>Norpropoxyphene</td><td>ng/mL</td><td>10</td><td>50</td><td>100</td><td>2–3 days</td></tr>
<tr><td>Oxycodone<br>Oxymorphone</td><td>ng/mL</td><td>60</td><td>120</td><td>300</td><td>2–3 days</td></tr>
<tr><td>Pentobarbital<br>Secobarbital</td><td>ng/mL</td><td>40</td><td>100</td><td>200</td><td>1–2 days</td></tr>
<tr><td>Phenobarbital</td><td>ng/mL</td><td>40</td><td>100</td><td>200</td><td>2 weeks</td></tr>
<tr><td>Phencyclidine</td><td>ng/mL</td><td>5</td><td>12.5</td><td>25</td><td>2–3 days</td></tr>
<tr><td>Tramadol</td><td>ng/mL</td><td>40</td><td>80</td><td>200</td><td>2–3 days</td></tr>
<tr><td>Zolpidem<br>Zolpidem Carboxylic Acid</td><td>ng/mL</td><td>4</td><td>8</td><td>20</td><td>2–3 days</td></tr>
</tbody>
</table>
</div>

<div id="urine-table2" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-table"></i></span>
  <span class="text-with-link">
  <span class="text">Mapping From Class to Screening & Confirmatory Tests</span>
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
<p>Assay results may be scored as invalid if specimens are identified as dilute, substituted, adulterated, or otherwise insufficient based on validation. Validation is based on creatinine, pH, and nitrite measurements, with creatinine analysis repeated to rule out issues with the first analysis (e.g., sample mix-ups, air bubble in a line on the instrument). Specimens with low creatinine (< 20 mg/dL) are confirmed using specific gravity via a refractometer. Decision grid:</p>
<table class="compact-table">
<thead><tr><th rowspan="2">Creatinine (mg/dL)</th><th colspan="5" style="text-align: center;">Specific Gravity</th></tr>
<tr><th>1.000</th><th>1.001</th><th>1.002</th><th>1.003–1.019</th><th>≥1.020</th></tr></thead>
<tbody>
<tr><td>0–1.9</td><td>Substituted</td><td>Substituted</td><td>Invalid</td><td>Invalid</td><td>Substituted</td></tr>
<tr><td>2.0–19.9</td><td>Invalid</td><td>Invalid</td><td>Dilute</td><td>Normal</td><td>Normal</td></tr>
<tr><td>&gt;20</td><td colspan="5" class="muted-cell">Normal — Specific Gravity not required</td></tr>
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
<p><b>Final results for each substance follow these rules:</b></p>
<ul>
  <li>If any confirmatory analyte test (e.g., Amphetamine / <code>c_amp_u</code>) is positive, the corresponding class-level (<code>c_any_stim_u</code>) and sample-level (<code>c_any_specimen_u</code>) results are also positive.</li>
  <li>If all confirmatory analyte tests within a class are negative (e.g., <code>c_ethglu_u</code>, <code>c_ethsyl_u</code>), the class-level result (e.g., <code>c_etgeia_u</code>) is negative. If all classes are negative, the sample-level result (<code>c_any_specimen_u</code>) is negative.</li>
  <li>If any confirmatory analyte test is invalid, the corresponding class- and sample-level results are also invalid.</li>
</ul>
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
<tr><td>Specimen</td>
<td style="word-wrap: break-word; white-space: normal;">Confirmatory results (presence of any analyte)</td><td><code>c_any_specimen_u</code></td><td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=invalid</td></tr>
<tr><td>Class</td>
<td style="word-wrap: break-word; white-space: normal;">Confirmatory results (presence of any analyte in class)</td><td><code>c_any_stim_u</code></td><td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=invalid</td></tr>
<tr>
<td rowspan="3">Analyte</td><td>Screening results</td><td><code>s_amp_u</code></td><td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=invalid</td></tr>
<tr><td>Confirmatory results</td><td><code>c_amp_u</code></td><td>concentration value</td></tr>
<tr><td>Confirmatory results - categorical</td><td><code>c_amp_u_cat</code>⁠<sup>1</sup></td><td><code>1</code>=positive; <code>0</code>=negative; <code>3</code>=invalid; <code>4</code>=screen negative</td></tr>
</tbody>
<tfoot>
<tr>
  <td colspan="4" style="word-wrap: break-word; white-space: normal; border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
    <sup><b>1</b></sup><i>Note: the categorical confirmatory test variable for nicotine follows the convention <code>c_nicotine_u</code><ii></td></tr>
</tfoot>
</table>
</div>

## References

<div class="references">
    <p>Sullivan, E. L., Bogdan, R., Bakhireva, L., Levitt, P., Jones, J., Sheldon, M., Croff, J. M., Thomason, M., Lo, J. O., MacIntyre, L., Shrivastava, S., Cioffredi, L.-A., Edlow, A. G., Howell, B. R., Chaiyachati, B. H., Lashley-Simms, N., Molloy, K., Lam, C., Stoermann, A. M., … HBCD Biospecimens Workgroup. (2024). Biospecimens in the HEALthy Brain and Child Development (HBCD) study: Rationale and protocol. Developmental Cognitive Neuroscience, 70(101451), 101451. <a href="https://doi.org/10.1016/j.dcn.2024.101451">https://doi.org/10.1016/j.dcn.2024.101451</a></p>
</div>
