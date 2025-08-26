# ASSIST V1/V2/V3

**Full Name**: Alcohol, Smoking and Substance Involvement Screening Test V1.0, V2.0, and V3.0                            

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
<td>&nbsp;</td>
<td style="text-align: center;"><b>Construct</b></td>
<td style="text-align: center;"><b>Table Name</b></td>
</tr>
</thead>
<tbody>
<tr><td><strong>ASSIST V1</strong></td>
<td>Substance use and problematic use before and during pregnancy</td>
<td><code>pex_bm_assistv1</code></td>
</tr>
<tr><td><strong>ASSIST V2</strong></td>
<td style="word-wrap: break-word; white-space: normal;">Substance use during end of pregnancy ( between V01 and delivery) and postnatal (weeks 0-4, between delivery and V2)</td>
<td><code>pex_bm_assistv2</code></td></tr>
<tr><td><strong>ASSIST V3</strong></td>
<td style="word-wrap: break-word; white-space: normal;">Substance use after pregnancy</td>
<td><code>pex_bm_assistv3</code></td></tr>
</tbody>
</table>

<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Responsible Use Warning: V1 & V2</i></span>
  <a class="anchor-link" href="#alert" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p>Responsible use of prenatal drug exposure data requires thoughtful interpretation of exposure-related outcomes in the context of measured and unmeasured confounders. These confounders include, but are not limited to, phenotypic risks associated with persistent alcohol, tobacco, and other drug use during pregnancy by birthing parents (<a href="https://doi.org/10.1111/j.1521-0391.2010.00110.x">Massey et al., 2010</a>), and confounding by familial risk from within-family studies (<a href="https://doi.org/10.1007/s10519-015-9762-2">Estabrook et al., 2016</a>).</p>
<p>Finally, unwarranted speculation about ‘neural bases of behavior’ form differences in neuroimaging between exposed and unexposed children in the absence of differences in behavioral performance can exacerbate stigma already faced by birthing parents with substance use disorders and their children (<a href="https://doi.org/10.1016/j.ntt.2015.07.002">McAllister & Hart 2015</a>).</p> 
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
<p>It was difficult for some participants to self-report the typical size of a single drink (in oz) to capture ‘standard drinks’ of alcohol for ASSIST, leading to some reports falling outside the expected range. Similarly, reporting the frequency of use for substances like electronic cigarette devices proved difficult, resulting in outliers. While sites were queried on these outliers, participants could not always be re-contacted for clarification.</p> 
</div>


## Administration & Quality Control

#### Common to All Versions
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>No</td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">HBCD Study Staff, in-person (except in Alabama, where participants were trained to self-administer)</td></tr>
</tbody>
</table>

#### Version-Specific Items
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
<td>&nbsp;</td>
<td style="text-align: center;"><b>ASSIST V1</b></td>
<td style="text-align: center;"><b>ASSIST V2</b></td>
<td style="text-align: center;"><b>ASSIST V3</b></td>
</tr>
</thead>
<tbody>
<tr><td><b>Respondent</b></td>
<td style="word-wrap: break-word; white-space: normal;">Pregnant Participant</td>
<td style="word-wrap: break-word; white-space: normal;">Birth Parent</td>
<td style="word-wrap: break-word; white-space: normal;">Person who gave birth or Primary Caregiver</td>
</tr>
<tr><td><b>Visits</b></td>
<td>V01</td>
<td>V02</td>
<td>V03</td>
</tr>
<tr><td><b>Completion Time</b></td>
<td>5 min</td>
<td>5 min</td>
<td>3 min</td>
</tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;">Response distributions are reviewed for outliers and additionally cross-checked with TLFB to ensure consistency in reported substances.</td>
<td style="word-wrap: break-word; white-space: normal;">Response distributions are reviewed for outliers and additionally cross-checked with TLFB to ensure consistency in reported substances.</td>
<td style="word-wrap: break-word; white-space: normal;">Response distributions are reviewed for outliers.</td>
</tr>
</tbody>
</table>

## Instrument Details

The HBCD ASSIST V1, V2, and V3 measures were modified from the [NIDA Quick Screen (Modified ASSIST)](https://nida.nih.gov/sites/default/files/pdf/nmassist.pdf) and included questions from the Family History Assessment Module (FHAM) and the All of Us Personal and Family Health History. The original NIDA quick screen was scored; however, our version is not scored. To acknowledge these changes in future publications, authors can note that questions were motivated from the NIDA Modified ASSIST.

The NIDA quick screen tool (*have you used alcohol, tobacco, prescription drugs, or illegal drugs in the last year*) was modified to assess more details regarding types of substances used and the timeline of use before and during pregnancy - see [HBCD Modification Details](#hbcd-mod) for modifications made to each instrument version. In addition, for lifetime and problematic use, and use pre-pregnancy, pregnancy, end-pregnancy, post-pregnancy, and past 3 months, use was greatly expanded - see [Expanded ASSIST Substance Type Options](#substance-options).

Finally, the Time Line Follow Back (TLFB) was triggered when substance use was reported before [`pre-use`] or during pregnancy [`during_use`] on the ASSIST V1 or at the end of pregnancy [`end_use`] on the ASSIST V2 (see [documentation on TLFB](tlfb.md)). 

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
<ul>
<b>Replacement Questions for NIDA Quick Screen Tool</b><br>
<b>ASSIST V1</b><br>
<strong>Assess lifetime use [lt] and disordered use, or use causing problems in their lives:</strong>
<ul>
    <li>[lt_use] IN YOUR LIFE, which of the following substances have you EVER used for any reason? [followed by list of substance options from section below]</li>
    <li>[concern] Have you EVER been concerned about your use of this substance or worried it was problematic use?</li>
    <li>[concernoth] Has a friend, relative, or anyone else EVER expressed concern about your use of this substance?</li>
    <li>[control] Have you EVER tried and failed to control, cut down, or stop using this substance?</li>
    <li>[tx] Have you EVER sought or received treatment related to your use of this substance by a medical provider, spiritual leader, community mutual help group (like AA or SMART Recovery), counselors, or in other settings</li>
    <li>[diagn] Have you EVER been clinically diagnosed with abuse, dependence, or a substance use disorder related to your use of this substance</li>
    <li>[med] Have you EVER taken (prescribed or otherwise) medication(s) as treatment for a problem substance</li>
</ul>
  <strong>Assess use 3 months pre-pregnancy [pre] and use during pregnancy [during]:</strong>
<ul>
  <li>[pre_use] IN THE THREE MONTHS BEFORE YOU BECAME PREGNANT, which of the following substances have you ever used for any reason? [followed by list of substance options from section below]</li>
  <li>[during_use] DURING YOUR PREGNANCY, which of the following substances have you ever used for any reason? [followed by list of substance options from section below]</li>
  <li>[during_med] DURING YOUR PREGNANCY, did you take (prescribed or otherwise) medication(s) as treatment for a problem substance? [followed by list of medications used to treat substance use problems]</li>
</ul>
<b>ASSIST V2</b><br>
<strong>Assess use after pregnancy:</strong>
<ul>
    <li>[end_use] SINCE WE LAST MET UNTIL THE END OF PREGNANCY, which of the following substances did you use for any reason? [followed by list of substance options from section below]</li>
    <li>[end_med] SINCE WE LAST MET UNTIL THE END OF PREGNANCY, did you take (prescribed or otherwise) medication(s) as treatment for a problem substance? [followed by list of medications used to treat substance use problems]</li>
    <li>[post_use] FROM THE TIME THAT YOU DELIVERED your child until now, how often have you used any of the following substances for any reason? [followed by list of substance options from section below]</li>
</ul>
<b>ASSIST V3</b><br>
<strong>Assess use and impact of substance use after pregnancy in past 3 months (3m):</strong>
<ul>
    <li>[3m_use] IN THE PAST THREE MONTHS, how often have you used any of the following substances for any reason? [followed by list of substance options from section below]</li>
    <li>[problem] DURING THE PAST THREE MONTHS, has your use of this substance led to physical or mental health, social, or financial problems?</li>
    <li>[perform] DURING THE PAST THREE MONTHS, have you ever failed to do what was normally expected of you (like work, go to school, be a parent, or household tasks) because of your use of this substance?</li>
</ul>
</div>

<div id="substance-options" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Expanded ASSIST Substance Type Options</span>
  <a class="anchor-link" href="#substance-options" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
 <ul>
      <li>[001] Nicotine or tobacco products (cigarettes, e-cigarettes, chewing tobacco, cigars, etc.)</li>
        <li>[002] Alcoholic beverages (beer, wine, spirits, etc.)
              <ul>
                  <li><b>IF ENDORSED:</b> specify type and average volume of one glass/container typically consumed (U.S.-defined ‘standard drinks’ were then calculated by dividing the amount reported by 12oz (beer, hard cider, hard seltzer), 5oz (wine) or 1.5 oz (spirits))</li>
              </ul>
        </li>
        <li>[003] Cannabis (marijuana, weed, pot, hash, wax, blunts, dabs, gummies, vapes, etc.)</li>
        <li>[004] Cannabidiol (CBD; not containing THC)</li>
        <li>[005] Synthetic cannabinoids (K2, spice, etc.)
        <li>[006] Prescription opioids (oxycodone, morphine, codeine, fentanyl, tramadol, etc.)
              <ul>
                  <li><b>IF ENDORSED:</b> specify type of opioid used and typical quantities per occasion for the following: heroin (grams, bags), prescription opioids (pills), buprenorphine (pills, injectables, films), and methadone (mg)</li>
              </ul>
        </li>
        <li>[007] Heroin or other illicit opioids (fentanyl, oxycodone, etc.)</li>
        <li>[008] Methadone</li>
        <li>[009] Buprenorphine</li>
        <li>[010] Benzodiazepines, sedatives, or sleeping pills (Valium, Xanax, Ambien, barbiturates, etc.)</li>
        <li>[011] Cocaine (coke, crack, etc.)</li>
        <li>[012] Amphetamine type stimulants (speed, Adderall, diet pills, etc.)</li>
        <li>[013] Methamphetamine (meth, crystal meth, etc.)</li>
        <li>[014] Inhalants (nitrous, glue, petrol, paint thinner, etc.)</li>
        <li>[015] Hallucinogens or club drugs (LSD, acid, mushrooms, psilocybin, MDMA, molly, ecstasy, Special K, GHB, etc.)</li>
        <li>[016] Androgenic anabolic steroids (for performance enhancement)</li>
        <li>[017] Phencyclidine (PCP)</li>
        <li>[018] Kratom</li>
        <li>[019] Xylazine</li>
      <strong>Medications used to treat substance use problems</strong>
        <li>[001] Acamprosate (Campral), topiramate (Topamax), or gabapentin (Neurontin)</li>
        <li>[002] Disulfiram (Antabuse)</li>
        <li>[003] Naltrexone (Revia, Vivitrol)</li>
    </ul>
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
<p>For each substance, participants indicate whether they had ever used it and, if endorsed, frequency of use with options: 0 (Never), 1 (Once or Twice), 2 (Monthly), 3 (Weekly), or 4 (Daily or Almost Daily). For substances reported as used pre-pregnancy, during pregnancy, and end-pregnancy, participants were asked about modes of use and typical quantities/amounts of consumption for alcohol and opioids (if applicable).</p>
</div>

## References
<div class="references">
<p>Coles, C. D. (1993). Saying “goodbye” to the “crack baby.” Neurotoxicology and Teratology, 15(5), 290–292; discussion 311-2. <a href="https://doi.org/10.1016/0892-0362(93)90024-i" target="_blank">https://doi.org/10.1016/0892-0362(93)90024-i</a></p>
  <p>
    Estabrook, R., Massey, S. H., Clark, C. A. C., Burns, J. L., Mustanski, B. S., Cook, E. H., O’Brien, T. C., Makowski, B., Espy, K. A., & Wakschlag, L. S. (2016). Separating family-level and direct exposure effects of smoking during pregnancy on offspring externalizing symptoms: Bridging the behavior genetic and behavior teratologic divide. <i>Behavior Genetics</i>, <b>46</b>(3), 389–402. <a href="https://doi.org/10.1007/s10519-015-9762-2" target="_blank">https://doi.org/10.1007/s10519-015-9762-2</a>
  </p>
  <p>
    Gal, P., & Sharpless, M. K. (1984). Fetal drug exposure-behavioral teratogenesis. <i>Drug Intelligence & Clinical Pharmacy</i>, <b>18</b>(3), 186–201. <a href="https://doi.org/10.1177/106002808401800304" target="_blank">https://doi.org/10.1177/106002808401800304</a>
  </p>
  <p>
    Level, R. A., Zhang, Y., Tiemeier, H., Estabrook, R., Shaw, D. S., Leve, L. D., Wakschlag, L. S., Reiss, D., Neiderhiser, J. M., & Massey, S. H. (2024). Unique influences of pregnancy and anticipated parenting on cigarette smoking: results and implications of a within-person, between-pregnancy study. <i>Archives of Women’s Mental Health</i>, <b>27</b>(2), 301–308. <a href="https://doi.org/10.1007/s00737-023-01396-z" target="_blank">https://doi.org/10.1007/s00737-023-01396-z</a>
  </p>
  <p>
    Massey, S. H., Lieberman, D. Z., Reiss, D., Leve, L. D., Shaw, D. S., & Neiderhiser, J. M. (2010). Association of clinical characteristics and cessation of tobacco, alcohol, and illicit drug use during pregnancy. <i>The American Journal on Addictions</i>, no-no. <a href="https://doi.org/10.1111/j.1521-0391.2010.00110.x" target="_blank">https://doi.org/10.1111/j.1521-0391.2010.00110.x</a>
  </p>
  <p>
    McAllister, D., & Hart, C. L. (2015). Inappropriate interpretations of prenatal drug use data can be worse than the drugs themselves. <i>Neurotoxicology and Teratology</i>, <b>52</b>, 57. <a href="https://doi.org/10.1016/j.ntt.2015.07.002" target="_blank">https://doi.org/10.1016/j.ntt.2015.07.002</a>
  </p>
  <p>National Institute on Drug Abuse. (n.d.). <em>NIDA Modified ASSIST</em>.</p>
  <p>
    Shah, S. K., Perez-Cardona, L., Helner, K., Massey, S. H., Premkumar, A., Edwards, R., Norton, E. S., Rogers, C. E., Miller, E. S., Smyser, C. D., Davis, M. M., & Wakschlag, L. S. (2023). How penalizing substance use in pregnancy affects treatment and research: a qualitative examination of researchers’ perspectives. <i>Journal of Law and the Biosciences</i>, <b>10</b>(2), lsad019. <a href="https://doi.org/10.1093/jlb/lsad019" target="_blank">https://doi.org/10.1093/jlb/lsad019</a>
  </p>
  <p>
    Wakeman, S. E., Bryant, A., & Harrison, N. (2022). Redefining child protection. <i>Obstetrics and Gynecology</i>, <b>140</b>(2), 167–173. <a href="https://doi.org/10.1097/aog.0000000000004786" target="_blank">https://doi.org/10.1097/aog.0000000000004786</a>
  </p>
</div>
<br>