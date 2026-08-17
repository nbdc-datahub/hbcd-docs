<!-- ADMIN NOTE: INCLUDES HARD-CODED TABLES -->

# APA 1/2

{{ readme_summary(instruments.apa) }}
{{ alert_warning(instruments.apa) }}
{{ data_warning(instruments.apa) }}
{{ issues_banner() }}

## Instrument Details

{{ instrument_description(instruments.apa) }}

##### Mental Health Domains Assessed By Levels 1/2

**Unless specified otherwise, Level 2 measures are only administered when symptoms are reported for Level 1.**

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Domain</th>
<th style="text-align:center;">Level 1</th>
<th style="text-align:center;">Level 2</th>
<th>HBCD Modifications</th>
</tr>
</thead>
<tbody>
<tr>
<td>Depression</td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td>Participants proceed to Level 2 irrespective of Level 1 answers;<br>
 Level 2 measures replaced with PROMIS-SF v1.0 Depression 8a questionnaire;<br>
 Clinical alert is triggered if responses (items from 'I felt worthless' to 'I felt that nothing could cheer me up') exceed threshold of 32</td>
</tr>
<tr>
<td>Anger</td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td></td>
</tr>
<tr>
<td>Mania</td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td></td>
</tr>
<tr>
<td>Anxiety</td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td></td>
</tr>
<tr>
<td>Somatic Symptoms</td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td>Participants proceed to Level 2 irrespective of Level 1 answers</td>
</tr>
<tr>
<td>Suicidal Ideation</td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
<td>Clinical alert is triggered if response to self-harm question exceeds threshold of 0</td>
</tr>
<tr>
<td>Psychosis</td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
<td></td>
</tr>
<tr>
<td>Sleep Disturbance</td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td>
 Level 2 symptom measures replaced with PROMIS-SF v1.0 Sleep Disturbance 8a</td>
</tr>
<tr>
<td>Memory</td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
<td></td>
</tr>
<tr>
<td>Repetitive Behaviors</td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td></td>
</tr>
<tr>
<td>Dissociation</td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
<td></td>
</tr>
<tr>
<td>Personality Inventory</td>
<td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
<td style="text-align:center;"><i class="fa-solid fa-check" style="color:green;"></i></td>
<td>Participants proceed to Level 2 without completing Level 1;<br>
Includes the Personality Inventory for DSM-5 Brief, which assesses 5 personality trait domains (<i>Negative Affect, Detachment, Antagonism, Disinhibition, & Psychoticism</i>)</td>
</tr>
<tr>
<td>Substance Use</td>
<td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
<td style="text-align:center;"><i class="fa-solid fa-x" style="color:red;"></i></td>
<td>Domain excluded (SU is measured by a separate set of instruments, e.g. ASSIST, Substance Use Patterns, & TLFB)</td>
</tr>
</tbody>
</table>

{{ hbcd_mods(instruments.apa) }}
{{ scoring(instruments.apa) }}



<div id="scoring" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fa fa-calculator"></i>
</span>
<span class="text-with-link">
    <span class="text">Scoring Procedures</span>
    <a class="anchor-link" href="#scoring" title="Copy link">
        <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Level 1 items (scored as 0=none, 1=slight, 2=mild, 3=moderate, 4=severe) and gating, including HBCD adaptations:</p>
<table class="compact-table-no-vertical-lines">
<tfoot><tr><td colspan="4"><b>*</b> <i>All items scored as 0=none, 1=slight, 2=mild, 3=moderate, 4=severe</i></td></tr></tfoot>
<thead>
<tr>
<th>&nbsp;</th>
<th>Level 1 Items*</th>
<th>Gate to level 2</th>
<th>Level 2 measure</th>
</tr>
</thead>
<tbody>
<tr>
<td>Depression</td>
<td>depr_001, depr_002</td>
<td>None (all proceed to Level 2)</td>
<td>PROMIS Adult Short Form v1.0 Depression 8a</td>
</tr>
<tr>
<td>Anger</td>
<td>apa_1_anger_001</td>
<td>apa_1_anger_001 &ge; 2</td>
<td>LEVEL 2-Anger-Adult (PROMIS Emotional Distress-Anger-Short Form)</td>
</tr>
<tr>
<td>Mania</td>
<td>apa_1_mania_001, apa_1_mania_002</td>
<td>apa_1_mania_001 or apa_1_mania_002  &ge; 2</td>
<td>LEVEL 2-Mania-Adult (Altman Self-Rating Mania Scale)</td>
</tr>
<tr>
<td>Anxiety</td>
<td>apa_1_anx_001</td>
<td>apa_1_anx_001  &ge; 2</td>
<td>LEVEL 2-Anxiety-Adult (PROMIS Emotional Distress-Anxiety-Short Form)</td>
</tr>
<tr>
<td>Somatic</td>
<td>apa_1_somat_001, apa_1_somat_002</td>
<td>None (all proceed to Level 2)</td>
<td>LEVEL 2-Somatic Symptom-Adult (Patient Health Questionnaire 15 Somatic Symptom Severity [PHQ-15])</td>
</tr>
<tr>
<td>Self-harm</td>
<td>apa_1_suic_001</td>
<td>No Level 2</td>
<td>No Level 2</td>
</tr>
<tr>
<td>Psychosis</td>
<td>apa_1_psych_001, apa_1_psych_002</td>
<td>No Level 2</td>
<td>No Level 2</td>
</tr>
<tr>
<td>Sleep</td>
<td>apa_1_sleep_001</td>
<td>apa_1_sleep_001  &ge; 2</td>
<td>Adult v1.0 - Sleep Disturbance 8a</td>
</tr>
<tr>
<td>Memory</td>
<td>apa_1_memo_001</td>
<td>No Level 2</td>
<td>No Level 2</td>
</tr>
<tr>
<td>Repetitive</td>
<td>apa_1_repet_001, apa_1_repet_002</td>
<td>apa_1_repet_001 or apa_1_repet_002  &ge; 2</td>
<td>LEVEL 2-Repetitive Thoughts and Behaviors-Adult (adapted from the Florida Obsessive-Compulsive Inventory [FOCI] Severity Scale [Part B])</td>
</tr>
<tr>
<td>Dissociation</td>
<td>apa_1_disso_001</td>
<td>No Level 2</td>
<td>No Level 2</td>
</tr>
<tr>
<td>Personality</td>
<td>Not administered</td>
<td>Not administered- all to personality inventory</td>
<td>Personality inventory for DSM-5 Brief</td>
</tr>
<tr>
<td>Substance use</td>
<td>Not administered</td>
<td>Not administered</td>
<td>Not administered</td>
</tr>
</tbody>
</table>

<p style="font-size: 1.0em;"><b>Level 2 items and scoring overview, including HBCD adaptations:</b></p>
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>&nbsp;</th>
<th>Level 2 Items</th>
<th>Scoring</th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>Depression</td>
<td>apa_2_depr_001-apa_2_depr_008</td>
<td>sum all items; look up t-score</td>
<td>All items must be answered in order to produce a valid score using the scoring tables</td>
</tr>
<tr>
<td>Anger</td>
<td>apa_2_anger_001-apa_2_anger_005</td>
<td>sum all items; look up t-score</td>
<td>One missing item, pro-rate ((raw score * 5)/(number answered)). Not scored if ≥2 items missing</td>
</tr>
<tr>
<td>Mania</td>
<td>apa_2_mania_001-apa_2_mania_005</td>
<td>sum all items; score of  &ge; 6 indicates high probability of mania</td>
<td>One missing item, pro-rate ((raw score * 5)/(number answered)). Not scored if ≥2 items missing</td>
</tr>
<tr>
<td>Anxiety</td>
<td>apa_2_anx_001-apa_2_anx_007</td>
<td>sum all items; look up t-score</td>
<td>Less than 3 missing items, pro-rate ((raw score *7)/(number answered)). Not scored if ≥3 items missing</td>
</tr>
<tr>
<td>Somatic</td>
<td>apa_2_somat_001-apa_2_somat_015</td>
<td>sum all items; interpreted using the Interpretation Table for the PHQ-15 Somatic Symptom Severity scale</td>
<td>Less than 4 missing items, pro-rate ((raw score *15)/(number answered)). Not scored if ≥4 items missing</td>
</tr>
<tr>
<td>Sleep</td>
<td>apa_2_sleep_001-apa_2_sleep_008</td>
<td>sum all items (<b>note: items 2 and 8 are reverse-scored</b>); look up t-score</td>
<td>All items must be answered in order to produce a valid score using the scoring tables</td>
</tr>
<tr>
<td>Repetitive</td>
<td>apa_2_repet_001-apa_2_repet_005</td>
<td>sum all items; look up t-score</td>
<td>One missing item, pro-rate ((raw score * 5)/(number answered)). Not scored if ≥2 items missing</td>
</tr>
<tr>
<td>Personality</td>
<td>apa_2_pers_001-apa_2_pers_025</td>
<td>sum all items; look up t-score</td>
<td>Six missing items, pro-rate ((raw score *25)/(number answered)). Not scored if ≥7 items missing</td>
</tr>
</tbody>
</table>
</div>

## Resources
{{ resources(instruments.apa) }}
{{ references(instruments.apa) }}

<!-- <img src="../DSM-5Level2Cross-CuttingSymptomMeasures.png" width="90%" height="auto" class="center"> -->
