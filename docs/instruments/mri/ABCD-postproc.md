## Post-Processing: ReproTM & ModelArrayIO

### QSIRecon ModelArray

```{ojs}
//| echo: false

data = [
  {subtype: "DIPY", param: "fa", description: "Fractional Anisotropy (tensor model)"},
  {subtype: "DIPY", param: "ad", description: "Axial Diffusivity"},
  {subtype: "DIPY", param: "rd", description: "Radial Diffusivity"},
  {subtype: "DIPY", param: "md", description: "Mean Diffusivity"},
  {subtype: "DIPY", param: "ak", description: "Axial Kurtosis (DKI model)"},
  {subtype: "DIPY", param: "mk", description: "Mean Kurtosis (DKI model)"},
  {subtype: "DIPY", param: "mkt", description: "Mean Kurtosis Tensor"},
  {subtype: "DIPY", param: "rk", description: "Radial Kurtosis"},
  {subtype: "DIPY", param: "kfa", description: "Kurtosis Fractional Anisotropy"},
  {subtype: "DSIStudio", param: "fa", description: "Fractional Anisotropy (tensor)"},
  {subtype: "DSIStudio", param: "ad", description: "Axial Diffusivity"},
  {subtype: "DSIStudio", param: "rd", description: "Radial Diffusivity"},
  {subtype: "DSIStudio", param: "md", description: "Mean Diffusivity"},
  {subtype: "DSIStudio", param: "ha", description: "Helix Angle"},
  {subtype: "DSIStudio", param: "gfa", description: "Generalized Fractional Anisotropy (GQI)"},
  {subtype: "DSIStudio", param: "qa", description: "Quantitative Anisotropy (GQI)"},
  {subtype: "DSIStudio", param: "iso", description: "Isotropic Diffusion"},
  {subtype: "DSIStudio", param: "rd1", description: "Restricted Diffusion Index 1"},
  {subtype: "DSIStudio", param: "rd2", description: "Restricted Diffusion Index 2"},
  {subtype: "TORTOISE", param: "fa", description: "Fractional Anisotropy (tensor)"},
  {subtype: "TORTOISE", param: "ad", description: "Axial Diffusivity"},
  {subtype: "TORTOISE", param: "rd", description: "Radial Diffusivity"},
  {subtype: "TORTOISE", param: "am", description: "Axial Mean Diffusivity"},
  {subtype: "TORTOISE", param: "li", description: "Linearity Index"},
  {subtype: "TORTOISE", param: "ng", description: "Non-Gaussianity (MAP-MRI)"},
  {subtype: "TORTOISE", param: "ngpar", description: "Non-Gaussianity (parallel)"},
  {subtype: "TORTOISE", param: "ngperp", description: "Non-Gaussianity (perpendicular)"},
  {subtype: "TORTOISE", param: "pa", description: "Propagator Anisotropy"},
  {subtype: "TORTOISE", param: "path", description: "Propagator Anisotropy (thresholded)"},
  {subtype: "TORTOISE", param: "rtap", description: "Return-to-Axis Probability"},
  {subtype: "TORTOISE", param: "rtop", description: "Return-to-Origin Probability"},
  {subtype: "TORTOISE", param: "rtpp", description: "Return-to-Plane Probability"},
  {subtype: "wmNODDI", param: "icvf", description: "Intracellular Volume Fraction"},
  {subtype: "wmNODDI", param: "isovf", description: "Isotropic Volume Fraction"},
  {subtype: "wmNODDI", param: "od", description: "Orientation Dispersion Index"},
]

subtypeColors = ({
  "DIPY":      {bg: "#EEEDFE", color: "#3C3489"},
  "DSIStudio": {bg: "#E1F5EE", color: "#085041"},
  "TORTOISE":  {bg: "#FAEEDA", color: "#633806"},
  "wmNODDI":   {bg: "#FAECE7", color: "#712B13"},
})

viewof selected = {
  const wrapper = html`<div style="display:flex; align-items:center; gap:10px; margin-bottom:4px;">
    <label style="font-size:0.85rem; color:#475569; white-space:nowrap; margin:0;">Select reconstruction method to view associated <code>&lt;PARAM&gt;</code> values:</label>
    <select style="font-size:0.85rem; padding:4px 8px; border:1px solid #e2e8f0; border-radius:6px; color:#334155; background:#fff; cursor:pointer;">
      <option value="" selected disabled><i>Select</i></option>
      <option value="DIPY">DIPY</option>
      <option value="DSIStudio">DSIStudio</option>
      <option value="TORTOISE">TORTOISE</option>
      <option value="wmNODDI">wmNODDI</option>
    </select>
  </div>`

  const sel = wrapper.querySelector("select")
  sel.addEventListener("input", () => wrapper.value = sel.value || null)

  wrapper.value = null
  return wrapper
}

filtered = selected === "All" ? data : data.filter(d => d.subtype === selected)

html`<style>
  .param-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
  .param-table thead tr { border-bottom: 2px solid #e2e8f0; }
  .param-table th { text-align: left; padding: 10px 14px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; color: #64748b; }
  .param-table td { padding: 9px 14px; border-bottom: 1px solid #f1f5f9; vertical-align: middle; }
  .param-table tbody tr:last-child td { border-bottom: none; }
  .param-table tbody tr:hover td { background: #f8fafc; }
  .badge { display: inline-block; padding: 2px 10px; border-radius: 999px; font-size: 0.72rem; font-weight: 600; letter-spacing: 0.03em; }
  .param-code { font-family: ui-monospace, monospace; font-size: 0.82rem; background: #f1f5f9; color: #334155; padding: 2px 7px; border-radius: 4px; }
  .desc-text { color: #475569; }
  .table-wrap { border: 1px solid #e2e8f0; border-radius: 10px; overflow: hidden; margin-top: 12px; }
  .table-footer { padding: 8px 14px; font-size: 0.78rem; color: #94a3b8; background: #f8fafc; border-top: 1px solid #f1f5f9; }
</style>

<div class="table-wrap">
  <table class="param-table">
    <thead>
      <tr>
        <th>Reconstruction Method</th>
        <th>Param</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      ${filtered.map(d => {
        const c = subtypeColors[d.subtype];
        return html`<tr>
          <td><span class="badge" style="background:${c.bg}; color:${c.color}">${d.subtype}</span></td>
          <td><span class="param-code">${d.param}</span></td>
          <td class="desc-text">${d.description}</td>
        </tr>`
      })}
    </tbody>
  </table>
</div>`
```

---

### XCP-D ModelArray

XCP-D-ModelArray outputs include cohort-level HDF5 arrays aggregating structural and functional derivatives, including:

  - **[1]** Surface morphometry (curvature, sulcal depth, cortical thickness)  
  - **[2]** Functional maps (ALFF, ReHo)  
  - **[3]** Resting-state functional connectivity.`<ATLAS>` = `Gordon`, `HCP`, `MIDB`

```default
abcd/
└── derivatives/
    └── abcc-xcp_d_v0.13.0-ModelArray/

    # Surface morphometry [1]
        ├── xcp_d_v0.13.0_param-<curv|sulc|thickness>.h5
        ├── xcp_d_v0.13.0_param-<curv|sulc|thickness>.csv

    # Functional maps [2]
        ├── xcp_d_v0.13.0_param-<alff|reho>.h5
        ├── xcp_d_v0.13.0_param-<alff|reho>.csv

    # Resting-state functional connectivity [3]
        ├── xcp_d_v0.13.0_task-rest_seg-<ATLAS>_param-pearsoncorrelation.h5
        └── xcp_d_v0.13.0_task-rest_seg-<ATLAS>_param-pearsoncorrelation.csv
```
---

## ReproTM 

Reproducible Template Matching ([ReproTM](https://github.com/KateJGodfrey/ReproTM)) [@godfrey2026reprotm] is a Python pipeline that generates individualized (i.e., subject-specific) functional network maps from dense functional connectivity data using the template matching network detection algorithm [@gordon2017; @hermosillo2024]. 

ReproTM compares the functional connectivity profile of each greyordinate against a set of canonical resting-state functional network templates to produce subject-specific functional network assignments. The primary output is a labeled CIFTI (`.dlabel.nii`) file assigning each greyordinate to one of 15 functional networks defined within the ABCC 2026 template.

### ABCC 2026 Template Networks

The ABCC 2026 templates were derived from ABCC Group 3 (n = 561 subjects) to capture canonical functional network patterns optimized for the developmental age range and scanning parameters of the ABCC cohort. The template set includes 15 canonical functional resting state networks:

::: {.callout-note title="ABCC 2026 Functional Networks"}
| | | |
|---|---|---|
| **[1]** Default Mode<br>**[2]** Visual<br>**[3]** Frontoparietal<br>**[4]** Dorsal Attention<br>**[5]** Ventral Attention | **[6]** Salience<br>**[7]** Action Mode<br>**[8]** Sensorimotor Dorsal<br>**[9]** Sensorimotor Lateral<br>**[10]** Auditory | **[11]** Temporal Pole<br>**[12]** Medial Temporal Lobe<br>**[13]** Parietal Memory<br>**[14]** Parietal Occipital<br>**[15]** Somato-Cognitive Action |
::: 

---

### Outputs

ReproTM derivatives include greyordinate-wise network assignments (`.dlabel.nii`) and intermediate greyordinate-to-network similarity matrices and assignments (`.mat`) organized under `abcc-ReproTM/`:

```default
abcc-ReproTM/
├── templates/
│   └── tpl-ABCC2026-a3-9to16_space-fsLR_den-91k_desc-seedmap_stat-zscored.mat
│
└── sub-<label>/
    └── ses-<label>/
        └── func/
            ├── *.dlabel.nii    # Final network assignments
            └── *.mat           # Intermediate metrics and assignments
```

 - The **`.dlabel.nii`** file contains greyordinate-wise functional network assignments derived from the preprocessed and denoised BOLD timeseries using the ABCC 2026 template networks. 
 - The accompanying **`.mat`** file contains ReproTM intermediates from which the grayordinate-wise network assignments were derived, including:
    - Similarity values (eta and linear bivariate r) for each greyordinate to every template network
    - Network assignments pre- and post-SCAN network refinements

::: {.callout-note collapse="true" title="Full Output Filenames"}
```
sub-<label>_ses-<label>_task-rest
  _space-fsLR_den-91k
  _desc-denoised-spatially-interpolated-smoothed-2.25mm-censor-ReproTM
  _template-ABCC-a3-9to16
  _refine-SCAN_minsize-30
  _boldmap.{dlabel.nii|mat}
```
:::

---

### Processing

Prior to running ReproTM, subject-level dense connectivity matrices (`dconn.nii`) were generated from XCP-D resting state timeserives derivatives using [cifti-connectivity](https://github.com/DCAN-Labs/cifti-connectivity). ReproTM v1.0.0 was then applied to compare dense connectivity matrices to the ABCC 2026 group-level template file provided in the derivatives and in the ReproTM Github repository.

**Cifti-Connectivity Workflow & Parameters**

1. Interpolate timeseries for zero-value greyordinates using the mean and standard deviation of greyordinates in the same structure.
2. Spatial smoothing.
3. Dense connectivity matrix generation with motion censoring.

::: {.callout-note collapse="true" title="Detailed `cifti-connectivity` Parameters"}
- **Input data:**
  - Denoised resting-state CIFTI timeseries (`*_desc-denoised_bold.dtseries.nii`)
  - Anatomical surface files in fsLR 32k space
  - Quality control outputs (`*_desc-abcc_qc.hdf5`)
- **Parameters:**
  - Repetition time: 0.8 s
  - Motion threshold: FD < 0.2 mm
  - Minimum usable data: 10 minutes
  - Spatial smoothing: 2.25 mm FWHM
:::

**ReproTM Workflow & Parameters**

4. Z-score connectivity matrices across greyordinates
5. Perform template matching with initial template network thresholding (z=1.00)
6. Perform optional refinement of somatomotor and somato-cognitive action networks with higher template network thresholding (`z=3.00`)
7. Apply minimum network size filtering (minimum 30 vertices)
8. Convert outputs to labeled CIFTI format (`.dlabel.nii`)

::: {.callout-note collapse="true" title="Detailed `ReproTM` Parameters"}
*Parameters are included in the run command used to generate ReproTM outputs for ABCC below:*
```bash
python3 ReproTM_v1.0.0.py \
  ${zscored_dconn_file} \
  --template_infile \
    tpl-ABCC2026-a3-9to16_space-fsLR_den-91k_desc-seedmap_stat-zscored.mat \
  --template_networks \
    "DMN Vis FP NaN DAN NaN VAN Sal AMN \
     SMd SMl Aud Tpole MTL PMN PON NaN SCAN" \
  --template_thresholding \
  --template_minthreshold 1 \
  --refineSCAN \
  --refineSCAN_minthreshold 3
```
:::