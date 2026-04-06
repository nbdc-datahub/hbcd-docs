# ERICA

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
  <td rowspan="2"><strong>ERICA</strong></td>
  <td rowspan="2">3-9M</td>
  <td>Child Emotional Regulation, Parenting, Caregiver-Child Relationship</td>
  <td><code>mh_cg_erica_3_9m</code></td>
</tr>
<tr>
  <td>ERICA Codes Reliability</td>
  <td><code>mh_cg_erica_rel_3_9m</code></td>
</tr>
</tbody>
</table>

<!-- LUCI NOTE <p>se they are consortium-wide fields that are usually included across all instruments (things like "age"). However ERICA is a special case because the SMEs noted that these fields will be inaccurate for this particular instrument.  ESPECIALLY when someone inevitably asks 9 months from now why "age" is missing from ERICA</p> -->

---

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
<p>The HBCD dataset includes many variables that may be important for sound and comprehensive analysis. The inclusion of additional variables will depend on the research question(s) and methodological approach. Users are encouraged to take time to explore the full range of available variables—especially those that may serve as controls, contextual indicators, confounders, mechanisms, or modifiers—to ensure thoughtful and well-supported analytic decisions. Other important considerations may include developmental functioning, broader family supports, and early adverse and protective exposures.</p>
<p>The ERICA assesses normative variations in child behavior, parenting, and the caregiver-child relationship and should be interpreted within the context of the child's age and developmental stage.  These data are meant to be used in aggregate, not on an individual basis.  This is not a clinical or diagnostic instrument.</p>
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
<p style="margin-bottom: 0;">Data Release 2.1 includes data from ERICA administrations completed as part of HBCD study visit 3 (3–9 Month) as of July 1, 2025, utilizing the ERICA infant paradigm, which includes a prelocomotor (3–7 month) and locomotor protocol (7–9 month).</p>
<hr style="margin-bottom: 0; margin-top: 0;">
<p>Coding data for a subset of participants may be missing from this data release for various reasons. This data will be added in future releases.</p>
<hr style="margin-bottom: 0; margin-top: 0;">
<p style="margin-bottom: 0;">The ERICA was administered in Spanish and English. The language of administration (i.e., in which RAs would deliver the instructions) does not always correspond with the language spoken by the caregiver/child during the activities. All videos in which the dyad speaks Spanish during the activities were coded by fully Spanish-English bilingual coders.</p>
<hr style="margin-bottom: 0; margin-top: 0;">
<p style="margin-bottom: 0;">Modifiers added at the activity level occasionally result in global scores of &lt;0 or &gt;3. Global scores that are &lt;0 should be converted to "0" by the user for analysis, and scores &gt;3 should be converted to "3" prior to analysis.</p>
<hr style="margin-bottom: 0; margin-top: 0;">
<p style="margin-bottom: 0;">The code for "caregiver irritable behavior" in Data Release 2.1 has a low base rate. We recommend dichotomizing (0 = 0 and &gt;0 = 1) for analysis.</p>
<hr style="margin-bottom: 0; margin-top: 0;">
<p style="margin-bottom: 0.1;">There are two data files included in this release. The files contain the same coding data for different participants and should be combined prior to analysis to create a single analytic file.</p>
</div>

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">Please review the <a href="https://docs.hbcdstudy.org/latest/changelog/issues-updates/" target="_blank">Known Issues & Pending Updates</a> page for updates that may affect data use.</span>
</div>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td><td>Yes</td></tr>
<tr><td><b>Respondent</b></td><td>Birth Parent or Primary Caregiver and Child</td></tr>
<tr><td><b>Administration</b></td><td>HBCD Study staff in-person</td></tr>
<tr><td><b>Visits</b></td><td>V03</td></tr>
<tr><td><b>Completion Time</b></td><td>20-30 minutes</td></tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;">QC procedures were conducted separately for <b>(1) ERICA site-level administration</b> and <b>(2) the centralized coding of ERICA videos</b>. Expand <a href="#qc">Quality Control Details</a> below for full documentation.</td></tr>
</tbody>
</table>

<div id="qc" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-shield"></i></span>
  <span class="text-with-link">
  <span class="text">Quality Control Details</span>
  <a class="anchor-link" href="#qc" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><b>ERICA Administration</b></p>
<ul style="font-size: 0.8em;">
<li>HBCD study staff were trained and certified to administer the ERICA by experienced ERICA administrators to ensure adherence to standardized procedures.</li>
<li>Ongoing quality of administration was ensured through video review of every 10th administration at each site, with higher levels of review conducted for sites that did not meet fidelity benchmarks.</li>
<li>Completion rates were monitored and site level data on administration was reviewed for potential QC issues (e.g., frequent protocol interruptions or tech issues), with results informing site-level training and follow-up.</li>
<li>Additional training was provided as needed.</li>
</ul>
<p><b>ERICA Coding</b></p>
<ul style="font-size: 0.8em;">
<li>An independent team of coders was trained for reliability by two expert coders, themselves trained and supervised by one of the ERICA developers.</li>
<li>Coders were certified as reliable upon achieving 80% agreement on each code (within ±0.5 decimal points) with the expert coders.</li>
<li>Once certified, 20% of each coder&#39;s videos were randomly selected and double coded by specially trained, gold-standard coders to ensure ongoing reliability.</li>
<li>Coders were required to maintain 80% reliability at the item-level (within ±0.5 decimal places) to continue coding videos.</li>
<li>Reliability was monitored weekly.</li>
<li>If a coder dropped below 80% reliability for two consecutive weeks, they were pulled for re-training/re-certification prior to coding additional videos.</li>
<li>All coding was done via a single, one-pass, video review, with codes entered into the HBCD database. Double data entry and conflict resolution were utilized to ensure the accuracy of coding data entry.</li>
<li>In addition to percent agreement, coder reliability was monitored utilizing a two-way, mixed effects, intraclass correlation coefficient (ICC) for all codes, except Caregiver Irritable Behavior, which had a low base rate and was thus dichotomized for Data Release 2.1, with reliability estimated using an unweighted kappa instead (see "Data Release 2.1 Reliability Statistics" in attachments for a table of alphas for this data set). We will continue to monitor all reliability and coding; thus, Caregiver Irritable Behavior may be updated in future data releases.</li>

<!-- LUCI NOTE: add ata Release 2.1 Reliability Statistics" -->
<li>Data dashboards and reports were regularly monitored for missing data or unexpected score distributions and completion reports were cross-tabulated with video files to ensure alignment.</li>
</ul>
</div>

## Instrument Details

The Early Regulation in Context Assessment (**ERICA**) is a standardized observational paradigm that is adapted from the well-validated Disruptive Behavior Diagnostic Observation Schedule (DB-DOS) ([Krogh-Jespersen et al. 2022](https://doi.org/10.3389/fpsyg.2021.732312)). The ERICA assesses early child regulation in the context of the caregiver-child relationship via a series of five brief, developmentally appropriate activities that “press” for regulation within the dyad (e.g., frustration, engagement, enjoyment).

The ERICA is coded using a one-pass, global coding system adapted for HBCD. Seven codes are organized across child, caregiver, and dyadic domains:

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
<td><b>Child</b></td>
<td>Positive affect; Irritability; Social engagement</td>
</tr>
<tr>
<td><b>Caregiver</b></td>
<td>Responsive behavior; Irritable behavior; Directive behavior</td>
</tr>
<tr>
<td><b>Dyadic</b></td>
<td>Caregiver–child connectedness</td>
</tr>
</tbody>
</table>

Codes are scored on a 4-point scale (0-3), reflecting the frequency, intensity and duration of observed behaviors across the paradigm, with higher scores indicating higher levels of observed behavior. See [Edwards et al. (2024)](https://doi.org/10.1016/j.dcn.2024.101422) for additional details on the ERICA paradigm and adaptation for HBCD.

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
<p style="color: red;">PLACEHOLDER - should anything be added or moved here from instrument details above?</p>
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
<p>Coders rate each construct at the activity level on a 4-point scale (None = 0, Low = 1, Medium = 2, High = 3). Activity-level ratings are then averaged across all activities to generate a continuous global score, ranging from 0-3, with higher scores reflecting higher levels of observed behavior.</p>

<p>Modifiers (-1, +1, and +2) may be used with three codes (<i>child irritability, caregiver responsive behavior, and dyadic connectedness</i>) to capture important qualitative distinctions. For example, for child irritability, a <b>+1</b> is added at the activity level when a child is highly irritable throughout an entire activity, with no recovery or re-engagement and a <b>+2</b> is added if a child becomes intensely dysregulated during an activity (e.g., intense crying with breath holding, gagging, other indications of intense dysregulation). When used, modifiers are included in the sum for the global scores.</p>

<p>Videos are coded and global scores generated as long as 3 out of the 5 ERICA activities are completed. If less than 3 activities are completed, the video is not coded and scores are not generated.</p>
</div>

## References
<div class="references"> 
<p>Krogh-Jespersen, S., MacNeill, L. A., Anderson, E. L., Stroup, H. E., Harriott, E. M., Gut, E., Blum, A., Fareedi, E., Fredian, K. M., Wert, S. L., Wakschlag, L. S., & Norton, E. S. (2021). Disruption leads to methodological and analytic innovation in developmental sciences: Recommendations for remote administration and dealing with messy data. <i>Frontiers in Psychology</i>, 12, 732312. <a href="https://doi.org/10.3389/fpsyg.2021.732312">https://doi.org/10.3389/fpsyg.2021.732312</a></p>
<p>Edwards, R. C., Planalp, E. M., Bosquet Enlow, M., Akshoomoff, N., Bodison, S. C., Brennan, M. B., Ciciolla, L., Eiden, R. D., Fillipi, C. A., Gustafsson, H. C., McKelvey, L. M., Morris, A. S., Peralta-Carcelén, M., Poehlmann, J., Wakschlag, L. S., Wilson, S., & HBCD Child Behavior and Caregiver-Child Interactions Workgroup. (2024). Capturing the complexity of child behavior and caregiver-child interactions in the HEALthy Brain and Child Development (HBCD) Study using a rigorous and equitable approach. <i>Developmental Cognitive Neuroscience</i>, 69(101422), 101422.<a href="https://doi.org/10.1016/j.dcn.2024.101422">https://doi.org/10.1016/j.dcn.2024.101422</a></p>
</div>
