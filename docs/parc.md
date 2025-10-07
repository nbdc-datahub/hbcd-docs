# Atlases

<div id="parc" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dde6fe;">
  <span class="emoji"><i class="fa-solid fa-book-atlas"></i></span>
  <span class="text-with-link">
<span class="text">Parcellation Atlases</span>
  <a class="anchor-link" href="#parc" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <th>Cortical/<br>Subcortical</th>
  <th>Atlas</th>
  <th>Description</th>
</thead>
<tbody>
<tr>
  <td rowspan="4">Cortical</td>
  <td>Glasser</td>
  <td style="word-wrap: break-word; white-space: normal;">Recommended for population-level anatomical maps (<a href="https://doi.org/10.1038/nature18933">Glasser et al., 2016</a>).</td>
</tr>
<tr>
  <td>Gordon</td>
  <td style="word-wrap: break-word; white-space: normal;">Gordon's 333 ROI template, parcellated using boundary detection on rs-fMRI data from 120 young adults with 14 minutes of data collected on average (<a href="https://doi.org/10.1093/cercor/bhu239">Gordon et al. 2016</a>). Recommended for population-level functional network maps.</td>
</tr>
<tr>
  <td>MIDB</td>
  <td style="word-wrap: break-word; white-space: normal;">MIDB precision brain atlas derived from ABCD data and thresholded at 75% probability (<a href="https://doi.org/10.1038/s41593-024-01596-5">Hermosillo et al., 2024</a>). Recommended for individualized functional network maps.</td>
</tr>
<tr>
<td>Myers Labonte</td>
<td style="word-wrap: break-word; white-space: normal;">Myers-Labonte infant probabilistic atlas thresholded at 50% probability (<a href="https://doi.org/10.1101/2023.11.10.566629" target="_blank">Meyers et al., 2023</a>)</td>
</tr>
<tr>
  <td rowspan="2">Subcortical</td>
  <td>HCP</td>
  <td style="word-wrap: break-word; white-space: normal;">HCP's 360 ROI template, parcellated from mutli-modal task, rest, and diffusion MRI data on 210 young adults (<a href="https://doi.org/10.1016/j.neuroimage.2013.04.127">Glasser et al., 2013</a>).</td>
</tr>
<tr>
  <td>Tian</td>
  <td>(<a href="https://doi.org/10.1038/s41593-020-00711-6">Tian et al., 2020</a>).</td>
</tr>
<tr>
  <td>Cortical+<br>Subcortical</td>
  <td style="word-wrap: break-word; white-space: normal;">4S Atlas</td>
  <td style="word-wrap: break-word; white-space: normal;">The 4S (Schaefer Supplemented with Subcortical Structures) atlas combines the <a href="https://doi.org/10.1093/cercor/bhx179">Schaefer 2018</a> cortical atlas (version v0143) at 10 different resolutions (100, 200, 300, 400, 500, 600, 700, 800, 900, and 1000 parcels) with the CIT168 subcortical atlas (<a href="https://doi.org/10.1038/sdata.2018.63">Pauli et al. 2018</a>), the Diedrichson cerebellar atlas (<a href="https://doi.org/10.1038/s41593-019-0436-x">King et al., 2019</a>), the HCP thalamic atlas (<a href="https://doi.org/10.1038/sdata.2018.270">Najdenovska et al., 2018</a>), and the amygdala and hippocampus parcels from the HCP CIFTI subcortical parcellation (<a href="https://doi.org/10.1016/j.neuroimage.2013.04.127">Glasser et al., 2013</a>). The 4S atlas is used in the same manner across three PennLINC BIDS Apps: XCP-D, QSIPrep, and ASLPrep, to produce synchronized outputs across modalities. For details: <a href="https://github.com/PennLINC/AtlasPack">https://github.com/PennLINC/AtlasPack</a>.</td>
</tr>
</tbody>
</table>
</div>