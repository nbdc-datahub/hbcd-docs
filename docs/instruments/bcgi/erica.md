# ERICA

<div class="info-block">
  <div class="info-row">
    <div class="info-label"><i class="fa fa-table"></i> Table Name:</div>
    <div class="info-value"><code>mh_pa_erica</code></div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-maximize"></i> Full Name:</div>
    <div class="info-value">
      Early Regulation in Context Assessment (<i>ERICA-FCM</i>) 
    </div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-tape"></i> Construct:</div>
    <div class="info-value">Co-regulation, Child Regulation/Dysregulation, Parenting</div>
  </div>
</div>

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
</div>

----

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>Yes</td></tr>
<tr><td><b>Respondent</b></td>
<td>Primary Caregiver on Child</td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">HBCD Study staff in-person</td></tr>
<tr><td><b>Visits</b></td>
<td>V03, V04, V06</td></tr>
<tr><td><b>Completion Time</b></td>
<td></td></tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;"></td></tr>
</tbody>
</table>

---

## Instrument Details

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
</div>

---

## Scoring: ERICA Final Derived Fields

A new set of derived fields are created as the final repository for the score fields on the ERICA coding. These fields draw from the values in the two 'ERICA - Coding' forms, the  'ERICA - Codes' (`mh_cg_erica_3_9m`) and the 'ERICA - Codes - Reliability' (`mh_cg_erica_rel_3_9m`). This logic is initially adapted for the 3 to 9 Months forms, but should be applicable for any given timepoint where the ERICA is administered. 

A hierarchical logic is implemented such that the score values are extracted from the 'ERICA - Codes' form unless there are values available in the 'Reliability' form. Any values extracted for the derived score fields will need to have DDE and all conflicts resolved ahead of the values being passed onto the derived fields. Logic and other details below.

#### ERICA Forms

<table class="table-no-vertical-lines">
<thead><tr>
<th>Visit</th>
<th>ERICA Forms</th>
<th>Table Name</th>
</tr></thead>
<tbody>
<tr><td colspan="1" rowspan="2">V03 (3 to 9 Months)</td><td>ERICA Codes (3&ndash;9M)</td><td><code>mh_cg_erica_3_9m</code></td></tr>
<tr><td>ERICA Codes (3&ndash;9M) &ndash; Reliability</td><td><code>mh_cg_erica_rel_3_9m</code></td></tr>
<tr><td colspan="1" rowspan="2">V06 (15 to 30 Months)</td><td>ERICA Codes (15&ndash;30M)</td><td><code>mh_cg_erica_15_30m</code></td></tr>
<tr><td>ERICA Codes (15&ndash;30M) &ndash; Reliability</td><td><code>mh_cg_erica_rel_15_30m</code></td></tr>
<tr><td colspan="1" rowspan="2">V10 (46 to 60 Months)</td><td>ERICA Codes (46&ndash;60M)</td><td><code>mh_cg_erica_46_60m</code></td></tr>
<tr><td>ERICA Codes (46&ndash;60M) &ndash; Reliability</td><td><code>mh_cg_erica_rel_46_60m</code></td></tr>
</tbody>
</table>

#### Derived Fieldnames
Derived fieldnames follow the same fieldname structure as the instruments, with an added `final_` suffix in the instrument section and pushed as backend fields under a new DQT category. List of derived fields as per attached spreadsheet for V03 fields.

#### DQT Category

<table class="table-no-vertical-lines">
<tbody>
<tr><td>ERICA Codes - 3 to 9 Months - Final - Derived</td><td><code>mh_cg_erica_3_9m_final</code></td></tr>
<tr><td>ERICA Codes - 15 to 30 Months - Final - Derived</td><td><code>mh_cg_erica_15_30m_final</code></td></tr>
<tr><td>ERICA Codes - 46 to 60 Months - Final - Derived</td><td><code>mh_cg_erica_46_60m_final</code></td></tr>
</tbody>
</table>

### Script Logic to Derive Fields

#### 'Reliability' form check:
**For any given instance, the logic checks first for data in the 'Reliability' form.**

* If data is available, as denoted by the instrument's 'Administration' status set to '*All*' or '*Partial*' and 'Data Entry' set to '*Complete*', as well as the DDE set to '*Complete/All*' or '*Complete/Partial*', then data can be transferred for fields with no conflict reported. For any given field, if there is a conflict yet to be resolved, the data for the field is not derived and a note is pushed saying "*Conflict noted and pending to be resolved*".  
* If initial data entry form is '*Complete/All*' or '*Complete/Partial*' and DDE form is '*In progress*' or not started ('Data Entry' is 'Null'), a note should be added to all fields saying "*Data in 'Reliability' form but no DDE done*".  
* If the 'Reliability' instrument's 'Administration' status is 'None' or 'Null', or the 'Data Entry' set to 'In progress', then no data from the 'Reliability' form is derived. 

Next, the script checks on the 'Codes' form, where a similar logic would ensue.

#### Check 'Codes' Form:

* If the original 'Codes' form's 'Administration' status is set to '*All*' or '*Partial*' and 'Data Entry' set to '*Complete*', as well as the DDE set to '*Complete/All'* or '*Complete/Partial*', then data can be transferred. For any given field, if there is a conflict yet to be resolved, the data is not derived and a note pushed saying "*Conflict noted and pending to be resolved*".  
* If initial data entry form is '*Complete/All*' or '*Complete/Partial*' and DDE form is '*In progress*' or not started ('Data Entry' is 'Null'), a note is added to all fields saying "*Data in 'Codes' form but no DDE done*".

### Logic Tree

#### Reliability Checks

1. Check 'Administration' status of 'Reliability' form  
    * If 'None', jump to check 'Codes' form (Step 1)  
2. If 'All' or 'Partial', check 'Data Entry' status of 'Reliability' form  
    * If 'In progress' or 'Null' (not started), jump to check 'Codes' form (Step 1)  
3. If 'Complete', check DDE 'Administration' status  
    * If 'None' or 'Null' (not started), add note "Data in 'Reliability' form but no DDE done" to all fields  
    * Process stops  
4. If 'All' or 'Partial', check DDE 'Data Entry' status  
    * If 'In progress, add note "Data in 'Reliability' form but no DDE done" to all fields  
    * Process stops  
5. If 'Complete', check conflicts per field  
    * Transfer data to derived fields for all fields with no conflicts  
    * For fields with conflicts, add note "Conflict noted and pending to be resolved"

#### Code Checks

1. Check 'Administration' status of 'Codes' form  
     * If 'None', stop process  
2. If 'All' or 'Partial', check 'Data Entry' status of 'Codes' form  
    * If 'In progress' or 'Null' (not started), stop process  
3. If 'Complete', check DDE 'Administration' status  
     * If 'None' or 'Null' (not started), add note "Data in 'Codes' form but no DDE done" to all fields  
     * Process stops  
4. If 'All' or 'Partial', check DDE 'Data Entry' status  
    * If 'In progress, add note "Data in 'Codes' form but no DDE done" to all fields  
     * Process stops  
5. If 'Complete', check conflicts per field  
     * Transfer data to derived fields for all fields with no conflicts  
     * For fields with conflicts, add note "Conflict noted and pending to be resolved"

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
<h2 id="scoring-erica-final-derived-fields">ERICA Final Derived Fields</h2>
<p>Final ERICA summary scores are derived fields populated from one of two forms: the <b>ERICA – Codes – Reliability</b> form when available; otherwise, values from the <b>ERICA – Codes</b> form are used. All DDE and data conflicts must be resolved before values are transferred to these derived fields. This additional logic and details are described below.</p>
<p><b>ERICA Forms</b></p>
<table class="table-no-vertical-lines">
<thead><tr>
<th>Visit</th>
<th>ERICA Form</th>
<th>Field Name</th>
</tr></thead>
<tbody>
<tr><td colspan="1" rowspan="2">V03 (3 to 9 Months)</td><td>ERICA Codes (3&ndash;9M)</td><td><code>mh_cg_erica_3_9m</code></td></tr>
<tr><td>ERICA Codes (3&ndash;9M) &ndash; Reliability</td><td><code>mh_cg_erica_rel_3_9m</code></td></tr>
<tr><td colspan="1" rowspan="2">V06 (15 to 30 Months)</td><td>ERICA Codes (15&ndash;30M)</td><td><code>mh_cg_erica_15_30m</code></td></tr>
<tr><td>ERICA Codes (15&ndash;30M) &ndash; Reliability</td><td><code>mh_cg_erica_rel_15_30m</code></td></tr>
<tr><td colspan="1" rowspan="2">V10 (46 to 60 Months)</td><td>ERICA Codes (46&ndash;60M)</td><td><code>mh_cg_erica_46_60m</code></td></tr>
<tr><td>ERICA Codes (46&ndash;60M) &ndash; Reliability</td><td><code>mh_cg_erica_rel_46_60m</code></td></tr>
</tbody>
</table>

<p><b>DQT Category</b></p>
<p>Derived fieldnames follow the same fieldname structure as the instruments, with an added <code>final_</code> suffix in the instrument section and pushed as backend fields under a new DQT category. </p>
<table class="table-no-vertical-lines">
<tbody>
<tr><td>ERICA Codes - 3 to 9 Months - Final - Derived</td><td><code>mh_cg_erica_3_9m_final</code></td></tr>
<tr><td>ERICA Codes - 15 to 30 Months - Final - Derived</td><td><code>mh_cg_erica_15_30m_final</code></td></tr>
<tr><td>ERICA Codes - 46 to 60 Months - Final - Derived</td><td><code>mh_cg_erica_46_60m_final</code></td></tr>
</tbody>
</table>

<h3 id="script-logic-to-derive-fields">Script Logic to Derive Fields</h3>
<h4 id="-reliability-form-check-">'Reliability' form check:</h4>
<p><strong>For any given instance, the logic checks first for data in the 'Reliability' form.</strong></p>
<ul>
<li>If data is available, as denoted by the instrument's 'Administration' status set to '<em>All</em>' or '<em>Partial</em>' and 'Data Entry' set to '<em>Complete</em>', as well as the DDE set to '<em>Complete/All</em>' or '<em>Complete/Partial</em>', then data can be transferred for fields with no conflict reported. For any given field, if there is a conflict yet to be resolved, the data for the field is not derived and a note is pushed saying &quot;<em>Conflict noted and pending to be resolved</em>&quot;.  </li>
<li>If initial data entry form is '<em>Complete/All</em>' or '<em>Complete/Partial</em>' and DDE form is '<em>In progress</em>' or not started ('Data Entry' is 'Null'), a note should be added to all fields saying &quot;<em>Data in 'Reliability' form but no DDE done</em>&quot;.  </li>
<li>If the 'Reliability' instrument's 'Administration' status is 'None' or 'Null', or the 'Data Entry' set to 'In progress', then no data from the 'Reliability' form is derived. </li>
</ul>
<p>Next, the script checks on the 'Codes' form, where a similar logic would ensue.</p>
<h4 id="check-codes-form-">Check 'Codes' Form:</h4>
<ul>
<li>If the original 'Codes' form's 'Administration' status is set to '<em>All</em>' or '<em>Partial</em>' and 'Data Entry' set to '<em>Complete</em>', as well as the DDE set to '<em>Complete/All'</em> or '<em>Complete/Partial</em>', then data can be transferred. For any given field, if there is a conflict yet to be resolved, the data is not derived and a note pushed saying &quot;<em>Conflict noted and pending to be resolved</em>&quot;.  </li>
<li>If initial data entry form is '<em>Complete/All</em>' or '<em>Complete/Partial</em>' and DDE form is '<em>In progress</em>' or not started ('Data Entry' is 'Null'), a note is added to all fields saying &quot;<em>Data in 'Codes' form but no DDE done</em>&quot;.</li>
</ul>
<h3 id="logic-tree">Logic Tree</h3>
<h4 id="reliability-checks">Reliability Form Checks</h4>
<ul>
<li><strong>Step 1. Check Reliability Administration status</strong><ul>
<li>If <strong>status = None</strong> → Skip following steps and go to Codes form Step 1  </li>
<li>OR If <strong>status = All or Partial</strong> → Proceed to Step 2</li>
</ul>
</li>
<li><strong>Step 2. Check Reliability Data Entry status</strong><ul>
<li>If <strong>status = In Progress or Null</strong> → Skip following steps and go to Codes form Step 1  </li>
<li>OR If <strong>status = Complete</strong> → Proceed to Step 3</li>
</ul>
</li>
<li><strong>Step 3. Check DDE Administration status</strong><ul>
<li>If <strong>status = None or Null</strong> → Add note: &quot;Data in Reliability form, but no DDE done&quot; → Stop  </li>
<li>OR If <strong>status = All or Partial</strong> → Proceed to Step 4</li>
</ul>
</li>
<li><strong>Step 4. Check DDE Data Entry status</strong><ul>
<li>If <strong>status = In progress</strong> → Add note: &quot;Data in Reliability form but no DDE done&quot; → Stop</li>
<li>OR If <strong>status = Complete</strong> → Proceed to Step 5</li>
</ul>
</li>
<li><strong>Step 5. Check conflicts per field</strong><ul>
<li>For fields with <strong>no conflicts</strong> → Transfer data to derived fields</li>
<li>For fields <strong>with conflicts</strong> → Add note: &quot;Conflict noted and pending to be resolved&quot;</li>
</ul>
</li>
</ul>

<h4 id="code-checks">Codes Form Checks</h4>
<ul>
<li><strong>Step 1. Check Administration status in Codes Form</strong>
  <ul>
  <li>If <strong>status = None</strong> → Stop process</li>
  <li>OR If <strong>status = All or Partial</strong> → Proceed to Step 2</li>
  </ul>
</li>
<li><strong>Step 2. Check Data Entry status</strong>
  <ul>
  <li>If <strong>status = In Progress or Null</strong> → Stop process</li>
  <li>OR If <strong>status = Complete</strong> → Proceed to Step 3</li>
  </ul>
</li>
<li><strong>Step 3. Check DDE Administration status</strong>
  <ul>
  <li>If <strong>status = None or Null</strong> (not started) → Add note "Data in 'Codes' form but no DDE done" to all fields</li>
  <li>OR If <strong>status = All or Partial</strong> → Proceed to Step 4</li>
  </ul>
</li>
<li><strong>Step 4. Check DDE Data Entry status</strong>
  <ul>
  <li>If <strong>status = In Progress</strong> → Add note "Data in 'Codes' form but no DDE done" to all fields</li>
  <li>OR If <strong>status = Complete</strong> → Proceed to Step 5</li>
  </ul>
</li>
<li><strong>Step 5. Check conflicts per field</strong>
  <ul>
  <li>For fields with <strong>no conflicts</strong> → Transfer data to derived fields</li>
  <li>For fields <strong>with conflicts</strong> → Add note: &quot;Conflict noted and pending to be resolved&quot;</li>
  </ul>
</li>
</ul>
</div>


## References
<div class="references"> 
</div>