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

<span style="color: red; font-size: 1.3em;"> <b>ADMIN NOTE:</b> <a style="color: red;" href="../HBCD-LED-DD.html" target="_blank">ADD HBCD-SPECIFIC DOCUMENTATION</a></span>

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
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Race: White, Alone; LODES; census tract</td>
</tr>
<tr>
<td>lodes_jobblack_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Race: Black or African American Alone; LODES; census tract</td>
</tr>
<tr>
<td>lodes_jobaian_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Race: American Indian or Alaska Native Alone; LODES; census tract</td>
</tr>
<tr>
<td>lodes_jobasian_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Race: Asian Alone; LODES; census tract</td>
</tr>
<tr>
<td>lodes_jobnhpi_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Race: Native Hawaiian or Other Pacific Islander Alone; LODES; census tract</td>
</tr>
<tr>
<td>lodes_jobmulti_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Race: Two or More Race Groups; LODES; census tract</td>
</tr>
<tr>
<td>lodes_jobnonhisp_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Ethnicity: Not Hispanic or Latino; LODES; census tract</td>
</tr>
<tr>
<td>lodes_jobhisp_density</td>
<td>Residential history derived - Density of jobs (per sq. mile of land area) for workers with Ethnicity: Hispanic or Latino; LODES; census tract</td>
</tr>
</tbody>
</table>
</div>
<p></p>

##### Key References
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

##### Key References
<div class="references"> 
<p>U.S. Department of Health & Human Services, Office of Minority Health. (n.d.). Minority Health Index. Retrieved from <a href="https://minorityhealth.hhs.gov/minority-health-index">https://minorityhealth.hhs.gov/minority-health-index</a>.</p>  
</div>

## Neighborhood Socioeconomic Status and Demographics (NaNDA)


