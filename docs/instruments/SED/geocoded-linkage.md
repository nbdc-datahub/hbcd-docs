<!-- ADMIN NOTE: INCLUDES HARDCODED TABLE -->

# Linked External Data

{{ readme_summary(instruments.gled) }}
{{ alert_warning(instruments.gled) }}
{{ data_warning(instruments.gled) }}
{{ issues_banner() }}

---

## Instrument Details

{{ instrument_description(instruments.gled) }}

##### Geocoded Linkage Measures

<div class="banner">
  <span class="emoji"><i class="fa-solid fa-table"></i></span>
  <span class="text">Links to <a href="../GLED-measures/">LED measure details</a> are provided in the table below. Also see <a href="../gled-dd.html">supplemental table</a>.</span>
</div>
<p></p>


<table class="compact-table-no-vertical-lines">
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
  <td><a href="../GLED-measures/#satellite-based-particulate-measures"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<!-- Soil Pollution -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>SOIL POLLUTION</b></td>
</tr>
<tr>
  <td>Soil Contamination Measures</td>
  <td><code>soilpoll_{at|hhet}_{As|Cd|Co|Cu|Ni|Pb}</code>; <code>gw_li</code></td>
  <td><a href="../GLED-measures/#grid-level-soil-pollution-measures-by-toxic-metals"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<!-- Amenities & Services -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>AMENITIES & SERVICES</b></td>
</tr>
<tr>
  <td>Neighborhood Socioeconomic Status and Demographics</td>
  <td><code>nbhsoc_{forborn|college|finc*|unemploy|factor*}_prop</code></td>
    <td><a href="../GLED-measures/#neighborhood-socioeconomic-status-and-demographics-nanda"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Parks</td>
  <td><code>parks_{parks*}_count</code></td>
  <td><a href="../GLED-measures/#parks-nanda"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Religious/Civic Organizations</td>
  <td><code>relciv_{civsoc*|relorg*}_{count|prop}</code></td>
  <td><a href="../GLED-measures/#religiouscivic-organizations-nanda"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Social Service</td>
  <td><code>socsrv_socsrv*_{count|prop}</code></td>
  <td><a href="../GLED-measures/#social-service-nanda"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<!-- Built Environment -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>BUILT ENVIRONMENT</b></td>
</tr>
<tr>
  <td>Building Density (EPA)</td>
  <td><code>densbld_density</code></td>
    <td><a href="../GLED-measures/#building-density-epa"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Population Density (EPA)</td>
  <td><code>denspop_density</code></td>
  <td><a href="../GLED-measures/#population-density-epa"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Vehicle Density (ACS)</td>
  <td><code>densveh_{area|pop}_density</code></td>
    <td><a href="../GLED-measures/#vehicle-density-acs"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
</tr>
<tr>
  <td>Urban/Rural Area (Census)</td>
  <td><code>urban_urbanclassification</code></td>
  <td><a href="../GLED-measures/#urbanrural-area-census"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
<tr>
  <td>Walkability (EPA)</td>
  <td><code>walk_idx</code></td>
  <td><a href="../GLED-measures/#walkability-epa"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
<!-- Community Health Burden -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>COMMUNITY HEALTH BURDEN</b></td>
</tr>
<tr>
  <td>Behavioral Health Measures (PLACES)</td>
  <td><code>places_*_preval</code></td>
  <td><a href="../GLED-measures/#behavioral-health-measures-places"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
<!-- Natural Space and Satellite -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>NATURAL SPACE & SATELLITE</b></td>
</tr>
<tr>
  <td>Measure of Land Cover and Tree Canopy (NLCD)</td>
  <td><code>nlcd</code>; <code>tcc</code></td>
  <td><a href="../GLED-measures/#measure-of-land-cover-and-tree-canopy-nlcd"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
<!-- Neighborhood Social Factors -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>NEIGHBORHOOD SOCIAL FACTORS</b></td>
<tr>
  <td>Census Return (Anomie/Disenfranchisement/Social Capital)</td>
  <td><code>censusret_*</code></td>
  <td><a href="../GLED-measures/#census-return"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
<tr>
  <td>Number of Jobs and Job Density (LODES)</td>
  <td><code>lodes_job*_{count|density}</code></td>
  <td><a href="../GLED-measures/#number-of-jobs-and-job-density-lodes"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>

<tr>
  <td>Rent and Mortgage Statistics (ACS)</td>
  <td><code>rentmort_*</code></td>
  <td><a href="../GLED-measures/#rent-and-mortgage-statistics-acs"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>

<tr>
  <td>Social Mobility (Opportunity Atlas)</td>
  <td><code>socmob_kfrpp_{count|mean|p*_percentile|se}</code></td>
  <td><a href="../GLED-measures/#social-mobility-opportunity-atlas"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>

<!-- Neighborhood Composite Measures -->
<tr>
  <td colspan="3" style="font-size: 0.9em; line-height: 1.0; color: #00819bff; background-color: #ebf8fa57;"><b>NEIGHBORHOOD COMPOSITE MEASURES</b></td>
<tr>
<tr>
  <td>Area Deprivation Index (ADI)</td>
  <td><code>adi_national_prcnt</code></td>
  <td><a href="../GLED-measures/#area-deprivation-index-adi"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Child Opportunity Index 2.0 (COI)</td>
  <td><code>coi_{coi|ed|he|se}_total_{metro|national|state}</code></td>
  <td><a href="../GLED-measures/#child-opportunity-index-30-coi"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Minority Health Social Vulnerability Index (MHSVI)</td>
  <td><code>ssvi_*_prcnt</code>; <code>ssvi_*_state_prop</code></td>
  <td><a href="../GLED-measures/#minority-health-social-vulnerability-index-mhsvi"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
  <td>Social Vulnerability Index (SVI)</td>
  <td><code>ssvi_*_{prcnt|prcntile}</code>; <code>ssvi_*_state_prop</code></td>
  <td><a href="../GLED-measures/#social-vulnerability-index-svi"
  target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
  </tbody>
</table>

{{ references(instruments.gled) }}





<!-- ### Release Data

The GLED dataset is provided as <a href="../../../datacuration/file-based-data/#concatenated-data">concatenated data</a>:


<code>
hbcd/
└── concatenated/ 
    └── geocoding/
        └── HBCD_address_history_geocoded_filtered.csv
</code> -->
