# FROM RELEASE 1.0 extra text 

## Diffusion MRI: Selecting Best DWI Scans
If there were multiple DWI scans available that passed QC, only the best quality scan was selected for processing based on additional QC metrics. For subjects with manual QC scores for all DWI images in a session (only a portion of data was selected for manual QC), to choose the best scan, the following metrics, in order of priority, were used to compare scan quality until the best was identified: `NumHeadCoilElem`, `QU_cotuff`, `QU_sus`, `QU_line`, `ngood_frames`, `line_mean_score`, and `tSNR_b0`. In the absence of manual QC metrics, the following were prioritized to select the best scan: `NumHeadCoilElem`, `ngood_frames`, `line_mean_score`, and `tSNR_b0`. These metrics are defined in the following table:

<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tfoot><tr><td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;" colspan="3"><b>**</b><i>Available for Siemens only: There are some visits on Siemens scanners with one or more scans for which some of the head coil elements were disabled (following detachment and reattachment of the anterior coil elements). In very rare cases, the site may recognize the problem at the time and reacquire the images. In cases like that, the scan with higher "NumHeadCoilElem” would be preferred.</i></td></tr></tfoot>
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">QC Metric</th>
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Defnition</th>  
      <th style="border: 1px solid #ddd; padding: 8px; text-align: left;">Scoring</th>   
    </tr>
  </thead>
<tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">QC</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Overall manual QC score of 1 (pass) or 0 (fail)</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">1 (pass) or 0 (fail)</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NumHeadCoilElem**</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Number of head coil elements</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NA</td>
  </tr>  
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">QU_cotuff</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Qualitative manual QC score for FOV cutoff artifact</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">0 = absent ; 1 = mild; 2 = moderate; 3 = severe </td>
  </tr>  
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">QU_sus</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Qualitative manual QC score for susceptibility artifact</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">0 = absent ; 1 = mild; 2 = moderate; 3 = severe </td>
  </tr>  
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">QU_line</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Qualitative manual QC score for line artifact</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">0 = absent ; 1 = mild; 2 = moderate; 3 = severe </td>
  </tr>  
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">ngood_frames</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Number of frames without outlier slices for dMRI</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NA</td>
  </tr>  
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">line_mean_score</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Average line artifact score in frames with line artifacts</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NA</td>
  </tr>  
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">tSNR_b0</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">Median temporal SNR in brain mask for b=0 frames</td>
    <td style="border: 1px solid #ddd; padding: 8px; word-wrap: break-word; white-space: normal;">NA</td>
  </tr>  
</tbody>
</table>

