<i style="color: red;">Administrative notes:<br>
 - <a href="https://drive.google.com/open?id=114NYqSe--744iuNJ3hZCsA2tmIaAB-ku">Data dictionary shared by Chun</a>: geocoded variables given the address history<br>
- some measures in ABCD documentation have data and responsible use warnings - should these be included for HBCD as well? eg: <a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_nbhsoc">NaNDa</a> - Chun says that these can be left out for HBCD for now<br>
- Per Chun, "geocoded linkage measure data were deliberately designed to be compatible with ABCD, but with appropriate year updates (many of ABCD variables tracing back to 2010 census, but HBCD is updated to 2020 census)." for documentation, we could: (1) just link to ABCD documentation as the draft does and make a qualifying statement above the table about year updates. (2) could add specific modifications made for HBCD compared to ABCD documentation as a separate column of the table. (3) add to a "HBCD Modificaations" section as we do for other measures</p>
</i></p>

# Linked External Data

**Geocoded Linked External Data (GLED) - Residential Address History** connects participants’ residential and care place addresses to external datasets. The data is computed for all visits (V01-V06); the current release contains data for visit V01 (including prenatal period up to 1 year before EDD).

## Release Data

<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Responsible Use Warning</span>
  <a class="anchor-link" href="#alert" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p>The geocoded variables should be considered as proxies for the exposure. Therefore, it is an estimates of the risk, which can differ from what is actually experienced by a given individual. In addition, researchers should not use any geospatial information to identify the actual geographical location.</p>
</div>

The GLED data in the current release include variables linked to the residential address history of the child for visit V01 (prenatal period up to 1 year before EDD). The dataset is provided as <a href="../../../datacuration/file-based-data/#concatenated-data">concatenated data</a> (<i>see <a href="../../../datacuration/overview" target="_blank">Data Structure Overview</a> for additional details</i>) under <code>geocoded_linkage/</code>:

<pre class="folder-tree">
hbcd/
|__ concatenated/ 
    |__ geocoding/
        |__ HBCD_address_history_geocoded_filtered.csv
</pre>

## Details

**Geocoded Linked External Data (GLED)** are external datasets linked to participants’ residential addresses. They serve as proxy measures of cumulative social, economic, and environmental contexts that may help explain individual differences in development ([Fan et al. 2021](https://doi.org/10.1016/j.dcn.2021.101030)). At each study visit, the Birth Parent or Primary Caregiver reports the child’s residential address history. Study staff collect this information in person or remotely (completion time: 5–15 minutes).

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
  <th>Measure</th>
  <th>Relevant Variable Names</th>
  <th>Link</th>
</tr>
</thead>
<tbody>
<!-- Air Pollution -->
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>AIR POLLUTION</b></td>
</tr>
<tr>
  <td>Satellite-based Particulate Measures</td>
  <td><code>particulate_{ec|oc|nh4|no3|so4}_mean_yb0</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_particulat" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<!-- Soil Pollution -->
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>SOIL POLLUTION</b></td>
</tr>
<tr>
  <td>Soil Contamination Meaasures</td>
  <td><code>soilpoll_{at|hhet}_{As|Cd|Co|Cu|Ni|Pb}</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_leadrisk" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<!-- Amenities & Services -->
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>AMENITIES & SERVICES</b></td>
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
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>BUILT ENVIRONMENT</b></td>
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
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>COMMUNITY HEALTH BURDEN</b></td>
</tr>
<tr>
  <td>Behavioral Health Measures (PLACES)</td>
  <td><code>places_*_preval</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_places" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>

<!-- Natural Space and Satellite -->
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>NATURAL SPACE & SATELLITE</b></td>
</tr>
<tr>
  <td>Measure of Land Cover and Tree Canopy (NLCD)</td>
  <td><code>nlcd</code></td>
  <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_nlcd" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<!-- Neighborhood Social Factors -->
<tr>
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>NEIGHBORHOOD SOCIAL FACTORS</b></td>
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
  <td colspan="3" style="font-size: 0.8em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>NEIGHBORHOOD COMPOSITE MEASURES</b></td>
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

## Quality Control

Quality control procedures involve several steps. First, input addresses from the address history form are verified to ensure they fall within the correct geographical boundaries of the catchment area. Next, the completeness of the address history is evaluated to confirm that the recorded addresses trace back continuously to at least one year before the child’s estimated due date (EDD). Finally, the addresses are geocoded, and the success of these conversions is checked to ensure accurate linkage.

## References

<div class="references"> 
<p>Fan, C. C., Marshall, A., Smolker, H., Gonzalez, M. R., Tapert, S. F., Barch, D. M., Sowell, E., Dowling, G. J., Cardenas-Iniguez, C., Ross, J., Thompson, W. K., & Herting, M. M. (2021). Adolescent Brain Cognitive Development (ABCD) study Linked External Data (LED): Protocol and practices for geocoding and assignment of environmental data. <i>Developmental Cognitive Neuroscience</i> , 52(101030), 101030. <a href="https://doi.org/10.1016/j.dcn.2021.101030">https://doi.org/10.1016/j.dcn.2021.101030</a></p>  
</div>

<br>
