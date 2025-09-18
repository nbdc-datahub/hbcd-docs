# Electroencephalography (EEG)

EEG tasks are acquired during visits V03, V04, and V06. For full details on the HBCD EEG protocol, please refer to [Fox et al. 2024](https://doi.org/10.1016/j.dcn.2024.101447) published in the Developmental Cognitive Neuroscience special issue on HBCD. 

![](images/EEG-Parameters.png)
*Source: [HBCD Study Protocols - EEG](https://hbcdstudy.org/wp-content/uploads/2023/06/EEG-Parameters.pdf)*

## Release Data

EEG data in the release includes <span class="tooltip">tabulated data<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> (see table names listed [here](../index.md#eeg)) and the following <span class="tooltip">file-based data<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span>:

- <i class="fa fa-hammer"></i><strong> Raw BIDS</strong> under subject- and session-specific <code>eeg/</code> folders - <a href="../../../datacuration/rawbids/#eeg">see details</a>
- <i class="fas fa-cog"></i><strong> Derivatives</strong> produced by the HBCD-MADE pipeline under <code>made/</code> - <a href="../../../datacuration/derivatives/#hbcd-made-made">see details</a>

*HBCD data structure summary with only EEG data included:*
<pre class="folder-tree">
hbcd/
|__ rawdata/ 
|   |__ phenotype/     <span class="hashtag"># Tabulated Data</span>
|   |   |__ eeg_made_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>_acq-eeg_preprocessingReport.*
|   |   |__ eeg_qc_task-<span class="placeholder">&lt;FACE|MMN|RS|VEP&gt;</span>.*
|   |
|   |__ sub-<span class="label">&lt;label&gt;</span>/   <span class="hashtag"># Raw BIDS (file-based data)</span>
|       |__ ses-<span class="label">&lt;label&gt;</span>/
|           |__ eeg/*
|
|__ derivatives/       <span class="hashtag"># Derivatives (file-based data)</span>
    |__ made/
</pre>

<p>
<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text">
    See <a href="../../../datacuration/overview/">here</a> for overview of tabulated vs file-based data.
  </span>
</div>
</p>

## Quality Control    
After EEG acquisition, quality control checks are performed using [EEG2BIDS Wizard](https://github.com/aces/eeg2bids), a custom MATLAB application installed at all HBCD sites. These checks are immediately provided to the user to ensure the data's integrity and usability. The process includes:

- Verifying event markers in the EEG data to confirm all required events are accurately recorded.
- Ensuring the setup for stimulus presentation and EEG data acquisition adheres to the study protocol.
- Inspecting electrode impedances to ensure they are within acceptable limits.
- Detecting multiple task runs and incomplete recordings.
- Confirming the use of correct E-Prime task versions.

Both study sites and the EEG Core team use an EEG Quality Control dashboard developed by LORIS to access and monitor incoming EEG data and QC metrics, such as retained epochs and line noise levels. Outputs from the HBCD-Maryland Analysis of Developmental EEG ([HBCD-MADE](https://hbcd-made.readthedocs.io/en/latest/)) pipeline, which handles preprocessing and data cleaning, are also integrated into the dashboard. These outputs include key metrics like outlier statistics for specific task epochs ([Debnath et al., 2020](https://doi.org/10.1111/psyp.13580)). Regular site-specific check-ins and troubleshooting are conducted to ensure consistent protocol adherence and data quality across sites. For a detailed description of QC procedures in the HBCD Study EEG protocol, refer to [Fox et al., 2024](https://doi.org/10.1016/j.dcn.2024.101447).

During quality control, a frequently observed issue across all tasks was the irregular application of EEG sensors. Additionally, partial task completion due to infant fussing and missing stimulus flags were commonly noted for the faces and auditory mismatch negativity tasks.

### EEG Net Placement ("Capping Quality") Ratings

<p>
<div id="demo-fyi" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">EEG data with a capping quality rating of "Not usable" are not included in the current release. Capping ratings can be found in the <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> QC file for each task (<code>eeg_qc_task-&lt;TASK&gt;</code>).</span>
</div>
</p>

EEG capping quality ratings are used to determine inclusion in the data release pool and subsequent processing. Photos are taken for each acquisition from the front, back, top, left, and right angles of the participant's head and uploaded via the BIDS Wizard application to a secure computing environment. They are then reviewed by the EEG Core at the University of Maryland to rate the quality of EEG net placement, or "capping quality," for each acquisition. 

“Average”, "Poor," and "Not usable" ratings correspond to net placement shifted 1-2 cm, 2-3 cm, and >3 cm from proper placement, respectively. To be rated as "Excellent," acquisitions must meet the following criteria:

1.	Net placement is symmetrical with midline electrodes centered on the scalp
2.	Ears are within the ear holes and not covered by sensors 
3.	Reference electrode is placed on the vertex of the scalp
4.	Electrode E17 is placed on the nasion

Please refer to the [HBCD EEG Acquisition Protocol](https://zenodo.org/records/14795030) for additional information about capping requirements.

## Resources
- [HBCD EEG Utilities](https://hbcd-eeg-utilities.readthedocs.io/)
- [HBCD E-Prime Task Manual](https://docs.google.com/document/d/1PghQQpLbxjQavtVlHyIz7JVJxlyKcC4Do8z8j7srdaI/edit?usp=sharing)
- [HBCD EEG Acquisition Protocol](https://zenodo.org/records/14795030)

## References

<div class="references">
    <p>Debnath, R., Buzzell, G. A., Morales, S., Bowers, M. E., Leach, S. C., & Fox, N. A. (2020). The Maryland analysis of developmental EEG (MADE) pipeline. Psychophysiology, 57(6), e13580. <a href="https://doi.org/10.1111/psyp.13580" target="_blank">https://doi.org/10.1111/psyp.13580</a></p>  
    <p>Fox, N. A., Pérez-Edgar, K., Morales, S., Brito, N. H., Campbell, A. M., Cavanagh, J. F., Gabard-Durnam, L. J., Hudac, C. M., Key, A. P., Larson-Prior, L. J., Pedapati, E. V., Norton, E. S., Reetzke, R., Roberts, T. P., Rutter, T. M., Scott, L. S., Shuffrey, L. C., Antúnez, M., Boylan, M. R., … Yoder, L. (2024). The development and structure of the Healthy Brain and Child Development (HBCD) study EEG Protocol. <i>Developmental Cognitive Neuroscience</i>, 69, 101447. <a href="https://doi.org/10.1016/j.dcn.2024.101447" target="_blank">https://doi.org/10.1016/j.dcn.2024.101447</a></p> 
</div>
<br>


