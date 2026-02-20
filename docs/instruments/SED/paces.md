# Protective and Compensatory Experience (*PACEs*)

<table class="table-no-vertical-lines" style="width: 100%; font-size: 16px;">
<thead>
<tr>
  <th>Instrument</th>
  <th>Acronym</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td><b>Current PACEs</b></td>
  <td>C-PACEs</td>
  <td>Protective Factors</td>
  <td><code>sed_bm_paces</code></td>
</tr>
<tr>
  <td><b>Retrospective PACEs &lt;18</b></td>
  <td>R-PACEs</td>
  <td>Protective Factors</td>
  <td><code>sed_cg_paces</code></td>
</tr>
</tbody>
</table>

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">This data has known issues - <a href="../../../changelog/knownissues/#social-environmental-determinants" target="_blank">see details</a>.</span>
</div>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>No</td></tr>
<tr><td><b>Respondent</b></td>
<td>Parent on Self</td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">Parent, in person or remote</td></tr>
<tr><td><b>Visits</b></td>
<td>V01 <strong>[C-PACEs]</strong>; V05 <strong>[R-PACEs]</strong>;</td></tr>
<tr><td><b>Completion Time</b></td>
<td>NA</td></tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;">Data dashboard was monitored for variable missingness, possible coding errors, scoring verification when needed, and data consistency.</td></tr>
</tbody>
</table>

## Instrument Details

**Protective and Compensatory Experience (PACEs)** is a 10-question scale with scores ranging between 0 and 10 assessing protective experiences, including **relationships, feelings of connectedness, physical activity, engagement, environment, and opportunities.** The versions assess protective experiences at two periods of time:

<table class="table-no-vertical-lines" style="font-size: 16px;">
<tbody>
<tr>
  <td><strong>Current PACEs (C-PACEs)</strong></td>
  <td>Protective experiences in the last year</td>
</tr>
<tr>
  <td><strong>Retrospective PACEs ( R-PACEs) &lt;18</strong></td>
  <td>Protective experiences in childhood through age 18</td>
</tr>
</tbody>
</table>

<div id="hbcd-mod" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-gear"></i></span>
  <span class="text-with-link">
  <span class="text">HBCD Modification Details</span>
  <a class="anchor-link" href="#hbcd-mod" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>“Decline to answer” was added as a response option for all items. Instruction item language was also modified as follows:</p>
<ul>
<li>Original text: <i>On a scale of 1 to 5, fill the circle of the number that best describes how often each of the items occurred.</i>
<li>Revised text: <i>Please select the response that best describes you.</i>
</ul>
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
<div class="collapsible-content">
<p><b>Current PACEs (C-PACEs)</b><br>
Item responses can range from <b>1 (Never)</b> to <b>5 (Very Often)</b>. Summary scores are calculated as the average of responses to the 10 items in the instrument (<code>sed_bm_paces_001</code> through <code>sed_bm_paces_010</code>), resulting in possible scores from <b>1 to 5</b>, with higher scores indicating more protective experiences.<br>
If one or two items are missing (i.e. have responses of ‘Decline to answer’ or ‘Don’t know’), the summary score is calculated as the average of the completed items. If three or more items are missing (i.e., seven or fewer items are completed), the summary score is set to missing.</p>
<p><b>Retrospective PACEs ( R-PACEs) &lt;18</b><br>
Item responses are coded as <b>0 (No)</b> and <b>1 (Yes)</b>. Total scores are calculated as the sum of responses to instrument items 1 through 10 (<code>sed_cg_paces_001</code> through <code>sed_cg_paces_010</code>). Therefore, total scores can range from <b>0 to 10</b> (higher scores indicating more protective experiences) if all items are answered. If items are skipped or missed, the score is calculated as the sum of all available responses.</p>
</div>

## References
<div class="references">
  <p>Morris, A. S., Hays-Grudo, J., Zapata, M. I., Treat, A., &amp; Kerr, K. L. (2021). Adverse and protective childhood experiences and parenting attitudes: The role of cumulative protection in understanding resilience. <em>Adversity and Resilience Science</em>, 2(3), 181–192. <a href="https://doi.org/10.1007/s42844-021-00036-8">https://doi.org/10.1007/s42844-021-00036-8</a></p>
  <p>Morris, A. S., Treat, A., Hays-Grudo, J., Chesher, T., Williamson, A. C., &amp; Mendez, J. (2018). Integrating research and theory on early relationships to guide intervention and prevention. In <em>Building Early Social and Emotional Relationships with Infants and Toddlers</em> (pp. 1–25). Springer International Publishing. <a href="https://doi.org/10.1007/978-3-030-03110-7_1">https://doi.org/10.1007/978-3-030-03110-7_1</a></p>
</div>