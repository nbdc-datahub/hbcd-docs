
## Cohort & Caregiver Types
**Cohort** information (<code>par_visit_data_cohort</code>) includes cohort subtypes and caregiver type for each participant:

- **Cohort subtypes**: *Main Child* and *Multiple Birth*, with additional labeling for *Postnatal Recruits* (*PNR*) and Multiple Birth siblings (*Main Child* vs. *Sibling*)
- **Caregiver types**: coded as *Type A-F* - see [Caregiver Types](#cg-types) below for details

<div id="cohorts" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Cohort Types (<i>Complete List</i>)</span>
  <a class="anchor-link" href="#cohorts" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<div style="display: flex; gap: 3rem; flex-wrap: wrap;">
  <table class="table-no-vertical-lines" style="flex: 1; min-width: 280px; border: none;">
  <thead style="border: none;"><tr style="border: none;"><th>Main Child Cohorts</th></tr></thead>
    <thead>
      <tr><th>Label</th><th>Value</th></tr>
    </thead>
    <tbody>
      <tr><td>HBCD Main Child</td><td>0</td></tr>
      <tr><td>HBCD Main Child - PNR</td><td>1</td></tr>
      <tr><td>HBCD Main Child - PNR - Split</td><td>2</td></tr>
      <tr><td>HBCD Main Child - Type A</td><td>3</td></tr>
      <tr><td>HBCD Main Child - Type B</td><td>4</td></tr>
      <tr><td>HBCD Main Child - Type C</td><td>5</td></tr>
      <tr><td>HBCD Main Child - Type D</td><td>6</td></tr>
      <tr><td>HBCD Main Child - Type E</td><td>7</td></tr>
    </tbody>
  </table>
  <table class="table-no-vertical-lines" style="flex: 1; min-width: 280px;">
  <thead style="border: none;"><tr><th>Multiple Birth Cohorts</th></tr></thead>
    <thead>
      <tr><th>Label</th><th>Value</th></tr>
    </thead>
    <tbody>
        <tr><td>HBCD Multiple Birth - Main Child</td><td>8</td></tr>
      <tr><td>HBCD Multiple Birth - PNR</td><td>9</td></tr>
      <tr><td>HBCD Multiple Birth - PNR - Sibling</td><td>10</td></tr>
      <tr><td>HBCD Multiple Birth - Sibling</td><td>11</td></tr>
      <tr><td>HBCD Multiple Birth - Type A</td><td>12</td></tr>
      <tr><td>HBCD Multiple Birth - Type B</td><td>13</td></tr>
      <tr><td>HBCD Multiple Birth - Type C</td><td>14</td></tr>
      <tr><td>HBCD Multiple Birth - Type D</td><td>15</td></tr>
      <tr><td>HBCD Multiple Birth - Type E</td><td>16</td></tr>
    </tbody>
  </table>
</div>
</div>

### Postnatal Recruits & Multiple Birth Participants

These cohort subtypes are defined below. Click the links to download participant lists for each, available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.

<table class="table-no-vertical-lines">
  <thead>
    <tr>
      <th>Cohort Subtype</th>
      <th>Description</th>
      <th>Download</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td>Multiple Birth</td>
    <td style="word-wrap: break-word; white-space: normal;">Siblings/twins enrolled in the study, categorized as <b>Main Child</b> and <b>Sibling</b>.</td>
    <td style="text-align: center;"><a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/multi_birth_participants-supplemental.csv"><i class="fa-solid fa-download"></i></a></td>
  </tr>
    <tr>
    <td>Postnatal Recruits (PNR)</td>
    <td style="word-wrap: break-word; white-space: normal;">Participants enrolled in the study after the child is born (complete a modified V01 and V02).</td>
    <td style="text-align: center;"><a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/PNR_participants-supplemental.csv"><i class="fa-solid fa-download"></i></a></td>
  </tr>
  </tbody>
  </table>

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text"><i>Note: Non-child-specific instrument fields are currently only populated for Main Child, and blank for Sibling</i></span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Certain fields are expected to be the same between siblings, such as caregiver/maternal instruments that aren't child-specific (e.g. <a href="../../SED/demo-cg/">Adult Demographics</a>). For twins/triplets, all <a href="../../agevariables/" target="_blank">age variables</a> will also be the same, including those computed with a jittered DOB.</p>
<p><strong>Currently, non-child-specific instrument data are only populated for the Main Child.</strong> Future release data will be updated to provide more complete information - see <a href="../../../changelog/pending/" target="_blank">Pending Updates</a> for details. In the meantime, users will need to source blank <strong>Sibling</strong> data fields from the corresponding Main Child data for non-child-specific instrument tables. Please refer to the participant list mapping Main Child to Sibling IDs provided above - <a href="#postnatal-recruits-multiple-birth-participants">above</a>.</p>
</div>

### Caregiver Types

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



<br>
<br><br><br><br>


#### Multiple Birth Participants - User Notes

<p>
<a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/
multi_birth_participants-supplemental.csv"><i class="fa-solid fa-download"></i> &nbsp; Download Multiple Birth Participants List</a> <i>(available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>)</i>
</p>

Multiple Birth participants (MBP) siblings/twins enrolled in the study, categorized as **Main Child** and **Sibling**.              
**Note that certain fields are expected to be the same between siblings**, such as caregiver/maternal instruments that aren't child-specific (e.g. [Adult Demographics](../SED/demo-cg.md)). For twins/triplets, all <a href="../../agevariables/" target="_blank">age variables</a> will also be the same, including those computed with a jittered DOB.

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text"><i>Note: Non-child-specific instrument fields are currently only populated for Main Child, and blank for Sibling</i></span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p><strong>Currently, non-child-specific instrument data, which should be the same across siblings, are only populated for the Main Child.</strong> Future release data will be updated to provide more complete information - see <a href="../../../changelog/pending/" target="_blank">Pending Updates</a> for details. In the meantime, users will need to source blank <strong>Sibling</strong> data fields from the corresponding Main Child data for non-child-specific instrument tables. Please refer to the participant list mapping Main Child to Sibling IDs - <a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/multi_birth_participants-supplemental.csv">click to download</a>.</p>
</div>
<p></p>




<br>
<br>
<br>


<i> <i style="color: #ffa500;" class="fas fa-exclamation-triangle"></i> See <a href="../../../changelog/knownissues/#pregnancy-exposure-including-substance-use" target="_blank">Known Issues &gt; TLFB</a> for the TLFB, reported on the wrong weeks for PNR participants.</i>

## EXTRA


##### <i style="color: #ffa500;" class="fas fa-exclamation-triangle"></i> Blank Fields for Sibling Cohorts

**Currently, non-child-specific instrument data, which should be the same across siblings, are only populated for the Main Child.** Future release data will be updated to provide more complete information - see <a href="../../../changelog/pending/" target="_blank">Pending Updates</a> for details. In the meantime, users will need to source blank **Sibling** data fields from the corresponding Main Child data for non-child-specific instrument tables. Please refer to the participant list mapping Main Child to Sibling IDs provided in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a> (*only accessible to DUC-authorized users*)</i>. 

<a href="https://hbcd-docs-private.lassoinformatics.com/participant_lists/
multi_birth_participants-supplemental.csv"><i class="fa-solid fa-download"></i> &nbsp; Download participant list</a> 



 

<div id="warning-PNR" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Postnatal Recruitment (PNR) Cohorts - Known Issue Regarding the TLFB</span>
  <a class="anchor-link" href="#warning-PNR" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>For <b>Postnatal Recruits</b>, the TLFB instrument was reported on the wrong weeks - see <a href="../../../changelog/knownissues/#pregnancy-exposure-including-substance-use" target="_blank">Known Issue &gt; TLFB</a> for details.</p>
</div>
<p></p>



