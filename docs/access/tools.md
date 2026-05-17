<style>
.wy-nav-content {
    width: 85% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>

# Recommended Programs & Utilities

## Download Platforms
HBCD study data can be downloaded via the [NBDC Data Access Platform](https://nbdc-datashare.lassoinformatics.com/) or [DEAP](https://hbcd.deapscience.com/#/home")- see [Access & Download Data](download.md#explore-download).

## Tabulated Data

### <i class="fas fa-database header-icon"></i> NBDC Sandbox   
The [NBDC Sandbox](https://nbdc-safe.lassoinformatics.com/pun/sys/dashboard) provides a secure, cloud-based analysis environment designed to support data analysis workflows, particularly for neuroimaging and large-scale tabular datasets, without having to download and manage data locally. See the [NBDC Sandbox Tutorial Series](https://hdcc-sandbox-rtd.readthedocs.io/latest/) to get started.

### <i class="fas fa-database header-icon"></i> NBDCtools
NBDCtools, available in both [R](https://software.nbdc-datahub.org/NBDCtools/) and [Python](https://software.nbdc-datahub.org/nbdctools-py/), is a package for creating custom, analysis-ready datasets by simply specifying the variable or table names you need. NBDCtools automatically retrieves the specified columns from locally downloaded HBCD tabulated data and assembles them into a single in-memory data frame, minimizing storage and memory use. This provides a flexible alternative to building datasets through the NBDC Data Access Platform or DEAP, eliminating the need to manually parse files or resolve formatting issues. In addition to dataset assembly, NBDCtools includes functions for working with shadow matrices as well as applying transformations and filters.   

## Brain Imaging Data

#### <i class="fa-solid fa-eye header-icon"></i> ITK-Snap & FSLeyes
For interactive visualization of MRI images, we recommend using either [ITK-Snap](http://www.itksnap.org/pmwiki/pmwiki.php) (see [Andy's Brain Blog](https://andysbrainbook.readthedocs.io/en/latest/ITK-Snap/ITK-Snap_Overview.html#itk-snap-overview) for a primer) or [FSLeyes](https://fsl.fmrib.ox.ac.uk/fsl/docs/#/utilities/fsleyes), part of the FSL software suite. Both are free, open-source image viewers for 3D and 4D medical images.

#### <i class="fa-solid fa-eye header-icon"></i><i class="fas fa-cogs header-icon"></i> Connectome Workbench
**[Connectome Workbench](https://www.humanconnectome.org/software/connectome-workbench)** is a free, open-source software package that includes critically useful tools such as:

- **wb_view**: For interactive visualization of surface-based and connectivity data, creating overlays of structural/functional data, etc.
- **wb_command**: A set of command-line tools for processing and analysis of neuroimaging data (see [usage](https://www.humanconnectome.org/software/workbench-command))

## NMIND

[NMIND](https://www.nmind.org/about) is a collaborative initiative dedicated to improving transparency, reproducibility, and efficiency in neuroimaging research. NMIND principles, standards, and tools were used to develop the HBCD [Processing & Derivative Data Standards](../standards/processing/standards.md). Explore a growing collection of tools tested and improved through the NMIND process at [Evaluated Tools](https://www.nmind.org/proceedings/).

## ReproSchema

<a href="https://github.com/ReproNim/HBCD-ReproSchema"><i class="fa-brands fa-github"></i> HBCD-ReproSchema</a>

Consistent data collection is essential to reproducible longitudinal research, particularly for large, multi-site studies like HBCD. **ReproSchema** ([https://www.repronim.org/reproschema](https://www.repronim.org/reproschema/)) provides both a **schema** and **software platform** for structuring, versioning, and managing research questionnaires over time, including integration with survey and data collection platforms like REDCap. 

### Schema

As a schema, ReproSchema defines a standardized structure for questionnaires, including consistent formatting across time points, with explicitly defined questions, response options, and skip logic linked metadata. Questionnaires are organized following a hierarchical model with three main components:
> ***Protocol* (all study instruments) → *Activity* (single instrument) → *Item* (single question within instrument)**

### Platform

As a platform, ReproSchema provides tools for automated storage, versioning in GitHub, tracking changes (e.g. wording updates, added/removed/re-ordered items, updated skip logic, etc.), and comparing questionnaires over time. It also provides a utility for browser-based survey deployment, with survey responses stored in JSON-LD format to link each answer to its protocol, activity, and item in the ReproSchema library. See [Chen et al. 2025 Figure 1](https://www.jmir.org/2025/1/e63343#figure1) for details.

### Tracking Changes: Example 

ReproSchema maintains transparent, detailed version histories so researchers can understand how questionnaires evolve between releases. For example, the following shows how a sleep question and its response options may evolve across releases. ReproSchema versioning captures these changes to allow researchers to adjust longitudinal analyses as needed.

<table class="table-no-vertical-lines">
<thead><tr>
<th>Release</th>
<th>Item Question</th>
<th>Response Options</th>
<th>Implications for Analysis</th>
</tr> </thead>
<tbody>
<tr><td>1.0</td> 
<td>How many hours do you sleep on a typical night?</td>
<td>Free-text numeric entry</td>
<td>-</td>
</tr>
<tr>
<td>2.0</td>
<td>On average, how many hours of sleep do you get per night?</td>
<td>Dropdown menu options (e.g. <i>Less than 5, 5-6, etc.</i>)</td>
<td>1.0 → 2.0: Categorical response options reduce variability, but lose detail</td>
</tr>
<tr> <td>3.0</td>
<td>On average, how many hours of sleep do you get in a 24-hour period, including naps?</td>
<td>Same as Release 2.0</td> 
<td>2.0 → 3.0: Adding naps changes the construct, affecting cross-release comparability</td>
</tbody> </table> 


<!-- ## Programming Languages

<i class="fas fa-laptop-code header-icon"></i> **MATLAB**   
  [MATLAB](https://www.mathworks.com/products/matlab.html) has a variety of built-in functions and toolboxes for neuroimaging data. Note that it is proprietary, but may be provided at no-cost through your institution or department. See Andy's Brain Blog [Matlab for Neuroimagers](https://andysbrainbook.readthedocs.io/en/latest/Matlab/Matlab_Overview.html#matlab-for-neuroimagers) for a primer.

<i class="fas fa-laptop-code header-icon"></i> **Python**   
  Python is also commonly used in the field of neuroimaging: useful Python modules for neuroimaging include NiBabel, Nilearn, Nipype, PyNIfTI, PySurfer, PyTorch, and others. See Andy's Brain Blog [Python for Neuroimagers](https://andysbrainbook.readthedocs.io/en/latest/PythonForNeuroimagers/PythonForNeuroimagers_Overview.html) for a primer. 

<i class="fas fa-laptop-code header-icon"></i> **R/RStudio**    
  Especially strong for statistical plots, often used in conjunction with analysis results.       
  [Download page for R/RStudio <i class="fa fa-download"></i>](https://posit.co/download/rstudio-desktop/) -->