<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
.pr-pill {
  display: inline-block;
  padding: 2px 8px;
  font-size: 1em;
  font-weight: 600;
  border-radius: 999px;
  line-height: 1;
  white-space: nowrap;
}
/* Version-specific styling */
.pr-general {
  background-color: #e6f0ff;
  color: #1a4fb3;
}
/* TBD */
.pr-tbd {
  background-color: #f1f3f5;
  color: #666;
  font-style: italic;
}
</style>

# Known Issues & Pending Updates 

The tables below summarize **[Known Issues](#known-issues)** affecting the current data release and **[Pending Updates](#pending-updates)** across study instruments. Entries are organized by domain and include the expected release in which each fix or update will be implemented. This page is updated regularly as new issues are identified and updates are planned.

To ask a question or report an issue, please submit a ticket through the [Help Center in the NBDC Data Access Platform →](https://nbdc.lassoinformatics.com/issue-tracker)

---

<p style="font-size: 1.2em; color: #555; text-align: center;">
<i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> = Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i> = Pending Update
</p>
    
---

### Behavior & Child-Caregiver Interaction
<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th><th style='text-align: center;'><span class="tooltip tooltip-left">Fix<span class="tooltiptext">Target Release</span></span></th></tr>
</thead>
<tbody>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>ERICA</td>
<td style='word-wrap: break-word; white-space: normal;'>Addition of all age and <code>date_taken</code> fields (currently excluded due to use of coding rather than visit dates)</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3.0</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>ERICA</td>
<td style='word-wrap: break-word; white-space: normal;'>
  For a subset of participants, ERICA Codes (N=17) or Reliability (N=2) form scores are inaccurate; corrected scores are available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>. Users should further exclude participants with values of 0 across all scores (N=23 Codes, 12 Reliability) prior to analysis. 
</td>
<td style='text-align: center;'><span class='pr-pill pr-general'>3.0</span></td>
</tr>
</tbody></table>

<br><br><br><br><br><br><br>
