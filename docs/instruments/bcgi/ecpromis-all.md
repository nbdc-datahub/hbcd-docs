<p style="font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION TO BE ADDED FOR R2.0 (addition of 1-5 year version)</i> 🚧 </p>

# ecPROMIS
The **ecPROMIS** (Early Childhood Patient-Reported Outcome Measurement Information System) is a set of primary caregiver report questionnaires that offer clinicians and researchers a brief, efficient, and precise way to evaluate young children’s well-being. HBCD includes three ecPROMIS instruments: the Child-Caregiver Relationship Scale, Peer Relationships Scale, and Self Regulation - Flexibility Scale.

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th>Instrument</th>
  <th>Version</th>
  <th>Construct</th>
  <th>Table Name</th>
  <th>Visits</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="2" style="word-wrap: break-word; white-space: normal;">Child-Caregiver Relationship Scale</td>
  <td><strong>&lt;1 year</strong></td>
  <td>Relationships</td>
  <td><code>mh_cg_pms__cc__inf</code></td>
  <td>V03, V05</td>
</tr>
<tr>
  <td><strong>1-5 years</strong></td>
  <td>Relationships</td>
  <td><code>mh_cg_pms__cc__1to5</code></td>
  <td>V05, V07, V09</td>
</tr>
<tr>
  <td>Peer Relationships Scale</td>
  <td></td>
  <td>Peer Relationships</td>
  <td><code>mh_cg_pms__peer</code></td>
<td>V05, V07, V09</td>
</tr>
<tr>
  <td>Self Regulation - Flexibility Scale</td>
  <td></td>
  <td>Self-Regulation and Flexibility</td>
  <td><code>mh_cg_pms__selfreg</code></td>
  <td>V05, V07, V09</td>
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
<p>The ecPROMIS assesses normative variations in child behavior and should be interpreted within the context of the child's age and developmental stage. This is not clinical or diagnostic instrument.</p> 
<p>The HBCD dataset includes many variables that may be important for sound and comprehensive analysis. The inclusion of additional variables will depend on the research question(s) and methodological approach. Users are encouraged to take time to explore the full range of available variables — especially those that may serve as controls, contextual indicators, confounders, mechanisms, or modifiers — to ensure thoughtful and well-supported analytic decisions. Other important considerations may include developmental functioning, broader family supports, and early adverse and protective exposures.</p>
</div>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>Yes</td></tr>
<tr><td><b>Respondent</b></td>
<td>Primary Caregiver on Child</td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">Self-administered remotely</td></tr>
<tr><td><b>Completion Time</b></td>
<td>1-2 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;">
  <ul>
    <li>Examination of missingness (by counting the number of items answered for each participant).</li>
    <li>Check age to ensure that it falls within expected ranges (i.e. 3-9 months for V01 and 1-5 years for V05-V07).</li>
    <li>Summary statistics and visualizations generated to review item-level frequencies, age, and scores (calculated with application of prorated scoring to account for missing data).</li>
  </ul>
</td></tr>
</tbody>
</table>

## Instrument Details

### ecPROMIS - Child-Caregiver Relationship Scale
The **Child–Caregiver Relationship Scale** evaluates the degree to which young children develop close, satisfying relationships with caregivers. It was originally developed to assess children aged 1 to 5 years old. Language adjustments were made for developmental appropriateness for infants and approved by the Health Measures (ecPROMIS) team.

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
<p><b>General Language Modifications</b><br>
Measure instructions and individual items that reference gendered pronouns (‘his/hers’, ‘he/she’) were edited to either eliminate the pronouns entirely or replace with ‘my child’ when eliminating pronouns was not grammatically possible. In contrast to other measures, following consultation with measure creators, the term “parent” was not replaced with “parent/caregiver.”</p>
<p>The wording changes are minimal, should have no effect on data, and were approved by the measure creators. Because ecPROMIS measures are copyrighted, however, it is important that publications account for and note edits made to individual items.</p>
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
<p>Each of the 5 items for ecPROMIS Child-Caregiver Interaction is answered on a scale of 1-5: 1 (Never), 2 (Rarely), 3  (Sometimes), 4 (Often), and 5 (Always). A sum score is generated when the caregiver answers at least 3 out of the 5 items (<i>ecpromis1, ecpromis2, ecpromis3, ecpromis4, ecpromis5</i>). If caregivers answer 3 or 4 items, a prorated sum score is calculated using the formula: 
<p style="font-size: 0.9em;">
  \[
  \text{Prorated Score} = \left( \frac{\text{Sum of answered items}}{\text{Number of items answered}} \right) \times \text{5}
  \]
</p>
If fewer than 3 items are completed, the sum score is marked as missing.</p>
</div>

### ecPROMIS - Peer Relationships Scale
The **Peer Relationships Scale** assesses young children’s positive peer interactions, sociability (getting along well with others), and empathic behaviors. 

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
  <p><b>Addition of New Item</b><br>
  The item <code>[peer_yn]</code> was added to the beginning of the survey instrument for HBCD to assess whether the child had opportunities to interact with other children during the primary period (past 7 days).</p>
  <blockquote>
    <strong>Item text</strong>: <i>“My child had opportunities to interact with other children."</i><br>
    <strong>Response options</strong>: 0 [No]; 1 [Yes]; Decline to Answer
  </blockquote>
  The addition of <code>[peer_yn]</code> does not affect scoring (as the item isn't scored), but can be used as a filter variable for analyses. This item was added with the approval of the measure creators. However, because ecPROMIS measures are copyrighted, it is important that any publications using this variable note that <code>[peer_yn]</code> was not part of the original measure.</p>
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
<p>Each of the 4 items are responded to using the following scale: 1, Never | 2, Almost Never | 3, Sometimes | 4, Often | 5, Almost Always | Decline to Answer, <code>peer_yn</code> is answered on a yes/no 0:1 scale. If all four items are answered, their sum is calculated. If at least three items are answered but some are missing, a prorated sum is computed: 
<p style="font-size: 0.9em;">
  \[
  \text{Prorated Score} = \left( \frac{\text{Sum of answered items}}{\text{Number of items answered}} \right) \times \text{4}
  \]
</p>
If fewer than two items are answered, the sum score is set to missing.</p>
</div>

### ecPROMIS - Self Regulation - Flexibility Scale
The **Self Regulation - Flexibility Scale** assesses young children’s ability to adapt in response to environmental demands, changes, and expectations. 

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
<p>The item queue was rearranged per the HBCD DEI Committee’s recommendation to: 2, 3, 4, 5, 1. The item order change is minimal, should have no effect on data, and was approved by the measure creators. While ecPROMIS measures are copyrighted, the content of each item is maintained.</p>
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
<p>Caregivers respond to five items on a 1–5 scale (1 = Never, 5 = Always; “Decline to Answer” is allowed, but “Don’t Know” is not recommended). If all items are answered, the sum of the numerical responses is used. If at least three items are answered but some are missing, a prorated sum is calculated:
<p style="font-size: 0.9em;">
  \[
  \text{Prorated Score} = \left( \frac{\text{Sum of answered items}}{\text{Number of items answered}} \right) \times \text{5}
  \]
</p>
If fewer than three items are answered, the sum score is set to missing.</p>
</div>



## References
<div class="references"> 
<p>Blackwell, C. K., Kallen, M. A., Lai, J. S., Bevans, K. B., Wakschlag, L. S., & Cella, D. (2022). Measuring PROMIS® Well-Being in Early Childhood. <i>Journal of Pediatric Psychology</i>, 47(5), 559–572. <a href="https://doi.org/10.1093/jpepsy/jsac030" target="_blank">https://doi.org/10.1093/jpepsy/jsac030</a></p>  
<p>Blackwell, C. K., Lai, J.-S., Kallen, M., Bevans, K. B., Davis, M. M., Wakschlag, L. S., & Cella, D. (2022). Measuring PROMIS® Social Relationships in early childhood. <i>Journal of Pediatric Psychology</i>, 47(5), 573–584. <a href="https://doi.org/10.1093/jpepsy/jsac031" target="_blank">https://doi.org/10.1093/jpepsy/jsac031</a></p>  
<p>Cella, D., Blackwell, C. K., & Wakschlag, L. S. (2022). Bringing PROMIS to Early Childhood: Introduction and quaptative methods for the development of Early Childhood Parent Report instruments. <i>Journal of Pediatric Psychology</i>, 47(5), 500–509. <a href="https://doi.org/10.1093/jpepsy/jsac027" target="_blank">https://doi.org/10.1093/jpepsy/jsac027</a></p>  
<p>Lai, J.-S., Kallen, M. A., Blackwell, C. K., Wakschlag, L. S., & Cella, D. (2022). Psychometric considerations in developing PROMIS® measures for early childhood. <i>Journal of Pediatric Psychology</i>, 47(5), 510–522. <a href="https://doi.org/10.1093/jpepsy/jsac025" target="_blank">https://doi.org/10.1093/jpepsy/jsac025</a></p>  
<p>Park, C. H., Blaisdell, C. J., & Gillman, M. W. (2022). The NIH ECHO program: An impetus for the development of early childhood PROMIS tools. <i>Journal of Pediatric Psychology</i>, 47(5), 497–499. <a href="https://doi.org/10.1093/jpepsy/jsac010" target="_blank">https://doi.org/10.1093/jpepsy/jsac010</a></p>
</div>