ORIG:
## Derivatives Highlight

Below is a summary of key MRI derivatives used for structural morphology and resting-state functional MRI (rsfMRI) functional connectivity analyses. Key derivatives, produced by the [XCP-D](https://xcp-d.readthedocs.io/en/latest/) pipeline, include volumetric and surface-based time series for each participant. The data release also includes dense and parcellated time series with at least 2.5 minutes of low-motion data (FD>0.3), functional connectivity matrices, regional homogeneity values, and amplitude of low-frequency fluctuation values. 


TEMP FILE:

### Reading the File Patterns

The patterns below show paths relative to a participant/session derivative directory:

- `anat/` contains anatomical derivatives; `func/` contains functional derivatives.
- `*` represents the filename prefix, including participant/session identifiers and any additional entities.
- `{PARC}` represents a [parcellation identifier](#parc).
- Braces containing alternatives, such as `{curv|sulc|thickness}`, indicate separate files for each listed measure.
- `{L|R}` identifies the left or right hemisphere; `{X}` represents a run number.


### Usable Data Requirements
The release includes dense and parcellated time series with at least **2.5 minutes of low-motion data**, using an **FD threshold of 0.3 mm** for motion censoring.

Before analysis:

- Check the usable data duration and motion characteristics for each run.
- Confirm the processing configuration, parcellation, and smoothing variant selected for your analysis.
- Apply any additional data quality or duration criteria required by your analysis plan.

