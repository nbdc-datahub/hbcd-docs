# Visit Information
      
**Table Name**: `par_visit_data`       

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
<p>Please note that participants who did not withdraw from the study (and so have a value of "no" for <code>par_visit_data_participant_withdrawal</code>) have a sentinel value of <code>12/26/1999</code>, <i>meaning no withdrawal</i>, for participant withdrawal date (<code>par_visit_data_participant_withdrawal_date</code>).</p>
</div>

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">This data has known issues - <a href="../../../changelog/knownissues/#visit-information" target="_blank">see details</a>.</span>
</div>
<p></p>

Visit information contains all participant visit data, including:

*   Label, Stage, Date, if the visit was missed, and the reason if visit was missed
*   Project, Cohort (see details below), and Site
*   Withdrawal information: if the participant withdrew from the study, the reason, and date
*   Protocol violation information: if there was a protocol exception and the date
*   Substance use flags raised by <a href="../../pregexp/su/tlfb" target="_blank">TLFB</a> (Self-reported use), <a href="../../biospec/urine" target="_blank">USDTL urine toxicology results</a>, and/or <a href="../../pregexp/pex" target="_blank">Health V2- Infancy</a> Field `007` when option 1 (*Neonatal Opioid Withdrawal Syndrome*) or 5 (*Fetal Alcohol Syndrome*) was selected

### Cohort & Caregiver Types

<p>Cohort types included in the data release are as follows, with each listed item indicating a specific subtype or Caregiver Type (e.g., "HBCD Main Child - Postnatal Recruitment"):</p>
<ul>
    <li><strong>HBCD Main Child -</strong> <em>Postnatal Recruitment</em>, <em>Type A-F</em></li>
    <li><strong>HBCD Multiple Birth -</strong> <em>Main Child</em>, <em>Postnatal Recruitment</em>, <em>Postnatal Recruitment - Sibling</em>, <em>Type A-F</em></li>
</ul>

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<caption>Caregiver Type A-F Definitions</caption>
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