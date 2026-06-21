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

The GLED data in the current release include variables linked to the residential address history of the child for visit V01 (prenatal period up to 1 year before EDD). The dataset is provided as <a href="../../../datacuration/file-based-data/#concatenated-data">concatenated data</a>:

#### Geocoded Linkage Measures
<div class="banner">
  <span class="emoji"><i class="fa-solid fa-table"></i></span>
  <span class="text">See <a href="../gled-dd.html" target="_blank">supplemental table</a> for full descriptions of each variable.</span>
</div>
<p></p>
<table class="compact-table-no-vertical-lines" style="font-size: 15px;">
<thead>
<tr>
  <th>Measure By Domain</th>
  <th>Relevant Variables</th>
  <th>Link</th>
</tr>
</thead>
<tbody>
<!-- Air Pollution -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>AIR POLLUTION</b></td>
</tr>
<tr>
  <td>Satellite-based Particulate Measures</td>
  <td><code>particulate_{ec|oc|nh4|no3|so4}_mean_yb0</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_particulat" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<!-- Soil Pollution -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>SOIL POLLUTION</b></td>
</tr>
<tr>
  <td>Soil Contamination Measures</td>
  <td><code>soilpoll_{at|hhet}_{As|Cd|Co|Cu|Ni|Pb}</code>; <code>gw_li</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_leadrisk" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<!-- Amenities & Services -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>AMENITIES & SERVICES</b></td>
</tr>
<tr>
  <td>Neighborhood Socioeconomic Status and Demographics</td>
  <td><code>nbhsoc_{forborn|college|finc*|unemploy|factor*}_prop</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_nbhsoc" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Parks</td>
  <td><code>parks_{parks*}_count</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_parks" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Religious/Civic Organizations</td>
  <td><code>relciv_{civsoc*|relorg*}_{count|prop}</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_relciv" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Social Service</td>
  <td><code>socsrv_socsrv*_{count|prop}</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_socsrv" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<!-- Built Environment -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>BUILT ENVIRONMENT</b></td>
</tr>
<tr>
  <td>Building Density (EPA)</td>
  <td><code>densbld_density</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_densbld" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Population Density (EPA)</td>
  <td><code>denspop_density</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_denspop" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Vehicle Density (ACS)</td>
  <td><code>densveh_{area|pop}_density</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_densveh" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Urban/Rural Area (Census)</td>
  <td><code>urban_urbanclassification</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_urban" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Walkability (EPA)</td>
  <td><code>walk_idx</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_walk" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<!-- Community Health Burden -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>COMMUNITY HEALTH BURDEN</b></td>
</tr>
<tr>
  <td>Behavioral Health Measures (PLACES)</td>
  <td><code>places_*_preval</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_places" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<!-- Natural Space and Satellite -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>NATURAL SPACE & SATELLITE</b></td>
</tr>
<tr>
  <td>Measure of Land Cover and Tree Canopy (NLCD)</td>
  <td><code>nlcd</code>; <code>tcc</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_nlcd" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<!-- Neighborhood Social Factors -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>NEIGHBORHOOD SOCIAL FACTORS</b></td>
<tr>
  <td>Census Return (Anomie/Disenfranchisement/Social Capital)</td>
  <td><code>censusret_*</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_censusret" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Number of Jobs and Job Density (LODES)</td>
  <td><code>lodes_job*_{count|density}</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_lodes" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Rent and Mortgage Statistics (ACS)</td>
  <td><code>rentmort_*</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_rentmort" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Social Mobility (Opportunity Atlas)</td>
  <td><code>socmob_kfrpp_{count|mean|p*_percentile|se}</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_socmob" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<!-- Neighborhood Composite Measures -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>NEIGHBORHOOD COMPOSITE MEASURES</b></td>
<tr>
<tr>
  <td>Area Deprivation Index (ADI)</td>
  <td><code>adi_national_prcnt</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_adi" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Child Opportunity Index 2.0 (COI)</td>
  <td><code>coi_{coi|ed|he|se}_total_{metro|national|state}</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_coi" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Minority Health Social Vulnerability Index (MHSVI)</td>
  <td><code>ssvi_*_prcnt</code>; <code>ssvi_*_state_prop</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_ssvi" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Social Vulnerability Index (SVI)</td>
  <td><code>ssvi_*_{prcnt|prcntile}</code>; <code>ssvi_*_state_prop</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_svi" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
  </tbody>
</table>

## References

<div class="references"> 
<p>Fan, C. C., Marshall, A., Smolker, H., Gonzalez, M. R., Tapert, S. F., Barch, D. M., Sowell, E., Dowling, G. J., Cardenas-Iniguez, C., Ross, J., Thompson, W. K., & Herting, M. M. (2021). Adolescent Brain Cognitive Development (ABCD) study Linked External Data (LED): Protocol and practices for geocoding and assignment of environmental data. <i>Developmental Cognitive Neuroscience</i> , 52(101030), 101030. <a href="https://doi.org/10.1016/j.dcn.2021.101030">https://doi.org/10.1016/j.dcn.2021.101030</a></p>  
</div>

<br>
