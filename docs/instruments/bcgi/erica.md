<!-- ADMIN NOTE: ALERT - INCLUDES HARD-CODED TABLE IN SUPP QC SECTION -->

# ERICA

{{ readme_summary(instruments.erica) }}
{{ alert_warning(instruments.erica) }}
{{ data_warning(instruments.erica) }}
{{ issues_banner() }}

---

## Instrument Details

{{ instrument_description(instruments.erica) }}
{{ hbcd_mods(instruments.erica) }}
{{ scoring(instruments.erica) }}

<!-- ## Centralized Coding of ERICA Videos -->
{{ suppx(instruments.erica, "1") }}

<!-- HARD-CODED TABLE -->
<table class="table-no-vertical-lines">
<thead>
<tr>
<th colspan="3"><b>ERICA Inter-rater Reliability for HBCD Data Release 2.1 (n=177)</b></th>
</tr><tr><th>Codes</th><th>ICC</th><th>Kappa</th></tr>
</thead>
<tbody>
<tr style="background-color: #e8f5fb;"><td>Child Positive Affect </td><td>0.88 (0.83,0.91)</td><td>--</td></tr>
<tr style="background-color: #e8f5fb;"><td>Child Irritability</td><td>0.96 (0.94,0.97)</td><td>--</td></tr>
<tr style="background-color: #e8f5fb;"><td>Child Social Engagement </td><td>0.76 (0.68,0.82)</td><td>--</td></tr>
<tr style="background-color: #bfe6f5;"><td>Caregiver Responsive Behavior </td><td>0.90 (0.87,0.93)</td><td>--</td></tr>
<tr style="background-color: #bfe6f5;"><td>Caregiver Irritable Behavior (Dichotomized)</td><td>0.61 (0.48,0.71)</td><td>0.44 (0.19,0.69)</td></tr>
<tr style="background-color: #bfe6f5;"><td>Caregiver Directive Behavior</td><td>0.87 (0.82,0.9)</td><td>--</td></tr>
<tr style="background-color: #8ad4f1;"><td>Dyadic Connectedness </td><td>0.76 (0.68,0.82)</td><td>--</td></tr>
<tr><td colspan="3"><i>ICC is a two-way, mixed effects, multiple rater intraclass correlation (ICC (3,k)) per Shrout and Fleiss (1979) conventions. ICC is best for continuous variables. Kappas are unweighted Cohen’s Kappa and are calculated for binary/categorical scores.</i></td></tr>
</tbody>
</table>

{{ references(instruments.erica) }}




<!-- <div id="qc" class="banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa fa-shield"></i></span><span class="text-with-link">
<span class="text">QC Procedures: Administration & Centralized Coding</span>
<a class="anchor-link" href="#qc" title="Copy link"><i class="fa-solid fa-link"></i></a></span><span class="arrow">▸</span></div>
<div class="collapsible-content my-box" markdown="1"> -->
<!-- 
## Centralized Coding of ERICA Videos

Videos are coded based on a single-pass review, with data entered directly into the HBCD database. Basic steps to ensure data completeness and accuracy include:

- Double data entry with conflict resolution to ensure accurate data entry
- Regular review of dashboards and reports to identify missing data and unexpected score distributions
- Completion reports cross-referenced with video files

##### ERICA Coding Training and Reliability Monitoring

Coders were trained and certified by coding experts under the supervision of ERICA developers. Certification required ≥80% agreement with expert ratings (exact agreement within ±0.5 decimal points per code). To ensure ongoing coder reliability, 20% of each coder's videos were randomly selected for double coding by experts (reliability coders) on a weekly basis. Coders who fell below 80% agreement for two consecutive weeks on any code were pulled from coding and re-trained/certified before continuing.

##### Coding Reliability Statistics

Inter-rater reliability was quantified using a two-way mixed-effects intraclass correlation coefficient (ICC) (see table below). All codes were evaluated using ICC except for Caregiver Irritable Behavior. Due to its low base rate, this code was dichotomized and reliability was estimated using an unweighted kappa statistic. Updated reliability estimates may be provided in future data releases as additional data become available. -->