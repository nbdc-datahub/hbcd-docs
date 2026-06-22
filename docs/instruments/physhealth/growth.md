<!-- ADMIN NOTE: ALERT - MANUALLY STYLED PAGE - data warning -->


# Anthropometrics

{{ readme(instruments.growth) }}
{{ alert_warning(instruments.growth) }}



{{ warning_banner_macro() }}
<div class="collapsible-content">
<div class="info-section">
<div class="info-section-title">
    Range Checks For Growth
</div>
<p>Range checks were performed to identify and exclude extreme out-of-range values. Values outside of the following valid ranges were converted to 'n/a'. 
<i>Note that these ranges are not age-specific, i.e. the same ranges were used for all visits.</i></p>
<table class="table-no-vertical-lines">
<tbody>
<tr>
<td><b>Name</b></td>
<td><code>ph_ch_anthro_len_001__03</code></td>
<td><code>ph_ch_anthro_head_001__03</code></td>
<td><code>ph_ch_anthro_wei_001__03</code></td>
</tr>
<tr>
<td><b>Description</b></td>
<td>Average length (in cm)</td>
<td>Head circumference (cm)</td>
<td>Average weight (in kg)</td>
</tr>
<tr>
<td><b>Valid Range</b></td>
<td>30 to 130 cm</td>
<td>25 to 55 cm</td>
<td>0.5 to 30 kg</td>
</tr>
</tbody>
</table>
</div>
<div class="info-section">
<div class="info-section-title">
    Sex-Specific Birthweight for Gestational Age
</div>
<p>
Sex-specific birthweight for gestational age centiles and z-scores will be calculated in future data releases using Intergrowth curves (<a href="https://doi.org/10.1016/S0140-6736(14)60932-6">Villar et al. 2014</a>). In the meantime, data users can use these growth curves or ones of their choice to calculate centiles and small/large for gestational age variables. 
</p>
</div>
</div>

{{ issues_banner_macro() }}

## Instrument Details

Anthropometrics is a standard direct measure of child growth, including height or length (in cm), weight (in kg), and head circumference (cm). In older children (including visits V08 and V10-V14), it will also include abdominal circumference (cm).

{{ scoring(instruments.growth) }}

## References

<div class="references">
    <p>Villar, J., Cheikh Ismail, L., Victora, C. G., Ohuma, E. O., Bertino, E., Altman, D. G., Lambert, A., Papageorghiou, A. T., Carvalho, M., Jaffer, Y. A., Gravett, M. G., Purwar, M., Frederick, I. O., Noble, A. J., Pang, R., Barros, F. C., Chumlea, C., Bhutta, Z. A., Kennedy, S. H., & International Fetal and Newborn Growth Consortium for the 21st Century (INTERGROWTH-21st). (2014). <i>International standards for newborn weight, length, and head circumference by gestational age and sex: the Newborn Cross-Sectional Study of the INTERGROWTH-21st Project</i>. Lancet, 384(9946), 857–868. <a href="https://doi.org/10.1016/S0140-6736(14)60932-6">https://doi.org/10.1016/S0140-6736(14)60932-6</a></p>
</div>




<!-- {{ scoring_banner_macro() }}
<div class="collapsible-content">
<p><b>Anthropometric Z-Score and Percentile Calculations</b><br>
Age-based z-scores and percentiles for growth measurements were calculated for V02 onward using the <a href="https://github.com/CDC-DNPAO/WHOanthro">WHOanthro</a> R package. Calculations are based on estimated date of delivery, inherently adjusting for pre-mature birth. WHO growth charts were used for participants &lt;2 years old, and CDC growth charts were used for participants 2 years and older.</p>
</div> -->