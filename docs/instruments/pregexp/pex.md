<style>
.wy-nav-content {
    width: 95% !important;
    max-width: 95% !important;
    flex-grow: 1 !important;
}
</style>

# Pregnancy & Infant Health Instruments

{{ instrument_description(instruments.pex_all) }}

<table class="compact-table-no-vertical-lines readme-intro">
<thead>
<tr>
    <th>Instrument</th>
    <th>Acronym</th>
    <th>Construct</th>
    <th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
    <td>Health V1 – Health History</td>
    <td>Healthhx</td>
    <td>Pre-pregnancy and pregnancy health</td>
    <td><code>pex_bm_health_preg__healthhx</code></td>
</tr>
<tr>
    <td>Health V1 – Chronic Conditions</td>
    <td>Chroncond</td>
    <td>Chronic conditions and STIs in pregnancy</td>
    <td><code>pex_bm_health_preg__chroncond</code></td>
</tr>
<tr>
    <td>Health V1 – Illness</td>
    <td>Illness</td>
    <td>Illness during pregnancy</td>
    <td><code>pex_bm_health_preg__illness</code></td>
</tr>
<tr>
    <td>Health V1 – ER Admissions</td>
    <td>ERhosp</td>
    <td>ER visits and hospitalizations during pregnancy</td>
    <td><code>pex_bm_health_preg__erhosp</code></td>
</tr>
<tr>
    <td>Health V1 – Medications</td>
    <td>Meds</td>
    <td>Medication use during pregnancy</td>
    <td><code>pex_bm_health_preg__meds</code></td>
</tr>
<tr>
    <td>Health V1 – Exposures &amp; Vaccines</td>
    <td>Vacc</td>
    <td>Vaccinations during pregnancy</td>
    <td><code>pex_bm_health_preg__exp__vacc</code></td>
</tr>
<tr>
    <td>Health V2 – Pregnancy</td>
    <td>Healthv2 Preg</td>
    <td>Health updates through delivery</td>
    <td><code>pex_bm_healthv2_preg</code></td>
</tr>
<tr>
    <td>Health V2 – Infancy</td>
    <td>Healthv2 Inf</td>
    <td>Delivery characteristics and birth outcomes</td>
    <td><code>pex_bm_healthv2_inf</code></td>
</tr>
</tbody>
</table>

{{ alert_warning(instruments.pex_all) }}
{{ data_warning(instruments.pex_all) }}
{{ issues_banner() }}

### Instrument Details

Below we outline the general information contained within each instrument in more detail.

<table class="compact-table-no-vertical-lines readme-intro">
<thead>
<tr>
    <th>Acronym</th>
    <th>Examples</th>
</tr>
</thead>
<tbody>
<tr>
    <td>Healthhx</td>
    <td>Gravidity and parity, height and weight, pregnancy intentions, use of assisted reproductive technology, start of prenatal care, prenatal vitamin or aspirin use, secondhand smoke</td>
</tr>
<tr>
    <td>Vacc</td>
    <td>Vaccines in pregnancy including receipt of common vaccines in pregnancy and trimester received</td>
</tr>
<tr>
    <td>Chroncond</td>
    <td>Chronic conditions and sexually transmitted infections (STIs) during pregnancy, including whether they are ongoing or resolved</td>
</tr>
<tr>
    <td>Illness</td>
    <td>Illness in pregnancy, including start and stop dates and whether the person had a fever</td>
</tr>
<tr>
    <td>ERhosp</td>
    <td>ER visit(s) or hospitalization(s) during pregnancy, including occurrence and reason</td>
</tr>
<tr>
    <td>Meds</td>
    <td>Prescription and over-the-counter medications used during pregnancy, including name of medication, indication, frequency of use, and start/stop dates</td>
</tr>
<tr>
    <td>Healthv2 Preg</td>
    <td>Health updates for the birth parent between enrollment and delivery, including: prenatal vitamin use, aspirin intake, infections and illnesses, vaccinations, medication use (ongoing and newly prescribed), pregnancy complications (e.g., gestational diabetes), labor and delivery method, location, and hospital stay
</td>
</tr>
<tr>
    <td>Healthv2 Inf</td>
    <td>Delivery and birth outcomes include infant characteristics (birth weight & length, duration of hospital stay); newborn conditions (birth defects, genetic diagnoses); medical interventions including NICU admission and length of stay, intubation, adverse outcomes (e.g. bronchopulmonary dysplasia, congenital syphilis), medications (name, indication, status), healthcare access, specialist visits, and newborn hearing test results
</td>
</tr>
</tbody>
</table> 

{{ references(instruments.pex_all) }}




<!-- 
### ARCHIVE

<table class="compact-table-no-vertical-lines">
<thead>
  <tr> 
  <th>Field Name</th>    
  <th>Field Description</th> 
  <th>Valid Range</th>
  </tr>
</thead>
<tbody>               
  <tr><td><code>pex_bm_healthv2_inf_001__01</code></td><td>Weight at birth (oz)</td><td>≤ 16</td></tr>     
  <tr><td><code>pex_bm_healthv2_inf_001__02</code></td><td>Weight at birth (lbs)</td><td>≤ 66</td></tr>     
  <tr><td><code>pex_bm_healthv2_inf_002</code></td><td>Length at birth (inches)</td><td>12 - 51</td></tr>     
  <tr><td><code>pex_bm_healthv2_inf_002__01</code></td><td>Calculated length at birth (cm)</td><td>30 - 130</td></tr>   
</tbody>
</table>


<table class="compact-table-no-vertical-lines readme-intro">
<thead>
<tr>
    <th>Instrument</th>
    <th>Acronym</th>
    <th>Construct</th>
    <th>Table Name</th>
</tr>
</thead>
<tbody>
<tr>
    <td>Health V1 – Health History</td>
    <td>Healthhx</td>
    <td>Pre-pregnancy and pregnancy health</td>
    <td><code>pex_bm_health_preg__healthhx</code></td>
</tr>

<tr>
    <td>Health V1 – Chronic Conditions</td>
    <td>Chroncond</td>
    <td>Chronic conditions and STIs in pregnancy</td>
    <td><code>pex_bm_health_preg__chroncond</code></td>
</tr>
<tr>
    <td>Health V1 – Illness</td>
    <td>Illness</td>
    <td>Illness during pregnancy</td>
    <td><code>pex_bm_health_preg__illness</code></td>
</tr>
<tr>
    <td>Health V1 – ER Admissions</td>
    <td>ERhosp</td>
    <td>ER visits and hospitalizations during pregnancy</td>
    <td><code>pex_bm_health_preg__erhosp</code></td>
</tr>
<tr>
    <td>Health V1 – Medications</td>
    <td>Meds</td>
    <td>Medication use during pregnancy</td>
    <td><code>pex_bm_health_preg__meds</code></td>
</tr>
<tr>
    <td>Health V1 – Exposures &amp; Vaccines</td>
    <td>Vacc</td>
    <td>Vaccinations during pregnancy</td>
    <td><code>pex_bm_health_preg__exp__vacc</code></td>
</tr>
<tr>
    <td>Health V2 – Pregnancy</td>
    <td>Healthv2 Preg</td>
    <td>Health updates through delivery</td>
    <td><code>pex_bm_healthv2_preg</code></td>
</tr>
<tr>
    <td>Health V2 – Infancy</td>
    <td>Healthv2 Inf</td>
    <td>Delivery characteristics and birth outcomes</td>
    <td><code>pex_bm_healthv2_inf</code></td>
</tr>
</tbody>
</table> -->


<!-- 
replace in data warning:

<table class="compact-table-no-vertical-lines">
<thead>
  <tr> 
  <th>Field Name</th>    
  <th>Field Description</th> 
  <th>Valid Range</th>
  </tr>
</thead>
<tbody>               
  <tr><td><code>pex_bm_healthv2_inf_001__01</code></td><td>Weight at birth (oz)</td><td>≤ 16</td></tr>     
  <tr><td><code>pex_bm_healthv2_inf_001__02</code></td><td>Weight at birth (lbs)</td><td>≤ 66</td></tr>     
  <tr><td><code>pex_bm_healthv2_inf_002</code></td><td>Length at birth (inches)</td><td>12 - 51</td></tr>     
  <tr><td><code>pex_bm_healthv2_inf_002__01</code></td><td>Calculated length at birth (cm)</td><td>30 - 130</td></tr>   
</tbody>
</table>


- Weight at birth (oz) (`pex_bm_healthv2_inf_001__01`): ≤16
- Weight at birth (lbs) (`pex_bm_healthv2_inf_001__02`): ≤66
- Length at birth (inches) (`pex_bm_healthv2_inf_002`): 12–51
- Calculated length at birth (cm) (`pex_bm_healthv2_inf_002__01`): 30–130 -->