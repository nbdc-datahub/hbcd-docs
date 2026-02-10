
# Pending Updates

## Release 2.1 (Release Date TBA)

### 2.1 Participant Data
##### Multiple Birth Participants
Family/maternal-level data is only present for the Main Child across instruments. In the future, HBCD Main Child data will be copied to the sibling profile (e.g. HBCD Multiple Birth - Sibling) for non-child-specific elements so that users won't have to populate these fields themselves. *See [Blank Fields in Sibling Data (Multiple Birth Cohorts)](../instruments/demo/visitinfo.md#warning) for details.*      
In addition, a new Data Dictionary element (***familyID***) will be incorporated to help identify siblings (Release # TBD).

### 2.1 Existing Study Data Updates
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead>
<th>Domain</th>
<th>Table/Data</th>
<th>Pending Update</th>
</thead>
<tbody>
<tr>
  <td style="text-align: center;"><span class="tooltip tooltip-right"><i class="fas fa-id-card" style="font-size:1.1em; margin-right: 2px;"></i><span class="tooltiptext">Demographics</span></span></td>
  <td>Visit Level Data<br>(<code>par_visit_data</code>)</td>
  <td style="word-wrap: break-word; white-space: normal;">Addition of <code>visit_missed_date</code> variable (date of missed visits)</td>
</tr>
<tr>
  <td style="text-align: center;"><span class="tooltip tooltip-right"><i class="fa fa-heart-pulse" style="font-size:1.1em; margin-right: 2px;"></i><span class="tooltiptext">Physical Health</span></span></td>
  <td>Growth<br>(<code>ph_ch_anthro</code>)</td>
  <td style="word-wrap: break-word; white-space: normal;">Addition of age-based z-scores & sex-specific birth weight for gestational age (<a href="../../instruments/physhealth/growth/#warning">details</a>)</td>
</tr>
<tr>
  <td style="text-align: center;"><span class="tooltip tooltip-right"><i class="fa fa-brain" style="font-size:1.1em; margin-right: 2px;"></i><span class="tooltiptext">Magnetic Resonance Imaging & Spectroscopy</span></span></td>
  <td>DICOMs</td>
  <td style="word-wrap: break-word; white-space: normal;">
  Addition of source DICOMs for <a href="../../datacuration/file-based-data/#raw-bids" target="_blank">raw BIDS</a> for all imaging modalities</td>
</tr>
</tbody>
</table>

## Release 3.0 (Release Date TBA)

### 3.0 Existing Study Data Updates
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead>
<th>Domain</th>
<th>Table/Data</th>
<th>Pending Update</th>
</thead>
<tbody>
<tr>
  <td style="text-align: center;"><span class="tooltip tooltip-right"><i class="fas fa-vial" style="font-size:1.1em; margin-right: 2px;"></i><span class="tooltiptext">Biospecimens</span></span></td>
  <td>Urine</td>
  <td style="word-wrap: break-word; white-space: normal;">Addition of creatinine results (<code>bio_bm_biosample_urine_results_bio_creat_u</code>)</td>
</tr>
<tr>
  <td rowspan="3" style="text-align: center;"><span class="tooltip tooltip-right"><i class="fa fa-heart-pulse" style="font-size:1.1em; margin-right: 2px;"></i><span class="tooltiptext">Physical Health</span></span></td>
  <td>BISQ-SF<br><code>ph_cg_bisq</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Addition of Infant Sleep (IS) sub-scale score.</td>
</tr>
<tr>
  <td>ecPROMIS- Physical Activity<br><code>ph_cg_pms__pags</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Addition of summary scores (Summed Score, T-score, and SE). Until added, users can calculate summary scores themselves by following the <a href="../../instruments/physhealth/ecpromis-pags/#scoring" target="_blank">Scoring Procedures</a> documented on the instrument page.</td>
</tr>
<tr>
  <td>ecPROMIS- Sleep<br><code>ph_cg_pms__sleep</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Addition of summary scores</td>
</tr>
</tbody>
</table>