# Raw BIDS & Processed Derivative File-Based Data

## Raw BIDS

The `rawdata/` folder includes raw <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> magnetic resonance imaging (MRI), spectroscopy (MRS), electroencephalography (EEG), and motion/accelerometry (i.e. [wearable sensor](../instruments/sensors/wearsensors.md) recordings for leg motion) data, converted to BIDS and organized under subject and session-specific directories for processing through BIDS App pipelines ([see details](../instruments/processing/index.md)). *Note that the folder and file counts may vary across subjects and sessions, which is expected in a large-scale infant MRI study.*

<pre class="folder-tree">
hbcd/
|__ rawdata/ 
    |__ sub-<span class="label">&lt;label&gt;</span>/
    |   |__ sub-<span class="label">&lt;label&gt;</span>_sessions.tsv
    |   |__ sub-<span class="label">&lt;label&gt;</span>_sessions.json
    |   |__ ses-<span class="label">&lt;label&gt;</span>/
    |       |__ anat/
    |       |__ dwi/
    |       |__ eeg/
    |       |__ fmap/
    |       |__ func/
    |       |__ motion/
    |       |__ mrs/
    |       |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_scans.tsv
    |       |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_scans.json
    |
    |__ dataset_description.json
    |__ participants.tsv
    |__ participants.json 
</pre>

## Participant-, Session-, & Scan-Level Data
Participant-, session-, and scan-level data are stored in standardized `.tsv` files, accompanied by a `.json` sidecar file that defines the columns and describes the data fields, located in the `rawdata/` directory and its subdirectories:

- **Participant-level**: Stored in `rawdata/participants.tsv`, this file includes basic demographic and participant information (e.g., sex).
- **Session-level**: Stored in `sub-<label>_sessions.tsv` within each subject folder, this file includes session information such as collection site, the participant’s age at each session, and head size.
- **Scan-level**:  Each session folder includes a `sub-<label>_ses-<label>_scans.tsv` file with per-scan information including participant age at scan as well as all raw data QC scores (see [HBCD MR Quality Control Procedures](../instruments/mri/qc.md#location-of-raw-data-qc-results-in-data-release)).

### Fields Reporting Age

See description of fields reporting age under Age Variable Definitions > <a href="../../instruments/agevariables/#raw-file-based-data" target="_blank">Raw File-Based Data</a>.



## Processed Derivatives

The `derivatives/` folder contains derivatives, which are file outputs from <a href="../../instruments/processing/" target="_blank">processing pipelines</a>. 

<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    <span class="hashtag"># Structural & Functional MRI</span>             
    |__ mriqc/      
    |__ bibsnet/    
    |__ nibabies/   
    |__ freesurfer/ 
    |__ mcribs/     
    |__ xcp_d/      
    |               
    <span class="hashtag"># Quantitative MRI</span>    
    |__ symri/           
    |__ qmri_postproc/  
    | 
    <span class="hashtag"># Diffusion MRI</span>                                  
    |__ qsiprep/                         
    |__ qsirecon/                        
    |__ qsirecon-DIPYDKI/                
    |__ qsirecon-DSIStudio/               
    |__ qsirecon-NODDI/                  
    |__ qsirecon-TORTOISE_model-MAPMRI/  
    |__ qsirecon-TORTOISE_model-tensor/  
    |
    |__ osprey/       <span class="hashtag"># MRS</span>
    |__ made/         <span class="hashtag"># EEG</span>
    |__ hbcd_motion/  <span class="hashtag"># Biosensors Recordings</span>
</pre>
