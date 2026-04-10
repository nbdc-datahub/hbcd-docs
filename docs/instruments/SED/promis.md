# PROMIS Perceived Stress/Social Support

<div class="info-block">
  <div class="info-row">
    <div class="info-label"><i class="fa fa-table"></i> Table Name:</div>
    <div class="info-value"><code>sed_bm_strsup</code></div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-maximize"></i> Full Name:</div>
    <div class="info-value">
       Patient-Reported Outcome Measurement Information System (<i>PROMIS</i>) Perceived Stress/Social Support
    </div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-tape"></i> Construct:</div>
    <div class="info-value">Perceived Stress/Social Support</div>
  </div>
</div>

---------------------------------------------

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">Please review the <a href="https://docs.hbcdstudy.org/latest/changelog/issues-updates/" target="_blank">Known Issues & Pending Updates</a> page for updates that may affect data use.</span>
</div>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>Yes</td></tr>
<tr><td><b>Respondent</b></td>
<td>Parent</td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">Remote survey</td></tr>
<tr><td><b>Visits</b></td>
<td>V01, V02, V03</td></tr>
<tr><td><b>Completion Time</b></td>
<td>4 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;">A data dashboard was used to routinely assess variable missingness, detect potential coding errors, verify scoring, and ensure overall data consistency.</td></tr>
</tbody>
</table>

## Instrument Details

The **Perceived Stress and Social Support (PROMIS)** tools assess caregiver perceived stress and emotional support within their social networks longitudinally. Questionnaires include:

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>PROMIS Emotional Support 4a</b><br>(first 4 questions)</td>
<td style="word-wrap: break-word; white-space: normal;">Evaluates the quality of emotional support available to the participant</td></tr>
<tr><td><b>Perceived Stress Scale-4 (PSS-4)</b><br>(last 4 questions)</td>
<td style="word-wrap: break-word; white-space: normal;">Shortened version of the PSS-14 that measures general perceived stress over the past month, used widely used across different populations (including pregnant individuals and young families)</td></tr>
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
<div class="collapsible-content">
<p>Response options for the PROMIS were modified to include the addition of “Don’t know” and “Decline to answer.”</p>
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
<p><b>PROMIS Emotional Support 4a</b><br>
Emotional support is reported on a 5-point Likert scale. Total raw scores (<code>total_raw_score</code>) are calculated as the sum of all item responses and are only computed when all items are answered<b style="font-size: 1.1em;">*</b>. Raw scores are converted to scale/T-scores (<code>scale_score</code>) with standard errors (<code>standard_error</code>) using the <a href="https://www.healthmeasures.net/images/PROMIS/manuals/Scoring_Manuals_/PROMIS_Emotional_Support_Scoring_Manual.pdf">official scoring tables</a>. Higher scores indicate greater emotional support. To include participants with missing item responses, researchers may instead use the <a href="https://www.assessmentcenter.net/ac_scoringservice">HealthMeasures Scoring Service</a> to generate T-scores.</p>
<p><b>Perceived Stress Scale–4 (PSS-4)</b><br> 
Perceived stress is reported on a 5-point Likert scale. Total scores (<code>total_score</code>) are calculated as the sum of all item responses and are only computed when all items are answered<b style="font-size: 1.1em;">*</b>. Items 2 and 3 are reverse-coded prior to scoring (i.e., <code>0</code>→<code>4</code> becomes <code>4</code>→<code>0</code>). Higher scores indicate greater perceived stress.</p>
<p><i><b style="font-size: 1.1em;">*</b> Items are considered "answered" if they have valid responses ranging from <code>0</code> to <code>4</code>, which excludes responses such as “Don’t know”</i></p>
</div>





<!-- 
PSS-4 Scoring Instructions:

 - In the last month, how often have you felt that you were unable to control the important things in your life?
 - In the last month, how often have you felt confident about your ability to handle your personal problems?
 - In the last month, how often have you felt that things were going your way?
 - In the last month, how often have you felt difficulties were piling up so high that you could not overcome them?

 - Questions 1 and 4: 0 = Never; 1 = Almost never; 2 = Sometimes; 3 = Fairly often; 4 = Very often 
 - Questions 2 and 3: 4 = Never; 3 = Almost never; 2 = Sometimes; 1 = Fairly often; 0 = Very often

These questions are NOT already reverse coded in the data dictionary.  -->

## References
<div class="references">
  <p>Cohen, S., Kamarck, T., &amp; Mermelstein, R. (1983). A global measure of perceived stress. <em>Journal of Health and Social Behavior</em>, 24(4), 385–396. <a href="https://doi.org/10.2307/2136404">https://doi.org/10.2307/2136404</a></p>
  <p>Hahn, E. A., Cella, D., Bode, R. K., &amp; Hanrahan, R. T. (2010). Measuring social well-being in people with chronic illness. <em>Social Indicators Research</em>, 96(3), 381–401. <a href="https://doi.org/10.1007/s11205-009-9484-z">https://doi.org/10.1007/s11205-009-9484-z</a></p>
</div>