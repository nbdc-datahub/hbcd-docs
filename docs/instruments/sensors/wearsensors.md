<!-- <style>
.wy-nav-content {
    width: 85% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style> -->

# Infant Leg Motion

{{ readme_summary(instruments.motion) }}
{{ alert_warning(instruments.motion) }}
{{ data_warning(instruments.motion) }}
{{ issues_banner() }}

## Release Data

Motion/accelerometry data collected from wearable infant leg sensors include raw and processed sensor recordings:

- <i class="fa fa-hammer header-icon"></i> [Raw BIDS](../../datacuration/file-based-data.md#file-based-data)</a> Axivity AX6 wearable sensor data stored under subject/session-specific `motion/` folders
- <i class="fas fa-cog header-icon"></i> [Derivatives](../../datacuration/file-based-data.md/#derivatives) from the HBCD-Motion pipeline stored under `hbcd_motion/`


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
<p>
The raw data include recordings from the left and right leg sensors (<code>motion.tsv</code>) with corresponding <code>channels.tsv</code> files describing each column (and sidecar JSON files with metadata). See <a href="https://doi.org/10.1038/s41597-024-03559-8">Jeung et al., 2024</a> for BIDS conversion procedures.</p>
<p><a href="../../../datacuration/overview/#filetrees"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>
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

<div id="derivatives" class="banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
    <span class="text">HBCD-Motion Derivatives</span>
  <a class="anchor-link" href="#derivatives" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Axivity Ax6 sensor recordings of infant leg movements across 72 continuous hours are processed via the HBCD-Motion pipeline. Derivative files are explained in the <a href="https://hbcd-motion-postproc.readthedocs.io/">HBCD-Motion documentation</a>.</p>
<p><a href="../../../datacuration/overview/#filetrees"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>
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

## Instrument Details

{{ instrument_description(instruments.motion) }}
{{ hbcd_mods(instruments.motion) }}
{{ scoring(instruments.motion) }}
{{ references(instruments.motion) }}
