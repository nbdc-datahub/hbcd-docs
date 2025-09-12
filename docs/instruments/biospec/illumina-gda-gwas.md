<p style="font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION TO BE ADDED FOR R2.0</i></p>

# Illumina Global Diversity GWAS Array 

Genomic data generated from the Illumina Global Diversity Array (*GDA GWAS*) are provided as <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> data under the `concatenated/` BIDS folder (see <a href="../../../datacuration/overview" target="_blank">Data Structure Overview</a> for details):

<p>
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
</p>

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

## Administration & Quality Control

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr><td><b>Child Specific</b></td>
<td>No</td></tr>
<tr><td><b>Respondent</b></td>
<td>Data will be included from the birth parent and child in the same files.</td></tr>
<tr><td><b>Administration</b></td>
<td style="word-wrap: break-word; white-space: normal;">HBCD Study staff in person, Self-administered remote</td></tr>
<tr><td><b>Visits</b></td>
<td style="word-wrap: break-word; white-space: normal;">Samples are assayed from one sample, but may come from any session (V01-V06) based on DNA Yields.</td></tr>
<tr><td><b>Quality Control Procedures</b></td>
<td style="word-wrap: break-word; white-space: normal;">
<ul>
  <li>Check that sampled ID matches from Sampled File and Lasso Database.</li>
  <li>Check that sample specific barcode matches between Sampled file and Lasso Database.</li>
  <li>Check that genomic sex matches with sex at birth.</li>
  <li>Check that genetic relatedness of each sample matches the anticipated based on Lasso data (i.e., that IBD is ~.50 between the birth parent and child as well as siblings; evaluate potential twins).</li>
  <li>Use FHET estimates to check for plate contamination.</li>
</ul>
</td></tr>      
</tbody>
</table>

## Instrument Details

Genomic data generated from the Illumina Global Diversity Array are provided as 3 interlinked `.bed`, `.bim`, and `.fam` plink files on the hg19 genome build. A `batch.info` file contains which batch each participant was run on. The README file contains details of initial QC to ensure sample matches (e.g., ID checks, sex checks, etc.). 

#### File Type Details

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
<td style="word-wrap: break-word; white-space: normal;"><a href="https://www.cog-genomics.org/plink/1.9/formats#bed">PLINK 1.9 .bed</a>: Binary genotype file table (note: these are distinct from UCSD genome browser BED files).</td>
</tr>
<tr>
<td><code>.bim</code></td>
<td style="word-wrap: break-word; white-space: normal;"><a href="https://www.cog-genomics.org/plink/1.9/formats#bim">PLINK 1.9 .bim</a>: Contains additional information regarding genotypes - e.g., chromosome, identifier (e.g., rs number), position, allele 1 and 2.</td>
</tr>
<tr>
<td><code>.fam</code></td>
<td style="word-wrap: break-word; white-space: normal;"><a href="https://www.cog-genomics.org/plink/1.9/formats#fam">PLINK 1.9 .fam</a>: Text file containing the participant information.</td>
</tr>
<tr>
<td><code>batch.info</code></td>
<td style="word-wrap: break-word; white-space: normal;">Simple text file listing what batch of genotype each subject was one.</td>
</tr>
<tr>
<td><code>README</code></td>
<td style="word-wrap: break-word; white-space: normal;">Describes the sample QC steps that were taken.</td>
</tr>
</tbody>
</table>

## References

<div class="references"> 
<p>Committee on the Use of Race, Ethnicity, and Ancestry as Population Descriptors in Genomics Research, Board on Health Sciences Policy, Committee on Population, Health and Medicine Division, Division of Behavioral and Social Sciences and Education, & National Academies of Sciences, Engineering, and Medicine. (2023). Using population descriptors in genetics and genomics research. National Academies Press. <a href="https://doi.org/10.17226/26902">https://doi.org/10.17226/26902</a></p>  
</div>

<br>
