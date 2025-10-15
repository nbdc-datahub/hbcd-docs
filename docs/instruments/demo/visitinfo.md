
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
<table class="table-no-vertical-lines" style="
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
  border: 2px solid #f0b429;
  border-radius: 8px;
  overflow: hidden;
  word-wrap: break-word;
  white-space: normal;
  margin-top: 1em;
">
  <thead>
    <tr style="background-color: #fff3e0;">
      <th colspan="2" style="
        text-align: left;
        font-size: 1.1em;
        padding: 4px;
        border-bottom: 2px solid #f0b429;
        word-wrap: break-word;
        white-space: normal;
      ">
        <i class="fas fa-bug" style="margin-right: 6px; color: orange;"></i>
        <b style="color: #6e6256ff;">KNOWN ISSUES – Expected Fix Release 2.0</b>
      </th>
    </tr>
    <tr style="background-color: #fdfaf5;">
      <th style="width: 25%; text-align: left; padding: 8px; color: #6e6256ff;">VARIABLE/FIELD</th>
      <th style="text-align: left; padding: 8px; color: #6e6256ff;">KNOWN ISSUE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="vertical-align: top; padding: 8px; word-wrap: break-word; white-space: normal;">
        <b>Withdrawal Date<br><code>participant_withdrawal_date</code></b>
      </td>
      <td style="vertical-align: top; padding: 8px; word-wrap: break-word; white-space: normal;">
        Participants who did <b>not</b> withdraw from the study (<code>participant_withdrawal</code> = “no”) are assigned a sentinel withdrawal date of <code>12/26/1999</code>. 
        These values will be updated to <code>null</code> for clarity.
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top; padding: 8px; word-wrap: break-word; white-space: normal;">
        <b>Biospec-Derived SU Flags<br><code>su_flag_bio_*</code></b>
      </td>
      <td style="vertical-align: top; padding: 8px; word-wrap: break-word; white-space: normal;">
        Erroneous inclusion of Biospec substance use flags 
        <a href="../../instruments/demo/visitinfo/#substance-use-flags">derived from USDTL urine toxicology</a> 
        for V02 (urine samples not collected at V02) — will be removed to fix.
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top; padding: 8px; word-wrap: break-word; white-space: normal;">
        <b>TLFB-Derived SU Flags<br><code>su_flag_tlfb_*</code></b>
      </td>
      <td style="vertical-align: top; padding: 8px; word-wrap: break-word; white-space: normal;">
        The TLFB substance use flags for participants who do not have a Visit 2 have incorrect values of “no;” these will be corrected to “null.”
      </td>
    </tr>
  </tbody>
</table>
</div>


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
