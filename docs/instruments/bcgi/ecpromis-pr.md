<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION TO BE ADDED FOR R2.0</i> 🚧 </p>

# ecPROMIS Peer Relationships Scale

<div class="info-block">
  <div class="info-row">
    <div class="info-label"><i class="fa fa-table"></i> Table Name:</div>
    <div class="info-value"><code>mh_cg_pms__peer</code></div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-tape"></i> Construct:</div>
    <div class="info-value">Peer Relationships</div>
  </div>
</div>

---------------------------------------------

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

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>Yes</td></tr>
<tr><td><b>Respondent</b></td>
<td>Primary Caregiver on Child</td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">Self-administered remotely</td></tr>
<tr><td><b>Visits</b></td>
<td>V05, V07, V09</td></tr>
<tr><td><b>Completion Time</b></td>
<td>1-2 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;">
<ul>
  <li>Examine missingness by counting the number of items answered for each participant.</li>
  <li>Check age to ensure that it falls within expected ranges (1-5 years).</li>
  <li>Generate summary statistics and visualizations to review item-level frequencies, age, and scores (calculated with application of prorated scoring to account for missing data).</li>
</ul>
</td></tr>
</tbody>
</table>

## Instrument Details
The **ecPROMIS** (Early Childhood Patient-Reported Outcome Measurement Information System) is a set of primary caregiver report questionnaires that offer clinicians and researchers a brief, efficient, and precise way to evaluate young children’s well-being. The **Peer Relationships Scale** assesses young children’s positive peer interactions, sociability (getting along well with others), and empathic behaviors. 

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
<p>The item <code>[peer_yn]</code> was added to the beginning of the survey instrument for HBCD to assess whether the child had opportunities to interact with other children during the primary period (past 7 days).</p>
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
<p>The Peer Relationship Scale includes the unscored <code>peer_yn</code> item and 4 scored items answered on a scale of 1-5:<br>
1 = <b>Never</b> &nbsp; 2 = <b>Almost Never</b> &nbsp; 3 = <b>Sometimes</b> &nbsp 4 = <b>Often</b> &nbsp; 5 = <b>Almost Always</b> &nbsp; <i>Decline to Answer = missing</i></p>
<p>If all items are answered, their sum is used as the total score. If fewer than three items are completed, the score is set to missing. If at least three items are answered but some are missing, a prorated score is calculated as:</p>
<p style="font-size: 0.9em;">
  \[
  \text{Prorated Score} = \left( \frac{\text{Sum of answered items}}{\text{Number of items answered}} \right) \times \text{4}
  \]
</p>
</div>

## References
<div class="references"> 
<p>Blackwell, C. K., Lai, J.-S., Kallen, M., Bevans, K. B., Davis, M. M., Wakschlag, L. S., & Cella, D. (2022). Measuring PROMIS® Social Relationships in early childhood. <i>Journal of Pediatric Psychology</i>, 47(5), 573–584. <a href="https://doi.org/10.1093/jpepsy/jsac031" target="_blank">https://doi.org/10.1093/jpepsy/jsac031</a></p>  
<p>Cella, D., Blackwell, C. K., & Wakschlag, L. S. (2022). Bringing PROMIS to Early Childhood: Introduction and quaptative methods for the development of Early Childhood Parent Report instruments. <i>Journal of Pediatric Psychology</i>, 47(5), 500–509. <a href="https://doi.org/10.1093/jpepsy/jsac027" target="_blank">https://doi.org/10.1093/jpepsy/jsac027</a></p>  
<p>Lai, J.-S., Kallen, M. A., Blackwell, C. K., Wakschlag, L. S., & Cella, D. (2022). Psychometric considerations in developing PROMIS® measures for early childhood. <i>Journal of Pediatric Psychology</i>, 47(5), 510–522. <a href="https://doi.org/10.1093/jpepsy/jsac025" target="_blank">https://doi.org/10.1093/jpepsy/jsac025</a></p>  
<p>Park, C. H., Blaisdell, C. J., & Gillman, M. W. (2022). The NIH ECHO program: An impetus for the development of early childhood PROMIS tools. <i>Journal of Pediatric Psychology</i>, 47(5), 497–499. <a href="https://doi.org/10.1093/jpepsy/jsac010" target="_blank">https://doi.org/10.1093/jpepsy/jsac010</a></p>
</div>


