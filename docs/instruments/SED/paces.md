# Protective and Compensatory Experience (*PACEs*)


<table class="table-no-vertical-lines">
<tbody>
<tr>
  <td></td>
  <td>Current PACEs (<b>C-PACES</b>)</td>
  <td>Retrospective PACEs &lt;18 (<b>R-PACES</b>)</td>
</tr>
<tr><td><b>Table Names</b></td><td><code>sed_bm_paces</code></td><td><code>sed_cg_paces</code></td></tr>
<tr><td><b>Study Visits</b></td><td>V01</td><td>V05</td></tr>
<tr><td><b>Construct</b></td><td  colspan="2">Protective Factors</td></tr>
<td><b>Administration</b></td><td colspan="2">
  <ul>
  <li><b>Child-specific</b>: No</li>
  <li><b>Respondent</b>: Parent on Self</li>
  <li><b>Method</b>: Self-administered, in-person or remote</li>
  </ul>
</tr>
<tr><td><b>Quality Control</b></td>
<td colspan="2">Data dashboard was monitored for variable missingness, possible coding errors, scoring verification, and data consistency.</td>
</tr>
</tbody>
</table>

{{ issues_banner() }}

## Instrument Details

Protective and Compensatory Experience (PACEs) is a 10-question scale with scores ranging between 0 and 10 assessing protective experiences, including relationships, feelings of connectedness, physical activity, engagement, environment, and opportunities. The versions assess protective experiences at two periods of time:

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

{{ mods_banner() }}
<div class="collapsible-content">
<p>“Decline to answer” was added as a response option for all items. Instruction item language was also modified as follows:</p>
<ul>
<li>Original text: <i>On a scale of 1 to 5, fill the circle of the number that best describes how often each of the items occurred.</i>
<li>Revised text: <i>Please select the response that best describes you.</i>
</ul>
</div>

{{ scoring_banner() }}
<div class="collapsible-content">
<p><b>Current PACEs (C-PACEs)</b><br>
Item responses can range from 1 (Never) to 5 (Very Often). The summary score is calculated as the average of responses to the 10 items (<code>sed_bm_paces_001</code> through <code>sed_bm_paces_010</code>), yielding scores from 1 to 5, with higher scores indicating more protective experiences.<br>
The summary score is calculated only if at least 7 items are completed, in which case the score is the average of the completed items. If fewer than 7 items are completed (i.e. 4 or more items have responses of ‘Decline to answer’ or ‘I don’t know’), the summary score is set to missing.</p>
<hr>
<p><b>Retrospective PACEs ( R-PACEs) &lt;18</b><br>
Item responses are coded as 0 (No) and 1 (Yes). Total scores are calculated as the sum of responses to instrument items 1 through 10 (<code>sed_cg_paces_001</code> through <code>sed_cg_paces_010</code>). Therefore, total scores can range from 0 to 10 (higher scores indicating more protective experiences) if all items are answered. If items are skipped or missed, the score is calculated as the sum of all available responses.</p>
</div>

## References
<div class="references">
  <p>Morris, A. S., Hays-Grudo, J., Zapata, M. I., Treat, A., &amp; Kerr, K. L. (2021). Adverse and protective childhood experiences and parenting attitudes: The role of cumulative protection in understanding resilience. <em>Adversity and Resilience Science</em>, 2(3), 181–192. <a href="https://doi.org/10.1007/s42844-021-00036-8">https://doi.org/10.1007/s42844-021-00036-8</a></p>
  <p>Morris, A. S., Treat, A., Hays-Grudo, J., Chesher, T., Williamson, A. C., &amp; Mendez, J. (2018). Integrating research and theory on early relationships to guide intervention and prevention. In <em>Building Early Social and Emotional Relationships with Infants and Toddlers</em> (pp. 1–25). Springer International Publishing. <a href="https://doi.org/10.1007/978-3-030-03110-7_1">https://doi.org/10.1007/978-3-030-03110-7_1</a></p>
</div>