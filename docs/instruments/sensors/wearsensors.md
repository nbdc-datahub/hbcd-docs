<style>
.wy-nav-content {
    width: 85% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>

# Infant Leg Motion

The HBCD data release includes Infant Leg Motion Wearable Sensor data acquired during visits V02 and V03.

## Release Data

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</i></span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Note that accelerometer sensor timestamps can drift over time. Although right and left leg sensors start recording simultaneously with the same sampling rate and duration, exact time alignment cannot be assumed. By our estimates, Axivity AX6 sensors recording at 25 samples/sec diverge from one another by a couple of seconds over 72 hours, with the magnitude of this discrepancy increasing over time. Furthermore, offsets differed between sensors, necessitating a calibration procedure to correct for these differences (<a href="https://doi.org/10.3390/s24175736">Oh et al. 2024</a>).</p>
<p>In addition, for raw data downloads, when calibration files are missing or not collected correctly, it is technically possible to use a different set of calibration files from the same 2 sensors that were collected from a different data collection session close in time. It is also possible to manually adjust (downsample) an incorrect sampling rate if it was set too high. For processed data downloads, when calibration files are missing or not collected correctly, or the sampling rate is incorrect, data are not processed. In analysis, users are advised to use caution in analyzing datasets with missing data as missing data may not be randomly distributed across the sample.</p> 
</div>

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">Please review the <a href="https://docs.hbcdstudy.org/latest/changelog/issues-updates/" target="_blank">Known Issues & Pending Updates</a> page for updates that may affect data use.</span>
</div>
<p></p>

Motion/accelerometry data collected from wearable infant leg sensors include raw and processed sensor recordings:

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b><i class="fas fa-hammer header-icon"></i> Raw BIDS</b></td>
<td>Raw Axivity AX6 wearable sensor data in BIDS format (<code>motion/</code> subfolder of <code>rawdata/</code> participant directories)</td></tr>
<tr><td><b><i class="fas fa-cog header-icon"></i> Derivatives</b></td>
<td>Processed outputs from the HBCD-Motion pipeline (<code>hbcd_motion/</code> subfolder of <code>derivatives/</code>)</td></tr>
</tbody></table>

<div id="rawbids" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dde6fe;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
  <span class="text">Raw BIDS</span>
  <a class="anchor-link" href="#rawbids" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>
The raw data include recordings from the left and right leg sensors (<code>motion.tsv</code>) with corresponding <code>channels.tsv</code> files describing each column (and sidecar JSON files with metadata). See <a href="https://doi.org/10.1038/s41597-024-03559-8" target="_blank">Jeung et al., 2024</a> for BIDS conversion procedures.</p>
<p><a href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>
<pre class="folder-tree" style="font-size: 12px; line-height: 1.4;">
hbcd/
└── rawdata/
    └── sub-[ID]/
        └── ses-[V0X]/
            └── motion/
                <span class="hashtag"># Calibration files</span>
                ├── *_task-<span class="var">{Left|Right}</span>LegMovement_tracksys-imu_acq-calibration_motion.tsv   <span class="hashtag">(+JSON)</span>
                └── *_task-<span class="var">{Left|Right}</span>LegMovement_tracksys-imu_acq-calibration_channels.tsv <span class="hashtag">(+JSON)</span>

                <span class="hashtag"># 72-hr recordings</span>
                ├── *_task-<span class="var">{Left|Right}</span>LegMovement_tracksys-imu_acq-primary_motion.tsv   <span class="hashtag">(+JSON)</span>
                └── *_task-<span class="var">{Left|Right}</span>LegMovement_tracksys-imu_acq-primary_channels.tsv <span class="hashtag">(+JSON)</span>
</pre>
</div>

<div id="derivatives" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
    <span class="text">HBCD-Motion Derivatives</span>
  <a class="anchor-link" href="#derivatives" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>Axivity Ax6 sensor recordings of infant leg movements across 72 continuous hours are processed via the HBCD-Motion pipeline. Derivative files are explained in the <a href="https://hbcd-motion-postproc.readthedocs.io/" target="_blank">HBCD-Motion documentation</a>.</p>
<p><a href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>
<pre class="folder-tree" style="font-size: 12px; line-height: 1.4;">
hbcd/
└── derivatives/
    └── hbcd_motion/
        └── sub-[ID]/
            └── ses-[V0X]/
                └── motion/
                    <span class="hashtag"># Kinematics</span>
                    ├── Kinematics/
                    │   └── sub-[ID]_ses-[V0X]_desc-kinematics_recording-<span class="var">{20|25}</span>_motion.json

                    <span class="hashtag"># Physical Activity (PA)</span>
                    ├── PA/
                    │   ├── sub-[ID]_ses-[V0X]_leg-<span class="var">{left|right}</span>_desc-<span class="var">{accelerationPA|jerkPA}</span>_BOUTS.tsv
                    │   ├── sub-[ID]_ses-[V0X]_leg-<span class="var">{left|right}</span>_desc-<span class="var">{accelerationPA|jerkPA}</span>_LOG.txt
                    │   ├── sub-[ID]_ses-[V0X]_leg-<span class="var">{left|right}</span>_desc-<span class="var">{accelerationPA|jerkPA}</span>_RAW.tsv
                    │   └── sub-[ID]_ses-[V0X]_leg-<span class="var">{left|right}</span>_desc-<span class="var">{accelerationPA|jerkPA}</span>_SUMMARY.json
                    
                    <span class="hashtag"># Metadata & Outputs</span>
                    ├── PARAMETERS.json
                    └── sub-[ID]_ses-[V0X]_leg-<span class="var">{left|right}</span>_desc-calibrated_recording-20_motion.tsv
</pre>
</div>

## Data Acquisition

Infant leg movement data collected by wearable sensors for HBCD captures information related to motor behavior, physical activity, sleep. Wearable sensors are placed on the child's right and left ankles by an HBCD Study team member during a visit. Sensor data (accelerometer and gyroscope) was collected continuously over 72 hours to estimate movement frequency, intensity, and sleep periods. Caregivers followed typical routines, removing sensors only for water exposure (e.g., baths) and replacing them afterward. Each sensor (Axivity AX6) was calibrated by recording 10 seconds on each of its six flat surfaces before data collection. Sensors recorded accelerometer (±16 g) and gyroscope (±2000 dps) data at 25 Hz, enabling estimates of sedentary, light, moderate-to-vigorous activity, and sleep. See [Pini et al. 2024](https://doi.org/10.1016/j.dcn.2024.101446) for a full measure description.

## Quality Control

For the calibration files, the 72-hour sensor data files, and the survey data, a random selection of files were manually reviewed on a weekly basis. Raw calibration files were checked to verify the presence of sufficient data for each of the six axes. Seventy-two hour sensor data files were checked for presence of data, labeling of right and left leg, and sampling rate used. Surveys were checked to confirm presence of responses. Note that only a small percentage of total files were reviewed due to the procedure being manual.

Issues were generally rare for sensor data and most data were deemed to be present and accurately collected. Errors that did arise were corrected when possible (though this was typically not feasible). Common errors noted include inadequate or missing data (due to human error, technical issues, or a parent/legal guardian declining to participate in this aspect of the study), sensors being removed for extended periods during the 72-hour collection, and incorrect sampling rate.

## References

<div id="ref" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-book-open"></i></span>
  <span class="text-with-link">
  <span class="text">References</span>
  <a class="anchor-link" href="#ref" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<div class="references">
    <p>Ghazi, M. A., Zhou, J., Havens, K. L., &amp; Smith, B. A. (2024). Accelerometer thresholds for estimating physical activity intensity levels in infants: A preliminary study. <em>Sensors</em> (Basel, Switzerland), 24(14), 4436. <a href="https://doi.org/10.3390/s24144436">https://doi.org/10.3390/s24144436</a></p>
    <p>Jeung, S., Cockx, H., Appelhoff, S., Berg, T., Gramann, K., Grothkopp, S., Warmerdam, E., Hansen, C., Oostenveld, R., BIDS Maintainers, &amp; Welzel, J. (2024). Motion-BIDS: an extension to the brain imaging data structure to organize motion data for reproducible research. <em>Scientific Data</em>, 11(1), 716. <a href="https://doi.org/10.1038/s41597-024-03559-8">https://doi.org/10.1038/s41597-024-03559-8</a></p>
    <p>Oh, J., Loeb, G. E., &amp; Smith, B. A. (2024). The utility of calibrating wearable sensors before quantifying infant leg movements. <em>Sensors</em> (Basel, Switzerland), 24(17), 5736. <a href="https://doi.org/10.3390/s24175736">https://doi.org/10.3390/s24175736</a></p>
    <p>Oh, J., Ordoñez, E. L. T., Velasquez, E., Mejía, M., Del Pilar Grazioso, M., Rohloff, P., &amp; Smith, B. A. (2024). Associating neuromotor outcomes at 12 months with wearable sensor measures collected during early infancy in rural Guatemala. <em>Gait &amp; Posture</em>, 113, 477–489. <a href="https://doi.org/10.1016/j.gaitpost.2024.08.005">https://doi.org/10.1016/j.gaitpost.2024.08.005</a></p>
    <p>Pini, N., Fifer, W. P., Oh, J., Nebeker, C., Croff, J. M., Smith, B. A., &amp; Novel Technology/Wearable Sensors Working Group. (2024). Remote data collection of infant activity and sleep patterns via wearable sensors in the HEALthy Brain and Child Development Study (HBCD). <em>Developmental Cognitive Neuroscience</em>, 69(101446), 101446. <a href="https://doi.org/10.1016/j.dcn.2024.101446">https://doi.org/10.1016/j.dcn.2024.101446</a></p>
    <p>Smith, B. A., Trujillo-Priego, I. A., Lane, C. J., Finley, J. M., &amp; Horak, F. B. (2015). Daily quantity of infant leg movement: Wearable sensor algorithm and relationship to walking onset. <em>Sensors</em> (Basel, Switzerland), 15(8), 19006–19020. <a href="https://doi.org/10.3390/s150819006">https://doi.org/10.3390/s150819006</a></p>
    <p>Trujillo-Priego, I. A., &amp; Smith, B. A. (2017). Kinematic characteristics of infant leg movements produced across a full day. <em>Journal of Rehabilitation and Assistive Technologies Engineering</em>, 4, 205566831771746. <a href="https://doi.org/10.1177/2055668317717461">https://doi.org/10.1177/2055668317717461</a></p>
    <p>Trujillo-Priego, I. A., Zhou, J., Werner, I. F., Deng, W., &amp; Smith, B. A. (2020). Infant leg activity intensity before and after naps. <em>Journal for the Measurement of Physical Behaviour</em>, 3(2), 157–163.<a href="https://doi.org/10.1123/jmpb.2019-0011">https://doi.org/10.1123/jmpb.2019-0011</a></p>
</div>
</div>
