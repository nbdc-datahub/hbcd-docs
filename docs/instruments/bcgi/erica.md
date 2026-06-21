<!-- ADMIN NOTE: ALERT - MANUALLY STYLED PAGE, including QC details and scoring -->


# ERICA

{{ readme(instruments.erica) }}

<div id="qc" class="banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-shield"></i></span><span class="text-with-link">
<span class="text">QC Procedures: Administration & Centralized Coding</span>
<a class="anchor-link" href="#qc" title="Copy link"><i class="fa-solid fa-link"></i></a></span><span class="arrow">▸</span></div>
<div class="collapsible-content">
<div class="info-section">
<div class="info-section-title">
    ERICA Site-Level Administration
</div>
<ul>
<li>HBCD study staff were trained and certified to administer the ERICA by experienced ERICA administrators to ensure adherence to standardized procedures.</li>
<li>Ongoing quality of administration was ensured through video review of at least 10 percent of administrations at each site, with higher levels of review conducted for sites that did not meet fidelity benchmarks. Video selection was not random, but sites were not told in advance which videos would be reviewed.</li>
<li>Completion rates were monitored, and site-level data on administration was reviewed for potential QC issues (e.g., frequent protocol interruptions or tech issues), with results informing site-level training and follow-up.</li>
<li>Additional training was provided as needed.</li>
</ul>
</div>

<div class="info-section">
<div class="info-section-title">
  Centralized Coding of ERICA Videos
</div>

<p>Videos are coded based on a single-pass review, with data entered directly into the HBCD database. Basic steps to ensure data completeness and accuracy include:</p>
<ul>
  <li>Double data entry with conflict resolution to ensure accurate data entry</li>
  <li>Regular review of dashboards and reports to identify missing data and unexpected score distributions</li>
  <li>Completion reports cross-referenced with video files</li>
</ul>
<p><b>ERICA Coding Training and Reliability Monitoring</b><br> 
Coders were trained and certified by coding experts under the supervision of ERICA
developers. Certification required ≥80% agreement with expert ratings (exact agreement within
±0.5 decimal points per code). To ensure ongoing coder reliability, 20% of each coder's videos
were randomly selected for double coding by experts (reliability coders) on a weekly basis.
Coders who fell below 80% agreement for two consecutive weeks on any code were pulled
from coding and re-trained/certified before continuing.</p>
<br>
<p><b>Coding Reliability Statistics</b><br>
Inter-rater reliability was quantified using a two-way mixed-effects intraclass correlation coefficient (ICC) (see table below). All codes were evaluated using ICC except for Caregiver Irritable Behavior. Due to its low base rate, this code was dichotomized and reliability was estimated using an unweighted kappa statistic. Updated reliability estimates may be provided in future data releases as additional data become available.</p>
<table class="table-no-vertical-lines">
<thead>
<tr>
<th colspan="3"><b>ERICA Inter-rater Reliability for HBCD Data Release 2.1 (n=177)</b></th>
</tr>
<tr>
<th>Codes</th>
<th>ICC</th>
<th>Kappa</th>
</tr>
</thead>
<tbody>
<tr style="background-color: #e8f5fb;">
<td>Child Positive Affect </td>
<td>0.88 (0.83,0.91)</td>
<td>NA</td>
</tr>
<tr style="background-color: #e8f5fb;">
<td>Child Irritability </td>
<td>0.96 (0.94,0.97)</td>
<td>NA</td>
</tr>
<tr style="background-color: #e8f5fb;">
<td>Child Social Engagement </td>
<td>0.76 (0.68,0.82)</td>
<td>NA</td>
</tr>
<tr style="background-color: #bfe6f5;">
<td>Caregiver Responsive Behavior </td>
<td>0.90 (0.87,0.93)</td>
<td>NA</td>
</tr>
<tr style="background-color: #bfe6f5;">
<td>Caregiver Irritable Behavior (Dichotomized)</td>
<td>0.61 (0.48,0.71)</td>
<td>0.44 (0.19,0.69)</td>
</tr>
<tr style="background-color: #bfe6f5;">
<td>Caregiver Directive Behavior </td>
<td>0.87 (0.82,0.9)</td>
<td>NA</td>
</tr>
<tr style="background-color: #8ad4f1;">
<td>Dyadic Connectedness </td>
<td>0.76 (0.68,0.82)</td>
<td>NA</td>
</tr>
<tr>
<td colspan="3">
<i>ICC is a two-way, mixed effects, multiple rater intraclass correlation (ICC (3,k)) per Shrout and Fleiss (1979) conventions. ICC is best for continuous variables. Kappas are unweighted Cohen’s Kappa and are calculated for binary/categorical scores.</i>
</td>
</tr>
</tbody>
</table>
</div>
</div>

{{ alert_warning(instruments.erica) }}
{{ data_warning(instruments.erica) }}
{{ issues_banner_macro() }}

---

## Instrument Details

The Early Regulation in Context Assessment (**ERICA**) is a standardized observational paradigm that is adapted from the well-validated Disruptive Behavior Diagnostic Observation Schedule (DB-DOS) ([Krogh-Jespersen et al. 2022](https://doi.org/10.3389/fpsyg.2021.732312)). The ERICA assesses early child regulation in the context of the caregiver-child relationship via a series of five brief, developmentally appropriate activities that “press” for regulation within the dyad (e.g., frustration, engagement, enjoyment).

The ERICA is coded using a one-pass, global coding system adapted for HBCD. Seven codes are organized across child, caregiver, and dyadic domains:

 - **Child**: Positive affect; Irritability; Social engagement
 - **Caregiver**: Responsive behavior; Irritable behavior; Directive behavior
 - **Dyadic**: Caregiver–child connectedness

Codes are scored on a 4-point scale (0-3), reflecting the frequency, intensity, and duration of observed behaviors across the paradigm, with higher scores indicating higher levels of observed behavior. See [Edwards et al. (2024)](https://doi.org/10.1016/j.dcn.2024.101422) for additional details on the ERICA paradigm and adaptation for HBCD.


{{ scoring(instruments.erica) }}


{{ scoring_banner_macro() }}
<div class="collapsible-content">
<p>Coders rate each construct at the activity level on a 4-point scale (None = 0, Low = 1, Medium = 2, High = 3). Activity-level ratings are then averaged across all activities to generate a continuous global score, ranging from 0-3, with higher scores reflecting higher levels of observed behavior.</p>
<p>Modifiers (-1, +1, and +2) may be used with three codes (<i>child irritability, caregiver responsive behavior, and dyadic connectedness</i>) to capture important qualitative distinctions. For example, for child irritability, a <b>+1</b> is added at the activity level when a child is highly irritable throughout an entire activity, with no recovery or re-engagement and a <b>+2</b> is added if a child becomes intensely dysregulated during an activity (e.g., intense crying with breath holding, gagging, other indications of intense dysregulation). When used, modifiers are included in the sum for the global scores. For caregiver responsive behavior, a <b>-1</b> is added at the activity level when a caregiver does not responds at all to intense dysregulation in a child, is delayed in responding to child distress and this results in the child becoming intensely dysregulated, or is repeatedly doing things that are dysregulating to the child, resulting in the child becoming more and more distressed. For dyadic connectedness, a <b>-1</b> is added at the activity level, when a child is distressed through much of the activity without any ability to be soothed by the caregiver and distress is not resolved by the end of the activity or during the immediate re-engagement period when transitioning to the next activity. </p>
<p>Modifiers are intended to weight the global score toward the higher or lower end of the 0-3 scale. When used, they are included in the sum for the global scores, however the scale is capped at 0-3, meaning the highest score possible is a 3.0, the lowest score possible is a 0. In cases where the use of modifiers results in global raw scores &gt;3.0, the value is converted to a 3 prior to analysis; similarly, if modifiers result in a global raw score &lt;0, the value is converted to a 0 prior to analysis.</p>
<p>Videos are coded and global scores generated as long as 3 out of the 5 ERICA activities are completed. If less than 3 activities are completed, the video is not coded and scores are not generated.</p>
<p>Please see the following table for a quick cross reference of codes and field names.</p>
<table class="table-no-vertical-lines">
  <thead>
    <tr>
      <th>Code</th>
      <th>Field Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Child Positive Affect (score)</td>
      <td><code>mh_cg_erica_3_9m_a_raw</code></td>
    </tr>
    <tr>
      <td>Child Irritability (score)</td>
      <td><code>mh_cg_erica_3_9m_b_raw</code></td>
    </tr>
    <tr>
      <td>Child Social Engagement (score)</td>
      <td><code>mh_cg_erica_3_9m_c_raw</code></td>
    </tr>
    <tr>
      <td>Caregiver Responsive Behavior (score)</td>
      <td><code>mh_cg_erica_3_9m_d_raw</code></td>
    </tr>
    <tr>
      <td>Caregiver Irritable Behavior (score)</td>
      <td><code>mh_cg_erica_3_9m_e_raw</code></td>
    </tr>
    <tr>
      <td>Caregiver Directive Behavior (score)</td>
      <td><code>mh_cg_erica_3_9m_f_raw</code></td>
    </tr>
    <tr>
      <td>Dyadic Connectedness (score)</td>
      <td><code>mh_cg_erica_3_9m_g_raw</code></td>
    </tr>
  </tbody>
</table>
</div>

## References
<div class="references"> 
<p>Krogh-Jespersen, S., MacNeill, L. A., Anderson, E. L., Stroup, H. E., Harriott, E. M., Gut, E., Blum, A., Fareedi, E., Fredian, K. M., Wert, S. L., Wakschlag, L. S., & Norton, E. S. (2021). Disruption leads to methodological and analytic innovation in developmental sciences: Recommendations for remote administration and dealing with messy data. <i>Frontiers in Psychology</i>, 12, 732312. <a href="https://doi.org/10.3389/fpsyg.2021.732312">https://doi.org/10.3389/fpsyg.2021.732312</a></p>
<p>Edwards, R. C., Planalp, E. M., Bosquet Enlow, M., Akshoomoff, N., Bodison, S. C., Brennan, M. B., Ciciolla, L., Eiden, R. D., Fillipi, C. A., Gustafsson, H. C., McKelvey, L. M., Morris, A. S., Peralta-Carcelén, M., Poehlmann, J., Wakschlag, L. S., Wilson, S., & HBCD Child Behavior and Caregiver-Child Interactions Workgroup. (2024). Capturing the complexity of child behavior and caregiver-child interactions in the HEALthy Brain and Child Development (HBCD) Study using a rigorous and equitable approach. <i>Developmental Cognitive Neuroscience</i>, 69(101422), 101422.<a href="https://doi.org/10.1016/j.dcn.2024.101422">https://doi.org/10.1016/j.dcn.2024.101422</a></p>
</div>





<!-- <p style="font-size: 1.4em; font-weight: 500; color: gray;"><i>Early Regulation in Context Assessment</i></p>

<table class="table-no-vertical-lines readme-intro">
<tbody>
<tr><td><b>Table Name</b></td><td>Primary coding data file: <code>mh_cg_erica_3_9m</code><br>
                                Reliability codes: <code>mh_cg_erica_rel_3_9m</code></td></tr>
<tr><td><b>Construct</b></td><td>Emotional Regulation, Parenting, Caregiver-Child Relationship</td></tr>
<tr><td><b>Study Visits</b></td><td>V03 (3-9 months)</td></tr>
<tr><td><b>Administration</b></td><td>
<b>Child-specific</b>: Yes<br>
<b>Respondent</b>: Birth Parent or Primary Caregiver and Child<br>
<b>Method</b>: HBCD Study staff in-person (20-30 min estimated duration)</td></tr>
<td width="10%"><b>Quality Control</b></td>
<td>QC procedures were conducted for ERICA site-level administration and centralized coding of ERICA videos - <a href="#qc">expand infobox below for details →</a></li>
</td></tr>
</tbody>
</table> -->

<!-- {{ alert_banner_macro() }}
<div class="collapsible-content">
<p>The HBCD dataset includes many variables that may be important for sound and comprehensive analysis. The inclusion of additional variables will depend on the research question(s) and methodological approach. Users are encouraged to take time to explore the full range of available variables—especially those that may serve as controls, contextual indicators, confounders, mechanisms, or modifiers—to ensure thoughtful and well-supported analytic decisions. Other important considerations may include developmental functioning, broader family supports, and early adverse and protective exposures.</p>
<p>The ERICA assesses variations in child behavior, parenting, and the caregiver-child relationship and should be interpreted within the context of the child's age and developmental stage. This is not a clinical or diagnostic instrument.</p>
</div> -->

<!-- {{ warning_banner_macro() }}
<div class="collapsible-content">
<p><b>Integrated Analytic Dataset (REQUIRED)</b></p>
<p>Prior to analysis, you must create a final integrated analytic dataset by merging the reliability codes (<code>mh_cg_erica_rel_3_9m</code>) into the primary coding data (<code>mh_cg_erica_3_9m</code>). <b>Failure to integrate these data prior to analysis will result in incorrect results.</b> In future releases, this will not be necessary, as the integrated, analytic data set will be created prior to release.</p>
<p>Download the instructions and relevant participant lists <i>(in <a href="https://hbcd-docs-private.lassoinformatics.com">HBCD Private Release Notes</a> - DUC access required)</i> as follows:</p>
<ul>
<li><a href="../ERICA_2.1_Integrated_Analytic_Data_INSTRUCTIONS.pdf" target="_blank">Integration Instructions (PDF)</a></li>
<li><a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/ERICA_2.1_DataError_EXCLUSIONS.csv"><code>ERICA_2.1_DataError_EXCLUSIONS.csv</code></a></li>
<li><a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/ERICA_2.1_Analytic_REMOVALS.csv"><code>ERICA_2.1_Analytic_REMOVALS.csv</code></a></li></ul>
<hr>
<p><b>General</b></p>
<p>Data Release 2.1 includes data from ERICA administrations completed as part of HBCD study visit 3 (3–9 Month) as of July 1, 2025, utilizing the ERICA infant paradigm, which includes a prelocomotor (3–7 month) and locomotor protocol (7–9 month).</p>
<p>Coded data for a subset of participants may be missing from this data release for various reasons. These data will be added in future releases.</p>
<p>The ERICA was administered in Spanish and English. The language of administration (i.e., language in which RAs delivered the instructions) does not always correspond with the language spoken by the caregiver/child during the activities. All videos in which the dyad speaks Spanish during the activities were coded by fully Spanish-English bilingual coders.</p>
<p>The code for "caregiver irritable behavior" in Data Release 2.1 has a low base rate because few caregivers exhibited elevated irritability. We recommend dichotomizing (0 = 0 and >0 = 1) for analysis.</p>
</div> -->
