# Quality Control Procedures   

## QC Dashboard

After EEG acquisition, quality control checks are performed using [EEG2BIDS Wizard](https://github.com/aces/eeg2bids), a custom MATLAB application installed at all HBCD sites. These checks are immediately provided to the user to ensure the data's integrity and usability. The process includes:

- Verifying event markers in the EEG data to confirm all required events are accurately recorded.
- Ensuring the setup for stimulus presentation and EEG data acquisition adheres to the study protocol.
- Inspecting electrode impedances to ensure they are within acceptable limits.
- Detecting multiple task runs and incomplete recordings.
- Confirming the use of correct E-Prime task versions.

Both study sites and the EEG Core team use an EEG Quality Control dashboard developed by LORIS to access and monitor incoming EEG data and QC metrics, such as retained epochs and line noise levels. Outputs from the HBCD-Maryland Analysis of Developmental EEG ([HBCD-MADE](https://hbcd-made.readthedocs.io/en/latest/)) pipeline, which handles preprocessing and data cleaning, are also integrated into the dashboard. These outputs include key metrics like outlier statistics for specific task epochs ([Debnath et al., 2020](https://doi.org/10.1111/psyp.13580)). Regular site-specific check-ins and troubleshooting are conducted to ensure consistent protocol adherence and data quality across sites. For a detailed description of QC procedures in the HBCD Study EEG protocol, refer to [Fox et al., 2024](https://doi.org/10.1016/j.dcn.2024.101447).

During quality control, a frequently observed issue across all tasks was the irregular application of EEG sensors. Additionally, partial task completion due to infant fussing and missing stimulus flags were commonly noted for the faces and auditory mismatch negativity tasks.

## Stimtracker Artifact Detection

<div class="table-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Presence of the StimTracker artifact is listed in the tabulated QC file for each task (<code>eeg_qc_task-&lt;TASK&gt;</code>).</span>
</div>
<p></p>

<div style="display: flex; align-items: center; gap: 25px;">
<div style="flex: 1;">
<p>The <b>StimTracker</b> device, used during EEG acquisition for visits V03, V04, and V06, provides precise timing for auditory and visual stimulus onset and marks task start and end points. The EEG Core identified an <b>electrical artifact</b> in a subset of files caused by intermittent spikes from the device at both stimulus onset and offset.</p>
<p>To detect the artifact, the EEG Core developed a custom MATLAB script that averages all epochs per task and flags voltage fluctuations >1 µV in two time windows: onset (–10 to 10 ms) and offset (250 to 270 ms) of the voltage spike.<p>
</div>
  <!-- Image on the right -->
  <div style="flex: 1; text-align: center;">
    <img src="../images/Fig1.png" style="max-width:100%; height:auto; display:block; margin:0 auto;">
    <p style="font-size: 0.8em; margin-top: 5px; line-height: 1.1; max-width:100%; margin-left:auto; margin-right:auto; text-align:justify;">
      <b>Figure 1.</b> Example of the electrical artifact detected in the MMN auditory oddball task in E55. 
      The artifact is characterized by a negative deflection at stimulus onset and a positive deflection at offset.
    </p>
  </div>
</div>

Flagged files in the raw EEG data (40–50%) were visually inspected after preprocessing with the MADE pipeline by examining all channels averaged across all trials. If the artifact was still visible, the file was labeled as artifact-present. If it was no longer visible, the file was labeled as artifact-free, indicating adequate artifact removal. **After preprocessing, roughly 10% of V03 files retained the StimTracker artifact.**

To evaluate the impact of the StimTracker artifact on EEG derivatives, event-related potentials (ERPs) were generated for relevant regions and time windows - see [Effects of Artifact on ERP Derivatives by Task](#effects-of-artifact-on-erp-derivatives-by-task) below for details and figures displaying artifact-free and artifact-present waveforms across tasks and ROIs. Statistical comparisons of mean ERP component amplitudes between artifact-free and artifact-present files across tasks revealed only two significant differences, both in the T7T8 cluster for the standard and deviant conditions of the MMN after FDR correction. Difference waves (Predeviant–Deviant) showed no significant effects for the FCz or T7T8 clusters, and no significant differences were found in the VEP or FACEs tasks.

Our analysis indicates that the **StimTracker artifact does not meaningfully affect mean ERP amplitudes** and has minimal impact on the released derivatives. However, we encourage users to assess potential effects in their own analyses. The presence of the artifact is provided in the task-specific `eeg_qc_task-<TASK>` files included as part of the <a href="../../#eeg" target="_blank">tabulated EEG data</a>. <span style="color: red;">The binary `eeg_qc_-<TASK>` variable indicates whether the artifact was present (yes/no) in the processed data. (UPDATE FIELD/VARIABLE NAME ONCE KNOWN)</span>
*Note: Due to limited data containing the artifact, no comparisons were conducted for V04 files.*

### Effects of Artifact on ERP Derivatives by Task
To assess the artifact’s impact on EEG derivatives, ERPs were computed for each task and ROI. Because there were many more artifact-free files, 100 artifact-present and 100 artifact-free files per task were randomly selected for comparison to balance the groups. Waveforms for each ERP are shown below, and differences by task and ROI are summarized in the accompanying tables.

<div id="vep" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-file-waveform"></i></span>
  <span class="text-with-link">
  <span class="text">VEP</span>
  <a class="anchor-link" href="#vep" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<img src="../images/vep-erp-oz.jpeg" width="50%" height="auto" class="center">
<p></p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
<thead>
<tr>
    <th style="word-wrap: break-word; white-space: normal;">Measure</th>
    <th style="word-wrap: break-word; white-space: normal;">N1 (40-79 ms) Mean Difference</th>
    <th style="word-wrap: break-word; white-space: normal;">N1 (40-79 ms) Significance</th>
    <th style="word-wrap: break-word; white-space: normal;">P1 (80-140 ms) Mean Difference</th>
    <th style="word-wrap: break-word; white-space: normal;">P1 (80-140 ms) Significance</th>
    <th style="word-wrap: break-word; white-space: normal;">N2 (141 - 300 ms) Mean Difference</th>
    <th style="word-wrap: break-word; white-space: normal;">N2 (141 - 300 ms) Significance</th>
</tr>
</thead>
<tbody>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Mean Amplitude</td>
    <td style="word-wrap: break-word; white-space: normal;">&Delta; = 0.07 &micro;V</td>
    <td style="word-wrap: break-word; white-space: normal;">p = 0.91</td>
    <td style="word-wrap: break-word; white-space: normal;">&Delta; = 0.18 &micro;V</td>
    <td style="word-wrap: break-word; white-space: normal;">p = 0.77</td>
    <td style="word-wrap: break-word; white-space: normal;">&Delta; = -0.008 &micro;V</td>
    <td style="word-wrap: break-word; white-space: normal;">p= 0.99</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Peak Amplitude</td>
    <td style="word-wrap: break-word; white-space: normal;">&Delta; = -0.43 &micro;V</td>
    <td style="word-wrap: break-word; white-space: normal;">p= 0.55</td>
    <td style="word-wrap: break-word; white-space: normal;">&Delta; = 0.67 &micro;V</td>
    <td style="word-wrap: break-word; white-space: normal;">p= 0.37</td>
    <td style="word-wrap: break-word; white-space: normal;">&Delta; = -0.56 &micro;V</td>
    <td style="word-wrap: break-word; white-space: normal;">p = 0.49</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Peak Latency</td>
    <td style="word-wrap: break-word; white-space: normal;">&Delta; = -0.3 ms</td>
    <td style="word-wrap: break-word; white-space: normal;">p = 0.85</td>
    <td style="word-wrap: break-word; white-space: normal;">&Delta; = 0.1 ms</td>
    <td style="word-wrap: break-word; white-space: normal;">p = 0.98</td>
    <td style="word-wrap: break-word; white-space: normal;">&Delta; = -1.3 ms</td>
    <td style="word-wrap: break-word; white-space: normal;">p = 0.86</td>
</tr>
<tr>
<td colspan="7" style="font-size: 1.0em; word-wrap: break-word; white-space: normal; border-bottom: none;"><b>Table 1.</b> Differences in ERPs between the artifact containing (n=100) and artifact-free (n=100) files.  Mean differences for mean amplitude, peak amplitude, and peak latency for the Oz cluster are presented for our time windows of interest.</td>
</tr>
</tbody>
</table>
</div>

<div id="mmn" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-file-waveform"></i></span>
  <span class="text-with-link">
  <span class="text">MMN</span>
  <a class="anchor-link" href="#mmn" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<img src="../images/mmn-artifact.jpeg" width="100%" height="auto" class="center">
<p></p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<thead>
<tr><th>Condition</th><th>ROI</th><th>Mean Amp Artifact (uV)</th><th>Mean Amp No Artifact (uV)</th><th>Delta (uV)</th><th>p Value</th><th>p Value Adj. (FDR)</th></tr>
</thead>
<tbody>
<tr><td>Standard</td><td>FCz</td><td>1.25</td><td>1.264</td><td>-0.014</td><td>0.946</td><td>0.946</td></tr>
<tr><td>Standard</td><td>T7T8</td><td>1.482</td><td>0.921</td><td>0.562</td><td>0.013</td><td>0.039</td></tr>
<tr><td>Predeviant</td><td>FCz</td><td>1.349</td><td>1.437</td><td>-0.089</td><td>0.77</td><td>0.946</td></tr>
<tr><td>Predeviant</td><td>T7T8</td><td>1.279</td><td>0.641</td><td>0.637</td><td>0.055</td><td>0.11</td></tr>
<tr><td>Deviant</td><td>FCz</td><td>1.478</td><td>1.444</td><td>0.034</td><td>0.927</td><td>0.946</td></tr>
<tr><td>Deviant</td><td>T7T8</td><td>3.118</td><td>1.987</td><td>1.132</td><td>0.004</td><td>0.024</td></tr>
<tr><td colspan="7" style="font-size: 13px; word-wrap: break-word; white-space: normal;"><b>Table 2.</b> Differences between the artifact containing (n=100) and artifact-free (n = 100) files for the mean amplitude for each condition, ROI, and time window.<br>
<i>Note:</i> Differences between means are presented for each artifact designation, as well as the difference between them (delta). P-values were calculated for the differences between means, and then FDR corrected.  Original and corrected p-values are presented.</td></tr>
</tbody>
</table>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<thead>
<tr><th>Contrast</th><th>ROI</th><th>Mean Amp Artifact (uV)</th><th>Mean Amp No Artifact (uV)</th><th>Delta (uV)</th><th>p Value</th></tr>
</thead>
<tbody>
<tr><td>Deviant-Predeviant</td><td>FCz</td><td>0.24</td><td>-0.10</td><td>0.34</td><td>0.45</td></tr>
<tr><td>Deviant-Predeviant</td><td>T7T8</td><td>1.70</td><td>1.03</td><td>0.67</td><td>0.10</td></tr>
<tr><td colspan="6" style="font-size: 13px; word-wrap: break-word; white-space: normal; border-bottom: none;"><b>Table 3.</b> Differences in mean amplitude for the difference wave of files containing the artifact (n = 100) and artifact-free files (n = 100). 
Contrast</td></tr>
</tbody>
</table>
</div>

<div id="face" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-file-waveform"></i></span>
  <span class="text-with-link">
  <span class="text">FACE Task (by ROI)</span>
  <a class="anchor-link" href="#face" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<div style="display: flex; justify-content: space-between; align-items: flex-start; text-align: center;">
  <div style="width: 49%;">
    <p style="font-weight: bold; margin-bottom: 4px; font-size: 1.1em;">P7</p>
    <img src="../images/P7.png" style="width: 100%;">
  </div>
  <div style="width: 49%;">
    <p style="font-weight: bold; margin-bottom: 4px; font-size: 1.1em;">P8</p>
    <img src="../images/P8.png" style="width: 100%;">
  </div>
</div>
<div style="display: flex; justify-content: space-between; align-items: flex-start; text-align: center;">
  <div style="width: 49%;">
    <p style="font-weight: bold; margin-bottom: 4px; font-size: 1.1em;">Oz</p>
    <img src="../images/oz.png" style="width: 100%;">
  </div>
  <div style="width: 50%;">
    <p style="font-weight: bold; margin-bottom: 4px; font-size: 1.1em;">Fcz</p>
    <img src="../images/fcz.png" style="width: 100%;">
  </div>
</div>
<p></p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<thead>
<tr>
<th>Condition</th>
<th>ROI</th>
<th style="word-wrap: break-word; white-space: normal;">Time Window (ms)</th>
<th style="word-wrap: break-word; white-space: normal;">Mean Amp Artifact (uV)</th>
<th style="word-wrap: break-word; white-space: normal;">Mean Amp No Artifact (uV)</th>
<th>Delta (uV)</th>
<th style="word-wrap: break-word; white-space: normal;">p Value</th>
<th style="word-wrap: break-word; white-space: normal;">p value Adjusted<br />(FDR)</th>
</tr>
</thead>
<tbody>
<tr><td>Upright (Inv)</td><td>FCz</td><td>300-600</td><td>-1.141</td><td>-1.855</td><td>0.713</td><td>0.228</td><td>0.547</td></tr>
<tr><td>Upright (Inv)</td><td>Oz</td><td>200-350</td><td>-1.38</td><td>-0.922</td><td>-0.459</td><td>0.668</td><td>0.836</td></tr>
<tr><td>Upright (Inv)</td><td>P7</td><td>200-350</td><td>1.418</td><td>1.445</td><td>-0.028</td><td>0.971</td><td>0.971</td></tr>
<tr><td>Upright (Inv)</td><td>P7</td><td>350-600</td><td>4.865</td><td>5.588</td><td>-0.723</td><td>0.496</td><td>0.744</td></tr>
<tr><td>Upright (Inv)</td><td>P8</td><td>200-350</td><td>1.933</td><td>1.705</td><td>0.229</td><td>0.789</td><td>0.836</td></tr>
<tr><td>Upright (Inv)</td><td>P8</td><td>350-600</td><td>5.144</td><td>4.862</td><td>0.282</td><td>0.799</td><td>0.836</td></tr>
<tr><td>Inverted</td><td>FCz</td><td>300-600</td><td>-1.353</td><td>-2.074</td><td>0.72</td><td>0.18</td><td>0.54</td></tr>
<tr><td>Inverted</td><td>Oz</td><td>200-350</td><td>-0.771</td><td>0.181</td><td>-0.953</td><td>0.373</td><td>0.639</td></tr>
<tr><td>Inverted</td><td>P7</td><td>200-350</td><td>1.648</td><td>3.367</td><td>-1.719</td><td>0.03</td><td>0.18</td></tr>
<tr><td>Inverted</td><td>P7</td><td>350-600</td><td>4.525</td><td>7.553</td><td>-3.029</td><td>0.009</td><td>0.108</td></tr>
<tr><td>Inverted</td><td>P8</td><td>200-350</td><td>2.728</td><td>2.958</td><td>-0.23</td><td>0.801</td><td>0.836</td></tr>
<tr><td>Inverted</td><td>P8</td><td>350-600</td><td>6.242</td><td>6.597</td><td>-0.355</td><td>0.776</td><td>0.836</td></tr>
<tr><td>Upright (Obj)</td><td>FCz</td><td>300-600</td><td>-2.185</td><td>-2.342</td><td>0.157</td><td>0.776</td><td>0.836</td></tr>
<tr><td>Upright (Obj)</td><td>Oz</td><td>200-350</td><td>0.554</td><td>1.836</td><td>-1.281</td><td>0.274</td><td>0.583</td></tr>
<tr><td>Upright (Obj)</td><td>P7</td><td>200-350</td><td>2.002</td><td>2.879</td><td>-0.877</td><td>0.316</td><td>0.583</td></tr>
<tr><td>Upright (Obj)</td><td>P7</td><td>350-600</td><td>4.968</td><td>6.708</td><td>-1.74</td><td>0.166</td><td>0.54</td></tr>
<tr><td>Upright (Obj)</td><td>P8</td><td>200-350</td><td>2.626</td><td>3.6</td><td>-0.974</td><td>0.305</td><td>0.583</td></tr>
<tr><td>Upright (Obj)</td><td>P8</td><td>350-600</td><td>5.74</td><td>7.277</td><td>-1.537</td><td>0.216</td><td>0.547</td></tr>
<tr><td>Object</td><td>FCz</td><td>300-600</td><td>-1.335</td><td>-2.302</td><td>0.968</td><td>0.09</td><td>0.36</td></tr>
<tr><td>Object</td><td>Oz</td><td>200-350</td><td>-2.097</td><td>-0.179</td><td>-1.918</td><td>0.057</td><td>0.274</td></tr>
<tr><td>Object</td><td>P7</td><td>200-350</td><td>0.607</td><td>2.357</td><td>-1.75</td><td>0.016</td><td>0.128</td></tr>
<tr><td>Object</td><td>P7</td><td>350-600</td><td>4.001</td><td>6.964</td><td>-2.963</td><td>0.004</td><td>0.096</td></tr>
<tr><td>Object</td><td>P8</td><td>200-350</td><td>1.532</td><td>1.866</td><td>-0.334</td><td>0.692</td><td>0.836</td></tr>
<tr><td>Object</td><td>P8</td><td>350-600</td><td>5.32</td><td>6.283</td><td>-0.963</td><td>0.405</td><td>0.648</td></tr>
<tr>
<td colspan="8" style="font-size: 13px; word-wrap: break-word; white-space: normal; border-bottom: none;"><b>Table 4.</b> Differences between the artifact containing (n=100) and artifact-free (n = 100) files for the mean amplitude for each condition, ROI, and time window.<br>
<b>Note:</b> The FACE task has 2 blocks: one with upright and inverted faces and the other with upright faces and Sheinbug objects.  The upright condition is separated into its corresponding block; “Upright (Inv)” are those upright faces during the inverted block while “Upright (Obj)” corresponds to upright faces during the object block. Differences between means are presented for each artifact designation, as well as the difference between them (delta).  P-values were calculated for the differences between means, and then FDR corrected.  Original and corrected p-values are presented.</td>
</tr>
</tbody>
</table>
</div>


#### EXTRA TEXT

**Table 5.** Differences between the artifact containing (n=100) and artifact-free (n = 100) files for the mean amplitude of the difference wave.  

**Note:** These are calculated for each Region of Interest (ROI) and timewindow.  The upright conditions are from the corresponding block.  Differences between means are presented for each artifact designation, as well as the difference between them (delta).  P-values were calculated for the differences between means, and then FDR corrected.  Original and corrected p-values are presented.


## EEG Net Placement ("Capping Quality") Ratings

<div class="table-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Capping ratings are included in the tabulated QC files for each task (<code>eeg_qc_task-&lt;TASK&gt;</code>).</span>
</div>
<p></p>

EEG capping quality ratings are used to determine inclusion in data processing. Photos used to assess EEG capping quality are taken for each acquisition from the front, back, top, left, and right angles of the participant's head and uploaded via the BIDS Wizard application to a secure computing environment. They are then reviewed by the EEG Core at the University of Maryland to rate the quality of EEG net placement, or "capping quality," for each acquisition.

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 18px;">
  <tbody>
    <tr>
      <td style="width: 30%;"><strong>Markers of Proper Net Placement</strong></td>
      <td>
        <ul style="margin: 0; padding-left: 1.2em;">
          <li>Reference electrode <strong>(REF)</strong> at the vertex</li>
          <li>Nasion electrode <strong>(#17)</strong> between eyebrows</li>
          <li>Ear electrodes <strong>(#44, #114)</strong> at preauricular points</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><strong>Net Placement Rubric</strong></td>
      <td>
        <ul style="margin: 0; padding-left: 1.2em;">
          <li><strong>Excellent</strong> – all markers <strong>0–0.5 cm</strong> from correct placement</li>
          <li><strong>Average</strong> – any marker <strong>0.5–2 cm</strong> off</li>
          <li><strong>Poor</strong> – any marker <strong>2–3 cm</strong> off</li>
          <li><strong>Very Poor</strong> – any marker <strong>>3 cm</strong> off</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

Please refer to the [HBCD EEG Acquisition Protocol](https://zenodo.org/records/14795030) for additional information about capping requirements.

<br>

