# Personal and Family Psychiatric History

{{ readme(instruments.fam_mh) }}
{{ alert_warning(instruments.fam_mh) }}
{{ data_warning(instruments.fam_mh) }}
{{ issues_banner_macro() }}

## Instrument Details

The **HBCD FAM MH** assesses self-reported diagnoses and mental health conditions of the biological mother, biological father, and biological maternal and paternal grandmother and grandfather. It was created from combining and modifying items from the following instruments:

- **[Family History Assessment Module (FHAM)](https://arc.psych.wisc.edu/self-report/family-history-assessment-module-fham/)**
    - Alcohol use (`alc`)
    - Drug use (`drug`)
    - Depression (`dep`)
    - Mania (`man`)
    - Schizophrenia (`sch`)

- **[All of Us Personal and Family Health History](https://www.researchallofus.org/wp-content/themes/research-hub-wordpress-theme/media/2023/PaFHH_Survey_English.pdf)** - *Only collected for biological mother and father (bm/bf) & excludes questions about age of diagnosis, treatment, and medications*

    - Alcohol Use Disorder (`001`)
    - Anxiety disorder or panic disorder (`002`)
    - Autism Spectrum Disorder (`003`)
    - Bipolar disorder (`004`)
    - Depressive disorder (`005`)
    - Drug or Substance Use Disorder (`006`)
    - Schizophrenia (`007`)
    - Attention Deficit/Hyperactivity Disorder (ADHD) (`008`)

Future publications should note that this measure is a combination of these and that this is not a scored scale, but simply descriptive for family psychiatric history.

{{ hbcd_mods(instruments.fam_mh) }}
{{ scoring(instruments.fam_mh) }}

{{ mods_banner_macro() }}
<div class="collapsible-content">
<div class="info-section">
<div class="info-section-title">
    FHAM
</div>
<p>The FAM MH excludes the following items from the original FHAM instrument:</p>
<ol>
  <li>Items related to Antisocial Personality Disorder (<code>ASP</code>) and Undifferentiated Psychiatric Disorder (<code>UPD</code>)</li>
  <li>Items regarding treatment for mental or emotional problems, hospitalization, and suicide</li>
</ol>
<p>Additionally, the original response options (<em>parents</em>, <em>grandparents</em>, <em>siblings</em>, <em>aunts</em>, <em>uncles</em>, and <em>cousins</em>) were restricted to:</p>
<ul>
  <li>Biological mother (<code>001</code>) & Biological father (<code>002</code>)</li>
  <li>Biological maternal: grandmother (<code>003</code>) & grandfather (<code>004</code>)</li>
  <li>Biological paternal: grandmother (<code>005</code>) & grandfather (<code>006</code>)</li>
</ul>
</div>
<div class="info-section">
<div class="info-section-title">
    All of Us
</div>
<p>
The original response options (<em>mom</em>, <em>dad</em>, <em>sibling</em>, <em>daughter</em>, <em>son</em>, <em>grandparent</em>) were limited to biological mother (<code>bm</code>) and biological father (<code>bf</code>).
</p>
</div>
</div>

## References
<div class="references">
<p>Rice, J. P., Reich, T., Bucholz, K., Neuman, R. J., Fishman, R., Rochberg, N., Hesselbrock, V. M., Numberger, J. I., Shuckit, M. A., & Begleiter, H. (1995). Comparison of Direct Interview and Family History Diagnoses of Alcohol Dependence.  <em>Alcoholism: Clinical and Experimental Research</em>, <em>19</em>, 1018-1023. <a href="https://doi.org/10.1111/j.1530-0277.1995.tb00983.x">https://doi.org/10.1111/j.1530-0277.1995.tb00983.x</a></p>
</div>



<!-- <table class="table-no-vertical-lines" style="font-size: 1em;">
<tbody>
<tr><td><b>Table Name</b></td><td><code>pex_bm_psych</code></td></tr>
<tr><td><b>Construct</b></td><td>Personal and Family Mental Health</td></tr>
<tr><td><b>Study Visits</b></td><td>V01</td></tr>
<tr><td><b>Administration</b></td><td>
<b>Child-specific</b>: No<br>
<b>Respondent</b>: Pregnant Participant<br>
<b>Method</b>: Self-administered in-person (5 min estimated duration)</td></tr>
<td><b>Quality Control</b></td>
<td>Response distributions reviewed for outliers</td></tr>
</tbody></table> -->
