# Linked External Data

{{ readme(instruments.gled) }}
{{ alert_warning(instruments.gled) }}
{{ data_warning(instruments.gled) }}
{{ issues_banner_macro() }}

---

## Instrument Details

**Geocoded Linked External Data (GLED)** are external datasets linked to participants’ residential addresses. They serve as proxy measures of cumulative social, economic, and environmental contexts that may help explain individual differences in development ([Fan et al. 2021](https://doi.org/10.1016/j.dcn.2021.101030)). At each study visit, the Birth Parent or Primary Caregiver reports the child’s residential address history. Study staff collect this information in person or remotely (completion time: 5–15 minutes).

Geocoded linkage measures were deliberately designed to be compatible with the ABCD Study data, with appropriate updates for year (i.e. many of ABCD variables trace back to 2010 Census data, whereas HBCD is updated to 2020 Census data). The table below lists the geocoded measures included in the release for HBCD, categorized by domain, and associated links to detailed measure documentation available on the ABCD Data Documentation site (descriptions for each individual variable are available via this <a href="../gled-dd.html" target="_blank">supplemental table</a>). See [Fan et al. 2021](https://doi.org/10.1016/j.dcn.2021.101030) for additional details regarding each domain/measure.

## Release Data

The GLED data in the current release include variables linked to the residential address history of the child for visit V01 (prenatal period up to 1 year before EDD). The dataset is provided as <a href="../../../datacuration/file-based-data/#concatenated-data">concatenated data</a>.

<!-- ### Geocoded Linkage Measures -->

<span style="color: red; font-size: 1.3em;"> <b>ADMIN NOTE:</b> COPIED FROM <a style="color: red;" href="../HBCD-LED-DD.html" target="_blank">HTML DOC</a> with some minor additonal polish</span>

<style>
.gled td:first-child {
  font-family: monospace;
  color: #af00b1;
  font-size: 0.8em !important;
  font-weight: 500;
  white-space: nowrap;
  padding: 0.1em 0.3em;
  border-radius: 3px;
}
</style>

## Area Deprivation Index (ADI)

##### Measure Description
The Neighborhood Atlas hosts the Area Deprivation Index (ADI), a scientifically validated measure of the adverse social exposome (i.e., neighborhood disadvantage) that can be used to evaluate and improve factors that impact health across populations. The ADI ranks neighborhoods by adverse social exposome in a region of interest (e.g., at the state or national level), taking into account factors related to income, education, employment, and housing quality. The 2023 version is the latest version available. This version was created using 2019-2023 ACS data.

##### Key Variables
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>adi_national_prcnt</td>
<td>National percentile of block group ADI score of Numeric Ranking (1-100) or Suppression Codes</td>
</tr>
</tbody>
</table>

##### Key Reference
<div class="references"> 
<p>Kind AJH, Buckingham W. Making Neighborhood Disadvantage Metrics Accessible: The Neighborhood Atlas. New England Journal of Medicine, 2018. 378: 2456-2458. DOI: 10.1056/NEJMp1802313. PMCID: PMC6051533. AND University of Wisconsin School of Medicine Public Health. 2023 Area Deprivation Index v4.0. Downloaded from <a href="https://www.neighborhoodatlas.medicine.wisc.edu/">https://www.neighborhoodatlas.medicine.wisc.edu/</a>.</p>  
</div>

## Census Return
##### Measure Description
The Census Bureau's Planning Database (PDB) contains select operational, housing, demographic, and socio-economic statistics from the Decennial Census and the American Community Survey (ACS) 5-year files. The 2023 PDB contains select 2017-2021 ACS 5-year estimates including the ACS tract level self-response rates, 2020 Census operational variables, and select Census variables typically found on the PDB.

##### Key Variables
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>censusret_return_rate_2020</td>
<td>Percent of occupied housing units providing a sufficient internet, paper, or phone self-response</td>
</tr>
<tr>
<td>censusret_selfresponse_rate_20192023</td>
<td>The self-response rate of in-ACS housing units in the tract</td>
</tr>
</tbody>
</table>

##### Key Reference
<div class="references"> 
<p>U.S. Census Bureau. (2024, June 13). 2023 Planning Database. U.S. Census Bureau. 
<a href="https://www.census.gov/topics/research/guidance/planning-databases/2023.html#list-tab-1219258324">https://www.census.gov/topics/research/guidance/planning-databases/2023.html#list-tab-1219258324</a>.</p>  
</div>

## Child Opportunity Index 3.0 (COI)
##### Measure Description
The Child Opportunity Index (COI) 3.0 is a composite index of neighborhood conditions and resources that, per the research evidence, matter for children's healthy development. COI 3.0 is based on 44 component indicators spanning three domains (education, health and environment, and social and economic) and 14 subdomains. The latest release of the Child Opportunity Index, COI 3.0-2023, was published in 2025 and includes data covering the years from 2012 through 2023.

##### Key Variables

- `coicoi_total{AREA}_{c5|score}`
- `coied_total{AREA}_{c5|score}`
- `coihe_total{AREA}_{c5|score}`
- `coise_total{AREA}_{c5|score}`

<div id="coi" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">COI Variables - Full List</span>
  <a class="anchor-link" href="#coi" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Domain</th>
<th>Norming</th>
<th>Measure</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>coi_coi_total_national_zscore</code></td>
<td>Overall COI</td>
<td>National</td>
<td>Z-score</td>
</tr>
<tr>
<td><code>coi_ed_total_national_c5</code></td>
<td>Education</td>
<td>National</td>
<td>Opportunity Level (Very Low–Very High)</td>
</tr>
<tr>
<td><code>coi_he_total_national_c5</code></td>
<td>Health & Environment</td>
<td>National</td>
<td>Opportunity Level (Very Low–Very High)</td>
</tr>
<tr>
<td><code>coi_se_total_national_c5</code></td>
<td>Social & Economic</td>
<td>National</td>
<td>Opportunity Level (Very Low–Very High)</td>
</tr>
<tr>
<td><code>coi_coi_total_national_c5</code></td>
<td>Overall COI</td>
<td>National</td>
<td>Opportunity Level (Very Low–Very High)</td>
</tr>
<tr>
<td><code>coi_ed_total_national_score</code></td>
<td>Education</td>
<td>National</td>
<td>Opportunity Score (1–100)</td>
</tr>
<tr>
<td><code>coi_he_total_national_score</code></td>
<td>Health & Environment</td>
<td>National</td>
<td>Opportunity Score (1–100)</td>
</tr>
<tr>
<td><code>coi_se_total_national_score</code></td>
<td>Social & Economic</td>
<td>National</td>
<td>Opportunity Score (1–100)</td>
</tr>
<tr>
<td><code>coi_coi_total_national_score</code></td>
<td>Overall COI</td>
<td>National</td>
<td>Opportunity Score (1–100)</td>
</tr>
<tr>
<td><code>coi_ed_total_state_c5</code></td>
<td>Education</td>
<td>State</td>
<td>Opportunity Level (Very Low–Very High)</td>
</tr>
<tr>
<td><code>coi_he_total_state_c5</code></td>
<td>Health & Environment</td>
<td>State</td>
<td>Opportunity Level (Very Low–Very High)</td>
</tr>
<tr>
<td><code>coi_se_total_state_c5</code></td>
<td>Social & Economic</td>
<td>State</td>
<td>Opportunity Level (Very Low–Very High)</td>
</tr>
<tr>
<td><code>coi_coi_total_state_c5</code></td>
<td>Overall COI</td>
<td>State</td>
<td>Opportunity Level (Very Low–Very High)</td>
</tr>
<tr>
<td><code>coi_ed_total_state_score</code></td>
<td>Education</td>
<td>State</td>
<td>Opportunity Score (1–100)</td>
</tr>
<tr>
<td><code>coi_he_total_state_score</code></td>
<td>Health & Environment</td>
<td>State</td>
<td>Opportunity Score (1–100)</td>
</tr>
<tr>
<td><code>coi_se_total_state_score</code></td>
<td>Social & Economic</td>
<td>State</td>
<td>Opportunity Score (1–100)</td>
</tr>
<tr>
<td><code>coi_coi_total_state_score</code></td>
<td>Overall COI</td>
<td>State</td>
<td>Opportunity Score (1–100)</td>
</tr>
<tr>
<td><code>coi_ed_total_metro_c5</code></td>
<td>Education</td>
<td>Metro</td>
<td>Opportunity Level (Very Low–Very High)</td>
</tr>
<tr>
<td><code>coi_he_total_metro_c5</code></td>
<td>Health & Environment</td>
<td>Metro</td>
<td>Opportunity Level (Very Low–Very High)</td>
</tr>
<tr>
<td><code>coi_se_total_metro_c5</code></td>
<td>Social & Economic</td>
<td>Metro</td>
<td>Opportunity Level (Very Low–Very High)</td>
</tr>
<tr>
<td><code>coi_coi_total_metro_c5</code></td>
<td>Overall COI</td>
<td>Metro</td>
<td>Opportunity Level (Very Low–Very High)</td>
</tr>
<tr>
<td><code>coi_ed_total_metro_score</code></td>
<td>Education</td>
<td>Metro</td>
<td>Opportunity Score (1–100)</td>
</tr>
<tr>
<td><code>coi_he_total_metro_score</code></td>
<td>Health & Environment</td>
<td>Metro</td>
<td>Opportunity Score (1–100)</td>
</tr>
<tr>
<td><code>coi_se_total_metro_score</code></td>
<td>Social & Economic</td>
<td>Metro</td>
<td>Opportunity Score (1–100)</td>
</tr>
<tr>
<td><code>coi_coi_total_metro_score</code></td>
<td>Overall COI</td>
<td>Metro</td>
<td>Opportunity Score (1–100)</td>
</tr>
</tbody>
</table>
</div>

<p></p>

##### Key Reference
<div class="references"> 
<p><a href="https://urldefense.com/v3/__http://diversitydatakids.org__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moK5dBS3qQ$">diversitydatakids.org</a>. (2025, July 24). Child Opportunity Index 3.0–2023 Census Tract Data. Retrieved from <a href="https://www.diversitydatakids.org/research-library/child-opportunity-index-30-2023-census-tract-data">https://www.diversitydatakids.org/research-library/child-opportunity-index-30-2023-census-tract-data</a></p>  
</div>

## Vehicle Density (ACS)

##### Measure Description

Vehicle density was calculated using data from the 2019-2023 American Community Survey 5-year estimates for primary, secondary, and tertiary addresses at the census tract level. Vehicle density was calculated in two ways:

 - As an area estimate (aggregate number of variables in a census tract per square mile of land area), and
 - As a population density (aggregate number of vehicles available in a census tract per individual). Vehicle density may be associated with neighborhood residents’ levels of exposure to noxious chemicals and their vulnerability to vehicle-related injuries or fatalities

##### Key Variables
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>densveh_area_density</td>
<td>Aggregate Number of vehicles available per square mile of land area</td>
</tr>
<tr>
<td>densveh_pop_density</td>
<td>Aggregate Number of Vehicles available per individual</td>
</tr>
</tbody>
</table>

##### Key Reference
<div class="references"> 
<p>U.S. Census Bureau, U.S. Department of Commerce. "Aggregate Number of Vehicles Available by Tenure." American Community Survey, ACS 5-Year Estimates Detailed Tables, Table B25046, <a href="https://data.census.gov/table/ACSDT5Y2023.B25046?q=B25046:+Aggregate+Number+of+Vehicles+Available+by+Tenure&g=010XX00US$1400000">https://data.census.gov/table/ACSDT5Y2023.B25046?q=B25046:+Aggregate+Number+of+Vehicles+Available+by+Tenure&g=010XX00US$1400000</a>. Accessed on 5 Jan 2026.</p>  
</div>

## Number of Jobs and Job Density (LODES)

##### Measure Description
Number of jobs and job density (number of jobs per square mile of land area) are available at the census tract level for participants’ addresses. Employment statistics are also available, broken down by race and ethnicity. Employment information was derived from the LEHD Origin-Destination Employment Statistics (LODES) dataset for the year 2019.

##### Key Variables

 - `lodes_job_count`
 - `lodes_job_density`
 - `lodes_job{RACE-ETH}_count`
 - `lodes_job{RACE-ETH}_density`

<div id="lodes" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">LODES Variables - Full List</span>
  <a class="anchor-link" href="#lodes" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>lodes_job_count</td>
<td>Total number of jobs</td>
</tr>
<tr>
<td>lodes_jobwhite_count</td>
<td>Number of jobs for workers with Race: White, Alone</td>
</tr>
<tr>
<td>lodes_jobblack_count</td>
<td>Number of jobs for workers with Race: Black or African American Alone</td>
</tr>
<tr>
<td>lodes_jobaian_count</td>
<td>Number of jobs for workers with Race: American Indian or Alaska Native Alone</td>
</tr>
<tr>
<td>lodes_jobasian_count</td>
<td>Number of jobs for workers with Race: Asian Alone</td>
</tr>
<tr>
<td>lodes_jobnhpi_count</td>
<td>Number of jobs for workers with Race: Native Hawaiian or Other Pacific Islander Alone</td>
</tr>
<tr>
<td>lodes_jobmulti_count</td>
<td>Number of jobs for workers with Race: Two or More Race Groups</td>
</tr>
<tr>
<td>lodes_jobnonhisp_count</td>
<td>Number of jobs for workers with Ethnicity: Not Hispanic or Latino</td>
</tr>
<tr>
<td>lodes_jobhisp_count</td>
<td>Number of jobs for workers with Ethnicity: Hispanic or Latino</td>
</tr>
<tr>
<td>lodes_job_density</td>
<td>Residential history derived - Total density of jobs (per sq. mile of land area)</td>
</tr>
<tr>
<td>lodes_jobwhite_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Race: White, Alone</td>
</tr>
<tr>
<td>lodes_jobblack_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Race: Black or African American Alone</td>
</tr>
<tr>
<td>lodes_jobaian_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Race: American Indian or Alaska Native Alone</td>
</tr>
<tr>
<td>lodes_jobasian_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Race: Asian Alone</td>
</tr>
<tr>
<td>lodes_jobnhpi_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Race: Native Hawaiian or Other Pacific Islander Alone</td>
</tr>
<tr>
<td>lodes_jobmulti_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Race: Two or More Race Groups</td>
</tr>
<tr>
<td>lodes_jobnonhisp_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Ethnicity: Not Hispanic or Latino</td>
</tr>
<tr>
<td>lodes_jobhisp_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Ethnicity: Hispanic or Latino</td>
</tr>
</tbody>
</table>
</div>
<p></p>

##### Key Reference
<div class="references"> 
<p>Urban Institute. 2022. Longitudinal Employer-Household Dynamics Origin-Destination Employment Statistics (LODES) Summary Files - Census Tract Level. Accessible from <a href="https://datacatalog.urban.org/dataset/longitudinal-employer-household-dynamics-origin-destination-employment-statistics-lodes">https://datacatalog.urban.org/dataset/longitudinal-employer-household-dynamics-origin-destination-employment-statistics-lodes</a>. Data originally sourced from the US Census Bureau, developed at Urban Institute, and made available under the ODC-BY 1.0 Attribution License.</p>  
</div>

## Minority Health Social Vulnerability Index (MHSVI)

##### Measure Description
The Minority Health Index is a data resource developed jointly by the Centers for Disease Control and Prevention (CDC) and the U.S. Department of Health and Human Services (HHS) Office of Minority Health to help identify racial and ethnic minority communities that are at greatest risk for disproportionate impacts and adverse outcomes during public health emergencies. Its purpose is to enhance existing data tools and support public health research, planning, and response efforts with a focus on health equity. The data version is 2023.

##### Key Variables

 - `ssvi_{RACE-ETH}_prcnt`
 - `ssvi_{LANGUAGE}_prcnt`
 - `ssvi_hosp_state_prop`
 - `ssvi_nocomp_prcnt`
 - `ssvi_noint_prcnt`
 - `ssvi_pcp_state_rate`
 - `ssvi_pharm_state_prop`
 - `ssvi_unins_prcnt`
 - `ssvi_urg_state_prop`

 <div id="mhsvi" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">MHSVI Variables - Full List</span>
  <a class="anchor-link" href="#mhsvi" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>ssvi_white_prcnt</td>
<td>Percentage population estimate White</td>
</tr>
<tr>
<td>ssvi_aian_prcnt</td>
<td>Percentage population estimate American Indian and Alaska Native</td>
</tr>
<tr>
<td>ssvi_asian_prcnt</td>
<td>Percentage population estimate Asian</td>
</tr>
<tr>
<td>ssvi_afam_prcnt</td>
<td>Percentage population estimate Black or African American</td>
</tr>
<tr>
<td>ssvi_nhpi_prcnt</td>
<td>Percentage population estimate Native Hawaiian/Pacific Islander</td>
</tr>
<tr>
<td>ssvi_his_prcnt</td>
<td>Percentage population estimate Hispanic or Latino</td>
</tr>
<tr>
<td>ssvi_span_prcnt</td>
<td>percent Spanish Speakers who indicated they speak English less than "very well"</td>
</tr>
<tr>
<td>ssvi_chin_prcnt</td>
<td>percent Chinese Speakers who indicated they speak English less than "very well"</td>
</tr>
<tr>
<td>ssvi_viet_prcnt</td>
<td>percent Vietnamese Speakers who indicated they speak English less than "very well"</td>
</tr>
<tr>
<td>ssvi_kor_prcnt</td>
<td>percent Korean Speakers who indicated they speak English less than "very well"</td>
</tr>
<tr>
<td>ssvi_rus_prcnt</td>
<td>percent Russian Speakers who indicated they speak English less than "very well"</td>
</tr>
<tr>
<td>ssvi_hosp_state_prop</td>
<td>number of hospitals</td>
</tr>
<tr>
<td>ssvi_urg_state_prop</td>
<td>number of urgent care clinics</td>
</tr>
<tr>
<td>ssvi_pharm_state_prop</td>
<td>number of pharmacies</td>
</tr>
<tr>
<td>ssvi_pcp_state_rate</td>
<td>primary care physicians per 100,000 people</td>
</tr>
<tr>
<td>ssvi_unins_prcnt</td>
<td>Percentage population estimate persons without health insurance</td>
</tr>
<tr>
<td>ssvi_noint_prcnt</td>
<td>Percentage population estimate persons with no internet access</td>
</tr>
<tr>
<td>ssvi_nocomp_prcnt</td>
<td>Percentage population estimate persons with no computer access</td>
</tr>
</tbody>
</table>
</div>

<p></p>

##### Key Reference
<div class="references"> 
<p>U.S. Department of Health & Human Services, Office of Minority Health. (n.d.). Minority Health Index. Retrieved from <a href="https://minorityhealth.hhs.gov/minority-health-index">https://minorityhealth.hhs.gov/minority-health-index</a>.</p>  
</div>

## Neighborhood Socioeconomic Status and Demographics (NaNDA)
##### Measure Description
These datasets contain measures of socioeconomic and demographic characteristics by U.S. census tract for the years 2018-2022

The following were derived from the ACS 2018-2022 5-year estimates at the census tract level:

*   Proportion of people who are foreign born
*   Proportion of families with income greater than 75K
*   Proportion of families with income greater than $100K
*   Proportion 16+ civilian labor force unemployed

In addition, three factors associated with neighborhood sociodemographics and structural characteristics are included (based on Morenoff et al. (2007)):

*   Neighborhood disadvantage score is characterized by high levels of poverty, unemployment, female-headed families, households receiving public assistance income, and a high proportion of African Americans in a census tract.
*   Neighborhood affluence score represents a mix of characteristics associated with neighborhood affluence (concentrations of adults with a college education; with incomes>75K; and employed in managerial and professional occupations).
*   Neighborhood ethnic/immigrant score represents ethnic and immigrant concentration. Higher values indicate more Hispanic and foreign born in the census tract.

##### Key Variables

 - `nbhsoc_college_prop`
 - `nbhsoc_factor{1|2|3}_tractscore`
 - `nbhsoc_finc{75k|100k}_prop`
 - `nbhsoc_forborn_prop`
 - `nbhsoc_unemploy_prop`

 <div id="nanda" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">NaNDA Variables - Full List</span>
  <a class="anchor-link" href="#nanda" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>nbhsoc*forborn_prop</td>
<td>Proportion of people who are foreign born</td>
</tr>
<tr>
<td>nbhsoc_college_prop</td>
<td>Proportion of persons with Bachelors Degree or Higher</td>
</tr>
<tr>
<td>nbhsoc_finc100k_prop</td>
<td>Proportion of families with income $125,000 or more; 100k no longer exist;</td>
</tr>
<tr>
<td>nbhsoc_finc75k_prop</td>
<td>Proportion of families with income 75,000 to 124,999; for 75 k or more, sum with pfamincge125k;</td>
</tr>
<tr>
<td>nbhsoc_unemploy_prop</td>
<td>Proportion of age 16+ civilian labor force unemployed;</td>
</tr>
<tr>
<td>nbhsoc_factor1_tractscore</td>
<td>mean of pnhblack pfhfam ppubas ppov punemp</td>
</tr>
<tr>
<td>nbhsoc_factor2_tractscore</td>
<td>mean of ped3* pfamincge125k pprof</td>
</tr>
<tr>
<td>nbhsoc_factor3_tractscore</td>
<td>mean of phispanic pfborn plimeng</td>
</tr>
</tbody>
</table>
</div>
<p></p>

##### Key Reference
<div class="references"> 
<p>Clarke, Philippa, Melendez, Robert, Noppert, Grace, Chenoweth, Megan, and Gypin, Lindsay. National Neighborhood Data Archive (NaNDA): Socioeconomic Status and Demographic Characteristics of Census Tracts and ZIP Code Tabulation Areas, United States, 1990-2022. Inter-university Consortium for Political and Social Research [distributor], 2025-10-27. <a href="https://urldefense.com/v3/__https://doi.org/10.3886/ICPSR38528.v6__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moKH9ffZsQ$">https://doi.org/10.3886/ICPSR38528.v6</a></p> 
</div>

## Parks (NaNDA)
##### Measure Description
Prior research has demonstrated that access to parks and greenspace can have a positive impact on many aspects of and contributors to health, including physical activity levels (Kaczynski et al., 2007), healthy aging (Finlay, 2015), and sense of well-being (Larson et al., 2016). Neighborhood parks can also contribute to sense of community (Gómez, 2015). These datasets describe the number and area of parks in each census tract or each ZIP code tabulation area (ZCTA) in the United States. Measures include the total number of parks, park area, and proportion of park area within each census tract for the years 2018-2022.

The dataset describes：

 - Total number of parks per census tract (top coded at 10)
 - Total number of open parks per county
 - Proportion of open park land within census tract

##### Key Variables
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>parks_parks_count</td>
<td>Total number of open parks in the census tract</td>
</tr>
<tr>
<td>parks_parkstc10_count</td>
<td>Total number of open parks (top coded at 10) in census tract</td>
</tr>
<tr>
<td>parks_parks_prop</td>
<td>Proportion of open park land within census tract (tot_park_area / tract_area)</td>
</tr>
<tr>
<td>parks_parkscounty_count</td>
<td>DERIVED: groupby COUNTYFP and sum by COUNT_OPEN_PARKS</td>
</tr>
</tbody>
</table>

##### Key Reference
<div class="references"> 
<p>Melendez, Robert, Pan, Longrong, Li, Mao, Khan, Anam, Gomez-Lopez, Iris, Clarke, Philippa, … Chemberlin, Birch. National Neighborhood Data Archive (NaNDA): Parks by Census Tract and ZIP Code Tabulation Area, United States, 2018 and 2022. Inter-university Consortium for Political and Social Research [distributor], 2023-11-29. <a href="https://urldefense.com/v3/__https://doi.org/10.3886/ICPSR38586.v2__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moLd7t1CCA$">https://doi.org/10.3886/ICPSR38586.v2</a></p>
</div>

## Behavioral Health Measures (PLACES)
##### Measure Description
Measures from the PLACES dataset are available for participants’ addresses at the census tract level. The PLACES dataset is an expansion of the 500 Cities Project and is available from the Center for Disease and Control and Prevention (CDC), the Robert Wood Johnson Foundation (RWJF) and CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2023 or 2022 data, Census Bureau 2020 population data, and American Community Survey 2019-2023 or 2018–2022 estimates. The 2025 release uses 2023 BRFSS data for 35 measures and 2022 BRFSS data for 5 measures (all teeth lost, dental visits, mammograms, colorectal cancer screening, and short sleep duration) that the survey collects data on every other year. Included are 24 measures for the entire United States including chronic disease-related unhealthy behaviors, health outcomes, and use of preventive services. More information about the methodology can be found at [www.cdc.gov/places](https://www.cdc.gov/places/).

##### Key Variables

 - `places_*`

 <div id="places" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">PLACES Variables - Full List</span>
  <a class="anchor-link" href="#places" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>places_access2_preval</td>
<td>Current lack of health insurance among adults aged 18-64 years</td>
</tr>
<tr>
<td>places_arthritis_preval</td>
<td>Arthritis among adults</td>
</tr>
<tr>
<td>places_binge_preval</td>
<td>Binge drinking among adults</td>
</tr>
<tr>
<td>places_bphigh_preval</td>
<td>High blood pressure among adults</td>
</tr>
<tr>
<td>places_bpmed_preval</td>
<td>Taking medicine to control high blood pressure among adults with high blood pressure</td>
</tr>
<tr>
<td>places_cancer_preval</td>
<td>Cancer (non-skin) or melanoma among adults</td>
</tr>
<tr>
<td>places_casthma_preval</td>
<td>Current asthma among adults</td>
</tr>
<tr>
<td>places_chd_preval</td>
<td>Coronary heart disease among adults</td>
</tr>
<tr>
<td>places_checkup_preval</td>
<td>Visits to doctor for routine checkup within the past year among adults</td>
</tr>
<tr>
<td>places_cholscreen_preval</td>
<td>Cholesterol screening among adults</td>
</tr>
<tr>
<td>places_colon_screen_preval</td>
<td>Colorectal cancer screening among adults aged 45&ndash;75 years</td>
</tr>
<tr>
<td>places_copd_preval</td>
<td>Chronic obstructive pulmonary disease among adults</td>
</tr>
<tr>
<td>places_csmoking_preval</td>
<td>Current cigarette smoking among adults</td>
</tr>
<tr>
<td>places_dental_preval</td>
<td>Visited dentist or dental clinic in the past year among adults</td>
</tr>
<tr>
<td>places_diabetes_preval</td>
<td>Diagnosed diabetes among adults</td>
</tr>
<tr>
<td>places_cholhigh_preval</td>
<td>High cholesterol among adults who have ever been screened</td>
</tr>
<tr>
<td>places_lpa_preval</td>
<td>No leisure-time physical activity among adults</td>
</tr>
<tr>
<td>places_mammouse_preval</td>
<td>Mammography use among women aged 50-74 years</td>
</tr>
<tr>
<td>places_mhlth_preval</td>
<td>Frequent mental distress among adults</td>
</tr>
<tr>
<td>places_obesity_preval</td>
<td>Obesity among adults</td>
</tr>
<tr>
<td>places_phlth_preval</td>
<td>Frequent physical distress among adults</td>
</tr>
<tr>
<td>places_sleep_preval</td>
<td>Short sleep duration among adults</td>
</tr>
<tr>
<td>places_stroke_preval</td>
<td>Stroke among adults</td>
</tr>
<tr>
<td>places_teethlost_preval</td>
<td>All teeth lost among adults aged &gt;=65 years</td>
</tr>
</tbody>
</table>
</div>

<p></p>

##### Key Reference
<div class="references"> 
<p>Centers for Disease Control and Prevention. (n.d.). PLACES: Local Data for Better Health, Census Tract Data. CDC Data Portal., from <a href="https://urldefense.com/v3/__https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh/about_data__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moKT9wS4LQ$">https://data.cdc.gov/500-Cities-Places/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh/about_data</a></p>
</div>

## Religious/Civic Organizations (NaNDa)
##### Measure Description
This dataset contains measures of the number and density of select types of civic, social, and religious organizations per United States Census Tract for the year 2021.

 - Total count of religious organizations
 - Number of all religious organizations per 1000 people
 - Total count of civic/social organizations
 - Number of all civic/social organizations per 1000 people

##### Key Variables

- `relcivcivsoc{count|prop}`
- `relcivcivsoccounty{count|prop}`
- `relcivrelorg{count|prop}`
- `relcivrelorgcounty{count|prop}`

 <div id="relciv" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Religious/Civic Organizations Variables - Full List</span>
  <a class="anchor-link" href="#relciv" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>relciv_relorg_count</td>
<td>Total counts: Religious Organizations</td>
</tr>
<tr>
<td>relciv_relorg_prop</td>
<td>Religious Organizations per 1000 people</td>
</tr>
<tr>
<td>relciv_relorgcounty_count</td>
<td>groupby(county) and sum(count_religiousorgs)</td>
</tr>
<tr>
<td>relciv_relorgcounty_prop</td>
<td>groupby(county) and sum(den_religiousorgs)</td>
</tr>
<tr>
<td>relciv_civsoc_count</td>
<td>Total counts: Civic and Social Associations</td>
</tr>
<tr>
<td>relciv_civsoc_prop</td>
<td>Civic and Social Associations per 1000 people</td>
</tr>
<tr>
<td>relciv_civsoccounty_count</td>
<td>groupby(county) and sum(count_civsoc)</td>
</tr>
<tr>
<td>relciv_civsoccounty_prop</td>
<td>groupby(county) and sum(den_civsoc)</td>
</tr>
</tbody>
</table>
</div>
<p></p>

##### Key Reference
<div class="references"> 
<p>Melendez, Robert, Finlay, Jessica, Clarke, Philippa, Noppert, Grace, and Gypin, Lindsay. National Neighborhood Data Archive (NaNDA): Civic, Social, and Religious Organizations by Census Tract and ZCTA, United States, 1990-2021. Ann Arbor, MI: Inter-university Consortium for Political and Social Research [distributor], 2024-07-24. <a href="https://urldefense.com/v3/__https://doi.org/10.3886/E207966V1__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moJ5svAf3w$">https://doi.org/10.3886/E207966V1</a></p>
</div>

## Rent and Mortgage Statistics (ACS)
##### Measure Description
In order to approximate cost of living that may be associated with housing, the following variables from the 2019-2023 American Community Survey (ACS) 5-year estimates have been linked to participants’ addresses at the census tract level:

 - Percent home ownership
 - Percent of households living with rent burden (rent is at least 30% of income),
 - Percent of households living with severe rent burden (rent is at least 50% of income)
 - Median monthly gross rent
 - Median monthly mortgage payments.

##### Key Variables

 <!-- - `rentmort_homevalue_med`
 - `rentmort_ownership_prcnt`
 - `rentmort_rent_med`
 - `rentmort_rentburden_prcnt`
 - `rentmort_rentburdensev_prcnt` -->

<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>rentmort_ownership_prcnt</td>
<td>Residential history derived - Percent Homeownership;ACS2019-2023; census tract; Occupied housing units(owner occupied) / Total tenure occupied housing units</td>
</tr>
<tr>
<td>rentmort_homevalue_med</td>
<td>Residential history derived - Median house value; ACS2019-2023; census tract</td>
</tr>
<tr>
<td>rentmort_rentburden_prcnt</td>
<td>Residential history derived - Percent rent burden(30% or more of income); ACS2019-2023; census tract</td>
</tr>
<tr>
<td>rentmort_rentburdensev_prcnt</td>
<td>Residential history derived - Percent severe rent burden (50% or more of income); ACS2019-2023; census tract</td>
</tr>
<tr>
<td>rentmort_rent_med</td>
<td>Residential history derived - Median rent per month; ACS2019-2023; census tract</td>
</tr>
</tbody>
</table>

##### Key Reference
From [https://www.census.gov/data/developers/data-sets/acs-5year.html](https://www.census.gov/data/developers/data-sets/acs-5year.html)

## Building Density (EPA)
##### Measure Description
This data is part of the Smart Location Database for the year 2021, which is a nationwide geographic data resource for measuring location efficiency. It measures Gross residential density (housing units per acre) on unprotected land.

##### Key Variables
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>densbld_density</td>
<td>Gross residential density (HU/acre) on unprotected land</td>
</tr>
</tbody>
</table>

##### Key Reference
<div class="references"> 
<p>U.S. Environmental Protection Agency. (2025, September 29). Smart Location Mapping. U.S. EPA. from <a href="https://urldefense.com/v3/__https://www.epa.gov/smartgrowth/smart-location-mapping__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moJUAuUGig$">https://www.epa.gov/smartgrowth/smart-location-mapping</a></p>
</div>

## Walkability (EPA)

##### Measure Description
The National Walkability Index is a nationwide geographic data resource that ranks block groups according to their relative walkability. The national dataset for the year 2021 includes walkability scores for all block groups as well as the underlying attributes that are used to rank the block groups.

##### Key Variables
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>walk_idx</td>
<td>Walkability index comprised of weighted sum of the ranked values of [D2a_EpHHm] (D2A_Ranked), [D2b_E8MixA] (D2B_Ranked), [D3b] (D3B_Ranked) and [D4a] (D4A_Ranked)</td>
</tr>
</tbody>
</table>

##### Key Reference
<div class="references"> 
<p>U.S. Environmental Protection Agency. (2025, September 29). Smart Location Mapping. U.S. EPA. from <a href="https://urldefense.com/v3/__https://www.epa.gov/smartgrowth/smart-location-mapping__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moJUAuUGig$">https://www.epa.gov/smartgrowth/smart-location-mapping</a></p>
</div>

## Social Mobility (Opportunity Atlas)
##### Measure Description
The Opportunity Atlas uses anonymous data based on 20 million Americans followed from childhood to their mid-30s to provide outcomes for adults who grew up in each census tract. Percentile household incomes correspond to outcomes in adulthood of people who grew up in each census tract and were born between 1978 and 1983.

The variable corresponding to the 25th percentile is typically the main index of upward social mobility for each census tract, as it captures the mean income rank in adulthood for children who grew up in low-income families in this census tract. See the US Census Bureau website for more details.

##### Key Variables
 - `socmobkfrpp{count|mean|se}`
 - `socmob_kfrpp_p{1|25|50|75|100}_prcntile`

 <div id="socmob" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Social Mobility Variables - Full List</span>
  <a class="anchor-link" href="#socmob" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><strong>Note:</strong> All variables are residential history–derived Opportunity Atlas measures at the census tract level. Child outcomes reflect mean earnings in 2014–2015 for ages 31–37.</p>
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>socmob_kfrpp_mean</td>
<td>Mean outcome for all children</td>
</tr>
<tr>
<td>socmob_kfrpp_count</td>
<td>Number of children</td>
</tr>
<tr>
<td>socmob_kfrpp_p1_prcntile</td>
<td>Mean household income rank for children with parents at the 1st percentile</td>
</tr>
<tr>
<td>socmob_kfrpp_p25_prcntile</td>
<td>Mean household income rank for children with parents at the 25th percentile (“upward mobility” per Chetty et al.)</td>
</tr>
<tr>
<td>socmob_kfrpp_p50_prcntile</td>
<td>Mean household income rank for children with parents at the 50th percentile</td>
</tr>
<tr>
<td>socmob_kfrpp_p75_prcntile</td>
<td>Mean household income rank for children with parents at the 75th percentile</td>
</tr>
<tr>
<td>socmob_kfrpp_p100_prcntile</td>
<td>Mean household income rank for children with parents at the 100th percentile</td>
</tr>
<tr>
<td>socmob_kfrpp_se</td>
<td>Estimated standard error (all children)</td>
</tr>
</tbody>
</table>
</div>
<p></p>

##### Key Reference
<div class="references"> 
<p>Opportunity Insights. Opportunity Atlas Data Tool Summary. 13 Aug. 2025, <a href="https://urldefense.com/v3/__http://opportunityinsights.org/wp-content/uploads/2025/08/OpportunityAtlas_DataToolSummary.pdf__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moLXaMuETA$">opportunityinsights.org/wp-content/uploads/2025/08/OpportunityAtlas_DataToolSummary.pdf</a></p>
</div>

## Social Service (NaNDa)
##### Measure Description
Measure includes senior centers, youth centers, food banks, job training programs, and day care centers(per census tract and per county) for the year 2021:

 - Total count of social services
 - Number of all social services per 1000 people

##### Key Variables
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>socsrv_socsrv_count</td>
<td>Total counts: Total Individual and Family Services</td>
</tr>
<tr>
<td>socsrv_socsrv_prop</td>
<td>Total Individual and Family Services per 1000 people</td>
</tr>
<tr>
<td>socsrv_socsrvcounty_count</td>
<td>groupby(county) and sum(count_indivfamilyservices)</td>
</tr>
<tr>
<td>socsrv_socsrvcounty_prop</td>
<td>groupby(county) and sum(den_indivfamilyservices)</td>
</tr>
</tbody>
</table>

##### Key Reference
<div class="references"> 
<p>Melendez, Robert, Finlay, Jessica, Clarke, Philippa , Noppert, Grace, Gypin, Lindsay, and Dyke, Ellis. National Neighborhood Data Archive (NaNDA): Social Services by Census Tract and ZCTA, United States, 1990-2021. Ann Arbor, MI: Inter-university Consortium for Political and Social Research [distributor], 2024-09-27. <a href="https://urldefense.com/v3/__https://doi.org/10.3886/E208207V3__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moKHP7-omA$">https://doi.org/10.3886/E208207V3</a></p>
</div>

## Social Vulnerability Index (SVI)
##### Measure Description

Every community must prepare for and respond to hazardous events, whether a natural disaster like a tornado or a disease outbreak, or an anthropogenic event such as a harmful chemical spill. The degree to which a community exhibits certain social conditions, including high poverty, low percentage of vehicle access, or crowded households, among others, may affect that community’s ability to prevent human suffering and financial loss in the event of a disaster. These factors describe a community’s social vulnerability.

ATSDR’s Geospatial Research, Analysis, & Services Program (GRASP) created the Centers for Disease Control and Prevention and Agency for Toxic Substances and Disease Registry Social Vulnerability Index (hereafter, CDC/ATSDR SVI or SVI) to help public health officials and emergency response planners identify and map the communities that will most likely need support before, during, and after a hazardous event.

SVI data for the year 2022 indicates the relative vulnerability of every U.S. census tract. Census tracts are subdivisions of counties for which the Census collects statistical data. SVI ranks the tracts on 16 social factors, such as unemployment, racial and ethnic minority status, and disability status. Then, SVI further groups the factors into four related themes. Thus, each tract receives a ranking for each Census variable and for each of the four themes as well as an overall ranking.

##### Key Variables

 - `svi_*`

 <div id="svi" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">SVI Variables - Full List</span>
  <a class="anchor-link" href="#svi" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>svi_17younger_prcnt</td>
<td>Percentile percentage of persons aged 17 and younger estimate</td>
</tr>
<tr>
<td>svi_17younger_prcntile</td>
<td>Percentage of persons aged 17 and younger estimate, 2018-2022 ACS</td>
</tr>
<tr>
<td>svi_65older_prcnt</td>
<td>Percentile percentage of persons aged 65 and older estimate</td>
</tr>
<tr>
<td>svi_65older_prcntile</td>
<td>Percentage of persons aged 65 and older estimate, 2018-2022 ACS</td>
</tr>
<tr>
<td>svi_crowding_prcnt</td>
<td>Percentage of occupied housing units with more people than rooms estimate</td>
</tr>
<tr>
<td>svi_crowding_prcntile</td>
<td>Percentile percentage households with more people than rooms estimate</td>
</tr>
<tr>
<td>svi_disability_prcnt</td>
<td>Percentile percentage of civilian noninstitutionalized population with a disability estimate</td>
</tr>
<tr>
<td>svi_disability_prcntile</td>
<td>Percentage of civilian noninstitutionalized population with a disability estimate, 2018-2022 ACS</td>
</tr>
<tr>
<td>svi_unemploy_prcnt</td>
<td>Percentile percentage of civilian (age 16+) unemployed estimate</td>
</tr>
<tr>
<td>svi_unemploy_prcntile</td>
<td>Unemployment Rate estimate</td>
</tr>
<tr>
<td>svi_lesseng_prcnt</td>
<td>Percentile percentage of persons (age 5+) who speak English "less than well" estimate</td>
</tr>
<tr>
<td>svi_lesseng_prcntile</td>
<td>Percentage of persons (age 5+) who speak English "less than well" estimate, 2018-2022 ACS</td>
</tr>
<tr>
<td>svi_groupquarters_prcnt</td>
<td>Percentile percentage of persons in group quarters estimate</td>
</tr>
<tr>
<td>svi_groupquarters_prcntile</td>
<td>Percentage of persons in group quarters estimate, 2018-2022 ACS</td>
</tr>
<tr>
<td>svi_multiplehousing_prcnt</td>
<td>Percentage of housing in structures with 10 or more units estimate</td>
</tr>
<tr>
<td>svi_multiplehousing_prcntile</td>
<td>Percentile percentage housing in structures with 10 or more units estimate</td>
</tr>
<tr>
<td>svi_nohsdiploma_prcnt</td>
<td>Percentile percentage of persons with no high school diploma (age 25+) estimate</td>
</tr>
<tr>
<td>svi_nohsdiploma_prcntile</td>
<td>Percentage of persons with no high school diploma (age 25+) estimate</td>
</tr>
<tr>
<td>svi_minority_prcnt</td>
<td>Percentile percentage minority (Hispanic or Latino (of any race); Black and African American, Not Hispanic or Latino; American Indian and Alaska Native, Not Hispanic or Latino; Asian, Not Hispanic or Latino; Native Hawaiian and Other Pacific Islander, Not Hispanic or Latino; Two or More Races, Not Hispanic or Latino; Other Races, Not Hispanic or Latino) estimate*</td>
</tr>
<tr>
<td>svi_minority_prcntile</td>
<td>Percentage minority (Hispanic or Latino (of any race); Black and African American, Not Hispanic or Latino; American Indian and Alaska Native, Not Hispanic or Latino; Asian, Not Hispanic or Latino; Native Hawaiian and Other Pacific Islander, Not Hispanic or Latino; Two or More Races, Not Hispanic or Latino; Other Races, Not Hispanic or Latino) estimate, 2018-2022 ACS*</td>
</tr>
<tr>
<td>svi_mobilehomes_prcnt</td>
<td>Percentile percentage mobile homes estimate</td>
</tr>
<tr>
<td>svi_mobilehomes_prcntile</td>
<td>Percentage of mobile homes estimate</td>
</tr>
<tr>
<td>svi_poverty_prcnt</td>
<td>Percentile percentage of persons below 150% poverty estimate</td>
</tr>
<tr>
<td>svi_poverty_prcntile</td>
<td>Percentage of persons below 150% poverty estimate</td>
</tr>
<tr>
<td>svi_singlehousehold_prcnt</td>
<td>Percentile percentage of single-parent households with children under 18 estimate</td>
</tr>
<tr>
<td>svi_singlehousehold_prcntile</td>
<td>Percentage of single-parent households with children under 18 estimate, 2018-2022 ACS</td>
</tr>
<tr>
<td>svi_theme1_prcntile</td>
<td>Percentile ranking for Socioeconomic Status theme summary</td>
</tr>
<tr>
<td>svi_theme2_prcntile</td>
<td>Percentile ranking for Household Characteristics theme summary</td>
</tr>
<tr>
<td>svi_theme3_prcntile</td>
<td>Percentile ranking for Racial and Ethnic Minority Status theme</td>
</tr>
<tr>
<td>svi_theme4_prcntile</td>
<td>Percentile ranking for Housing Type/ Transportation theme</td>
</tr>
<tr>
<td>svi_total_prcntile</td>
<td>Overall percentile ranking</td>
</tr>
<tr>
<td>svi_uninsured_prcnt</td>
<td>Percentage uninsured in the total civilian noninstitutionalized population estimate, 2018-2022 ACS</td>
</tr>
<tr>
<td>svi_novehicle_prcnt</td>
<td>Percentile percentage households with no vehicle available estimate</td>
</tr>
<tr>
<td>svi_novehicle_prcntile</td>
<td>Percentage of households with no vehicle available estimate</td>
</tr>
</tbody>
</table>
</div>
<p></p>

##### Key Reference
<div class="references"> 
<p>Centers for Disease Control and Prevention/ Agency for Toxic Substances and Disease Registry/ Geospatial Research, Analysis, and Services Program. CDC/ATSDR Social Vulnerability Index 2022 Database U.S.. <a href="https://urldefense.com/v3/__https://www.atsdr.cdc.gov/placeandhealth/svi/data_documentation_download.html__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moLlCHA8xQ$">https://www.atsdr.cdc.gov/placeandhealth/svi/data_documentation_download.html</a>.</p>
</div>

## Urban/Rural Area (Census)
##### Measure Description
The Census Bureau’s urban-rural classification is a delineation of geographic areas, identifying both individual urban areas and the rural area of the nation. The Census Bureau’s urban areas represent densely developed territory, and encompass residential, commercial, and other non-residential urban land uses. The Census Bureau delineates urban areas after each decennial census by applying specified criteria to decennial census and other data. Rural encompasses all population, housing, and territory not included within an urban area.

For the 2020 Census, an urban area will comprise a densely settled core of census blocks that meet minimum housing unit density and/or population density requirements. This includes adjacent territory containing non-residential urban land uses. To qualify as an urban area, the territory identified according to criteria must encompass at least 2,000 housing units or have a population of at least 5,000.

##### Key Variables
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</thead>
<tbody>
<tr>
<td>urban_urbanclassification</td>
<td>Urban/Rural Classification 1=urban; 0 not urban; urban cluster label no longer exist;</td>
</tr>
</tbody>
</table>

##### Key Reference
U.S. Census Bureau. (2024, December 16). Urban and rural. U.S. Census Bureau. from [https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural.html](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/urban-rural.html)

## Satellite-based Particulate Measures
##### Measure Description
The Annual Mean PM2.5 Components (EC, NH4, NO3, OC, SO4) 50m Urban and 1km Non-Urban Area Grids for Contiguous U.S., 2019, v1 data set contains annual predictions of the chemical concentrations at a hyper resolution (50m x 50m grid cells) in urban areas and at a high resolution (1km x 1km grid cells) in non-urban areas for the years 2019. Particulate matter with an aerodynamic diameter less than 2.5 microgram per cubic meter (PM2.5) increases mortality and morbidity. The Coordinate Reference System (CRS) for predictions is the World Geodetic System 1984 (WGS84) and the Units for the PM2.5 Components are microgram per cubic meter.

##### Key Variables
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>particulat_ec_mean_yb0</td>
<td>annual average of Elemental Carbon in mcg/m^3</td>
</tr>
<tr>
<td>particulat_nh4_mean_yb0</td>
<td>annual average of Ammonium in mcg/m^3</td>
</tr>
<tr>
<td>particulat_no3_mean_yb0</td>
<td>annual average of Nitrate in mcg/m^3</td>
</tr>
<tr>
<td>particulat_oc_mean_yb0</td>
<td>annual average of Organic Carbon in mcg/m^3</td>
</tr>
<tr>
<td>particulat_so4_mean_yb0</td>
<td>annual average of Sulfate in mcg/m^3</td>
</tr>
</tbody>
</table>

##### Key Reference

<div class="references"> 
<p>Amini, H., Danesh-Yazdi, M., Di, Q., Requia, W., Wei, Y., AbuAwad, Y., Shi, L., Franklin, M., Kang, C., Wolfson, M. J., James, P., Habre, R., Zhu, Q., Apte, J. S., Andersen, Z. J., Xing, X., Hultquist, C., Kloog, I., Dominici, F., … Schwartz, J. (2023). Annual Mean PM2.5 Components (EC, NH4, NO3, OC, SO4) 50m Urban and 1km Non-Urban Area Grids for Contiguous U.S., 2000-2019 v1 (Version 1.00) [Data set]. Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). 
<a href="https://doi.org/10.7927/7WJ3-EN73">https://doi.org/10.7927/7WJ3-EN73 Date Accessed: 2026-01-05</a></p>
</div>

## Population Density (EPA)

##### Measure Description
The spatial distribution of population density in 2020 in 1km resolution, United States

##### Key Variables
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>denspop_density</td>
<td>UN adjusted Population density (people per square mile) in 2020</td>
</tr>
</tbody>
</table>

##### Key Reference
<div class="references"> 
<p>WorldPop. (n.d.). Population density for United States of America. Humanitarian Data Exchange. from <a href="https://urldefense.com/v3/__https://data.humdata.org/dataset/worldpop-population-density-for-united-states-of-america__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moK2awTZ2w$">https://data.humdata.org/dataset/worldpop-population-density-for-united-states-of-america</a></p>
</div>

## Measure of Land Cover and Tree Canopy (NLCD) 
##### Measure Description
The USGS Land Cover program has combined the tried-and-true methodologies from premier land cover projects, National Land Cover Database (NLCD) and Land Change Monitoring, Assessment, and Projection (LCMAP), together with modern innovations in geospatial deep learning technologies to create the next generation of land cover and land change information. These land cover science product algorithms harness the remotely sensed Landsat data record to provide state-of-the-art land surface change information needed by scientists, resource managers, and decision-makers. Annual NLCD uses a modernized, integrated approach to map, monitor, synthesize, and understand the complexities of land use, cover, and condition change. Included in this release is the Annual NLCD, Collection 1.1, for the Conterminous U.S. for 2024. Questions about the Annual NLCD product suite can be directed to the Annual NLCD mapping team at USGS EROS, Sioux Falls, SD (605) 594-6151 or <a href="mailto:custserv@usgs.gov">custserv@usgs.gov</a>. See included spatial metadata for more details.

##### Key Variables
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>nlcd</td>
<td>National Land Cover Database (NLCD)</td>
</tr>
<tr>
<td>tcc</td>
<td>Tree Canopy Cover (TCC)</td>
</tr>
</tbody>
</table>

##### Key Reference
<div class="references"> 
<p>Multi-Resolution Land Characteristics Consortium. (n.d.). MRLC from <a href="https://urldefense.com/v3/__https://www.mrlc.gov/__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moI2jNLjIg$">https://www.mrlc.gov/</a></p>
</div>

## Soil Contamination Measures
### Lithium Concentrations in Groundwater Sources of Drinking Water
##### Measure Description
This data release contains data used to develop models and maps that estimate the occurrence of lithium in groundwater used as drinking water throughout the conterminous United States. The measure is lithium concentration in soil C horizon milligrams per kilogram.

##### Key Variables
<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>gw_li</td>
<td>Lithium concentration in soil C horizon (milligrams per kilogram)</td>
</tr>
</tbody>
</table>

##### Key Reference
<div class="references"> 
<p>Lombard, M. A., Brown, E. E., Saftner, D. M., Arienzo, M. M., Fuller-Thomson, E., Brown, C. J., &amp; Ayotte, J. D. (2024). Estimating Lithium Concentrations in Groundwater Used as Drinking Water for the Conterminous United States. Environmental Science &amp; Technology. <a href="https://urldefense.com/v3/__https://doi.org/10.1021/acs.est.3c03315__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moJu178O7Q$">https://doi.org/10.1021/acs.est.3c03315</a></p>
</div>

### Grid-level Soil Pollution Measures by Toxic Metals 
##### Measure Description
A compilation of a comprehensive global dataset on soil contamination by arsenic, cadmium, cobalt, chromium, copper, nickel and lead, sourced from investigations encompassing sampling locations across various climate zones, geological formations, and land usage patterns. The data measures the probability of exceedance for different toxic metals under Human Health and Ecological Thresholds (HHET) or the Agricultural Thresholds (AT) for each grid.

##### Key Variables

 - `soilpollat{As|Cd|Co|Cr|Cu|Ni|Pb}`
 - `soilpollhhet{As|Cd|Co|Cr|Cu|Ni|Pb}`


 <div id="soilpoll" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Soil Pollution Variables - Full List</span>
  <a class="anchor-link" href="#soilpoll" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">

<table class="table-no-vertical-lines gled">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>soilpoll_hhet_As</td>
<td>probability of exceedance for arsenic (As) under Human Health and Ecological Thresholds for each grid</td>
</tr>
<tr>
<td>soilpoll_hhet_Cd</td>
<td>probability of exceedance for cadmium (Cd) under Human Health and Ecological Thresholds for each grid</td>
</tr>
<tr>
<td>soilpoll_hhet_Co</td>
<td>probability of exceedance for cobalt (Co) under Human Health and Ecological Thresholds for each grid</td>
</tr>
<tr>
<td>soilpoll_hhet_Cr</td>
<td>probability of exceedance for chromium (Cr) under Human Health and Ecological Thresholds for each grid</td>
</tr>
<tr>
<td>soilpoll_hhet_Cu</td>
<td>probability of exceedance for copper (Cu) under Human Health and Ecological Thresholds for each grid</td>
</tr>
<tr>
<td>soilpoll_hhet_Ni</td>
<td>probability of exceedance for nickel (Ni) under Human Health and Ecological Thresholds for each grid</td>
</tr>
<tr>
<td>soilpoll_hhet_Pb</td>
<td>probability of exceedance for lead (Pb) under Human Health and Ecological Thresholds for each grid</td>
</tr>
<tr>
<td>soilpoll_at_As</td>
<td>probability of exceedance for arsenic (As) under Agricultural Thresholds for each grid</td>
</tr>
<tr>
<td>soilpoll_at_Cd</td>
<td>probability of exceedance for cadmium (Cd) under Agricultural Thresholds for each grid</td>
</tr>
<tr>
<td>soilpoll_at_Co</td>
<td>probability of exceedance for cobalt (Co) under Agricultural Thresholds for each grid</td>
</tr>
<tr>
<td>soilpoll_at_Cr</td>
<td>probability of exceedance for chromium (Cr) under Agricultural Thresholds for each grid</td>
</tr>
<tr>
<td>soilpoll_at_Cu</td>
<td>probability of exceedance for copper (Cu) under Agricultural Thresholds for each grid</td>
</tr>
<tr>
<td>soilpoll_at_Ni</td>
<td>probability of exceedance for nickel (Ni) under Agricultural Thresholds for each grid</td>
</tr>
<tr>
<td>soilpoll_at_Pb</td>
<td>probability of exceedance for lead (Pb) under Agricultural Thresholds for each grid</td>
</tr>
</tbody>
</table>
</div>
<p></p>

##### Key Reference
<div class="references"> 
<p>Hou, Deyi; Jia, Xiyue; Wang, Liuwei et al. (2025). Data from: Global soil pollution by toxic metals threatens agriculture and human health [Dataset]. Dryad. <a href="https://urldefense.com/v3/__https://doi.org/10.5061/dryad.83bk3jb2z__;!!Mih3wA!EpVTB9LMtTc2M41bAhf1JjoFfZ5Dr9N1J7o2i7kVRkIuAyvSy9ILZwGp0ZJHJ-fdgvZiZ5Z9Tge3moJPz-LwVg$">https://doi.org/10.5061/dryad.83bk3jb2z</a></p>
</div>