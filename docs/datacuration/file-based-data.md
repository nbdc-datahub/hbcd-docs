# File-Based Data: Raw BIDS & Processed Derivatives

## Raw BIDS

The `rawdata/` folder includes raw <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> magnetic resonance imaging (MRI), spectroscopy (MRS), electroencephalography (EEG), and motion/accelerometry (i.e. [wearable sensor](../instruments/sensors/wearsensors.md) recordings for leg motion) data, converted to BIDS and organized under subject and session-specific directories for processing through BIDS App pipelines ([see details](../instruments/processing/index.md)). *Note that the folder and file counts may vary across subjects and sessions, which is expected in a large-scale infant MRI study.*

<pre class="folder-tree">
hbcd/
|__ rawdata/ 
    |__ sub-<span class="label">{ID}</span>/
    |   |__ sub-<span class="label">{ID}</span>_sessions.tsv
    |   |__ sub-<span class="label">{ID}</span>_sessions.json
    |   |__ ses-<span class="label">{V0X}</span>/
    |       |__ anat/
    |       |__ dwi/
    |       |__ eeg/
    |       |__ fmap/
    |       |__ func/
    |       |__ motion/
    |       |__ mrs/
    |       |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_scans.tsv
    |       |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_scans.json
    |
    |__ dataset_description.json
    |__ participants.tsv
    |__ participants.json 
</pre>

### Participant-, Session-, & Scan-Level Data
Participant-, session-, and scan-level data are stored in standardized `.tsv` files, accompanied by a `.json` sidecar file that defines the columns and describes the data fields, located in the `rawdata/` directory and its subdirectories:

- **Participant-level**: Stored in `rawdata/participants.tsv`, this file includes basic demographic and participant information (e.g., sex).
- **Session-level**: Stored in `sub-<label>_sessions.tsv` within each subject folder, this file includes session information such as collection site, the participant’s age at each session, and head size.
- **Scan-level**:  Each session folder includes a `sub-<label>_ses-<label>_scans.tsv` file with per-scan information including participant age at scan as well as all raw data QC scores (see [HBCD MR Quality Control Procedures](../instruments/mri/qc.md#location-of-raw-data-qc-results-in-data-release)).

### Fields Reporting Age

See description of fields reporting age under Age Variable Definitions > <a href="../../instruments/agevariables/#raw-file-based-data" target="_blank">Raw File-Based Data</a>.

### Modality-Level Descriptions

- [EEG](../instruments/eeg/index.md#raw-bids)
- [Motion](../instruments/sensors/wearsensors.md#raw-bids)
- [MRS](../instruments/mrs/index.md#raw-bids)
- [dMRI](../instruments/mri/dmri.md#raw-bids)
- [qMRI](../instruments/mri/qmri.md#release-data)
- [sMRI](../instruments/mri/smri.md#raw-bids)
- [fMRI](../instruments/mri/fmri.md#raw-bids)


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

### Guide To File Tree Visuals

**The following formatting was employed to enhance readability of the file structure visuals:**

*   Some entities include a set of specific values, each of which is associated with a separate file: these values are either enclosed within `<>` as a list, separated by `|`, or listed in a **Label Values Legend**
*   For brevity, sidecar JSON files containing metadata for the corresponding data file may not be displayed, in which case files with corresponding JSONs are labeled with `(+JSON)` after the filename
*   Several pipelines produce an `.html` visual summary report intended to be used for quality assessment of processed outputs. These files, typically located at either the pipeline folder or session-level, source their images from a `figures/` folder found in the derivatives. For readability, the contents of the `figures/` folders are not listed


### Modality-Level Descriptions

- [EEG](../instruments/eeg/index.md#derivatives)
- [Motion](../instruments/sensors/wearsensors.md#derivatives)
- [MRS](../instruments/mri/mrs.md#derivatives)
- [dMRI](../instruments/mri/dmri.md#derivatives)
- [qMRI](../instruments/mri/qmri.md#derivatives)