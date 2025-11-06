<p style="font-size: 1.5em;">🚧 <i>UNDER RUD REVIEW</i></p>

# Infant Heart Rate (GABI)

The HBCD data release includes Infant Heart Rate Wearable Sensor data acquired via Gabi SmartCare during visits V02 and V03.

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
<p>Users of HBCD infant heart rate wearable sensor data must follow the study's data use guidelines and the conditions of the Data Use Certificate (DUC). These standards are in place to protect participant privacy, ensure scientific rigor, and promote respectful, non-stigmatizing research practices. Users should review relevant data warnings before downloading or analyzing infant heart rate sensor variables. This includes checking the data dictionary and instrument documentation for indicators such as incomplete recordings, periods of sensor removal, or discrepancies with setup/return metadata.</p>
<p>Users should avoid reporting results from groups smaller than ten participants to reduce the risk of re-identification. Users should interpret findings within broader social and environmental contexts, incorporating relevant covariates (e.g., demographic, environmental, caregiving factors) to improve scientific rigor and avoid oversimplifying developmental outcomes.</p>
<p>In analysis, users should exercise caution when working with datasets containing missing data, as missingness may not be random. Users should ensure transparency and reproducibility in all analyses by sharing analytic scripts, documenting missing data, and clearly describing decisions about wear-time, sensor removal, or exclusions. Users should not upload HBCD data to generative AI tools or other public platforms, as this would violate the DUC and risk unintended data exposure.</p>
</div>

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Note that infant heart rate sensor data may contain non-consecutive samples. The most likely reason is an inconsistent connection between the sensor and the receiver tablet, which can result in missing samples. Always refer to the timestamps embedded in the files to reconstruct the temporal sequence of the data. Infant heart rate sensor recordings may also be shorter than the planned 72 hours, which can occur due to human error, technical issues, or a parent/legal guardian deciding to discontinue data collection.</p> 
</div>

Infant heart rate data collected from wearable sensors includes **file-based** data (raw and processed data files in modality-specific formats). <i>See <a href="../../../datacuration/overview" target="_blank">Data Structure Overview</a> for an explanation of these data types.</i>

- <i class="fa fa-hammer"></i> <a href="../../../datacuration/file-based-data/#raw-bids" target="_blank">Raw BIDS</a> stored under subject- and session-specific <code>gabi/</code> folders
 - <i class="fas fa-cog"></i> <a href="../../../datacuration/file-based-data/#derivatives" target="_blank">Derivatives</a> will be available in a future release 

<div id="rawbids" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dde6fe;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
  <span class="text">Raw BIDS Files (<code>gabi/</code>)</span>
  <a class="anchor-link" href="#rawbids" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>The raw data contain the heart rate (HR), the blood oxygen saturation (SpO2), and the respiratory rate (RR), along with their respective measures of reliability, timestamps and metadata.</p>
<pre class="folder-tree">
hbcd/
|__ rawdata/ 
    |__ sub-<span class="label">&lt;label&gt;</span>/   <span class="hashtag"># Raw sensor data</span>
        |__ ses-<span class="label">&lt;label&gt;</span>/
            |__ gabi/
</pre>
</div>

<div id="derivatives" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
    <span class="text">Derivatives - <i>not currently available, but will be included in a future release</i></span>
  <a class="anchor-link" href="#derivatives" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
</div>

## Data Acquisition

**Infant heart rate sensor data** collected by the infant heart rate wearable sensor for HBCD captures information related to the infant's physiology and sleep. The device is fastened to the infant's upper arm with a soft-textile band by HBCD Study staff and worn for 72 hours, during which time data is collected across the child's typical activities in their natural environment. The photoplethysmography (PPG) sensors (one emitting green light PPG and one emitting red light PPG) embedded in the device allow for the collection of three biosignal estimates sampled at 1 Hz: 

 - **Rulse rate** (beats per minute)
 - **Blood oxygen saturation** (SpO<sub>2</sub>, percentage)
 - **Respiratory rate** (breaths per minute)

In addition, sleep states are derived from these vital sign data. Data collection is planned for 72 continuous hours. Caregivers followed typical routines, removing the sensor only for water exposure (e.g., baths) and repositioning it afterward. See [Pini et al. 2024](https://www.sciencedirect.com/science/article/pii/S1878929324001075?via%3Dihub) for a full measure description.

## Quality Control

For the infant heart rate wearable sensor (the 72-hour sensor data files), a random selection of files was manually reviewed on a weekly basis for the presence of data, adequate file duration, and discrepancies with the set-up/return forms. Note that only a small percentage of the total infant heart rate wearable sensor data files were reviewed because the procedure was manual.

Issues with the sensor data were generally rare, and most data were deemed present and accurately collected (when captured correctly). Errors that did arise were corrected, when possible, though this was typically not feasible. Common errors noted included inadequate or missing data (due to human error, technical issues, or a parent/legal guardian declining participation in this aspect of the study), sensors being removed for extended periods during the 72-hour collection, or unavailability of devices to conduct the data collection.

## References

<div class="references"> 
<p>Fifer, W. P., Myers, M. M., Sahni, R., Ohira-Kist, K., Kashyap, S., Stark, R. I., & Schulze, K. F. (2005). Interactions between sleeping position and feeding on cardiorespiratory activity in preterm infants. <i>Developmental Psychobiology</i>, 47(3), 288–296. <a href="https://doi.org/10.1002/dev.20096">https://doi.org/10.1002/dev.20096</a></p>
<p>Hamideh, D., & Nebeker, C. (2020). The digital health landscape in addiction and substance use research: Will digital health exacerbate or mitigate health inequities in vulnerable populations? <i>Current Addiction Reports</i>, 7(3), 317–332. <a href="https://doi.org/10.1007/s40429-020-00325-9">https://doi.org/10.1007/s40429-020-00325-9</a></p>
<p>Nebeker, C., Bartlett Ellis, R. J., & Torous, J. (2020). Development of a decision-making checklist tool to support technology selection in digital health research. <i>Translational Behavioral Medicine</i>, 10(4), 1004–1015. <a href="https://doi.org/10.1093/tbm/ibz074">https://doi.org/10.1093/tbm/ibz074</a></p>
<p>Pini, N., Fifer, W. P., Oh, J., Nebeker, C., Croff, J. M., Smith, B. A., & Novel Technology/Wearable Sensors Working Group. (2024). Remote data collection of infant activity and sleep patterns via wearable sensors in the HEALthy Brain and Child Development Study (HBCD). <i>Developmental Cognitive Neuroscience</i>, 69(101446), 101446. <a href="https://doi.org/10.1016/j.dcn.2024.101446">https://doi.org/10.1016/j.dcn.2024.101446</a></p>  
<p>Pini, N., Ong, J. L., Yilmaz, G., Chee, N. I. Y. N., Siting, Z., Awasthi, A., Biju, S., Kishan, K., Patanaik, A., Fifer, W. P., & Lucchini, M. (2022). An automated heart rate-based algorithm for sleep stage classification: Validation using conventional polysomnography and an innovative wearable electrocardiogram device. <i>Frontiers in Neuroscience</i>, 16, 974192. <a href="https://doi.org/10.3389/fnins.2022.974192">https://doi.org/10.3389/fnins.2022.974192</a></p> 
<p>Zinzuwadia, A., & Singh, J. P. (2022). Wearable devices-addressing bias and inequity. <i>The Lancet Digital Health</i>, 4(12), e856–e857. <a href="https://doi.org/10.1016/S2589-7500(22)00194-7">https://doi.org/10.1016/S2589-7500(22)00194-7</a></p>
</div>
