# Behavior Questionnaire + Inhibition

<table class="table-no-vertical-lines">
<tbody>
<tr>
  <td></td>
  <td><b>IBQ-R VSF +BI</b><br>Infant Behavior Questionnaire–Revised <span class="tooltip tooltip-left">VSF +BI<span class="tooltiptext">Very Short Form + Behavior Inhibition</span></span></td>
  <td><b>ECBR VSF +BI</b><br>Early Childhood Behavior Questionnaire <span class="tooltip tooltip-left">VSF +BI<span class="tooltiptext">Very Short Form + Behavior Inhibition</span></span></td>
</tr>
<tr><td><b>Table Names</b></td><td><code>mh_cg_ibqr</code></td><td><code>mh_cg_ecbq</code></td></tr>
<tr><td><b>Study Visit(s)</b></td><td>V03, V05</td><td>V05</td></tr>
<tr><td><b>Construct</b></td><td  colspan="2">Behavioral Inhibition • Negative Affectivity • Effortful Control • Surgency/Extraversion</td></tr>
<td><b>Administration</b></td><td colspan="2">
  <ul>
  <li><b>Child-specific</b>: Yes</li>
  <li><b>Respondent</b>: Primary caregiver on Child</li>
  <li><b>Method</b>: Self-administered remotely (7-10 min)</li>
  </ul>
</tr>
<tr><td><b>Quality Control</b></td>
<td colspan="2">
  <ul>
  <li>Examine missingness by counting items answered per participant.</li>
  <li>Check age is within expected ranges.</li>
  <li>Review summary statistics and visualizations (item frequencies, age, prorated scores).</li>
  <li>Cronbach's Alpha calculated to assess reliability.</li>
  </ul>
</td>
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

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">Please review the <a href="https://docs.hbcdstudy.org/latest/changelog/issues-updates/" target="_blank">Known Issues & Pending Updates</a> page for updates that may affect data use.</span>
</div>

## Instrument Details
The *Infant Behavior Questionnaire–Revised Very Short Form + Behavior Inhibition* **(IBQ-R VSF+BI)** and *Early Childhood Behavior Questionnaire Very Short Form + Behavior Inhibition* **(ECBQ VSF+BI)** are caregiver-report measures of temperamental reactivity and self-regulation in early development. Both instruments extend the validated Very Short Forms (VSF) of the IBQ-R and ECBQ by incorporating additional items from the long-form questionnaires (items 38–47) to capture Behavioral Inhibition (Social Fear).

The HBCD versions therefore include four scale domains: **Behavioral Inhibition**, **Negative Affectivity**, **Effortful Control**, and **Surgency/Extraversion**. Scale domain items for the IBQ and ECBQ are listed in the table below, with reverse scoring (“R”) and duplicate items for BEH and NEG scale noted:

##### IBQ-R & ECBQ DOMAIN ITEMS
<div style="display: flex; gap: 24px; flex-wrap: wrap;">
<div style="flex: 1; min-width: 350px;">
<table class="compact-table-no-vertical-lines" style="font-size: 14px; line-height: 1.4; width: 100%;">
<tbody>
<tr><td colspan="4" style="border-top: 2px solid #cce7e7; padding-top: 8px;">
<b>IBQ-R Items</b><span style="color:#666; font-weight: normal;"> (prefix: <code>mh_cg_ibqr_</code>)</span></td>
</tr>
<tr>
<td><b>BEH</b><br><span style="color:#888; font-size:0.9em;">(13 items)</span></td>
<td><b>NEG</b><br><span style="color:#888; font-size:0.9em;">(12 items)</span></td>
<td><b>EFRT</b><br><span style="color:#888; font-size:0.9em;">(12 items)</span></td>
<td><b>SURG</b><br><span style="color:#888; font-size:0.9em;">(13 items)</span></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
  <!-- <td><code>beh__neg_001</code></td><td><code>beh__neg_001</code></td> -->
  <td colspan="2" style="text-align: center; color:#666;"><code>beh__neg_001</code></td>
  <td><code>efrt_001</code></td>
  <td><code>surg_001</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td colspan="2" style="text-align: center; color:#666;"><code>beh__neg_002</code></td>
    <td><code>efrt_002</code></td>
    <td><code>surg_002</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td colspan="2" style="text-align: center; color:#666;"><code>beh__neg_003</code></td>
    <td><code>efrt_003</code> <span style="color: #4e7dff;"><b>(R)</b></span></td>
    <td><code>surg_003</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_001</code></td><td><code>neg_001</code></td><td><code>efrt_004</code></td><td><code>surg_004</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_002</code></td><td><code>neg_002</code></td><td><code>efrt_005</code></td><td><code>surg_005</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_003</code></td><td><code>neg_003</code></td><td><code>efrt_006</code></td><td><code>surg_006</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_004</code></td><td><code>neg_004</code></td><td><code>efrt_007</code></td><td><code>surg_007</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_005</code></td><td><code>neg_005</code></td><td><code>efrt_008</code></td><td><code>surg_008</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_006</code></td><td><code>neg_006</code></td><td><code>efrt_009</code></td><td><code>surg_009</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_007</code></td><td><code>neg_007</code></td><td><code>efrt_010</code></td><td><code>surg_010</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_008</code></td><td><code>neg_008</code></td><td><code>efrt_011</code></td><td><code>surg_011</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_009</code> <span style="color: #4e7dff;"><b>(R)</b></span></td>
    <td><code>neg_009</code></td>
    <td><code>efrt_012</code></td>
    <td><code>surg_012</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_010</code></td><td></td><td></td><td><code>surg_013</code></td>
</tr>
</tbody>
</table>
</div>
<div style="flex: 1; min-width: 350px;">
<table class="compact-table-no-vertical-lines" style="font-size: 14px; line-height: 1.4; width: 100%;">
<tbody>
<tr>
<td colspan="4" style="border-top: 2px solid #cce7e7; padding-top: 8px;"><b>ECBQ Items</b>
<span style="color:#666; font-weight: normal;">(prefix: <code>mh_cg_ecbq_</code>)</span>
</td>
</tr>
<tr>
<td><b>BEH</b><br><span style="color:#888; font-size:0.9em;">(12 items)</span></td>
<td><b>NEG</b><br><span style="color:#888; font-size:0.9em;">(12 items)</span></td>
<td><b>EFRT</b><br><span style="color:#888; font-size:0.9em;">(12 items)</span></td>
<td><b>SURG</b><br><span style="color:#888; font-size:0.9em;">(12 items)</span></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
<td colspan="2" style="text-align: center; color:#666;"><code>beh__neg_001</code></td>
<td><code>efrt_001</code></td>
<td><code>surg_001</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
<td><code>beh_001</code> <span style="color: #4e7dff;"><b>(R)</b></span></td>
<td><code>neg_001</code></td>
<td><code>efrt_002</code></td>
<td><code>surg_003</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_002</code></td><td><code>neg_002</code></td><td><code>efrt_003</code></td><td><code>surg_004</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_003</code></td>
    <td><code>neg_003</code></td>
    <td><code>efrt_004</code> <span style="color: #4e7dff;"><b>(R)</b></span></td>
    <td><code>surg_004</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_004</code></td>
    <td><code>neg_004</code></td>
    <td><code>efrt_005</code> <span style="color: #4e7dff;"><b>(R)</b></span></td>
    <td><code>surg_005</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_005</code></td><td><code>neg_005</code></td><td><code>efrt_006</code></td><td><code>surg_006</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_006</code></td><td><code>neg_006</code></td><td><code>efrt_007</code></td><td><code>surg_007</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
    <td><code>beh_007</code></td><td><code>neg_007</code></td><td><code>efrt_008</code></td><td><code>surg_008</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
<td><code>beh_008</code> <span style="color: #4e7dff;"><b>(R)</b></span></td>
<td><code>neg_008</code></td>
<td><code>efrt_009</code></td>
<td><code>surg_009</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
<td><code>beh_009</code></td><td><code>neg_009</code></td><td><code>efrt_010</code></td><td><code>surg_010</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
<td><code>beh_010</code></td><td><code>neg_010</code></td><td><code>efrt_011</code></td><td><code>surg_011</code></td>
</tr>
<tr style="border-top: 1px solid #f5f5f5;">
<td><code>beh_011</code> <span style="color: #4e7dff;"><b>(R)</b></span></td>
<td><code>neg_011</code> <span style="color: #4e7dff;"><b>(R)</b></span></td>
<td><code>efrt_012</code></td>
<td><code>surg_012</code></td>
</tr>
</tbody>
</table>
</div>
</div>

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
<p>The IBQ-R and ECBQ item responses are reported on a 7-point Likert scale (from <i>1 = Never</i> to <i>7 = Always</i>). For each domain (Behavioral Inhibition, Negative Affectivity, Effortful Control, and Surgency/Extraversion), summary scores are computed as the mean of all items with values of 1-7. This excludes non-response options, "Does not apply" and "Decline to answer," which are not scored and considered missing.</p>
<p>Prior to computing summary scores, reverse scoring (i.e. values reassigned from 1→7 to 7→1) is applied to items labeled with <b>(R)</b> in the <a href="#ibq-r-ecbq-domain-items">Domain Items</a> table above. In the release data, the raw item-level data is not reverse-scored already. However, the domain scores do incorporate the reverse scoring. Summary scores are not computed if more than 40% of the items are missing responses (e.g. there are only 7/12 items with numerical responses of 1-7) and are instead marked as missing.</p>
<p>For additional information, see the HBCD data dictionary for details on items and scales and <a href="https://research.bowdoin.edu/rothbart-temperament-questionnaires">Mary Rothbart's Temperament Questionnaires</a> for background on measure development.</p>
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


<!-- 
<table class="compact-table-no-vertical-lines" style="width:100%; border-collapse:collapse; font-size:0.9em;">
  <thead><tr>
    <th style="text-align:center;">1</th><th style="text-align:center;">2</th>
    <th style="text-align:center;">3</th><th style="text-align:center;">4</th>
    <th style="text-align:center;">5</th><th style="text-align:center;">6</th>
    <th style="text-align:center;">7</th>
  </tr></thead>
  <tbody><tr>
    <td>Never</td><td>Very rarely</td><td>Less than half the time</td>
    <td>About half the time</td><td>More than half the time</td>
    <td>Almost always</td><td>Always</td>
  </tr></tbody>
</table> -->