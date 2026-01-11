# Behavior Questionnaire + Inhibition
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Instrument</th>
  <th>Version</th>
  <th>Construct</th>
  <th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td>IBQ-R (VSF)+BI</td>
  <td>Infant (<i>I</i>)</td>
  <td rowspan="2" style="word-wrap: break-word; white-space: normal;">Temperamental Surgency/Extraversion, Negative Affectivity, Effortful Control, and Behavioral Inhibition</td>
  <td><code>mh_cg_ibqr</code></td>
</tr>
<tr>
  <td>ECBQ (VSF)+BI</td>
  <td>Early Childhood (<i>EC</i>)</td>
  <td><code>mh_cg_ecbq</code></td>
</tr>
</tbody>
</table>

<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Responsible Use Warning</span>
  <a class="anchor-link" href="#alert" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p>The HBCD dataset includes many variables that may be important for sound and comprehensive analysis. The inclusion of additional variables will depend on the research question(s) and methodological approach. Users are encouraged to take time to explore the full range of available variables — especially those that may serve as controls, contextual indicators, confounders, mechanisms, or modifiers — to ensure thoughtful and well-supported analytic decisions. Other important considerations may include developmental functioning, broader family supports, and early adverse and protective exposures.</p>
</div>

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
<p><b>Interpreting IBQ-R and ECBQ Data</b><br>
The IBQ-R (VSF)+BI and ECBQ (VSF)+BI measure normative variations in infant and child behavior and should be interpreted in the context of the child’s age and developmental stage. These instruments are not clinical or diagnostic tools.</p>
<p><b>IBQ-R vs ECBQ Administration at V05</b><br>
At V05 (10–17 months), participants could be administered either the IBQ-R (validated for ages 3–12 months) or the ECBQ (validated for ages 18–36 months), depending on their age at the visit. Because no validated measure exists for 12–18 months, researchers are advised to select the instrument that best aligns with their study design. The HBCD protocol spans this age gap, so the decision was made to administer the IBQ-R to all infants at V03 and V05.<br>
However, early in data collection, the ECBQ was inadvertently administered to infants older than 12 months (N=78). In a small number of cases (N=10), caregivers had not completed all of their V05 remote surveys before the child aged into the ECBQ range, resulting in both measures being administered at V05. Although IBQ-R and ECBQ assess similar constructs, they are not interchangeable. Users should review measure-specific properties before incorporating these data into analyses.</p>
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
<td>
  <strong>IBQ-R (VSF)+BI</strong>: V03, V05 / <strong>ECBQ (VSF)+BI</strong>: V05</td></tr>
<tr><td><b>Completion Time</b></td>
<td>7-10 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;">QC procedures involved examination of missingness (by counting the number of items answered for each participant) and age to ensure that it falls within the expected range of 3-18 months. Summary statistics and visualizations were generated to review item-level frequencies, age, and scores (calculated with application of prorated scoring to account for missing data). Finally, Cronbach's Alpha was calculated to assess reliability.</td></tr>
</tbody>
</table>

## Instrument Details

The Infant Behavior Questionnaire–Revised Very Short Form + Behavior Inhibition (**IBQ-R (VSF)+BI**) and Early Childhood Behavior Questionnaire Very Short Form + Behavior Inhibition (**ECBQ (VSF)+BI**) are caregiver-report questionnaires used to evaluate temperamental reactivity and self-regulation during the early years of development. These instruments are adapted from the validated Very Short Forms (VSF) of the IBQ-R and ECBQ, with additional items (items 38-47) drawn from the long forms to capture **Behavioral Inhibition (Social Fear)**.

**The HBCD versions therefore include four scale domains:**

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; font-size: 16px; line-height: 1.4; text-align: center;">
  <thead>
    <tr>
      <th style="text-align: left;">Scale Domain</th>
      <th>IBQ-R (# items)</th>
      <th>ECBQ (# items)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left;"><strong>Surgency / Extraversion</strong></td>
      <td>13</td>
      <td>12</td>
    </tr>
    <tr>
      <td style="text-align: left;"><strong>Negative Affectivity</strong></td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <td style="text-align: left;"><strong>Effortful Control</strong></td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <td style="text-align: left;"><strong>Behavioral Inhibition (Social Fear)</strong></td>
      <td>13 <span style="font-size: 0.9em; color: #666;">(3 overlap with Negative Affectivity)</span></td>
      <td>12 <span style="font-size: 0.9em; color: #666;">(1 overlaps with Negative Affectivity)</span></td>
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
<div class="collapsible-content">
<p>Alterations were made to replace “parent” with “parent/caregiver” where appropriate. In addition, the pronouns "she/he" or "her/him" in reference to the child/baby were changed to “the baby/child” or “they/them” as fit the item wording.</p>
<p>The creators of this measure have requested that these alterations be noted in all documentation and publications.</p>
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
<p><b>Response Scale</b><br>
Caregivers are asked to report on the infant’s behaviors on a 7-point Likert scale:<br> 
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; font-size: 0.9em;">
<thead>
<tr>
<th style="text-align: center;">1</th>
<th style="text-align: center;">2</th>
<th style="text-align: center;">3</th>
<th style="text-align: center;">4</th>
<th style="text-align: center;">5</th>
<th style="text-align: center;">6</th>
<th style="text-align: center;">7</th>
</tr>
</thead>
<tbody>
<tr>
<td>Never</td>
<td>Very rarely</td>
<td>Less than half the time</td>
<td>About half the time</td>
<td>More than half the time</td>
<td>Almost always</td>
<td>Always</td>
</tr>
</tbody>
</table>
<p>NOTE: Options also include "Does not apply" and "Choose not to respond," which are not scored and should be treated as NAs. <b>Note that "Does not apply" is coded as as "0" and "8" in the ECBQ and IBQ-R, respectively.</b> For consistency between instruments, the coding will be changed to 8 for IBQ-R in a future release.
<hr>
<p><b>Scoring Procedure</b><br>
Scale scores for the IBQ-R VSF+BI and ECBQ(VSF)+BI represent the mean score of all scale items applicable to the child, as judged by the caregiver. Scale scores are computed for each domain (Negative Affectivity, Surgency/Extraversion, Effortful Control, and Behavioral Inhibition) as follows:</p>
<p><b>1. Sum all numerical item responses for a given scale. Note that:</b></p>
<ul>
  <li>If caregiver omitted an item, <strong>that item receives no numerical score and should be treated as missing</strong>.</li>
  <li>If caregiver checked the <strong>“Does not apply” or "Choose not to respond"</strong> response option for an item, that item receives no numerical score and should be treated as 'NA'.</li>
  <li>All item-level data is raw data. However, items marked with an “R” should be <strong>reverse-scored</strong> when calculating scale scores. This reverse-scoring is already included in the HBCD scoring algorithm.</li>
</ul>
<p><b>2. Divide the total by the number of items receiving a numerical response.</b></p>
<ul>
  <li><strong>Do not include items marked “Does not apply (N/A)” or “Choose not to respond” in determining the total number of scale items.</strong></li>
  <li><strong><i>Of the items included in computing the total number of scale items,</i> if &gt;40% are missing (e.g., there are only 7/12 completed responses in a scale), it is not possible to score the individual domain.</strong></li>
</ul>
<p>For example, given a sum of 47 for a scale of 12 items, with one item receiving no response, two items marked "Does not apply", and 9 items receiving a numerical response, the sum of 47 would be divided by 9 to yield a mean of 5.22 for the scale score.</p>
<p><strong>For additional information</strong>, see the HBCD data dictionary for details on items and scales and <a href="https://research.bowdoin.edu/rothbart-temperament-questionnaires">Mary Rothbart's Temperament Questionnaires</a> for background on measure development.</p>
</div>

## References
<div class="references">
<p>Edwards, R. C., Planalp, E. M., Bosquet-Enlow, M., Akshoomoff, N., Bodison, S. C., Brennan, M. B., Ciciolla, L., Eiden, R. D., Fillipi, C. A., Gustafsson, H. C., McKelvey, L. M., Morris, A. S., Peralta-Carcelén, M., Poehlmann, J., Wakschlag, L. S., Wilson, S., & HBCD Child Behavior and Caregiver-Child Interaction Workgroup. (2024). Capturing the complexity of child behavior and caregiver-child relationships in the HEALthy Brain and Child Development (HBCD) Study using a rigorous and equitable approach. <em>Developmental Cognitive Neuroscience</em>, 69, 101422. <a href="https://doi.org/10.1016/j.dcn.2024.101422">https://doi.org/10.1016/j.dcn.2024.101422</a></p>
    <p>Gartstein, M. A., & Rothbart, M. K. (2003). Studying infant temperament via the Revised Infant Behavior Questionnaire. <i>Infant Behavior & Development</i>, 26(1), 64–86. <a href="https://doi.org/10.1016/s0163-6383(02)00169-8" target="_blank">https://doi.org/10.1016/s0163-6383(02)00169-8</a></p>  
    <p>Putnam, S. P., Gartstein, M. A., & Rothbart, M. K. (2006). Measurement of fine-grained aspects of toddler temperament: the early childhood behavior questionnaire. <i>Infant Behavior & Development</i>, 29(3), 386–401. <a href="https://doi.org/10.1016/j.infbeh.2006.01.004" target="_blank">https://doi.org/10.1016/j.infbeh.2006.01.004</a></p> 
    <p>Putnam, S. P., Helbig, A. L., Gartstein, M. A., Rothbart, M. K., & Leerkes, E. (2014). Development and assessment of short and very short forms of the infant behavior questionnaire-revised. <i>Journal of Personapty Assessment</i>, 96(4), 445–458. <a href="https://doi.org/10.1080/00223891.2013.841171" target="_blank">https://doi.org/10.1080/00223891.2013.841171</a></p> 
    <p>Putnam, S. P., Jacobs, J., Gartstein, M., & Rothbart, M. K. (2010). <i>Development assessment short very short forms Early Childhood Behavior Questionnaire<i>. In Poster presented International Conference Infant Studies (<a href="http://research.bowdoin.edu/rothbart-temperament-questionnaires/files/2016/09/ICIS_2010_ECBQ_sf_poster.pdf">LINK</a>).</p> 
    <p>Rothbart, M. K. (1981). Measurement of temperament in infancy. <i>Child Development</i>, 52(2), 569–578. <a href="https://doi.org/10.1111/j.1467-8624.1981.tb03082.x" target="_blank">https://doi.org/10.1111/j.1467-8624.1981.tb03082.x</a></p>  
</div>
