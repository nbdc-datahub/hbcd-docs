# Infant Heart Rate (GABI)

{{ readme_summary(instruments.gabi) }}
{{ alert_warning(instruments.gabi) }}
{{ data_warning(instruments.gabi) }}
{{ issues_banner() }}

## Release Data

Infant heart rate data collected from wearable sensors includes:

- <i class="fa fa-hammer header-icon"></i> [Raw BIDS](../../datacuration/file-based-data.md#file-based-data)</a> stored under subject- and session-specific `gabi/` folders
- <i class="fas fa-cog header-icon"></i> [Derivatives](../../datacuration/file-based-data.md/#derivatives) will be available in a future release 

<div id="rawbids" class="banner" onclick="toggleCollapse(this)" style="background-color: #dde6fe;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
  <span class="text">Raw BIDS</span>
  <a class="anchor-link" href="#rawbids" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>The raw data contain the heart rate (HR), the blood oxygen saturation (SpO2), and the respiratory rate (RR), along with their respective measures of reliability, timestamps and metadata.</p>
<pre class="folder-tree">
hbcd/
└── rawdata/ 
    └── sub-<span class="label">&lt;label&gt;</span>/   <span class="hashtag"># Raw sensor data</span>
        └── ses-<span class="label">&lt;label&gt;</span>/
            └── gabi/
</pre>
</div>


<!-- <div id="derivatives" class="banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
    <span class="text">Derivatives</span>
  <a class="anchor-link" href="#derivatives" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
</div> -->

## Instrument Details

{{ instrument_description(instruments.gabi) }}
{{ hbcd_mods(instruments.gabi) }}
{{ scoring(instruments.gabi) }}
{{ references(instruments.gabi) }}







<!-- 
## Data Acquisition

**Infant heart rate sensor data** collected by the infant heart rate wearable sensor for HBCD captures information related to the infant's physiology and sleep. The device is fastened to the infant's upper arm with a soft-textile band by HBCD Study staff and worn for 72 hours, during which time data is collected across the child's typical activities in their natural environment. The photoplethysmography (PPG) sensors (one emitting green light PPG and one emitting red light PPG) embedded in the device allow for the collection of three biosignal estimates sampled at 1 Hz: 

 - **Rulse rate** (beats per minute)
 - **Blood oxygen saturation** (SpO<sub>2</sub>, percentage)
 - **Respiratory rate** (breaths per minute)

In addition, sleep states are derived from these vital sign data. Data collection is planned for 72 continuous hours. Caregivers followed typical routines, removing the sensor only for water exposure (e.g., baths) and repositioning it afterward. See [Pini et al. 2024](https://www.sciencedirect.com/science/article/pii/S1878929324001075?via%3Dihub) for a full measure description.


## Quality Control

For the infant heart rate wearable sensor (the 72-hour sensor data files), a random selection of files was manually reviewed on a weekly basis for the presence of data, adequate file duration, and discrepancies with the set-up/return forms. Note that only a small percentage of the total infant heart rate wearable sensor data files were reviewed because the procedure was manual.

Issues with the sensor data were generally rare, and most data were deemed present and accurately collected (when captured correctly). Errors that did arise were corrected, when possible, though this was typically not feasible. Common errors noted included inadequate or missing data (due to human error, technical issues, or a parent/legal guardian declining participation in this aspect of the study), sensors being removed for extended periods during the 72-hour collection, or unavailability of devices to conduct the data collection. -->
