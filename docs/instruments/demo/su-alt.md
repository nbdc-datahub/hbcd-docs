
## Substance Use Flags

**SU flag** variables indicate whether a participant met study-defined criteria for prenatal exposure to **Alcohol, Nicotine, Cannabis, Opioids, and/or Stimulants.** Flags include [instrument-specific](#instrument-specific-su-flags) and [derived](#derived-su-flags) variables that aggregate evidence across instruments to provide a single indicator per substance. See [Gurka et al., 2025](https://doi.org/10.1016/j.dcn.2024.101494) for full methodological details.

<p style="margin-bottom: 0.5em;"><i>For readability, <code><span style="color: teal;">SUFLAG</span></code> is used in place of <code>par_visit_data_su_flag</code> for variable names in the table below.</i></p>
<table class="table-no-vertical-lines" style="font-size: 15px;">
<thead>
<tr>
<th rowspan="2">Substance</th>
<th rowspan="2">Derived SU Flag</th>
<th colspan="3" style="text-align:center;">Instrument-Specific SU Flags</th>
</tr>
<tr>
<th style="text-align: center; font-size: 0.8em; line-height: 0.5;"><i>Urine</i></th>
<th style="text-align: center; font-size: 0.8em; line-height: 0.5;"><i>TLFB</i></th>
<th style="text-align: center; font-size: 0.8em; line-height: 0.5;"><i>Health V2</i></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Alcohol</strong></td>
<td><code><span style="color: teal;">SUFLAG</span>_alcohol</code></td>
<td><code><span style="color: teal;">SUFLAG</span>_bio_bm_ethanol</code></td>
<td><code><span style="color: teal;">SUFLAG</span>_tlfb_bm_alcohol</code></td>
<td><code><span style="color: teal;">SUFLAG</span>_healthv2_ch_fas</code></td>
</tr>
<tr>
<td><strong>Nicotine</strong></td>
<td><code><span style="color: teal;">SUFLAG</span>_nicotine</code></td>
<td><code><span style="color: teal;">SUFLAG</span>_bio_bm_nicotine</code></td>
<td><code><span style="color: teal;">SUFLAG</span>_tlfb_bm_nicotine</code></td>
<td>—</td>
</tr>
<tr>
<td><strong>Cannabis</strong></td>
<td><code><span style="color: teal;">SUFLAG</span>_cannabis</code></td>
<td><code><span style="color: teal;">SUFLAG</span>_bio_bm_cannabinoid</code></td>
<td><code><span style="color: teal;">SUFLAG</span>_tlfb_bm_cannabis</code></td>
<td>—</td>
</tr>
<tr>
<td><strong>Opioids</strong></td>
<td><code><span style="color: teal;">SUFLAG</span>_opioid</code></td>
<td><code><span style="color: teal;">SUFLAG</span>_bio_bm_opioid</code></td>
<td><code><span style="color: teal;">SUFLAG</span>_tlfb_bm_opioid</code></td>
<td><code><span style="color: teal;">SUFLAG</span>_healthv2_ch_nows</code></td>
</tr>
<tr>
<td><strong>Stimulants</strong></td>
<td><i>None</i></td>
<td><code><span style="color: teal;">SUFLAG</span>_bio_bm_stim</code></td>
<td><code><span style="color: teal;">SUFLAG</span>_tlfb_bm_stimulant</code></td>
<td>—</td>
</tr>
</tbody>
</table>

### Instrument-Specific SU Flags

Instrument-specific flags are generated from positive reports in the instruments listed below. 


<table class="table-no-vertical-lines" style="width:100%; table-layout:fixed;"> 
<thead> <tr> 
<th>Instrument</th>
<th>SU Flag Variables</th>
<th>Positive Report</th>
</tr> </thead>
<tbody>
<tr>
<td>Biospecimen - <a href="../../biospec/urine" target="_blank">Urine</a><sup><b>1</b></sup></td>
<td><code>su_flag_bio_bm_&lt;<span class="tooltip">SUBSTANCE<span class="tooltiptext">ethanol; nicotine; cannabinoid; opioid; stim</span></span>&gt;</code></td>
<td style="word-wrap: break-word; white-space: normal;">Positive USDTL urine toxicology result</td>
</tr>
<tr>
<td>Timeline Follow Back (<a href="../../pregexp/su/tlfb" target="_blank">TLFB</a>)</td>
<td><code>su_flag_tlfb_bm_&lt;<span class="tooltip">SUBSTANCE<span class="tooltiptext">alcohol; nicotine; cannabis; opioid; stimulant</span></span>&gt;</code></td>
<td style="word-wrap: break-word; white-space: normal;">Self-reported use</td>
</tr>
<tr>
<td><strong><a href="../../pregexp/pex" target="_blank">Health V2 - Infancy</a></strong></td>
<td><code>su_flag_healthv2_ch_&lt;fas|nows&gt;</code></td>
<td style="word-wrap: break-word; white-space: normal;">Diagnosis of <span class="tooltip to">NOWS<span class="tooltiptext">Neonatal Opioid Withdrawal Syndrome</span></span> or <span class="tooltip">FAS<span class="tooltiptext">Fetal Alcohol Syndrome</span></span></td>
</tr>
</tbody>
<tfoot>
<tr>
  <td colspan="3" style="word-wrap: break-word; white-space: normal; border-top: 2px solid #cce7e7; padding: 10px 8px 6px 8px;">
    <sup><b>1</b></sup> <i><a href="../../biospec/nails" target="_blank">Nails</a> Biospecimen results will additionally be integrated into creation of SU flags in a future release</i>
  </td>
</tr>
</tfoot>
</table>

### Derived SU Flags

In addition to the above, the following derived SU flags **aggregate evidence across instruments** to provide a single indicator per substance. **A derived SU flag is reported as "Yes" if one or more contributing instrument-specific flags are positive.**

<table class="table-no-vertical-lines" style="width:100%; table-layout:fixed;"> 
<thead>
<tr> 
<th style="width:20%">Substance</th>
<th style="width:25%">Derived SU Flag</th>
<th style="width:55%">Contributing Instrument Flags</th>
</tr>
</thead>
<tbody>
<tr>
<td>Alcohol</td>
<td><code>su_flag_alcohol</code></td>
<td>
<code>su_flag_bio_ethanol</code> (Urine toxicology)<br>
<code>su_flag_tlfb_alcohol</code> (TLFB self-report)<br>
<code>su_flag_healthv2_fas</code> (Health V2 – FAS diagnosis)
</td>
</tr>
<tr>
<td>Nicotine</td>
<td><code>su_flag_nicotine</code></td>
<td>
<code>su_flag_bio_nicotine</code> (Urine toxicology)<br>
<code>su_flag_tlfb_nicotine</code> (TLFB self-report)
</td>
</tr>
<tr>
<td>Cannabis</td>
<td><code>su_flag_cannabis</code></td>
<td>
<code>su_flag_bio_cannabinoid</code> (Urine toxicology)<br>
<code>su_flag_tlfb_cannabis</code> (TLFB self-report)
</td>
</tr>
<tr>
<td>Opioids</td>
<td><code>su_flag_opioid</code></td>
<td>
<code>su_flag_bio_opioid</code> (Urine toxicology)<br>
<code>su_flag_tlfb_opioid</code> (TLFB self-report)<br>
<code>su_flag_healthv2_nows</code> (Health V2 – NOWS diagnosis)
</td>
</tr>
</tbody>
</table>

<div id="su" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-sliders"></i></span>
  <span class="text-with-link">
  <span class="text">Prenatal Exposure Thresholds</span>
  <a class="anchor-link" href="#su" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>The thresholds below define the criteria used to determine whether an instrument-specific report is considered positive for prenatal exposure. <b>For each substance, only one of the listed exposure thresholds must be met for the derived SU flag to be positive</b>.</p>

<table class="compact-table-no-vertical-lines" style="width:100%; table-layout:fixed;"> 
<thead> <tr> 
<th>Substance</th>
<th>Data Source</th>
<th>Exposure Threshold
<i>(Substance use flagged as positive if ≥1 criterion is met)</i></th>
</tr> </thead>
<tbody>
<tr> 
<td rowspan="4"><strong>Alcohol</strong></td>
<td>TLFB</td> <td>Self-reported use ≥7 standard drinks per week for ≥2 weeks during pregnancy (Wk 03-09)</td></tr>
<tr><td>TLFB</td> <td>Self-reported use ≥3 standard drinks per occasion on ≥2 occasions during pregnancy (Wk 03-09)</td> </tr>
<tr><td>Health V2-Infancy</td> <td>Diagnosis of Fetal Alcohol Syndrome (FAS)</td></tr>
<tr><td>Urine</td> <td>Positive alcohol toxicology result</td>
</tr>
<tr>
<td rowspan="3"><strong>Opioids</strong></td>
<td>TLFB</td>
<td style="word-wrap: break-word; white-space: normal;">Self-reported use of prescribed (including medications for opioid use disorder) or illicit opioids for ≥2 weeks during pregnancy (Wk 03-09)</td></tr>
<tr>
<td>Health V2-Infancy</td> 
<td>Diagnosis of Neonatal Opioid Withdrawal Syndrome (NOWS)</td>
</tr>
<tr>
<td>Urine</td> <td>Positive opioid toxicology result in research-collected biospecimen</td>
</tr>
<tr>
<td rowspan="2"><strong>Cannabis</strong></td> <td>TLFB</td> <td>Self-reported cannabis use for ≥4 weeks during pregnancy (Wk 03-09)</td> </tr>
<tr> <td>Urine</td> <td>Positive cannabis toxicology result</td> </tr> 
<tr> <td rowspan="2"><strong>Nicotine</strong></td> <td>TLFB</td> <td>Self-reported nicotine or nicotine product use for ≥4 weeks during pregnancy (Wk 03-09)</td> </tr> 
<tr> <td>Urine</td> <td>Positive nicotine toxicology result</td> </tr> 
</tbody> </table>

<p>© Copyright 2025 by Elsevier. All rights reserved. Used/adapted with permission from <a href="https://doi.org/10.1016/j.dcn.2024.101494">Gurka et al., Dev Cogn Neurosci. 2025</a>.</p>
</div>
<p></p>