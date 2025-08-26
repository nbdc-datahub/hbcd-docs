<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION TO BE ADDED FOR R2.0 (addition of ECBQ)</i> 🚧 </p>

# Behavior Questionnaire + Inhibition

<div class="table-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">This instrument has several versions. Below you’ll find details for each version included in release data.</span>
</div>
<p></p>

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
<td><strong>Instrument</strong></td>
<td><strong>Version</strong></td>
<td><strong>Construct</strong></td>
<td><strong>Table Name</strong></td>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="2" style="word-wrap: break-word; white-space: normal;">Behavior Questionnaire Very Short Form + Behavior Inhibition</td>
  <td><span class="tooltip tooltip-right"><strong>IBQ-R</strong><span class="tooltiptext">Infant Behavior Questionnaire – Revised</span></span> <strong>(VSF)+BI</strong></td>
  <td style="word-wrap: break-word; white-space: normal;">Temperamental Surgency/Extraversion, Negative Affectivity, Effortful Control, Behavioral Inhibition</td>
  <td><code>mh_cg_ibqr</code></td>
</tr>
<tr>
  <td><span class="tooltip tooltip-right"><strong>ECBQ</strong><span class="tooltiptext">Early Childhood Behavior Questionnaire</span></span> <strong>(VSF)+BI</strong></td>
  <td style="word-wrap: break-word; white-space: normal;">Temperamental Surgency, Negative Affect, Effortful Control & Behavior Inhibition</td>
  <td><code>mh_cg_ecbq</code></td>
</tr>
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
<p>The IBQ-R (VSF)+BI assesses normative variations in child behavior and should be interpreted within the context of the child's age and developmental stage. This is not clinical or diagnostic instrument.</p> 
</div>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>Yes</td></tr>
<tr><td><b>Respondent</b></td>
<td>Primary caregiver on Child</td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">Self-administered remotely</td></tr>
<tr><td><b>Visits</b></td>
<td style="word-wrap: break-word; white-space: normal;">V03 <strong>[IBQ-R (VSF)+BI]</strong>; V05 <strong>[ECBQ]</strong> (<i>Validated for ages 3 months, 0 days to 17 months, 30 days for HBCD</i>)</td></tr>
<tr><td><b>Completion Time</b></td>
<td>7-10 min (<b>SAME FOR ECBQ?</b>)</td></tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;">QC procedures involved examination of missingness (by counting the number of items answered for each participant) and age to ensure that it falls within the expected range of 3-18 months. Summary statistics and visualizations were generated to review item-level frequencies, age, and scores (calculated with application of prorated scoring to account for missing data). Finally, Cronbach's Alpha was calculated to assess reliability.</td></tr>
</tbody>
</table>


## Instrument Details

The IBQ-R (VSF)+BI is a caregiver report form used to assess temperamental reactivity and regulation in infancy, focusing on key traits that influence development and behavior during the early years. It is adapted from the well-validated IBQ-R Very Short Form with additional items reflecting Behavioral Inhibition from the long form of the IBQ-R.

In addition to the overall Surgency, Negative Affect and Effortful Control scales derived from the validated IBQ-R-VSF, the HBCD Workgroup and measure experts added a Behavior Inhibition (or Social Fear) scale using items from the long form of the IBQ-R (IBQ-R-LF). The HBCD measure therefore consists of 4 scale domains: surgency/extraversion (13 items), negative affectivity (12 items), effortful control (12 items), and behavioral inhibition (13 items).

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
<p>Alterations were made to replace “parent” with “parent/caregiver” where appropriate. Because the psychometric validation for these measures was done using items from the original measures, future publications should account for and note edits made to individual items.</p>
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
<p>Caregivers are asked to report on the infant’s behaviors on a 7-point Likert scale: 1 [Never], 2 [Very rarely], 3 [Less than half the time], 4 [About half the time], 5 [More than half the time], 6 [Almost always], 7 [Always].</p>
<p>Scale scores, generated for each domain, are the mean score of all scale items applicable to the child as judged by the caregiver. Importantly, this calculation only includes items with scores of 1 through 7: items where the caregiver selects "does not apply" or “choose not to respond" receive no numerical score and are not included in the total number of items for the scale. Items with an “R” are reverse-scored and already implemented in the HBCD scoring algorithm.</p>
<p>For additional information, please see the data dictionary for details on items and scales as well as <a href="https://research.bowdoin.edu/rothbart-temperament-questionnaires">Mary Rothbart's Temperament Questionnaires</a>.</p>
</div>

## References
<div class="references">
    <p>Gartstein, M. A., & Rothbart, M. K. (2003). Studying infant temperament via the Revised Infant Behavior Questionnaire. <i>Infant Behavior & Development</i>, 26(1), 64–86. <a href="https://doi.org/10.1016/s0163-6383(02)00169-8" target="_blank">https://doi.org/10.1016/s0163-6383(02)00169-8</a></p>  
    <p>Putnam, S. P., Helbig, A. L., Gartstein, M. A., Rothbart, M. K., & Leerkes, E. (2014). Development and assessment of short and very short forms of the infant behavior questionnaire-revised. <i>Journal of Personapty Assessment</i>, 96(4), 445–458. <a href="https://doi.org/10.1080/00223891.2013.841171" target="_blank">https://doi.org/10.1080/00223891.2013.841171</a></p>  
    <p>Rothbart, M. K. (1981). Measurement of temperament in infancy. <i>Child Development</i>, 52(2), 569–578. <a href="https://doi.org/10.1111/j.1467-8624.1981.tb03082.x" target="_blank">https://doi.org/10.1111/j.1467-8624.1981.tb03082.x</a></p>  
</div>
<br>