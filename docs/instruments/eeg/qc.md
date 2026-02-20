# EEG Quality Control Procedures   

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
<p>The <b>StimTracker</b> device used during EEG acquisition for visits V03, V04, and V06 provides precise timing for auditory and visual stimulus onset and marks task start and end points. The EEG Core identified an <b>electrical artifact</b> in a subset of files caused by intermittent spikes from the device at both stimulus onset and offset.</p>
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

Flagged files in the raw EEG data (40–50%) were visually inspected after preprocessing with the MADE pipeline by examining all channels averaged across all trials. If the artifact was still visible, the file was labeled as artifact-present. If it was no longer visible, the file was labeled as artifact-free, indicating adequate artifact removal. **After preprocessing, ~10% of V03 files retained the StimTracker artifact.**

To evaluate the impact of the StimTracker artifact on EEG derivatives, event-related potentials (ERPs) were generated for relevant regions and time windows - see <a href="../artifact/" target="_blank">Effects of Artifact on ERP Derivatives by Task</a> for details and figures displaying artifact-free and artifact-present waveforms across tasks and ROIs. Statistical comparisons of mean ERP component amplitudes between artifact-free and artifact-present files across tasks revealed only two significant differences, both in the T7T8 cluster for the standard and deviant conditions of the MMN after FDR correction. Difference waves (Predeviant–Deviant) showed no significant effects for the FCz or T7T8 clusters, and no significant differences were found in the VEP or FACEs tasks.

In sum, our analysis indicates that the **StimTracker artifact does not meaningfully affect mean ERP amplitudes** and has minimal impact on the released derivatives. However, we encourage users to assess potential effects in their own analyses. The presence of the artifact is provided in the task-specific `eeg_qc_task-<TASK>` files included as part of the <a href="../../#eeg" target="_blank">tabulated EEG data</a>. The `eeg_qc_task-<TASK>_stimtracker_artifact` variable indicates whether the artifact was present (yes/no) in the processed data. *Note: Due to limited data containing the artifact, no comparisons were conducted for V04 files.*

See <a href="../artifact/" target="_blank">Effects of Artifact on ERP Derivatives by Task</a> for more information about the StimTracker artifact.

## EEG Net Placement ("Capping Quality") Ratings

<div class="table-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Each task’s tabulated QC file includes capping ratings in the variable <code>eeg_qc_task-&lt;TASK&gt;_capping_quality</code>.</span>
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

