<p style="font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION TO BE ADDED FOR R2.0</i></p>


<i style="color: red;">Administrative notes:<br>
 - <a href="https://drive.google.com/open?id=114NYqSe--744iuNJ3hZCsA2tmIaAB-ku">Data dictionary shared by Chun</a>: geocoded variables given the address history<br>
 - who can give more information on what the data look like?<br>
  - figure out what domain will be - currently under SED, but might be its own domain LED<br>
</i></p>

# led



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

<div id="concat" class="static-banner" style="background-color: #dcd8fb; border-left: 5px solid #b5aef2;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
    <span class="text">Concatenated Data (<code>genetics/</code>)</span>
    <a class="anchor-link" href="#concat" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
</div>
<div class="notification-static-content" style="border-left: 5px solid #b5aef2;">
  <p>The GLED data in the current release include variables linked to the residential address history of the child for visit V01 (prenatal period up to 1 year before EDD). The dataset is provided as <a href="../../../datacuration/file-based-data/#concatenated-data">concatenated data</a> (<i>see the <a href="../../../datacuration/overview" target="_blank">Data Structure Overview</a> for additional details</i>) under 
    <code>geocoded_linkage/</code>:</p>
  <pre class="folder-tree">
hbcd/
|__ concatenated/ 
    |__ geocoded-linkage/
        |__ ADD FILENAMES
</pre>
</div>

## Details

Brain development is shaped not only by biological factors, but also by the environments in which children live and grow. To capture these influences, the HBCD Study incorporates **Geocoded Linked External Data (GLED)**, connecting participants’ residential and care place addresses to external datasets. GLED enables estimation of participants’ cumulative exposure to environmental and socioeconomic factors, providing measures of social, economic, and environmental context that may help explain individual differences in development ([Fan et al. 2021](https://doi.org/10.1016/j.dcn.2021.101030)).

*Administration:* The Birth Parent or Primary Caregiver provides residential address history of the child to HBCD Study staff (in person or remote) for all visits. Completion time (5-15 minutes).

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
<thead>
  <th>Subdomain</th>
  <th>Linked Measure</th>
  <th style="text-align: center;">Documentation</th>
</thead>
<tbody>
<tr>
<td>Air Pollution</td>
<td>Satellite-based Particulate Measures (Air Quality Data for Health-Related Applications)</td>
<td style="text-align: center;"><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_particulat" target="_blank"><i style="font-size: 0.8em;" class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
<td colspan="1" rowspan="4">Amenities & Services</td>
<td>Neighborhood Socioeconomic Status and Demographics (NaNDA)</td>
<td style="text-align: center;"><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_nbhsoc" target="_blank"><i style="font-size: 0.8em;" class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
<td>Parks (NaNDA)</td>
<td style="text-align: center;"><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_parks" target="_blank"><i style="font-size: 0.8em;" class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
<td>Religious/Civic Organizations (NaNDA)</td>
<td style="text-align: center;"><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_relciv" target="_blank"><i style="font-size: 0.8em;" class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
</tr>
<tr>
<td>Social Service (NaNDA)</td>
</tr>
<tr>
<td colspan="1" rowspan="5">
<div>Built Environment</div>
</td>
<td>Building Density (EPA)</td>
</tr>
<tr>
<td>Population Density (EPA)</td>
</tr>
<tr>
<td>Vehicle Density (ACS)</td>
</tr>
<tr>
<td>Urban/Rural Area (Census)</td>
</tr>
<tr>
<td>Walkability (EPA)</td>
</tr>
<tr>
<td>Community Health Burden</td>
<td>Behavioral Health Measures (PLACES)</td>
</tr>
<tr>
<td>Natural Space and Satellite</td>
<td>Measure of Land Cover and Tree Canopy (NLCD)</td>
</tr>
<tr>
<td colspan="1" rowspan="4">
<div>Neighborhood Social Factors</div>
</td>
<td>Census Return (Anomie/Disenfranchisement/Social Capital)</td>
</tr>
<tr>
<td>Number of Jobs and Job Density (LODES)</td>
</tr>
<tr>
<td>Rent and Mortgage Statistics (ACS)</td>
</tr>
<tr>
<td>Social Mobility (Opportunity Atlas)</td>
</tr>
<tr>
<td colspan="1" rowspan="4">
<div>Neighhorhood Composite Measures</div>
</td>
<td>Area Deprivation Index (ADI)</td>
</tr>
<tr>
<td>Child Opportunity Index 2.0 (COI)</td>
</tr>
<tr>
<td>Minority Health Social Vulnerability Index (MHSVI)</td>
</tr>
<tr>
<td>Social Vulnerability Index (SVI)</td>
</tr>
</tbody>
</table>

## Quality Control

Quality control procedures includes the following:
<ul>
  <li>The input addresses from the address history form are first checked to see if they fall into correct geographical boundaries of the catchment area.</li>
  <li>The address history completedness is check if the recorded address for a given participant can gaplessly tracing back to one year before child's EDD.</li>
  <li>The addresses are geocoded and checked if the conversions are success or not</li>
</ul>

## References

<div class="references"> 
<p>Fan, C. C., Marshall, A., Smolker, H., Gonzalez, M. R., Tapert, S. F., Barch, D. M., Sowell, E., Dowling, G. J., Cardenas-Iniguez, C., Ross, J., Thompson, W. K., & Herting, M. M. (2021). Adolescent Brain Cognitive Development (ABCD) study Linked External Data (LED): Protocol and practices for geocoding and assignment of environmental data. <i>Developmental Cognitive Neuroscience</i> , 52(101030), 101030. <a href="https://doi.org/10.1016/j.dcn.2021.101030">https://doi.org/10.1016/j.dcn.2021.101030</a></p>  
</div>

<br>

