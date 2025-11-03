<p style="font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION TO BE ADDED FOR R2.0</i></p>

# Illumina Global Diversity GWAS Array 

Genomic data generated from the Illumina Global Diversity Array (*GDA GWAS*) is provided for both the birth parent and child. Samples are assayed from one sample, but may come from any visit (V01-V06) based on DNA yields.

## Release Data

<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Responsible Use Warning</span>
  <a class="anchor-link" href="#alert" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p><b>Anonymity</b><br>
Data users are prohibited from using HBCD data, including genomic data, to identify participants or their relatives.  You accessed these data under a Data Use Certification (DUC) agreement in which you and your institution agreed that you would not attempt to establish the individual identity of any study participants or their relatives.  You also agreed to adhere to a minimum cell threshold of 10 in any public reporting of data (i.e., publications, posters, or other presentations).  Protecting participants’ anonymity demonstrates respect for them and minimizes their research-related risks.</p>
<p><b>Population Descriptors</b><br>
The use of population descriptors in genetic research has been varied and inconsistent. The National Academies of Science, Engineering, and Medicine (NASEM) published a report on the use of population descriptors, such as ancestry, race, ethnicity, and geography, in genomics (<a href="https://doi.org/10.17226/26902">https://doi.org/10.17226/26902</a>). We encourage data users working with HBCD genomics data to consult the NASEM report to understand the past and current use of population descriptors in genomics research as well as current best practice recommendations when analyzing or reporting on HBCD genomic data. Race and ethnicity represent social constructs that are conceptually distinct from ancestry inferred from genetic data. Description of race and ethnicity variables in HBCD may be found in <a href="../../demo/basicdemo/#race-ethnicity-variables" target="_blank">Basic Demographics</a>.</p>
<p><b>Ethical Obligations to Minimize Risks</b><br>
Analysts using HBCD data have ethical obligations to minimize risks, including psychological, social, and economic risks, to research participants who generously provided their data. Risk minimization includes avoiding stigmatizing language when describing participants or the populations with which they identify, their phenotypes, or their genetic risks. It also includes carefully and clearly articulating limitations and caveats when reporting results and discussing how the results should and should not be interpreted or generalized.</p>
<p>Results generated from HBCD data may be used to guide policy (e.g., for social services, education, or public health interventions). Researchers should be aware of policy implications and controversies related to their research. Some approaches for ethically conducting and reporting research using genetic data are discussed in <a href="https://doi.org/10.1002/hast.1477">Meyer et al. (2023)</a>, <i>Wrestling with Social and Behavioral Genomics: Risks, Potential Benefits, and Ethical Responsibility</i> (<b>The Hastings Center Report</b>).</p>
<p>Researchers cannot control how others, including members of the public and policy makers, interpret scientific results we publish. However, we can take steps to minimize the likelihood our results will be misinterpreted or overinterpreted. In addition to clearly denoting limitations and caveats when reporting results, specific approaches for working with genomic data in this context are discussed in <a href="https://doi.org/10.1146/annurev-genom-011224-015733">Martshenko et al (2025)</a>, <i>Social and Behavioral Genomics: On the Ethics of the Research and Its Downstream Applications</i> (<b>Annual Reviews Genomics and Human Genetics</b>). For examples of brief documents that explain social and behavioral genomics for non-experts, see “FAQs on Human Genomics Studies” at <a href="https://www.thehastingscenter.org/genomics-research-index/">https://www.thehastingscenter.org/genomics-research-index/</a>.</p> 
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
<p>Any removal of data during QC will be described in the README file accompanying the data.</p> 
</div>

<div id="concat" class="static-banner" style="background-color: #dcd8fb; border-left: 5px solid #b5aef2;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
    <span class="text">Concatenated Data (<code>genetics/</code>)</span>
    <a class="anchor-link" href="#concat" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
</div>
<div class="notification-static-content" style="border-left: 5px solid #b5aef2;">
  <p>The GDA GWAS dataset is provided as <a href="../../../datacuration/file-based-data/#concatenated-data">concatenated data</a> under 
    <code>genetics/</code>. <i>See the <a href="../../../datacuration/overview" target="_blank">Data Structure Overview</a> to learn more about BIDS and data types.</i></p>
  <pre class="folder-tree">
hbcd/
└── concatenated/
    └── genetics/
        ├── .bed
        ├── .bim
        ├── .fam
        ├── batch.info
        └── README
  </pre>
  <p>The dataset includes <strong>three interlinked PLINK files</strong> (<code>.bed</code>, <code>.bim</code>, <code>.fam</code>) aligned to the <strong>hg19 genome build</strong>, plus supporting documentation and batch metadata:</p>
  <table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <thead>
      <tr>
        <th>File</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>.bed</code></td>
        <td><a href="https://www.cog-genomics.org/plink/1.9/formats#bed">PLINK 1.9 <code>.bed</code> format</a> — Binary genotype file (not UCSC BED).</td>
      </tr>
      <tr>
        <td><code>.bim</code></td>
        <td><a href="https://www.cog-genomics.org/plink/1.9/formats#bim">PLINK 1.9 <code>.bim</code> format</a> — Variant information (chromosome, rsID, position, alleles).</td>
      </tr>
      <tr>
        <td><code>.fam</code></td>
        <td><a href="https://www.cog-genomics.org/plink/1.9/formats#fam">PLINK 1.9 <code>.fam</code> format</a> — Participant information.</td>
      </tr>
      <tr>
        <td><code>batch.info</code></td>
        <td>Plain-text file mapping participants to genotyping batches.</td>
      </tr>
      <tr>
        <td><code>README</code></td>
        <td>Documentation of QC procedures to ensure sample matches (e.g., ID concordance, sex checks).</td>
      </tr>
    </tbody>
  </table>
</div>

## Details

Add more info?

## Quality Control

Quality control procedures involved the following:

<ul>
  <li>Check that sampled ID matches from Sampled File and Lasso Database.</li>
  <li>Check that sample specific barcode matches between Sampled file and Lasso Database.</li>
  <li>Check that genomic sex matches with sex at birth.</li>
  <li>Check that genetic relatedness of each sample matches the anticipated based on Lasso data (i.e., that IBD is ~.50 between the birth parent and child as well as siblings; evaluate potential twins).</li>
  <li>Use FHET estimates to check for plate contamination.</li>
</ul>

## References
<div class="references"> 
<p>Committee on the Use of Race, Ethnicity, and Ancestry as Population Descriptors in Genomics Research, Board on Health Sciences Policy, Committee on Population, Health and Medicine Division, Division of Behavioral and Social Sciences and Education, & National Academies of Sciences, Engineering, and Medicine. (2023). Using population descriptors in genetics and genomics research. National Academies Press. <a href="https://doi.org/10.17226/26902">https://doi.org/10.17226/26902</a></p>  
<p>Martschenko, D. O., Lee, S. S.-J., Meyer, M. N., & Parens, E. (2025). Social and behavioral genomics: On the ethics of the research and its downstream applications. <i>Annual Review of Genomics and Human Genetics</i>, 26(1), 425–447. <a href="https://doi.org/10.1146/annurev-genom-011224-015733">https://doi.org/10.1146/annurev-genom-011224-015733</a></p>
<p>Meyer, M. N., Appelbaum, P. S., Benjamin, D. J., Callier, S. L., Comfort, N., Conley, D., Freese, J., Garrison, N. A., Hammonds, E. M., Harden, K. P., Lee, S. S.-J., Martin, A. R., Martschenko, D. O., Neale, B. M., Palmer, R. H. C., Tabery, J., Turkheimer, E., Turley, P., & Parens, E. (2023). Wrestling with social and behavioral genomics: Risks, potential benefits, and ethical responsibility. <i>The Hastings Center Report</i>, 53 Suppl 1, S2–S49. <a href="https://doi.org/10.1002/hast.1477">https://doi.org/10.1002/hast.1477</a></p>
</div>


  