# Infant Heart Rate (GABI)

{{ readme_summary(instruments.gabi) }}
{{ alert_warning(instruments.gabi) }}
{{ data_warning(instruments.gabi) }}
{{ issues_banner() }}

## Release Data

{{ instrument_description(instruments.gabi) }}


##### Raw BIDS
The raw data includes HR, SpO2, and RR along with their respective measures of reliability, timestamps, and metadata.

<pre class="folder-tree">
hbcd/
└── rawdata/ 
    └── sub-<span class="label">&lt;label&gt;</span>/
        └── ses-<span class="label">&lt;label&gt;</span>/
            └── gabi/
</pre>


##### Derivatives

Derivatives include processed, analysis-ready data.

---

{{ references(instruments.gabi) }}







<!-- 

## Quality Control

For the infant heart rate wearable sensor (the 72-hour sensor data files), a random selection of files was manually reviewed on a weekly basis for the presence of data, adequate file duration, and discrepancies with the set-up/return forms. Note that only a small percentage of the total infant heart rate wearable sensor data files were reviewed because the procedure was manual.

Issues with the sensor data were generally rare, and most data were deemed present and accurately collected (when captured correctly). Errors that did arise were corrected, when possible, though this was typically not feasible. Common errors noted included inadequate or missing data (due to human error, technical issues, or a parent/legal guardian declining participation in this aspect of the study), sensors being removed for extended periods during the 72-hour collection, or unavailability of devices to conduct the data collection. -->
