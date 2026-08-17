# EEG Release Data

{{ alert_warning(instruments.eeg) }}
{{ data_warning(instruments.eeg) }}
{{ issues_banner() }}

---

EEG release data include the following:


- **[Raw BIDS](#raw-eeg-bids)**: Raw imaging/spectroscopy data in the standardized BIDS format under `eeg/`
- **[HBCD-MADE pipeline derivatives](#hbcd-made-derivatives)**: Processed, analysis-ready pipeline outputs
- **[Tabular EEG](../index.md#eeg-tabular-eeg)**: Questionnaires/forms and tabulated HBCD-MADE derivatives

---

## Raw EEG BIDS

<div id="bids-conversion" class="banner" onclick="toggleCollapse(this)">
<span class="emoji">
    <i class="fas fa-arrows-rotate"></i>
</span>
<span class="text-with-link">
    <span class="text">BIDS Conversion Procedures</span>
    <a class="anchor-link" href="#bids-conversion" title="Copy link">
    <i class="fa-solid fa-link"></i>
    </a>
</span>
<span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>BIDS conversion was performed with the <a href="https://github.com/aces/eeg2bids">EEG2BIDS Wizard</a>, a custom MATLAB application for HBCD EEG data management and formatting, installed at all HBCD sites. After each EEG session, raw data are uploaded to the Wizard, which converts them to the BIDS standard.</p>
</div>
<p></p>

Each participant’s BIDS `eeg/` folder contains task-specific .set and .fdt EEG recordings, along with channel metadata (*channels* and *events* TSV files). Electrodes are placed on either the head or chest (*acq-eeg/ecg*) and electrode placement information is stored in *electrodes* TSV files accompanied by *coordsystem* JSON files that define the Cartesian coordinates. Finally, the `sourcedata/` subfolder includes impedance measurements (*impedances* JSON) used to ensure good electrode contact and task *eventlogs* txt files describing stimulus presentation timing.

<pre class="folder-tree">
<span><a href="../../../datacuration/overview/#filetrees"><i class="fa fa-circle-info"></i> How To Read File Trees →</a></span>
hbcd/
└── rawdata/
    └── sub-[ID]/
        └── ses-[V0X]/
            └── eeg/
              <span class="hashtag"># Task Acquisitions</span>
                ├── *_task-<span class="var">{FACE|MMN|RS|VEP}</span>_acq-<span class="var">{eeg|ecg}</span>_run-[X]_channels.tsv
                ├── *_task-<span class="var">{FACE|MMN|RS|VEP}</span>_acq-<span class="var">{eeg|ecg}</span>_run-[X]_eeg.set <span class="hashtag">(+JSON)</span>
                ├── *_task-<span class="var">{FACE|MMN|RS|VEP}</span>_acq-<span class="var">{eeg|ecg}</span>_run-[X]_events.tsv <span class="hashtag">(+JSON)</span>
                ├── *_task-<span class="var">{FACE|MMN|RS|VEP}</span>_acq-eeg_run-[X]_eeg.fdt
              <span class="hashtag"># Electrode Placement</span>
                ├── *_acq-eeg_space-<span class="var">{CapTrak|CTF}</span>_electrodes.tsv
                ├── *_acq-eeg_space-<span class="var">{CapTrak|CTF}</span>_coordsystem.json
                └── sourcedata/
                    ├── *_acq-eeg_flags.json
                    ├── *_acq-eeg_impedances.json
                    └── *_task-<span class="var">{FACE|MMN|RS|VEP}</span>_acq-eeg_run-[X]_eventlogs.txt
</pre>

---

## HBCD-MADE Derivatives

EEG data were processed using [HBCD-MADE](https://docs-hbcd-made.readthedocs.io/), an adaptation of the Maryland Analysis of Developmental EEG (MADE) pipeline ([Debnath et al., 2020](https://doi.org/10.1111/psyp.13580)) developed specifically for the HBCD Study. HBCD-MADE is implemented as a containerized BIDS App that adheres to HBCD processing and derivative data standards. Full documentation of processing parameters, pipeline configuration, and file selection logic is available at the official [HBCD-MADE documentation site](https://docs-hbcd-made.readthedocs.io/) and external [HBCD Processing website](https://hbcd-cbrain-processing.readthedocs.io/release_2.0/tools/made.html).

<pre class="folder-tree">
<span><a href="../../../datacuration/overview/#filetrees"><i class="fa fa-circle-info"></i> How To Read File Trees →</a></span>
hbcd/
└── derivatives/
    └── made/
        └── sub-[ID]/
            └── ses-[V0X]/
                └── eeg/
                    ├── filtered_data/
                    │   └── *_task-<span class="var">{FACE|MMN|RS|VEP}</span>_acq-eeg_run-[X]_desc-filtered_eeg<span class="var">{.fdt|.set}</span>
                    │
                    ├── ica_data/
                    │   ├── *_adjustReport.txt
                    │   └── *_desc-mergedICA_eeg<span class="var">{.fdt|.set}</span>
                    │
                    ├── merged_data/
                    │   └── *_desc-merged_eeg<span class="var">{.fdt|.set}</span>
                    │   └── *_desc-merged_eeg.json
                    │
                    ├── processed_data/
                    │   ├── *.jpg <span class="comment"># Topographic and ERP plots- <a href="https://docs-hbcd-made.readthedocs.io/en/latest/expected-outputs/#expected-outputs-from-hbcd-made">see details</a></span>
                    │   ├── *_task-RS_<span class="var">{Log|db|Abs}</span>PowerSpectra.csv
                    │   ├── *_task-RS_spectra.mat
                    │   ├── *_task-<span class="var">{FACE|MMN|VEP}</span>_ERPSummaryStats.csv
                    │   ├── *_task-<span class="var">{FACE|MMN|VEP}</span>_ERPTrialMeasures.csv
                    │   ├── *_task-<span class="var">{FACE|MMN|VEP}</span>_acq-eeg_run-[X]_ERP.mat
                    │   └── *_task-<span class="var">{FACE|MMN|RS|VEP}</span>_acq-eeg_run-[X]_desc-filteredprocessed_eeg<span class="var">{.fdt|.set}</span>
                    │
                    ├── *_acq-eeg_preprocessingReport.csv
                    └── *_task-<span class="var">{FACE|MMN|RS|VEP}</span>_acq-eeg_run-[X]_MADEspecification.json
</pre>

##### File Selection For Processing

Not all raw EEG sessions are eligible for processing. Inclusion in the HBCD-MADE pipeline requires that sessions meet predefined quality control criteria. Common causes of exclusion include missing EEG capping images or very poor capping quality. For participants with multiple EEG acquisition attempts within a session, only the final run was processed and included in the MADE derivatives.

---

{{ references(instruments.eeg) }}
