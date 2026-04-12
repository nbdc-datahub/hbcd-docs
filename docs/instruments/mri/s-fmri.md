# Structural & Functional MRI

The information below describes general as well as data acquisition details for structural and functional MRI data. Details of processing and pipeline derivative outputs are described under [Processed Derivatives](mri-proc.md).

## Structural MRI (sMRI)

HBCD protocols for structural MRI were informed by recent large-scale developmental neuroimaging studies including [ABCD](https://abcdstudy.org/), HCP Lifespan, and BCP ([Howell et al., 2019](https://pubmed.ncbi.nlm.nih.gov/29578031/)). These studies laid critical foundation for the development of well-validated, high-resolution protocols harmonized across all three major scanner vendors ([Casey et al., 2018](https://doi.org/10.1016/j.dcn.2018.03.001)). In addition, the findings emphasized the importance of T2w acquisition in infants due to suboptimal grey/white T1w contrast resulting from incomplete myelination ([Howell et al., 2019](https://doi.org/10.1016/j.neuroimage.2018.03.049), [Myers et al., 2023](https://doi.org/10.1016/j.neuroimage.2018.03.049)).
<!-- 
<div id="smri-ref" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-book-open"></i></span>
  <span class="text-with-link">
  <span class="text">References</span>
  <a class="anchor-link" href="#smri-ref" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<div class="references">
    <p>Casey, B. J., Cannonier, T., Conley, M. I., Cohen, A. O., Barch, D. M., Heitzeg, M. M., Soules, M. E., Teslovich, T., Dellarco, D. V., Garavan, H., Orr, C. A., Wager, T. D., Banich, M. T., Speer, N. K., Sutherland, M. T., Riedel, M. C., Dick, A. S., Bjork, J. M., Thomas, K. M., … ABCD Imaging Acquisition Workgroup. (2018). The Adolescent Brain Cognitive Development (ABCD) study: Imaging acquisition across 21 sites. <em>Developmental Cognitive Neuroscience</em>, 32, 43–54. <a href="https://doi.org/10.1016/j.dcn.2018.03.001">https://doi.org/10.1016/j.dcn.2018.03.001</a></p>
    <p>Howell, B. R., Styner, M. A., Gao, W., Yap, P.-T., Wang, L., Baluyot, K., Yacoub, E., Chen, G., Potts, T., Salzwedel, A., Li, G., Gilmore, J. H., Piven, J., Smith, J. K., Shen, D., Ugurbil, K., Zhu, H., Lin, W., & Elison, J. T. (2019). The UNC/UMN Baby Connectome Project (BCP): An overview of the study design and protocol development. <em>NeuroImage</em>, 185, 891–905. <a href="https://doi.org/10.1016/j.neuroimage.2018.03.049">https://doi.org/10.1016/j.neuroimage.2018.03.049</a></p>
    <p>Myers, M. J., Labonte, A. K., Gordon, E. M., Laumann, T. O., Tu, J. C., Wheelock, M. D., Nielsen, A. N., Schwarzlose, R., Camacho, M. C., Warner, B. B., Raghuraman, N., Luby, J. L., Barch, D. M., Fair, D. A., Petersen, S. E., Rogers, C. E., Smyser, C. D., & Sylvester, C. M. (2023). Functional parcellation of the neonatal brain. In <em>bioRxivorg</em>. <a href="https://doi.org/10.1101/2023.11.10.566629">https://doi.org/10.1101/2023.11.10.566629</a></p>
</div>
</div> -->

## Quantitative MRI (qMRI)

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</i></span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Note that different sites may apply varying criteria for identifying motion-degraded QALAS and B1⁺ mapping scans. For 3D-QALAS, the SyMRI toolbox does <strong>not</strong> incorporate externally acquired B1⁺ field maps when estimating quantitative T1, T2, and proton density (PD) values.</p>
<p>Additionally, estimated quantitative T1 values show variability across MRI vendors and participant age. Current estimates do not align well with values reported in the literature, likely due to assumptions made in the modeling procedures. Work is ongoing to address these issues. As a result, quantitative T1 values (and by extension, PD values) will not be included in the initial data release.</p> 
</div>

Quantitative MRI data was processed through two pipelines, SyMRI and qMRI PostProc. <a href="https://syntheticmr.com/products/symri-neuro/">SyMRI</a>, a proprietary software for quantitative MRI, is used to generate T1w and T2w images and derived relaxometry maps from <a href="https://pubmed.ncbi.nlm.nih.gov/25526880/">QALAS</a> brain images. These outputs are then minimally preprocessed by <a href="https://hbcd-symri-postproc.readthedocs.io/en/latest/index.html">qMRI PostProc</a>.

<div id="derivatives" class="table-banner" onclick="toggleCollapse(this)" style="background-color: #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
<span class="text">SyMRI (<code>symri/</code>) & qMRI PostProc (<code>qmri_postproc/</code>) Derivatives</span>
  <a class="anchor-link" href="#derivatives" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><a href="../../../datacuration/overview/#filetrees" target="_blank"><i style="color: #199bd6; margin-right: 4px;" class="fa fa-circle-info"></i> How To Read File Trees →</a></p>
<pre class="folder-tree">
hbcd/
|__ derivatives/ 
    |__ symri/  <span class="hashtag"># SyMRI Derivatives</span>
    |   |__ sub-<span class="label">{ID}</span>/
    |       |__ ses-<span class="label">{V0X}</span>/
    |           |__ anat/
    |               |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-QALAS_T1w.nii.gz <span class="hashtag">(+JSON)</span>
    |               |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-QALAS_T2map.nii.gz <span class="hashtag">(+JSON)</span>
    |               |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-QALAS_T2w.nii.gz <span class="hashtag">(+JSON)</span>
    |               |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_acq-QALAS_desc-SymriContainer.log
    | 
    |__ qmri_postproc/ <span class="hashtag"># qMRI Post-Proc Derivatives</span>
        |__ sub-<span class="label">{ID}</span>/
            |__ ses-<span class="label">{V0X}</span>/
                |__ anat/  
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-AsegROIs_scalarstats.tsv <span class="hashtag">(+JSON)</span>
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-BilateralAsegROIs_scalarstats.tsv <span class="hashtag">(+JSON)</span>
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_desc-RegistrationQCAid.png <span class="hashtag">(+JSON)</span>
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-QALAS_desc-aseg_dseg.nii.gz
                    |__ sub-<span class="label">{ID}</span>_ses-<span class="label">{V0X}</span>_space-T2w_desc-QALAS_T2map.nii.gz <span class="hashtag">(+JSON)</span>
</pre>
</div>

## Functional MRI (fMRI)

<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Responsible Use Warning</i></span>
  <a class="anchor-link" href="#alert" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p>Head motion is a serious issue for neuroimaging, and especially for resting state fMRI. It creates brain-wide artifactual effects including elevated short-distance connectivity and attenuated long-distance connectivity (<a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">Power et al. 2012</a>). In order to guard against artifactual effects due to head motion, researchers typically implement a variety of strategies that operate at multiple points of the data collection and processing pipeline, with guidance regularly evolving over time (<a href="https://doi.org/10.1016/j.neuroimage.2013.08.048">Power et al. 2014</a>; <a href="https://doi.org/10.1016/j.neuroimage.2014.10.044">2015</a>; <a href="https://doi.org/10.1016/j.neuroimage.2012.08.052">Satterthwaite et al. 2013</a>; <a href="https://doi.org/10.1093/cercor/bhw253">Siegel et al. 2017</a>; <a href="https://doi.org/10.1016/j.neuroimage.2020.116866">Gratton et al. 2020</a>). Some of these strategies include discarding entire runs of data that exceed certain motion thresholds and discarding individual functional imaging frames that are proximal to motion events (i.e., “motion censoring”). These strategies in particular typically lead to the exclusion of some participants from further analysis for lack of sufficient data.</p> <p>Levels of head motion differ according to demographic factors such as sex, race/ethnicity, and SES (<a href="https://doi.org/10.1007/s11682-022-00665-2">Cosgrove et al., 2022</a>). Therefore, strategies to deal with head motion may introduce questions of fairness and may lead to differential exclusions across demographic groups. In addition, motion censoring causes sessions to vary by the amount of data remaining. Such variability may continue to inflate findings especially in the presence of conditions that may correlate with the motion artifact like autism or ADHD (<a href="https://doi.org/10.1093/cercor/bhw403">Eggebrecht, 2017</a>). The amount of data remaining influences the variation in the connectivity calculations by affecting the degrees of freedom. Therefore, even after motion censoring, issues concerning fairness may persist when examining factors that might be affected by motion like sex, race/ethnicity, SES, and BMI (<a href="https://doi.org/10.1007/s11682-022-00665-2">Cosgrove et al., 2022</a>). One strategy that avoids this confound is to strictly control the degrees of freedom, where functional connectivity measures are calculated with the exact same amount of data. Researchers should assess whether control of artifactual effects of head motion effects can be achieved by alternative means that mitigate this impact. Examples of such strategies could include data augmentation approaches such as sampling from other datasets, data processing strategies like the include use of ICA-based denoising (<a href="https://doi.org/10.1016/j.neuroimage.2015.02.064">Pruim et al., 2015a</a>; <a href="https://doi.org/10.1016/j.neuroimage.2015.02.063">2015b</a>), use of bootstrap aggregation (<a href="https://doi.org/10.1101/2024.06.22.600221">Ramduny et al., 2024</a>), or the creation of “pseudo-rest” by removing task signals from the task data (<a href="https://doi.org/10.1016/j.neuroimage.2006.11.051">Fair et al. 2007</a>), or post-hoc approaches like propensity weighting.</p> 
<p>Researchers interested in examining brain-behavior associations or multivariate predictions should follow strategies such as those in <a href="https://doi.org/10.1093/cercor/bhw403">Eggebrecht 2017</a> to: 1) assess how missing data impacts dependent, independent variables and covariates, 2) examine the association between the degrees of freedom and non-FC variables, 3) use trimmed FC measures when needed to mitigate artifacts due to data quality.</p>
</div>

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p><b>Philips signal intensity clipping - Overview</b><br>
A subset of Philips fMRI scans is affected by a signal intensity clipping issue. Due to a scaling error during real-time reconstruction, raw pixel intensity values above 4095 are capped, resulting in hyperintense regions that obscure gray/white matter signal. This artifact can significantly impact BOLD registration and derived measures such as ROI-to-ROI correlations.</p>
<p><b>Detection and Prevalence</b><br>
The artifact was initially detected during HBCD pilot scanning through manual quality control (QC) and addressed with a protocol patch applied at most Philips sites prior to the start of the HBCD main study. However, the patch was implemented later (October 2024) at sites VAN and CCH, leading to residual cases at these locations. Severe cases typically fail manual QC (QC=0), while less severe cases often pass (QC=1), as they may not be visually apparent. Overall, ~20% of scans from VAN and CCH show some degree of clipping, with ~6% classified as severe enough to fail QC. Updates to real-time reconstruction are in development to recover affected data. In the meantime, only scans that pass QC, including those with mild clipping, are included in the release.</p>
<p><b>How to Identify Affected Scans</b><br>
Clipping severity can be estimated using the ratio of median to maximum image intensity and the fraction of voxels at maximum intensity within the brain mask (both available in the <a href="../../../datacuration/file-based-data/#participant-session-scan-level-data"><code>scans.tsv</code> file</a>):</p> 
<ul>
<li><i>Severe clipping</i>: (brain_median / brain_max) > 0.8 AND brain_fvox_max > 0.001</li> 
<li><i>Potential clipping</i>: (brain_median / brain_max) > 0.5 AND brain_fvox_max > 0.001</li> 
</ul>
</div>
<p></p>

fMRI measures functional brain activity based on the blood oxygen level–dependent (BOLD) signal. Resting-state (rs-fMRI) data is acquired at 2mm isotropic resolution with a repetition time (TR) of 1725 ms and multi-band (MB) factor of 4. A minimum of 2 runs are acquired (during sleep for infants <30 months old), each lasting 7.5 minutes. [FIRMM](https://firmm.readthedocs.io/) ([Dosenbach et al., 2017](https://doi.org/10.1016/j.neuroimage.2017.08.025)) is used to monitor head motion in real time and additional runs are acquired as needed to obtain at least 7.5 minutes of low-motion data (FD < 0.3 mm) across runs.

### Quality Control Summary Statistics

<div id="fconn" class="static-banner" style="border-left: 5px solid #199bd6;">
  <span class="emoji"><i class="fa fa-circle-check"></i></span>
  <span class="text-with-link">
    <span class="text">Functional Connectivity as Data Quality Improves</span>
    <a class="anchor-link" href="#fconn" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
</div>
<div class="table-static-content">
<p>Average functional connectivity matrices were computed using the Gordon parcellation from <a href="../mri-proc/#xcp-d">XCP-D derivatives</a> for V02 sessions with data inclusion based on various thresholds of BrainSwipes QC results (<code>img_brainswipes_xcpd-bold</code>; <a href="../qc/#brainswipes">see details</a>). Functional connectivity patterns remained consistent even when incorporating data with lower QC scores, suggesting robustness to mild quality variations.</p>
<p><strong>Connectivity matrices as data quality improves (Left -> Right) based on QC thresholds of 0.1, 0.5, and 0.9:</strong></p>
<img src="../images/fconn_qc.png" style="width: 90%;" class="center">
<br>
</div>
<p></p>


<!-- <div id="fmri-ref" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-book-open"></i></span>
  <span class="text-with-link">
  <span class="text">References</span>
  <a class="anchor-link" href="#fmri-ref" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<div class="references">
  <p>Dosenbach, N. U. F., Koller, J. M., Earl, E. A., Miranda-Dominguez, O., Klein, R. L., Van, A. N., Snyder, A. Z., Nagel, B. J., Nigg, J. T., Nguyen, A. L., Wesevich, V., Greene, D. J., & Fair, D. A. (2017). Real-time motion analytics during brain MRI improve data quality and reduce costs. <em>NeuroImage</em>, 161, 80-93. <a href="https://doi.org/10.1016/j.neuroimage.2017.08.025">https://doi.org/10.1016/j.neuroimage.2017.08.025</a></p>
  <p>Gratton, C., Dworetsky, A., Coalson, R. S., Adeyemo, B., Laumann, T. O., Wig, G. S., Kong, T. S., Gratton, G., Fabiani, M., Barch, D. M., Tranel, D., Miranda-Dominguez, O., Fair, D. A., Dosenbach, N. U. F., Snyder, A. Z., Perlmutter, J. S., Petersen, S. E., & Campbell, M. C. (2020). Removal of high frequency contamination from motion estimates in single-band fMRI saves data without biasing functional connectivity. <i>NeuroImage</i>, 217(116866), 116866. <a href="https://doi.org/10.1016/j.neuroimage.2020.116866" target="_blank">doi: 10.1016/j.neuroimage.2020.116866</a></p>
  <p>Power, J. D., Barnes, K. A., Snyder, A. Z., Schlaggar, B. L., & Petersen, S. E. (2012). Spurious but systematic correlations in functional connectivity MRI networks arise from subject motion. <i>NeuroImage</i>, 59(3), 2142–2154. <a href="https://doi.org/10.1016/j.neuroimage.2011.10.018" target="_blank">doi: 10.1016/j.neuroimage.2011.10.018</a></p>
  <p>Power, J. D., Mitra, A., Laumann, T. O., Snyder, A. Z., Schlaggar, B. L., & Petersen, S. E. (2014). Methods to detect, characterize, and remove motion artifact in resting state fMRI. <i>NeuroImage</i>, 84, 320–341. <a href="https://doi.org/10.1016/j.neuroimage.2013.08.048" target="_blank">doi: 10.1016/j.neuroimage.2013.08.048</a></p>
  <p>Power, J. D., Schlaggar, B. L., & Petersen, S. E. (2015). Recent progress and outstanding issues in motion correction in resting state fMRI. <i>NeuroImage</i>, 105, 536–551. <a href="https://doi.org/10.1016/j.neuroimage.2014.10.044" target="_blank">doi: 10.1016/j.neuroimage.2014.10.044</a></p>
  <p>Pruim RHR, Mennes M, van Rooij D, Llera A, Buitelaar JK, Beckmann CF. ICA-AROMA: A robust ICA-based strategy for removing motion artifacts from fMRI data. <i>Neuroimage</i> 112, 267-277, 2015a. <a href="https://doi.org/10.1016/j.neuroimage.2015.02.064" target="_blank">doi: 10.1016/j.neuroimage.2015.02.064</a></p>
  <p>Pruim RHR, Mennes M, Buitelaar JK, Beckmann CF. Evaluation of ICA-AROMA and alternative strategies for motion artifact removal in resting state fMRI. <i>Neuroimage</i> 112, 278-287, 2015b. <a href="https://doi.org/10.1016/j.neuroimage.2015.02.063" target="_blank">doi: 10.1016/j.neuroimage.2015.02.063</a></p>
  <p>Ramduny, J., Uddin, L. Q., Vanderwal, T., Feczko, E., Fair, D. A., Kelly, C., & Baskin-Sommers, A. (2024). Increasing the representation of minoritized youth for inclusive and reproducible brain-behavior associations. <i>bioRxiv</i>. <a href="https://doi.org/10.1101/2024.06.22.600221" target="_blank">doi: 10.1101/2024.06.22.600221</a></p>
  <p>Satterthwaite TD, Elliott MA, Gerraty RT, Ruparel K, Loughead J, Calkins ME, Eickhoff SB, Hakonarson H, Gur RC, Gur RE, Wolf DH. An improved framework for confound regression and filtering for control of motion artifact in the preprocessing of resting-state functional connectivity data. <i>Neuroimage</i> 64, 240-256, 2013. <a href="https://doi.org/10.1016/j.neuroimage.2012.08.052" target="_blank">doi: 10.1016/j.neuroimage.2012.08.052</a></p>
  <p>Siegel JS, Mitra A, Laumann TO, Seitzman BA, Raichle M, Corbetta M, Snyder AZ. Data Quality Influences Observed Links Between Functional Connectivity and Behavior. <i>Cereb Cortex</i> 27, 4492-4502, 2017. <a href="https://doi.org/10.1093/cercor/bhw253" target="_blank">doi: 10.1093/cercor/bhw253</a></p>
</div>
</div> -->

<!-- 
<div class="references">
<p>Cosgrove KT, McDermott TJ, White EJ, Mosconi MW, Thompson WK, Paulus MP, Cardenas-Iniguez C, Aupperle RL. Limits to the generalizability of resting-state functional magnetic resonance imaging studies of youth: An examination of ABCD Study® baseline data. <i>Brain Imaging Behav</i> 16, 1919-1925, 2022. <a href="https://doi.org/10.1007/s11682-022-00665-2" target="_blank">doi: 10.1007/s11682-022-00665-2</a></p>

  <p>Eggebrecht, A. T., Elison, J. T., Feczko, E., Todorov, A., Wolff, J. J., Kandala, S., Adams, C. M., Snyder, A. Z., Lewis, J. D., Estes, A. M., Zwaigenbaum, L., Botteron, K. N., McKinstry, R. C., Constantino, J. N., Evans, A., Hazlett, H. C., Dager, S., Paterson, S. J., Schultz, R. T., … Pruett, J. R., Jr. (2017). Joint attention and brain functional connectivity in infants and toddlers. <i>Cerebral Cortex (New York, N.Y.: 1991)</i>, 27(3), 1709–1720. <a href="https://doi.org/10.1093/cercor/bhw403" target="_blank">doi: 10.1093/cercor/bhw403</a></p>
  <p>Fair, D. A., Schlaggar, B. L., Cohen, A. L., Miezin, F. M., Dosenbach, N. U. F., Wenger, K. K., Fox, M. D., Snyder, A. Z., Raichle, M. E., & Petersen, S. E. (2007). A method for using blocked and event-related fMRI data to study “resting state” functional connectivity. <i>NeuroImage</i>, 35(1), 396–405. <a href="https://doi.org/10.1016/j.neuroimage.2006.11.051" target="_blank">doi: 10.1016/j.neuroimage.2006.11.051</a></p>
  <p>Gratton, C., Dworetsky, A., Coalson, R. S., Adeyemo, B., Laumann, T. O., Wig, G. S., Kong, T. S., Gratton, G., Fabiani, M., Barch, D. M., Tranel, D., Miranda-Dominguez, O., Fair, D. A., Dosenbach, N. U. F., Snyder, A. Z., Perlmutter, J. S., Petersen, S. E., & Campbell, M. C. (2020). Removal of high frequency contamination from motion estimates in single-band fMRI saves data without biasing functional connectivity. <i>NeuroImage</i>, 217(116866), 116866. <a href="https://doi.org/10.1016/j.neuroimage.2020.116866" target="_blank">doi: 10.1016/j.neuroimage.2020.116866</a></p>
  <p>Power, J. D., Barnes, K. A., Snyder, A. Z., Schlaggar, B. L., & Petersen, S. E. (2012). Spurious but systematic correlations in functional connectivity MRI networks arise from subject motion. <i>NeuroImage</i>, 59(3), 2142–2154. <a href="https://doi.org/10.1016/j.neuroimage.2011.10.018" target="_blank">doi: 10.1016/j.neuroimage.2011.10.018</a></p>
  <p>Power, J. D., Mitra, A., Laumann, T. O., Snyder, A. Z., Schlaggar, B. L., & Petersen, S. E. (2014). Methods to detect, characterize, and remove motion artifact in resting state fMRI. <i>NeuroImage</i>, 84, 320–341. <a href="https://doi.org/10.1016/j.neuroimage.2013.08.048" target="_blank">doi: 10.1016/j.neuroimage.2013.08.048</a></p>
  <p>Power, J. D., Schlaggar, B. L., & Petersen, S. E. (2015). Recent progress and outstanding issues in motion correction in resting state fMRI. <i>NeuroImage</i>, 105, 536–551. <a href="https://doi.org/10.1016/j.neuroimage.2014.10.044" target="_blank">doi: 10.1016/j.neuroimage.2014.10.044</a></p>
  <p>Pruim RHR, Mennes M, van Rooij D, Llera A, Buitelaar JK, Beckmann CF. ICA-AROMA: A robust ICA-based strategy for removing motion artifacts from fMRI data. <i>Neuroimage</i> 112, 267-277, 2015a. <a href="https://doi.org/10.1016/j.neuroimage.2015.02.064" target="_blank">doi: 10.1016/j.neuroimage.2015.02.064</a></p>
  <p>Pruim RHR, Mennes M, Buitelaar JK, Beckmann CF. Evaluation of ICA-AROMA and alternative strategies for motion artifact removal in resting state fMRI. <i>Neuroimage</i> 112, 278-287, 2015b. <a href="https://doi.org/10.1016/j.neuroimage.2015.02.063" target="_blank">doi: 10.1016/j.neuroimage.2015.02.063</a></p>
  <p>Ramduny, J., Uddin, L. Q., Vanderwal, T., Feczko, E., Fair, D. A., Kelly, C., & Baskin-Sommers, A. (2024). Increasing the representation of minoritized youth for inclusive and reproducible brain-behavior associations. <i>bioRxiv</i>. <a href="https://doi.org/10.1101/2024.06.22.600221" target="_blank">doi: 10.1101/2024.06.22.600221</a></p>
  <p>Satterthwaite TD, Elliott MA, Gerraty RT, Ruparel K, Loughead J, Calkins ME, Eickhoff SB, Hakonarson H, Gur RC, Gur RE, Wolf DH. An improved framework for confound regression and filtering for control of motion artifact in the preprocessing of resting-state functional connectivity data. <i>Neuroimage</i> 64, 240-256, 2013. <a href="https://doi.org/10.1016/j.neuroimage.2012.08.052" target="_blank">doi: 10.1016/j.neuroimage.2012.08.052</a></p>
  <p>Siegel JS, Mitra A, Laumann TO, Seitzman BA, Raichle M, Corbetta M, Snyder AZ. Data Quality Influences Observed Links Between Functional Connectivity and Behavior. <i>Cereb Cortex</i> 27, 4492-4502, 2017. <a href="https://doi.org/10.1093/cercor/bhw253" target="_blank">doi: 10.1093/cercor/bhw253</a></p>
</div> -->
