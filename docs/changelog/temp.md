
<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
.pr-pill {
  display: inline-block;
  padding: 2px 8px;
  font-size: 1em;
  font-weight: 600;
  border-radius: 999px;
  line-height: 1;
  white-space: nowrap;
}
/* Version-specific styling */
.pr-general {
  background-color: #e6f0ff;
  color: #1a4fb3;
}
/* TBD */
.pr-tbd {
  background-color: #f1f3f5;
  color: #666;
  font-style: italic;
}
</style>

# Known Issues & Pending Updates 


### <i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Known Issues

<table class="compact-table-no-vertical-lines">

    <thead>
    <tr style="text-decoration: bold; font-size: 1.2em;">
    <th>TABLE/TOPIC</th>
    <th>SUMMARY</th>
    <th style='text-align: center;'><span class="tooltip tooltip-left">PR<span class="tooltiptext">Target Release</span></span></th>
    </tr>
    </thead>
    <tbody>


<tr class="domain-row-issue"><td colspan="3"><strong>SOCIAL &amp; ENVIRONMENTAL DETERMINANTS</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Demographics</td>
<td style='word-wrap: break-word; white-space: normal;'>Variables on the Other Biological Parent are missing from <code>sed_bm_demo</code>.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Demographics</td>
<td style='word-wrap: break-word; white-space: normal;'>The variables <code>sed_bm_demo_residence_{001|002}</code>, present in the prior release, are missing in the current release and will be added back.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
</tbody></table>



### <i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i> Pending Updates

<table class="compact-table-no-vertical-lines">

    <thead>
    <tr style="text-decoration: bold; font-size: 1.2em;">
    <th>TABLE/TOPIC</th>
    <th>SUMMARY</th>
    <th style='text-align: center;'><span class="tooltip tooltip-left">PR<span class="tooltiptext">Target Release</span></span></th>
    </tr>
    </thead>
    <tbody>
    

<tr class="domain-row-pending"><td colspan="3"><strong>GENERAL</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Language</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of language of administration across all instruments where applicable.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>

<tr class="domain-row-pending"><td colspan="3"><strong>MRI</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>BrainSwipes</td>
<td style='word-wrap: break-word; white-space: normal;'>BrainSwipes QC results will be updated with latest results  currently available in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>DICOMs</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of source DICOMs for all imaging modalities.</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Scanner Info</td>
<td style='word-wrap: break-word; white-space: normal;'>Scanner information (currently available in the scans TSV files within the raw BIDS data as well as all sidecar JSON files) will be provided as tabulated data.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Summary Forms</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of MRI &apos;Scan Session&apos; and &apos;Data&apos; Summary Forms to release data with information from the MRI technician obtained on day of scan.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Var name length</td>
<td style='word-wrap: break-word; white-space: normal;'>Variable names for tabulated MRI data (particularly XCP-D outputs) can be upwards of 167 characters, which may exceed variable name limits in some software and lead to truncation or import errors. Shorter variable names will be implemented in a future release.</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr class="domain-row-pending"><td colspan="3"><strong>NEUROCOGNITION &amp; LANGUAGE</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Bayley-4</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of item-level scores.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>CDI</td>
<td style='word-wrap: break-word; white-space: normal;'>Set percentile scores in <code>ncl_ch_cdiwgen</code> (with the exception of <code>percentile_both</code>) to data type=integer.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Vineland</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of language field to <code>ncl_cg_vabs</code>.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr class="domain-row-pending"><td colspan="3"><strong>PHYSICAL HEALTH</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>BISQ-SF</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of age-based z-scores to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Z-Scores Excluded</a>).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of sex-specific birth weight to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Sex-Specific Birthweight for GA</a>).</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Vision Screener</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>ecPROMIS- Sleep</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of summary scores to <code>ph_cg_pms__sleep</code>.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>ecPROMIS-PAG</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of summary scores to <code>ph_cg_pms__pags</code>. Until added, scores can be calculated by following the <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/ecpromis-pags/#scoring">Scoring Procedures</a> documentation.</td>
<td style='text-align: center;'><span class='pr-pill pr-tbd'>TBD</span></td>
</tr>
<tr class="domain-row-pending"><td colspan="3"><strong>PREGNANCY &amp; EXPOSURE</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>PEX Health</td>
<td style='word-wrap: break-word; white-space: normal;'>ICD codes for the <code>pex_bm_health*</code> instrument tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3</span></td>
</tr>
<tr class="domain-row-pending"><td colspan="3"><strong>SOCIAL &amp; ENVIRONMENTAL DETERMINANTS</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Child Demo</td>
<td style='word-wrap: break-word; white-space: normal;'>Household roster will be updated to clarify that counts exclude the main child - see "Household Roster" under <a href="https://docs.hbcdstudy.org/latest/instruments/SED/demo-ch/#warning">Data Warning</a> for details.</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>2.1</span></td>
</tr>
</tbody></table>

<!-- END KNOWN_ISSUES_TABLE -->



Doc file 'access/tools.md' contains a link 'download.md#explore-download-hbcd-study-data', but the doc 'access/download.md' does
           not contain an anchor '#explore-download-hbcd-study-data'.
INFO    -  Doc file 'changelog/issues-updates.md' contains a link '#known-issues', but there is no such anchor on this page.
INFO    -  Doc file 'changelog/issues-updates.md' contains a link '#pending-updates', but there is no such anchor on this page.
INFO    -  Doc file 'instruments/index.md' contains a link '../changelog/issues-updates.md#pending-updates', but the doc
           'changelog/issues-updates.md' does not contain an anchor '#pending-updates'.
INFO    -  Doc file 'instruments/overview.md' contains a link '../changelog/issues-updates.md#pending-updates', but the doc
           'changelog/issues-updates.md' does not contain an anchor '#pending-updates'.
INFO    -  Doc file 'instruments/eeg/index.md' contains a link '../processing/index.md#pipeline-standards-design', but the doc
           'instruments/processing/index.md' does not contain an anchor '#pipeline-standards-design'.
INFO    -  Doc file 'instruments/processing/standards.md' contains a link '#obtaining-a-doi', but there is no suc