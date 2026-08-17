# Illumina Global Diversity GWAS Array 

{{ readme_summary(instruments.illumina) }}
{{ alert_warning(instruments.illumina) }}
{{ data_warning(instruments.illumina) }}
{{ issues_banner() }}

---

<!-- ## Instrument Details -->
{{ instrument_description(instruments.illumina) }}

<!-- ## Release Data -->
{{ suppx(instruments.illumina, "1") }}

---

{{ references(instruments.illumina) }}










<!-- 


- **`batch.info`**: Plain-text file mapping participants to genotyping batches.
- **`hbcd.bed`**: [PLINK 1.9 `.bed` format](https://www.cog-genomics.org/plink/1.9/formats#bed) — Binary genotype file (not UCSC BED).
- **`hbcd.bim`**: [PLINK 1.9 `.bim` format](https://www.cog-genomics.org/plink/1.9/formats#bim) — Variant information (chromosome, rsID, position, alleles).
- **`hbcd.fam`**: [PLINK 1.9 `.fam` format](https://www.cog-genomics.org/plink/1.9/formats#fam) — Participant information. -->





<!--
### Cryptic Relatedness
<img src="https://raw.githubusercontent.com/nbdc-datahub/hbcd-docs/main/docs/resources/biospec/family-clusters.png" alt="ADD ALT TEXT" width="500" height="auto" class="center"> -->

<!-- ### Genetic Ancestry-Based Clustering
<div style="text-align: center;">
  <img src="../images/pca.png" style="max-width: 70%; height:auto; display:block; margin:0 auto;">
</div>

- **`pcrelate_relatedness.grm.bin`**: PC-Relate adjusted genetic relatedness matrix.
- **`pcrelate_relatedness.grm.N.bin`**: PC-Relate pairwise common SNP count.
- **`pcrelate_relatedness.grm.id`**: PC-Relate subject IDs, corresponding to the matrix column and row order.
- **`pcrelate_relatedness.tsv`**:
- **`family_clusters.txt`**: -->