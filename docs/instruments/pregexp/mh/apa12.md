# APA Level 1 / Level 2

**Full Name**: DSM-5 Self-Rated Level 1 and Level 2 Cross-Cutting Symptom Measure—Adult           
**Acronym**: APA Level 1 / Level 2         
**Table Name**: `pex_bm_apa`       
**Construct**: Mental health

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p><b>Consideration of Mental Health Symptoms Experienced During Pregnancy</b><br>

The co-occurrence of psychiatric symptoms and substance use during pregnancy is well-documented (<a href="https://doi.org/10.1111/j.1521-0391.2010.00110.x">Massey et al., 2011</a>, <a href="https://doi.org/10.1016/j.addbeh.2012.04.002">Massey et al., 2012</a>). Phenotypic risk in birthing parents may affect offspring neurodevelopment through both prenatal and postnatal mechanisms, beyond direct exposure alone (<a href="https://doi.org/10.1007/s10519-015-9762-2">Estabrook et al., 2016</a>, <a href="https://doi.org/10.1016/j.ntt.2015.11.010">Massey et al., 2016</a>, <a href="https://doi.org/10.1016/j.ntt.2018.02.003">Massey et al., 2018</a>). These factors may confound associations between exposures and neuroimaging or neurodevelopmental outcomes, but they also represent malleable targets for prevention and early intervention. When possible, incorporating parental mental health symptoms as covariates offers a robust strategy to account for these confounding influences.</p> 

<p><b>Level 2 Scoring Not Available in Current Release (1.0)</b><br>
Note that calculated scores for Level 2 measures will be included in a future release - see the relevant <a href="../../../../changelog/knownissues/#apa-12">Known Issue</a> for details. In the interim, users are encouraged to score individual scales themselves according to the provided <a href="#scoring">scoring procedures</a>.</p>
</div>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>No</td></tr>
<tr><td><b>Respondent</b></td>
<td style="word-wrap: break-word; white-space: normal;">Pregnant Participant, Birth Parent, or Primary Caregiver</td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">Self-administered in-person or remote</td></tr>
<tr><td><b>Visits</b></td>
<td>V01, V02, V03</td></tr>
<tr><td><b>Completion Time</b></td>
<td>5 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;">
<ul>
<li>Checks for missing data based on counts for items completed by each participant</li>
<li>Verification of scoring accuracy</li>
<li>Summary statistics to examine item-level frequencies and total scores</li>
<li>Review of response distributions for potential outliers</li>
</ul>        
</td></tr>
</tbody>
</table>

## Instrument Details

The HBCD mental health screening instrument is a highly sensitive screening tool for use in community samples. It has two levels, adapted from DSM-5 Self-Rated [Level 1](https://www.psychiatry.org/getmedia/e0b4b299-95b3-407b-b8c2-caa871ca218d/APA-DSM5TR-Level1MeasureAdult.pdf) and [Level 2](https://www.psychiatry.org/psychiatrists/practice/dsm/educational-resources/assessment-measures) Cross-Cutting Symptom Measures:

<img src="../DSM-5Level2Cross-CuttingSymptomMeasures.png" width="90%" height="auto" class="center">

**Level 1** includes 1 - 2 questions for each of <span class="tooltip">11 mental health domains <span class="emoji"><i class="fa-solid fa-circle-info"></i></span><span class="tooltiptext">Depression, Anger, Mania, Anxiety, Somatic Symptoms, Suicidal Ideation, Psychosis, Sleep Disturbance, Memory, Repetitive Behaviors, Dissociation</span></span>. This excludes *Personality Functioning* and *Substance Use* present in the original measure (SU is captured by a separate set of instruments for HBCD - see measures listed [here](../../index.md#pregexp)). When symptoms were reported for Level 1, participants were subsequently administered corresponding **Level 2** measures, which asked about <span class="tooltip">additional symptoms <span class="emoji"><i class="fa-solid fa-circle-info"></i></span><span class="tooltiptext">Anger, Anxiety, Depression, Somatic Symptoms, Mania, Repetitive Thoughts, Sleep Problems</span></span> associated with the following 8 mental health domains: Anxiety, Anger, Depression, Mania, Personality, Repetitive Behavior, Sleep, and Somatic symptoms. For HBCD, Level 2 symptom measures for *Depression* and *Sleep Disturbance* were replaced with the PROMIS Short Forms v1.0 [Depression 8a questionnaire](https://www.phenxtoolkit.org/toolkit_content/supplemental_info/psychiatric/measures/07_Depressed_Mood.doc) and [Sleep Disturbance 8a](https://heal.nih.gov/files/CDEs/2024-07/promis-sleep-disturbance-8a-crf.pdf). Level 2 additionally includes the [Personality Inventory for DSM-5 Brief](https://www.psychiatry.org/File%20Library/Psychiatrists/Practice/DSM/APA_DSM5_The-Personality-Inventory-For-DSM-5-Brief-Form-Adult.pdf), which assesses <span class="tooltip">5 personality trait domains <span class="emoji"><i class="fa-solid fa-circle-info"></i></span><span class="tooltiptext">Negative Affect, Detachment, Antagonism, Disinhibition, Psychoticism</span></span>.

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
<p><b>Gating Modifications</b><br>
Gating was adapted for the HBCD study population so that participants proceeded automatically to the Level 2 measure for Personality Inventory. In addition, all participants answered the Level 1 questions for Depression and Somatic Symptoms, but proceeded to Level 2 questions irrespective of answers. <strong>Future publications should be sure to acknowledge the removal of Level 1 and 2 Substance Use and the gating mechanisms for Personality Inventory, Depression, and Somatic Symptoms.</strong></p>
<p><b>Clinical Alerts</b><br>
This measure was modified to alert HBCD study staff if responses to the Level 1 APA self-harm question ('Thoughts of actually hurting yourself?') or Level 2 APA Depression questionnaire (items from 'I felt worthless' to 'I felt that nothing could cheer me up') exceed thresholds of 0 and 32, respectively.</p>
<p><b>Response Option Changes</b><br>
For HBCD, the response option ‘Decline to answer’ was added to all questions. The response option ‘Don’t know’ was also included at the beginning of data collection, but was subsequently removed. Questions answered with ‘Decline to answer’ or ‘Don’t know’ are marked as missing.</p> 
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
<p><b>Depression and Sleep</b><br>
For Depression and Sleep, when any item responses are marked missing, the sum score is marked as missing.</p>

<p><b>Personality Inventory</b><br>
For the Personality Inventory measure, the total sum and average scores are only calculated for the full scale; individual subscale scores are not provided. Data users interested in subscale scores should refer to Personality Inventory scoring procedures for instructions on calculating subscale scores.</p>

<p><b>Remaining Level 2 Measures</b><br>
For the remaining Level 2 measures, sum scores are prorated when up to 25% of item responses are marked missing. If more than 25% of items are missing, the sum score is marked as missing. The following formula is used to generated a prorated score, with the answer rounded to the nearest whole number: 
<p style="font-size: 0.9em;">
  \[
  \text{Prorated Score} = \left( \frac{\text{Sum of answered items}}{\text{Number of items answered}} \right) \times \text{Total number of items}
  \]
</p>
</p>
<p>
<ul>
<b>Scoring Resources</b><br>
<li><a href="https://www.psychiatry.org/getmedia/e0b4b299-95b3-407b-b8c2-caa871ca218d/APA-DSM5TR-Level1MeasureAdult.pdf">Level 1 Cross-Cutting Symptom Measures</a> </li>
<li><a href="https://www.psychiatry.org/psychiatrists/practice/dsm/educational-resources/assessment-measures">Level 2 Cross-Cutting Symptom Measures</a></li>
<li><a href="https://www.healthmeasures.net/images/PROMIS/manuals/Scoring_Manual_Only/PROMIS_Depression_Scoring_Manual_05Dec2023.pdf">Depression 8a questionnaire</a> </li>
<li><a href="https://www.healthmeasures.net/images/PROMIS/manuals/Scoring_Manual_Only/PROMIS_Sleep_Scoring_Manual.pdf">Sleep Disturbance 8a</a></li>
<li><a href="https://www.psychiatry.org/File%20Library/Psychiatrists/Practice/DSM/APA_DSM5_The-Personality-Inventory-For-DSM-5-Brief-Form-Adult.pdf">Personality Inventory for DSM-5 Brief</a></li>
</ul>
</p>
</div>

## References
<div class="references">
<p>Doss, R. A., &amp; Lowmaster, S. E. (2022). Validation of the DSM-5 Level 1 Cross-Cutting Symptom Measure in a Community  Sample. <em>Psychiatry Research</em>, <em>318</em>, 114935. <a href="https://doi.org/10.1016/j.psychres.2022.114935">https://doi.org/10.1016/j.psychres.2022.114935</a></p>
<p>Estabrook, R., Massey, S. H., Clark, C. A. C., Burns, J. L., Mustanski, B. S., Cook, E. H., O’Brien, T. C., Makowski, B., Espy, K. A., & Wakschlag, L. S. (2016). Separating family-level and direct exposure effects of smoking during pregnancy on offspring externalizing symptoms: Bridging the behavior genetic and behavior teratologic divide. Behavior Genetics, 46(3), 389–402. <a href="https://doi.org/10.1007/s10519-015-9762-2">https://doi.org/10.1007/s10519-015-9762-2</a></p>
<p>Massey, S. H., Lieberman, D. Z., Reiss, D., Leve, L. D., Shaw, D. S., & Neiderhiser, J. M. (2011). Association of clinical characteristics and cessation of tobacco, alcohol, and illicit drug use during pregnancy. The American Journal on Addictions. <a href="https://doi.org/10.1111/j.1521-0391.2010.00110.x">https://doi.org/10.1111/j.1521-0391.2010.00110.x</a></p>
<p>Massey, S. H., Mroczek, D. K., Burns, J. L., Clark, C. A. C., Espy, K. A., & Wakschlag, L. S. (2018). Positive parenting behaviors in women who spontaneously quit smoking during pregnancy: Clues to putative targets for preventive interventions. Neurotoxicology and Teratology, 67, 18–24.<a href="https://doi.org/10.1016/j.ntt.2018.02.003">https://doi.org/10.1016/j.ntt.2018.02.003</a></p>
<p>Massey, S. H., Neiderhiser, J. M., Shaw, D. S., Leve, L. D., Ganiban, J. M., & Reiss, D. (2012). Maternal self concept as a provider and cessation of substance use during pregnancy. Addictive Behaviors, 37(8), 956–961. <a href="https://doi.org/10.1016/j.addbeh.2012.04.002">https://doi.org/10.1016/j.addbeh.2012.04.002</a></p>
<p>Massey, S. H., Reiss, D., Neiderhiser, J. M., Leve, L. D., Shaw, D. S., & Ganiban, J. M. (2016). Maternal personality traits associated with patterns of prenatal smoking and exposure: Implications for etiologic and prevention research. Neurotoxicology and Teratology, 53, 48–54. <a href="https://doi.org/10.1016/j.ntt.2015.11.010">https://doi.org/10.1016/j.ntt.2015.11.010</a></p>
<p>Roche, M. J., Pincus, A. L., &amp; Cole, P. E. (2019). Linking dimensions and dynamics in psychopathology research: An example using DSM-5 instruments. <em>Journal of Research in Personality</em>, <em>82</em>, 103852. <a href="https://doi.org/https://doi.org/10.1016/j.jrp.2019.103852">https://doi.org/https://doi.org/10.1016/j.jrp.2019.103852</a></p>
</div>
<br>
