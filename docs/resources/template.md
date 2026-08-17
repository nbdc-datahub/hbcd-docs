# [Instrument name]

<table class="table-no-vertical-lines readme-intro">
<tbody>
<tr><td>Name</td><td>Full name of instrument with acronyms spelled out</td></tr>
<tr><td>Table Name</td><td> Table name in Lasso</td></tr>
<tr><td>Construct</td><td>The construct(s) that the measure assesses</td></tr>
<tr><td>Study Visits</td><td>e.g. V01, V03, V05</td></tr>
<tr><td>Type</td><td>e.g. Remote Questionnaire (Parent on Child; 4-8 min)</td></tr>
<td><b>Quality Control</b></td>
<td>Detail the QC procedures for this measure- scoring algorithm verification, data consistency checks, etc. May be provided as a list.</td></tr>
</tbody>
</table>


<div id="data-alert" class="banner alert" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fas fa-exclamation-circle"></i>
</span>
<span class="text-with-link">
    <span class="text">Responsible Use Warning [IF APPLICABLE]</span>
    <a class="anchor-link" href="#data-alert" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content" style="background-color: #f9f2f3;">
<p>The purpose of this warning is to offer guidance for research design, data interpretation, and communication of findings, including conceptual information. These warnings also include information on stigma and stigmatizing language related to some variables, or information on the manner in which race variables were conceptualized and collected for this study.</p>
</div>

<div id="data-warning" class="banner data-warning" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fas fa-exclamation-triangle"></i>
</span>
<span class="text-with-link">
    <span class="text">Data Warning [IF APPLICABLE]</span>
    <a class="anchor-link" href="#data-warning" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content" style="background-color: #fcfaed;">
<p>Please provide any issue flagged by subject matter experts that are critical for users of this data. The purpose of this warning is to improve transparency and offer technical assistance by alerting the user to issues of data quality, providing information on how variables were constructed, providing instructions on how to calculate or analyze specific variables, or providing code (if necessary).</p>
<p><b>Note that Data Warnings do not typically include descriptions of known issues and pending updates, as those are documented on a single page across instruments <a href="../../changelog/issues-updates/">here</a>.</b> The Data Warnings should focus more on technical advice that is less variable across releases.</p>
</div>
{{ issues_banner() }}

---

## Instrument Details

*Describe the instrument, including its purpose, the constructs it measures, and any relevant background information. Provide enough context for researchers unfamiliar with the instrument to understand what it measures and why it was included in the study.*

*Note: HBCD data users should primarily rely on the data dictionary in Lasso/DEAP for comprehensive variable information. Avoid duplicating this information too much in the README, otherwise you run the risk of the README information falling out of sync and confusing users. That being said, use your best judgment and if you are unsure, err on the side of including more, not less, information in the documentation.* 

*Remember to write for an external research audience. Avoid references to HBCD-specific workflows, internal documentation, data management systems, or study operations that would not help end users understand or use the data.*

<div id="hbcd_mods" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
     <i class="fa fa-gear"></i>
</span>
<span class="text-with-link">
    <span class="text">HBCD Modifications [IF APPLICABLE]</span>
    <a class="anchor-link" href="#hbcd_mods" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><b>This section describes how the HBCD version differs from the original instrument.</b> If measure was NOT previously published or validated, please skip this section.</p>
<p>Please describe any changes made to response options, item wording, and/or administration procedures, including:</p>
<ul>
<li>Was the language altered for use of gender-neutral terms? </li>
<li>Was the language altered from ‘parent’ to caregiver or alternate? </li>
<li>Do any modifications made for HBCD impact data analyses or interpretation of results? If yes, please describe</li>
<li>Does the Workgroup recommend measure changes be noted in future publications? If yes, are there particular details you would want users to be sure to mention?</li>
<li>Other?</i>

</div>

<div id="scoring" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fa fa-calculator"></i>
</span>
<span class="text-with-link">
    <span class="text">Scoring Procedures [IF APPLICABLE]</span>
    <a class="anchor-link" href="#scoring" title="Copy link">
        <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>
This section describes how instrument responses are converted into scores and how those scores should be interpreted. Provide enough detail for a user to reproduce all calculated and summary scores from the item-level data.<br>
Include scoring algorithms, formulas, reverse-coding information, lookup tables, normative data, and other supporting materials used to calculate or interpret scores. When these materials are publicly available online, provide a link to the source. If they are not available online, a PDF may be provided for inclusion on the website (if not proprietary).
</p>
<h5>General Example</h5>
<p>
The {INSTRUMENT NAME} includes 10 items, each rated on a 5-point scale from <i>1 = Never</i> to <i>5 = Always</i>. The total score is calculated as the sum of the numerical responses to all 10 items and has a possible range of 10–50 when all items are completed. Higher scores indicate a higher level of {CONSTRUCT BEING MEASURED}.
</p>
<p>
Responses of “Decline to Answer” are treated as missing and are not included in the score calculation. A total score is calculated only when at least 6 of the 10 items have valid responses. If fewer than 6 items have valid responses, the total score is set to missing. When 6-9 items have valid responses, a prorated total score is calculated as:
</p>
<p>
<i><b>Prorated score</b> = (Sum of answered items ÷ Number of items answered) × 10</i>
</p>
</div>

---

## Resources

[List key resources related to the instrument, such as manuals, scoring guides, or relevant publications. Include links to these resources if available]

---

<div id="references" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fa-solid fa-book-open"></i>
</span>
<span class="text-with-link">
    <span class="text">References</span>
    <a class="anchor-link" href="#references" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<div class="references">
<p>APA format, listed alphabetically, for all resources referenced on this page. Be sure to include DOI link. For example:</p>
<p>
Marchman, V. A., & Dale, P. S. (2023). The MacArthur-Bates Communicative Development Inventories: Updates from the CDI advisory board. Frontiers in Psychology, 14, 1170303.<a href="https://doi.org/10.3389/fpsyg.2023.1170303">https://doi.org/10.3389/fpsyg.2023.1170303</a>
</p>
</div>
</div>



 