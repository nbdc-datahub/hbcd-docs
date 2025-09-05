<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION TO BE ADDED FOR R2.0</i></p>

# Illumina Global Diversity GWAS Array
     
**Acronym:** GDA GWAS           
**Table Name**: `add` (maternal child saliva)         
**Construct:** Genomics

<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
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
<p>Any removal of data during QC will be described.</p> 
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
<td style="word-wrap: break-word; white-space: normal;">V01, V02, V03, V04, V05, V06, These samples are assayed from one sample but it may come from any session based on DNA Yields.</td></tr>
<tr><td><b>Quality Control Procedures</b></td>
<td style="word-wrap: break-word; white-space: normal;">
<ol>
  <li>Check that sampled ID matches from Sampled File and Lasso database</li>
  <li>Check that sample specific barcode matches between Sampled file and Lasso Database.</li>
  <li>Check that genomic sex matches with sex at birth.</li>
  <li>Check that genetic relatedness of each sample matches the anticipated based on Lasso data (i.e., that IBD is ~.50 between the birth parent and child as well as siblings; evaluate potential twins)</li>
  <li>Use FHET estimates to check for plate contamination.</li>
</ol>
</td></tr>      
</tbody>
</table>

## Instrument Details

Additional description will be added. These data contain a `.bed`, `.bim`, and `.fam` file which include genomic data. There is also a `batch.info` file which details sample batching for genotyping. A README file describes these data.

**Genome Build**: hg19    
**Number of variants**: ~XXX    
**Number of Individuals**: X,XXX

<div id="hbcd-mod" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa fa-gear"></i></span>
  <span class="text-with-link">
  <span class="text">HBCD Modification Details</span>
  <a class="anchor-link" href="#hbcd-mod" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>No modifications. It is possible that samples whose identity cannot be resolved will be removed during QC.</p> 
</div>

## References

<div class="references"> 
<p>Committee on the Use of Race, Ethnicity, and Ancestry as Population Descriptors in Genomics Research, Board on Health Sciences Policy, Committee on Population, Health and Medicine Division, Division of Behavioral and Social Sciences and Education, & National Academies of Sciences, Engineering, and Medicine. (2023). Using population descriptors in genetics and genomics research. National Academies Press. <a href="https://doi.org/10.17226/26902">https://doi.org/10.17226/26902</a></p>  
</div>

<br>

