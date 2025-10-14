<style>

</style>


<table class="compact-table-no-vertical-lines">
<thead>
  <tr>
    <th>Table/Data</th>
    <th>Resolved Known Issue</th>
  </tr>
</thead>
<tbody>

<!-- Demo -->
<tr>
  <td rowspan="5">
    <div class="icon-text-block">
      <a href="../../instruments/#demo" target="_blank">
        <i class="fas fa-id-card"></i>
      </a>
      <div class="text-block">
        Basic Demographics<br>
        <code>sed_basic_demographics</code>
      </div>
    </div>
  </td>
  <td>Added income fields (<code>income</code>) originally missing for subset of subjects.</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Removed Mother Race (<code>screen_mother_race</code>) variable option #3, a duplicate of option #5 for 'Black African American.'</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Removed Gestational/Mother’s Age at Delivery (<code>&lt;gestational|mother&gt;_age_delivery</code>) that occurred after the R1.0 cutoff date of 2025-07-01 (and therefore did not undergo QC).</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Removed invalid levels 0 & 1 from Mother Ethnicity (<code>screen_mother_ethnicity</code>). Valid levels remaining: 2 (Hispanic) and 3 (Non-Hispanic).</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Added response option ("None of these fully describe me/Other") for Mother Race & Ethnicity (<code>rc_mother_ethnoracial_aou_race_ethnicity</code>).</td>
</tr>

<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#demo" target="_blank">
        <i class="fas fa-id-card"></i>
      </a>
      <div class="text-block">
        Visit Information<br>
        <code>par_visit_data</code>
      </div>
    </div>
  </td>
  <td style="word-wrap: break-word; white-space: normal;">Added Substance Use flags (<i><a href="../../instruments/demo/visitinfo/#substance-use-flags">see details</a></i>) for alcohol, opioid, cannabis, and nicotine.</td>
</tr>

<!-- Biospec -->
<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#biospec" target="_blank">
        <i class="fas fa-vial"></i>
      </a>
      <div class="text-block">
        All (Nails & Urine)<br>
        <code>bio_bm_biosample_*</code>
      </div>
    </div>
  </td>
  <td style="word-wrap: break-word; white-space: normal;">Added collection and analysis dates (<i>Collection/Received/Report</i>) to all tables.</td>
</tr>

<tr>
  <td rowspan="3">
    <div class="icon-text-block">
      <a href="../../instruments/#biospec" target="_blank">
        <i class="fas fa-vial"></i>
      </a>
      <div class="text-block">
        Urine<br>
        <code>bio_bm_biosample_urine</code>
      </div>
    </div>
  </td>
  <td style="word-wrap: break-word; white-space: normal;">Corrected 'Urine Specific Gravity' field (<code>bio_spg_u</code>) to floating point values for the appropriate thousandths format (previously set to '1' and data type to 'integer').</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Set all negative values for Urinary Toxicology (Cotinine) results (<code>bio_c_cot_u</code>) to ‘0’ (negative values are not biologically plausible).</td>
</tr>
<tr>
  <td>Corrected negative gestational ages for 2 participants in the Urine dataset.</td>
</tr>

<!-- Neurocog -->
<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#neurocog" target="_blank">
        <i class="fa-solid fa-puzzle-piece"></i>
      </a>
      <div class="text-block">
        SPM-2<br>
        <code>ncl_cg_spm2__inf</code>
      </div>
    </div>
  </td>
  <td>Added verified t-scores (originally excluded due to errors in conversion from raw scores).</td>
</tr>

<!-- PEX -->
<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#pex" target="_blank">
        <i class="fa-solid fa-baby"></i>
      </a>
      <div class="text-block">
        Health V2 - Infancy<br>
        <code>pex_bm_healthv2_inf</code>
      </div>
    </div>
  </td>
  <td>Removed erroneously included descriptive fields <code>001__00</code> - <code>005__00</code>.</td>
</tr>

<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#pex" target="_blank">
        <i class="fa-solid fa-baby"></i>
      </a>
      <div class="text-block">
        APA 1/2<br>
        <code>pex_bm_apa</code>
      </div>
    </div>
  </td>
  <td>Added summary scores and corresponding T-scores, where appropriate, for Level 2 domains.</td>
</tr>

<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#pex" target="_blank">
        <i class="fa-solid fa-baby"></i>
      </a>
      <div class="text-block">
        EPDS<br>
        <code>pex_bm_epds</code>
      </div>
    </div>
  </td>
  <td style="word-wrap: break-word; white-space: normal;">Removed duplicate data for each item (e.g., <code>epds_001</code> and <code>epds_001_01</code>).</td>
</tr>

<tr>
  <td rowspan="2">
    <div class="icon-text-block">
      <a href="../../instruments/#pex" target="_blank">
        <i class="fa-solid fa-baby"></i>
      </a>
      <div class="text-block">
        TLFB<br>
        <code>pex_ch_tlfb</code>
      </div>
    </div>
  </td>
  <td style="word-wrap: break-word; white-space: normal;">Corrected logic for TLFB substance use flags. Previously, only the alcohol use flag applied the intended criteria (use during or after pregnancy across V01–V02).</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Removed age variable fields (<i>gestational_age</i>, <i>adjusted_age</i>, and <i>candidate_age</i>) due to incorrect values.</td>
</tr>

<!-- EEG -->
<tr>
  <td>
    <div class="icon-text-block">
      <a href="../../instruments/#eeg" target="_blank">
        <i class="fa fa-bolt"></i>
      </a>
      <div class="text-block">
        HBCD-MADE Derivatives
      </div>
    </div>
  </td>
  <td style="word-wrap: break-word; white-space: normal;">Removed erroneous resting-state summary files (<code>*_task-RS_powerSummaryStats.csv</code>) due to a pipeline bug. Users can generate these summary statistics with <a href="https://hbcd-eeg-utilities.readthedocs.io/en/stable/">HBCD EEG Utilities</a>.</td>
</tr>

</tbody>
</table>

