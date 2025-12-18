## Geocoded Linkage: Detailed Variable Descriptions

<table class="compact-table-no-vertical-lines" style="font-size: 14px;">
<thead>
<tr>
  <th>Variable Name (By Measure)</th>
  <th>Variable Label</th>
</tr>
</thead>
<tbody>
<!-- Admin -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;">Administrative</td>
</tr>
<tr>
  <td><code>PSCID</code></td>
  <td>Participant ID</td>
</tr>
<tr>
  <td><code>month_rel</code></td>
  <td>Time relative to EDD, in months (range -12 to 32)</td>
</tr>
<!-- Air Pollution -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Satellite-based Particulate Measures</b></td>
</tr>
<tr>
<td><code>particulat_{X}_mean_yb0</code></td>
<td style="word-wrap: break-word; white-space: normal;">
Annual average (mcg/m^3) measure of <code>{X}</code>:<br>
  <code>ec</code> (Elemental Carbon); <code>nh4</code> (Ammonium); <code>no3</code> (Nitrate); <code>oc</code> (Organic Carbon); <code>so4</code> (Sulfate)
</td>
</tr>
<!-- Soil Pollution -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Soil Contamination Measures</b></td>
</tr>
<tr>
  <td><code>gw_li</code></td>
  <td>Lithium concentration in soil C horizon (mg/kg)</td>
</tr>
<tr>
  <td><code>soilpoll_at_{X}</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Grid-level probability of exceedance (<i>Agricultural Thresholds</i>) for <code>{X}</code>:<br>
  <code>As</code> (Arsenic); <code>Cd</code> (Cadmium): <code>Co</code> (Cobalt); <code>Cr</code> (Chromium); <code>Cu</code> (Copper); <code>Ni</code> (Nickel); <code>Pb</code> (Lead)
</td>
</tr>
<tr>
  <td><code>soilpoll_hhet_{X}</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Grid-level probability of exceedance (<i>Human Health & Ecological Thresholds</i>) for <code>{X}</code>:<br>
  <code>As</code> (Arsenic); <code>Cd</code> (Cadmium): <code>Co</code> (Cobalt); <code>Cr</code> (Chromium); <code>Cu</code> (Copper); <code>Ni</code> (Nickel); <code>Pb</code> (Lead)
</tr>
<!-- Amenities & Services -->
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Neighborhood Socioeconomic Status and Demographics</b></td>
</tr>
<tr>
<td><code>nbhsoc_college_prop</code></td>
<td>Proportion of persons with Bachelors Degree or Higher</td>
</tr>
<tr>
<td><code>nbhsoc_factor{1|2|3}_tractscore</code></td>
<td>ADD DEFINITION</td>
</tr>
<tr>
<td><code>nbhsoc_finc{75k|100k}_prop</code></td>
<td>Proportion of families with income {$75k|$100k} or more</td>
</tr>
<tr>
<td><code>nbhsoc_forborn_prop</code></td>
<td>Proportion of people who are foreign born</td>
</tr>
<tr>
<td><code>nbhsoc_unemploy_prop</code></td>
<td>Proportion of age 16+ civilian labor force unemployed</td>
</tr>
<!-- parks -->
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Parks</b></td>
</tr>
<tr>
<td><code>parks_parks_{count|prop}</code></td>
<td>Total number (<code>count</code>)/Proportion (<code>prop</code>) of open parks in the census tract</td>
</tr>
<tr>
<td><code>parks_parkscounty_count</code></td>
<td>Total number of open parks in county</td>
</tr>
<tr>
<td><code>parks_parkstc10_count</code></td>
<td>Total number of open parks (top coded at 10) in census tract</td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Religious/Civic Organizations</b></td>
</tr>
<tr>
<td><code>relciv_civsoc_{count|prop}</code></td>
<td>Total number (<code>count</code>)/Proportion per 1000 people (<code>prop</code>) of Civic and Social Associations</td>
</tr>
<tr>
<td><code>relciv_civsoccounty_{count|prop)</code></td>
<td style="word-wrap: break-word; white-space: normal;">Total number (<code>count</code>)/Proportion per 1000 people (<code>prop</code>) of Civic and Social Associations- County-Level</td>
</tr>
<tr>
<td><code>relciv_relorg_{count|prop}</code></td>
<td>Total number (<code>count</code>)/Proportion per 1000 people (<code>prop</code>) of Religious Organizations</td>
</tr>
<tr>
<td><code>relciv_relorgcounty_{count|prop}</code></td>
<td style="word-wrap: break-word; white-space: normal;">Total number (<code>count</code>)/Proportion per 1000 people (<code>prop</code>) of Religious Organizations- County-Level</td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Social Service</b></td>
</tr>
<tr>
<td><code>socsrv_socsrv_{count|prop}</code></td>
<td></td>
</tr>
<tr>
<td><code>socsrv_socsrvcounty_{count|prop}</code></td>
<td></td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Building Density (EPA)</b></td>
</tr>
<tr>
<td><code>densbld_density</code></td>
<td></td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Population Density (EPA)</b></td>
</tr>
<tr>
<td><code>denspop_density</code></td>
<td></td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Vehicle Density (ACS)</b></td>
</tr>
<tr>
<td><code>densveh_{area|pop}_density</code></td>
<td>Aggregate Number Of Vehicles Available per sq. mile of land area (<code>area</code>)/individual (<code>pop</code>)</td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Urban/Rural Area (Census)</b></td>
</tr>
<tr>
<td><code>urban_urbanclassification</code></td>
<td></td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Walkability (EPA)</b></td>
</tr>
<tr>
<td><code>walk_idx</code></td>
<td>Walkability index</td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Behavioral Health Measures (PLACES)</b></td>
</tr>
<tr>
<td><code>places_access2_preval</code></td>
<td>Current lack of health insurance among adults aged 18-64 years</td>
</tr>
<tr>
<td><code>places_arthritis_preval</code></td>
<td>Arthritis among adults</td>
</tr>
<tr>
<td><code>places_binge_preval</code></td>
<td>Binge drinking among adults</td>
</tr>
<tr>
<td><code>places_bphigh_preval</code></td>
<td>High blood pressure among adults</td>
</tr>
<tr>
<td><code>places_bpmed_preval</code></td>
<td>Taking medicine to control high blood pressure among adults with high blood pressure</td>
</tr>
<tr>
<td><code>places_cancer_preval</code></td>
<td>Cancer (non-skin) or melanoma among adults</td>
</tr>
<tr>
<td><code>places_casthma_preval</code></td>
<td>Current asthma among adults</td>
</tr>
<tr>
<td><code>places_chd_preval</code></td>
<td>Coronary heart disease among adults</td>
</tr>
<tr>
<td><code>places_checkup_preval</code></td>
<td>Visits to doctor for routine checkup within the past year among adults</td>
</tr>
<tr>
<td><code>places_cholhigh_preval</code></td>
<td>High cholesterol among adults who have ever been screened</td>
</tr>
<tr>
<td><code>places_cholscreen_preval</code></td>
<td>Cholesterol screening among adults</td>
</tr>
<tr>
<td><code>places_colon_screen_preval</code></td>
<td>Colorectal cancer screening among adults aged 45&ndash;75 years</td>
</tr>
<tr>
<td><code>places_copd_preval</code></td>
<td>Chronic obstructive pulmonary disease among adults</td>
</tr>
<tr>
<td><code>places_csmoking_preval</code></td>
<td>Current cigarette smoking among adults</td>
</tr>
<tr>
<td><code>places_dental_preval</code></td>
<td>Visited dentist or dental clinic in the past year among adults</td>
</tr>
<tr>
<td><code>places_diabetes_preval</code></td>
<td>Diagnosed diabetes among adults</td>
</tr>
<tr>
<td><code>places_lpa_preval</code></td>
<td>No leisure-time physical activity among adults</td>
</tr>
<tr>
<td><code>places_mammouse_preval</code></td>
<td>Mammography use among women aged 50-74 years</td>
</tr>
<tr>
<td><code>places_mhlth_preval</code></td>
<td>Frequent mental distress among adults</td>
</tr>
<tr>
<td><code>places_obesity_preval</code></td>
<td>Obesity among adults</td>
</tr>
<tr>
<td><code>places_phlth_preval</code></td>
<td>Frequent physical distress among adults</td>
</tr>
<tr>
<td><code>places_sleep_preval</code></td>
<td>Short sleep duration among adults</td>
</tr>
<tr>
<td><code>places_stroke_preval</code></td>
<td>Stroke among adults</td>
</tr>
<tr>
<td><code>places_teethlost_preval</code></td>
<td>All teeth lost among adults aged &gt;=65 years</td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Measure of Land Cover and Tree Canopy (NLCD)</b></td>
</tr>
<tr>
<td><code>nlcd</code></td>
<td>?</td>
</tr>
<tr>
<td><code>tcc</code></td>
<td>Percent Tree Canopy Cover</td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Census Return (Anomie/Disenfranchisement/Social Capital)</b></td>
</tr>
<tr>
<td><code>censusret_return_rate_2020</code></td>
<td style="word-wrap: break-word; white-space: normal;">% occupied housing units providing sufficient internet, paper, or phone self-response (2020 Census)</td>
</tr>
<tr>
<td><code>censusret_selfresponse_rate_20192023</code></td>
<td style="word-wrap: break-word; white-space: normal;">Self-response rate for the 2019-2023 ACS, census tract; from Census Bureau Planning Database</td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Number of Jobs and Job Density (LODES)</b></td>
</tr>
<tr>
<td><code>lodes_job_{count|density}</code></td>
<td>Total count/density of jobs (per sq. mile of land area)</td>
</tr>
<tr>
<td><code>lodes_job{RACE-ETH}_{count|density}</code></td>
<td>Total count/density of jobs (per sq. mile of land area) by race & ethnicity<br>
<code>{RACE-ETH}</code>=<code>aian</code>; <code>asian</code>; <code>black</code>; <code>hisp</code>; <code>multi</code>; <code>nhpi</code>; <code>nonhisp</code>; <code>white</code></td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Rent and Mortgage Statistics (ACS)</b></td>
</tr>
<tr>
<td><code>rentmort_homevalue_med</code></td>
<td>&nbsp;</td>
</tr>
<tr>
<td><code>rentmort_ownership_prcnt</code></td>
<td>&nbsp;</td>
</tr>
<tr>
<td><code>rentmort_rent_med</code></td>
<td>&nbsp;</td>
</tr>
<tr>
<td><code>rentmort_rentburden_prcnt</code></td>
<td>&nbsp;</td>
</tr>
<tr>
<td><code>rentmort_rentburdensev_prcnt</code></td>
<td>&nbsp;</td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Social Mobility (Opportunity Atlas)</b></td>
</tr>
<tr>
<td><code>socmob_kfrpp_{count|mean|se}</code></td>
<td>Opportunity Atlas outcome for all children (count/mean/standard error)</td>
</tr>
<tr>
<td><code>socmob_kfrpp_p{1|25|50|75|100}_prcntile</code></td>
<td style="word-wrap: break-word; white-space: normal;">Opportunity Atlas Mean household income rank for children whose parents were at the {1st/25th/50th/75th/100th} percentile of the national income distribution</td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Area Deprivation Index (ADI)</b></td>
</tr>
<tr>
<td><code>adi_national_prcnt</code></td>
<td>National percentile of block group ADI score of Numeric Ranking (1-100) or Suppression Codes</td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Child Opportunity Index 2.0 (COI)</b> <i>(<code>{AREA}</code> = <code>state</code>/<code>metro</code>/<code>national</code>)</i></td>
</tr>
<tr>
<td><code>coi_coi_total_national_zscore</code></td>
<td>??? difference between score and zscore in this case?</td>
</tr>
<tr>
<td><code>coi_coi_total_{AREA}_{c5|score}</code></td>
<td>COI value (<code>c5</code>) & z-score (<code>score</code>)</td>
</tr>
<tr>
<td><code>coi_ed_total_{AREA}_{c5|score}</code></td>
<td>COI value (<code>c5</code>) & z-score (<code>score</code>) - Education Domain</td>
</tr>
<tr>
<td><code>coi_he_total_{AREA}_{c5|score}</code></td>
<td>COI value (<code>c5</code>) & z-score (<code>score</code>) - Health & Environment Domain</td>
</tr>
<tr>
<td><code>coi_se_total_{AREA}_{c5|score}</code></td>
<td>COI value (<code>c5</code>) & z-score (<code>score</code>) - Social & Economic Domain</td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Minority Health Social Vulnerability Index (MHSVI)</b></td>
</tr>
<tr>
<td><code>ssvi_{RACE-ETH}_prcnt</code></td>
<td style="word-wrap: break-word; white-space: normal;">Percentage population estimate <code>{RACE-ETH}</code><br>
<code>{RACE-ETH}</code> = <code>afam</code> (Black or African American); <code>aian</code> (American Indian and Alaska Native); <code>asian</code> (Asian); <code>his</code> (Hispanic or Latino); <code>nhpi</code> (Native Hawaiian/Pacific Islander); <code>white</code> (white)
</td>
</tr>
<tr>
<td><code>ssvi_{LANGUAGE}_prcnt</code></td>
<td>Percentage of <code>{LANGUAGE}</code> speakers who indicated that they speak English less than "very well."<br>
<code>{LANGUAGE}</code>= <code>rus</code> (Russian); <code>span</code> (Spanish); <code>chin</code> (Chinese); <code>kor</code> (Korean); <code>viet</code> (Vietnamese)</td>
</tr>
<tr>
<td><code>ssvi_hosp_state_prop</code></td>
<td>Number of hospitals</td>
</tr>
<tr>
<td><code>ssvi_nocomp_prcnt</code></td>
<td>Percentage population estimate persons with no computer access</td>
</tr>
<tr>
<td><code>ssvi_noint_prcnt</code></td>
<td>Percentage population estimate persons with no internet access</td>
</tr>
<tr>
<td><code>ssvi_pcp_state_rate</code></td>
<td>Primary care physicians per 100,000 people</td>
</tr>
<tr>
<td><code>ssvi_pharm_state_prop</code></td>
<td>Number of pharmacies</td>
</tr>
<tr>
<td><code>ssvi_unins_prcnt</code></td>
<td>Percentage population estimate persons without health insurance</td>
</tr>
<tr>
<td><code>ssvi_urg_state_prop</code></td>
<td>Number of urgent care clinics</td>
</tr>
<tr>
<td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>Social Vulnerability Index (SVI)</b></td>
</tr>
<tr>
<td><code>svi_17younger_{prcnt|prcntile}</code></td>
<td style="word-wrap: break-word; white-space: normal;">{Percentage/Percentile percentage} of persons aged 17 and younger</td>
</tr>
<tr>
<td><code>svi_65older_{prcnt|prcntile}</code></td>
<td style="word-wrap: break-word; white-space: normal;">{Percentage/Percentile percentage} of persons aged 65 and older</td>
</tr>
<tr>
<td><code>svi_crowding_{prcnt|prcntile}</code></td>
<td style="word-wrap: break-word; white-space: normal;">{Percentage/Percentile percentage} households with more people than rooms estimate</td>
</tr>
<tr>
<td><code>svi_disability_{prcnt|prcntile}</code></td>
<td style="word-wrap: break-word; white-space: normal;">{Percentage/Percentile percentage} of civilian noninstitutionalized population with a disability estimate</td>
</tr>
</tbody>
</table>





