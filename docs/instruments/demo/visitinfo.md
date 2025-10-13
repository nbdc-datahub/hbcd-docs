
# Visit Information

<div class="info-block">
  <div class="info-row">
    <div class="info-label"><i class="fa fa-table"></i> Table Name:</div>
    <div class="info-value"><code>par_visit_data</code></div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-tape"></i> Construct:</div>
    <div class="info-value">Derived Visit Information</div>
  </div>
</div>

---------------------------------------------

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">This data has known issues - <a href="../../../changelog/knownissues/#visit-information-par_visit_data" target="_blank">see details</a>.</span>
</div>
<p></p>

## Details

Visit information contains all participant visit data, including:

#### General Visit Information
 - Label, Stage, Date, Project, and Site
 - If the visit was missed and reason 
 - Withdrawal information (if the participant withdrew from the study, the reason, and date)
 - Protocol violation information (if there was a protocol exception and the date)

#### Substance Use Flags

Visit information also includes **substance use flags**, which are single summary variables that indicate substance use status (yes/no) based on any positive reports from the following instruments:

 - The Timeline Follow Back (<a href="../../pregexp/su/tlfb" target="_blank">TLFB</a>) (self-reported use)
 - <a href="../../pregexp/pex" target="_blank">Health V2- Infancy</a> when options 1 (*Neonatal Opioid Withdrawal Syndrome*) and/or 5 (*Fetal Alcohol Syndrome*) were selected for field `007` (self-reported use)
 - <a href="../../biospec/urine" target="_blank">USDTL urine toxicology results</a> (<i>note: <a href="../../biospec/nails" target="_blank">Nail toxicology results</a> were not used in the creation of the substance use flags</i>)
 

#### Cohort & Caregiver Types

**Cohort** information includes cohort subtype and caregiver type for each participant. Possible values include:

 - HBCD Main Child - Postnatal Recruitment
 - HBCD Main Child - Type {*A-F*}
 - HBCD Multiple Birth - {*Main Child | Postnatal Recruitment | Sibling*}
 - HBCD Multiple Birth - Type {*A-F*}

<div id="cg-types" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Caregiver Type A-F Definitions</span>
  <a class="anchor-link" href="#cg-types" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
    <tr>
        <td>Type A</td>
        <td>Temporary Alternative Caregiver</td>
    </tr>
    <tr>
        <td>Type B</td>
        <td style="word-wrap: break-word; white-space: normal;">Change in Primary Caregiver (Placement Only) Without Change in Legal Custody (But Birth Parent Unable to Complete Visit)</td>
    </tr>
    <tr>
        <td>Type C</td>
        <td>Change in Joint Custody</td>
    </tr>
    <tr>
        <td>Type D</td>
        <td style="word-wrap: break-word; white-space: normal;">Child Removed From Birth Parent and Placed in Foster Care (Change in Placement)</td>
    </tr>
    <tr><td>Type E</td><td>Change in Legal Custody and Placement (e.g. adoption)</td>
    </tr>
    <tr><td>Type F</td><td>Original Consented Parent</td>
    </tr>            
</tbody>
</table>
</div>

<br>