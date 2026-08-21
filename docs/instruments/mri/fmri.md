
# Functional MRI

{{ alert_warning(instruments.fmri) }}
{{ data_warning(instruments.fmri) }}
{{ issues_banner() }}

<p></p>

<!-- ##### Overview & Acquisition -->
{{ instrument_description(instruments.fmri) }}

## Quality Control Summary Statistics

We evaluated the impact of data quality on functional connectivity. Average functional connectivity matrices were computed using the Gordon-parcellated time series available in the V02 XCP-D derivatives. Data were included based on varying thresholds of <a href="../qc/#brainswipes">BrainSwipes</a> QC scores. Functional connectivity patterns were not substantially altered with the inclusion of lower-quality data, indicating robustness to mild quality variation

**Connectivity matrices as data quality improves (left -> right) based on QC thresholds of 0.1, 0.5, and 0.9:**
<img src="../images/fconn_qc.png" style="width: 90%;" class="center">


{{ references(instruments.fmri) }}
