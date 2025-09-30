<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION TO BE ADDED FOR R2.0: add additional versions for later visits to this same page</i></p>

# Demographics Child

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
<tr>
  <th style="width: 25%;"><i class="fa-solid fa-maximize"></i> Instrument</th>
  <th style="width: 15%;"><i class="fa-solid fa-clone"></i> Version</th>
  <th style="width: 25%;"><i class="fa-solid fa-tape"></i> Construct</th>
  <th style="width: 25%;"><i class="fa fa-table"></i> Table Name</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="2">HBCD Child Demographics</td>
  <td><strong>V4</strong></td>
  <td>Demographics (Child Visit 4)</td>
  <td><code>sed_bm_demo_child</code></td>
</tr>
<tr>
  <td><strong>V6</strong></td>
  <td>Demographics (Child Visit 6)</td>
  <td><code></code>ADD</td>
</tr>
</tbody>
</table>

<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Responsible Use Warning</i></span>
  <a class="anchor-link" href="#alert" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p>When using HBCD data, all data users must agree to responsible use as described in the DUC. When conceptualizing studies, analyzing data, and communicating findings from studies that use variables such as race, ethnicity, country of origin, and socioeconomic data, it is critical to consider strategies to avoid stigmatization of any groups and perpetuating harmful biases.</p> 
<p>Race and ethnicity are collected as a part of the HBCD protocol to reflect social experiences (i.e., representing social constructs), and should not be conceptualized as biological, natural, intrinsic, or fixed categories of people. In addition, researchers sometimes use race and/or ethnicity variables as proxies for unmeasured social experiences or environmental exposures. HBCD measures a wide variety of social experiences and environmental exposures. In analyzing HBCD data, race/ethnicity should not be used as a proxy for measured variables.</p>
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
<p><b>Participant-Reported Challenges</b><br>
Some participants reported challenges in answering certain questions, such as those related to race and ethnicity (e.g. options did not capture how they choose to identify their child).</p> 
<p><b>Withheld Variables/Variable Data With Small Cell Sizes</b><br>
<i style="color: red;">[INTERNAL NOTE from Natalie: this may need to be updated. There is an ongoing discussion re: a principled approached to deciding if we will withhold small cell sizes or release all and rely on the DUC. I can update you as soon as I know more]</i><br>
Some variables with small cell sizes were withheld from the data release to minimize the risk of disclosing identifying information. In addition, there are some variables that do not contain any data in the current data release (e.g., household roster response options allowed for more household members than were reported by the respondents who completed V04 or V06  to date). These variables are currently being retained, as their relevance may change as data collection proceeds.</p> 
<p><b>Branching Logic</b><br>
There are several items with branching logic; please consult the following resources for each questionnaire to see question flow and data dictionaries for information on skip patterns. Topics with branching logic include <a href="../images/household-relationships.png" target="_blank">Household Roster</a> and Child Custody/Guardianship (see <a href="../images/child-custody-branching-logic.png" target="_blank">items 15 and 16</a>). See <a href="../demo-ch-table" target="_blank">Child Demographics Branching Logic</a> for full branching logic details.</p>
</div>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>Yes</td></tr>
<tr><td><b>Respondent</b></td>
<td>Primary Caregiver reporting on Child</td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">HBCD Study Staff, in person</td></tr>
<tr><td><b>Visits</b></td>
<td>V04, V06</td></tr>
<tr><td><b>Completion Time</b></td>
<td>10 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;">Data dashboard was monitored for variable missingness, possible coding errors, scoring verification when needed, and data consistency - high missingness was noted for income, although this is in line with expectations.</td></tr>
</tbody>
</table>

## Instrument Details

Demographic information is crucial for understanding the child’s environment and identifying how social, structural, and economic factors influence development over time in a longitudinal study of child development. **Beginning at Visit 4, there is a child demographic form** that collects information about the child’s background and household environment. It includes questions on the child’s sex at birth, race and ethnicity (with multiple selectable categories to capture diverse identities), and how others classify the child’s race or ethnicity. 

The form also documents the respondent’s relationship to the child, legal guardianship status, and whether the respondent lives with the child, including the number of days per month in shared residence. Additional sections capture detailed household composition, such as the number of adults and children, and request a table listing all individuals who live with the child at least two nights per week, including their age and sex. Additionally, the child form requires the respondent to report the total household income for the past year (note: if the child resides in more than one household, they are asked to provide the average of the household incomes). These data are designed to support a nuanced analysis of the child’s social and family context within the study. See [Cioffredi et al. 2024](https://doi.org/10.1016/j.dcn.2024.101429) for a detailed description of the HBCD Demographics survey.

Also see [Basic Demographics](../demo/basicdemo.md), which includes variables derived from the HBCD Demographics instruments and data collected during study enrolment/screening.

<div id="demo-tables" class="table-banner" onclick="toggleCollapse(this)">
 <span class="emoji"><i class="fa fa-magnifying-glass"></i></span>
  <span class="text-with-link">
  <span class="text">Sources for Child Demographic Questions</span>
  <a class="anchor-link" href="#demo-tables" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<br>
<strong>&nbsp;&nbsp;Table 1. Citations for Major Topics in Child Demographics</strong>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
    <tr>
    <th style="width: 30%;">Construct</th>
    <th style="width: 30%;">Source</th>
    <th style="width: 30%;">Citations</th>
    </tr>
</thead>
    <tbody>
    <tr>
      <td>Household Roster</td>
      <td>Environmental Influences on Child Health Outcomes (<a href="https://echochildren.org/">ECHO</a>)</td>
      <td>None available</td>
    </tr>
    <tr>
      <td>Race/Ethnicity</td>
      <td>Office of Management & Budget (OMB)</td>
      <td><a href="https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards">Federal Register 2023</a></td>
    </tr>
    <tr>
      <td>Others Describe Your Child</td>
      <td><span class="tooltip">BRFSS<span class="tooltiptext">Behavioral Risk Factor Surveillance System</span></span></td>
      <td>Jones et al. 2008</td>
    </tr>
    <tr>
      <td>Annual Household Income</td>
      <td><span class="tooltip">ABCD<span class="tooltiptext">Adolescent Brain Child Development Study</span></span></td>
      <td>Barch et al. 2017</td>
    </tr>
  </tbody>  
  </table>
</div>

## References

<div class="references">
  <p>Barch, D. M., Albaugh, M. D., Avenevoli, S., Chang, L., Clark, D. B., Glantz, M. D., Hudziak, J. J., Jernigan, T. L., Tapert, S. F., Yurgelun-Todd, D., Alia-Klein, N., Potter, A. S., Paulus, M. P., Prouty, D., Zucker, R. A., & Sher, K. J. (2018). Demographic, physical and mental health assessments in the adolescent brain and cognitive development study: Rationale and description. <em>Developmental Cognitive Neuroscience</em>, 32, 55–66. <a href="https://doi.org/10.1016/j.dcn.2017.10.010" target="_blank">https://doi.org/10.1016/j.dcn.2017.10.010</a></p>
  <p>Cioffredi, L.-A., Yerby, L. G., Burris, H. H., Cole, K. M., Engel, S. M., Murray, T. M., Slopen, N., Volk, H. E., Acheson, A., & HBCD Social and Environmental Determinants Working Group. (2024). Assessing prenatal and early childhood social and environmental determinants of health in the HEALthy Brain and Child Development Study (HBCD). <em>Developmental Cognitive Neuroscience</em>, 69(101429), 101429. <a href="https://doi.org/10.1016/j.dcn.2024.101429" target="_blank">https://doi.org/10.1016/j.dcn.2024.101429</a></p>
  <p>Federal Register. (2023, January 27). Initial Proposals For Updating OMB’s Race and Ethnicity Statistical Standards (<a href="https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards" target="_blank">Document No. 2023-01635</a>). 88 FR 5375-5384.</p>
  <p>Jones, C. P., Truman, B. I., Elam-Evans, L. D., Jones, C. A., Jones, C. Y., Jiles, R., Rumisha, S. F., & Perry, G. S. (2008). Using “socially assigned race” to probe white advantages in health status. <em>Ethnicity & Disease</em>, 18(4), 496–504. <a href="https://www.ncbi.nlm.nih.gov/pubmed/19157256" target="_blank">https://www.ncbi.nlm.nih.gov/pubmed/19157256</a></p>
</div>
<br>


