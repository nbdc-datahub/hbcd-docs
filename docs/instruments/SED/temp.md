# Demographics (Adult)

{{ warning_banner_macro() }}
<div class="collapsible-content">

<p><b>Branching Logic</b><br>
There are several items that Alternate Caregivers receive with branching logic; please consult the following resources for each questionnaire to see question flow and data dictionaries for information on skip patterns. Topics with branching logic include: 
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><strong>Nativity</strong></td>
<td><a href="https://www.phenxtoolkit.org/protocols/view/10201">PhenX Toolkit</a></td></tr>
<tr><td><strong>Jobs / work environment</strong></td>
<td>(1) <a href="https://doi.org/10.1093/occmed/kqz094">Zachek et al., 2019</a> <i>(Original instrument for the Workplace Hazard)</i><br>
(2) <a href="https://www.phenxtoolkit.org/protocols/view/60501">PhenX Occupation/Occupational History Toolkit</a>
</td></tr>
<tr><td><strong>Items on other biological parent with opt-in responses</strong></td>
<td><a href="../images/other-parent.png" target="_blank"><i>Click to view</i></a></td></tr>
</tbody>
</table>
</div>

{{ issues_banner_macro() }}

## Instrument Details

Demographic information is crucial for understanding the child’s environment and identifying how social, structural, and economic factors influence development over time in a longitudinal study of child development. The **HBCD Study demographics survey at V01** was designed to gather comprehensive information on socioeconomic status and various demographic factors. Its primary purpose is to capture data on race, ethnicity, nativity, income, education, and occupation, as well as relationship status, primary residence, and household composition of the parent carrying the child, and some basic information on the other biological parent. Please see [Cioffredi et al. 2024](https://doi.org/10.1016/j.dcn.2024.101429) for a detailed description of the baseline HBCD Demographics survey.

**At subsequent times of assessment (i.e., V04+)**, a selected set of variables that can change over time were re-administered, and several new questions were added (i.e., disability status and access to reliable transportation). Of note, from V04 onward, there is a separate <a href="../demo-ch" target="_blank">Child Demographics</a> form that includes child-focused information including child race and ethnicity, relationship to the child/custody, household roster, type of residence, and household income. In addition, from V04 onward, data on caregiver work/employment characteristics are in a separate form (see <a href="../current-employment" target="_blank">Current Employment</a>).

{{ mods_banner_macro() }}
<div class="collapsible-content">
<p>Below are alterations made to demographic constructs to tailor it to the HBCD Study. The modifications were made to reduce bias and capture a more inclusive and accurate breadth of demographic information, e.g., by correcting for embedded assumptions of heteronormative nuclear-family structures.</p>
  <ul>
    <li><b>Marital & Relationship Status</b> alterations to reduce heteronormative bias:
      <ul>
      <li>Combine "Divorced/Separated"</li>
      <li>"Never Married" replaced by "Single"</li>
      <li>"Member of an Unmarried Couple" replaced by "Partnered"</li>
      </ul>
    </li>
    <li><b>Primary Residence</b> destigmatization of living situations: Inclusion of options for individuals in treatment facilities, shelters, or unhoused.</li>
    <li><b>Household Roster</b> alteration to reduce nuclear family assumptions: expansion of family/caregiver roles</li>
    </li>
    <li><b>Race/Ethnicity</b> and <b>Others Describe You</b>: Inclusion of racial and ethnic categories aligned with proposed OMB recommendations using a combined race and ethnicity variable with 7 response options (<a href="https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards 
    ">Federal Register 2023</a>). Participant can select all that apply.</li>
    <li><b>Income</b>: Alteration of household income brackets.</li>
  </ul>
</div>

<div id="demo-tables" class="banner" onclick="toggleCollapse(this)">
 <span class="emoji"><i class="fa fa-magnifying-glass"></i></span>
  <span class="text-with-link">
  <span class="text">Sources for Demographic Protocols & Modifications</span>
  <a class="anchor-link" href="#demo-tables" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><b>Table 1. Demographics of Birth Parent</b></p>
<table class="compact-table-no-vertical-lines">
<thead>
    <tr>
    <th>Construct</th>
    <th>Source</th>
    <th>Citations</th>
    </tr>
</thead>
    <tbody>
    <tr>
    <td>Marital and Relationship Status</td>
    <td><a href="https://www.phenxtoolkit.org/protocols/view/10903">PhenX</a></td>
    <td>Hamilton, et al. (2011)</td>
    </tr>
    <tr>
        <td>Sexual Orientation</td>
        <td><a href="https://www.phenxtoolkit.org/protocols/view/11701">PhenX</a></td>
        <td>Hamilton, et al. (2011)</td>
    </tr>
    <tr>
        <td>Primary Residence</td>
        <td>HBCD</td>
        <td>Cioffredi, et al. (2024)</td>
    </tr>
    <tr>
        <td>Years At Current Address</td>
        <td>HBCD</td>
        <td>Cioffredi, et al. (2024)</td>
    </tr>
    <tr>
        <td>Household Roster</td>
        <td>
      <span class="tooltip">
      <a href="https://echochildren.org/">ECHO</a>
      <span class="tooltiptext">Environmental Influences on Child Health Outcomes</span>
      </span>
    </td>
        <td>None available</td>
    </tr>
    <tr>
        <td>Birthplace and Heritage</td>
        <td><a href="https://www.phenxtoolkit.org/protocols/view/10201">PhenX</a></td>
        <td>Hamilton, et al. (2011)</td>
    </tr>
    <tr>
        <td>Years Living in the United States</td>
        <td><a href="https://www.phenxtoolkit.org/protocols/view/11201">PhenX</a></td>
        <td>Hamilton, et al. (2011)</td>
    </tr>
    <tr>
    <tr>
      <td>Race/Ethnicity</td>
      <td><span class="tooltip">OMB<span class="tooltiptext">Office of Management & Budget</span></span></td>
      <td><a href="https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards">Federal Register 2023</a></td>
    </tr>
    <tr>
      <td>Others Describe You</td>
      <td><span class="tooltip">BRFSS<span class="tooltiptext">Behavioral Risk Factor Surveillance System</span></span></td>
      <td>Jones et al. 2008</td>
    </tr>
    <tr>
        <td>Biological Parents Birthplace and Heritage</td>
        <td><a href="https://www.phenxtoolkit.org/protocols/view/10301">PhenX</a></td>
        <td>Hamilton, et al. (2011)</td>
    </tr>
    <tr>
      <td>Annual Household Income</td>
      <td><span class="tooltip">ABCD<span class="tooltiptext">Adolescent Brain Child Development Study</span></span></td>
      <td>Barch et al. 2017</td>
    </tr>
    <tr>
        <td>Educational Attainment</td>
        <td><a href="https://www.phenxtoolkit.org/protocols/view/11002">PhenX</a></td>
        <td>Hamilton, et al. (2011)</td>
    </tr>
    <tr>
        <td>Active-Duty Military</td>
        <td>HBCD</td>
        <td>Cioffredi, et al. (2024)</td>
    </tr>
    <tr>
        <td>Currently Work for Pay</td>
    <td>
      <span class="tooltip">BFY<span class="tooltiptext">Baby's First Years</span></span>
    </td>
        <td>Year 1 Protocol - G35, Mwork</td>
    </tr>
    <tr>
        <td>Total Hours of Work In Last Week</td>
        <td>HBCD</td>
        <td>Cioffredi, et al. (2024)</td>
    </tr>
    <tr>
    <td>Jobs During Pregnancy -<br>
      <b>{</b> All Jobs - Work 35+ Hr/Wk; At Least 1 Job At 20 Hr/Wk for 1 Month;<br>
      Type of Work; Job Start/Stop Dates; Typical Hours/Week <b>}</b>
    </td>
        <td>HBCD</td>
        <td>Cioffredi, et al. (2024)</td>
    </tr>
    <tr>
        <td>Jobs During Pregnancy - Shift Schedule</td>
    <td>
      <span class="tooltip">BFY
      <span class="tooltiptext">Baby's First Years</span>
      </span>
    </td>
        <td>Year 1 Protocol - G39, SchedMain</td>
    </tr>
    <tr>
      <td>Disability</td>
      <td><span class="tooltip">ACS<span class="tooltiptext">US Census Bureau's American Community Survey</span></span> Disability Questions</td>
      <td><a href="https://www.census.gov/topics/health/disability/guidance/data-collection-acs.html">US Census Bureau 2021</a></td>
    </tr>
    <tr>
      <td>Transportation</td>
      <td><span class="tooltip">CMS<span class="tooltiptext">Centers for Medicare & Medicaid Services</span></span></td>
      <td><a href="https://www.cms.gov/priorities/innovation/files/worksheets/ahcm-screeningtool.pdf"><span class="tooltip">AHC HRSN<span class="tooltiptext">Accountable Health Communities Health-Related Social Needs</span></span> Screening Tool</a></td>
    </tr>
  </tbody>
  </table>
<p><b>Table 2. Demographics of Other Biological Parent <i>(Only collected at V01 baseline interview)</i></b></p>
<table class="compact-table-no-vertical-lines">
<thead>
    <tr>
    <th>Construct</th>
    <th>Source</th>
    <th>Citations</th>
    </tr>
</thead>
    <tbody>
<tr>
    <td>Age</td>
    <td>HBCD</td>
    <td>Cioffredi, et al. (2024)</td>
</tr>
<tr>
  <td>Race/Ethnicity</td>
  <td><span class="tooltip">OMB<span class="tooltiptext">Office of Management & Budget</span></span></td>
  <td><a href="https://www.federalregister.gov/documents/2023/01/27/2023-01635/initial-proposals-for-updating-ombs-race-and-ethnicity-statistical-standards">Federal Register 2023</a></td>
</tr>
<tr>
    <td>Birthplace and Heritage</td>
    <td><a href="https://www.phenxtoolkit.org/protocols/view/10201">PhenX</a></td>
    <td>Hamilton, et al. (2011)</td>
</tr>
<tr>
    <td>Years Living in The United States</td>
    <td><a href="https://www.phenxtoolkit.org/protocols/view/11201">PhenX</a></td>
    <td>Hamilton, et al. (2011)</td>
</tr>
<tr>
    <td>Biological Parents Country of Origin</td>
    <td><a href="https://www.phenxtoolkit.org/protocols/view/10301">PhenX</a></td>
    <td>Hamilton, et al. (2011)</td>
</tr>
<tr>
    <td>Education</td>
    <td><a href="https://www.phenxtoolkit.org/protocols/view/11002">PhenX</a></td>
    <td>Hamilton, et al. (2011)</td>
</tr>
<tr>
     <td>Job At Conception - <b>{</b> Work for Pay; Type of Work; Full Time/ Part Time <b>}</b></td>
    <td>HBCD</td>
    <td>Cioffredi, et al. (2024)</td>
</tr>
<tr>
    <td>Active-Duty Military</td>
    <td>HBCD</td>
    <td>Cioffredi, et al. (2024)</td>
</tr>
<tr>
    <td>Help Out Financially</td>
    <td>HBCD</td>
    <td>Cioffredi, et al. (2024)</td>
</tr>
</tbody>
</table>
</div>
