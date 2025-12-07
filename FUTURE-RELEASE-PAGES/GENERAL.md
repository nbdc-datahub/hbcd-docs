## BrainSwipes QC for diffusion data

Removed for now as diffusion QC result inclusion is not currently planned:

<p style="font-size: 1em; margin: 0 0 5px;"><b>Diffusion Direction Encoding (<i>to be included in future release</i>):</b></p>
Swipes display GIFs of full-resolution T2w images as a grayscale background, with the "Direction Encoded Color" (DEC) map overlaid. These GIFs sweep through a portion of the brain across the three anatomical planes. High-quality processed DWI images exhibit bands of color that closely follow the folds and contours of the grayscale background. These visuals are derived from the QSIPrep report.
<p>

Also removed this python helper function for 2.0 since it doesn't seem particularly helpful:

QC scores range from 0 (Fail) to 1 (Pass), averaged across reviewers. For example, a score of 0.6 indicates that 60% of reviewers rated the image as a pass. The data includes overall average QC scores and average number of reviewers for each session-level T1w/T2w and BOLD run (summarizing across all visual reports for a given run) as well as the average QC and number of reviewers for each visual report. A Python helper function is provided below to load a BrainSwipes TSV file into a Pandas DataFrame and filter runs with average QC scores above a user-specified threshold:

<div id="python-helper-function" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-brands fa-python"></i></span>
  <span class="text-with-link">
  <span class="text">Python Helper Function</span>
  <a class="anchor-link" href="#python-helper-function" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<pre class="helper-code"><code>
import pandas as pd

def read_and_filter_tsv(file_path, threshold):
    """
    Reads an HBCD BrainSwipes TSV file into a DataFrame and keeps subject rows where 
	the overall average QC value is greater than or equal to the specified threshold.

    Parameters:
    - file_path (str): Path to the .tsv file
    - threshold (float): Threshold value for filtering

    Returns:
    - pd.DataFrame: Filtered DataFrame
    """
    df = pd.read_csv(file_path, sep='\t')

    fourth_col = df.columns[3]
    return df[df[fourth_col] >= threshold]

# Example usage:
# Filter to keep only subjects with an average structural QC of at least 0.6 (60% pass rate)
filtered_df = read_and_filter_tsv("img_brainswipes_xcpd_T2w.tsv", 0.6)
print(filtered_df.head())
</code></pre>
</div>



<p style="font-size: 0.9em; color: #696969ff; font-weight: bold;">
<i style="color: teal;" class="fas fa-layer-group"></i>&nbsp;= Concatenated Data - <a href="../datacuration/file-based-data/#concatenated-data" target="_blank"><i>see details</i></a>
</p>
<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th style="width: 30%;">Instrument</th>
      <th style="width: 30%;">Construct</th>
      <th style="width: 30%;">Table Name</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><a href="admin/transitions-in-care" target="_blank">Transition in Care Screener</a></td>
    <td style="word-wrap: break-word; white-space: normal;">Recruitment/Retention</td>
    <td><code>sed_cg_tic_screener</code></td>
  </tr>
  </tbody>
  </table>