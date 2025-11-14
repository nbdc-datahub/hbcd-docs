# Growth

<div class="info-block">
  <div class="info-row">
    <div class="info-label"><i class="fa fa-table"></i> Table Name:</div>
    <div class="info-value"><code>ph_ch_anthro</code></div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-maximize"></i> Full Name:</div>
    <div class="info-value">Height/Weight/Head Circumference</div>
  </div>
  <div class="info-row">
    <div class="info-label"><i class="fa-solid fa-tape"></i> Construct:</div>
    <div class="info-value">Growth</div>
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
<p><b>Z-Scores Excluded From Current Release</b><br>
Because dates of birth are jittered and calculated chronologic and adjusted ages are ±6 days, we do not provide z-scores in the current data release. Further, <strong>we do NOT recommend calculating z-scores using V02 data</strong>. Caution is recommended when calculating Z-scores using data from subsequent visits. Future data releases will have z-scores calculated with age in days for investigators wanting to compare to normative growth metrics.</p>
<p><b>Range Checks for Growth</b><br>
Range checks for Growth (<code>ph_ch_anthro</code>) were implemented in the database on 7/1/2024 and so are not reflected in data included in the first data release. Extreme out-of-range values outside of the following valid ranges were excluded (converted to 'n/a') (though some outliers are still possible):</p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <tr> 
  <th>Field Name</th>    
  <th>Field Description</th> 
  <th>Valid Range</th>
  </tr>
</thead>
<tbody>        
<tr><td><code>ph_ch_anthro_len_001__03</code></td><td>Length</td><td>30 to 130 cm</td></tr>     
<tr><td><code>ph_ch_anthro_head_001__03</code></td><td>Head circumference</td><td>25 to 55 cm</td></tr>          
<tr><td><code>ph_ch_anthro_wei_001__03</code></td><td>Weight</td><td>0.5 to 30 kg</td></tr>          
</tbody>
</table>
</div>

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>Yes</td></tr>
<tr><td><b>Respondent</b></td>
<td>NA</td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">HBCD Study Staff, in person.</td></tr>
<tr><td><b>Visits</b></td>
<td>V02, V03, V04, V06, V08</td></tr>
<tr><td><b>Completion Time</b></td>
<td>5 min</td></tr>
<tr><td><b>Quality Control</b></td>
<td style="word-wrap: break-word; white-space: normal;">Monitor data dashboard for variable missingness, possible coding errors, scoring verification when needed, and data consistency.</td></tr>
</tbody>
</table>

## Instrument Details

Growth is a standard direct measure of child growth, including height or length (in cm), weight (in kg), and head circumference (cm). In older children, it will also include abdominal circumference (cm). Because of the jittered date of birth we do not recommend using raw data to calculate age based z-score for growth measurements for V02 data. Children in this window are between 0-30 days older than their estimated due date thus the jittering of age may introduce error. 


