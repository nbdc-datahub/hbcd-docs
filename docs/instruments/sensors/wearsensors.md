# Infant Leg Motion

{{ readme_summary(instruments.motion) }}
{{ alert_warning(instruments.motion) }}
{{ data_warning(instruments.motion) }}
{{ issues_banner() }}

## Release Data

{{ instrument_description(instruments.motion) }}

##### Raw BIDS

The raw data include recordings from the left and right Axivity AX6 leg sensors (`motion.tsv`) with corresponding `channels.tsv` files describing each column (and sidecar JSON files with metadata). See [Jeung et al., 2024](https://doi.org/10.1038/s41597-024-03559-8) for BIDS conversion procedures.
<pre class="folder-tree">
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
<p><a href="../../../datacuration/overview/#filetrees"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>


##### Derivatives

Axivity Ax6 sensor recordings of infant leg movements across 72 continuous hours are processed via the HBCD-Motion pipeline, which output the following processed derivative files. See derivative documentation in the [HBCD-Motion documentation](https://hbcd-motion-postproc.readthedocs.io/).
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

---

{{ references(instruments.motion) }}
