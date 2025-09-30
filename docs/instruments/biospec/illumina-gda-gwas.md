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
<p><b>Balanced Research Practices</b><br>
Researchers must adhere to ethical guidelines and ensure that genetic data are analyzed and interpreted responsibly. Research should aim to advance scientific understanding and avoid misinterpretation or misuse of genetic findings. Evidence of users engaging in stigmatizing research will result in termination of data access.</p>
<p><b>Consideration of Population Descriptors</b><br>
The use of population descriptors in genetic research can often be varied and inconsistent. We encourage users to review the <a href="https://doi.org/10.17226/26902">NASEM report</a> for consideration of appropriate population descriptors. Self-reported race and ethnicity may reflect social and environmental experiences that do not directly correspond to genetic variation.</p>
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

<div id="concat" class="static-banner" style="background-color: #dcd8fb; border-left: 5px solid #dcd8fb;">
  <span class="emoji"><i class="fa fa-folder-tree"></i></span>
  <span class="text-with-link">
  <span class="text">Concatenated Data (<code>genetics/</code>)</span>
  <a class="anchor-link" href="#concat" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
</div>
<div class="notification-static-content" style="border-left: 5px solid #dcd8fb;">
<p>The GDA GWAS dataset is provided as <a href="../../../datacuration/file-based-data/#concatenated-data">concatenated data</a> under <code>genetics/</code> (<i>see the <a href="../../../datacuration/overview" target="_blank">Data Structure Overview</a> to learn more about BIDS and data types</i>):</p>
<pre class="folder-tree">
hbcd/
|__ concatenated/ 
    |__ genetics/
        |__ .bed 
        |__ .bim
        |__ .fam
        |__ batch.info
        |__ README
</pre>
<p>The dataset includes three interlinked PLINK files (<code>.bed</code>, <code>.bim</code>, and <code>.fam</code>) aligned to the <strong>hg19 genome build</strong>, along with a <code>batch.info</code> file specifying genotyping batches and a <code>README</code> describing initial QC procedures:</p>
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
  <td style="word-wrap: break-word; white-space: normal;"><a href="https://www.cog-genomics.org/plink/1.9/formats#bed">PLINK 1.9 .bed</a>: Binary genotype file (distinct from UCSC Genome Browser BED files).</td>
</tr>
<tr>
  <td><code>.bim</code></td>
  <td style="word-wrap: break-word; white-space: normal;"><a href="https://www.cog-genomics.org/plink/1.9/formats#bim">PLINK 1.9 .bim</a>: Variant information (e.g., chromosome, rsID, position, alleles).</td>
</tr>
<tr>
  <td><code>.fam</code></td>
  <td style="word-wrap: break-word; white-space: normal;"><a href="https://www.cog-genomics.org/plink/1.9/formats#fam">PLINK 1.9 .fam</a>: Participant information.</td>
</tr>
<tr>
  <td><code>batch.info</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Text file indicating the genotyping batch for each participant.</td>
</tr>
<tr>
  <td><code>README</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Documents QC procedures to ensure sample matches (ID concordance, sex checks, etc.).</td>
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
</div>

<br>
