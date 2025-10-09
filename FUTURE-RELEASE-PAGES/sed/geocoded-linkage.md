<p style="font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION TO BE ADDED FOR R2.0</i></p>


<i style="color: red;">Administrative notes:<br>
- original form responses are <a href="../GLED-alt">here</a> - page below has been reorganized to follow format of concat data pages and filled with more info from external sources<br>
 - <a href="https://drive.google.com/open?id=114NYqSe--744iuNJ3hZCsA2tmIaAB-ku">Data dictionary shared by Chun</a>: geocoded variables given the address history<br>
 - who can give more information on what the data look like?<br>
- figure out what domain will be - currently under SED, but might be its own domain LED<br>
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

<div id="concat" class="static-banner" style="background-color: #dcd8fb; border-left: 5px solid #b5aef2;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
    <span class="text">Concatenated Data (<code>geocoded-linkage/</code>)</span>
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

**Geocoded Linked External Data (GLED)** are external datasets linked to participants’ residential addresses. They serve as proxy measures of cumulative social, economic, and environmental contexts that may help explain individual differences in development ([Fan et al. 2021](https://doi.org/10.1016/j.dcn.2021.101030)). At each study visit, the Birth Parent or Primary Caregiver reports the child’s residential address history. Study staff collect this information in person or remotely (completion time: 5–15 minutes).

<table class="expandable-table">
  <colgroup>
    <col style="width: 100%;">
    <col style="width: 50%;">
  </colgroup>
  <tbody>
  <tr>
  <td colspan="2" style="word-wrap: break-word; white-space: normal; font-size: 15px; background-color: ;">
  <i>Expand the subdomains below to view linked external data measures included in HBCD Study data (and <a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_particulat" target="_blank"><i style="font-size: 0.8em;" class="fa-solid fa-arrow-up-right-from-square"></i></a> to be directed to detailed measure documentation available on the ABCD Data Documentation site).</i>
  </td>
  </tr>
    <!-- Air Pollution -->
    <tr onclick="toggleRows('airpollution')" class="group-header">
      <td colspan="2"><i class="fa-solid fa-caret-right"></i> Air Pollution</td>
    </tr>
    <tr class="airpollution child-row" style="display:none;">
      <td style="padding-left: 40px;">Satellite-based Particulate Measures (Air Quality Data for Health-Related Applications)</td>
      <td>
        <a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_particulat" target="_blank">
          <i class="fa-solid fa-arrow-up-right-from-square"></i>
        </a>
      </td>
    </tr>
    <!-- Amenities & Services -->
    <tr onclick="toggleRows('amenities')" class="group-header">
      <td colspan="2"><i class="fa-solid fa-caret-right"></i> Amenities & Services</td>
    </tr>
    <tr class="amenities child-row" style="display:none;">
      <td style="padding-left: 40px;">Neighborhood Socioeconomic Status and Demographics (NaNDA)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_nbhsoc" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <tr class="amenities child-row" style="display:none;">
      <td style="padding-left: 40px;">Parks (NaNDA)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_parks" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <tr class="amenities child-row" style="display:none;">
      <td style="padding-left: 40px;">Religious/Civic Organizations (NaNDA)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_relciv" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <tr class="amenities child-row" style="display:none;">
      <td style="padding-left: 40px;">Social Service (NaNDA)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_socsrv" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <!-- Built Environment -->
    <tr onclick="toggleRows('built')" class="group-header">
      <td colspan="2"><i class="fa-solid fa-caret-right"></i> Built Environment</td>
    </tr>
    <tr class="built child-row" style="display:none;">
      <td style="padding-left: 40px;">Building Density (EPA)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_densbld" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <tr class="built child-row" style="display:none;">
      <td style="padding-left: 40px;">Population Density (EPA)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_denspop" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <tr class="built child-row" style="display:none;">
      <td style="padding-left: 40px;">Vehicle Density (ACS)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_densveh" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <tr class="built child-row" style="display:none;">
      <td style="padding-left: 40px;">Urban/Rural Area (Census)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_urban" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <tr class="built child-row" style="display:none;">
      <td style="padding-left: 40px;">Walkability (EPA)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_walk" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <!-- Community Health Burden -->
    <tr onclick="toggleRows('healthburden')" class="group-header">
      <td colspan="2"><i class="fa-solid fa-caret-right"></i> Community Health Burden</td>
    </tr>
    <tr class="healthburden child-row" style="display:none;">
      <td style="padding-left: 40px;">Behavioral Health Measures (PLACES)</td>
      <td>
        <a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_places" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a>
      </td>
    </tr>
    <!-- Natural Space and Satellite -->
    <tr onclick="toggleRows('naturalspace')" class="group-header">
      <td colspan="2"><i class="fa-solid fa-caret-right"></i> Natural Space and Satellite</td>
    </tr>
    <tr class="naturalspace child-row" style="display:none;">
      <td style="padding-left: 40px;">Measure of Land Cover and Tree Canopy (NLCD)</td>
      <td>
        <a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_nlcd" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a>
      </td>
    </tr>
    <!-- Neighborhood Social Factors -->
    <tr onclick="toggleRows('social')" class="group-header">
      <td colspan="2"><i class="fa-solid fa-caret-right"></i> Neighborhood Social Factors</td>
    </tr>
    <tr class="social child-row" style="display:none;">
      <td style="padding-left: 40px;">Census Return (Anomie/Disenfranchisement/Social Capital)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_censusret" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <tr class="social child-row" style="display:none;">
      <td style="padding-left: 40px;">Number of Jobs and Job Density (LODES)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_lodes" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <tr class="social child-row" style="display:none;">
      <td style="padding-left: 40px;">Rent and Mortgage Statistics (ACS)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_rentmort" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <tr class="social child-row" style="display:none;">
      <td style="padding-left: 40px;">Social Mobility (Opportunity Atlas)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_socmob" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <!-- Neighborhood Composite Measures -->
    <tr onclick="toggleRows('composite')" class="group-header">
      <td colspan="2"><i class="fa-solid fa-caret-right"></i> Neighborhood Composite Measures</td>
    </tr>
    <tr class="composite child-row" style="display:none;">
      <td style="padding-left: 40px;">Area Deprivation Index (ADI)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_adi" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <tr class="composite child-row" style="display:none;">
      <td style="padding-left: 40px;">Child Opportunity Index 2.0 (COI)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_coi" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <tr class="composite child-row" style="display:none;">
      <td style="padding-left: 40px;">Minority Health Social Vulnerability Index (MHSVI)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_ssvi" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
    <tr class="composite child-row" style="display:none;">
      <td style="padding-left: 40px;">Social Vulnerability Index (SVI)</td>
      <td><a href="https://docs.abcdstudy.org/latest/documentation/non_imaging/le.html#le_l_svi" target="_blank"><i class="fa-solid fa-arrow-up-right-from-square"></i></a></td>
    </tr>
  </tbody>
</table>
<script>
function toggleRows(group) {
  const rows = document.querySelectorAll("." + group);
  const headerIcon = document.querySelector(`tr[onclick*="${group}"] i`);
  const isHidden = [...rows].every(row => row.style.display === "none");
  rows.forEach(row => row.style.display = isHidden ? "table-row" : "none");
  headerIcon.classList.toggle("fa-caret-right", !isHidden);
  headerIcon.classList.toggle("fa-caret-down", isHidden);
}
</script>

## Quality Control

Quality control procedures involve several steps. First, input addresses from the address history form are verified to ensure they fall within the correct geographical boundaries of the catchment area. Next, the completeness of the address history is evaluated to confirm that the recorded addresses trace back continuously to at least one year before the child’s estimated due date (EDD). Finally, the addresses are geocoded, and the success of these conversions is checked to ensure accurate linkage.

## References

<div class="references"> 
<p>Fan, C. C., Marshall, A., Smolker, H., Gonzalez, M. R., Tapert, S. F., Barch, D. M., Sowell, E., Dowling, G. J., Cardenas-Iniguez, C., Ross, J., Thompson, W. K., & Herting, M. M. (2021). Adolescent Brain Cognitive Development (ABCD) study Linked External Data (LED): Protocol and practices for geocoding and assignment of environmental data. <i>Developmental Cognitive Neuroscience</i> , 52(101030), 101030. <a href="https://doi.org/10.1016/j.dcn.2021.101030">https://doi.org/10.1016/j.dcn.2021.101030</a></p>  
</div>

<br>
