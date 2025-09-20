# Infant Leg Motion Wearable Sensor

The HBCD data release includes Infant Leg Motion Wearable Sensor data acquired during visits V02 and V03, V04.

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

Motion/accelerometry data collected from wearable infant leg sensors includes raw and processed <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> data:

- <i class="fa fa-hammer"></i> <a href="../../../datacuration/rawbids/#motion" target="_blank">Raw BIDS</a> under subject- and session-specific <code>motion/</code> folders (*file-based data*)
- <i class="fas fa-cog"></i> <a href="../../datacuration/derivatives/#biosensors-hbcd-motion" target="_blank">Derivatives</a> processed through the HBCD-Motion pipeline under <code>hbcd_motion/</code> (*file-based data*)

<pre class="folder-tree">
hbcd/
|__ rawdata/ 
|   |__ sub-<span class="label">&lt;label&gt;</span>/   
|       |__ ses-<span class="label">&lt;label&gt;</span>/
|           |__ motion/  <span class="hashtag"># Raw sensor data</span>
|
|__ derivatives/        
    |__ hbcd_motion/     <span class="hashtag"># HBCD-Motion pipeline derivatives</span>
</pre>

## Details

Infant leg movement data collected by wearable sensors for HBCD captures information related to motor behavior, physical activity, sleep. Wearable sensors are placed on the child's right and left ankles by an HBCD Study team member during a visit. Sensor data (accelerometer and gyroscope) was collected continuously over 72 hours to estimate movement frequency, intensity, and sleep periods. Caregivers followed typical routines, removing sensors only for water exposure (e.g., baths) and replacing them afterward. Each sensor (Axivity AX6) was calibrated by recording 10 seconds on each of its six flat surfaces before data collection. Sensors recorded accelerometer (±16 g) and gyroscope (±2000 dps) data at 25 Hz, enabling estimates of sedentary, light, moderate-to-vigorous activity, and sleep. See [Pini et al. 2024](https://doi.org/10.1016/j.dcn.2024.101446) for a full measure description.

## Quality Control

For the calibration files, the 72-hour sensor data files, and the survey data, a random selection of files were manually reviewed on a weekly basis. Raw calibration files were checked to verify the presence of sufficient data for each of the six axes. Seventy-two hour sensor data files were checked for presence of data, labeling of right and left leg, and sampling rate used. Surveys were checked to confirm presence of responses. Note that only a small percentage of total files were reviewed due to the procedure being manual.

Issues were generally rare for sensor data and most data were deemed to be present and accurately collected. Errors that did arise were corrected when possible (though this was typically not feasible). Common errors noted include inadequate or missing data (due to human error, technical issues, or a parent/legal guardian declining to participate in this aspect of the study), sensors being removed for extended periods during the 72-hour collection, and incorrect sampling rate.

## References

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
<br>
