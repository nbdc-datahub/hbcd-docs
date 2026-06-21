# Illumina Global Diversity GWAS Array 

{{ readme(instruments.illumina) }}
{{ alert_warning(instruments.illumina) }}
{{ data_warning(instruments.illumina) }}
{{ issues_banner_macro() }}

---

## Instrument Details

Genomic data generated from the **Illumina Global Diversity Array (GDA GWAS)** is provided for both the birth parent and child. Samples are assayed from one sample, but may come from any visit (V01-V06) based on DNA yields. The dataset includes batch metadata and interlinked PLINK files (`.bed`, `.bim`, `.fam`) aligned to the **GRCh38/hg38 Build**.
<!-- replaced: **hg19 genome build** -->

## Concatenated Release Data

The GDA GWAS dataset is provided as <a href="../../../datacuration/file-based-data/#concatenated-data" target="_blank">concatenated data</a> organized within the file tree [above](#illumina-global-diversity-gwas-array), including:

<table class="table-no-vertical-lines">
<thead>
  <tr><th>File</th><th>Description</th></tr>
</thead>
<tbody>
<tr>
  <td><code>batch.info</code></td>
  <td>Plain-text file mapping participants to genotyping batches.</td>
</tr>
<tr>
  <td><code>hbcd.bed</code></td>
  <td><a href="https://www.cog-genomics.org/plink/1.9/formats#bed">PLINK 1.9 <code>.bed</code> format</a> — Binary genotype file (not UCSC BED).</td>
</tr>
<tr>
  <td><code>hbcd.bim</code></td>
  <td><a href="https://www.cog-genomics.org/plink/1.9/formats#bim">PLINK 1.9 <code>.bim</code> format</a> — Variant information (chromosome, rsID, position, alleles).</td>
</tr>
<tr>
  <td><code>hbcd.fam</code></td>
  <td><a href="https://www.cog-genomics.org/plink/1.9/formats#fam">PLINK 1.9 <code>.fam</code> format</a> — Participant information.</td>
</tr>
</tbody>
</table>

## GDC Genomics QC Pipeline Analysis

Along with [general QC](#illumina-global-diversity-gwas-array) described above, genomics data are processed through the [GDC Genomics QC](https://gdcgenomicsqc.readthedocs.io/en/latest/genomics.html) pipeline (<a href="https://github.com/UMN-GDC/GDCGenomicsQC"><i class="fa-brands fa-github" style="font-size: 1.1em;"></i></a>) to perform additional checks. Summary results are outlined below. Key features of this pipeline include:

<ul style="font-size: 0.9em;">
<li>Alternating filters for variant and subject missingness (10% followed by 2%)</li>
<li>Sex checks</li>
<li>Outlier detection based on the first two principal components derived from the genetic relatedness matrix using PC-AIR and PC-Relate (<a href="https://bioc.r-universe.dev/GENESIS">GENESIS</a>)</li>
<li>Classification of relatedness using IBD estimates from <a href="https://www.kingrelatedness.com/">KING</a></li>
</ul>

### Cryptic Relatedness
<div style="display: flex; align-items: center; gap: 25px; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 250px;">
    <p>KING coefficient–inferred relatedness identified previously unreported familial relationships. The anonymized cryptic relatedness family graphs (<i>right</i>) show inferred relationships based on the following KING coefficient intervals (all visualized edges represent unreported relationships):</p>
    <ul style="font-size: 0.9em;">
      <li>[0.354, ∞] → Monozygotic twins or duplicate samples</li>
      <li>[0.177, 0.354] → First-degree (parent–offspring or siblings)</li>
      <li>[0.0884, 0.177] → Second-degree</li>
      <li>[0, 0.0884] → Unrelated</li>
    </ul>
  </div>
  <div style="flex: 1; min-width: 200px; text-align: center;">
    <img src="../images/family-clusters.png" style="max-width:100%; height:auto; display:block; margin:0 auto;">
  </div>
</div>
<br>

### Genetic Ancestry-Based Clustering
PC space derived from the first two PC-Relate components was visually inspected to assess clustering by reported race. Reported race largely clustered within the first two genetic principal components:

<div style="text-align: center;">
  <img src="../images/pca.png" style="max-width: 70%; height:auto; display:block; margin:0 auto;">
</div>

Subject scores along the first 32 principal components, along with IBD estimates, genetic relatedness (estimated through PC-Relate), and kinship estimates are all included as derivatives. These derivatives were calculated off of the full sample less the individuals removed for QC related reasons. Individuals that were excluded for other non genomic QC related reasons were included in these computations even if their data and related derivatives are not included for release. The description of file names and their content are described in the following table.

<table class="table-no-vertical-lines">
<thead>
<tr>
<th>File Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td><code>pcrelate_relatedness.grm.bin</code></td>
  <td>PC-Relate adjusted genetic relatedness matrix</td>
</tr>
<tr>
  <td><code>pcrelate_relatedness.grm.N.bin</code></td>
  <td>PC-Relate pairwise common SNP count</td>
</tr>
<tr>
  <td><code>pcrelate_relatedness.grm.id</code></td>
  <td>PC-Relate subject IDs, corresponding to matrix column and row order</td>
</tr>
<tr>
  <td><code>pcrelate_relatedness.tsv</code></td>
  <td>&nbsp;</td>
</tr>
<tr>
<td><code>family_clusters.txt</code></td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>



## References
<div class="references"> 
<p>Committee on the Use of Race, Ethnicity, and Ancestry as Population Descriptors in Genomics Research, Board on Health Sciences Policy, Committee on Population, Health and Medicine Division, Division of Behavioral and Social Sciences and Education, & National Academies of Sciences, Engineering, and Medicine. (2023). Using population descriptors in genetics and genomics research. National Academies Press. <a href="https://doi.org/10.17226/26902">https://doi.org/10.17226/26902</a></p>  
<p>Martschenko, D. O., Lee, S. S.-J., Meyer, M. N., & Parens, E. (2025). Social and behavioral genomics: On the ethics of the research and its downstream applications. <i>Annual Review of Genomics and Human Genetics</i>, 26(1), 425–447. <a href="https://doi.org/10.1146/annurev-genom-011224-015733">https://doi.org/10.1146/annurev-genom-011224-015733</a></p>
<p>Meyer, M. N., Appelbaum, P. S., Benjamin, D. J., Callier, S. L., Comfort, N., Conley, D., Freese, J., Garrison, N. A., Hammonds, E. M., Harden, K. P., Lee, S. S.-J., Martin, A. R., Martschenko, D. O., Neale, B. M., Palmer, R. H. C., Tabery, J., Turkheimer, E., Turley, P., & Parens, E. (2023). Wrestling with social and behavioral genomics: Risks, potential benefits, and ethical responsibility. <i>The Hastings Center Report</i>, 53 Suppl 1, S2–S49. <a href="https://doi.org/10.1002/hast.1477">https://doi.org/10.1002/hast.1477</a></p>
</div>


  
<!-- potential suggestions to clarify QC description:


- Verify consistent sample information between the source data (Sampled Genomics Services) and central HBCD database (Lasso Informatics), including sample IDs, sample-specific barcodes, and genetic relatedness (i.e., that IBD is ~0.25 between the birth parent and child as well as siblings; evaluate potential twins).
- Verify that genomic sex matches with sex at birth.
- Use FHET estimates to check for plate contamination.
- Visually inspect plate effects on principal component space derived from PC-Relate. -->

  <!-- {{ warning_banner_macro() }}
<div class="collapsible-content">
<p><b>Twins Present in Birth Parents</b><br>
The dataset includes two birth parents who are monozygotic twins (along with their respective families), which may complicate certain analyses. The participant IDs associated with this twin pair are under internal review and may be shared in a future update.</p> 
<p><b>Data Exclusions</b><br>
See <a href="#data-exclusions">Data Exclusions</a> below.</p>
</div> -->

<!-- 
<pre class="folder-tree">

hbcd/
└── concatenated/genetics/genotype_microarray/GDA/
    ├── batch.info
    ├── hbcd.bed
    ├── hbcd.bim
    └── hbcd.fam
</pre> -->

<!-- 
{{ alert_banner_macro() }}
<div class="collapsible-content">
<p><b>Anonymity</b><br>
Data users are prohibited from using HBCD data, including genomic data, to identify participants or their relatives.  You accessed these data under a Data Use Certification (DUC) agreement in which you and your institution agreed that you would not attempt to establish the individual identity of any study participants or their relatives.  You also agreed to adhere to a minimum cell threshold of 10 in any public reporting of data (i.e., publications, posters, or other presentations).  Protecting participants’ anonymity demonstrates respect for them and minimizes their research-related risks.</p>
<p><b>Population Descriptors</b><br>
The use of population descriptors in genetic research has been varied and inconsistent. The National Academies of Science, Engineering, and Medicine (NASEM) published a report on the use of population descriptors, such as ancestry, race, ethnicity, and geography, in genomics (<a href="https://doi.org/10.17226/26902">https://doi.org/10.17226/26902</a>). We encourage data users working with HBCD genomics data to consult the NASEM report to understand the past and current use of population descriptors in genomics research as well as current best practice recommendations when analyzing or reporting on HBCD genomic data. Race and ethnicity represent social constructs that are conceptually distinct from ancestry inferred from genetic data. Description of race and ethnicity variables in HBCD may be found in <a href="../../demo/basicdemo/#race-ethnicity-variables" target="_blank">Basic Demographics</a>.</p>
<p><b>Ethical Obligations to Minimize Risks</b><br>
Analysts using HBCD data have ethical obligations to minimize risks, including psychological, social, and economic risks, to research participants who generously provided their data. Risk minimization includes avoiding stigmatizing language when describing participants or the populations with which they identify, their phenotypes, or their genetic risks. It also includes carefully and clearly articulating limitations and caveats when reporting results and discussing how the results should and should not be interpreted or generalized.</p>
<p>Results generated from HBCD data may be used to guide policy (e.g., for social services, education, or public health interventions). Researchers should be aware of policy implications and controversies related to their research. Some approaches for ethically conducting and reporting research using genetic data are discussed in <a href="https://doi.org/10.1002/hast.1477">Meyer et al. (2023)</a>, <i>Wrestling with Social and Behavioral Genomics: Risks, Potential Benefits, and Ethical Responsibility</i> (<b>The Hastings Center Report</b>).</p>
<p>Researchers cannot control how others, including members of the public and policy makers, interpret scientific results we publish. However, we can take steps to minimize the likelihood our results will be misinterpreted or overinterpreted. In addition to clearly denoting limitations and caveats when reporting results, specific approaches for working with genomic data in this context are discussed in <a href="https://doi.org/10.1146/annurev-genom-011224-015733">Martshenko et al. (2025)</a>, <i>Social and Behavioral Genomics: On the Ethics of the Research and Its Downstream Applications</i> (<b>Annual Reviews Genomics and Human Genetics</b>). For examples of brief documents that explain social and behavioral genomics for non-experts, see “FAQs on Human Genomics Studies” at <a href="https://www.thehastingscenter.org/genomics-research-index/">https://www.thehastingscenter.org/genomics-research-index/</a>.</p> 
</div> -->


<!-- ## Data Exclusions

A total of 22 samples were excluded from data release (i.e., are not contained in the public release files) due to poor genotyping quality (i.e., SNP Missingness >10%), unexpected unrelatedness with no confirmed use of reproductive technology, unexpected relatedness (i.e., identical samples across adults), and sex check mismatch. -->