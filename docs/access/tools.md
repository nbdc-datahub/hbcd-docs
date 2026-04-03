# Recommended Programs & Utilities

<!-- ## Download Platforms

### NBDC Data Access Platform

### DEAP -->

## Tabulated Data
<i class="fas fa-database"></i> **NBDCtools**  
NBDCtools is an R package for creating custom, analysis-ready datasets by simply specifying the variable and/or table names you need. The package automatically retrieves the specified columns from locally downloaded HBCD tabulated data and assembles them into a single in-memory data frame, minimizing storage and memory use. This provides a flexible alternative to building datasets through the Lasso or DEAP platforms, eliminating the need to manually parse files or resolve formatting issues. In addition to dataset assembly, NBDCtools includes functions for working with [shadow matrices](phenotypes.md#shadow-matrices-for-missing-data) as well as applying transformations and filters.   
[Download page for NBDCtools <i class="fa fa-download"></i>](https://software.nbdc-datahub.org/NBDCtools/index.html) 

## Brain Imaging Data
#### Interactive Visualization of Volumetric NIfTI (`.nii.gz`) files (e.g. T1w, T2w, DTI, etc.)
<i class="fa-solid fa-eye"></i></i> **[ITK-Snap](http://www.itksnap.org/pmwiki/pmwiki.php)**    
A free, open-source software application used to visualize and segment 3D and 4D medical images. See an overview of ITK-Snap on Andy's Brain Blog [here](https://andysbrainbook.readthedocs.io/en/latest/ITK-Snap/ITK-Snap_Overview.html#itk-snap-overview) for a primer.      
[Download page for ITK-Snap <i class="fa fa-download"></i>](http://www.itksnap.org/pmwiki/pmwiki.php?n=Downloads.SNAP4)

<i class="fa-solid fa-eye"></i></i> **[FSLeyes](https://fsl.fmrib.ox.ac.uk/fsl/docs/#/utilities/fsleyes)**    
A free, open-source image viewer for medical images, particularly MRI data. Part of the FSL software suite.    
[Download page for FSLeyes <i class="fa fa-download"></i>](https://fsl.fmrib.ox.ac.uk/fsl/docs/#/utilities/fsleyes)

#### Interactive Visualization & Processing of Surface Data
**[Connectome Workbench](https://www.humanconnectome.org/software/connectome-workbench)** is a free, open-source software package particularly useful for visualizing connectivity data, surface-based analyses, and more. It is recommended for viewing and processing surface data (`.gii` files), volume data (`.nii/.nii.gz` files), and CIFTI data (dlabel, dscalar, dtseries, pconn, etc. files) - check out this [blog post](https://mvpa.blogspot.com/2014/03/nifti-cifti-gifti-in-hcp-and-workbench.html) for a helpful primer on the difference between these various file formats. Useful Workbench tools include wb_view and wb_command.    
[Download page for Connectome Workbench <i class="fa fa-download"></i>](https://humanconnectome.org/software/get-connectome-workbench)

<i class="fa-solid fa-eye"></i></i> **wb_view**       
<span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 0.9em; border: 1px solid #d0e7ff;">
  <i class="fa-regular fa-lightbulb" style="margin-right: 6px; color:rgb(13, 148, 8);"></i>
  <strong>Good for:</strong> interactive visualization
</span>     
An interactive GUI used for inspecting images, particularly useful for visualizing surface-based data. It allows users to view and manipulate 3D brain images, including the ability to rotate, zoom, and pan the images. It also provides tools for overlaying different types of data, such as functional and structural images, and for visualizing connectivity data.  

<i class="fas fa-cogs"></i> **wb_command**          
<span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 0.9em; border: 1px solid #d0e7ff;">
  <i class="fa-regular fa-lightbulb" style="margin-right: 6px; color:rgb(13, 148, 8);"></i>
  <strong>Good for:</strong> processing & analysis
</span>     
A command-line tool that provides a variety of functions for processing and analyzing neuroimaging data. It can be used to perform a wide range of tasks, including image registration, surface generation, and statistical analysis. The command-line interface allows for batch processing of data and can be integrated into scripts for automated analysis.

## Programming Languages

<i class="fas fa-laptop-code"></i> **[MATLAB](https://www.mathworks.com/products/matlab.html)**   
  MATLAB has a variety of built-in functions and toolboxes for neuroimaging data. Note that it is proprietary, but may be provided at no-cost through your institution or department. See Andy's Brain Blog [Matlab for Neuroimagers](https://andysbrainbook.readthedocs.io/en/latest/Matlab/Matlab_Overview.html#matlab-for-neuroimagers) for a primer.

<i class="fas fa-laptop-code"></i> **Python**   
  Python is also commonly used in the field of neuroimaging: useful Python modules for neuroimaging include NiBabel, Nilearn, Nipype, PyNIfTI, PySurfer, PyTorch, and others. See Andy's Brain Blog [Python for Neuroimagers](https://andysbrainbook.readthedocs.io/en/latest/PythonForNeuroimagers/PythonForNeuroimagers_Overview.html) for a primer. 

<i class="fas fa-laptop-code"></i> **R/RStudio**    
  Especially strong for statistical plots, often used in conjunction with analysis results.       
  [Download page for R/RStudio <i class="fa fa-download"></i>](https://posit.co/download/rstudio-desktop/)

## NMIND

[NMIND](https://www.nmind.org/about) is a collaborative initiative dedicated to improving transparency, reproducibility, and efficiency in neuroimaging research. NMIND principles, standards, and tools were used to develop the [HBCD Processing & Analytic Software Standards](../instruments/processing/standards.md). Explore a growing collection of tools tested and improved through the NMIND process in the [Proceedings](https://www.nmind.org/proceedings/) page of the NMIND website.

## ReproSchema

<a href="https://github.com/ReproNim/HBCD-ReproSchema"><i class="fa-brands fa-github"></i> HBCD-ReproSchema</a>

Consistent data collection is essential to reproducible longitudinal research, particularly for large, multi-site studies like HBCD. **ReproSchema** ([https://www.repronim.org/reproschema](https://www.repronim.org/reproschema/)) provides both a **schema** and **software platform** for structuring, versioning, and managing research questionnaires over time, including integration with survey and data collection platforms like REDCap. 

**As a [schema](https://repronim.org/reproschema/schema/schema/)**, ReproSchema defines a standardized structure for questionnaires, including consistent formatting across time points, with explicitly defined questions, response options, and skip logic linked metadata. Questionnaires are organized following a hierarchical model with three main components:
> ***Protocol* (all study instruments) → *Activity* (single questionnaire/instrument) → *Item* (single question within instrument)**

**As a [platform](https://repronim.org/reproschema/user-guide/create-new-protocol/)**, ReproSchema provides tools for automated storage, versioning in GitHub, tracking changes (e.g. wording updates, added/removed/re-ordered items, updated skip logic, etc.), and comparing questionnaires over time. It also provides a utility for browser-based survey deployment, with survey responses stored in JSON-LD format to link each answer to its protocol, activity, and item in the ReproSchema library. See [Chen et al. 2025 Figure 1](https://www.jmir.org/2025/1/e63343#figure1) for details.

<p>
<div id="rs-example" class="table-banner" onclick="toggleCollapse(this)"> <span class="emoji"><i class="fa-solid fa-circle-info"></i></span> <span class="text-with-link">
<span class="text">Tracking Changes: Example</span> <a class="anchor-link" href="#rs-example" title="Copy link"> <i class="fa-solid fa-link"></i> </a> </span> <span class="arrow">▸</span> </div>
<div class="table-collapsible-content"> 
<p>ReproSchema maintains transparent, detailed version histories so researchers can understand how questionnaires evolve between releases. For example, the following shows how a sleep question and its response options may evolve across releases. ReproSchema versioning captures these changes to allow researchers to adjust longitudinal analyses as needed.</p> 
<table class="compact-table-no-vertical-lines">
<thead><tr>
<th>Release</th>
<th>Item Question</th>
<th>Response Options</th>
<th>Implications for Analysis</th>
</tr> </thead>
<tbody>
<tr><td>1.0</td> 
<td style="word-wrap: break-word; white-space: normal;"><i>How many hours do you sleep on a typical night?</i></td>
<td style="word-wrap: break-word; white-space: normal;">Free-text numeric entry</td>
<td>-</td>
</tr>
<tr>
<td>2.0</td>
<td style="word-wrap: break-word; white-space: normal;"><i>On average, how many hours of sleep do you get per night?</i></td>
<td style="word-wrap: break-word; white-space: normal;">Dropdown menu options (e.g. <i>Less than 5, 5-6, etc.</i>)</td>
<td style="word-wrap: break-word; white-space: normal;">1.0 → 2.0: Categorical response options reduce variability, but lose detail</td>
</tr>
<tr> <td>3.0</td>
<td style="word-wrap: break-word; white-space: normal;"><i>On average, how many hours of sleep do you get in a 24-hour period, including naps?</i></td>
<td style="word-wrap: break-word; white-space: normal;">Same as Release 2.0</td> 
<td style="word-wrap: break-word; white-space: normal;">2.0 → 3.0: Adding naps changes the construct, affecting cross-release comparability</td>
</tbody> </table> 
</div>
</p>