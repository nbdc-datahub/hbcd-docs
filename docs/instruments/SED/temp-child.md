# Child Demographics

## Instrument Details


Demographic information is crucial for understanding the child’s environment and identifying how social, structural, and economic factors influence development over time in a longitudinal study of child development. **Beginning at Visit 4, the study includes a child demographic form** that captures detailed information about the child’s background, family structure, and household environment (see [Sources for Demographic Protocols & Modifications](demo-cg.md#demo-tables)). This includes:

 - Child's sex at birth
 - Child's race and ethnicity (with multiple selections allowed to capture diverse identities)
 - Respondent's relationship to the child, legal guardianship status, and whether the respondent lives with the child (including the number of days per month they share residence)
 - Detailed household composition, including the number of adults and children in the home and a household roster listing all individuals who live with the child at least two nights per week (including their age and sex)
 - Total household income for the past year (if the child resides in more than one household, respondents are asked to provide the average household income across residences)

These data are designed to support a nuanced analysis of the child’s social and family context within the HBCD study. See [Cioffredi et al. 2024](https://doi.org/10.1016/j.dcn.2024.101429) for a detailed description of the HBCD Demographics survey.

{{ hbcd_mods(instruments.demographics_ch) }}
{{ scoring(instruments.demographics_ch) }}


{{ warning_banner_macro() }}
<div class="collapsible-content">

<p><b>Branching Logic</b><br>
<p><b>Incorrect Interpretation of Days Per Month Living with Child Item</b><br>
The item “How many days per month do you live with the child?” (<code>sed_bm_demo_child__relat_002__01</code>) appears to have been misunderstood by some participants. An unexpectedly high number of respondents entered “7,” which suggests that they may have interpreted the question as referring to days per week rather than per month. The question formatting has since been revised to emphasize “per month” and to present 30 as the first response option. Users should interpret earlier responses (in V04) with caution, as some values may reflect misunderstanding of the reference period.</p>
<hr>
<p><b>Household Roster</b><br>
For household roster variables, respondents were instructed to <b>exclude the main child</b> when reporting the number of people living in the household (e.g., <a href="../demo-ch-table/#household-specific-details" target="_blank">item 29</a>). Metadata for relevant fields (<code>sed_bm_demo_child__roster_002__02__*</code>) will be updated in the future to make this instruction explicit. This includes fields describing the total number of children younger than 17, the total number of people in the household, and corresponding fields for a second household, if applicable.</p>
</div> 
