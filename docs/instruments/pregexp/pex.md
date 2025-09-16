# Pregnancy & Infant Health Instruments

## Health V1 & V2 Instruments

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
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
    <td>Health V1- Health History</td>
    <td>Healthhx</td>
    <td>Pre-pregnancy and pregnancy health</td>
    <td><code>pex_bm_health_preg__healthhx</code></td>
</tr>
<tr>
    <td>Health V1- Exposures & Vaccines</td>
    <td>Vacc</td>
    <td>Vaccines in pregnancy</td>
    <td><code>pex_bm_health_preg__exp__vacc</code></td>
</tr>
<tr>
    <td>Health V1- Chronic Conditions</td>
    <td>Chroncond</td>
    <td>Chronic conditions/STIs in pregnancy</td>
    <td><code>pex_bm_health_preg__chroncond</code></td>
</tr>
<tr>
    <td>Health V1- Illness</td>
    <td>Illness</td>
    <td>Illness in pregnancy</td>
    <td><code>pex_bm_health_preg__illness</code></td>
</tr>
<tr>
    <td>Health V1- ER Admissions</td>
    <td>ERhosp</td>
    <td>ER or hospitalization in pregnancy</td>
    <td><code>pex_bm_health_preg__erhosp</code></td>
</tr>
<tr>
    <td>Health V1- Medications</td>
    <td>Meds</td>
    <td>Medications in pregnancy</td>
    <td><code>pex_bm_health_preg__meds</code></td>
</tr>
<tr>
    <td>Health V2- Pregnancy</td>
    <td>Healthv2 Preg</td>
    <td>Health updates up to delivery</td>
    <td><code>pex_bm_healthv2_preg</code></td>
</tr>
<tr>
    <td>Health V2- Infancy</td>
    <td>Healthv2 Inf</td>
    <td>Delivery and birth outcomes</td>
    <td><code>pex_bm_healthv2_inf</code></td>
</tr>
</tbody>
</table>

<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Responsible Use Warning (<i>Health V1- Health History</i>)</span>
  <a class="anchor-link" href="#alert" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p>Amidst powerful societal expectations to ‘do what’s best for the baby’ during pregnancy (i.e. by stopping substance use), up to half of pregnancies in the United States are unintended with 1 in 5 unwanted (<a href="https://doi.org/10.1016/S2214-109X(20)30315-6">Bearak et al. 2020</a>). This discrepancy contributes to implicit bias against pregnant individuals who use substances as ‘not caring about their babies’ which is neither humane, nor evidence based (<a href="https://doi.org/10.1016/j.socscimed.2022.115071">Massey et al., 2022</a>). While cessation of substance use during pregnancy is universally recognized as optimal, the ability to make this “parental” sacrifice varies substantially between birthing individuals and within individuals between their different pregnancies (<a href="https://doi.org/10.1007/s00737-023-01396-z">Level et al., 2024</a>). Failure to recognize this inherent heterogeneity in pregnancy intention stigmatizes substance users who did not intend to want to become pregnant. Summarily, inclusion of pregnancy intention as a covariate in all studies that characterize prenatal substance exposure (in the absence of a strong justification otherwise) is thus strongly recommended to acknowledge myriad experiences of birthing parents who participated in HBCD who made this research possible.</p>
</div>

<div id="warning-coding" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning: (<i>Coding Issues- ICD, WHO, RxNORM</i>)</span>
  <a class="anchor-link" href="#warning-coding" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Coding challenges were identified for the following systems:</p>
  <ul>
    <li>ICD codes (via BioPortal) – reasons for medication use, ER visits, and hospitalizations</li>
    <li>WHO symptom codes – symptom reporting</li>
    <li>RxNORM – medication names</li>
  </ul>
  <p>Difficulties arose both for participants (describing symptoms/medications) and for HBCD staff (locating the correct term in the databases).  
    The following instruments were impacted by coding issues:</p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
    <th>Instrument</th>
    <th>Coding Issues</th>
</thead>
<tbody>
<tr>
    <td>Health V1- Illness</td>
    <td style="word-wrap: break-word; white-space: normal;">
    • Illnesses captured via BioPortal ICD or WHO symptom codes<br>
    • Participants had difficulty naming conditions<br>
    • Staff had difficulty locating correct codes
    </td>
</tr>
<tr>
    <td>Health V1- ER Admissions</td>
    <td style="word-wrap: break-word; white-space: normal;">
    • Reasons captured via BioPortal ICD codes<br>
    • Coding difficult for use of ER for normal care visits (no diagnosis)<br>
    • False alarms (e.g., suspected water break) often coded as “don’t know”
    </td>
</tr>
<tr>
    <td>Health V1- Medications</td>
    <td style="word-wrap: break-word; white-space: normal;">
    • Medication names from RxNORM; reasons from BioPortal ICD<br>
    • No option for preventive use → aspirin (to prevent preeclampsia) moved to prenatal vitamin section a few months into the study<br>
    • PRN (“as needed”) medications inconsistently reported<br>
    • Some medications were coded with dose, but this was not asked and should not be used
    </td>
</tr>
<tr>
    <td>Health V2- Pregnancy</td>
    <td style="word-wrap: break-word; white-space: normal;">Same ICD (via BioPortal) and RxNORM issues as V1</td>
</tr>
<tr>
    <td>Health V2- Infancy</td>
    <td style="word-wrap: break-word; white-space: normal;">Same ICD (via BioPortal) and RxNORM issues as V1</td>
</tr>
</tbody>
</table>
</div>

<div id="warning-filt" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning (<i>Health V2- Infancy Filters</i>)</span>
  <a class="anchor-link" href="#warning-filt" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Out-of-range values were filtered (i.e. changed to "n/a") for Health V2- Infancy (<code>pex_bm_healthv2_inf</code>). Valid field values are documented <a href="../../../changelog/versions/R1/#filtered-field-values" target="_blank">here</a> under Exclusion Criteria for the current release.</p>
</div>

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">The data for one or more of these instruments has known issues - <a href="../../../changelog/knownissues/#pregnancy-infant-health" target="_blank">see details</a>.</span>
</div>

## Administration & Quality Control

#### Administration
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px">
<thead>
<tr>
    <th>Instrument</th>
    <th>Child-Specific</th>
    <th>Respondent</th>
    <th>Administration</th>
    <th>Visits</th>
    <th>Completion</th>
</tr>
</thead>
<tbody>
<tr>
<td>Healthhx</td>
<td>No</td>
<td>Pregnant Participant</td>
<td>Self-Administered</td>
<td>V01</td>
<td>5 min</td>
</tr>
<tr>
<td>Vacc</td>
<td>No</td>
<td>Pregnant Participant</td>
<td>Self-Administered</td>
<td>V01</td>
<td>3 min</td>
</tr>
<tr>
<td>Chroncond</td>
<td>No</td>
<td>Pregnant Participant</td>
<td>Self-Administered (in person)</td>
<td>V01</td>
<td>3 min</td>
</tr>
<tr>
<td>Illness</td>
<td>No</td>
<td>Pregnant Participant</td>
<td>HBCD Study Staff (in-person)</td>
<td>V01</td>
<td>3 min</td>
</tr>
<tr>
<td>ERhosp</td>
<td>No</td>
<td>Pregnant Participant</td>
<td>HBCD Study Staff (in-person)</td>
<td>V01</td>
<td>5 min</td>
</tr>
<tr>
<td>Meds</td>
<td>No</td>
<td>Pregnant Participant</td>
<td>HBCD Study Staff (in-person)</td>
<td>V01</td>
<td>5 min</td>
</tr>
<tr>
<td>Healthv2 Preg</td>
<td>No</td>
<td>Birth Parent</td>
<td>HBCD Study Staff (in person)</td>
<td>V02</td>
<td>10 min</td>
</tr>
<tr>
<td>Healthv2 Inf</td>
<td>Yes</td>
<td style="word-wrap: break-word; white-space: normal;">Birth Parent or Primary Caregiver on Child</td>
<td>HBCD Study Staff (in person)</td>
<td>V02</td>
<td>10 min</td>
</tr>
</tbody>
</table>

#### Quality Control  
For all pregnancy and infant health instruments listed on this page, quality control was performed by reviewing response distributions for outliers.

## Instrument Details
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
    <td>Healthhx</td>
    <td style="word-wrap: break-word; white-space: normal;">Pre-pregnancy and pregnancy health outcomes, including: gravidity and parity, height and weight, pregnancy intentions, use of assisted reproductive technology, start of prenatal care, prenatal vitamin or aspirin use, secondhand smoke</td>
</tr>
<tr>
    <td>Vacc</td>
    <td style="word-wrap: break-word; white-space: normal;">Vaccines in pregnancy, including receipt of common vaccines in pregnancy and trimester received.</td>
</tr>
<tr>
    <td>Chroncond</td>
    <td style="word-wrap: break-word; white-space: normal;">Information on chronic conditions and sexually transmitted infections (STIs) during pregnancy, including whether they are ongoing or resolved.</td>
</tr>
<tr>
    <td>Illness</td>
    <td style="word-wrap: break-word; white-space: normal;">Illness in pregnancy, including start and stop dates and whether the person had a fever.</td>
</tr>
<tr>
    <td>ERhosp</td>
    <td style="word-wrap: break-word; white-space: normal;">ER visit(s) or hospitalization(s) during pregnancy, including occurrence(s) and reason(s).</td>
</tr>
<tr>
    <td>Meds</td>
    <td style="word-wrap: break-word; white-space: normal;">Medications used during pregnancy (since last menstrual period), including prescription and over-the-counter medications. It includes details such as the name of the medication, its indication, frequency of use, and start/stop dates.</td>
</tr>
<tr>
    <td>Healthv2 Preg</td>
    <td style="word-wrap: break-word; white-space: normal;">Health updates for the birth parent between enrollment and delivery, including: prenatal vitamin use, aspirin intake, infections and illnesses, vaccinations, medication use (ongoing and newly prescribed), pregnancy complications (e.g., gestational diabetes), labor and delivery details (e.g., delivery method, location, and hospital stay duration)
    </td>
</tr>
<tr>
    <td>Healthv2 Inf</td>
    <td style="word-wrap: break-word; white-space: normal;">Delivery and birth outcomes, including: infant characteristics (birth weight & length, duration of hospital stay); newborn conditions (birth defects, genetic diagnoses); medical interventions including NICU admission and length of stay, intubation, adverse outcomes (e.g. bronchopulmonary dysplasia, congenital syphilis), medications (name, indication, status), healthcare access, and specialist visits; and newborn hearing test results</td>
</tr>
</tbody>
</table>

## References
<div class="references">
    <p>Bearak, J., Popinchalk, A., Ganatra, B., Moller, A.-B., Tunçalp, Ö., Beavin, C., Kwok, L., & Alkema, L. (2020). Unintended pregnancy and abortion by income, region, and the legal status of abortion: estimates from a comprehensive model for 1990-2019. The Lancet. Global Health, 8(9), e1152–e1161. <a href="https://doi.org/10.1016/S2214-109X(20)30315-6">https://doi.org/10.1016/S2214-109X(20)30315-6</a></p>
    <p>Level, R. A., Zhang, Y., Tiemeier, H., Estabrook, R., Shaw, D. S., Leve, L. D., Wakschlag, L. S., Reiss, D., Neiderhiser, J. M., & Massey, S. H. (2024). Unique influences of pregnancy and anticipated parenting on cigarette smoking: results and implications of a within-person, between-pregnancy study. Archives of Women’s Mental Health, 27(2), 301–308. <a href="https://doi.org/10.1007/s00737-023-01396-z">https://doi.org/10.1007/s00737-023-01396-z</a></p>
    <p>Massey, S. H., Neiderhiser, J. M., Shaw, D. S., Leve, L. D., Ganiban, J. M., & Reiss, D. (2012). Maternal self concept as a provider and cessation of substance use during pregnancy. Addictive Behaviors, 37(8), 956–961. <a href="https://doi.org/10.1016/j.addbeh.2012.04.002">https://doi.org/10.1016/j.addbeh.2012.04.002</a></p>
    <p>Massey, S. H., Estabrook, R., Lapping-Carr, L., Newmark, R. L., Decety, J., Wisner, K. L., & Wakschlag, L. S. (2022). Are empathic processes mechanisms of pregnancy’s protective effect on smoking? Identification of a novel target for preventive intervention. Social Science & Medicine (1982), 305(115071), 115071. <a href="https://doi.org/10.1016/j.socscimed.2022.115071">https://doi.org/10.1016/j.socscimed.2022.115071</a></p>
    <p>Schoenaker, D. A. J. M., Ploubidis, G. B., Goodman, A., & Mishra, G. D. (2017). Factors across the life course predict women’s change in smoking behaviour during pregnancy and in midlife: results from the National Child Development Study. Journal of Epidemiology and Community Health, 71(12), 1137–1144. <a href="https://doi.org/10.1136/jech-2017-209493">https://doi.org/10.1136/jech-2017-209493</a></p>
</div>